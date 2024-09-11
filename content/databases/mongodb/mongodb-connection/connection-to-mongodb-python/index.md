---
draft: false
title: "Python Connection to MongoDB"
aliases: "/connection-to-mongodb-python/"
seoindex: "index, follow"
seotitle: "Python Connection to MongoDB"
seokeywords: "python mongodb example, how to connect to mongodb, mongodb connection tutorial, connect to mongodb database, python mongodb tutorial, test connection to mongodb, mongodb connection tutorial python, connect to mongodb database python, connect mongodb in python, how to connect mongodb using python, python connection to mongodb, python driver for mongodb, python install mongodb driver, python mongodb connection example, mongodb connection string"
seodesc: "Here is the step-by-step tutorial on how to connect to MongoDB database server from your application, deployed on Python application server in PaaS hosting."
menu:
    docs:
        title: "Python Connection to MongoDB"
        url: "/connection-to-mongodb-python/"
        weight: 30
        parent: "mongodb-connection"
        identifier: "connection-to-mongodb-python.md"
---

# Python Application Connection to MongoDB
**MongoDB** is one of the most popular NoSQL databases, which allows developers to easily work with the stored data. This tutorial provides an example of connection to the MongoDB server from your **Python** application.

1\. In our case we have an environment with *Python* and *MongoDB* containers inside (you can [create](/setting-up-environment) such one at any time), but this instruction is suitable for the remote servers as well.
![Python MongoDB environment](1.png)

2\. Connect your compute node via [SSH Gate](/ssh-gate).
![SSH Gate](2.png)

3\. Install a [MongoDB driver for Python](https://github.com/mongodb/mongo-python-driver) using the command below:
```bash
pip install pymongo
```
![install MongoDb driver for Python](3.png)

4\. Set up a simple script to check your DB server connection. For that use any preferable text editor and create a file with the ***.py*** extension (e.g. ***vim script.py***).
```py
from pymongo import MongoClient
client = MongoClient("mongodb://{user}:{password}@{host}:{port}")
db = client.{database}
try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")
client.close()
```

Just adjust the [connection string](https://docs.mongodb.com/manual/reference/connection-string/) with a relevant date, which can be gained from email for your MongoDB node:

* ***{user}*** - username to log into database with
* ***{password}*** - password for the appropriate user
* ***{host}*** - link to your MongoDB container
* ***{port}*** - port to be used for connection (use the default one - *27017*)
* ***{database}*** - database to be accessed (e.g. the default *admin* one)

![MongoDB connection script](4.png)

This script will connect to the specified database server and will try to get its status. If any error occurs in the process, its description will be printed; otherwise, just a &ldquo;*You are connected!*&rdquo; string will be displayed.

5\. So, execute code in the file by running the appropriate command:
```bash
python script.py
```
![run DB connection script](5.png)

The &ldquo;*You are connected!*&rdquo; string ensures, that application was able to connect the DB server successfully, so you can start managing database node by [extending code](http://api.mongodb.com/python/current/api/pymongo/) with other operations.


## What's next?

* [Java Connection to MongoDB](/connection-to-mongodb/)
* [PHP Connection to MongoDB](/connection-to-mongodb-for-php/)
* [Node.js Connection to MongoDB](/connection-to-mongodb-nodejs/)
* [MongoDB Auto-Clustering](/mongodb-auto-clustering/)
* [MongoDB Replica Set](/mongodb-replica-set/)