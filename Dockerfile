FROM python:3.8

RUN pip install --upgrade pip
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install -r /var/www/requirements.txt
COPY . /app
WORKDIR /app
CMD flask run --host=0.0.0.0