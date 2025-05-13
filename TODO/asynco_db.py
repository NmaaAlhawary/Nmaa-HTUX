# app/DB/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import configs

# Define your asynchronous database connection URL
# Note the use of 'asyncpg' driver
ASYNC_SQLALCHEMY_DATABASE_URL = configs.DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Create an asynchronous engine instance connected to your PostgreSQL database
async_engine = create_async_engine(
    ASYNC_SQLALCHEMY_DATABASE_URL,
    pool_pre_ping=True,
    pool_size=10,         # Adjust based on your needs
    max_overflow=12,
    pool_timeout=30,
    pool_recycle=1800,
)

# Configure async sessionmaker to establish new asynchronous sessions
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False,  # keep objects in-memory after commit
    autoflush=False  # only flush when you explicitly call .flush()/.commit()
)

# Declare the base class for all models
Base = declarative_base()
