---
title: "TYPO3 CMS Deployment"
aliases: "/typo3/"
seoindex: "index, follow"
seotitle: "TYPO3 CMS Deployment"
seokeywords: "typo3, typo3 cms, typo content management system, typo3 paas, typo3 php, typo3 deployment, typo3 hosting, typo3 tutorial, typo3 guide"
seodesc: "A step-by-step tutorial on how to deploy an open-source TYPO3 CMS (Content Management System) into PHP environment at the platform."
menu: 
    docs:
        title: "TYPO3 CMS Deployment"
        url: "/typo3/"
        identifier: "typo3.md"
---

# How to Deploy TYPO3

Here's a step-by-step tutorial on how to deploy **[TYPO3](https://typo3.org/)**, an enterprise-class, open-source CMS (Content Management System), into the platform.

So, let's get started!


## Create Environment

1\. Log in to the platform dashboard.

2\. Click the **Create environment** button at the top left:

![create environment button](01-create-environment-button.png)

3\. Pick **Apache** application server, **PHP v5.4** and **MySQL** (or **MariaDB**) database. Specify your cloudlet limits and name of your environment (for example, *typo3*). Click **Create**.

![TYPO3 environment topology](02-typo3-environment-topology.png)

Wait just a minute for your environment to be created.

![environment for TYPO3 created](03-environment-for-typo3-created.png)


## Upload Application Package

1\. Visit the official [TYPO3 web-site](https://sourceforge.net/projects/typo3/files/TYPO3%20Source%20and%20Dummy/TYPO3%206.0.4/introductionpackage-6.0.4.zip/download?use_mirror=garr&download=) to download the latest TYPO3 version as a **zip** package (the downloading will start automatically).

2\. Using the **Deployment manager** upload the package you've just downloaded.

![upload TYPO3 package](04-upload-typo3-package.png)

3\. Once the package is in the platform, deploy it to the environment you have just created.

![deploy TYPO3 application](05-deploy-typo3-application.png)


## Environment Configuration

You need to disable ***zend_extension*** in order to get your TYPO3 application up and running. For that follow the next steps:

1\. Click **Config** button for **Apache** server.

![Apache config button](06-apache-config-button.png)

2\. Navigate to **etc &gt; php.ini** file and comment the following line: 

```
#zend_extension=/usr/lib64/php/modules/opcache.so
```

![disable zend extension](07-disable-zend-extension.png)

3\. Don't forget to **Save** the changes and **Restart** your application server.


## Install TYPO3

1\. Click **Open in Browser** button next to the Apache node.

![open Apache in browser](08-open-apache-in-browser.png)

2\. The Typo3 installation will be started. Click **Continue**.

![TYPO3 install tool](09-typo3-install-tool.png)

3\. In the *Connect to your database host* window choose the **MySQL/MySQLi** driver and fill in the **Username** and **Password** fields with credentials to your database (you've got them via email while creating the environment). Put database server address in the **Host** field and click **Continue** button.

![TYPO3 connect to database](10-typo3-connect-to-database.png)

4\. Then specify the name of a new database (for example, *typo3*) and click **Continue** button.

![TYPO3 select database](11-typo3-select-database.png)

5\. In the next window choose the *Introduction package*. Click **Continue**.

![TYPO3 choose package](12-typo3-choose-package.png)

6\. The installation will be started. Wait a few minutes for its completion.

![TYPO3 installation in progress](13-typo3-installation-in-progress.png)

7\. Finally, enter the password for access to TYPO3 Admin Panel and choose the color of TYPO3 main page.

![TYPO3 provide password](14-typo3-provide-password.png)

8\. Congratulations! The TYPO3 was installed. Click **Go to your Website** button.

![TYPO3 successfully installed](15-typo3-successfully-installed.png)

9\. Now you can see a default main page. Click **Log into TYPO3**.

![TYPO3 introduction package](16-typo3-introduction-package.png)

10\. Here just enter your login and password (which you've stated in the 7th step) and click **Login**.

![TYPO3 log in](17-typo3-log-in.png)

11\. Your admin page will be opened.

![TYPO3 admin panel](18-typo3-admin-panel.png)

That's it! Now you have your own TYPO3 in the platform.


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [PHP Tutorials](/php-tutorials/)
* [Setting Up Environment](/setting-up-environment/)