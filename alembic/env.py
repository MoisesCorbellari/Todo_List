import os
from dotenv import load_dotenv
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Carregar variáveis de ambiente
load_dotenv()
database_url = os.getenv("SQLALCHEMY_DATABASE_URL")
if not database_url:
    raise ValueError("A variável de ambiente SQLALCHEMY_DATABASE_URL não foi definida.")

# Configuração do Alembic
config = context.config
config.set_main_option('sqlalchemy.url', database_url)

# Configuração de logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Importação dos modelos
from project_todo_list.models.todo_list_model import Task  # type: ignore
from shared.database import Base

target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Executa migrações no modo offline."""
    context.configure(
        url=config.get_main_option("sqlalchemy.url"),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Executa migrações no modo online."""
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
