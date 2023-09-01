from dependency_injector import providers

from shopy.common.domain.unit_of_work import AbstractUnitOfWork


class UnitOfWorkProvider(providers.Singleton):
    provider_type = AbstractUnitOfWork
