from pathlib import Path
import os
import getpass
from .error_handler import *
from .yaml import *
from .log import *
from .print import *
from .settings import *

user_home = (
    os.environ.get("HOME")
    if not os.environ.get("HOME").__contains__("root")
    and (getpass.getuser() != "root" and not getpass.getuser().__contains__("root"))
    else ""
)

dots = (
    Path(Path(user_home) / "/.dotfiles")
    if Path(Path(user_home) / "/.dotfiles").exists()
    else ""
)
