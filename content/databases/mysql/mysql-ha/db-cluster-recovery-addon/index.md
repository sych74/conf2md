---
draft: false
title: "Database Cluster Recovery"
aliases: "/db-cluster-recovery-addon/"
seoindex: "index, follow"
seotitle: "Cluster Recovery Add-On"
seokeywords: "database recovery, db cluster recovery, recovery addon, database cluster diagnostic, restore database cluster, galera recovery, mysql recovery addon, mariadb cluster recovery"
seodesc: "The Database Cluster Recovery add-on can provide diagnostic and restore operability of the Primary-Secondary, Primary-Primary, and Galera database clusters."
menu:
    docs:
        title: "Cluster Recovery Add-On"
        url: "/db-cluster-recovery-addon/"
        weight: 50
        parent: "mysql-ha"
        identifier: "db-cluster-recovery-addon.md"
---

# Database Cluster Recovery Add-On

The platform has several popular out-of-box clustering options for the MariaDB/MySQL databases, which can be automatically implemented via the [auto-clustering](/auto-clustering/) feature. Such database clusters offer an advanced high availability and auto-scalability while remaining accessible to any user through automation.

In order to make the solution even more alluring, the platform offers a free diagnostic and recovery add-on to help with database maintenance. Currently, the **Database Cluster Recovery** add-on supports the following database clusters:

- **Primary-Secondary Cluster** based on the MySQL/MariaDB/Percona stacks
- **Primary-Primary Cluster** based on the MySQL/MariaDB/Percona stacks
- **Galera Cluster** based on the MariaDB stack
- **XtraDB Cluster** based on the Percona stack


## Add-On Specifics

The **Database Cluster Recovery** add-on can operate in the *diagnostic* and *recovery* modes. The first one scans the database to identify if there are any problems, and the second tries to resolve the issue based on the obtained information.

During diagnostic, the add-on checks the following:
- replication for the Primary-Secondary and Primary-Primary topologies
- the cluster size for Galera/XtraDB clusters
- Galera/XtraDB clusters status
- cluster services status

In order to perform the required recovery operations, the add-on applies the following adjustments to the database cluster during the installation:

A *replica* user is added to perform the validation of the clusters. Also, this user is used in the ProxySQL configuration. The credentials can be viewed via the dedicated [environment variables](/environment-variables/):

- **REPLICA_USER:** repl-xxxxxx
- **REPLICA_PSWD:** xxxxxxxxxxxx

![replica user credentials](01-replica-user-credentials.png)

Also, SSH access is configured between the database nodes (with the dedicated set of SSH keys) to allow data coping with *rsync* during the restoration procedure.


## Add-On Installation

The add-on is available via the platform Marketplace. Alternatively, you can import the appropriate ***[Database Cluster Recovery](https://github.com/jelastic-jps/mysql-cluster/tree/master/addons/recovery)*** package from GitHub.

![database recovery add-on](02-database-recovery-addon.png)

In the opened confirmation window, provide the required data:

- **User** and **Password** - the database admin user credentials
- **Environment name** - select an environment with the required database cluster from the list
- **Nodes** - choose a layer with the database cluster

![recovery add-on installation](03-recovery-addon-installation.png)

Click **Install** and wait a few minutes for the add-on to be installed. It will appear in the list of add-ons of the appropriate layer.

![recovery add-on actions](04-recovery-addon-actions.png)


## Add-On Usage

The add-on can perform two actions that can be executed by clicking the appropriate buttons:

- ***Cluster Diagnostic*** - detects problems with the database cluster (scans if nodes are accessible and databases are consistent)
- ***Cluster Recovery*** - tries resolving common problems to restore cluster operability

The result of the ***Cluster Diagnostic*** action can be either “*Cluster is OK*” or “*Errors discovered*” dashboard notification.

![recovery add-on diagnostic errors](05-recovery-addon-diagnostic-errors.png)

For extended details, you can click the **Show Logs** button to open the ***/var/log/db_recovery.log*** file:

![recovery add-on logs](06-recovery-addon-logs.png)

In case some problems are discovered, you can try to resolve them automatically with the ***Cluster Recovery*** action. It should handle most of the issues and fully restore cluster operability:

{{%note%}}**Note:** We recommend [making a backup](/database-backups/) of the database before the recovery.{{%/note%}}

![successful recovery](07-successful-recovery.png)

For additional details or in case of recovery failure, you can check the ***db_recovery*** [log](/view-log-files/) mentioned above. Also, check the **[Manual Recovery](https://github.com/jelastic-jps/mysql-cluster/blob/master/addons/recovery/docs/ManualRecoveryGuide.md#configuration-file-restoration)** guide if the problem is not resolved.


## What's next?

- [Create DB Server](/database-hosting/)
- [Database Backups](/database-backups/)
- [Galera Cluster Recovery](/galera-recovery/)