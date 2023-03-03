from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


#testing change the database name for prod

SERVER=os.getenv('SERVER')
DATABASE= os.getenv('DATABASE')
connection_string = "DRIVER={SQL Server};SERVER=%s;DATABASE=%s;Trusted_Connection=yes" % (
            SERVER, DATABASE)
SQLALCHEMY_DATABASE_URL = URL.create(
            "mssql+pyodbc", query={"odbc_connect": connection_string})
            

engine = create_engine(SQLALCHEMY_DATABASE_URL,)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
