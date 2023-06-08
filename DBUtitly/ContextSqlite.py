from dataclasses import dataclass
from datetime import datetime
from sqlalchemy import Integer, Column, String, func, UniqueConstraint
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ContextSqlite:
    """"""
    def __init__(self, url):
        """Constructor"""
        print('__init__')
        connection_str = ("sqlite:///%s" %url)
        #connection_str = connection_format.format(db_user,db_host,db_name)
        engine = create_engine(connection_str)
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

