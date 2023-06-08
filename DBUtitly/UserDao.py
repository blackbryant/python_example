
from ContextSqlite import ContextSqlite
from dataclasses import dataclass
from sqlalchemy import Integer, Column, String, func, UniqueConstraint
from sqlalchemy.orm import declarative_base
Base = declarative_base()

@dataclass
class Person(Base):
    __tablename__= 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class UserDao:
    def __init__(self,url):
        """Constructor"""
        self.url = url
    
    def AddUser(self,p:Person)->int:
        with ContextSqlite(self.url) as conn:
            iid=12
            conn.session.add(p)
            conn.commit()

    def CreateTable(self)->int:
        with ContextSqlite(self.url) as conn:
            Person()
            Base.metadata.create_all(conn.engine)

if __name__ == '__main__':
    url = r'E:\python範例\python_example\DBUtitly\test.db'
    userDao = UserDao(url)
    userDao.CreateTable()
    p = Person(name="John Doe", age=10, id=13)
    userDao.AddUser(p)

