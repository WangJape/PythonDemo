from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.dialects.mysql import VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# 定义User对象:
class User(Base):
    __tablename__ = 't_user'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


class User1(Base):
    __tablename__ = 't_user1'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(20))
    sex = Column(VARCHAR(1))
    qq = Column(String(10))
    birthday = Column(Date)
