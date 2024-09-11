---
draft: false
title: "MongoDB Dump Import/Export"
aliases: "/dump-import-export-to-mongodb/"
seoindex: "index, follow"
seotitle: "MongoDB Dump Import/Export"
seokeywords: "mongodb dump files, mongodb dump database to file, dump mongodb database to file, dump file mongodb, mongodb database dump to file, import dump mongodb, export dump mongodb, import mongodb, export mongodb, dump mongodb"
seodesc: "Find out the two ways to dump MongoDB database to the local file and import previously created dump to the MondoDB: using any MongoDB client or using RockMongo."
menu:
    docs:
        title: "Dump Import/Export"
        url: "/dump-import-export-to-mongodb/"
        weight: 80
        parent: "mongodb"
        identifier: "dump-import-export-to-mongodb.md"
---

# Import and Export Dump Files to MongoDB

You can import and export dump files to MongoDB in two ways:

* [using any **MongoDB client**](#mongodb-client-database-master)
* [using **RockMongo** administration GUI tool](#rockmongo-admin-panel)

{{%tip%}}**Note:** If you would like to use MongoDB client, you need to have **[public IP](/public-ip/)** feature enabled in your MongoDB node.{{%/tip%}}


## MongoDB Client (Database Master)

### Dump Import to MongoDB

1\. After remote connection to **MongoDB** click on **Import** in the desktop client (we use *Database Master 4* as an example) and select the type of file you want to import.

![Database Master file import](01-database-master-file-import.jpg)

2\. Browse **XML/Csv** file, you want to import. Then browse a log file.

![browse XML and log file](02-browse-xml-and-log-file.jpg)

3\. Merge source tables to the target tables.

![merge source and target tables](03-merge-source-target-tables.jpg)

![XML import success](04-xml-import-success.png)

4\. Now you can go back to the platform's dashboard, open MongoDB in a web browser and find imported dumps in the **test** directory.

![check imported dump](05-check-imported-dump.jpg)

### Dump Export from MongoDB

1\. Click **Export > Data Export**.

![Database Master data export](06-database-master-data-export.jpg)

2\. Browse a target folder and select tables to export.

![select tables for export](07-select-tables-for-export.jpg)

3\. Select data export options and click **Finish**.

![data export options](08-data-export-options.png)

4\. Data export is successfully finished. You can check your target folder to ensure that everything is ok.

![data export success](09-data-export-success.png)


## RockMongo Admin Panel

1\. Click **Open in Browser** button for MongoDB node in your enviroment:

![open MongoDB in browser](10-open-mongodb-in-browser.png)

2\. In the opened window you'll be requested to log in with your credentials, which you've received within email after creating MongoDB node.

3\. To **Export** or **Import** dump files use the corresponding buttons:

![RockMongo import export](11-rockmongo-import-export.png)

Hope this instruction will be useful for you.


## What's next?

- [MongoDB Auto-Clustering](/mongodb-auto-clustering/)
- [Upgrading to MongoDB 6/7](/updating-to-mongodb-7/)
- [MongoDB License Pricing](/mongodb-license/)
- [MongoDB Backup/Restore Add-On](/mongodb-backup-restore-addon/)
- [MongoDB Encryption in Transit Add-On](/mongodb-ssl-addon/)
- [MongoDB Remote Access](/remote-access-to-mongodb/)