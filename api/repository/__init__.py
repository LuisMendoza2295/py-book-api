from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)
engine = create_engine(os.getenv('DATABASE_URL'), echo=True)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = scoped_session(SessionLocal)
