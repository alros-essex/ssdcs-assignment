# MyMonit

## Documents Part 1

📜 [team contract](documents/TeamContract.docx)

🍉 [Documentation MyMONIT](documents/safe-repository.pdf)

🔎 [turnitin](documents/turnitin.pdf)

<img src="https://img.shields.io/badge/Word_count-1013-%230a0"/>
<img src="https://img.shields.io/badge/Content-complete-%230a0"/>
<img src="https://img.shields.io/badge/Turnitin-ok-%230a0"/>

🧑‍🏫 [feeback on an old draft](https://nam11.safelinks.protection.outlook.com/?url=https%3A%2F%2Fkaplanopenlearning.zoom.us%2Frec%2Fshare%2FU3axgeb_Pd2M4ofFlkGgZS63-nBp-KuXP9LDy_Ap_PGQHjvL13K4pHSI5kfAYrq6.y_sNkwmrFAJTR3RO&data=04%7C01%7Ccathryn.peoples%40kaplan.com%7Ca9634329b9364a87bd5508da117aaac3%7C057daf85b1d544cdab7b0a4ce1b29eae%7C0%7C0%7C637841515788167027%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000&sdata=WF7kdU5lxUgIQ36NsIqLIqMb2nC%2Bu0%2FykupHDNCFL90%3D&reserved=0). The feedback refers to [this version](https://github.com/ros101/ssdcs-assignment/blob/d7a013503cfe135dfdf533ff008e088bf9b89e1e/documents/safe-repository.pdf)

## Documents Part 2

🔥 [README](README/README.pdf)

<img src="https://img.shields.io/badge/Content-complete-%230a0"/>
<img src="https://img.shields.io/badge/Turnitin-ok-%230a0"/>

🎁 [Presentation](README/presentation.keynote.pdf)

### Other documents

🎸 [MONIT at CERN](https://www.epj-conferences.org/articles/epjconf/pdf/2019/19/epjconf_chep2018_08031.pdf) (the real one)

🧲 The Computer Security Team (2020) Computer Security: Digital Stolen Goods of CERN?. Availble from [home.cern](https://home.cern/news/news/computing/computer-security-digital-stolen-goods-cern) or [this repo](documents/Computer-Security-Digital-stolen-goods-of-CERN.pdf)

## 🔐 Implementation

🍊 [project with adapters](./adapters)

🍐 [project with MyMonit - core](./containers/app)

🍋 [Logstash](./containers/logstash)

🥦 [Mysql](./containers/mysql)

🥑 [Nginx](./containers/nginx)

🚀 [Postman collection](./postman)

### Requirements

- docker
- python
- postman (optional)

### How to deploy

to start the complete deployment: `./run.sh`

to deploy only RabbitMQ and MySQL: `./run-infra.sh`

### Python projects

setup with `pip3 install -e .`

run the tests with `python3 setup.py test`

start it with `python3 main.py` (adapters use different names)

### Code quality

`containers/app/run-checks.sh` runs `pylint`, `cov`, and `bandit` generating reports in `containers/app/reports`

#### Pylint

rules from https://github.com/google/styleguide

### 😃 How to take a quick look 😃

Install the prerequisites.

start infra:

```bash
./runInfra.sh
```

start the application:
```
cd containers/app/
# On Windows
$Env:GOOGLE_APPLICATION_CREDENTIALS = "$(pwd)\private_key.json"
# Other systens
export GOOGLE_APPLICATION_CREDENTIALS="$(pwd)/private_key.json"
python3 main.py
```

start stdin adapter:

```bash
cd adapters/generators
python3 from_stdin.py
```

insert data by typing in the adapter's console (push return) and retrieve data with:

```bash
curl --location --request GET 'http://localhost:5000/measures/1'
```

Please note that there is hardcoded data in the db (for testing)ng 

### 🌐 How to work on statics 🌐

start infra and flask

```bash
./runInfra.sh
./runFlask.sh
```

the statics are in [static](static) (currently they are just placeholders 💩)

### 👮 How to login 👮

open http://localhost:5000/static/index.html and login with one of the 3 users:

|email            |password|user|type     |
|-----------------|--------|----|---------|
|aalcorn@home.cern|123456  |A001|ADMIN    |
|phigg@home.cern  |123456  |S001|SCIENTIST|
|kbouman@home.cern|123456  |S002|SCIENTIST|
    
### 📒 How to generate the api docs 📒

The process is far from being perfect but here it is:

* export the postman collection
* convert it in [https://metamug.com/util/postman-to-swagger/](https://metamug.com/util/postman-to-swagger/)
* fix it with [https://editor.swagger.io/#/](https://editor.swagger.io/#/)
* save it in `swagger`
* run `python3 tohtml.py > api.html`
