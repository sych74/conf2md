---
draft: false
title: "MySQL-Based Dump Import/Export"
aliases: ["/dump-import-export-to-mysql/", "/dump-import-export-mariadb/"]
seoindex: "index, follow"
seotitle: "MySQL-Based Dump Import/Export"
seokeywords: "mysql dump files, mariadb dump files, percona dump files, mysql create dump file, mariadb create dump file, percona create dump file, import dump mysql, import dump mariadb, import dump percona, export dump mysql, export dump mariadb, export dump percona"
seodesc: "Examine how to create server instance in desktop MySQL/MariaDB/Percona client and dump database to the local file. You can also easily import previously created dump to your MySQL/MariaDB/Percona database in the same way."
menu:
    docs:
        title: "Dump Import/Export"
        url: "/dump-import-export-to-mysql/"
        weight: 50
        parent: "mysql"
        identifier: "dump-import-export-to-mysql.md"
---

# Import and Export Dump Files to MySQL/MariaDB/Percona


## Dump Import

1\. Create a new server instance using any desktop client for **MySQL/MariaDB/Percona** (we use MySQL Workbench as an example).

![MySQL workbench](01-mysql-workbench.png)

2\. Specify your **host machine** (just paste your public IP into the address field) and click **Next**.

![remote host public IP](02-remote-host-public-ip.png)

3\. Set the database connection values: **IP address, port number, username** and **password** (when you created the environment, the platform sent you an email with credentials to the database).

![database connection credentials](03-database-connection-credentials.png)

4\. Then your database connection will be tested for a couple of minutes.

![testing database connection](04-testing-database-connection.png)

5\. Set the type of remote management you want to use.

![do not use remote management](05-do-not-use-remote-management.png)

6\. Enter the name for your server instance.

![server instance name](06-server-instance-name.png)

7\. You can see that your server instance is successfully created.

![database connection established](07-database-connection-established.png)

8\. Open your instance and pick **Data Import/Restore** and choose the dump you want to import.

![data import/restore](08-data-import-restore.png)

The import process can take several minutes.

![start import](09-start-import.png)

9\. Go back to the platform dashboard and open **MySQL** (**MariaDB**) in a browser. Using the credentials, which the platform sent you, sign in into admin page. Select **test**, click on **example** and you'll see your imported dump.

![phpMyAdmin imported dump ](10-phpmyadmin-imported-dump.png)


## Dump Export

1\. Open the server instance you have created earlier in your desktop client and pick **Data Export** and select database objects to export. Specify the path to the directory, in which you want to export the dump.

![data export](11-data-export.png)

2\. The export process can take several minutes, depending on the size of exported data.

![start export](12-start-export.png)

 Your dump file will be in the directory, the path to which you have specified.


## What's next?

* [Java Connection to MySQL/MariaDB](/connection-to-mysql/)
* [PHP Connection to MySQL/MariaDB](/connection-to-mysql-php/)
* [Remote Access to MySQL/MariaDB](/remote-access-mysql/)