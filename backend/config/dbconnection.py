from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")



dataBaseUrl = "mysql+pymysql://root:1234567@127.0.0.1:3306/userManagement"

# print(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/userManagement", "======")

# dataBaseUrl = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/userManagement"

engine = create_engine(dataBaseUrl, pool_size=20, max_overflow=0)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

base = declarative_base()