from . import web
from flask import request, jsonify, render_template

@web.route('/test')
def test():
    from app.libs.none_local import n
    print(n.v)
    n.v = 2
    print('-------------------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print(request.v)
    print('-------------------')
    # return ''
    return render_template('test.html', data=n)

@web.route('/user')
def login():
    return jsonify(request.args)