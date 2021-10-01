#### This project is a monitoring for a Zabbix agent monitoring a RabbitMQ 😁
------------
##### 👨🏻‍💻 About this project
###### This project is a monitoring for a zabbix agent monitoring a rabbitmq, where there is a shellscript consuming the automatically installed API from the rabbitmq monitoring panel, a python file that reads all registered queues and prints how many messages have not yet been consumed
###### With this you can monitor if your rabbitmq consumer is working correctly
------------
##### Installation

- Requirement: use a linux or shell-compatible scripting system

- Python version used: 3.8.0+

- Change the RabbitMQ server API URL in collect.sh

- Check if all your queues have been collected:
```
python3 app.py
```

- Customize your zabbix agent in rabbit.conf

------------
