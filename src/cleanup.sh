#!/usr/bin/env bash
set -euo pipefail
if [  ${PWD##*/} != "src" ]; then
exit 1
fi

rm -rf ./libs/*
./bin/gum confirm "Would you like to delete the entire repo? aka $(realpath ../)/*" && rm -rf ../* || exit 0
