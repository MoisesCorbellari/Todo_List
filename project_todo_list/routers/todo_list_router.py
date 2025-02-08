from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, ConfigDict, Field
from shared.dependencies import get_db
from sqlalchemy.orm import Session
from project_todo_list.models.todo_list_model import Task
from typing import List
from shared.exception import NotFound

router = APIRouter(prefix='/ToDo_List')

class ToDoListResponse(BaseModel):
    id: int
    title: str
    description: str
    created: date
    completed: bool

    class Config:
        model_config = ConfigDict(
            from_attributes=True
        )

class ToDoListRequest(BaseModel):
    title: str = Field(min_length=3, max_length=30)
    description: str = Field(min_length=3, max_length=255)
    completed: bool = Field(default=False)

@router.get("", response_model=List[ToDoListResponse])
def get_all_todo_list(db: Session = Depends(get_db)) -> List[ToDoListResponse]:
    return db.query(Task).all()

@router.get("/{id_task}", response_model=ToDoListResponse)
def get_todo_list_by_id(id_task: int,
                        db: Session = Depends(get_db)) -> List[ToDoListResponse]:
    todo_list: Task = find_todo_list_by_id(id_task, db)
    return todo_list

@router.post("", response_model=ToDoListResponse, status_code=201)
def create_todo_list(task_request: ToDoListRequest,
                     db: Session = Depends(get_db)) -> ToDoListResponse:

    todo_list = Task(
        **task_request.model_dump() 
    )
    
    db.add(todo_list) 
    db.commit() 
    db.refresh(todo_list) 
    return todo_list 

@router.put("/{id_task}/finished", response_model=ToDoListResponse, status_code=200)
def update_todo_list_by_id(id_task: int, task_request: ToDoListRequest, db: Session = Depends(get_db)) -> ToDoListResponse:
    todo_list = find_todo_list_by_id(id_task, db)

    for field, value in task_request.model_dump(exclude_unset=True).items():
        if field == "completed" and todo_list.completed and value:
            raise HTTPException(status_code=400, detail="Tarefa já foi finalizada!")
        setattr(todo_list, field, value)

    db.commit()
    db.refresh(todo_list)
    return todo_list

@router.delete("/{id_task}", status_code=204)
def delete_todo_list_by_id(id_task: int,
                     db: Session = Depends(get_db)) -> None:
    todo_list = find_todo_list_by_id(id_task, db)

    db.delete(todo_list)
    db.commit()

def find_todo_list_by_id(id_task: int, db: Session) -> Task:
    todo_list = db.get(Task, id_task)
    if todo_list is None:
        raise NotFound(name="")
    
    return todo_list
