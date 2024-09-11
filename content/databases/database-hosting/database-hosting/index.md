---
draft: false
title: "Database Hosting Overview"
aliases: ["/database-hosting/", "/connection-to-couchdb/", "/percona-server-for-mongodb/", "/general-information/", "/add-database/", "/orientdb/", "/orientdb-replication/", "/cassandra/", "/neo4j/"]
seoindex: "index, follow"
seotitle: "Database Hosting Overview"
seokeywords: "database access admin credentials, cloud cassandra hosting, cloud mysql database hosting, cloud mongodb hosting, database administrator panel credentials, cloud mariadb database hosting, postgresql cloud hosting, database administrator console credentials, cloud couchdb hosting, cloud perconadb hosting, neo4j cloud hosting"
seodesc: "Learn how to create a new environment with SQL and/or NoSQL database or just add a DB node to the existing environment. Access your database administration panel via the appropriate URL to apply essential configurations required by your application."
menu:
    docs:
        title: "DB Hosting Overview"
        url: "/database-hosting/"
        weight: 10
        parent: "database-hosting"
        identifier: "database-hosting.md"
---

# Database Hosting

Platform provides a set of scalable and fully manageable database servers that you can easily install and operate with. The process of a new database creation is fairly simple and can be accomplished in just a few minutes.

1\. Open the Topology wizard through either clicking **New Environment** (to set up a new environment) or selecting the **Change environment topology** button (to add database to the already existing environment).

![new environment wizard](01-new-environment-wizard.png)

2\. Then refer to the **SQL** or **NoSQL** wizard section to select database server of the corresponding type.

![create environment with database](2.png)

Use the drop-down list to choose among the available DB management systems:

* for **SQL** - MySQL, MariaDB, PostgreSQL, PerconaDB
* for **NoSQL** - MongoDB, Couchbase, Redis, OpenSearch

{{%tip%}}**Note:** The list of available [database servers](/software-stacks-versions/#databases) can vary and depends on your hosting provider settings. If some of these servers are not available in your wizard, please, contact your hosting provider for activation.{{%/tip%}}

When the corresponding database server is created, you'll receive an email notification with credentials (*access URL*, *login* and *password*) to the database administration panel.

3\. To launch your database admin panel, click the **Open in Browser** button next to the target database node at the dashboard (or compose the admin panel URL [manually](#database-admin-panel-url)).

![access database admin panel](3.png)

In the opened page, use credentials from the email to log in and start applying configurations required by your application.

{{%tip%}}**Tip:** For containers without [Public IP](/public-ip/) address attached, the database admin console is available via *https://* by default.{{%/tip%}}

When your database server is up and ready, you can [Connect your application to DB](/database-connection-strings/).


## Database Password Reset

To **Reset password** for a database node, click the same-named button next to it at the dashboard (or for a set of [scaled DB](/horizontal-scaling/) instances to get new credentials for all of them at once).

![database password reset](4.png)

As a result, you'll receive email with a new password to access your database admin console.


## Database Admin Panel URL

The administration panel URL for DB servers should consist of the following parts:

*node{node_id}-{environment_name}.{hoster_domain}*

where

* *{node_id}* - ID of the target database container that can be located at the dashboard (e.g. *35316* for MongoDB)

![database node ID](5.png)

* *{environment-name}* - name of the environment you've added the server to (e.g. *database*)
* *{hoster_domain}* - your hosting provider domain; can be found within the last column of the appropriate table in the [Hosters Info](/paas-hosting-providers/) page

{{%tip%}}**Note:** In case your hosting provider platform has several [environment regions](/environment-regions/) to choose, the *{hoster_domain}* value for your environment can differ from the general platform's one.{{%/tip%}}

In such a way, the whole access URL for the database administration panel will be the following in our case:

*https\://node35316-database.jelastic.com*


## What's next?

* [Connection to Database](/connect-app-to-db/)
* [Database Configuration](/database-configuration-files/)
* [Scheduling DB Backups](/scheduling-backups/)
* [Connection to DB via JNDI](/connection-to-db-via-jndi/)
* [Connection to DB using Hibernate](/connect-db-hibernate/)