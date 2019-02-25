from . import web
from flask_login import login_required, current_user
from app.model.gift import Gift
from app.model.base import db
from flask import current_app, flash


__author__ = '彤'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    """赠送此书"""
    if current_user.can_save_to_list(isbn):
        try:
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']

            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            # 数据库回滚
            db.session.rollback()
            raise e
    else:
        flash('这本书已添加至你的赠送清单或已存在与你的心愿清单，请不要重复添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
