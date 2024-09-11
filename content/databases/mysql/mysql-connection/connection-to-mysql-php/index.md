---
draft: false
title: "PHP Connection to MySQL/MariaDB/Percona"
aliases: ["/connection-to-mysql-php/", "/connection-to-mysql-php-5-3/", "/connection-to-mariadb-php/", "/mariadb-php-connection/"]
seoindex: "index, follow"
seotitle: "PHP Connection to MySQL/MariaDB/Percona"
seokeywords: "mysql, mariadb, php, install mysql, login phpmyadmin, phpmyadmin, mysql connection string, start mysql, php connection mariadb example, php connection mysqli, configure php connection mariadb"
seodesc: "Find out the detailed instruction on how to connect to MySQL/MariaDB databases from your application, deployed to PHP-based application server in the platform."
menu:
    docs:
        title: "PHP Connection"
        url: "/connection-to-mysql-php/"
        weight: 20
        parent: "mysql-connection"
        identifier: "connection-to-mysql-php.md"
---

# Connection to MySQL/MariaDB/Percona for PHP

**MySQL**, **MariaDB**, and **Percona** are highly popular open source databases, used by developers all over the world. Follow the instruction below to learn how to connect your PHP application, hosted within the platform, to one of these DB servers:

* [create environment](#environment-creation)
* [connect to database](#connection-to-database)
* [check connection](#checking-connection)
* [execute request](#executing-simple-request)
* [additional configurations](#useful-to-know)


## Environment Creation

1\. Log into your PaaS account and [create an environment](/setting-up-environment/) with **MySQL** or **MariaDB** database server (both are available within the ***SQL*** wizard section).

![create PHP MySQL environment](01-create-php-mysql-environment.png)

In order to provide a connection example, we've added **Apache PHP** application server.

2\. After environment creation, you'll get an email with the MySQL (or MariaDB) administration and connection details:

![email MySQL connection details](02-email-mysql-connection.png)

3\. Return to your dashboard and click the **Open in Browser** button for the appropriate database node (either MySQL or MariaDB).

![MySQL node open in browser button](03-mysql-node-open-in-browser-button.png)

Log into the opened admin panel using credentials you've received in the above-mentioned email.

4\. Go to the ***Databases*** tab and **Create** a new database (e.g., *mysqldb*).

![MySQL create new database](04-mysql-create-new-database.png)

Now, you can [deploy](/deployment-guide/) your application (either from *archive* or *GIT/SVN repository*) to the created environment.


## Connection to Database

Once your project is successfully deployed, you need to connect it to your database. For that, your application should be appropriately configured, for example using the inbuilt [MySQLi](http://php.net/manual/en/book.mysqli.php) (MySQL Improved) extension.

Refer to the linked official documentation page for the full list of available functions, while we'll overview just the basic ones below:

1\. To get a connection string for accessing your MySQL/MariaDB node:

```bash
mysqli_connect('{host}', '{user}', '{password}', '{db_name}');
```

The appropriate placeholders should be substituted with your connection data from the MySQL or MariaDB node:

* ***{host}*** - link to your DB node without protocol part
* ***{user}*** and ***{password}*** - database admin credentials (for production usage, it's recommended to create a dedicated account with the appropriate permissions)
* ***{db_name}*** - name of required database (e.g. the previously created *mysqldb* one)

2\. For switching to different database within the same server, use the next function:

```bash
mysql_select_db('{connect}','{db_name}');
```

Here, the ***{connect}*** should be substituted with the connection string obtained using the above-described *mysqli_connect* function.

3\. In order to close a connection to your database, execute the following:

```bash
mysqli_close( );
```

{{%note%}}**Note:** You need to specify the necessary functions in every **\*.php** page, which should be connected to the database<a id="check-connection"></a>.{{%/note%}}


## Checking Connection

In order to ensure everything works fine, you can check the connection using this code:

```php
<?php
$link = mysqli_connect('{host}', '{user}', '{password}', '{db_name}');
//if connection is not successful you will see text error
if (!$link) {
       die('Could not connect: ' . mysql_error());
}
//if connection is successfully you will see message below
echo 'Connected successfully';

mysqli_close($link);
?>
```

{{%note%}}**Note:** Do not forget to substitute ***{host}***, ***{user}***, ***{password}*** and ***{db_name}*** in the connection string with the corresponding values (as it is described in the [Connection to Database](#connection-to-database) section).{{%/note%}}

If everything is OK, you'll get the following message, when this page is opened in browser.

![MySQL database connected](05-mysql-database-connected.png)


## Executing Simple Request

And here is an example on how to execute a simple request to your database and output it onto a table.

The plain PHP script below will establish a connection to your database server (do not forget to specify the appropriate hostname and credentials), connect to the default *mysql* database it contains, read the values from the *help_topic* table and display them in a self-generated table.

```php
<?php
// Connection checking:
$link = mysqli_connect('{host}', '{user}', '{password}', '{db_name}');
if (!$link)
{
    echo "<h2>MySQL Error!</h2>";
    exit;
}

// Switch to a different database:
$db="mysql";
mysqli_select_db($link, $db);
// table header output:
echo "<table border=\"1\" width=\"100%\" bgcolor=\"#FFFFE1\">";
echo "<tr><td>Value1</td><td>Value2</td><td>Value3</td>";
// SQL-request:
$q = mysqli_query ($link, "SELECT * FROM help_topic;");
// table-result output
for ($c=0; $c<mysqli_num_rows($q); $c++)
{
    echo "<tr>";
    $f = mysqli_fetch_array($q); // Returns an array that corresponds to the fetched row and moves the internal data pointer ahead.
    echo "<td>$f[0]</td><td>$f[1]</td><td>$f[5]</td>";
    echo "</tr>";
}
echo "</table>";
?>
```

As a result, you'll receive a kind of index for all available MySQL functions with links to the instructions on their using.

![database connection example applicatiom](06-database-connection-example-applicatiom.png)

Great! Now you can easily connect your PHP application to the **MySQL** or **MariaDB** database.


## Useful to Know

The platform also lets you extend your MySQL/MariaDB servers functionality by following the appropriate instructions in our documentation:

* set up the preferred database replication type - [primary-secondary](/database-primary-secondary-replication/) or [primary-primary](/multi-primary-replication/) - in order to get the increased DB performance and data loss protection
* adjust [Backups Scheduling](/database-backups/) for ensuring safety of the information inside your DBs in the case of unexpected server failure
* see the [Remote Access](/remote-access-mysql/) instruction and learn how to access your database remotely via the preferred desktop MySQL client
* use the [Dump Files Import/Export](/dump-import-export-to-mysql/) guide to find out how to manually backup and restore your data from the previously created dumps


## What's next?

* [MySQL/MariaDB Primary-Secondary Replication](/database-primary-secondary-replication/)
* [Remote Access to MySQL/MariaDB](/remote-access-mysql/)
* [Database Backups](/database-backups/)
* [Database Configuration](/database-configuration-files/)