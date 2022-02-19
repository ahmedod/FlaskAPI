FROM python:3.7.1-stretch
ADD . /code
WORKDIR /code
RUN pip3 install --upgrade pip &&\
    pip3 install -r requirements.txt
RUN pip3 install gunicorn
EXPOSE 5000
CMD [ "gunicorn", "-w", "4", "--timeout", "360", "--bind", "0.0.0.0:5000", "wsgi", "--reload"]
