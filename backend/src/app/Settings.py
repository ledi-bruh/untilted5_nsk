import typing as t
from pathlib import Path
from yaml import safe_load


__all__ = [
    'Settings',
    'settings_load',
]


Settings = t.Mapping[str, t.Any]


def settings_load(path: str) -> Settings:
    file_extension = Path(path).suffix

    with open(path, 'r') as file:

        if file_extension in ('.yml', '.yaml'):
            return safe_load(file)

        raise Exception(f'Settings file with the {file_extension} extension is not supported.')
