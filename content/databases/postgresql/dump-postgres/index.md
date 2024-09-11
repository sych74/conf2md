---
draft: false
title: "PostgreSQL Dump Import/Export"
aliases: "/dump-postgres/"
seoindex: "index, follow"
seotitle: "PostgreSQL Dump Import/Export"
seokeywords: "postgresql dump files, postgresql dump database to file, dump postgres database to file, dump file postgresql, postgresql database dump to file, import dump postgresql, export dump postgresql, import postgresql, export postgresql, dump postgresql"
seodesc: "Use this step-by-step instruction to learn how to dump your PostgreSQL database to the local file, as well as how to import previously created dump to the PostgreSQL server in your environment. "
menu:
    docs:
        title: "Dump Import/Export to PostgreSQL"
        url: "/dump-postgres/"
        weight: 50
        parent: "postgresql"
        identifier: "dump-postgres.md"
---

# Import and Export Dump Files to PostgreSQL

Create two database environments and connect to them using any desktop client (we use *pgAdmin4* as an example. Learn more in our [tutorial](/remote-access-postgres)).

![create two postgresql databases](two-postgresql-databases.png)
## Dump export from PostgreSQL

1. We put environments **remotepostgres.vip.jelastic.cloud** and **destination.vip.jelastic.cloud** to the respective server groups **backupsource** and **destination** at the *pgAdmin4* application.

![pgadmin server groups](pgadmin-server-groups.png)

2. Make a right-click on the required database to be backed up e.g. **Jelastic** and choose **Backup**.

![backup required database](backup-required-database.png)

3. Specify your dump file name and the format of the output file. E.g. **mybackup** and **Tar** file format respectively.

![backup dialog general](backup-dialog-general.png)

4. Click on the **Dump options** tab and select backup options for database objects.

![backup dialog dump options](backup-dialog-dump-options.png)

5. Finally, click the **Backup** button. The successful window should appear.

![successful backup](successful-backup.png)
Your dump file will be stored in the user home directory or by the path to which you have specified at the host the *pgAdmin4* is running on.

## Dump import to PostgreSQL

1. Create an empty database at the destination server.

![create new database](create-new-database.png)

2. Set the name in the field **Database** either the same e.g. **Jelastic** or any arbitrary name.

![create database dialog](crate-database-dialog.png)

3. To perform dump import to PostgreSQL database make the right-click on the new database and choose **Restore**.

![restore database](restore-database.png)

4. Select the file format used during the database backup operation. As for our example, we used **tar** format. Specify the name of the backup file or use file open dialogue at the right of the **Filename** field to choose the necessary file.

![restore dialog general](restore-dialog-general.png)

5. Set advanced restoring options if needed.

![restore dialog options](restore-dialog-options.png)

6. Finally, click on the **Restore** button.
7. Navigate back to the **Jelastic** database at the **destination** server group and make sure that the database was restored properly with its content at both servers **Master** and **Slave**.

![ensure database restored and replicated](ensure-database-restored-and-replicated.png)

That's all! Hope this how-to was useful for you.

## What's next?

* [Remote Access to PostgreSQL](/remote-access-postgres)
* [Java Connection to PostgreSQL](/connection-to-postgresql)
* [PHP Connection to PostgreSQL](/connection-to-postgresql-for-php)
* [PostgreSQL Replication](/postgresql-database-replication)