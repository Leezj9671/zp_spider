PROXY_API_URL = 'http://123.207.89.91:5000/get'

SQL_ADDR = '127.0.0.1'
SQL_PORT = 3306
SQL_USER = 'root'
SQL_PWD = 'toor'
SQL_DATABASE = 'employ'
SQL_TABLE = 'employ_info_test'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(SQL_USER, SQL_PWD, SQL_ADDR, SQL_PORT, SQL_DATABASE)

SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True