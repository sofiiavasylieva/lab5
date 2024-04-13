from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

from app import model
from app import schemas
from app.schemas import UserList
from fastapi import HTTPException, Depends, status
from app.db import engine, SessionLocal, Base
from sqlalchemy.orm import Session
from typing import Annotated

Base.metadata.create_all(bind=engine)
app = FastAPI()


class UserList(BaseModel):
    id: int
    first_name: str
    last_name: str
    gender: str
    password: str
    username: str
    status: str
    create_at: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependecy = Annotated[Session, Depends(get_db)]


@app.post('/users/', status_code=status.HTTP_201_CREATED)
def create_user(user: UserList, db: db_dependecy):
    db_user = model.User(**user.dict())
    db.add(db_user)
    db.commit()


@app.get('/users/{user_id}', status_code=status.HTTP_200_OK)
def read_user(user_id: int, db: db_dependecy):
    user = db.query(model.User).filter(
        model.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='Користувача не знайдено')
    return user


@app.delete('/user/{user_id}', status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: db_dependecy):
    db_user = db.query(model.User).filter(
        model.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='Запис не знайдено')
    db.delete(db_user)
    db.commit()


@app.put('/user/{user_id}', status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UserList, db: db_dependecy):
    db_user = db.query(model.User).filter(
        model.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail='Запис не знайдено')
    db.query(model.User).filter(model.User.id == user_id).update(
        user.dict(), synchronize_session=False)
    db.commit()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
