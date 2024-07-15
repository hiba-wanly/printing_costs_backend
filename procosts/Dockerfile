FROM python:3.9

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
COPY . /code_api
WORKDIR /code_api
# COPY ./requirements.txt /code_api/requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
# RUN set -e;\
# apt-get update -y;\
# apt-get install -y python3-dev;\
# apt-get install -y default-libmysqlclient-dev;\
# apt-get -y install netcat-traditional ;\
# apt-get install mysql-server mysql;\
# apt-get install -y sqlite3 libsqlite3-dev;\
# apt-get -y install gettext ;

# RUN mkdir /code_api
RUN chmod +x /code_api/docker/entrypoints/entrypoint.sh

EXPOSE 8050
# ENTRYPOINT [ "/code_api/docker/entrypoints/entrypoint.sh" ]
