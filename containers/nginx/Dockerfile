FROM nginx:latest

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY key.pem /root/ssl/key.pem
COPY cert.pem /root/ssl/cert.pem
RUN rm /var/log/nginx/access.log && rm /var/log/nginx/error.log

RUN curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-8.1.0-amd64.deb
RUN dpkg -i filebeat-8.1.0-amd64.deb
COPY filebeat.yml /etc/filebeat/filebeat.yml
RUN filebeat modules enable nginx
COPY nginx.yml /etc/filebeat/modules.d/
COPY filebeat-restart.sh /
COPY docker-entrypoint.sh /
RUN chmod a+x /filebeat-restart.sh && chmod a+x /docker-entrypoint.sh