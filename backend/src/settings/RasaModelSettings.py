from pydantic import BaseModel
import typing as t


class RasaModelSettings(BaseModel):
    base: str
    domain: str
    config: str
    training_files: t.Sequence[str]
    output: str
    dry_run: bool = False
    force_training: bool = False
    finetuning_epoch_fraction: float = 1.0
