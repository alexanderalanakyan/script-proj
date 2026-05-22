#!/usr/bin/env bash
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source "$script_dir/installdeps.sh"
uv run pylint $(git ls-files '*.py') 
uv run pyright $(git ls-files '*.py')
uv run bandit -r $(git ls-files '*.py')
uv runruff check $(git ls-files '*.py')"