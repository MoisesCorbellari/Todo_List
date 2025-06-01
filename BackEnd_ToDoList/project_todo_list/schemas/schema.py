from pydantic import BaseModel, ConfigDict, Field
from datetime import date

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