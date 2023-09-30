from pydantic import BaseModel
import typing as t


class Intent(BaseModel):
    name: str
    answer: str
    questions: t.List[str]
