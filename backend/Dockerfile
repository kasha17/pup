FROM python:3.12
ENV PYTHONUNBUFFERED 1
WORKDIR /code/backend
COPY requirements.txt /code/backend/

RUN pip install --upgrade pip && pip install -r requirements.txt
ADD . /code/backend/        
WORKDIR /code
COPY docker/entrypoint.sh ./
WORKDIR /code/backend