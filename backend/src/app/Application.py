from fastapi import FastAPI
import spacy

from .Settings import Settings
from ..common import BasePlugin
from ..qg import (
    MarkdownUploadView,
    MarkdownUploadFunc,
    UpdateRasaFunc,
    TranslateEnFunc,
    TranslateRuFunc,
    QuestionGenerateFunc,
)


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
        
        nlp = spacy.load('en_core_web_sm')
        
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
            '/md/',
            endpoint=markdown_upload_view.__call__,
            response_class=markdown_upload_view.__call__.__annotations__['return'],
            methods=['PUT'],
            tags=['md'],
        )

    async def deinitialize(self) -> None:
        pass
