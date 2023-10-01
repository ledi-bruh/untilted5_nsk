from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from ..func import GetIntentsFunc
from ..func.models import Intent


class GetIntentsView:

    def __init__(
        self,
        get_intents_func: GetIntentsFunc,
    ) -> None:
        self.__get_intents_func = get_intents_func

    async def __call__(self) -> JSONResponse:
        return JSONResponse(content=jsonable_encoder(await self.__get_intents_func()))
