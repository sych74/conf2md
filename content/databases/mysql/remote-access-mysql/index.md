---
draft: false
title: "Remote Access to MySQL/MariaDB/Percona"
aliases: ["/remote-access-mysql/", "/mariadb-remote-access/"]
seoindex: "index, follow"
seotitle: "Remote Access to MySQL/MariaDB/Percona"
seokeywords: "mysql remote access, mariadb remote access, percona remote access, access mysql database, access mariadb database, access percona database, remote access to mysql, remote access to mariadb, remote access to percona"
seodesc: "Examine how to work with your database server remotely from your computer. Get the remote access to your MySQL/MariaDB/Percona database in a few clicks and start querying."
menu:
    docs:
        title: "Remote Access"
        url: "/remote-access-mysql/"
        weight: 40
        parent: "mysql"
        identifier: "remote-access-mysql.md"
---

# Remote Access to MySQL/MariaDB/Percona

You can work with your databases remotely from your computer without having to login to our dashboard. So here are some instructions on how to access with **MySQL**. They can be used both for Java and PHP environments.

{{%tip%}}**Tip:** The same steps can be used for remote access to **MariaDB** and **Percona**.{{%/tip%}}


## Create Environment

1\. Log into the platform.

2\. Click the **Create environment** button at the top left.

![create environment](01-create-environment.png)

3\. In the **Environment Topology** dialog, pick your application server (for example, **Tomcat**) and **MySQL** as the database you want to use. Switch on **Public IPv4** for **MySQL**. Then type your environment name, for example, *dumptest*.

![environment wizard](02-environment-wizard.png)

Wait just a minute for your environment to be created.

4\. Click **info** button for MySQL and you'll see your **public IP** in the end of the dropdown list.

![MySQL node public IP](03-mysql-node-public-ip.png)


## Remote Connection to MySQL

1\. Create a new open connection to start querying using any desktop client for **MySQL** (we'll use MySQL Workbench as an example). Specify the connection name, enter the host name (your Public IP), port number (3306), username and password (when you created the environment, the platform sent you an email with credentials to the database).

![remote connection credentials](04-remote-connection-credentials.png)

2\. Now MySQL remote access is configured and you can start querying.

![remote access to MySQL](05-remote-access-to-mysql.png)


## What's next?

* [Dump Import/Export to MySQL/MariaDB](/dump-import-export-to-mysql/)
* [Java Connection to MySQL/MariaDB](/connection-to-mysql/)
* [PHP Connection to MySQL/MariaDB](/connection-to-mysql-php/)