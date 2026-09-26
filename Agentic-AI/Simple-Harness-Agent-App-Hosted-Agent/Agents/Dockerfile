FROM ghcr.io/astral-sh/uv:0.11.7 AS uv
FROM python:3.13-slim

COPY --from=uv /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml ./
ARG UV_DEFAULT_INDEX=https://pypi.org/simple
RUN uv sync \
    --default-index "${UV_DEFAULT_INDEX}" \
    --no-dev \
    --no-install-project

COPY hosted_harness_agent_definition.py harness_tools.py ./
COPY skills ./skills

EXPOSE 8088

CMD ["/app/.venv/bin/python", "hosted_harness_agent_definition.py"]
