# Helper functions for YAML style config
from pathlib import Path
import tomllib
from libs.yaml import load, dump

try:
    from libs.yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from libs.yaml import Loader, Dumper

cfg_file = (Path(__file__).parent.parent / "settings" / "settings.yaml").resolve()


def write(section, key, value=None, file_path=cfg_file):
    # Function for writing specific values to certain files
    data = read(file_path=file_path)

    if section not in data:
        data[section] = {}
    elif not value:
        data[section] = key
    else:
        data[section][key] = value
    with open(file_path, "w") as write_file:
        dump(data, write_file)


def read(file_path=cfg_file):
    # Function for reading certain files
    if not file_path.exists():
        raise FileNotFoundError("File not found")
    with open(file_path, "r") as read_file:
        data = load(read_file, Loader=Loader) or {}
    return data
