from pathlib import Path
from functions import functions as f
import tomllib
import os

config_file = Path(__file__).resolve().parent.parent / "settings" / "settings.toml"

with open(config_file, "rb") as f:
    config = tomllib.load(f)

main_cfg = config.get("main")
user_cfg = config.get("user")
dots_cfg = config.get("dots")

home_dir = os.environ.get("HOME")
user_home = Path(home_dir).resolve() if home_dir else None

if main_cfg.get("install_done") != "False":
    # REFACTOR
    raise SystemExit

if main_cfg.get("dotfiles_enabled") and user_home:
    if Path.exists(user_home / ".dotfiles"):
        # REFACTOR
        raise SystemExit
    else:
        dest = Path(user_home / ".dotfiles").resolve()
        dots_dir = dots_cfg.get("dots_dir")
        src_path = Path(dots_dir) / ".dotfiles" if dots_dir else None
        src = src_path.resolve() if src_path and src_path.resolve().exists() else None

        if (
            src
            and not dest.exists()
            and not input(f"Input (y or n) to symlink: {src} to {dest}")
            .lower()
            .strip()
            .startswith("n")
        ):
            try:
                os.symlink(src, dest, True)
            except os.error as e:
                # REFACTOR
                raise SystemExit from e
        else:
            # REFACTOR
            raise SystemExit

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
