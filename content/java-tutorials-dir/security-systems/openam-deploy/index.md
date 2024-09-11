---
title: "OpenAM Deployment"
aliases: ["/openam-deploy/", "/jelastic-openam-deploy/"]
seoindex: "index, follow"
seotitle: "OpenAM Deployment"
seokeywords: "openam, openam tutorial, openam war download, openam example, openam tomcat, openam installation, openam federation, openam howto, openam server, openam hosting, openam in the cloud, openam cloud hosting, openam server platform"
seodesc: "See how to deploy OpenAM, open-source access management and federation server platform. For installation just download and upload OpenAM war to dashboard and get the best performance with PaaS hosting!"
menu:
    docs:
        title: "OpenAM Deployment"
        url: "/openam-deploy/"
        identifier: "openam-deploy.md"
---

# How to Deploy OpenAM

**[OpenAM](https://www.forgerock.com/platform/access-management)** is a market leading open-source access management, entitlements, and federation server platform.

As with any Java applications and frameworks, this one is very easy to deploy to the PaaS! Here's how.


## Create Environment

1\. Log into the platform dashboard.

2\. Click the **Create environment** button at the top left:

![create environment](01-create-environment.png)

3\. In the **Environment topology** window,  choose your application server (for example, [Tomcat](/tomcat/)) and specify your environment name, for example, *OpenAM*, then click **Create**.

![environment wizard](02-environment-wizard.png)

In a minute your environment will be created.

![OpenAM environment created](03-openam-environment-created.png)


## Upload Java Package

1\. Navigate to [ForgeRock web site](https://www.forgerock.com/platform/access-management)  and click on **Download Stack**.

![OpenAM download](04-openam-download.png)

2\. Select **OpenAM**, fill in the required form and copy to clipboard the URL of the latest OpenAM release (WAR archive).

![OpenAM WAR package](05-openam-war-package.png)

3\. Go back to the platform dashboard, click **Upload** and paste the URL you have just copied.

![upload OpenAM](06-upload-openam.png)

4\. Once the package is in the platform, deploy it to the environment you have just created.

![deploy OpenAM](07-deploy-openam.png)

{{%tip%}}**Note:** Do not deploy OpenAM to the **ROOT** context (otherwise you will get configuration errors later on).{{%/tip%}}

5\. Once the deployment is successfully finished, launch the application in web browser.

![open OpenAM in browser](08-open-openam-in-browser.png)


## Configure OpenAM

1\. Select **Create New Configuration** in **Configuration Options** window.

2\. Specify the default user password that you want to have and click **Next**.

![set OpenAM password](09-set-openam-password.png)

3\. In the **Server Settings** window, confirm the server URL, cookie domain, platform locate, and configuration directory settings.

![OpenAM server settings](10-openam-server-settings.png)

4\. At the **Configuration Data Store Settings** step, select the **First Instance** and confirm configuration store details.

![OpenAM configuration store](11-openam-configuration-store.png)

5\. In **User Store Settings**, select **OpenAM User Data Store**. You can ignore the warning message and go ahead.

![OpenAM site configuration](12-openam-site-configuration.png)

6\. Type the password for the **Default Policy Agent User** different from the default user password.

![OpenAM agent information](13-openam-agent-information.png)

7\. View the **Summary**. If the information is correct, click **Create Configuration**.

In few minutes the configuration process will be finished.

Now you can use **OpenAM** in your applications in the PaaS!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Java Tutorials](/java-tutorials/)
* [Setting Up Environment](/setting-up-environment/)