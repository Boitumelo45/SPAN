FROM python:3.9-slim-buster

WORKDIR league
ADD . league

CMD ["python", "league/app/main.py"]
