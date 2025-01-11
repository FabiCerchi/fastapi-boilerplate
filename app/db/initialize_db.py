from .database import get_db
from app.models.user import User
from app.utils.hashing import Hasher
import os

def create_superuser():
    db = next(get_db())
    try:
        existing_user = db.query(User).filter_by(is_superuser=True).first()
        if not existing_user:
            superuser = User(
                username=os.getenv("SUPERUSER_USERNAME"),
                email=os.getenv("SUPERUSER_EMAIL"),
                password=Hasher.get_password_hash(os.getenv("SUPERUSER_PASS")),  # Hashea la contraseña
                is_superuser=True
            )
            db.add(superuser)
            db.commit()
            print("Superusuario creado exitosamente.")
    except Exception as e:
        print(f"Error al crear superusuario: {e}")
        db.rollback()