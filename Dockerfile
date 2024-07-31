FROM python:3.11

ENV PYTHONUNBUFFERED=1

WORKDIR /crm

RUN pip install --upgrade pip "poetry==1.8.2"

RUN poetry config virtualenvs.create false --local
COPY crm .
COPY requirements .
RUN poetry install
