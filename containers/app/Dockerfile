FROM python:3.9

COPY setup.* /home/
COPY main.py /home/
COPY .bandit /home/
COPY .static-tmp/* /home/static/
COPY my_monit/*.py /home/my_monit/
WORKDIR /home
RUN pip3 install -e .

ENTRYPOINT python3 main.py
