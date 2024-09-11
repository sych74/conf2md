---
draft: false
title: "Pydio Deployment"
aliases: "/pydio/"
seoindex: "index, follow"
seotitle: "Pydio Deployment"
seokeywords: "pydio, pydio file management, file management platform, php pydio, install pydio, pydio deployment, pydio hosting, pydio paas, pydio tutorial, pydio guide"
seodesc: "Pydio is a modern file management platform that can be easily deployed into PaaS. Follow the steps of this step-by-step tutorial to get Pydion in a matter of minutes."
menu: 
    docs:
        title: "Pydio Deployment"
        url: "/pydio/"
        identifier: "pydio.md"
---

# How to Install Pydio

**Pydio** (ex-ajaXplorer) is a free and open-source launcher that can turn your server (on premise, NAS, cloud IaaS or PaaS) into a powerful and convenient information exchanging system for you company. It is really safe, private and controllable alternative to SaaS Boxes and Drives. There are freeware clients for iOS and Android, so you can get an access to your files from any smartphone or tablet. 

You can install it with ease into your platform.


## Create Environment

{{%tip%}}If you don't have a PaaS account, please register it as described in the [Getting Started](/getting-started/) document.{{%/tip%}}

1\. Log in to the platform dashboard and click **Create environment** button in the upper left corner of the dashboard.

![create environment button](01-create-environment-button.png)

2\. Choose the ***PHP*** tab. Pick **Apache** as your application server and **MySQL** as a database. State the cloudlet limits for the chosen nodes and name your environment or use the default name. Click the **Create** button.

![Pydio environment topology](02-pydio-environment-topology.png)

3\. Just in seconds your new environment will be created and displayed in the environment list.  

You have received two emails as well: the first one with the confirmation of the successful creation of the environment and the second one - with MySQL authorization details. 


## Configure MySQL Database

1\. In the platform dashboard panel click the **Open in Browser** button for the MySQL node in your environment.

![open MySQL in browser](03-open-mysql-in-browser.png)

2\. Open the letter with *MySQL node successfully added* subject in your email box. Find there your **Login** and **Password** (you can also enter the **phpMyAdmin** panel by clicking on the **Access URL** from the same letter omitting the first step).

3\. Enter your **Username** and **Password** (or copy them from the email).

![MySQL database log in](04-mysql-database-log-in.png)

4\. Navigate to the **Users** tab and create a new user (name it, for example, *pydio*) with an option ***Create database with same name and grant all privileged*** ticked. Click the **Go** button in the bottom right corner.

![database add user](05-database-add-user.png)

![create dedicated database](06-create-dedicated-database.png)


## Download and Deploy Application 

1\. Go to the official [Pydio site](https://pydio.com/), find **Download** tab and choose the **Latest Stable** item.

![download Pydio](07-download-pydio.png)

2\. Choose **Click Here!** in the Manual Installation box.

![Pydio package](08-pydio-package.png)

3\. Add your email and name to subscribe to Pydio mailing or just click ***No thanks, to the download now!*** link at the right-bottom corner of the pop-up window.

![subscribe or skip Pydio mailing](09-subscribe-or-skip-pydio-mailing.png)

4\. In the opened browser tab select the latest branch (*5.2.3* in our case).

![latest Pydio branch](10-latest-pydio-branch.png)

5\. Download a ***pydio-core*** *.zip* file (in our example it is named *pydio-core-5.2.3.zip*).

![download Pydio archive](11-download-pydio-archive.png)

6\. Switch back to your platform dashboard. Click **Upload** in the **Deployment Manager**. Choose your archive file and click the **Upload** button.

![upload Pydio archive](12-upload-pydio-archive.png)

7\. Then click the **Deploy to** icon next to the name of your archive file in the **Deployment Manager** and choose your environment within drop-down list. In the opened frame specify the application's target context if you want to deploy several projects into one server (in our case it is not necessary) or just leave it blank. 


## Run Application 

1\. Open your environment in browser by clicking the **Open in Browser** icon next to it.

![open Pydio in browser](13-open-pydio-in-browser.png)

2\. Click on the ***click here to continue to Pydio*** link.

![Pydio diagnostic tool](14-pydio-diagnostic-tool.png)

3\. Choose the language you prefer and click **Start Wizard**. Follow the instructions.

![choose Pydio language](15-choose-pydio-language.png)

4\. Expand parameters sections one by one and fill in the required data.

In the **Configurations storage** section choose *Database (Requires MySQL, PostgreSQL or SQLite)* **Storage Type**. Enter your database **Host** (access URL from the received email <u>without *http://*</u>), type **Database** name and **User** name (you've specified them while DB setting up).

Once you've customized all the necessary settings, press **Install Pydio Now** button.

![Pydio configure database](16-pydio-configure-database.png)

5\. After installation has been successfully completed you'll be automatically redirected to the Pydio login page. Type the credentials of administrator account you've created in the previous step and click button with green tick.

![Pydio log in](17-pydio-log-in.png)

6\. Congrats! Now you can work with Pydio application installed to your platform. Enjoy and share!

![Pydio successfully installed](18-pydio-successfully-installed.png)


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [PHP Tutorials](/php-tutorials/)
* [PHP Dev Center](/php-center/)