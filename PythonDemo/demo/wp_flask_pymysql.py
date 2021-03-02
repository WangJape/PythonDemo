# -*- coding: utf-8 -*-
from urllib.parse import quote, unquote

from flask import Flask, render_template, request, make_response, session
import pymysql

app = Flask(__name__)

# 连接mysql字符串
db = pymysql.connect("123.57.140.84", "root", "weipeng.?3656LL$#>", "course_selection_sys")
# 新建游标
cursor = db.cursor()
# 设置SECRET_KEY
app.config['SECRET_KEY'] = '123456'


# 验证登录
def do_the_login():
    username = request.form['username']
    password = request.form['password']
    cursor.execute("SELECT us_id FROM `t_user` WHERE username= '%s' and password='%s'" % (username, password))
    user_id = None
    for data in cursor.fetchall():
        user_id = data[0]
    if user_id:
        session['userId'] = user_id
        session['userName'] = username
        return {'code': 200, 'msg': "登录成功"}
    return {'code': 500, 'msg': "登录失败"}


# 登录页面
def show_the_login_form():
    return render_template('login.html')


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()


@app.route('/findCheckedByPage')
def findCheckedByPage():
    user_id = session.get('userId')
    # 获取分页参数
    page = int(request.args.get("page"))
    limit = int(request.args.get("limit"))
    begin_index = (page - 1) * limit
    # 执行sql语句
    cursor.execute("SELECT count(1) FROM t_us_co_da ucd where ucd.us_id=%s" % user_id)
    total = cursor.fetchone()
    cursor.execute(
        "SELECT co.co_id,co.name,da.content,IF(ucd.co_id>0,'已选','未选') as state  FROM t_course co LEFT JOIN t_date da on co.da_id=da.da_id LEFT JOIN t_us_co_da ucd on ucd.co_id=co.co_id where ucd.us_id=%s LIMIT %s , %s" %
        (user_id, begin_index, limit))
    data = []
    for item in cursor.fetchall():
        data.append({'id': item[0], 'name': item[1], 'content': item[2], 'state': item[3]})
    return {'code': 200, 'total': total, 'data': data}


@app.route('/findCourseByPage')
def findCourseByPage():
    user_id = session.get('userId')
    # 获取分页参数
    page = int(request.args.get("page"))
    limit = int(request.args.get("limit"))
    begin_index = (page - 1) * limit
    # 执行sql语句
    cursor.execute("SELECT count(1) FROM t_course co LEFT JOIN t_date da on co.da_id=da.da_id")
    total = cursor.fetchone()
    cursor.execute(
        "SELECT co.co_id,co.name,da.content,IF(ucd.co_id>0,'已选','未选') as state  FROM t_course co LEFT JOIN t_date da on co.da_id=da.da_id LEFT JOIN t_us_co_da ucd on ucd.co_id=co.co_id and ucd.us_id=%s LIMIT %s , %s" %
        (user_id, begin_index, limit))
    data = []
    for item in cursor.fetchall():
        data.append({'id': item[0], 'name': item[1], 'content': item[2], 'state': item[3]})
    return {'code': 200, 'total': total, 'data': data}


# 选课
@app.route('/course_on', methods=['POST'])
def course_on():
    user_id = session.get('userId')
    co_id = request.form['co_id']
    cursor.execute("SELECT da_id FROM t_course WHERE co_id=%s" % co_id)
    da_id = cursor.fetchone()[0]

    try:
        cursor.execute("INSERT INTO t_us_co_da VALUES(%s,%s,%s)" % (user_id, co_id, da_id))
        db.commit()
        return {'code': 200, 'msg': '选课成功'}
    except Exception as e:
        return {'code': 500, 'msg': '时间冲突,选课失败'}


# 退课
@app.route('/course_off', methods=['POST'])
def course_off():
    user_id = session.get('userId')
    co_id = request.form['co_id']
    cursor.execute("DELETE FROM t_us_co_da WHERE us_id=%s and co_id=%s" % (user_id, co_id))
    db.commit()
    return {'code': 200, 'msg': '退课成功'}


@app.route('/index')
def index(username=None):
    username = session.get('userName')
    return render_template('index.html', username=username)


@app.route('/course_table')
def course_table():
    return render_template('course_table.html')


@app.route('/checked_table')
def checked_table():
    return render_template('checked_table.html')


if __name__ == '__main__':
    app.run()
