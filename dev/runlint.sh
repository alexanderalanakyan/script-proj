#!/usr/bin/env bash
source $(find . | grep "installdeps.sh")
uv sync --locked --all-extras --dev && uv run sh -c "pylint \$(git ls-files '*.py') && pyright && bandit -r \$(git ls-files '*.py') && ruff check \$(git ls-files '*.py')"