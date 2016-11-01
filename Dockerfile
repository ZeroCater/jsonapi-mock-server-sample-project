FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
RUN pip install --upgrade pip
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --src=/pip-install -r requirements.txt
ADD . /code/
