---
title: "Joomla Deployment"
aliases: "/joomla/"
seoindex: "index, follow"
seotitle: "Joomla Deployment"
seokeywords: "joomla, joomla cms, joomla content management, install joomla, joomla deployment, joomla hosting, php joomla, joomla tutorial, joomla guide, joomla paas"
seodesc: "This is a step-by-step instruction on deploying Joomla into the platform so that you can use it as a content management system (CMS)."
menu: 
    docs:
        title: "Joomla Deployment"
        url: "/joomla/"
        identifier: "joomla.md"
---

# How to Deploy Joomla

You can have a **Joomla** instance up and running within minutes using one-click install option.

<div data-app="joomla" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app">
</div>

The process is simple - just click **Get it hosted now**, type your email and install **Joomla** in a minute skipping the steps of manual installation.

The full list of similar prepackaged solutions for quick deploy can be found at [platform Marketplace](https://www.virtuozzo.com/application-platform/marketplace/).


## Manual Joomla Installation

This is a step-by-step instruction on deploying [Joomla](https://www.joomla.org/) into the platform so you can use it as a content management system (CMS), which enables you to build Web sites and powerful online applications.

To host a PHP Joomla application follow the next instruction:

### Create Environment

1\. Log in to the platform dashboard.

2\. Click the **Create environment** button at the top left:

![create environment button](01-create-environment-button.png)

3\. Pick **Apache** application server, **PHP v5.3** and **MySQL** database.

![Joomla environment topology](02-joomla-environment-topology.png)

In a minute your environment with both **Apache** and **MySQL** will be created and appear in the environment list.

### Upload Application

1\. Go to the official [Joomla web-site](https://downloads.joomla.org/) and download **.zip** archive by clicking **Download Joomla! 3.0** button.

![download Joomla](03-download-joomla.png)

2\. Upload this **.zip** archive to the **Deployment manager**.

![upload Joomla package](04-upload-joomla-package.jpg)

3\. Once the package is in the platform, deploy it to the environment you have just created.

![deploy Joomla application](05-deploy-joomla-application.png)

### Configure Database

1\. Once the deployment is finished, click **Open in Browser** button for **MySQL** node.

2\. When you created the environment, the platform sent you an email with credentials to the database. Create an account and the database with the application using these credentials.

![database login](06-database-login.jpg)

![database add user](07-database-add-user.jpg)

![create dedicated database](08-create-dedicated-database.png)

### Install Joomla

1\. Click the **Open in Browser** button for Apache in your environment.

![open Apache in browser](09-open-apache-in-browser.png)

2\. Follow the steps of **Joomla** installation starting with **Main Configuration** settings.

![Joomla main configuration](10-joomla-main-configuration.png)

3\. At the **Database Configuration** stage fill in the required fields in the following way:

* choose Database Type: **MySQL** or **MariaDB**
* state **Host Name** (insert the link to your database without "http://" and "/")
* type **Username** (which you've entered while creating database or just root)
* type **Password** (which you've entered while creating database or which you've got by email)
* type **Database name** (which you've entered while creating database)
* Click **Next** button

![Joomla database configuration](11-joomla-database-configuration.png)

4\. The final step is **Overview**:

* Choose **Sample Data** from the list if you want to install any.
* Activate **Email Configuration** if you want to get the settings info to your email after installation.
* Look through configurations and click **Install** button.

![Joomla installation finalisation](12-joomla-installation-finalisation.png)

Now you have your own Joomla in the platform. Enjoy!


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
