from . import web

__author__ = 'tong'

@web.route('/')
def index():
    return 'hello'

@web.route('/personal')
def personal_center():
    pass