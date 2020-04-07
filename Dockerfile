FROM python:3.7
COPY . /Fruits_Vegetables_Classifier_WebApp

WORKDIR /Fruits_Vegetables_Classifier_WebApp

RUN pip install -r requirements.txt
