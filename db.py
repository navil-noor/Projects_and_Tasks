import os
import time  # <--- Add this
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.exc import OperationalError # <--- Add this

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///database.db")
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    # We try 5 times to connect, waiting 2 seconds between each try
    retries = 5
    while retries > 0:
        try:
            SQLModel.metadata.create_all(engine)
            print("✅ Database connected and tables created!")
            return # Exit the function if successful
        except OperationalError:
            retries -= 1
            print(f"⏳ Database is starting up... retries left: {retries}")
            time.sleep(2)
    
    # If we get here, it really failed
    raise Exception("Could not connect to the database after several attempts.")

def get_session():
    with Session(engine) as session:
        yield session