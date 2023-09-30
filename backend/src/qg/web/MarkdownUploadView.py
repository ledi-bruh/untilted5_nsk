from fastapi import Response, Depends
import re

from ..func import MarkdownUploadFunc, UpdateRasaFunc, TranslateEnFunc, TranslateRuFunc, QuestionGenerateFunc
from .model import MarkdownUploadModel


class MarkdownUploadView:

    def __init__(
        self,
        markdown_upload_func: MarkdownUploadFunc,
        translate_en_func: TranslateEnFunc,
        qg_fuc: QuestionGenerateFunc,
        translate_ru_func: TranslateRuFunc,
        update_rasa_func: UpdateRasaFunc,
    ) -> None:
        self.__markdown_upload_func = markdown_upload_func
        self.__translate_en_func = translate_en_func
        self.__qg_func = qg_fuc
        self.__translate_ru_func = translate_ru_func
        self.__update_rasa_func = update_rasa_func

    async def __call__(self, request: MarkdownUploadModel = Depends()) -> Response:
        file = await request.file.read()
        data = file.decode('utf-8')

        data = await self.__markdown_upload_func(data)
        print('[INFO] MD UPLOADED')
        data_en = await self.__translate_en_func(data)
        print('[INFO] TO EN DONE')
        result_en = await self.__qg_func(data_en, 8)
        print('[INFO] QG DONE')
        result_ru = [
            [
                re.sub(' ', '_', (await self.__translate_ru_func(a)).strip()),
                [await self.__translate_ru_func(q) for q in qs],
            ]
            for a, qs in result_en
        ]
        print('[INFO] TO RU DONE')
        await self.__update_rasa_func(result_ru)
        print('[INFO] RASA UPDATED')
