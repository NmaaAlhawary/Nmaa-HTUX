from databases import Database
from sqlalchemy import MetaData

DATABASE_URL = "postgresql+asyncpg://postgres:Nma2hawary@localhost:5432/postgres"
database = Database(DATABASE_URL)
metadata = MetaData()
