from fastapi import Depends, FastAPI, HTTPException

from api.depends.container_manager import container_manager
from shopy.user.application.container.user_container import UserContainer
from shopy.user.application.services.create import UserCreateService
from shopy.user.domain.schemes.user_scheme import UserScheme
from shopy.user.domain.user import User

app = FastAPI()


@app.post("/user", response_model=User)
async def user(
    payload: UserScheme,
    container_use_case: UserContainer = Depends(container_manager(UserContainer)),
) -> User:
    _user = payload.model_dump()

    try:
        unit_of_work = await container_use_case.main_container.unit_of_work()
        async with unit_of_work as uow:
            user_create_service = UserCreateService(
                user_repository=await container_use_case.user_repository()
            )
            await user_create_service(user_scheme=payload)
            await uow.commit()

        return _user

    except Exception as e:
        # Handle specific exceptions and return custom error responses if needed
        raise HTTPException(status_code=400, detail=str(e))

    # query = select(User).where(User.name == _user_factory.name)

    # _user = await db.execute(query.limit(1))

    # assert _user_factory.name == _user.scalar().name
    #    async with await container_use_case.main_container.unit_of_work() as uow:
    #        user_create_service = UserCreateService(
    #            user_repository=await container_use_case.user_repository()
    #        )
    #        await user_create_service(user_scheme=payload)
    #        await uow.commit()

    return _user
