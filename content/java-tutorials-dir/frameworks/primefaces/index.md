---
title: "PrimeFaces Deployment"
aliases: "/primefaces/"
seoindex: "index, follow"
seotitle: "PrimeFaces Deployment"
seokeywords: "primefaces tutorial, primefaces example, primefaces download, primefaces file upload, primefaces tomcat, primefaces quick start tutorial, primefaces upload, deploy primefaces, primefaces how to, primefaces hosting, primefaces in the cloud"
seodesc: "Here is a quick start tutorial on how to deploy PrimeFaces, popular UI Java framework, to the platform. Just download PrimeFace war and upload it to dashboard to get the best Java hosting performance!"
menu: 
    docs:
        title: "PrimeFaces Applications Deployment"
        url: "/primefaces/"
        identifier: "primefaces.md"
---

# How to Deploy PrimeFaces Applications

**[PrimeFaces](https://www.primefaces.org/)** is one of the most popular UI frameworks in Java Ecosystem.

Let's deploy PrimeFaces application to the platform and you'll see how easy it is!


## Create Environment

1\. Log into the platform dashboard.

2\. Click the **Create environment** button at the top left.

![create environment](01-create-environment.png)

3\. In the **Environment Topology** dialog, pick your application server (for example, **Tomcat**). Then type your environment name, for example, *primefacestest*.

![environment wizard](02-environment-wizard.png)

Wait just a minute for your environment to be created.


## Upload Java Package

1\. Upload your **war** file to the **Deployment manager** (we use *[prime-showcase-1.0.0-SNAPSHOT.war](http://repository.primefaces.org/org/primefaces/prime-showcase/1.0.0-SNAPSHOT/prime-showcase-1.0.0-SNAPSHOT.war)* as an example).

![upload PrimeFaces](03-upload-primefaces.png)
 
2\. Once the package is in the platform, deploy it to the environment you have created earlier.

![deploy PrimeFaces](04-deploy-primefaces.png)


## Start Application

That's all you have to do! Now you can launch your application in a web browser and enjoy.

![PrimeFaces](05-primefaces.png)


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Java Tutorials](/java-tutorials/)
* [Setting Up Environment](/setting-up-environment/)