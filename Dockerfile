FROM python:3.8-slim

WORKDIR /app

COPY app.py .
COPY questions.json .

CMD ["python", "app.py"]
