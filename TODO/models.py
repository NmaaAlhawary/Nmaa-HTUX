from sqlalchemy import Table, Column, String, Boolean
from database import metadata

todolist_table = Table(
    "todolist",
    metadata,
    Column("id", String, primary_key=True),
    Column("title", String),
    Column("description", String),
    Column("completed", Boolean, default=False),
)
