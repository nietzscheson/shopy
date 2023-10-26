from dependency_injector import providers

from shopy.common.domain.unit_of_work import AbstractUnitOfWork


class UnitOfWorkProvider(providers.Singleton):
    provider_type = AbstractUnitOfWork


from dependency_injector import containers, providers


class SingletonSessionProvider(providers.Provider):
    __slots__ = ("_factory", "_instance")

    def __init__(self, provides, *args, **kwargs):
        self._factory = providers.Factory(provides, *args, **kwargs)
        self._instance = None  # Initialize the instance holder
        super().__init__()

    def __deepcopy__(self, memo):
        copied = memo.get(id(self))
        if copied is not None:
            return copied

        copied = self.__class__(
            self._factory.provides,
            *providers.deepcopy(self._factory.args, memo),
            **providers.deepcopy(self._factory.kwargs, memo),
        )
        self._copy_overridings(copied, memo)

        # Copy the instance if it exists
        if self._instance is not None:
            copied._instance = self._instance

        return copied

    @property
    def related(self):
        """Return related providers generator."""
        yield from [self._factory]
        yield from super().related

    def _provide(self, args, kwargs):
        if self._instance is None:
            self._instance = self._factory(*args, **kwargs)
        return self._instance
