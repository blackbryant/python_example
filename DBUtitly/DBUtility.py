from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Integer, Column, String, func, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from enum import StrEnum
from contextlib import contextmanager

class Directions(StrEnum):
    DRIVER_NAME_POSTGRESQL = 'postgresql',    
    DRIVER_NAME_POSTGRESQL_PSY = 'postgresql+psycopg2',    
    DRIVER_NAME_POSTGRESQL_PG8000 = 'postgresql+pg8000',    
    DRIVER_NAME_MYSQL = 'mysql',    
    DRIVER_NAME_MYSQL_DB = 'mysql+mysqldb',    
    DRIVER_NAME_MYSQL_PY = 'mysql+pymysql',    
    DRIVER_NAME_MSSQL_ODBC = 'mssql+pyodbc',
    DRIVER_NAME_MSSQL_PY = 'mssql+pymssql',
    DRIVER_NAME_ORACLE = 'oracle',
    DRIVER_NAME_ORACLE_CX = 'oracle+cx_oracle',
    DRIVER_NAME_SQLITE = 'sqlite:///',

'''
url_object = URL.create(
    "postgresql+pg8000",
    username="dbuser",
    password="kx@jj5/g",  # plain (unescaped) text
    host="pghost10",
    database="appdb",
)
'''

class SessionUtil:


    def __init__(self, Directions,Host,Username, Password,Database ):
        """Constructor"""
        print('__init__')
        url_object = URL.create(
                    Directions,
                    username=Username,
                    password=Password,  # plain (unescaped) text
                    host=Host,
                    database=Database,
                )
        #connection_str = ("sqlite:///%s" %URL)
        #connection_str = connection_format.format(db_user,db_host,db_name)
        engine = create_engine(url_object)
        self.engine = engine

    @contextmanager
    def Session(self, Directions,Host,Username, Password,Database ):
        print('__enter__')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()
        yield
        print('Closing')
        self.session.close()
        

    def Commit(self):
        '''
            commit
        '''
        print('commit')
        self.session.commit()

if __name__ == '__main__':
    url = r'sqlite:///E:\python範例\python_example\DBUtitly\test.db'
    util = SessionUtil(Directions=Directions.DRIVER_NAME_SQLITE,Host=r"E:\python範例\python_example\DBUtitly\test.db",Username=None,Password=None,Database=None)
    with util.Session():
         print("AAAAAAAAAA")
         util.Commit()
    