from app.web import web
from flask import request, jsonify, flash, render_template
from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookCollection
import json

@web.route('/book/search')
def search():
    """
        q :普通关键字 isbn
        page
        ?q=金庸&page=1
    """
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        yushu_book = YuShuBook()
        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)
        
        books.fill(yushu_book, q)
        return json.dumps(books,ensure_ascii=False, default=lambda o: o.__dict__)
        # return jsonify(yushu_book.books)
    else:
        # flash('搜索的关键字不符合要求，请重新输入关键字')
        return '搜索的关键字不符合要求，请重新输入关键字'
    # return render_template('search_result.html', books = books)



    # arg = '没有参数'
    # if request.args:
    #     arg = jsonify(request.args)
    # 这里是简化写法
    # return jsonify(request.args) if request.args else '没有参数'
