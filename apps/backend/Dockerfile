FROM python:3.9-slim
WORKDIR /app
COPY src/backend.py .
RUN pip install flask requests
CMD ["python", "backend.py"]