
from enum import StrEnum


'''
url_object = URL.create(
    "postgresql+pg8000",
    username="dbuser",
    password="kx@jj5/g",  # plain (unescaped) text
    host="pghost10",
    database="appdb",
)
'''

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
    DRIVER_NAME_SQLITE = 'sqlite:///'





