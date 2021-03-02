from flask import Blueprint

bl_login = Blueprint('bl_login', __name__)


@bl_login.before_request
def bf():
    print('pre')


@bl_login.after_request
def af(rsp):
    print(rsp)
    return rsp


@bl_login.route('/login/')
def get_by_name():
    return "login"
