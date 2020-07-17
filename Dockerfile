FROM tiangolo/uwsgi-nginx-flask:python3.8
COPY ./src /app
COPY requirements.txt /app
RUN pip3 install -r requirements.txt
RUN sudo apt-get install certbot python3-certbot-nginx
RUN sudo certbot --nginx
EXPOSE 80