from pathlib import Path
from functions import functions as f
import tomllib
import os

config_file=Path(__file__).resolve().parent.parent / "settings" / "settings.toml"

with open(
    config_file, "rb"
) as f:
    config = tomllib.load(f)

main_cfg=config.get("main")
user_cfg=config.get("user")
dots_cfg=config.get("dots")

if os.environ.get("HOME"):
    user_home=Path(os.environ.get("HOME")).resolve()
else:
    user_home=None

if main_cfg.get("install_done") != "False":
    #REFACTOR
    raise SystemExit

if main_cfg.get("dotfiles_enabled") == "True" and user_home:
    if(Path.exists(user_home / ".dotfiles")):
        #REFACTOR
        raise SystemExit
    else:
        dest=Path(user_home / ".dotfiles").resolve()
        src=Path(dots_cfg.get("dots_dir") / ".dotfiles").resolve() if Path(dots_cfg.get("dots_dir") / ".dotfiles").resolve().exists() else None

        if src and not dest and not input(f"Input (y or n) to symlink: {src} to {dest}").lower().strip().startswith("n"):
                try:
                    os.symlink(src, dest, True)
                except os.error as e:
                    #REFACTOR
                    raise SystemExit from e
        else: 
            #REFACTOR
            raise SystemExit
    
else:
    print("\n----Skipping dotfiles linking: no userhome/dotfiles not enabled----\n")

if user_cfg.get("user_services"):
    f.run(["systemctl", "--user", "enable", "--now"].extend(user_cfg.get("user_services")))



