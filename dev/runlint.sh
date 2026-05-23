#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
py_files=$(git ls-files '*.py' | grep -v "__init__.py") 
if [ $# -ne 0 ]; then
py_files=$(git ls-files '*.py' | grep -v "/") 
fi
source "$script_dir/installdeps.sh"
uv run pylint $py_files
uv run pyright $py_files
uv run bandit -r $py_files
uv run ruff check --no-cache $py_files