#!/usr/bin/env bash
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
py_files=$(git ls-files '*.py') 
if [ ! -z "$1" ]; then
$py_files=$(git ls-files '*.py' | grep pwd) 
fi
source "$script_dir/installdeps.sh"
uv run pylint $py_files
uv run pyright $py_files
uv run bandit -r $py_files
uv run ruff check --no-cache $py_files