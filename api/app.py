from fastapi import Depends, FastAPI, Response

from api.depends.container_manager import container_manager
from shopy.user.application.container.user_container import UserContainer
from shopy.user.application.services.create import UserCreateService
from shopy.user.domain.schemes.user_scheme import UserScheme
from shopy.user.domain.user import User

app = FastAPI()


@app.post("/user", response_model=User)
async def user(
    payload: UserScheme,
    response: Response,
    container_use_case: UserContainer = Depends(container_manager(UserContainer)),
) -> User:
    _user = payload.model_dump()

    async with container_use_case.main_container.unit_of_work():
        user_create_service = UserCreateService(
            user_repository=container_use_case.user_repository
        )
        await user_create_service(_user)

        # uow.commit()

    return _user
    # container_use_case.user_repository.add(_user)
    # container_use_case.main_container.session().commit()
    # return "Hello"
    # return User(_user)
