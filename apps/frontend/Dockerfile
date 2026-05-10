FROM python:3.12-slim
WORKDIR /app
COPY apps/frontend/src/frontend.py .
COPY pyproject.toml .
RUN pip install .
CMD ["python", "frontend.py"]