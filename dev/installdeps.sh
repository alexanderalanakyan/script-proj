if [ -z $(command -V uv) ]; then
curl -LsSf https://astral.sh/uv/install.sh | sh
fi

uv sync
uv lock --check