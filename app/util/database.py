from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

pymysql.install_as_MySQLdb()

engine = create_engine('mysql://root:root@localhost/torando_db1',
                       encoding='utf-8', echo=True)
Session = sessionmaker(bind=engine)
sess = Session()
db = declarative_base(bind=engine)