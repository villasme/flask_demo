from flask import Flask
from app.model.base import db
from flask_login import LoginManager

login_manager = LoginManager()

def createApp():
    "创建app"
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)

    db.init_app(app)
    # db.create_all(app=app)
    login_manager.init_app(app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录'

    with app.app_context():
        db.create_all()
    return app

def register_blueprint(app):
    """
    注册蓝图
    """
    from app.web import web
    app.register_blueprint(web)
