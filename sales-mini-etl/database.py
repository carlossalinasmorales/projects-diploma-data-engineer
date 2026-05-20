from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from etl import DB_PATH

engine = create_engine(f"sqlite:///{DB_PATH}")

def get_session():
    return Session(engine)
