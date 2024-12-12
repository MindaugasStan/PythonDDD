# pylint: disable=unused-import, protected-access
from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine, pool

import app.configs
import app.core.base_db_model
import migrations.models

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

database_dsn = app.configs.database.Database().postgres_dsn
target_metadata = app.core.base_db_model._BaseDeclarative.metadata

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)


def run_migrations_offline() -> None:
    context.configure(
        url=database_dsn,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    connectable = create_engine(database_dsn, poolclass=pool.NullPool)
    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )
        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
