import typing as t
import yaml

from ...settings import RasaModelSettings
from .models import Intent


class GetIntentsFunc:

    def __init__(self, rasa_model_settings: RasaModelSettings) -> t.Sequence[Intent]:
        self.__rasa_model_settings = rasa_model_settings

    async def __call__(self) -> t.Sequence[Intent]:
        with open(f'{self.__rasa_model_settings.base}/domain.yml', encoding='utf-8') as f:
            d = yaml.safe_load(f)

        with open(f'{self.__rasa_model_settings.base}/data/nlu.yml', encoding='utf-8') as f:
            n = yaml.safe_load(f)

        nlu_intents = [i['intent'] for i in n['nlu']]
        intents = [
            Intent(
                name=n['nlu'][i]['intent'],
                answer=d['responses']['utter_' + n['nlu'][i]['intent']][0]['text'],
                questions=n['nlu'][i]['examples'].split('\n'),
            )
            for i in range(len(d['intents']))
            if d['intents'][i] in nlu_intents
        ]

        return intents
