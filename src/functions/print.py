import sys

sys.path.append("libs")
from rich import get_console, print

console = get_console()


def cprint(x="No str?", style="bold red"):
    console.print(x, style=style)


def pprint(x="[bold red] No Str? [/bold red]"):
    print(x)
