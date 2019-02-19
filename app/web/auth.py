from . import web
from app.model.user import User
from app.model.book import Book
from flask import render_template, request, redirect, url_for, flash
from app.forms.auth import RegisterForm, LoginForm
from app.model.base import db
from flask_login import login_user

@web.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))

    return render_template('auth/register.html', form=form)

@web.route('/login')
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
        else:
            flash('账号不存在或密码错误')
    return render_template('auth/login.html', form=form)

@web.route('/reset/password')
def forget_password_request():
    pass

@web.route('/reset/password/<token>')
def forget_password(token):
    pass