---
draft: false
title: "ownCloud Deployment"
aliases: "/owncloud/"
seoindex: "index, follow"
seotitle: "ownCloud Deployment"
seokeywords: "owncloud, owncloud storage, owncloud php, install owncloud, owncloud deployment, owncloud storage hosting, owncloud paas, owncloud tutorial, owncloud storage guide"
seodesc: "You can deploy the ownCloud file storage within minutes using one-click install option or by following the manual installation guide."
menu: 
    docs:
        title: "ownCloud Deployment"
        url: "/owncloud/"
        identifier: "owncloud.md"
---

# How to Deploy ownCloud

You can have a **ownCloud** instance up and running within minutes using one-click install option.

<div data-app="owncloud" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app"></div>

The process is simple - just click **Get it hosted now**, type your email and install ownCloud in a minute skipping the steps of manual installation.

Find the full list of applications available for one-click installation at our [Marketplace page](https://www.virtuozzo.com/application-platform/marketplace/).


## Manual ownCloud Installation

**ownCloud** represents an open source and free file cloud storage. It can be easily used for data sharing and synchronization, as well as just for storing documents.

So, follow the next instruction to get your **ownCloud storage** hosted with PaaS PHP cloud. 

### Create Environment

1\. Log in to the platform using PaaS account.

2\. Press **Create environment** button in order to open the environment topology wizard.

![create environement](01-create-environment.png)

3\. Navigate to the **PHP** tab, pick up the application server (e.g. **Apache**) and database node (e.g. **MySQL**) you would like to use.

![ownCloud environment topology](02-owncloud-environment-topology.png)


### Upload and Deploy Application

1\. Open the official ownCloud [web-site](https://owncloud.com/download-server/) and press the **Tar or Zip File** button in order to get the latest ownCloud version. 

![ownCloud package](03-owncloud-package.png)

2\. In the appeared window choose **.tar.bz2** or **.zip** archive in the first line. Press the appropriate link to start downloading.

![download ownCloud archive](04-download-owncloud-archive.png)

3\. Navigate back to the platform dashboard and upload the ownCloud archive within **Deployment Manager**.

![upload ownCloud archive](05-upload-owncloud-archive.png)

4\. Find the uploaded archive in the list of the application packages and deploy it to the necessary environment.

![deploy ownCloud application](06-deploy-owncloud-application.png)

### Database Configurations

1\. Check your email inbox and find the letter with MySQL credentials. Open the phpMyAdmin panel for MySQL (**Open in Browser** button next to the db node) and log in using them.

![phpMyAdmin log in](07-phpmyadmin-log-in.png)

2\. Create a new user and database with the same names. Specify the password for a new user.

![add MySQL user](08-add-mysql-user.png)

![MySQL ownCloud database](09-mysql-owncloud-database.png)

### ownCloud Installation

1\. Press **Open in Browser** button for your environment.

![open ownCloud in browser](10-open-owncloud-in-browser.png)

2\. In the opened window create the administrator account by specifying the desired **username** and **password**. Then expand the **Advanced** settings.

![ownCloud database settings](11-owncloud-database-settings.png)

3\. Using the appeared fields you can edit the path to your data directory and specify your database server information (**MySQL** in our case):

* **Database user**: the one you've created while db configuration
* **Database password**: the one you've specified while db configuration
* **Database name**: the same as the db user
* **Host**: the host of your db 

In order to get your MySQL server string URL or host number, navigate back to the platform dashboard and press the rightmost button for MySQL node. Choose the **Info** option and in the appeared window copy the circled below string or host number and enter it to the localhost field.

![MySQL node info](12-mysql-node-info.png)

![MySQL connection string](13-mysql-connection-string.png)

4\. Eventually, press the **Finish Setup** button.

Congrats! Now you can use your personal ownCloud storage hosted at PaaS.

![ownCloud hosting](14-owncloud-hosting.png)


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [PHP Tutorials](/php-tutorials/)
* [Setting Up Environment](/setting-up-environment/)

<script>
    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.async = true;
        js.src = "//go.jelastic.com/widgets.js";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'jelastic-jssdk'));
</script>
