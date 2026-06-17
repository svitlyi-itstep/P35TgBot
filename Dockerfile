FROM python:3.14-alpine

WORKDIR /app

COPY requrements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "bot.py"]

