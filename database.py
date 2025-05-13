from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("mysql+mysqlconnector://root@localhost/DARBAS")
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
