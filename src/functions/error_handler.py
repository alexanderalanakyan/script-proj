# Simple module for functions needed for handling errors
from pathlib import Path
import traceback

def exception_exit(e):
    print(f"{type(e).__name__} has occured...\n")
    print("as such exiting program, please send the follow sections to developers:\n")
    print(traceback.format_exc())
    print("\nSettings:")
    try:
        settings_path = Path(__file__).parent.parent / "settings" / "settings.yaml"
        settings_path = settings_path.resolve()

        with open(settings_path, "r", encoding="utf-8") as f:
            print(f.read())

    except FileNotFoundError:
        print("Settings file is missing. Reinstall config file or set the path properly.")

    except PermissionError:
        print(f"No permission to read (and maybe write) settings file try reinstalling the file or manually running:\nchmod a+rw {settings_path}\n")
        print("If that doesn't work report to repo.")

    except Exception as e:
        print(f"Unexpected error: {type(e).__name__}: {e}\n Check file integrity or reinstall.")
    raise SystemExit from e