FROM python:3.7.1-stretch
ADD . /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
EXPOSE 5000
CMD [ "gunicorn", "-w", "4", "--timeout", "360", "--bind", "0.0.0.0:5000", "wsgi"]
