---
draft: false
title: "Cyclos Deployment"
aliases: ["/cyclos-deploy/", "/jelastic-cyclos-deploy/"]
seoindex: "index, follow"
seotitle: "Cyclos Deployment"
seokeywords: "cyclos, cyclos banking system, install cyclos, cyclos deployment, cyclos hosting, cyclos tutorial, cyclos guide, cyclos paas, java cyclos"
seodesc: "You can have a Cyclos instance up and running within minutes using one-click install option. Follow the manual steps of deployment for a full control over the Cyclos instance installation."
menu:
    docs:
        title: "Cyclos Deployment"
        url: "/cyclos-deploy/"
        identifier: "cyclos-deploy.md"
---

# How to Deploy Cyclos

You can have a **Cyclos** instance up and running within minutes using one-click install option.

<div data-app="cyclos" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app">
</div>

The process is simple - just click **Get it hosted now**, type your email and install Cyclos in a minute skipping the steps of manual installation.

Find out even more solutions at our [platform Marketplace](/marketplace/).


## Instruction on manual Cyclos installation

[Cyclos](http://cyclos.org/) is a complete on-line banking system with additional modules such as e-commerce and communication tools.

It's pretty easy to deploy it, just follow the steps below:


### Create Environment

1\. Log into the platform dashboard.

2\. While in the platform dashboard, click the **Create environment** button:

![create environment button](01-create-environment-button.png)

3\. In the **Environment topology** window select [Tomcat](/tomcat/) as your application server. Pick **MySQL** as the database you want to use and then choose your environment name, for example, *Cyclos*, and click **Create**.

![Cyclos environment topology](02-cyclos-environment-topology.png)

It will take just a minute for your environment to be created.

![Cyclos environment created](03-cyclos-environment-created.png)

### Upload Java Package

1\. Navigate to the [Cyclos web site](https://www.cyclos.org/) and download the basic installation package.

![Cyclos download](04-cyclos-download.png)

![Cyclos basic installation package](05-cyclos-basic-installation-package.png)

2\. Extract the files from zip package you have just downloaded and create a **.WAR file** from **web** folder contents.

3\. Upload your Java package to the **Deployment manager**.

![upload Cyclos package](06-upload-cyclos-package.png)

4\. Once the package is in the platform, deploy it to the environment you have just created.

![deploy Cyclos application](07-deploy-cyclos-application.png)

### Configure Database

1\. Click **Open in Browser** button for **MySQL**.

![MySQL open in browser](08-mysql-open-in-browser.png)

2\. When you created the environment, the platform sent you an email with credentials to the database. Use these credentials to create a user account and the database with the application.

![database add new user](09-database-add-new-user.png)

![configure new database user](10-configure-new-database-user.png)

### Configure Cyclos

1\. Switch back to the platform dashboard and click **Config** button for **Tomcat**.

![Tomcat configs](11-tomcat-configs.png)

2\. Open the Cyclos configuration file (***home/webapps/ROOT/WEB-INF/classes/cyclos.properties***) and type the host URL.

![Cyclos configuration file](12-cyclos-configuration-file.png)

3\. In the same file you will have to set the database configuration (database URL, username and password).

![configure Cyclos database connection](13-configure-cyclos-database-connection.png)

Don't forget to **Save** your changes and **Restart** Tomcat.

### Start Cyclos

Finally, you can launch Cyclos and use all of its functions!

![Cyclos successfully deployed](14-cyclos-successfully-deployed.png)

The default credentials are *admin/1234*.


## What's next?

* [Java Tutorials](/java-tutorials/)
* [Cyclos 4](/cyclos-4/)
* [Cyclos SMS Module with Mobile Gateway](https://www.virtuozzo.com/company/blog/mobile-banking-in-the-cloud-part-ii-cyclos-sms-module-with-a-mobile-phone-gateway/)

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
