---
draft: false
title: "MongoDB License Pricing"
aliases: "/mongodb-license/"
seoindex: "index, follow"
seotitle: "MongoDB License Pricing"
seokeywords: "mongo, mongodb, mongo database, mongo license, mongo pricing, mongo license pricing"
seodesc: "Learn about the license fee for using MongoDB stacks. Check the MongoDB license price directly in the topology wizard."
menu:
    docs:
        title: "MongoDB License Pricing"
        url: "/mongodb-license/"
        weight: 40
        parent: "mongodb"
        identifier: "mongodb-license.md"
---

# MongoDB License Pricing

{{%note%}}The availability of the **latest MongoDB versions** depends on the service hosting provider - check the list of [supported platforms](https://www.virtuozzo.com/application-platform-partners/?featuresSupport=MDB).{{%/note%}}

Historically, Virtuozzo Application Platform provided MongoDB software stack as a certified container without any additional charges. However, due to the license changes, MongoDB versions newer than **3.6.8** and **4.0.2** cannot be distributed freely and require additional agreement.

If you want to use the latest versions of MongoDB with the Virtuozzo Application Platform, an additional **license fee** will be automatically applied. The exact amount can vary for different hosting providers, but you can always check the price via the [topology wizard](/setting-up-environment/) (both before the installation and for the existing environments). Once the environment topology is set up, choose the *hourly/dayly/monthly* estimated cost period, and hover over the price in the right part of the wizard:

{{%tip%}}**Tip:** The Virtuozzo Application Platform provides a **[MongoDB Sandbox](/mongodb-sandbox/)** image for testing purposes. It is offered license-free but includes some restrictions compared to the production version.{{%/tip%}}

![license cost in wizard](01-license-cost-in-wizard.png)

The MongoDB license price corelates to the number of dynamic cloudlets (scaling limit) provided for the MongoDB nodes.

*<u>For example,</u>* for replica set with 3 nodes with 32 cloudlets each and the license cost of 10$/month for 8 cloudlets (equivalent to per 1 GB of RAM):

- 3 \* 32 = **96** (total cloudlets limit for MongoDB)

![mongodb nodes cloudlets](02-mongodb-nodes-cloudlets.png)

- 10 / 8 = **1.25** (license cost for a single cloudlet of resources)
- 96 \* 1.25 = **120** (total license cost)

![03-total license cost](03-total-license-cost.png)


## What's next?

- [MongoDB Auto-Clustering](/mongodb-auto-clustering/)
- [Upgrading to MongoDB 6/7](/updating-to-mongodb-7/)
- [MongoDB Backup/Restore Add-On](/mongodb-backup-restore-addon/)
- [MongoDB Encryption in Transit Add-On](/mongodb-ssl-addon/)
- [MongoDB Remote Access](/remote-access-to-mongodb/)
- [MongoDB Dump Import/Export](/dump-import-export-to-mongodb/)