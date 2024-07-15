FROM python:3.9.13-slim-buster

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN set -e; \
    apt-get update ;\
    apt-get -y install netcat-traditional ;\
    # apt-get install -y sqlite3 libsqlite3-dev;\
    apt-get -y install gettext ;

# COPY ./requirements.txt /code_api/requirements.txt
RUN set -e; \
    /usr/local/bin/python -m pip install --upgrade pip ;\
    # pip install pipreqs;
    # pipreqs ./;
    python -m pip install -r requirements.txt ;

# RUN mkdir /code_api
COPY . /code_api/
WORKDIR /code_api

RUN chmod +x /code_api/docker/entrypoints/entrypoint.sh

EXPOSE 8000
ENTRYPOINT [ "/code_api/docker/entrypoints/entrypoint.sh" ]
