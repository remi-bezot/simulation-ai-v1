from logging.config import fileConfig
import os
import sys
from sqlalchemy import engine_from_config, pool
from alembic import context
from dotenv import load_dotenv
import pkgutil
import importlib

# Ajouter le chemin du projet au sys.path pour éviter des problèmes d'import
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../../../"))
)

# Charger les variables d'environnement depuis un fichier .env
if not load_dotenv():
    print("⚠️  Fichier .env non trouvé. Assurez-vous qu'il est correctement configuré.")

# Configuration Alembic
config = context.config

# Remplacer l'URL de la base dans alembic.ini par celle des variables d'environnement
DATABASE_URL = os.getenv("DATABASE_URL_POSTGRESQL")
if DATABASE_URL:
    config.set_main_option("sqlalchemy.url", DATABASE_URL)
else:
    raise RuntimeError(
        "❌ La variable d'environnement 'DATABASE_URL_POSTGRESQL' n'est pas définie. Vérifiez votre configuration."
    )

# Configurer le logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importer dynamiquement les modèles SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import dynamique des modèles SQLAlchemy dans `models/`
models_dir = os.path.join(
    os.path.dirname(__file__), "../../../models"
)  # Chemin vers `models/`

for _, module_name, _ in pkgutil.iter_modules([models_dir]):
    importlib.import_module(
        f"app.infrastructure.database.postgresql.models.{module_name}"
    )

# Configuration des métadonnées pour Alembic
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Exécuter les migrations en mode 'offline'."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Exécuter les migrations en mode 'online'."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
