from fastapi import FastAPI

from shopy.user.adapter.inmemory_user_repository import InmemoryUserRepository
from shopy.user.domain.user import User

app = FastAPI()

user_repository = InmemoryUserRepository()


@app.post("/user", response_model=User)
def user() -> User:
    return User().save(user_repository)


@app.get("/users", response_model=int)
def users() -> int:
    return user_repository.total()
