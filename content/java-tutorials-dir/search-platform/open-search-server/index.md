---
draft: false
title: "OpenSearchServer Deployment"
aliases: "/open-search-server/"
seoindex: "index, follow"
seotitle: "OpenSearchServer Deployment"
seokeywords: "opensearchserver, open search server, java opensearchserver, install opensearchserver, opensearchserver deployment, opensearchserver hosting, opensearchserver tutorial, opensearchserver paas"
seodesc: "Learn how to host the OpenSearchServer server for the development of the index-based applications. Follow a few simple steps from this guide to get OpenSearchServer at the platform."
menu: 
    docs:
        title: "OpenSearchServer Deployment"
        url: "/open-search-server/"
        identifier: "open-search-server.md"
---

# How to Install OpenSearchServer

**OpenSearchServer** is an open source application server that allows to easily develop index-based applications such as search engines. It provides a set of advanced searching functions, such as full-text, boolean and phonetic search, filtered search, automatic language detection, relevance customization, etc.

OpenSearchServer is written in Java and can be integrated into almost any kind of application without the need to produce Java code. REST/XML APIs make OpenSearchServer connectable to other programming languages, and "advanced plugins" capability allows sophisticated customizations.

So, let's find out how to get the OpenSearchServer application hosted just in a few minutes with the help of the platform.


## Create Environment

1\. Log in to the platform and click **Create environment** button in the upper left corner of the dashboard.

![create environment](01-create-environment.png)

2\. In the opened window select **Java** tab and choose **Tomcat** as your application server. Use the cloudlets sliders to determine the required resources usage, type your environment name (e.g. *osserver*) and click **Create** button.

![environment wizard](02-environment-wizard.png)

3\. Wait just about a minute for your environment to be created.

![Open Search Server environment created](03-environment-created.png)


## Upload and Deploy Application

1\. Navigate to the OpenSearchServer [official web-site](https://www.opensearchserver.com/) and click **.WAR** button in the ***Downloads & documentation*** section to download the required distributive package.

![Open Search Server download](04-open-search-server-download.png)

2\. Return to your platform dashboard and click **Upload** button at the **Deployment Manager** tab. In the opened frame browse to the downloaded file and click **Upload**.

![upload archive](05-upload-archive.png)

3\. Now press **Deploy to** icon next to the uploaded ***.war*** file, choose the environment you've created before, and confirm the deployment in the opened frame.

![deploy Open Search Server](06-deploy-open-search-server.png)

4\. Wait until the deployment is successfully finished and run the application by means of pressing **Open in Browser** icon next to your environment.

![open in browser](07-open-in-browser.png)

Now you have your OpenSearchServer hosted and ready for work at the platform.

![Open Search Server](08-open-search-server.png)

Congrats!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Java Tutorials](/java-tutorials/)
* [Setting Up Environment](/setting-up-environment/)