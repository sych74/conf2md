---
draft: false
title: "Portofino Deployment"
aliases: "/portofino/"
seoindex: "index, follow"
seotitle: "Portofino Deployment"
seokeywords: "portofino, portofino framework, java portofino, install portofino, portofino deployment, portofino hosting, portofino paas, portofino tutorial, portofino guide"
seodesc: "Portofino is web application framework for creating a complete web applictions with database connection. Follow this guide to deploy Portofino into the platform's Java-based environment."
menu: 
    docs:
        title: "Portofino Deployment"
        url: "/portofino/"
        identifier: "portofino.md"
---

# How to Install Portofino

**Portofino** is an open source web framework, which helps developers to create the outstanding enterprise applications. It was designed to comply with the following widely-spread requirements:

* *productivity*: Portofino gives results quickly (using its wizard you can create webapp just in a 30 seconds!) and allows developers to stay productive during the whole cycle of project implementation.
* *features*: Portofino package includes the set of features for common enterprise needs, that users will appreciate.
* *architecture*: Portofino has a well layered, flexible, and secure architecture, which is simple to understand.

So, let's find out how to get the Portofino application hosted with the help of the platform.


## Create Environment

1\. Log in to the platform and click **Create environment** button in the upper left corner of the dashboard.

![create environment](01-create-environment.png)

2\. Choose **Tomcat** and **MySQL** instances at the **Java** tab. Name your environment (e.g. *portofino*), define the required amount of resources within cloudlets sliders, and click **Create** button.

![environment wizard](02-environment-wizard.png)

3\. Wait just a minute for your environment to be created.


## Upload and Deploy Application

1\. Navigate to the [Portofino website](https://portofino.manydesigns.com/en#download) and click **Download** button in order to get the application package.

![Portofino site](03-portofino-site.png)

2\. After you were automatically redirected to the SourceForge site, navigate to the **Files** section.

![Portofino files](04-portofino-files.png)

3\. Open the ***manydesigns-portofino*** directory and select a folder with the latest Portofino version. Download the archive (named **portofino-x.x.zip**) it contains.

![Portofino download](05-portofino-download.png)

4\. Unzip the archive you've just downloaded.

5\. Go to your platform dashboard and click **Upload** button at the **Deployment Manager** tab. In the opened frame browse to the **ROOT.war** file, located in the *portofino-x.x/apache-tomcat-7.0.54/webapps/* folder of the extracted archive, and click **Upload**.

![upload Portofino archive](06-upload-portofino-archive.png)

6\. Then press **Deploy to** icon next to the Portofino ***.war*** file, choose the environment you've created before, and confirm the deployment in the opened window.

![deploy Portofino](07-deploy-portofino.png)

7\. Once the deployment is successfully finished, launch the application by means of pressing **Open in browser** button next to your environment.

![open in browser](08-open-in-browser.png)

Congrats! For now you can start working with your own Portofino web framework, easily hosted within the platform.

![Portofino](09-portofino.png)

Enjoy!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Java Tutorials](/java-tutorials/)
* [Setting Up Environment](/setting-up-environment/)