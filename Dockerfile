FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./src /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
EXPOSE 80