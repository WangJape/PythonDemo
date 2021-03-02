from flask import Flask
from flask_demo.dao import db
from flask_demo.web.login import bl_login
from flask_demo.web.user import bl_user

app = Flask(__name__)
app.config.from_object('config.Dev')
# 注册蓝图
app.register_blueprint(bl_login)
app.register_blueprint(bl_user)
# 初始化数据库
db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'
