FROM python:3.12-slim
WORKDIR /app
COPY apps/backend/src/backend.py .
COPY pyproject.toml .
RUN pip install .
CMD ["python", "backend.py"]