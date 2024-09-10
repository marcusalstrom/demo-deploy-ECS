FROM python:3.12-alpine

COPY /app /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 80

CMD ["python", "main.py"]
