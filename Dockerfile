FROM python:3.12-slim
WORKDIR /app
COPY inventory.py .
CMD ["python", "inventory.py"]