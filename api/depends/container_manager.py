from typing import Type

from dependency_injector import containers
from fastapi import Depends

from api.utils import get_main_container
from shopy.common.containers.main_container import MainContainer


def container_manager(
    container_use_case: Type[containers.DeclarativeContainer],
):
    def container_use_case_factory(
        main_container: MainContainer = Depends(get_main_container),
    ):
        container = container_use_case()
        container.main_container.override(main_container)
        return container

    return container_use_case_factory
