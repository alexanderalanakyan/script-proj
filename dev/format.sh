#!/usr/bin/env bash
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
source "$script_dir/installdeps.sh"
uv run ruff format -v "$(git ls-files '*.py')"