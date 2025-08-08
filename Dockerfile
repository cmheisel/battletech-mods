FROM python:3.10-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:0.8.6 /uv /bin/uv

ENV UV_COMPILE_BYTECODE=1 UV_LINK_MODE=copy
WORKDIR /app
COPY uv.lock pyproject.toml /app/
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-install-project --no-dev
COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
  uv sync --frozen --no-dev


ENV PATH="/app/.venv/bin:$PATH"
ENTRYPOINT ["uv", "run"]