class Dev:
    # 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.73.114:3306/jape?charset=utf8'

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True  # 每次请求结束后都会自动提交数据库中的变动.
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_MAX_OVERFLOW = 5
