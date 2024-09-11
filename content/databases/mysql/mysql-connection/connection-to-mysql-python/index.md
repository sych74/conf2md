---
draft: false
title: "Python Connection to MySQL/MariaDB/Percona"
aliases: ["/connection-to-mysql-python/", "/connection-to-mariadb-python/"]
seoindex: "index, follow"
seotitle: "Python Connection to MySQL/MariaDB/Percona"
seokeywords: "mysql, mariadb, python, mysql connection python, mariadb connection python, python mysql tutorial, python mariadb tutorial, python connection to mysql, python connection to mariadb, python driver for mysql, python driver for mariadb, mysql connector python, mariadb connector python"
seodesc: "Here is the step-by-step tutorial on how to connect to MySQL database servers from your application, deployed on the Python-based application server in the platform."
menu: 
    docs:
        title: "Python Connection"
        url: "/connection-to-mysql-python/"
        weight: 30
        parent: "mysql-connection"
        identifier: "connection-to-mysql-python.md"
---

# Python Application Connection to MySQL/MariaDB/Percona

**MySQL**, **MariaDB**, and **Percona** are highly popular among developers all over the world, when an open source SQL databases are required. In this instruction we'll show you how to connect your **Python** application, hosted within the platform, to these DB servers.

1\. Log into the platform dashboard and [create a new environment](/setting-up-environment/) with both *Python* and *MySQL* (or *Python* and *MariaDB*) servers.

![create Python MySQL environment](01-create-python-mysql-environment.png)

{{%tip%}}**Tip:** Locating instances within a single environment is just an example, you can establish connection between different environments in just the same way.{{%/tip%}}

2\. After environment creation, access your application server via SSH Gate, e.g. by pressing the **[Web SSH](/web-ssh-client/)** button.

![Python Web SSH button](02-python-web-ssh-button.png)

A terminal emulator with the automatically established SSH connection to your node will be opened in the appropriate tab.

3\. Now, install a [MySQL connector for Python](https://github.com/sanpingz/mysql-connector) (it works with MariaDB as well) with the following command:
```bash
pip install mysql-connector==2.1.6
```

![install Python MySQL connector](03-install-python-mysql-connector.png)

{{%note%}}**Note:** In order to use the newer version of the MySQL connector, you need to additionally install [Protobuf C++](https://developers.google.com/protocol-buffers/docs/downloads) of the *2.6.0* version or above.{{%/note%}}

4\. Next, let's create a simple Python script to establish database connection. You can use any preferable text editor for this task, as well as any filename with the ***.py*** extension (e.g. ***vim script.py***).
```py
import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(user='{user}', password='{password}',
                                host='{host}', database='{database}')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  print("You are connected!")
  cnx.close()
```

Here, you need to adjust the connection string (all the required information is provided within email for your MySQL / MariaDB node):

* ***{user}*** - username to log into database with
* ***{password}*** - password for the appropriate user
* ***{host}*** - link to your MySQL / MariaDB container
* ***{database}*** - database to be accessed (e.g. the default *mysql* one)

![Python MySQL connection code](04-python-mysql-connection-code.png)

This script will connect to the specified database server with the provided credentials and will print connection errors (if any) or just a "*You are connected!*" phrase.

5\. So, let's execute our code with the appropriate command:
```bash
python script.py
```

![Python MySQL connection test](05-python-mysql-connection-test.png)

If the "*You are connected!*" string appeared within terminal, the connection was successful. Now, you can be sure that your database server is accessible and you can [extend the code](https://dev.mysql.com/doc/connector-python/en/) to execute the required actions.


## What's next?

* [Java Connection to MySQL](/connection-to-mysql/)
* [PHP Connection to MySQL](/connection-to-mysql-php/)
* [Node.js Connection to MySQL](/connection-to-mysql-nodejs/)
* [MySQL Master Slave Replication](/database-master-slave-replication/)
* [MySQL Multi Master Replication](/multi-master-mysql-replication/)