---
draft: false
title: "Cluster Access Levels"
aliases: "/cluster-access-levels/"
seoindex: "index, follow"
seotitle: "Cluster Access Levels"
seokeywords: "access levels, paas access levels, administrators access, developers access, end users access"
seodesc: "Administrators, developers (or SMBs), and end users access levels and specifics to interact with the PaaS."
menu:
    docs:
        title: "Cluster Access Levels"
        url: "/cluster-access-levels/"
        weight: 90
        parent: "platform-overview"
        identifier: "cluster-access-levels.md"
---

# Cluster Access Levels

PaaS is targeted at a wide audience of developers and SMBs, enterprises and hosting providers. Each class of customers has its own level of access and a specific way to interact with our platform.

There are three levels of access to the PaaS Cluster:

* [administrators](#administrators)
* [developers or SMBs](#developers-or-smbs)
* [end users](#end-users)

![PaaS access levels](01-paas-access-levels.png)

The platform provides two admin panels for accessing the cluster. Cluster Panel (JCA) is available for administrators at hosting providers and enterprise companies. The other admin panel is the Platform Dashboard which is used by developers. This makes the system ideal for DevOps teams.


## Administrators

The **administrators** of the platform are operations departments of [hosting providers](/paas-hosting-providers/) or IT departments of enterprise companies. After the platform installation, they become the owner and begin to manage the overall performance via *Cluster Admin Panel* by setting the main configurations (quotas, tariffs, customization etc.) and supporting all of the required aspects.

There are four main tasks performed by the administrators during the PaaS Cluster lifecycle:

* Installation
* Launch
* Management
* Update

![PaaS administrator tasks](02-paas-administrator-tasks.png)

The platform provides a full set of analytics, documentation and required tools for performing the above mentioned tasks in an efficient and high quality way.


## Developers or SMBs

This group of platform customers can create environments, deploy their applications and perform all the actions required for the successful [lifecycle of their applications](/how-to-manage-application-lifecycle/). Environment and application management is performed via the platform's panel for developers - [PaaS Dashboard](/dashboard-guide/).

The main activities available for developers or SMBs in the platform are as follows:

* create simple and complex environments
* deploy applications in different ways without any code change
* ability to tune and tweak configurations
* scale applications vertically and horizontally
* test and debug applications remotely
* application lifecycle management
* clone and share environments
* suspend and activate stopped environments
* process statistics and logs
* upgrade and fund account, etc.

While using PaaS, the typical developer might go from trial registration to features testing during the trial period. The major steps of this life cycle are represented in the diagram below:

![account lifecycle](03-account-lifecycle.png)

At the end of the trial period developers decide whether to upgrade the account and reach the production or to get the account destroyed.

Enterprise installations do not have a trial period. In the enterprise private cloud developers can self-manage their application environments using the platform dashboard relieving IT administrators from environment configuration and setup tasks.


## End Users

The ***end-users*** are connected to the PaaS Cluster indirectly by **using applications** deployed to the environments created by developers or SMBs or enterprise developers. All of the incoming users' requests are sent to the domain name of an appropriate application and are processed in one of the following ways:

* via **[Global Resolvers](/shared-load-balancer/)**
The platform uses several synchronized Resolvers (SLBs) for receiving requests simultaneously. As a result, there can be several entry points for environments used at the same time.
![cluster access shared balancer](04-cluster-access-shared-balancer.png)

* via **[Public IP](/public-ip/)** if it is attached to the entry point of the environment (balancer, app server or database container). This solution provides less risk of being affected by other applications (as in the case with shared Resolvers) and is recommended for production applications. Also Public IP usage makes more features available such as remote debugging, remote backup, JMX, FTP, Custom SSL, websockets and polling etc.
![cluster access public IP](05-cluster-access-public-ip.png)

Access levels make using and managing the PaaS Cluster fully efficient, convenient and easy. Each type of customer is provided with their own range of rights and limitations making the system well structured and organized.


## What's next?

* [What is Platform-as-a-Service](/what-is-paas-and-caas/)
* [Dashboard Guide](/dashboard-guide/)
* [Application Lifecycle](/how-to-manage-application-lifecycle/)
* [Shared Load Balancer](/shared-load-balancer/)
* [Public IP](/public-ip/)