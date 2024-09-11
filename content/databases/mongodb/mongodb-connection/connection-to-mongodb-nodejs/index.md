---
draft: false
title: "Node.js Connection to MongoDB"
aliases: "/connection-to-mongodb-nodejs/"
seoindex: "index, follow"
seotitle: "Node.js Connection to MongoDB"
seokeywords: "mongodb connection tutorial, node js mongodb example, nodejs connection to mongodb, connect to mongodb database, tutorial mongodb connection, connection tutorial mongodb, connect nodejs mongodb, mongo db connect nodejs, test mongodb connection, mongodb connection example, how to connect to mongodb, connect to mongodb, how to connect to mongodb using nodejs, test connection to mongodb, nodejs mongodb connection, connect to mongodb database nodejs, nodejs driver, mongodb connection nodejs, connect mongo database, nodejs driver for mongodb, mongodb connection string"
seodesc: "Here is the step-by-step tutorial on how to connect to MongoDB database server from your application, deployed on Node.js application server in PaaS hosting."
menu:
    docs:
        title: "Node.js Connection to MongoDB"
        url: "/connection-to-mongodb-nodejs/"
        weight: 40
        parent: "mongodb-connection"
        identifier: "connection-to-mongodb-nodejs.md"
---

# Node.js Application Connection to MongoDB

**MongoDB** is a popular NoSQL database, which is natively supported by the platform and can be easily installed on the Cloud. Below, we'll consider a simple example of how to connect this DB stack from your **Node.js** application server.

1\. In order to follow this guide, you'll need *Node.js* and *MongoDB* servers either within the platform (you can [create](/setting-up-environment/) it at any time) or on any external resources.

![MongoDB Node.js environment](01-mongodb-nodejs-environment.png)

In our case, both instances are hosted within a single environment.

2\. Connect to your application server via [SSH Gate](/ssh-gate/).

![SSH connection to Node.js](02-ssh-connection-to-nodejs.png)

3\. Next, download and install an official [MongoDB driver for Node.js](https://github.com/mongodb/node-mongodb-native):
```bash
npm install -s mongodb
```

![install MongoDB driver for Node.js](03-install-mongodb-driver-for-nodejs.png)

In a moment the package will be successfully installed.

4\. Now, create a file with a script to establish connection with your database. You can use any preferable text editor for this task, as well as any filename with the ***.js*** extension (e.g. ***vim script.js***).
```js
var MongoClient = require('mongodb').MongoClient;
// Connect to the db
MongoClient.connect("mongodb://{user}:{password}@{host}:{port}/{database}", { useUnifiedTopology: true, useNewUrlParser: true }, function(err, db) {
if(!err) {
   console.log("You are connected!");
   };
      db.close();
});
```

Here, you need to adjust the [connection string](https://docs.mongodb.com/manual/reference/connection-string/) (all the required information is provided within email for your MongoDB node):

* ***{user}*** - username to log into database with
* ***{password}*** - password for the appropriate user
* ***{host}*** - link to your MongoDB container
* ***{port}*** - port to be used for connection (use the default one - *27017*)
* ***{database}*** - database to be accessed (e.g. the default one - *admin*)

![MongoDB connection script](04-mongodb-connection-script.png)

With this script you can access the specified database server and, if connection is successfully established, see the "*You are connected!*" phrase.

5\. Let's run the code, using the appropriate command:
```bash
node script.js
```

![check Node.js connection to MongoDB](05-check-nodejs-connection-to-mongodb.png)

If everything is specified correctly, you should see the "*You are connected!*" string within terminal. Next, you can [extend code](http://mongodb.github.io/node-mongodb-native/2.2/api/) to execute all of the required actions.


## What's next?

* [Java Connection to MongoDB](/connection-to-mongodb/)
* [PHP Connection to MongoDB](/connection-to-mongodb-for-php/)
* [Python Connection to MongoDB](/connection-to-mongodb-python/)
* [MongoDB Auto-Clustering](/mongodb-auto-clustering/)
* [MongoDB Replica Set](/mongodb-replica-set/)