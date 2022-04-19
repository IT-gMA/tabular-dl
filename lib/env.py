import os
from pathlib import Path

ABSOLUTE_PATH = r"C:\Users\tiend\PycharmProjects\tabular-dl"
PROJECT_DIR = Path(os.environ[ABSOLUTE_PATH]).absolute().resolve()
DATA_DIR = PROJECT_DIR / 'data'
OUTPUT_DIR = PROJECT_DIR / 'output'


def get_path(relative_path: str) -> Path:
    return (
        Path(relative_path)
        if relative_path.startswith('/')
        else PROJECT_DIR / relative_path
    )
