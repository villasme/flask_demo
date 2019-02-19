from wtforms import Form, StringField, IntegerField, PasswordField
from wtforms.validators import Length, NumberRange, DataRequired, Email, ValidationError
from app.model.user import User


class RegisterForm(Form):
    # 字符串类型 校验规则 不为空 长度 8-64位
    email = StringField(validators=[DataRequired(), Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6,32)])
    nickname = StringField(validators=[DataRequired(), Length(2, 10, message='昵称至少需要两个字符， 最多10个字符')])

    # 自定义校验
    def validate_email(self, field):
        # filter_by 可以写一组查询条件
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('电子邮件已被注册')
    
    def validate_nickname(self, field):
        # filter_by 可以写一组查询条件
        if User.query.filter_by(nickname=field.data).first():
            raise ValidationError('该昵称已被注册')

class LoginForm(Form):
    email = StringField(validators=[DataRequired(),Length(8, 64), Email(message='电子邮箱不符合规范')])
    password = PasswordField(validators=[DataRequired(message='密码不可以为空，请输入你的密码'), Length(6, 32)])