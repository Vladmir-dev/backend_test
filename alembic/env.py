from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
import sys
import os

# Add the project root to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.database import Base  # Import SQLAlchemy Base
from src.config import DATABASE_URL  # Import DATABASE_URL
from src.models import User, Post  # Import models directly for Alembic

# Alembic will configure this object when running the script
config = None

def run_migrations_online():
    """Run migrations in 'online' mode."""
    if not config:
        raise RuntimeError("Configuration not set by Alembic")
    
    # Interpret the config file for Python logging.
    if config.config_file_name:
        fileConfig(config.config_file_name)

    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=Base.metadata
        )

        with context.begin_transaction():
            context.run_migrations()

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    if not config:
        raise RuntimeError("Configuration not set by Alembic")
    
    # Interpret the config file for Python logging.
    if config.config_file_name:
        fileConfig(config.config_file_name)

    context.configure(
        url=DATABASE_URL,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

if __name__ == "__main__":
    # This block should not be executed directly; Alembic handles the call
    raise RuntimeError("This file is intended to be run by Alembic, not directly.")
