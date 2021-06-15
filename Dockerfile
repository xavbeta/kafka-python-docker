FROM python:3.9.1

#ADD . /tesseract-python
WORKDIR /python-script
RUN pip install kafka-python