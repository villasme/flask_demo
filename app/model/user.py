from app.model.base import db, Base
from app import login_manager

from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.model.gift import Gift
from app.model.wish import Wish

class User(UserMixin, Base):
    # __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    # nullable 可空
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    email = Column(String(50), unique=True, nullable=False)
    _password= Column('password', String(128), nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0) # 鱼豆数量 （积分）
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    # 让一个方法编程属性 修饰器
    # getter 方法
    @property
    def password(self):
        return self._password

    # password 设置时 先调用 这个
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
    
    def check_password(self, raw):
        return check_password_hash(self._password, raw)

    # login_user 默认执行此函数  实例对象覆盖
    # def get_id(self):
    #     return self.id

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不允许用户同时赠送多本相同的图书
        # 一个用户不可能同时成为赠送者和索要者

        # 既不在赠送书单中， 也不再心愿清单中才能添加 
        gifting = Gift.query.filter_by(id=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(id=self.id, isbn=isbn, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))