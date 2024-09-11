---
draft: false
title: "Alto"
aliases: "/alto/"
seoindex: "index, follow"
seotitle: "Alto"
seokeywords: ""
seodesc: "Alto CMS is a modern engine for creation of the sites with different purposes. It is open-source, freeware, and can be used with MySQL and PostgreSQL databases.This CMS is based on a MVC (Model..."
menu: 
    docs:
        title: "Alto"
        url: "/alto/"
        weight: 6
        parent: "wiki"
        identifier: "alto.md"
---

# How to Install Alto CMS

**Alto CMS** is a modern engine for creation of the sites with different purposes. It is open-source, freeware, and can be used with MySQL and PostgreSQL databases.

This CMS is based on a MVC (Model Viewer Controller) paradigm. Its basic functionality is permanently updated with hooks and plug-ins, created by the community of independent developers for this system. In addition, Alto CMS supports Smarty 3+ template engine for PHP, which makes it easy to customize your site appearance. 

Find out how to install **Alto CMS** application into your platform by following the next steps.

## Create an Environment

*NOTE: If you don't have a PaaS account, please register it as described in the [Getting Started](/getting-started) document.*

1\. Log in to the platform and click **Create environment** button in the upper left corner of the dashboard.

2\. Choose the **PHP** tab. Pick **Apache** as your application server and **MySQL** as a database. Define the resources limits for the chosen nodes and name your environment (or use the default name). Click the **Create** button.
![alto alto1](alto1.PNG)

3\. In a seconds your environment with both Apache and MySQL will be created and appear in the environments list.
![](alto2.PNG)


## Upload the Application

1\. Go to [this link](http://sourceforge.net/projects/altocms/files/?source=navbar) and choose the latest version of Alto CMS to download.

![](alto_download.PNG)

2\. Go to your platform dashboard. Click **Upload** in the Deployment Manager. Choose your archive file and click the **Upload** button.
![alto alto4](alto4.png)

3\. Click the **Deploy to** icon next to the name of your archive file and choose the appropriate environment. If you would like to deploy several projects into one server, specify the application's target context (in our case it is not necessary).
![alto alto45](alto45.png)


## Configure Database

1\. Once the deployment is finished, click **Open** in browser icon for MySQL node in your AltoCMS environment.
![alto alto5](alto5.png)

2\. After the environment creation you've received two emails: the first one with the confirmation of successful environment creation and the second one &ndash; with MySQL authorization details. Find there **Login** and **Password** for signing in to the phpMyAdmin. 
![](alto6.PNG)

3\. In the opened administrator panel navigate to the **Users** tab and create a new user with an option **Create database** **with same name and grant all privileges** ticked. Name it, for example, alto.

![](alto7.PNG)

![](alto8.PNG)

## Install Alto CMS

1\. Switch back to the platform dashboard and click the **Open in browser** icon for Apache server in your environment.
![alto alto9](alto9.png)

2\. In the opened tab you'll see the first step of Alto CMS installation, which starts with checking if your environment configurations meet the requirements. Click the **Next** button.
![](alto10.PNG)

3\. The next step is DB configuration. Type the **hostname** of your database (it is the access URL from the received email <u>without *http://*</u>), **DB name** and **Username** (you've created them while DB setting). Click the **Next** button. 
![](alto11.PNG)

4\. In the next stage enter your **Email** and type **Login** and **Password** for administrator user. Click the **Next** button. 
![](alto12.PNG)

5\.  Installation will be started. Wait till its completion.
![](alto13.PNG)

6\. Open your platform dashboard and click on the Apache **Config** icon. Now find the **install** folder (**/webroot/ROOT/install**) and delete it.

![](alto14.PNG)


That's all! Now you have your own Alto CMS in PaaS PHP Cloud. Enjoy it!