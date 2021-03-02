from flask import Blueprint
from flask_demo.dao.models import User
from flask_demo.dao import db

bl_user = Blueprint('bl_user', __name__)


@bl_user.route('/getByName/<name>')
def get_by_name(name):
    # 创建一个新用户对象
    user = User.query.filter_by(name=name).first()
    return user.uuid
