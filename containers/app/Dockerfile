FROM python:3.9

COPY setup.py /home/
COPY my_monit/*.py /home/
WORKDIR /home
RUN pip3 install flask pika mysql-connector-python python-logstash dependency_injector pyjwt

# RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.1.0-amd64.deb
# RUN dpkg -i filebeat-8.1.0-amd64.deb
# COPY filebeat.yml /etc/filebeat/filebeat.yml
# COPY filebeat-restart.sh /
# COPY docker-entrypoint.sh /
# RUN chmod a+x /filebeat-restart.sh && chmod a+x /docker-entrypoint.sh

ENTRYPOINT python3 app.py
