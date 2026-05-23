"""User part of installation modules"""

from pathlib import Path
import os
import getpass

from functions import yaml
from functions import error_handler as error


config: dict = yaml.read() or {}  # type: ignore[reportAssignmentType]
main_cfg: dict = config.get("main") or {}
user_cfg: dict = config.get("user") or {}
dots_cfg: dict = config.get("dots") or {}


home_dir = os.environ.get("HOME") or ""
user_home = Path(home_dir).resolve() or ""
try:
    username=getpass.getuser
except OSError as e:
    error.exception_exit(e)

if main_cfg.get("install_done") or username == "root":
    raise SystemExit from Exception(
        "\nInstalltion config either malformed or finished\n"
    )

if dots_cfg.get("dotfiles_enabled"):
    if not user_home.exists():
        print("You do seemingly do not have a user home dir")
        # REFACTOR


else:
    print("\n----Skipping dotfiles linking: no userhome/dotfiles not enabled----\n")
#ADD SERVICES
