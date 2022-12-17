from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_name}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_username}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


#import psycopg2
#from psycopg2.extras import RealDictCursor
#from datetime import time

# while True:                             #connecting to DB
#     try:
#         conn = psycopg2.connect(host = 'localhost' , database = 'pythonapi' , user = 'postgres' , password = 'nahatasde123' , cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Connection established!")
#         break

#     except Exception as error:
#         print("Connection Failed ",error)
#         time.sleep(3)
