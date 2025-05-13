from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
from sqlalchemy.future import select

from DB.models.todo import Todo as TodoModel
from routes.deps import SessionDep

app = FastAPI()


# Pydantic models
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False


class TodoCreate(TodoBase):
    pass


class TodoRead(TodoBase):
    id: str

    class Config:
        orm_mode = True


@app.get("/", tags=["Welcome"])
async def root():
    return {"message": "Hello Nmaa Hawary"}


@app.get("/todos", response_model=List[TodoRead])
async def get_todos(db: SessionDep):
    result = await db.execute(select(TodoModel))
    todos = result.scalars().all()
    return todos


@app.post("/todos", response_model=TodoRead)
async def create_todo(todo: TodoCreate, db: SessionDep):
    new_todo = TodoModel(
        id=uuid.uuid4(),
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
    )
    db.add(new_todo)
    await db.commit()
    await db.refresh(new_todo)
    return new_todo


@app.get("/todos/{todo_id}", response_model=TodoRead)
async def get_todo(todo_id: str, db: SessionDep):
    result = await db.execute(select(TodoModel).where(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@app.put("/todos/{todo_id}", response_model=TodoRead)
async def update_todo(todo_id: str, updated_todo: TodoCreate, db: SessionDep):
    result = await db.execute(select(TodoModel).where(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    todo.title = updated_todo.title
    todo.description = updated_todo.description
    todo.completed = updated_todo.completed
    await db.commit()
    await db.refresh(todo)
    return todo


@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str, db: SessionDep):
    result = await db.execute(select(TodoModel).where(TodoModel.id == todo_id))
    todo = result.scalar_one_or_none()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    await db.delete(todo)
    await db.commit()
    return {"message": "Todo deleted"}
