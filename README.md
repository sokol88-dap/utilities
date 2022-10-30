# **Goals**

Main idea that project to create simple utility scripts to used them in routine jobs.

# **How to install**

## **local dev environment**
If you want just test utilities or run it in your machine without docker containers you can 
just install local dev environment
```
> sudo apt install python3.10
> sudo apt install python3.10-venv
> python3.10 -m venv .dev-3.10
> source .dev-3.10/bin/activate
> python -m pip install -r setup/requirements_dev.txt
```

## **Build docker container**

```
> docker build -f setup/notify.Dockerfile -t notify_changed_ip:latest .
```

# **List of utilities and how to run them**
## **Notify changed IP**

### **Environment variables used in .env file**
We use pydantic approach for parsing .env file. Supported parameters:

Currently we support only PostgreDB. Parameters for setting connect to database:
```
DB_SETTINGS__HOST = "127.0.0.1"
DB_SETTINGS__PORT = 5432
DB_SETTINGS__BD = "notifier"
DB_SETTINGS__USER = "user"
DB_SETTINGS__PASSWORD = "passowrd"
```
Parameters for setting email notification:
```
EMAIL_SETTINGS__SMTP_INSTANCE = "smtp.gmail.com"
EMAIL_SETTINGS__SMTP_PORT = 587
EMAIL_SETTINGS__SENDER_ADDRESS = "sender@mail.com"
EMAIL_SETTINGS__SENDER_PASSWORD = "sender_password"
EMAIL_SETTINGS__TARGET_ADDRESS = "target@mail.com"
```

### **Using command line**
```
> python src/notify_changed_ip/app.py
```

### **Using docker-compose**
This utility used like as job. So it's pass only once.
Before run you also should create .env file with your parameters and place it next to docker-compose.yml 
```
> docker-compose -f setup/docker-compose.yml up
```