from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

# 初始化数据库连接:
# echo: 当设置为True时会将orm语句转化为sql语句打印，一般debug的时候可用
# pool_size: 连接池的大小，默认为5个，设置为0时表示连接无限制
# pool_recycle: 设置时间以限制数据库多久没连接自动断开
engine = create_engine('mysql+pymysql://root:123456@192.168.0.105:3306/jape?charset=utf8',
                       echo=True,
                       pool_size=5,
                       pool_recycle=60 * 30)
# 创建DBSession类型:
# session的常见操作方法包括：
# flush：预提交，提交到数据库文件，还未写入数据库文件中,可以在add之后执行db.session.flush()，这样便可在session中get到对象的属性。
# commit：提交了一个事务
# rollback：回滚
# close：关闭
DBSession = sessionmaker(bind=engine)
# 创建session对象:
session = DBSession()


def add():
    # 创建新User对象:
    User()
    new_user = User(uuid='2', name='ws', age=23)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()


def query_page(page_no, page_size):
    offset = (page_no - 1) * page_size
    users = session.query(User).filter_by(name='Jape0').offset(offset).limit(page_size).all()
    for user in users:
        print(user.uuid)


if __name__ == '__main__':
    query_page(1, 100)
    # 关闭session:
    session.close()
