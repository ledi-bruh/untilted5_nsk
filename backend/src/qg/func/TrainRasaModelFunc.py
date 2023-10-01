from rasa import train

from ...settings import RasaModelSettings


class TrainRasaModelFunc:

    def __init__(self, rasa_model_settings: RasaModelSettings) -> None:
        self.__rasa_model_settings = rasa_model_settings

    async def __call__(self) -> None:
        train(**dict(self.__rasa_model_settings))
