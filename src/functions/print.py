import sys

sys.path.append("libs")
from rich import get_console
from rich.pretty import pprint

console = get_console()


def console_print(x="No str?", style="bold red"):
    console.print(x, style=style)


def super_print(x):
    pprint(x)
