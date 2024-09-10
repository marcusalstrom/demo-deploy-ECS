FROM python:3.12-alpine

COPY /app /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 80:5000

CMD ["python", "main.py"]
