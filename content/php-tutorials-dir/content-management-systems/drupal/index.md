---
draft: false
title: "Drupal Deployment"
aliases: "/drupal/"
seoindex: "index, follow"
seotitle: "Drupal Deployment"
seokeywords: "cloud hosting, drupal, drupal cms, create drupal, drupal deployment, drupal php, php cms, drupal tutorial, drupal deployment guide"
seodesc: "Follow this guide to host Drupal CMS in the PHP-based environment at the platform in a few simple steps or use the automated one-click instalation option."
menu: 
    docs:
        title: "Drupal Deployment"
        url: "/drupal/"
        identifier: "drupal.md"
---

# How to Deploy Drupal

You can have a **Drupal** instance up and running within minutes using one-click install option.

<div data-app="drupal" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app">
</div>

The process is simple - just click **Get it hosted now**, type your email and install **Drupal** in a minute skipping the steps of manual installation.


## Manual Drupal Installation

**[Drupal](http://drupal.org/)** is an open source content management platform powering millions of websites and applications. It's built, used, and supported by an active and diverse community of people around the world. Let's deploy it to the platform right now!

It's pretty easy, just follow a few simple steps below:


## Create an Environment

1\. Log in to the platform dashboard.

2\. Click the **Create environment** button at the top left:

![create environment](01-create-environment.png)

3\. Pick **Apache PHP** application server and **MySQL** (or **MariaDB**) database.

![environment wizard](02-environment-wizard.png)

In a minute your environment with both **Apache** and **MySQL** will be created and appear in the environment list.

4\. Click **Config** button for your Apache server.

![Apache PHP config](03-apache-php-config.png)

5\. Navigate to **etc** folder and open ***php.ini*** file.

6\. Add ***extension=gd.so*** line after **extension=mysql.so**.

![add PHP extension](04-add-php-extension.png)

7\. Save the changes and **Restart** the node.

![Apache PHP restart](05-apache-php-restart.png)


## Upload the Application

1\. Go to the official [Drupal web-site](https://www.drupal.org/download) and download **.zip** archive. For that just click **Download Drupal** button and choose the appropriate version in the opened window.

![download Drupal](06-download-drupal.png)

![Drupal ZIP package](07-drupal-zip-package.png)

2\. Upload this **.zip** archive to the **Deployment Manager**.

![upload Drupal](08-upload-drupal.png)

3\. Once the package is in the platform, **Deploy** it to the environment you have just created.

![deploy Drupal](09-deploy-drupal.png)


## Configure Database

1\. Once the deployment is finished, click **Open in Browser** button for **MySQL** node.

2\. When you created the environment, the platform sent you an email with credentials to the database. Create an account and the database with the application using these credentials.

![database log in](10-database-log-in.png)

![database add user](11-database-add-user.png)

![create dedicated database](12-create-dedicated-database.png)


## Install Drupal

1\. Click the **Open in Browser** button for Apache in your environment.

![open Apche PHP in browser](13-open-apche-php-in-browser.png)

2\. Process of installation is rather simple, but let's pay more attention to the database connection. Fill in the required fields in the following way:
* choose Database Type: **MySQL, MariaDB, or equivalent**
* type **Database name** (which you've entered while creating database)
* type **Database Username** (which you've entered while creating database or just root)
* type **Database Password** (which you've entered while creating database or which you've got by email)
* state **Database Host** (insert the link to your database without "http://" and "/")
* Click **Save and Continue** button

![Drupal set up database](14-drupal-set-up-database.png)

3\. Fill in the last form of installation. That's all!

Now you can easily use **Drupal** in the platform.


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
