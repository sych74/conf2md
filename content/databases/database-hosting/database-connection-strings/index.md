---
draft: false
title: "Database Connection Strings"
aliases: ["/database-connection-strings/", "/database-connection/", "/connect-app-to-db/"]
seoindex: "index, follow"
seotitle: "Connecting Database to Application"
seokeywords: "database connection string in php, connect to mysql database, connect to mysql database java, connect to mongodb database, connect to database java peculiarities, connect to postgresql database, connect to mariadb database, connect to cassandra database, postgresql connection string, couchdb connect to database, mongodb connection string, connect to neo4j database, connect to perconadb, couchdb connection string, mariadb connection string "
seodesc: "Learn how to establish connection between your database (MariaDB, PostgreSQL, MySQL, MongoDB, CouchDB, etc.) and deployed application. Explore connection peculiarities inherent to Java and PHP powered application. "
menu: 
    docs:
        title: "Database Connection Strings"
        url: "/database-connection-strings/"
        weight: 40
        parent: "database-hosting"
        identifier: "database-connection-stringx.md"
---

# Database Connection Strings

All instances, created inside the platform, are operated as independent containers. To establish connection to a database from the application, deployed within application server, you need to set a connection string for it, using either:

* [CNAME](/database-hosting/#database-admin-panel-url) of database, e.g. *node{node_id}-{environment_name}.{hoster_domain}*
* Private IP address
* [Public IP](/public-ip/) address (if attached)

{{%note%}}**Note:** Specifying *localhost* within a connection string will not work for establishing connection between application and database.{{%/note%}}

Depending on the engine that powers your environment, refer to one of the sections below:

* [Java](#database-connection-for-java-apps)
* [PHP](#database-connection-for-php-apps)


## Database Connection for Java Apps

Look through the table of database types to find the appropriate DB connection code for your application:

{{%tablecols1to3%}}
|DB Type|Connection code|
|---|---|
|[MySQL](/connection-to-mysql)/[MariaDB](/connection-to-mariadb)|*String URL = "jdbc:mysql://node{node_id}-{environment_name}.{hoster_domain}/{dbname}";DriverManager.getConnection(URL, user_name,user_password);*|
|MySQL [Auto-Cluster](/auto-clustering)|*Highly available connection via the scaled dedicated ProxySQL load balancers.<br> String URL = "jdbc:mysql://proxy.{environment_name} .{hoster_domain}:3306/{dbname}"; DriverManager.getConnection(URL, user_name,user_password);*|
|MariaDB [Auto-Cluster](/auto-clustering)|<i>Highly available connection via the scaled dedicated ProxySQL load balancers.<br> String URL = "jdbc:mariadb://proxy.{environment_name} .{hoster_domain}:3306/{dbname}**?usePipelineAuth=false**"; DriverManager.getConnection(URL, user_name,user_password);</i>|
|[PostgreSQL](/connection-to-postgresql)|<i>String URL = "jdbc:postgresql://node{node_id}-{environment_name}.{hoster_domain}/{dbname}**"**; DriverManager.getConnection(URL, user_name,user_password);</i>|
|[MongoDB](/connection-to-mongodb)|*Mongo m = new Mongo(node{node_id}-{environment_name}.{hoster_domain});  DB db = m.getDB ({database_name});  if(db.authenticate(user_name,user_password.toCharArray())) { System.out.println("Connected!");  }*|
{{%/tablecols1to3%}}

For the UTF-8 encoding, modify your connection string according to this:

*"jdbc:{dbtype}://{dbtype}{node_id}-{environment_name}.{hoster_domain}/{dbname}?useUnicode=yes&characterEncoding=UTF-8"*

{{%tip%}}**Tip:** Your hosting provider domain can be found within the last column of the appropriate table in the [Hosters Info](/paas-hosting-providers/) page.

In case your hosting provider platform has several [environment regions](/environment-regions) to choose, the *{hoster_domain}* value for your environment can differ from the general platform's one.{{%/tip%}}


## Database Connection for PHP Apps

Based on the used DB type, check out the connection code examples below and adjust your application appropriately:

{{%tablecols1to3%}}
|DB Type|Connection code|
|---|---|
|[MySQL and MariaDB](/connection-to-mysql-php)|*mysql_connect('HOST', 'USERNAME', 'PASSWORD')*|
|[MongoDB](/connection-to-mongodb-for-php)|*Mongo("hostaddress", array("username" =&gt; "username", "password" =&gt; "password"))*|
|[PostgreSQL](/connection-to-postgresql-for-php)|*pg_connect("host=host_address port=5432 dbname=postgres user=webadmin password=password")*|
{{%/tablecols1to3%}}

{{%tip%}}**Note:** It is required to specify the host string without *http://*. The appropriate address and credentials are located in the email you've received upon database creation.{{%/tip%}}


## What's next?

* [Create DB Server](/database-hosting/)
* [Database Configuration](/database-configuration-files/)
* [Scheduling DB Backups](/scheduling-backups/)
* [Connection to DB via JNDI](/connection-to-db-via-jndi/)
* [Connection to DB using Hibernate](/connect-db-hibernate/)