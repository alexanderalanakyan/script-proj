from pathlib import Path
import os
import sys

from functions import yaml as yaml


config = yaml.read()

main_cfg = config.get("main")
user_cfg = config.get("user")
dots_cfg = config.get("dots")
home_dir = os.environ.get("HOME")
user_home = Path(home_dir).resolve() if Path(home_dir).resolve().exists() else None

if main_cfg.get("install_done") != False:
    # REFACTOR
    raise SystemExit

if dots_cfg.get("dotfiles_enabled"):
    if not user_home.exists():
        print("You do seemingly do not have a user home dir")


else:
    print("\n----Skipping dotfiles linking: no userhome/dotfiles not enabled----\n")

if user_cfg.get("user_services"):
    f.run(
        ["systemctl", "--user", "enable", "--now", *user_cfg.get("user_services", [])]
    )

try:
    # REFACTOR
    with open(config_file, "w") as cfg_file:
        write_file = tomllib.load(cfg_file)
        write_file["main"]["userdone"] = "True"
        config.write(write_file)
except Exception as e:
    # REFACTOR
    raise SystemExit from e
