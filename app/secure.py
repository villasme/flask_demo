DEBUG = False
# SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:123456@10.165.0.106:3306/fisher'
SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://root:example@www.liujiantong.cn:3306/fisher'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# session 使用  否则报错
SECRET_KEY = 'liujiantong'
SESSION_TYPE = 'filesystem'