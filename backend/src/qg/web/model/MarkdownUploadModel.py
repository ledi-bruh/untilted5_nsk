from fastapi import UploadFile
from pydantic import BaseModel


class MarkdownUploadModel(BaseModel):
    file: UploadFile
