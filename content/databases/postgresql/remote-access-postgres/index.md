---
draft: false
title: "Remote Access to PostgreSQL"
aliases: "/remote-access-postgres/"
seoindex: "index, follow"
seotitle: "Remote Access to PostgreSQL"
seokeywords: "postgresql remote access, access to postgresql, access postgresql database, remote access to postgresql, postgresql access database, postgresql database access, access postgresql server, postgresql server remote access, access a postgresql database"
seodesc: "See how to configure the remote access to your PostgreSQL database node from your computer just in a few steps. As an example of desktop client we use SQL Manager for PostgreSQL database."
menu:
    docs:
        title: "Remote Access to PostgreSQL"
        url: "/remote-access-postgres/"
        weight: 40
        parent: "postgresql"
        identifier: "remote-access-postgres.md"
---

# Remote Access to PostgreSQL

You have an opportunity to work with your databases remotely from your computer without having to login to our dashboard. Here's a how-to for PostgreSQL users.


## Create Environment

The database can be accessed either via [public IP](/public-ip/) or [endpoints](/endpoints/) (no public IP required). Let's take a look at both options of creating database environment.

### Environment with Public IP

1\. Log into the platform.

2\. Click the **New Environment** button at the top left of the dashboard.

![create new environment button](01-create-new-environment-button.png)

3\. In the **Environment Topology** wizard pick **PostgreSQL** as the database you want to use. In case you want to get a database cluster just slide to the right the Auto-Clustering switch. Then add a **Public IPv4**. After that enter an environment name, for example, ***remotepostgres***, and click **Create** button.

![wizard PostgreSQL auto-clustering](02-wizard-postgresql-auto-clustering.png)

It can take about a minute for creating your environment.

![environment created](03-environment-created.png)

Both nodes have the public IP addresses attached to.

### Environment without Public IP

The algorithm is the same as above and clustered database environment will be created but with no public IP attached.

![environment without public IP](04-environment-without-public-ip.png)

Once the environment is ready, go to the **Endpoints** at the **Settings** section and click on **Add** to create new port mapping.

![add endpoint](05-add-endpoint.png)

Choose the **Node** you need to access and PostgreSQL service **Name**. The rest parameters will be generated automatically: **Private Port**, **Protocol**, **Public Port**, and **Access URL**.

![endpoints dialog](06-endpoints-dialog.png)

A port mapping to the database master node may look like this.

![endpoint added](07-endpoint-added.png)

If necessary do the same for the Slave node of the database cluster.


## Remote Connection to PostgreSQL

Let's create a new connection to the database using any desktop or web client. Here we use the **pgAdmin4** which is the most popular and feature-rich Open Source administration and development platform for PostgreSQL. You can get client software that meets your platform. See the download page to get the proper link ([https://www.pgadmin.org/download/](https://www.pgadmin.org/download/)) or you may get familiar with this application in the platform by deploying it via [import](/environment-import/) of corresponding pgAdmin4 [manifest](https://github.com/jelastic-jps/pgadmin/blob/master/manifest.yaml).

![pgAdmin panel](08-pgadmin-panel.png)

1\. If you have a database cluster it will be more convenient to create a group of all servers that belong to the cluster.

![create server group](09-create-server-group.png)

2\. Then enter Name of the group e.g. ***remotepostgres***.

![server group name](10-server-group-name.png)

3\. After that add one by one all of the database servers to the group. Let's see how to do that for the Master database. Make a right-click on the group (e.g. *remotepostgres*) and choose **Create > Server**.

![add server](11-add-server.png)

4\. Enter the server name (e.g. **Master** for the primary database of your cluster) at the **General** tab.

![create server dialog](12-create-server-dialog.png)

5\. At this step you have to specify server access settings depending on whether you created database with or without public IP as described above.

### Connection to Public IP

Go to the Connection tab and enter public IP of your master database at the **Host name/address** field. Specify **Username** and **Password** you have obtained while creating the database environment via email.

![server connection public ip](13-server-connection-public-ip.png)

### Connection via Endpoints

Take the **URL** and **Public Port** from generated port mapping and set the database server connection settings. The **Username** and **Password** are the same as described above.

![server connection endpoint](14-server-connection-endpoint.png)

6\. You may change other specific options if you are rather confident in your actions.

7\. Finally, press the **Save** to apply the changes and you will see that connection is successfully established.

As for our example, both master and slave databases are displayed as follows:

![check connection](15-check-connection.png)

Now PostgreSQL remote access is configured and you can start querying.

## What's next?

* [Java Connection to PostgreSQL](https://www.virtuozzo.com/company/blog/java-connection-to-postgresql/)
* [PHP Connection to PostgreSQL](/connection-to-postgresql-for-php/)
* [PostgreSQL Replication](/postgresql-database-replication/)
* [Dump Import/Export to PostgreSQL](/dump-postgres/)