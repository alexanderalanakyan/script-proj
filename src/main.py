from pathlib import Path
import tomllib

cfg_file = Path("./settings/test.toml").resolve()

if not cfg_file.exists():
    raise SystemExit


def write_to_toml(section, key, value):
    with open(cfg_file, "rb") as f:
        data = tomllib.load(f)
    if section not in data:
        data[section] = {}
    data[section][key] = value
    lines = []
    for sec, it in data.items():
        lines.append(f"[{sec}]\n")
        for k, v in it.items():
            if isinstance(v, bool):
                v = "true" if v else "false"
            elif isinstance(v, list):
                v = "[" + ", ".join(f'"{i}"' for i in v) + "]"
            elif not isinstance(v, (int, float)):
                v = f'"{v}"'
            lines.append(f"{k} = {v}\n")
        lines.append("\n")
    with open(cfg_file, "w", encoding="utf-8") as f:
        f.writelines(lines)


write_to_toml("ttt", "jo", 102)
