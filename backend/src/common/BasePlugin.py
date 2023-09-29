
__all__ = ['BasePlugin']


class BasePlugin:

    __slots__ = ()

    async def initialize(self) -> None:
        raise NotImplementedError()

    async def deinitialize(self) -> None:
        raise NotImplementedError()
