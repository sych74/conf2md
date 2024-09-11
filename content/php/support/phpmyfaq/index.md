---
draft: false
title: "phpMyFAQ Deployment"
aliases: "/phpmyfaq/"
seoindex: "index, follow"
seotitle: "phpMyFAQ Deployment"
seokeywords: "phpmyfaq, faq system, php faq system, install phpmyfaq, phpmyfaq deployment, phpmyfaq hosting, phpmyfaq paas, phpmyfaq tutorial, phpmyfaq guide"
seodesc: "Find out how to quickly deploy phpMyFAQ - a multilingual database-driven FAQ-system - into PHP environment with MySQL database at the platform."
menu: 
    docs:
        title: "phpMyFAQ Deployment"
        url: "/phpmyfaq/"
        identifier: "phpmyfaq.md"
---

# How to Deploy phpMyFAQ

**phpMyFAQ** is a multilingual database-driven FAQ-system. It supports various databases and PHP 5.3 (or higher).

phpMyFAQ offers:

* multi-language Content Management-System (CMS) with a WYSIWYG editor and an Image Manager;
* HTML Editor;
* flexible multi-user support with user and group based permissions, templates;
* PDF support;
* Facebook and Twitter support;
* LDAP and Microsoft Active Directory support;
* Easy-to-use installation script.

It is easy to install this application into your platform. Just follow the next steps.


## Create Environment 

{{%tip%}}If you don't have an account, please register it as described in the [Getting Started](/getting-started/) document.{{%/tip%}}

1\. Log in to the platform dashboard and click **Create environment** button in the upper left corner of the dashboard.

![create environment button](01-create-environment-button.png)

2\. Choose the ***PHP*** tab. Pick **Apache** as your application server and **MySQL** as a database. Name your environment or use the default name. State the cloudlet limit for each added node. Click the **Create** button.

![phpMyFAQ environment topology](02-phpmyfaq-environment-topology.png)

Your new environment will be created in seconds. You have received two emails as well: the first one with the confirmation of the successful creation of the environment and the second one - with MySQL authorization details. 


## Configure Database

1\. Open the letter with *MySQL node successfully added* subject in your email box. Find there your **Access URL**, **Login** and **Password**.

2\. Enter the **phpMyAdmin panel** by clicking on the **Access URL**. Add your username and password (or copy them from the email).

![MySQL database log in](03-mysql-database-log-in.png)

3\. Go to the **Users** tab, create a new user (e.g. *phpmy*) with an option *Create database with same name and grant all privileges* ticked.

![database add user](04-database-add-user.png)

![create dedicated database](05-create-dedicated-database.png)


## Upload and Install Application

1\. Go to [phpMyFAQ official site](https://www.phpmyfaq.de/download) and download the latest version as **.zip** archive.

![download phpMyFAQ](06-download-phpmyfaq.png)

2\. Go to your platform dashboard and click **Upload** in the **Deployment Manager** window. Choose your local archive file and push the **Upload** button.

![upload phpMyFAQ package](07-upload-phpmyfaq-package.png)

3\. Then click the **Config** button for Apache server in your environment.

![Apache config button](08-apache-config-button.png)

4\. You can see a config manager below. Navigate to the **ROOT** folder (***/webroot/ROOT***) and create new **attachments**, **data**, and **images** folders (without capital letters).

![create folders for phpMyFAQ](09-create-folders-for-phpmyfaq.png)

5\. Open your application by clicking the **Open in Browser** button.

![open Apache in browser](10-open-apache-in-browser.png)

6\. You have reached a **phpMyFAQ Setup** page. Fill in all the needed fields here:

* **Database hostname** (without http://);
* **Database user** (the one you've created during database configuration);
* **Database password** (you've created during database configuration); 
* Your **email**.

And choose three more parameters for administrator: *Name*, *Login*, *Password*.

Press the **Click to install phpMyFAQ** button.

![phpMyFAQ configuration](11-phpmyfaq-configuration.png)

7\. You will be redirected to the Survey page. Enjoy it and click the **Click here to submit the data and finish the installation process** link.

![phpMyFAQ survey](12-phpmyfaq-survey.png)

8\. Here you can see your version of phpMyFAQ and login into your admin section.

![phpMyFAQ successfully installed](13-phpmyfaq-successfully-installed.png)

9\. Go back to your platform dashboard and open **Apache** configuration manager. Navigate to the ***/webroot/ROOT/install*** folder. Find **update.php** file there and delete it.

![delete update.php file](14-delete-updatephp-file.png)

Your application is installed into your platform. Enjoy!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [PHP Tutorials](/php-tutorials/)
* [Setting Up Environment](/setting-up-environment/)