FROM python:3.10.6

ENV PYTHONUNBUFFERED 1

LABEL maintainer="ehensnfl@gmail.com" 

WORKDIR /srv/blogproject

COPY . .

RUN pip3 install -r /srv/blogproject/requirements.txt

CMD ["uwsgi", "-i", "/srv/blogproject/uwsgi/uwsgi.ini"]