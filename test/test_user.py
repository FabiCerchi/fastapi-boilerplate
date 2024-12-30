from fastapi.testclient import TestClient
import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from main import app
from app.db.database import Base, get_db

# Create a test database
db_path = os.path.join(os.path.dirname(__file__), 'test.db')
SQL_ALCHEMY_DATABASE_URL = f"sqlite:///{db_path}"
engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
