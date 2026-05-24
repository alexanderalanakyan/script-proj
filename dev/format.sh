#!/usr/bin/env bash
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
py_files=$(git ls-files '*.py' | grep -v "__init__.py")
if [ $# -ne 0 ]; then
py_files=$(git ls-files '*.py' | grep -v "/")
fi
source "$script_dir/installdeps.sh"
uv run ruff format -v --no-cache $py_files
