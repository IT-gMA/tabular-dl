import os
from pathlib import Path
import unittest
from mock import patch

ABSOLUTE_PATH = r"/Users/tiend/PycharmProjects/tabular-dl"
# set the project directory within the code file instead of via the console
with patch.dict('os.environ', {"PROJECT_DIR": ABSOLUTE_PATH}):
    PROJECT_DIR = Path(os.environ['PROJECT_DIR']).absolute().resolve()
    DATA_DIR = PROJECT_DIR / 'data'
    OUTPUT_DIR = PROJECT_DIR / 'output'


def get_path(relative_path: str) -> Path:
    return (
        Path(relative_path)
        if relative_path.startswith('/')
        else PROJECT_DIR / relative_path
    )
