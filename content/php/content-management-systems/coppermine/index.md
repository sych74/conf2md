---
draft: false
title: "Coppermine CMS Deployment"
aliases: "/coppermine/"
seoindex: "index, follow"
seotitle: "Coppermine CMS Deployment"
seokeywords: "coppermine, coppermine cms, coppermine deployment, coppermine guide, deploy coppermine, coppermine installation, coppermine paas, install coppermine cms, coppermine php hosting"
seodesc: "Coppermine is a specialized CMS for creating and managing photo galleries in the Internet. Deploy your own Coppermine CMS at PHP environment with the platform"
menu:
    docs:
        title: "Coppermine CMS Deployment"
        url: "/coppermine/"
        identifier: "coppermine.md"
---

# How to Install Coppermine

**Coppermine Photo Gallery** is a specialized CMS for creating and managing photo galleries in the Internet. It has been translated into dozens of languages. Powered by PHP/MySQL, Coppermine is open-source and freeware.

It is not a rocket science to get Coppermine inside your platform. Just follow the instruction.


## Create Environment

1\. Log in to the platform. If you don't have an account and don't know how to get it, please, use our [Getting Started](/getting-started/) document.

2\. Click the **Create environment** button which can be seen in the upper left corner of your platform dashboard.

![create environment](01-create-environment.png)

3\. Choose the **PHP** tab and pick up the **Apache** and **MySQL** nodes there. State the cloudlets limits for the chosen servers and name your environment (for example, *coppermine*). Now click the **Create** button.

![environment wizard](02-environment-wizard.png)

4\. Your environment has appeared in your platform dashboard with both Apache and MySQL.

![environment for Coppermine created](03-environment-for-coppermine-created.png)


## Upload the Application

1\. Go to the official [Coppermine web-site](https://coppermine-gallery.net/) and download its **.zip** archive by clicking the **Download** button.

![Coppermine download](04-coppermine-download.png)

2\. Go back to the platform dashboard. Open the **Upload archive** frame via the Deployment Manager and choose **.zip** archive you have just downloaded. Now click the **Upload** button.

![upload Coppermine](05-upload-coppermine.png)

3\. Once the package is in the platform, deploy it to the environment you have just created by clicking the **Deploy to** icon and then **Deploy** button.

![deploy Coppermine](06-deploy-coppermine.png)


## Database Configuration

1\. Open the **phpMyAdmin** panel for your database. You can reach it via the **Access URL** you've got in the email about MySQL node adding right after your environment has been created.

![database credentials email](07-database-credentials-email.png)

Or click **Open in Browser** button for MySQL server in the platform dashboard.

![open database in browser](08-open-database-in-browser.png)

2\. In the mentioned above email you can also find the **Login** and the **Password**. Use them for logging into the **phpMyAdmin** panel.

![database log in](09-database-log-in.png)

3\. Go to the **Users** tab and press **Add user** link. Create a new user (e.g. *coppermine*) with an option *Create database with same name and grant all privileges* ticked. Click the **Go** button.

![create dedicated database and user](10-create-dedicated-database-and-user.png)


## Install Coppermine

1\. Switch back to your platform dashboard and click the **Open in Browser** button for **Apache** in your environment.

![open Apache in browser](11-open-apache-in-browser.png)

2\. Click the **here** link to get the classical installation view.

![Coppermine clasic installation](12-coppermine-clasic-installation.png)

3\. In the opened window specify a **Username**, **Password** and **Email** for your administrator user.

Then fill in the following fields:

* **MySQL Host** (insert the link to your database <u>without *http://*)</u>
* **MySQL Username** and **Database name** (the one you've created during database configuring)
* **MySQL Password** (the one you've entered for the created DB user)

![Coppermine database connection](13-coppermine-database-connection.png)

Click **Let's Go!**

4\. Read the provided information and click **Let's continue!** button.

![Coppermine installation completed](14-coppermine-installation-completed.png)

That's all! For now your Coppermine is ready to work right in your platform. Congratulations!

![Coppermine gallery](15-coppermine-gallery.png)


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [PHP Tutorials](/php-tutorials/)
* [PHP Dev Center](/php-center/)