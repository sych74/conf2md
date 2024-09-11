---
draft: false
title: "Node.js Connection to MySQL/MariaDB/Percona"
aliases: ["/connection-to-mysql-nodejs/", "/connection-to-mariadb-nodejs/"]
seoindex: "index, follow"
seotitle: "Node.js Connection to MySQL/MariaDB/Percona"
seokeywords: "mysql, mariadb, nodejs, nodejs connection to database, nodejs mysql example, nodejs mariadb example, connect mysql using nodejs, connect mariadb using nodejs, mysql nodejs tutorial, mariadb nodejs tutorial, nodejs driver, nodejs driver for mysql, nodejs mysql npm"
seodesc: "Here is the step-by-step tutorial on how to connect to MySQL/MariaDB database servers from your application, deployed based on a NodeJS application server in the platform."
menu: 
    docs:
        title: "Node.js Connection"
        url: "/connection-to-mysql-nodejs/"
        weight: 40
        parent: "mysql-connection"
        identifier: "connection-to-mysql-nodejs.md"
---

# Node.js Application Connection to MySQL/MariaDB/Percona

**MySQL**, **MariaDB**, and **Percona** are among of the most popular open source SQL databases, used by world's largest organizations. In this guide we'll overview a simple example of **Node.js** application connection to MySQL or MariaDB server.

1\. Log into your PaaS account and [create an environment](/setting-up-environment/) with *MySQL* (or *MariaDB*) database server, we'll also add a *NodeJS* compute node for this tutorial.

![create NodeJS MySQL environment](01-create-nodejs-mysql-environment.png)

2\. Access your NodeJS server via SSH, e.g. with embedded [Web SSH](/web-ssh-client/) client.

![NodeJS Web SSH button](02-nodejs-web-ssh-button.png)

3\. Once connected, get an official [MySQL driver for Node.js](https://www.npmjs.com/package/mysql) (compatible with MariaDB) by executing the following command:
```bash
npm install mysql
```

{{%tip%}}**Note:** MySQL driver for NodeJS 10 is currently in testing, so if the deprecation warnings are shown while operating this server version, you may need to install the testing version:
```bash
npm install mysqljs/mysql
```
{{%/tip%}}

![NodeJS install MySQL connector](03-nodejs-install-mysql-connector.png)

Installation will be finished in a moment.

4\. Prepare a simple Node.js script to verify connection. Create a file with the ***.js*** extension, using any text editor of your choice (e.g. ***vim script.js***).
```js
var mysql = require('mysql');
var con = mysql.createConnection({
  host: "{host}",
  user: "{user}",
  password: "{password}",
  database: "{database}"
});

con.connect(function(err) {
  if (err) throw err;
  console.log("You are connected!");
});
con.end();
```

The placeholders in the code above should be adjusted using the appropriate connection information (is provided within email for your MySQL / MariaDB container):

* ***{user}*** - username to log into database with
* ***{password}*** - password for the appropriate user
* ***{host}*** - link to your MySQL / MariaDB container
* ***{database}*** - database to be accessed (e.g. the default one - *mysql*)

![NodeJS MySQL connection code](04-nodejs-mysql-connection-code.png)

Using this script, you can check connection to the database from your application server and, if it fails, get an error description.

5\. Run code with the appropriate command:
```bash
node script.js
```

![nodejs successful connection](05-nodejs-mysql-connection-test.png)

For successful connection a "*You are connected!*" phrase will be displayed in terminal, otherwise error description will be provided. Now, when you are sure your database container is accessible, [expand the code](https://www.npmjs.com/package/mysql) to execute some real actions on your DB server.


## What's next?

* [Java Connection to MySQL](/connection-to-mysql/)
* [PHP Connection to MySQL](/connection-to-mysql-php/)
* [Python Connection to MySQL](/connection-to-mysql-python/)
* [MySQL Master Slave Replication](/database-master-slave-replication/)
* [MySQL Multi Master Replication](/multi-master-mysql-replication/)