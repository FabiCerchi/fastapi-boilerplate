# FastAPI Boilerplate

Este proyecto es una plantilla base para aplicaciones construidas con FastAPI, diseñada para proporcionar una estructura clara y modular que facilita la escalabilidad y el mantenimiento.

## Características

- **FastAPI**: Framework rápido y eficiente para crear APIs.
- **Modularidad**: Separación clara de responsabilidades con carpetas para API, servicios, repositorios, modelos y esquemas.
- **Autenticación**: Manejo de tokens JWT para autenticación segura.
- **Base de datos**: Integración con SQLAlchemy para ORM.
- **Migraciones**: Uso de Alembic para gestionar migraciones de la base de datos.
- **Paginación**: Soporte para paginación en los endpoints.
- **Pruebas**: Configuración inicial para pruebas con Pytest.

## Funcionalidades

### 1. Gestión de Usuarios
- Crear, leer, actualizar y eliminar usuarios.
- Validación de datos con Pydantic.
- Seguridad con contraseñas encriptadas.

### 2. Autenticación
- Inicio de sesión con OAuth2 y JWT.
- Generación y validación de tokens.
- Protección de rutas mediante dependencias.

### 3. Paginación
- Implementación de paginación en endpoints de tipo lista.
- Métodos opcionales para `limit` y `offset`.

### 4. Manejo de Excepciones
- Excepciones personalizadas para errores comunes (e.g., usuario no encontrado, conflictos).
- Respuestas de error consistentes.

### 5. Base de Datos
- Conexión a base de datos relacional mediante SQLAlchemy.
- Modelos definidos para usuarios y otras entidades.

### 6. Pruebas Unitarias
- Configuración inicial para pruebas con Pytest.
- Pruebas básicas para usuarios y autenticación.
- 85% de coverage

## Estructura del Proyecto

```plaintext
fastapi-boilerplate/
├── app/
│   ├── api/              # Routers y endpoints
│   ├── core/             # Configuración y excepciones
│   ├── db/               # Configuración de la base de datos
│   ├── models/           # Modelos SQLAlchemy
│   ├── repositories/     # Lógica de acceso a datos
│   ├── schemas/          # Validación y serialización con Pydantic
│   ├── services/         # Lógica de negocio
│   └── utils/            # Utilidades auxiliares
├── test/                 # Pruebas
├── main.py               # Punto de entrada
├── requirements.txt      # Dependencias
├── Procfile              # Despliegue en Railway
└── .gitignore            # Archivos ignorados por Git
```

## Requisitos Previos

- Python 3.8 o superior
- PostgreSQL (u otra base de datos compatible con SQLAlchemy)

## Instalación

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git](https://github.com/FabiCerchi/fastapi-boilerplate
   cd fastapi-boilerplate
   ```
2. Inicializa tu entorno virtual e instala los requerimientos
   ```bash
   python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
   ```
2. Crea tu archivo .env en el root ./
   ```plaintext
    PROJECT_NAME='fastapi-RESTful-Boilerplate'
    #Database connection
    POSTGRES_USER= 'TU_USER'
    POSTGRES_PASSWORD= 'TU_PASSWORD'
    POSTGRES_DB= 'TU_DB_NAME'
    POSTGRES_HOST= 'TU_LOCAL_HOST'
    POSTGRES_PORT= 5432
    SECRET_KEY = 'TU_SECRET_KEY'
    ALGORITHM = 'HS256'
   ```
3. Realiza las migraciones con alembi
    1. alembic init migrations (Inicializa la migracion). Genera un alembic.init
    2. en alembic.init borrar sqlalchemy.url
    3. En migrations/env.py antes de run_migrations_offline() incluir:
       
    ```plaintext
    # Importa tu configuración de la base de datos
    from app.core.config import settings
    
    # Importa la base y los modelos
    from app.db.database import Base
    
    # Configuración de Alembic
    config = context.config
    config.set_main_option('sqlalchemy.url', settings.SQLALCHEMY_DATABASE_URI)
    
    if config.config_file_name is not None:
        fileConfig(config.config_file_name)
    
    # Registra el metadata de los modelos
    target_metadata = Base.metadata
    ```
    
    4. alembic revision —autogenerate -m “crear modelos” #Hace un commit de los modelos
    5. alembic upgrade heads
  
4. Inicializa la aplicacion
   ```bash
   uvicorn main:app --reload
   ```

## Licencia
Este proyecto está licenciado bajo la MIT License. Consulta el archivo LICENSE para más información.





