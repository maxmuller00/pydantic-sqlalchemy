from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db" #connect to database

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} #SQLAlchemy only allows one thread to communicate, we turn this off so fastapi can use > 1 thread
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #database session

Base = declarative_base() #parent clase for all models/classes

