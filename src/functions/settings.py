from .yaml import write
from functions import user_home, dots


def update_packages():
    f_data = []

    for i in Path("./settings/packages").resolve().iterdir():
        for _ in i.iterdir():
            data.update(yaml.read(_)[_.parent.name.removesuffix("-packages.yaml")])

    def walk(x: dict):
        for k, v in x.items():
            if isinstance(v, dict):
                walk(v)
            elif isinstance(v, list) and k == "packages":
                for i in v:
                    f_data.append(i)

    walk(data)

    write("install", "packages", f_data)


def make_dots():
    if (not dots) and user_home:
        (Path(user_home) / ".dotfiles").mkdir(parents=True, exist_ok=True)
