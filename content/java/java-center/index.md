---
draft: false
aliases: "/java-center/"
seoindex: "index, follow"
seotitle: "Java Dev Center"
seokeywords: "java, java paas, java cloud, java hosting, java application, java hosting specifics, java versions, java application servers, java application deployment, java domain management, java scaling, java automatic scaling, java clusterization, java database connection"
seodesc: "Get acquainted with the distinctive features of scalable and highly-available Java cloud hosting within the PaaS."
menu:
    docs:
        title: "Java Dev Center"
        url: "/java-center/"
        weight: 10
        parent: "java"
        identifier: "java-center.md"
---

# Java Developer’s Center

{{%imageLeft%}}<img src="01-java-center-illustration.png" alt="Java center illustration" width="120"/>{{%/imageLeft%}}

Currently multilingual, the platform was initially created as pure Java Cloud and still maintains a primary focus on this programming language. The maturity of the platform technology was recognized by the Java community with [Duke’s Choice Award](https://www.virtuozzo.com/company/blog/duke-choice-award-2018-winner/) already twice (in 2012 and 2018). This guide acquaints you with the distinctive features of Java hosting within the platform and lets you easily get started with a broad functionality list.

Use the table of content below to find required information within the guide quicker:

- [Java Versions](#java-versions)
- [Java Application Servers](#java-application-servers)
- [Java Environment Creation](#java-environment-creation)
- [Java Application Deployment](#java-application-deployment)
- [Domains Management](#domains-management)
- [Automatic Vertical Scaling](#automatic-vertical-scaling)
- [Horizontal Scaling: Manual and Automatic](#horizontal-scaling-manual-and-automatic)
- [Java Clusterization](#java-clusterization)
- [Database Connection to Java Application](#database-connection-to-java-application)


## Java Versions

Currently (at the time of this writing), the following Java versions and distributions are available:

* **[AdoptOpenJDK](https://adoptopenjdk.net/)**: 8.0.312; 11.0.13; 13.0.2; 14.0.2; 15.0.2; 16.0.2
* **[Alibaba Dragonwell](https://dragonwell-jdk.io/)**: 8.11.12
* **[Amazon Corretto](https://aws.amazon.com/corretto/)**: 8.422.05.1; 11.0.24.8.1; 15.0.2.7.1; 16.0.2.7.1; 17.0.12.7.1; 18.0.2.9.1; 19.0.2.7.1; 20.0.2.10.1; 21.0.4.7.1
* **[Eclipse OpenJ9](https://www.eclipse.org/openj9/)**: 0.11.0 (8u192-b12; 11.0.1); 0.15.1 (8u222-b10; 11.0.4); 0.17.0 (8u232-b09; 11.0.5; 13.0.1); 0.18.1(8u242-b08; 11.0.6; 13.0.2) 0.20.0 (8u252-b09; 11.0.7); 0.21.0 (8u262-b10; 8u265-b01; 11.0.8; 14.0.2); 0.22.0 (15.0.0); 0.23.0 (8u272-b10; 11.0.9); 0.24.0 (8u282-b08; 11.0.10); 0.25.0-16; 0.26.0 (8u292-b10; 11.0.11); 0.27.0 (8u302-b08; 11.0.12); 0.29.0 (8u312-b07; 11.0.13); 0.30.0 (8u322-b06; 11.0.14); 0.32.0 (8u332-b09; 11.0.15); 0.33.1 (8u345-b01; 11.0.16); 0.35.0 (8u352-b08; 11.0.17); 0.36.1 (8u362-b09; 11.0.18); 0.38.0 (8u372-b07; 11.0.19); 0.41.0 (8u392-b08; 11.0.21); 0.43.0 (8u402-b06; 11.0.22)
* **[Eclipse Temurin](https://projects.eclipse.org/projects/adoptium.temurin)**: 8.0.422; 11.0.24; 17.0.12; 18.0.2.1; 19.0.2; 20.0.2; 21.0.2
* **[GraalVM CE](https://www.graalvm.org/)** (currently, for *Java Engine* and *Maven* only): 19.3.1; 20.2.0; 21.3.0; 22.3.3
* **[Liberica JDK](https://bell-sw.com/)**: 8.0.322; 11.0.14; 13.0.2; 14.0.2; 15.0.0; 16.0.0; 17.0.2
* **[Oracle JDK Dev](https://www.oracle.com/technetwork/java/javase/downloads/index.html)**: 7.0_79; 8.0_202; 11.0.2
* **[Oracle OpenJDK](http://jdk.java.net/)**: 7.0.261; 8.0.412; 11.0.24; 13.0.2; 14.0.2; 15.0.2; 16.0.2; 17.0.2; 18.0.2.1; 19.0.2; 20.0.2; 21.0.2; 22.0.2; 23.ea-b31
* **[Zulu Community](https://www.azul.com/downloads/zulu/)**: 7.0.352; 8.0.422; 11.0.24; 13.0.9; 14.0.2; 15.0.10; 16.0.2; 17.0.12; 18.0.2.1; 19.0.2; 20.0.2; 21.0.4; 22.0.2

The *6th*, *9th*, *10th*, and *12th* Java versions cannot be created within the new environments anymore due to end-of-life of the respective releases. However, the already existing instances remain fully operable (including redeploy, cloning, horizontal scaling).

{{%tip%}}The up-to-date list of the releases available on the platform is provided via the dedicated, regularly (weekly) updated [Software Stack Versions](/software-stacks-versions/#engines) document.{{%/tip%}}

You can choose the preferred version while creating an environment, or change it later. These procedures are described in the [Java Versions](/java-versions/) document.


## Java Application Servers

Within a wide variety of software stacks, the platform supports a pure [Java Engine](/java-engine/) and the following Java application servers:

- [GlassFish](/glassfish/)
- [Jetty](/eclipse-jetty/)
- [Payara](https://www.virtuozzo.com/company/blog/glassfish-payara-auto-clustering-cloud-hosting/)
- [Spring Boot](https://www.virtuozzo.com/company/blog/hosting-spring-boot-java-applications/)
- [Tomcat](/tomcat/)
- [TomEE](/apache-tomee/)
- [WildFly](/wildfly/)

Read the documentation below for additional information on Java servers specifics within the platform:

- [Java App Server Configuration](/java-application-server-config/)
- [Java Garbage Collection](https://www.virtuozzo.com/company/blog/garbage-collection/)
- [Java Agent](/javaagent/)
- [Java Tutorials](/java-tutorials/)


## Java Environment Creation

To host a Java application, you need to create an appropriate environment. Just open the ***[topology wizard](/setting-up-environment/)*** in your PaaS dashboard, navigate to the **Java** language tab, pick the desired Java application server, databases, and other stacks. If needed, customize settings (such as cloudlets, disk space, region, etc.) and click **Create**.

![Java environment creation](02-java-environment-creation.png)

All added servers represent [fully isolated containers](/isolated-containers/), located on different hosts for more availability, while isolation eliminates the risks of interfering with one another. You can attach the [public IP](/public-ip/) address to any of these servers for being accessed directly. Otherwise (i.e. if using default settings), the incoming requests sent to your application will be proxied by [Shared Load Balancer](/shared-load-balancer/).


## Java Application Deployment

After environment creation, you can deploy your Java application. The platform fully automates the deployment process allowing you to get the project up and running effortlessly.

The following deployment methods are supported:

- via the application ***archive*** - *.war*, *.zip*, *.jar*, and *.ear* archives
- from the *GIT/SVN* remote ***repository***, using the *Maven* build node

![Java application deployment](03-java-application-deployment.png)

You can read the appropriate documents to learn more about the deployment of the Java applications:

- [Deployment Guide](/deployment-guide/)
- [Maven Build Node](/java-vcs-deployment/)
- [Auto-Deploy Overview](/git-svn-auto-deploy/)
- [Deployment Hooks](/deployment-hooks/)

There are also separate instructions for managing your projects via [Gitblit](/gitblit/) and [WebDAV](/remote-access-via-webdav/).


## Domains Management

You can bind a [custom domain](/custom-domains/) name to your application’s URL and use it instead of the default environment domain:

* **CNAME redirect** if using *Shared Load Balancer*; is recommended for ***dev*** and ***test*** environments
* **DNS A Record** if using *public IP*; can handle high traffic load and is suitable for ***production*** environments

Also, with the help of the [swapping domains](/swap-domains/) feature or the ***SwapExtIps*** [API](https://docs.jelastic.com/api/#!/api/environment.Binder-method-SwapExtIps)/[CLI](/cli-ip-swap/) method, you can upgrade and modify your application with zero downtime (i.e. your users won’t notice any interruption).

![Java domains management](04-java-domains-management.png)

{{%tip%}}**Tip:** The platform allows using multiple domains within a single environment to increase its usability, efficiency, and scalability, while simultaneously saving your costs by avoiding a need to set up separate instances for different apps. Check the appropriate examples below:

- [Multiple Domains with Public IP](/multiple-domains/)
- [Multiple Domains for Tomcat](/multiple-domains-tomcat-server/)
- [Multiple Domains for GlassFish](/multiple-domains-glassfish/){{%/tip%}}


## Automatic Vertical Scaling

The platform dynamically provides the number of cloudlets (i.e. RAM and CPU resources), which are required by your application to handle the current load. Just specify the maximum limit, and everything else will be performed by the platform automatically - no manual intervention required. This feature is called ***[automatic vertical scaling](/automatic-vertical-scaling/)*** and ensures that you never overpay for unused capacities without experiencing a resource shortage.

![automatic vertical scaling](05-automatic-vertical-scaling.png)

To set or change the vertical scaling limit, just use the appropriate slider within the topology wizard:

![configure Java vertical scaling](06-configure-java-vertical-scaling.png)


## Horizontal Scaling: Manual and Automatic

In case your application becomes highly popular and a single node is not enough, feel free to scale it [horizontally](/horizontal-scaling/). In order to ensure even more reliability and high-availability, all the newly added nodes are created on the different hardware nodes.

![Java horizontal scaling](07-java-horizontal-scaling.png)

Click the **+/-** buttons within the *Horizontal Scaling* section of the topology wizard to set the required number of nodes (load balancer will be added automatically).

Also, you can adjust the preferred [scaling mode](/horizontal-scaling/#scaling-modes):

* ***Stateless*** - simultaneously creates all of the new nodes from the base image template
* ***Stateful*** - sequentially copies file system of the master container into the new nodes

Horizontal scaling can be performed not only manually but also automatically based on the current load on the node, which is monitored through the tunable triggers.

Within the **Settings > Monitoring > [Auto Horizontal Scaling](/automatic-horizontal-scaling/)** section, you can adjust the scaling conditions due to your needs, i.e. the lower/upper limit (percentage) for the specified resource type during a certain period. If the load stays out of the set limits, the nodes removal/addition process will be called automatically.

There are five different types of resources, which are monitored by triggers:

- CPU
- Memory (RAM)
- Network
- Disk I/O
- Disk IOPS

![Java auto horizontal scaling](08-java-auto-horizontal-scaling.png)

The trigger starts monitoring the resource consumption immediately after addition, and when the usage level exceeds the stated limit, a trigger becomes invoked. Subsequently, if the load persists for a defined period, it will be executed, adjusting the number of nodes.


## Java Clusterization

The embedded application server clustering feature provides replication of sessions between pairs of nodes and eliminates the necessity of additional software or Memcached usage for increasing application availability.

The platform provides automated session replication between *Tomcat* and *TomEE* servers with the help of multicast to gain web application high availability within the Java cluster. This **[High-Availability](/session-replication/)** feature can be enabled in the wizard during environment creation or topology tuning.

![Java clusterization](09-java-clusterization.png)

The newer modern **[Auto-Clustering](/auto-clustering/)** solution is provided for the *GlassFish*, *Payara*, and *WildFly* stacks:

* [Out-of-Box GlassFish & Payara Clustering](https://www.virtuozzo.com/company/blog/glassfish-payara-auto-clustering-cloud-hosting/)
* [WildFly Automatic Micro Clustering and Scaling](https://www.virtuozzo.com/company/blog/wildfly-managed-domain-in-containers-auto-micro-clustering-and-scaling/)

![Java auto-clustering](10-java-auto-clustering.png)


## Database Connection to Java Application

A set of scalable and fully manageable database servers can be easily installed within the Java environment. To establish the connection, adjust your application following the instruction based on the database you require:

- [MySQL and MariaDB Connection](/connection-to-mysql/)
- [PostgreSQL Connection](https://www.virtuozzo.com/company/blog/java-connection-to-postgresql/)
- [MongoDB Connection](/connection-to-mongodb/)

The platform provides high-quality Java hosting with improved availability, redundancy, and scalability strengths for your application.


## What's next?

* [Setting Up Environment](/setting-up-environment/)
* [Dashboard Guide](/dashboard-guide/)
* [Deployment Guide](/deployment-guide/)
* [SSH Access](/ssh-access/)
* [Java Tutorials](/java-tutorials/)