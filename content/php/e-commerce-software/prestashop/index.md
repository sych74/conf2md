---
draft: false
title: "PrestaShop Deployment"
aliases: "/prestashop/"
seoindex: "index, follow"
seotitle: "PrestaShop Deployment"
seokeywords: "prestashop, online store, prestashop online store, php prestashop, install prestashop, prestashop deployment, prestashop hosting, prestashop paas, prestashop tutorial, prestashop guide"
seodesc: "Learn how to deploy PrestaShop - popular online stores platform - into PHP environment at PaaS. Use the one-click installer or manual guide for PrestaShop installation."
menu: 
    docs:
        title: "PrestaShop Deployment"
        url: "/prestashop/"
        identifier: "prestashop.md"
---

# How to Deploy PrestaShop

You can have a **PrestaShop** instance up and running within minutes using one-click install option.

<div data-app="prestashop" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app">
</div>

The process is simple - just click **Get it hosted now**, type your email and install **PrestaShop** in a minute, skipping the steps of manual installation.

Find the full list of applications available for one-click installation at our [Marketplace page](https://www.virtuozzo.com/application-platform/marketplace/).


## Manual PrestaShop Installation

Here's a step-by-step tutorial on how to deploy [PrestaShop](https://www.prestashop.com/en), popular all over the world online stores platform.

So, let's get started!

### Create Environment

1\. Log in to the platform dashboard.

2\. While in the dashboard, click the **Create environment** button at the top left:

![create environment](01-create-environment.png)

3\. Pick **Apache PHP** application server and **MySQL** database.

![environment wizard](02-environment-wizard.png)

Wait just a minute for your environment to be created.

![environment for PrestaShop created](03-environment-for-prestashop-created.jpg)

### Upload Application Package

1\. Go to [PrestaShop site](https://www.prestashop.com/en), download the latest PrestaShop version as a **zip** package and upload it using Deployment manager.

![upload PrestaShop archive](04-upload-prestashop-archive.jpg)

2\. Once the package is in the platform, deploy it to the environment you have just created.

![deploy PrestaShop archive](05-deploy-prestashop-archive.jpg)

3\. For using PrestaShop you need to include *gd.so, xcache.so, apc.so, memcache.so* modules. For this click **Config** button for your Apache server, navigate to **etc/php.ini** and add *extension=gd.so, extension=xcache.so, extension=apc.so, extension=memcache.so* lines as it is shown in the picture below:

![PHP modules for PrestaShop](06-php-modules-for-prestashop.png)

Click **Open in Browser** button next to the MySQL node. Log in to *phpMyAdmin* using credentials, which you've got via email while creating your environment. Create an account and the same-named database.

![add database user](07-add-database-user.jpg)

4\. Go back to the dashboard and restart Apache node.

![restart Apache](08-restart-apache.jpg)

5\. That's all. Now you can open your application in browser and install it. Process of installation is rather simple, but let's pay a little attention to the database connection. Just fill in form with database server address, database name, login and password which you've used while creating your MySQL user.

![configure database connection](09-configure-database-connection.png)

Now you can easily configure your online-store and install it.

![PrestaShop installed](10-prestashop-installed.png)

Hope this instruction will be helpful for you.


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [PHP Tutorials](/php-tutorials/)
* [PHP Dev Center](/php-center/)

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
