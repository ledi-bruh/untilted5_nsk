from fastapi import FastAPI
import nltk
# import spacy

from ..settings import Settings, RasaModelSettings
from ..common import BasePlugin
from ..qg import (
    MarkdownUploadView,
    TrainRasaModelView,
    MarkdownUploadFunc,
    UpdateRasaFunc,
    TranslateEnFunc,
    TranslateRuFunc,
    QuestionGenerateFunc,
    TrainRasaModelFunc,
)
from ..intent import (
    # UpdateIntentView,
    # DeleteIntentView,
    GetIntentsView,
    # UpdateIntentFunc,
    # DeleteIntentFunc,
    GetIntentsFunc,
)


nltk.download('stopwords')
nltk.download('brown')
nltk.download('punkt')


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
        # nlp = spacy.load('en_core_web_sm')

        tr_en_func = TranslateEnFunc()
        tr_ru_func = TranslateRuFunc()
        qg_func = QuestionGenerateFunc()
        markdown_upload_func = MarkdownUploadFunc()
        update_rasa_func = UpdateRasaFunc()
        markdown_upload_view = MarkdownUploadView(
            markdown_upload_func,
            tr_en_func,
            qg_func,
            tr_ru_func,
            update_rasa_func,
        )

        self.__app.add_api_route(
            '/md',
            endpoint=markdown_upload_view.__call__,
            response_class=markdown_upload_view.__call__.__annotations__['return'],
            methods=['PUT'],
            tags=['upload markdown file'],
        )

        rasa_model_settings = RasaModelSettings(**self.__settings['rasa'])
        
        train_rasa_model_func = TrainRasaModelFunc(rasa_model_settings)
        train_rasa_model_view = TrainRasaModelView(train_rasa_model_func)
        self.__app.add_api_route(
            '/train',
            endpoint=train_rasa_model_view.__call__,
            response_class=train_rasa_model_view.__call__.__annotations__['return'],
            methods=['POST'],
            tags=['train rasa model'],
        )

        # update_intent_view = UpdateIntentView(UpdateIntentFunc())
        # self.__app.add_api_route(
        #     '/intent/{id}',
        #     endpoint=update_intent_view.__call__,
        #     response_class=update_intent_view.__call__.__annotations__['return'],
        #     methods=['POST'],
        #     tags=['update intent'],
        # )

        # delete_intent_view = DeleteIntentView(DeleteIntentFunc())
        # self.__app.add_api_route(
        #     '/intent/{id}',
        #     endpoint=delete_intent_view.__call__,
        #     response_class=delete_intent_view.__call__.__annotations__['return'],
        #     methods=['DELETE'],
        #     tags=['delete intent'],
        # )

        get_intents_view = GetIntentsView(GetIntentsFunc(rasa_model_settings))
        self.__app.add_api_route(
            '/intents/',
            endpoint=get_intents_view.__call__,
            response_class=get_intents_view.__call__.__annotations__['return'],
            methods=['GET'],
            tags=['get all intents'],
        )

    async def deinitialize(self) -> None:
        pass
