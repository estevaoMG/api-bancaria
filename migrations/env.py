from logging.config import fileConfig

from alembic import context
from sqlalchemy import create_engine

from src.config import settings

# Alembic Config
config = context.config

# Logging
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importa metadata e models (garante registro das tabelas)
from src.database import metadata  # noqa
from src.models.account import accounts  # noqa
from src.models.transaction import transactions  # noqa

target_metadata = metadata


def run_migrations_offline() -> None:
    """Modo offline (gera SQL sem conectar no banco)."""
    context.configure(
        url=settings.database_url.replace("+aiosqlite", ""),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Modo online (executa migrations no banco)."""

    # 🔥 ENGINE SINCRONO (OBRIGATÓRIO pro Alembic)
    connectable = create_engine(settings.database_url.replace("+aiosqlite", ""))

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,  # ajuda a detectar mudanças de colunas
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
