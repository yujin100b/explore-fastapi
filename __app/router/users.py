from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from fastapi import Query

#APIRouter creates path operations for user module
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

class User(BaseModel):
    user_id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    father_name: Optional[str] = Field(
        None, title="The father name of the user", max_length=300
    )
    age: float = Field(..., gt=0,
                       description="The age must be greater than zero")

@router.get("/")
async def read_root():
    return {"Hello": "World"}

@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "full_name": "Danny Manny", "email": "danny.manny@gmail.com"}

@router.get("/detail")
async def read_users(q: Optional[str] = Query(None, max_length=50)):
    results = {"users": [{"user_id": 1}, {"user_id": 2}]}
    if q:
        results.update({"q": q})
    return results

@router.post("/add")
async def add_user(user: User):
    return {"full_name": user.first_name+" "+user.last_name}

@router.put("/update")
async def read_user(user: User):
    return {"user_id": user.user_id, "full_name": user.first_name+" "+user.last_name, "email": user.email}

@router.delete("/{user_id}/delete")
async def read_user(user_id: int):
    return {"user_id": user_id, "is_deleted": True}