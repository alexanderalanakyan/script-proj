# Simple module for functions needed for handling errors
from pathlib import Path
from .print import console_print
from .log import log
import traceback
import sys
import logging

sys.path.append("libs")
from rich.traceback import install

install(show_locals=True)


def exception_exit(e):
    console_print(f"{type(e).__name__} has occured...\n")
    console_print(
        "as such exiting program, please send the follow sections to developers:\n"
    )
    console_print(traceback.format_exc())
    console_print("\nSettings:")
    try:
        settings_path = Path(__file__).parent.parent / "settings" / "settings.yaml"
        settings_path = settings_path.resolve()

        with open(settings_path, "r", encoding="utf-8") as f:
            print(f.read())

    except FileNotFoundError:
        log("Settings file is missing.", logging.CRITICAL)
        log("Reinstall config file or set the path properly.", logging.DEBUG)

    except PermissionError:
        log("No permission to read (and maybe write) settings file\n", logging.CRITICAL)
        log(
            f"try reinstalling the file or manually running:\nchmod a+rw {settings_path} If that doesn't work report to repo.",
            logging.DEBUG,
        )

    except Exception as e:
        log(f"Unexpected error: {type(e).__name__}: {e}\n", logging.CRITICAL)
        log("Check file integrity or reinstall.", logging.DEBUG)
    raise SystemExit from e
