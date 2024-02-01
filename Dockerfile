FROM python:3.8-slim

WORKDIR /app

COPY study_tool.py .
COPY questions.json .

CMD ["python", "app.py"]
