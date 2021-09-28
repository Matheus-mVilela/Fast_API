from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine



engine = create_engine('sqlite:///../db_test.db', echo = True) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine )

Base = declarative_base()
