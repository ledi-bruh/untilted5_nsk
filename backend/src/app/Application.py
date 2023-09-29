from fastapi import FastAPI

from .Settings import Settings
from ..common import BasePlugin


__all__ = ['Application']


class Application(BasePlugin):

    __slots__ = (
        '__settings',
        '__app',
    )

    def __init__(self, settings: Settings, app: FastAPI) -> None:
        self.__settings = settings
        self.__app = app

    async def initialize(self) -> None:
        pass

        # self.__app.add_api_route(
        #     '/users/{user_guid}'
        #     endpoint=view.get_by_id,
        #     methods=['GET'],
        #     tags=[''],
        # )

    async def deinitialize(self) -> None:
        pass
