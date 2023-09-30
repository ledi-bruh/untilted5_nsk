import typing as t

from .BasePlugin import BasePlugin


__all__ = ['BasePluginFactory']


class BasePluginFactory:

    __slots__ = ()

    async def __call__(self, kwargs: t.Mapping[str, t.Any]) -> BasePlugin:
        raise NotImplementedError()
