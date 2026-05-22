#!/usr/bin/env bash
source ./installdeps.sh

uv run ruff format "$(git ls-files '*.py')"