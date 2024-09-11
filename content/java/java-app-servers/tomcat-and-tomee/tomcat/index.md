---
draft: false
title: "Tomcat Server"
url: "/tomcat/"
aliases: ["/tomcat/", "/tomcat8/", "/tomcat8-9/", "/jelastic-tomcat7/"]
seoindex: "index, follow"
seotitle: "Tomcat Server"
seokeywords: "tomcat, tomcat server, apache tomcat, tomcat hosting, java tomcat, tomcat deploy, create tomcat, tomcat clustering, tomcat scaling, tomcat configurations, tomcat security, change tomcat version"
seodesc: "Guide on how to install Tomcat latest version, configure this Java web server and its load balancing, deploy application, and improve Tomcat security on the platform."
menu:
    docs:
        title: "Tomcat Server"
        url: "/tomcat/"
        weight: 10
        parent: "tomcat-and-tomee"
        identifier: "tomcat.md"
---

# Tomcat Server Cloud Hosting

Apache Tomcat occupies the leading positions among Java servers for running web applications. Considering the demand, we compiled the main details on the Tomcat web server management on the platform - installation, configuration, load balancing, application deployment, and security enhancement.

{{%tip%}}**Note:** This template utilizes a modern ***systemd*** initialization daemon.{{%/tip%}}

## Create Tomcat Server

The Platform-as-a-Service provides easy steps for Tomcat installation.

1\. Log in to the PaaS dashboard at the chosen hosting service provider and click the **New Environment** button.

2\. Pick a desirable **Tomcat** version for your application server, as shown in the picture below. The cloud platform allows you to use Apache Tomcat versions starting from 7 up to the latest Tomcat 10, depending on your application requirements. All you need is to choose from the versions available in the drop-down list:

![new Tomcat environment](01-tomcat-new-environment.png)

Once the environment is created, you have ready to use the Tomcat application server installed there. To check if Tomcat is running, click the **Open in Browser** button next to the application server.

![Tomcat environment created](02-tomcat-environment-created.png)

If you can see a Tomcat's welcome page in your browser, the server is installed correctly.

![open Tomcat in browser](03-open-tomcat-in-browser.png)

The application server operates in a separate container (node), an isolated virtualized instance. Each Tomcat container has its own private IP and unique DNS record.

![Tomcat node ID](04-tomcat-node-id.png)


## Change Tomcat Version

If you need to change (update) the server's version, you can do this any time [without losing data or configurations](/container-redeploy/).

Just click the **Redeploy Containers** button next to the Apache Tomcat server nodes.

![Tomcat redeploy button](05-tomcat-redeploy-button.png)

Select new Tomcat and JDK engine versions in the appeared dialog and confirm the change.

![container redeploy dialog](06-container-redeploy-dialog.png)


## Tomcat Clustering and Scaling

The platform makes Tomcat hosting truly flexible due to automatic scaling (both vertical and horizontal) and clustering.

For the manual adjustment of the existing Tomcat server(s), click **Change Environment Topology**:

![change environment topology button](07-change-environment-topology-button.png)

### Automatic Vertical Scaling

Automatic vertical scaling is possible due to the platform's ability to dynamically change allocated resources (RAM and CPU) for a server. Adjustment is performed automatically, according to the Tomcat server's current demands. This feature guarantees you [never overpay for unused resources](https://www.virtuozzo.com/company/blog/deceptive-cloud-efficiency-do-you-really-pay-as-you-use/) and saves your time by eliminating the necessity of manual handling of the load-related adjustments.

In order to set up automatic resource provisioning for your Tomcat server, open the environment topology wizard and specify the upper scaling limit in [cloudlets](/cloudlet/) (128 MiB and 400 MHz each):

![vertical scaling cloudlets](08-vertical-scaling-cloudlets.png)

Your application will work within these limits reducing resource allocation when the load goes down and increasing when it goes up. Thus, you only pay for the resources that are actually consumed. For more information, please refer to the documentation about [automatic vertical scaling](/automatic-vertical-scaling/).

### Manual Horizontal Scaling

You can adjust the number of Tomcat nodes via the dedicated *Horizontal Scaling* section in the topology wizard. Use the **+/-** buttons or provide the required number via the central part. Click the **gear** icon next to the slider to access the advanced management options.

![manual horizontal scaling](09-manual-horizontal-scaling.png)

Also, based on your needs, you can select one of the two scaling modes for the layer:

- ***Stateless*** - simultaneously creates all the new nodes from the base image template
- ***Stateful*** - sequentially copies file system of the master container into the new nodes

![horizontal scaling mode](10-horizontal-scaling-mode.png)

The maximum number of the same-type servers within a single environment layer depends on a particular hosting provider settings (usually, this limit stands for 16 nodes and can be adjusted by sending a request to support). You can check the exact value within the **Quotas & Pricing > [Account Limits](/quotas-system/)** information frame.

Upon scaling out a single node, NGINX (you can manually switch to another one) load balancing is added automatically. [Load Balancer](/load-balancing/) represents a frontend that receives all the incoming requests and evenly distributes them between backends (application servers).

Please, find more details about manual [horizontal scaling](/horizontal-scaling/) in the documentation.

### Automatic Horizontal Scaling

Automatic horizontal scaling can be implemented through tunable triggers, which monitor the changes in the application's load and increase or decrease the number of nodes.

To configure a trigger for the automatic horizontal scaling, use the **Settings** button for the desired environment and switch to the ***Auto Horizontal Scaling*** section to proceed.

![automatic horizontal scaling](11-automatic-horizontal-scaling.png)

Click the **Add** button to configure the triggers for a specific layer and resource type (CPU, RAM, Network, Disk) within your environment. Specify the required conditions of scaling and **Apply** changes.

![Tomcat automatic horizontal scaling](12-tomcat-automatic-horizontal-scaling.png)

Find out more about [automatic horizontal scaling](/automatic-horizontal-scaling/) in the corresponding document.

### Automatic Tomcat Clustering

The platform can automatically configure a reliable Tomcat Cluster of the following topology in a single click:

<img src="13-tomcat-auto-clustering-scheme.svg" alt="Tomcat auto-clustering scheme" width="250" >

Just enable the **[Auto-Clustering](/auto-clustering/)** option via the dashboard, as it is shown in the picture below:

{{%note%}}**Note:** The **Auto-Clustering** feature for Tomcat and TomEE is available since the following stack versions:

- **Tomcat** - *10.0.5*; *9.0.45*; *8.5.64*; *7.0.108*
- **TomEE** - *9.0.0-M3*; *8.0.5*

Older versions can still operate with the preceding [clustering](/tomcat-server-clustering/) and [session replication](/session-replication/) functionality instead.{{%/note%}}

![enable Tomcat auto-clustering](14-enable-tomcat-auto-clustering.png)


## Deploy Application to Tomcat Environment

There are several options for [deploying an application](/deployment-guide/) at the platform, but the most straightforward way is to upload an archive to the [Deployment Manager](/deployment-manager/).

{{%tip%}}**Tip:** Tomcat and TomEE servers are provided with a special ***HOT_DEPLOY*** variable (not set by default) that defines whether the server should be restarted (*false*, *disabled*, *0*) or not (*true*, *enabled*, *1*) during the application deployment.

![Tomcat hot deploy variable](15-tomcat-hot-deploy-variable.png)

**Hot deploy** (without restart) is relatively faster and allows avoiding downtime during the deployment process. However, it is not supported by some applications and thus is disabled by default.{{%/tip%}}

1\. Open **Deployment Manager** at the bottom of the dashboard and click the **Upload** button in the *Archive* tab.

![deployment manager](16-deployment-manager.png)

2\. **Browse** your local files and **Upload** your project (or provide it via ***URL***). Common Java archives have *WAR*, *EAR*, or *ZIP* extension.

![upload application archive](17-upload-application-archive.png)

3\. Hover over the required package in the list and click the appeared **Deploy to** button:

![deploy application from archive](18-deploy-application-from-archive.png)

4\. Choose the appropriate environment, specify a context name (or leave the default ROOT value) and start deploying the application.

![application deployment dialog](19-application-deployment-dialog.png)

{{%tip%}}**Note:** At this step, you can also add [deployment hooks](/deployment-hooks/) to execute your custom scripts before or after the application deployment.{{%/tip%}}

5\. When the process is completed, you can see your project within deployments of the environment.

![application deployed](20-application-deployed.png)

There are more options for deploying your application to Tomcat, for example, via Git/SVN using [Maven build node](/java-vcs-deployment/). For more information, refer to the [Deployment Guide](/deployment-guide/).


## Tomcat Configurations

This chapter will cover some settings and features that help optimize your work with the Tomcat web server.

### Environment Variables

In order to make your application more portable and flexible, you can use **environment variables** instead of specifying the required values in the application code each time. The platform provides you with many Tomcat [default environment variables](/environment-variables/) for the most common stack data. You can also add [custom environment variables](/custom-environment-variables/) for your Tomcat node to make its management even more convenient.

### Configuration Files

The Tomcat configuration files are available for editing right from the dashboard. To access them, click the **Config** button next to the server.

![configuration file manager](21-configuration-file-manager.png)

The most frequently used directories are added to the *Favorites* list for quick access. You can learn more about [Tomcat server configurations](/java-application-server-config/) in the linked document.

### Tomcat Security Settings

In order to restrict access to your project deployed to the Tomcat server, we recommend two possible solutions: set up **user authentication** and **deny access** to your web application from specific IP addresses. The detailed instruction is described in the article on how to [Secure Tomcat Hosting](https://www.virtuozzo.com/company/blog/restrict-access-tomcat-web-application-hosting/).

Another way to ensure the security of your applications is the **Container Firewall** feature. It lets you control your node's availability both from inside and outside of the platform. Configure Tomcat container firewall using the information from the [Container Firewall Management](/custom-firewall/) article.

![Tomcat firewall](22-tomcat-firewall.png)

### Multiple Domains on Single Tomcat Server

You can set up multiple domain names on the Tomcat server to increase the usability, efficiency, and scalability of your application, as well as save your costs without having to configure separate instances. For this, adjust the Tomcat configuration files as described in the [multiple domains](/multiple-domains-tomcat-server/) instruction.

![Tomcat multiple domains](23-tomcat-multiple-domains.png)

As you can see, the platform makes Tomcat hosting easy and flexible. The cloud platform provides a wide range of already predefined settings for you not to bother about routine tasks. At the same time, it leaves the server fully customizable for specific complex configurations. Get started with effortless Tomcat cloud hosting from the [PaaS](https://www.virtuozzo.com/application-platform/) and enjoy the benefits in a turnkey package.


## What's next?

* [TomEE](/tomee/)
* [Java Application Server Configuration](/java-application-server-config/)
* [Tomcat Multiple Domains](/multiple-domains-tomcat-server/)
* [Deployment Guide](/deployment-guide/)
* [Environment Variables](/environment-variables/)
* [Tomcat Security](/tomcat-security/)