---
title: "OpenCMS Deployment"
aliases: ["/opencms-deploy/", "/jelastic-opencms-deploy/"]
seoindex: "index, follow"
seotitle: "OpenCMS Deployment"
seokeywords: "opencms tutorial, opencms war, opencms database, opencms hosting, opencms java, opencms free, opencms example, opencms open source, opencms performance, opencms deploy, opencms how to, opencms in the cloud, opencms cloud hosting"
seodesc: "See the tutorial on how to deploy OpenCMS, free and open source content managment system. Upload OpenCMS war to dashboard, configure database, and get the best performance with PaaS Java hosting!"
menu: 
    docs:
        title: "OpenCMS Deployment"
        url: "/opencms-deploy/"
        identifier: "opencms-deploy.md"
---

# How to Deploy OpenCMS

You can have a **OpenCMS** instance up and running within minutes using one-click install option.

<div data-app="opencms" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app">
</div>

The process is simple - just click **Get it hosted now**, type your email and install **OpenCMS** in a minute skipping the steps of manual installation.


## Instruction on Manual OpenCMS Installation

This is a step-by-step instruction on deploying [OpenCMS](http://www.opencms.org/), content management system, into PaaS. The platform can natively run any Java application with no code changes required so the procedure below is applicable to most Java applications.

### Create Environment

1\. Log into the platform dashboard.

2\. Click **Create environment** to set up a new environment.

![create environment](01-create-environment.png)

3\. In the **Environment topology** window, select **Tomcat** as your application server and **Maria DB** as a database, type your environment name, for example, *opencms*, and click **Create**.

![environment wizard](02-environment-wizard.jpg)

4\. In a minute your environment with both [Tomcat](/tomcat/) and **Maria DB** will be created and appears in the environments list.

### Upload Java Package

1\. Go to [OpenCMS web-site](http://www.opencms.org/) and download the latest OpenCMS distribution WAR file.

![download OpenCMS](03-download-opencms.png)

2\. Upload the downloaded Java WAR package using **Deployment manager**.

![upload OpenCMS](04-upload-opencms.png)

3\. Once the package is in the platform, deploy it to the environment you have just created.

![deploy OpenCMS](05-deploy-opencms.jpg)

### Configure Database

1\. Switch back to the platform dashboard and click **Open in Browser** button for **Maria DB**.

![open MariaDB in browser](06-open-mariadb-in-browser.jpg)

2\. While you were creating the environment, the platform sent you an email with credentials to the database. Create an account and the database with the application using these credentials.

![database add user](07-database-add-user.jpg)
 
![create dedicated database](08-create-dedicated-database.jpg)

### Configure OpenCMS

1\. Increase the limit of **max_allowed_packet** as [OpenCMS](http://www.opencms.org/) prompts you to do so.

![max allowed packet](09-max-allowed-packet.jpg)

2\. Restart the database.

### Install and Start OpenCMS

1\. Open the application in web browser (click **Open in Browser** buttom for your environment). You will get the next message:

![OpenCMS not initialized](10-opencms-not-initialized.jpg)

It's ok but you need to launch OpenCMS startup. To do so, navigate to *http://{your_environment_name}.{[hoster's_domain](/paas-hosting-providers/)}/setup* and come through the **Setup Wizard** and accept the license agreement.

![OpenCMS license](11-opencms-license.jpg)

2\. In **OpenCMS Setup Wizard**, specify the URL of the database and the credentials, you have just provisioned.

![OpenCMS database connection](12-opencms-database-connection.jpg)
 
Finally you can launch OpenCMS and use all its capabilities!

![OpenCMS](13-opencms.jpg)

Hope this instruction will be useful for you!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Java Tutorials](/java-tutorials/)
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
