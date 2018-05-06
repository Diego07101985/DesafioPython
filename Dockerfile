FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install colorlog
RUN pip install -r requirements.txt
ADD . /code/
