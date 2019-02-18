from . import web
from app.model.user import User
from app.model.book import Book
from flask import render_template, request
from app.forms.auth import RegisterForm
from app.model.base import db

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()

    return render_template('auth/register.html', form=form)

@web.route('/login')
def login():
    pass

@web.route('/reset/password')
def forget_password_request():
    pass

@web.route('/reset/password/<token>')
def forget_password(token):
    pass