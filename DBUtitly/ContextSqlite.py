from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Integer, Column, String, func, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from enum import StrEnum

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
    DRIVER_NAME_SQLITE = 'sqlite',

    
url_object = URL.create(
    "postgresql+pg8000",
    username="dbuser",
    password="kx@jj5/g",  # plain (unescaped) text
    host="pghost10",
    database="appdb",
)


class ContextSqlite:
    """"""
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
    
    def __enter__(self):
        """
        Open the database connection
        """
        print('__enter__')
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        #return self.session,self.base
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close the connection
        """
        print('Closing')
        self.session.close()
        if exc_val:
            raise
    def commit(self):
        '''
            commit
        '''
        print('commit')
        self.session.commit()
    '''
    def CreateSchema(self):
        #建立資料表以及刪除資料表
        #Define Class Data
        self.base.metadata.create_all(self.engine)
    
    def DropSchema(self):
        #建立資料表以及刪除資料表
        #Define Class Data
        self.base.metadata.drop_all(self.engine)
    '''

