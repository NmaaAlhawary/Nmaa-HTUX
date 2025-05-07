from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
from database import database
from models import todolist_table


app = FastAPI()

# Connect to Postgresql DB
@app.on_event("connection")
async def connection():
    await database.connect()

# disConnect to Postgresql DB
@app.on_event("disconnection")
async def disconnection():
    await database.disconnect()

# Pydantic model
class Todo(BaseModel):
    id: Optional[str]
    title: str
    description: Optional[str] = None
    completed: bool = False

@app.get("/")
async def root():
    return {"message": "Hello Nmaa Hawary"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    query = todolist_table.select()
    return await database.fetch_all(query)

@app.post("/todos", response_model=Todo)
async def create_todo(todo: Todo):
    todo.id = str(uuid.uuid4())
    query = todolist_table.insert().values(
        id=todo.id, title=todo.title, description=todo.description, completed=todo.completed
    )
    await database.execute(query)
    return todo

@app.get("/todolist/{todo_id}", response_model=Todo)
async def get_todo(todo_id: str):
    query = todolist_table.select().where(todolist_table.c.id == todo_id)
    todo = await database.fetch_one(query)
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.put("/todolist/{todo_id}", response_model=Todo)
async def update_todo(todo_id: str, updated_todo: Todo):
    query = todolist_table.update().where(todolist_table.c.id == todo_id).values(
        title=updated_todo.title,
        description=updated_todo.description,
        completed=updated_todo.completed,
    )
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated_todo.id = todo_id
    return updated_todo

@app.delete("/todolist/{todo_id}")
async def delete_todo(todo_id: str):
    query = todolist_table.delete().where(todolist_table.c.id == todo_id)
    result = await database.execute(query)
    if not result:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted"}
