---
draft: false
title: "MongoDB Backup/Restore Add-On"
aliases: "/mongodb-backup-restore-addon/"
seoindex: "index, follow"
seotitle: "MongoDB Backup/Restore Add-On"
seokeywords: "mongo, mongodb, mongo database, mongo backups, mongo restore, mongo backup restore, backup restore addon"
seodesc: "The Backup/Restore add-on fot the MongoDB databases, allows scheduling automatic backups, perform immediate manual backups, and restore data from the Backup Storage."
menu:
    docs:
        title: "Backup/Restore Add-On"
        url: "/mongodb-backup-restore-addon/"
        weight: 50
        parent: "mongodb"
        identifier: "mongodb-backup-restore-addon.md"
---

# Database Backup/Restore Add-On

**[Database Backup](https://github.com/jelastic-jps/database-backup-addon)** add-on is compatible with all the standalone and clustered (replica set) MongoDB databases in the Virtuozzo Application Platform. It works in tandem with [Backup Storage](https://github.com/jelastic-jps/backup-storage) to help users automatically create and store database backups at the remote storage.


## Add-On Installation

Before the add-on installation, you need to create a dedicated storage instance to keep all the backup data.

1\. If you don’t have one, it can be created in a few minutes using the dedicated **Backup Storage** package in the [platform Marketplace](/marketplace/).

![marketplace backup storage](01-marketplace-backup-storage.png)

If you already have such storage, you can skip to the *fourth* step.

2\. Within the installation window, you can choose between the ***Standalone*** and ***Cluster*** storage options. Next, specify the preferred **Number of nodes** (for Cluster option) and **Storage size**. Finalize by providing the standard data:

- **Environment** – environment domain name
- **Display Name** – [environment's alias](/environment-aliases/)
- **Region** – [environment's region](/environment-regions/) (if multiple ones are available)

![backup storage installation](02-backup-storage-installation.png)

3\. Click the Install button and wait several minutes for the storage to be created. It will be automatically added to the “*Backup storage nodes*” [group](/environment-groups/).

![backup storage environment](03-backup-storage-environment.png)

{{%tip%}}**Tip:** One storage can be used by as many databases as needed.{{%/tip%}}

4\. Once the storage is ready, you can install the backup add-on. Hover over your database and click the **Add-Ons** icon.

![backup restore add-on](04-backup-restore-addon.png)

Locate the required ***Database Backup/Restore Add-On*** and click **Install**.

5\. Provide the following data:

- Choose scheduling option
  - **Pre-defined** – select from a list of standard backup intervals (hourly, daily, weekly, monthly)
  - **Custom** – choose the exact Time, required Days of the week, and Time Zone
![custom backup schedule](05-custom-backup-schedule.png)
  - **Manual (crontab)** - provide a simple [cron-based expression](https://en.wikipedia.org/wiki/Cron#Overview) (using the UTC zone) to schedule backups
![crontab backup schedule](06-crontab-backup-schedule.png)
- **Backup storage** – choose from the list of the backup storages installed on the account
- **Number of backups** – set the number of the newest backups to keep for the current database
- **Database User** and **Database Password** – provide user credentials to access the database

![backup restore add-on installation](07-backup-restore-addon-installation.png)

6\. In a minute, you’ll see the installation success pop-up.

![add-on installed](08-addon-installed.png)

Your backup add-on is already working. Just wait for the specified time for backups to be created or trigger it manually (see the section below).


## Managing Add-On

After the installation, the add-on gives you the options to:

- **Backup Now** – creates an immediate backup
- **Configure** – adjusts parameters specified during the creation (schedule, storage node, quantity of backups, user credentials)
- **Restore** – restores from backup
- **Uninstall** – removes the backup add-on

![managing add-on](09-managing-addon.png)

*<u>During the backup process,</u>* a snapshot of the database is created using the standard ***mongodump*** utility. It is stored on the *Backup Storage* under the dedicated folder (named based on the backed-up database) and uses a distinct name (execution timestamp). Such a structure helps keep backups organized, especially when working with multiple databases.

*<u>During the restore process,</u>* the corresponding directory on the storage server is mounted to the master node of the target database. Next, the SQL dump from the required backup snapshot is restored (using the standard ***mongorestore*** utility) and applied to the database.

{{%note%}}**Note:** Take into consideration that all the operations are performed on the database ***layer’s master node*** only. So, *for the non-clustered databases with multiple nodes*, the data will be restored on one node only.{{%/note%}}


## Restoring Database

*Database restoration from the backup overrides all the existing data. Any recent changes that were made since the backup creation will be permanently lost.*

In order to restore a database from a backup, you need to select the **Restore** option for the add-on. A dialogue window with the following options will be opened:

- **Restore from** – choose the target environment (multiple options may be available if the backup add-on is used on several environments)
- **Backup** – select from a list of backups for the selected environment (names contain timestamps for quick identification)

![restore from backup](10-restore-from-backup.png)

Click **Restore** and confirm via pop-up. Once initiated, the action cannot be canceled or reverted. You'll see the success notification in the dashboard after the process completion.


## What's next?

- [MongoDB Auto-Clustering](/mongodb-auto-clustering/)
- [Upgrading to MongoDB 6/7](/updating-to-mongodb-7/)
- [MongoDB License Pricing](/mongodb-license/)
- [MongoDB Encryption in Transit Add-On](/mongodb-ssl-addon/)
- [MongoDB Remote Access](/remote-access-to-mongodb/)
- [MongoDB Dump Import/Export](/dump-import-export-to-mongodb/)