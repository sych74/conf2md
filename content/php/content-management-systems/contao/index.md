---
draft: false
title: "Contao CMS Deployment"
aliases: "/contao/"
seoindex: "index, follow"
seotitle: "Contao CMS Deployment"
seokeywords: "contao, contao cms, contao deployment, contao guide, deploy contao, contao installation, contao paas, install contao cms, contao php hosting"
seodesc: "Contao is an open-source content management system (CMS). Follow the instructions in this guide to host your own Contao CMS at the platform."
menu:
    docs:
        title: "Contao CMS Deployment"
        url: "/contao/"
        identifier: "contao.md"
---

# Install Contao

**Contao** is a content management system (CMS), freeware and open-source. It is good for the users who want to have professional but easy to maintain sites. Contao's interface is built on Ajax and Web 2.0 technologies, supports many languages and themes. This CMS has a powerful permissions system, versioning and undo management, advanced search and sorting options. It contains modern CSS framework and a lot of integrated modules (news, calendar, forms, etc.).

To host **Contao** into your platform, please, follow this instruction's steps.


## Create Environment

1\. Log in to the platform and click the **Create Environment** button at the top left of your dasboard.

![create environment](01-create-environment.png)

2\. Find a **PHP** tab in the opened topology wizard. Pick the **Apache** application server and **MySQL** database there. State the cloudlet limits. Name your environment and click the **Create** button.

![environment wizard](02-environment-wizard.png)

3\. You have got your environment appeared in the platform dashboard list.

![Contao environment created](03-contao-environment-created.png)


## Upload the Application

1\. Go to the official **[Contao](https://contao.org/en/download.html)** web-site. Find the latest stable application version there and download it as a **.zip** archive.

![download Contao archive](04-download-contao-archive.png)

2\. Go back to your platform dashboard and click the **Upload** button at the **Deployment manager** tab. Choose the downloaded **.zip** archive for uploading.

![upload Contao archive](05-upload-contao-archive.png)

3\. Once the package is in the platform, deploy it to the environment you have just created by clicking on the **Deploy to** icon. If you want to deploy several projects into one server specify the application's target context (it is not necessary in our case, so you can just leave it empty).

![deploy Contao](06-deploy-contao.png)

![Contao context](07-contao-context.png)


## Database Configuration

1\. While the environment creation at the very beginning of this tutorial, the platform sent you an email with database credentials. Find there your **Access URL**, **Login** and **Password**.

![database credentials email](08-database-credentials-email.png)

2\. Enter the **phpMyAdmin** panel by clicking the *Access URL* (you can do it from your platform dashboard or from email). Type your username and password (copy them from the email).

![database log in](09-database-log-in.png)

3\. Go to the **Users** tab and press **Add user**.

![database add user](10-database-add-user.png)

Create a new user with an option *Create database with same name and grant all privileges* ticked.

![create dedicated database](11-create-dedicated-database.png)


## Install Contao CMS

1\. Go back to the platform dashboard and click the **Open in Browser** icon for Apache in your environment.

![open Apache in browser](12-open-apache-in-browser.png)

2\. The window about **Incomplete installation** will be opened.

![Contao incomplete installation](13-contao-incomplete-installation.png)

3\. Don't worry, everything is going well. Just go to the following address: ***http://{your_app_address}/contao/install.php***

This will open the Contao install tool, which will guide you through the installation process.

4\. In the opened window click on the **Accept license** button.

![Contao accept license](14-contao-accept-license.png)

5\. Then specify and confirm your security password (it has to be at least 8 characters long).

![Contao password](15-contao-password.png)

6\. At the next wizard step choose the *MySQL* **Driver Type** in the appropriate drop-down list and fill in the following fields:

* **Host:** link to your database <u>without *http://*</u>
* **User**: name of the user you've specified while database configuration
* **Password**: password for the DB user you've created while database configuration
* **Database**: same as the DB user name

![Contao database connection](16-contao-database-connection.png)

Click the **Save database settings** button.

7\. You will get a warning that the database is not up to date. That's ok, just click the **Update Database** button.

![Contao update database](17-contao-update-database.png)

8\. In the opened window navigate to the **Create an admin user** section and fill in the following fields:

* **User**: insert the administrator login
* **Name**: type the name of the administrator account
* **E-mail address**: paste the administrator e-mail
* **Password**: enter the password for admin account

Click the **Create admin account** button.

![Contao create admin user](18-contao-create-admin-user.png)

9\. Congratulations! Contao installed and now you just need to configure some system settings.

![Contao installed](19-contao-installed.png)

10\. Go back to the platform dashboard and click on the **Config** icon for your **Apache**.

![Apache config](20-apache-config.png)

11\. Go to the **/webroot/ROOT/contao** folder and find there **install.php** file. Delete or rename it.

![rename install php](21-rename-install-php.png)

That's all. Now you have your own Contao up and running in the platform. Visit your Contao website to make sure it works correctly. After filling Username and Password fields, you will see your administration panel.

![Contao admin panel](22-contao-admin-panel.png)

Enjoy your work with Contao CMS!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [PHP Tutorials](/php-tutorials/)
* [PHP Dev Center](/php-center/)