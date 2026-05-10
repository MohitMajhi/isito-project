FROM python:3.9-slim
WORKDIR /app
COPY src/frontend.py .
RUN pip install flask requests
CMD ["python", "frontend.py"]