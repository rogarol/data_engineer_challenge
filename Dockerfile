#FROM python:3.12-slim
FROM python:3.9-slim

# Install uv.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the application into the container.
COPY . /app

# Install the application dependencies.
WORKDIR /app
RUN uv sync --frozen --no-cache

# Expose port for traffic
EXPOSE 80

# Run the application.
CMD ["/app/.venv/bin/uvicorn", "app.main:app", "--port", "80", "--host", "0.0.0.0"]