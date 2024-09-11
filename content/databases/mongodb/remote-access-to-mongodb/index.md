---
draft: false
title: "Remote Access to MongoDB"
aliases: "/remote-access-to-mongodb/"
seoindex: "index, follow"
seotitle: "Remote Access to MongoDB"
seokeywords: "mongodb remote access, access to mongodb, access mongodb database, remote access to mongodb, mongodb access database, mongodb database access, access mongodb server, mongodb server remote access, access a mongodb database, access to mongodb database"
seodesc: "See how to remotely connect to your database node remotely from computer. Set up the remote access to your MongoDB database in a few minutes via Public IP."
menu:
    docs:
        title: "Remote Access"
        url: "/remote-access-to-mongodb/"
        weight: 70
        parent: "mongodb"
        identifier: "remote-access-to-mongodb.md"
---

# Remote Access to MongoDB

You can work with your databases remotely from your computer without having to login to our dashboard. So here are some instructions on how to do this with MongoDB. They can be used both for Java and PHP environments.


## Create the Environment

1\. Log into the platform.

2\. Click the **Create environment** button at the top left.

![create environment](01-create-environment.png)

3\. In the **Environment Topology** dialog, pick your application server (for example, **Tomcat**) and **MongoDB** as the database you want to use. Switch on **Public IPv4** for **MongoDB**. Then type your environment name, for example, *remotemongo.*

![environment wizard](02-environment-wizard.png)

Wait just a minute for your environment to be created.

4\. Click the **info** button for MongoDB and you'll see your **Public IP** at the end of the dropdown list.

![MongoDB node public IP](03-mongodb-node-public-ip.png)


## Remote Connection to MongoDB

1\. Create a new project using any desktop client suitable for **MongoDB** (we use Database Master 4 as an example).

![remote connection new project](04-remote-connection-new-project.png)

![add remote connection](05-add-remote-connection.png)

2\. Specify the **host** (your public IP), **port number** (27017), **username** and **password** (when you created the environment, the platform sent you the email with credentials to the database).

![remote connection credentials](06-remote-connection-credentials.png)

Then click **Test Connection**.

![test remote connection](07-test-remote-connection.png)

As you can see the connection is successfully created.

![remote connection created](08-remote-connection-created.png)


## What's next?

- [MongoDB Auto-Clustering](/mongodb-auto-clustering/)
- [Upgrading to MongoDB 6/7](/updating-to-mongodb-7/)
- [MongoDB License Pricing](/mongodb-license/)
- [MongoDB Backup/Restore Add-On](/mongodb-backup-restore-addon/)
- [MongoDB Encryption in Transit Add-On](/mongodb-ssl-addon/)
- [MongoDB Dump Import/Export](/dump-import-export-to-mongodb/)