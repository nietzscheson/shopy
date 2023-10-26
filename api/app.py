from dependency_injector.wiring import inject
from fastapi import Depends, FastAPI, Response

from shopy.user.application.container.user_container import UserContainer
from shopy.user.application.services.create import UserCreateService
from shopy.user.domain.schemes.user_scheme import UserScheme
from shopy.user.domain.user import User

app = FastAPI()


@app.post("/user", response_model=User)
@inject
async def user(
    payload: UserScheme,
    response: Response,
    container_use_case: UserContainer = Depends(UserContainer),
) -> User:
    _user = payload.model_dump()

    async with await container_use_case.main_container.unit_of_work() as uow:
        user_create_service = UserCreateService(
            user_repository=await container_use_case.user_repository()
        )
        await user_create_service(user_scheme=payload)
        await uow.commit()

    return _user
