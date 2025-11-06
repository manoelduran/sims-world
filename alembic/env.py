from logging.config import fileConfig
from dotenv import load_dotenv
from sqlalchemy import engine_from_config
from sqlalchemy import pool
import sys
import os


dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
print(f"--- [env.py] Tentando carregar .env de: {dotenv_path}")  # DEBUG PRINT 1
loaded = load_dotenv(dotenv_path=dotenv_path)
from alembic import context
from src.core.database import Base
from src.modules.sims.infrastructure.persistence.needs_model import *
from src.modules.sims.infrastructure.persistence.memory_models import *
from src.modules.sims.infrastructure.persistence.relationship_model import *
from src.modules.sims.infrastructure.persistence.sim_model import *
from src.modules.sims.infrastructure.persistence.skill_model import *
from src.modules.sims.infrastructure.persistence.status_model import *
from src.modules.sims.infrastructure.persistence.action_log_model import *

db_url_from_env = os.getenv("DATABASE_URL")


sys.path.insert(
    0, os.path.realpath(os.path.join(os.path.dirname(__file__), "..", "src"))
)
# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
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
    """Run migrations in 'online' mode."""

    db_url = os.getenv("DATABASE_URL")
    if not db_url:
        raise ValueError("Environment variable DATABASE_URL is not set.")

    # Modificar a configuração para usar a URL obtida
    ini_section = config.get_section(config.config_ini_section, {})
    ini_section["sqlalchemy.url"] = db_url  # Define a URL programaticamente

    connectable = engine_from_config(
        ini_section,  # Usa a seção modificada
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
