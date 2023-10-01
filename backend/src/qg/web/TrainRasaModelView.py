from fastapi import Response

from ..func import TrainRasaModelFunc


class TrainRasaModelView:

    def __init__(
        self,
        train_rasa_model_func: TrainRasaModelFunc,
    ) -> None:
        self.__train_rasa_model_func = train_rasa_model_func

    async def __call__(self) -> Response:
        await self.__train_rasa_model_func()
