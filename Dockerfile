FROM python:slim

ENV FLASK_ENV production

WORKDIR /home/streamapp

COPY requirements.txt requirements.txt
RUN python -m venv env
RUN env/bin/pip install -r requirements.txt

COPY app app
COPY main.py settings.py boot.sh .env ./

EXPOSE 8000
ENTRYPOINT ["./boot.sh"]
