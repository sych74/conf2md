---
draft: false
aliases: "/nodejs-center/"
seoindex: "index, follow"
seotitle: "Node.js Dev Center"
seokeywords: "nodejs, nodejs paas, nodejs cloud, nodejs hosting, nodejs application, nodejs hosting specifics, nodejs versions, nodejs application server, nodejs application deployment, nodejs domain management, nodejs scaling, nodejs automatic scaling, nodejs package managers, nodejs process managers"
seodesc: "Find out the main tools and features available on the PaaS to provide the required level of Node.js hosting."
menu:
    docs:
        title: "Node.js Dev Center"
        url: "/nodejs-center/"
        weight: 10
        parent: "node-js"
        identifier: "nodejs-center.md"
---

# Node.js Hosting

The platform provides an out-of-box integration of the fast, lightweight and highly scalable NodeJS application server. It is automatically supplied with numerous optimization and management tools to make the hosting process maximally convenient for developers. In this article, we’ll go through the main tools and features available on the platform to provide the required level of Node.js hosting.

![Node.js cloud hosting](01-node-js-cloud-hosting.png)

Use the table of content below to find required information within the guide quicker:

- [Node.js Environment Hosting](#nodejs-environment-hosting)
- [Node.js Versioning](#nodejs-versioning)
- [Node.js Application Deployment](#nodejs-application-deployment)
- [Node.js Package Managers](#nodejs-package-managers)
- [Node.js Process Managers](#nodejs-process-managers)
- [Domains Management](#domains-management)
- [Automatic Vertical Scaling](#automatic-vertical-scaling)
- [Manual Horizontal Scaling](#manual-horizontal-scaling)
- [Automatic Horizontal Scaling](#automatic-horizontal-scaling)


## Node.js Environment Hosting

To run your Node.js application, you need to [set up](/setting-up-environment/) the appropriate environment using the powerful and intuitive **Topology Wizard**. Switch to the ***Node.js*** tab, select the required engine version for your application server and add any other [software stack](/software-stacks-versions/) required. If needed, adjust other parameters, such as cloudlets and nodes count, Public IPv4 and IPv6, etc.

![Node.js topology wizard](02-nodejs-topology-wizard.png)

{{%tip%}}**Note:** Each instance is a completely [isolated container](/isolated-containers/), fully independent and uninfluenced by other stacks. Additionally, scaled out nodes are automatically distributed across the physical servers (or VMs) ensuring [high availability](/isolated-containers/#high-availability-for-applications).{{%/tip%}}


## Node.js Versioning

Currently (at the time of this writing), the following Node.js versions are supported:

- 14.21.3
- 16.20.0
- 18.20.4
- 20.17.0
- 21.7.3
- 22.5.1
- 22.8.0

{{%tip%}}The up-to-date list of the releases available on the platform is provided via the dedicated, regularly (weekly) updated [Software Stack Versions](/software-stacks-versions/#engines) document.{{%/tip%}}

![Node.js versions](03-nodejs-versions.png)

You can select the required [version of Node.js](/nodejs-versions/) directly from the topology wizard during the creation of a new environment and adjust it for the existing one via [container redeployment](/container-redeploy/).


## Node.js Application Deployment

The platform automates the deployment process for the managed NodeJS application servers using:

* application *archive* uploaded from the local machine or via external URL
* remote *VCS* repository (e.g. GitHub)

![deploy Node.js application](04-deploy-nodejs-application.png)

{{%tip%}}**Tip:** Usually, due to the [ports auto-redirect](/container-ports/#ports-auto-redirect) algorithm, the deployed projects are instantly accessible without any additional manipulations. Herewith, for greater accuracy, you can manually exclude some of the services from the auto-redirect search by listing the appropriate ports via the ***REDIRECT_EXCLUDE_PORTS*** [variable](/container-variables/).{{%/tip%}}

You can read the appropriate documents to learn more about the deployment of the Node.js applications:

- [Deployment Manager](/deployment-manager/)
- [Deployment Guide](/deployment-guide/)
- [Auto-Deploy Overview](/git-svn-auto-deploy/)
- [Deployment Hooks](/deployment-hooks/)


## Node.js Package Managers

For greater convenience, each NodeJS application server contains a built-in development tool called **[Package Manager](/nodejs-package-managers/)**, which provides standardization and automation of the installation, update, configuration, and removal processes.

The platform supports two types of package managers:

* ***[npm](https://www.npmjs.com/)*** - manages your project requirements by installing the additional modules, packages, and ready-to-use applications 
* ***[yarn](https://classic.yarnpkg.com/en/)*** - operates the same requirements as in *npm* (so no changes are required for the existing applications), while providing higher speed, reliability, and convenience

By default, the *npm* package manager is used for the NodeJS application servers, but, if necessary, it can be easily switched to *yarn*. For that, access the [container variables](/container-variables/) frame and set the appropriate ***PACKAGE_MANAGER*** value (either *npm* or *yarn*).

![Node.js package manager](05-nodejs-package-manager.png)


## Node.js Process Managers

**[Process Managers](/nodejs-process-managers/)** provide the ability to control application lifecycle, monitor running services and maintain the project operability. The platform provides support of the following process managers for the NodeJS stack:

- ***[npm](https://docs.npmjs.com/cli/v8/commands/npm-run-script)*** - provides the ability to start the application
- ***[pm2](https://pm2.keymetrics.io/)*** - provides a huge variety of application management features, including the launched Node.js processes monitoring
- ***[forever](https://www.npmjs.com/package/forever)*** - allows running your Node.js processes continuously and automatically restarting them upon failure

Users can choose the necessary process manager during container [redeployment](/container-redeploy/) or by adjusting the ***PROCESS_MANAGER*** [variable](/container-variables/) (using *forever*, *npm*, or *pm2* as value, container restart is needed to apply new options).


## Domains Management

Your Node.js application can be easily supplemented with the [custom domain](/custom-domains/) name to be used instead of the default one. There are two options based on your environment topology:

* **CNAME redirect** if using *Shared Load Balancer*; is recommended for ***dev*** and ***test*** environments
* **DNS A Record** if using *Public IP*; can handle high traffic load and is suitable for ***production*** environments

Also, you can quickly switch traffic between your environments (e.g. to redirect customers to the newer application version without downtime) by utilizing the [swap domains](/swap-domains/) functionality or with the help of the ***SwapExtIps*** [API](https://docs.jelastic.com/api/#!/api/environment.Binder-method-SwapExtIps)/[CLI](/cli-ip-swap/) method.

![Node.js domain management](06-nodejs-domain-management.png)


## Automatic Vertical Scaling

The platform dynamically provides the exact amount of resources (RAM and CPU) required by your nodes according to the current load with no manual intervention required. As a result, you [never overpay for unused resources](https://www.virtuozzo.com/company/blog/deceptive-cloud-efficiency-do-you-really-pay-as-you-use/) and save your time as the platform eliminates the need to handle the load-related adjustments or architectural changes.

You just need to set the upper [cloudlets](/cloudlet/) limit (each one equals to *128 MiB* of RAM and *400 MHz* of CPU) for your NodeJS application server and everything else will be handled by platform automatically.

![Node.js vertical scaling](07-nodejs-vertical-scaling.png)

Refer to the [automatic vertical scaling](/automatic-vertical-scaling/) documentation for more information.


## Manual Horizontal Scaling

To scale out/in NodeJS application servers, you need to access the topology wizard and click the **+/-** buttons within the *Horizontal Scaling* section to set the required number of nodes. Also,  starting with the 5.5 platform version, you can adjust the preferred scaling mode:

* ***Stateless*** - simultaneously creates all new nodes from the base image template
* ***Stateful*** - sequentially copies file system of the master container into the new nodes

![Node.js horizontal scaling](08-nodejs-horizontal-scaling.png)

The maximum number of the same-type servers within a single environment layer depends on a particular hosting provider settings (usually this limit stands for 16 nodes and can be enlarged by sending the appropriate request to support).

Also, for the proper requests distribution, a [load balancer](/load-balancing/) instance is automatically added upon NodeJS server scaling. Refer to the [horizontal scaling](/horizontal-scaling/) documentation for more details.


## Automatic Horizontal Scaling

Access the environment **Settings > Monitoring > Auto Horizontal** Scaling section to set up special tunable triggers, which allow to increase or decrease the number of nodes due to the application load. Configure type of resource to be monitored (*CPU*, *RAM*, *Network*, *Disk*) and the exact condition of scaling.

![Node.js automatic horizontal scaling](09-nodejs-automatic-horizontal-scaling.png)

Learn more about [automatic horizontal scaling](/automatic-horizontal-scaling/) in the linked document.

In addition, hosting at the platform allows using other inbuilt tools and features, for example:

- Custom or Built-In SSL
- Public IPv4 and IPv6
- A wide range of managed software stacks
- Container firewalls, endpoints, and environment isolation
- User-friendly UI and direct SSH access for management
- Open API and Cloud Scripting for automation
- Pay-as-you-use pricing model
- Collaboration functionality for teamwork
- Multi-cloud distribution

As you can see, the platform provides all the necessary conditions for smooth Node.js hosting!


## What's next?

* [Setting Up Environment](/setting-up-environment/)
* [Dashboard Guide](/dashboard-guide/)
* [Deployment Guide](/deployment-guide/)
* [SSH Access](/ssh-access/)
* [Node.js Tutorials](/nodejs-tutorials/)