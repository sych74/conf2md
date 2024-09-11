---
draft: false
title: "How to Deploy EJB to the PaaS"
aliases: "/enterprise-javabeans/"
seoindex: "index, follow"
seotitle: "How to Deploy EJB to the PaaS"
seokeywords: "enterprise java beans, deploy ejb, ejb deploy, ejb deployment, ejb deployment process, ejb deployment example, ejb deployment tutorial, deploy ejb to glassfish, deploy ejb application, ejb deploy glassfish, ejb deployment glassfish, deploy java beans"
seodesc: "Here's a tutorial on Enterprise Java Beans deployment process to GlassFish application server as an example. Deploy your EJB application just in few minutes with the platform!"
menu: 
    docs:
        title: "How to Deploy EJB to the PaaS"
        url: "/enterprise-javabeans/"
        identifier: "enterprise-javabeans.md"
---

# How to Deploy EJB to the PaaS

This instruction shows you how easy it is to deploy your **Enterprise JavaBeans (EJB)** applications to the platform. You don't have to change a single line of code or custom configuration.

It's just a few simple steps.


## Create Environment

1\. Log into the platform dashboard.

2\. Click the **Create environment** button:

![create environment](01-create-environment.png)

3\. In the **Environment topology** window, select **GlassFish** as your application server, set the cloudlets limit, type your environment name, for example, *ejbtest*, and click **Create**.

![environment wizard](02-environment-wizard.png)

In a minute your environment will be created and will appear in the environments list.

![environment for Enterprize JavaBeans created](03-environment-for-ejb-created.png)


## Upload Java Package

1\. Upload your **EAR** archive to the **Deployment manager**.

![upload Enterprize JavaBeans application](04-upload-ejb-application.png)

2\. Deploy it to the environment you have created earlier.

![deploy Enterprize JavaBeans application](05-deploy-ejb-application.png)

Now you can open your application in a web browser and enjoy!

![Enterprize JavaBeans application](06-ejb-application.png)


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Java Tutorials](/java-tutorials/)
* [Setting Up Environment](/setting-up-environment/)