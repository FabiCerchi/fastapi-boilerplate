import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import app
from app.db.database import Base, get_db

# Configuración global para la base de datos de pruebas
DB_PATH = os.path.join(os.path.dirname(__file__), 'test.db')
SQL_ALCHEMY_DATABASE_URL = f'sqlite:///{DB_PATH}'
ENGINE_TEST = create_engine(SQL_ALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE_TEST)

# Sobrescribir la dependencia de la base de datos
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)

# Usuario de prueba
TEST_USER = {
    "email": "auth@prueba.com",
    "username": "authPrueba",
    "password": "authPassword",
    "address": "auth Address"
}

@pytest.fixture(scope="session", autouse=True)
def cleanup():
    """Elimina la base de datos de pruebas al final de todas las pruebas"""
    yield
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    assert not os.path.exists(DB_PATH)


@pytest.fixture(scope="function", autouse=True)
def setup():
    """Crea y limpia las tablas de la base de datos antes y después de cada prueba"""
    Base.metadata.create_all(bind=ENGINE_TEST)
    yield
    Base.metadata.drop_all(bind=ENGINE_TEST)


@pytest.fixture
def test_client():
    """Devuelve un cliente de pruebas para FastAPI"""
    return client


@pytest.fixture
def auth_token(test_client):
    """Devuelve un token de autenticación válido"""
    test_client.post("/users/", json=TEST_USER)
    response = test_client.post(
        "/auth/login", data={"username": TEST_USER['username'], "password": TEST_USER['password']}
    )
    return response.json()['access_token']
