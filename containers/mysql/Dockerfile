FROM mysql:5.7

RUN apt-get update
RUN apt-get install curl -y

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.1.0-amd64.deb
RUN dpkg -i filebeat-8.1.0-amd64.deb

COPY filebeat.yml /etc/filebeat/filebeat.yml
COPY mysql.yml /etc/filebeat/modules.d/
COPY filebeat.cnf /etc/mysql/conf.d/

RUN chmod a+x /etc/init.d/filebeat
RUN filebeat modules enable mysql
RUN update-rc.d filebeat defaults
