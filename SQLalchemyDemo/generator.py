import os

# pip install sqlacodegen
# pip install mysqlclient
ret = os.popen(
    "sqlacodegen --tables t_user1 --noviews --noconstraints --noindexes mysql://root:123456@192.168.0.105:3306/jape"
)
print(ret.read())
