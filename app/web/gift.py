from . import web
from flask_login import login_required, current_user
from app.model.gift import Gift
from app.model.base import db
from flask import current_app


__author__ = '彤'


@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'My Gifts'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    """赠送此书"""
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']

    db.session.add(gift)
    db.session.commit()
    pass


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
