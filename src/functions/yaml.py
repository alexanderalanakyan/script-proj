# Helper functions for YAML style config
from pathlib import Path
from libs.yaml import load, dump
from .error_handler import exception_exit

try:
    from libs.yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from libs.yaml import Loader

cfg_file = (Path(__file__).parent.parent / "settings" / "settings.yaml").resolve()


def write(section, key, value=None, file_path=cfg_file):
    # Function for writing specific values to certain files
    data = read(file_path=file_path)

    if section not in data:
        data[section] = {}
    elif value is None:
        data[section] = key
    else:
        data[section][key] = value
    try:
        with open(file_path, "w", encoding="utf-8") as write_file:
            dump(data, write_file)
    except PermissionError as e:
        exception_exit(e)


def read(file_path=cfg_file):
    # Function for reading certain files
    if not file_path.exists():
        exception_exit(FileNotFoundError)
    try:
        with open(file_path, "r") as read_file:
            data = load(read_file, Loader=Loader) or {}
    except PermissionError as e:
        exception_exit(e)
    return data
