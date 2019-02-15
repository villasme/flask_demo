from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange

class SearchForm(Form):
    "搜索验证"
    q = StringField(validators=[Length(max=30, min=1)])
    page = IntegerField(validators=[NumberRange(min=1, max=99)], default=1)