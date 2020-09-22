FROM mysql:5.7.31
COPY ./conf-file.cnf /etc/mysql/conf.d/conf-file.cnf
RUN apt-get update && apt-get install -y netcat
HEALTHCHECK CMD nc -z localhost 3306
