---
draft: false
title: "Setting Up Environment"
aliases: "/setting-up-environment/"
seoindex: "index, follow"
seotitle: "Setting Up Environment"
seokeywords: "setting up environment, topology wizard, create environment, create new environment, configure environment, environment wizard, environment programming language, environment topology, configure environment nodes, environment cost"
seodesc: "This tutorial will guide you through the steps required to create a new environment in the platform. Learn about the specifics of the topology wizard - a powerful UI for environment creation."
menu: 
    docs:
        title: "Setting Up Environment"
        url: "/setting-up-environment/"
        weight: 10
        parent: "environment-management"
        identifier: "setting-up-environment.md"
---

# Setting Up Environment

The first step of any application hosting is a creation of the [environment](/paas-components-definition/#environment) with the required isolated containers. The platform provides a powerful and intuitive UI to create and configure environments up to your specific needs. This document will guide you through all the needed steps, giving an extended explanation of available specifics and features.

1\. Log in to the platform dashboard and click the **New Environment** button in the upper-left corner.

![PaaS main buttons](01-paas-main-buttons.png)

2\. Within the opened ***topology wizard*** dialog, you can set up all the necessary customizations. We recommend performing adjustments in the following order:

* [choose programming language](#choosing-programming-language-or-specific-deployment-option) or specialized deployment solution (*Docker Engine* or *Kubernetes Cluster*)
* [set up topology](#configuring-topology) by adding required software stacks
* [configure nodes](#configuring-nodes-resources-and-specifics) resources and specifics
* review estimations, name the environment and [confirm the creation](#reviewing-and-confirming-environment-creation)

![configure environment via wizard](02-configure-environment-via-wizard.png)

Below, we'll review each of these points in detail, providing explanations on all of the available possibilities. The process may seem complex at first, but after familiarizing yourself, you'll be able to configure a new (or adjust existing) environment in under a minute.


## Choosing Programming Language or Specific Deployment Option

As the first step of your environment creation, you need to select the deployment solution required for your project. PaaS is an extremely versatile platform that supports multiple options for application development and hosting thus it suits even the most demanding clients.

1\. The most common and recommended choice (unless you are pursuing a specific application/architecture) is **certified containers**. These [stacks](/software-stacks-versions/) are specifically configured and managed by the platform (e.g. version updates, security patches). By default, they support all platform features (scaling, automated deployment, redeploy, SSL, etc.) for the most smooth and convenient hosting and development.

![environment programming languages in wizard](03-environment-programming-languages-in-wizard.png)

Click on the tab with the required programming language (*Java*, *PHP*, *Ruby*, *.NET*, *Node.js*, or *Python*) tab to proceed with the platform certified containers.

2\. The other deployment options are available via the *Custom* tab. All the variants listed below utilize the basic platform's [system container](/what-are-system-containers/) (so-called OS container), which makes them compatible with the most (but not all) of the platform-distinguishing features (e.g. vertical and horizontal scaling).

![topology wizard docker tab](04-topology-wizard-docker-tab.png)

* **Custom Container Images** - any *Docker image* (based on the [supported OS](/docker-supported-distributions/)) deployed into the system container. Compared to the **managed containers**, this option provides access to a greater variety of solutions, search the entire Docker Hub registry or use your private repository. However, the software operability and compatibility with the platform cannot be guaranteed as the content is managed by respective image maintainers. It's recommended to build custom container images based on [platform certified images](https://hub.docker.com/u/jelastic) using [FROM instruction](https://docs.docker.com/engine/reference/builder/#from).

* **Docker Engine** - a *[Docker Engine CE](https://www.virtuozzo.com/company/blog/docker-engine-automatic-install-swarm-connect/)* deployed into the system container. It provides access to all the Docker native functionality, including deployment, scaling, and management of multiple [application containers](/what-are-application-containers/) inside.

* **Kubernetes Cluster** - ready-to-go *[Kubernetes cluster](/kubernetes-cluster/)* with a preconfigured control plane and worker nodes created based on the system containers. The deployment, scaling, and orchestration of the microservices inside are handled by Kubernetes control units, while the platform scales and manages control plane and worker nodes.

3\. Also, it is recommended to select the preferred [region](/environment-regions/) (if available) before proceeding further.

![environment regions list](05-environment-regions-list.png)


## Configuring Topology

You can configure environment topology ([layers](/paas-components-definition/#layer) structure) via the left part of the wizard. Сonsider it as a constructor that helps you to create your environment. Here, the following blocks are available:

* **[Load Balancers](/load-balancing/)** - stacks that operate as an entry point for the environment to distribute incoming request and create even load on other nodes
* **[Application Servers](/tomcat/)** (compute nodes) - web servers that run your application
* **[Databases](/database-hosting/)** (*SQL* & *NoSQL*) - database solutions to store and manage data
* **[Cache Node](/memcached/)** - a Memcached object caching system for speeding up web applications through alleviating database load
* **[Shared Storage](/shared-storage-container/)** - dedicated storage node with NFSv4 support, enlarged disk space and optimized performance
* **[Elastic VPS](/vps/)** - virtual private servers on top of the *CentOS*, *Ubuntu*, *Debian*, and *Windows* OS
* **[Build Node](/java-vcs-deployment/)** - a build automation tool for Java projects
* **Extra** (custom layers) - any of the stacks mentioned above

![environment topology builder ui](06-environment-topology-builder-ui.png)

{{%tip%}}**Tip:** The sequence of blocks displayed above is the default order. However, you can mix and match them in any preferable way to create your custom topologies.

![custom topology order](06-1-custom-topology-order.png)
{{%/tip%}}

1\. The platform offers a number of the most popular options for each of these sections based on the default role. If you want to add a [stack](/software-stacks-versions/) of a different role, click the **More** option at the bottom of the list. Also, you can use **Search** to quickly find any platform-managed stack.

![categorized stacks with search](07-categorized-stacks-with-search.png)

{{%tip%}}**Tip:** If you cannot find a required software solution, you can add it as a [custom container](/custom-containers-deployment/) from Docker Hub or your private repository.{{%/tip%}}

2\. An **SSL** protection can be configured for your environment via the same-named section. Here, two options are available:

* ***[Built-In SSL](/built-in-ssl/)*** - enables an already trusted SSL certificate, avoiding any additional checks and saving your time on the certificate validation. However, it is applied to the default environment domain name only (i.e. with the hoster's domain at the end) and does not work if [public IP](/public-ip/) is attached to your servers.
* ***[Custom SSL](/custom-ssl/)*** - shows the pre-conditions of using your custom SSL certificates for the environment. Click the **Enable** button to automatically fulfill the requirements (e.g. enable Public IP) and refer to the linked instruction for further guidance.

{{%tip%}}**Tip:** Also, you can apply the ***[Let's Encrypt SSL](https://www.virtuozzo.com/company/blog/free-ssl-certificates-with-lets-encrypt/)*** add-on after the environment creation to automatically issue and integrate a free SSL certificate.{{%/tip%}}

![environment ssl configuration](08-environment-ssl-configuration.png)<a id="configure-nodes"></a>


## Configuring Nodes Resources and Specifics

Once you are done with the topology structure, you can adjust each particular layer via the wizard's central part. Let's review the available options from top to the bottom of the section.

1\. You can toggle a layer **on/off**, as well as provide a custom alias for it.

![environment layer switcher](09-environment-layer-switcher.png)

2\. Configure the [automatic vertical scaling](/automatic-vertical-scaling/) by setting the number of reserved and dynamic [cloudlets](/cloudlet/) (1 cloudlet = **128 MiB** of RAM and **400 MHz** of CPU) for the nodes within the layer.

![layer vertical scaling configuration](10-layer-vertical-scaling-configuration.png)

Think of it as a minimum and maximum CPU & RAM capacities per server. It is worth mentioning that no matter how high the scaling limit is, only actually consumed resources are charged. This helps to overcome load spikes and, at the same time, not to overpay for unused memory or processor.

3\. The *[Horizontal Scaling](/horizontal-scaling/)* part allows defining a number of nodes within the layer and choosing a preferred scaling mode (stateful or stateless).

![horizontal scaling and engine search](11-horizontal-scaling-and-engine-search.png)

You can use the drop-down lists to change stack and engine type/versions (if needed, expand and start typing to **Search**). In case of adjusting an existing environment, these lists will redirect to the [container redeploy](/container-redeploy/) dialog in order to apply changes.

{{%tip%}}**Tip:** Click on the *gear* icon (circled in the image below) for additional [management options](/horizontal-scaling/#managing-nodes-within-layer) during scaling.

![scaled nodes management](12-scaled-nodes-management.png)
{{%/tip%}}

4\. Next, you need to configure additional settings.

![additional layer configuration](13-additional-layer-configuration.png)

The list may vary depending on the particular stack and account permissions:

* **[Auto-Clustering](/auto-clustering/)** - automatic clusterization for some platform certified templates. Additional fields can appear after activation, e.g. scheme selection (*master-slave*, *master-master*, or *galera*) for the database cluster.
* **Disk Limit** - an amount of disk space reserved per node. The dedicated [Shared Storage](/shared-storage-container/) containers are usually provided with enlarged storage capacity.
* **Sequential restart delay** - a delay between the restart operation completion on one node and start on the other. It is used to avoid downtime, ensuring that at least one server is active. You can set it to "*-1*" for the simultaneous restart of all nodes within the layer.
* **[High-Availability](/session-replication/)** (deprecated option, it is recommended redeploying to the latest version of the stack and using the *Auto-Clustering* feature instead) - automated session replication for the *Tomcat* and *TomEE* application servers
* **[Access via SLB](/shared-load-balancer/#deny-access-via-shared-load-balancer)** - blocks access to the nodes of the layer via the platform Shared Load Balancer
* **[Public IPv4/IPv6](/public-ip/)** - attach the specified number of external IP addresses to each node within the layer

5\. At the bottom of the section, you can find buttons to the container configuration tools:

* **[Variables](/container-variables/)** - review and manage a list of the [environment variables](/environment-variables/) for the current layer
* **[Links](/container-links/)** - interconnect layers inside the environment
* **[Volumes](/container-volumes/)** - manage a list of the data volumes to ensure files integrity during container lifecycle
* **[Ports](/container-ports/)** - view information about containers' ports
* **[CMD / Entry Point](/container-run-configuration/)** - configure containers' *Entry Point* and *Run Command*

![layer containers configuration](14-layer-containers-configuration.png)<a id="review-environment"></a>


## Reviewing and Confirming Environment Creation

After all the configurations are done, you can review the amount of allocated resources and the estimated cost of the environment.

1\. The main resource measuring units in the platform are [cloudlets](/cloudlet/). Here, you can see the number of *reserved* ones and the *scaling limit* (dynamic) for the whole environment.

![environment resource usage](15-environment-resource-usage.png)

For better analysis, the values are divided into the color-marked groups:

* *green* - load balancers
* *blue* - application servers
* *orange* - databases and cache nodes
* *gray* - all other stacks

2\. Next, you can view the **Estimated Cost** of your environment. The widget displays price using the same color-marking as above, and you can change the period - *hourly*, *daily*, or *monthly*.

![environment estimated cost](16-environment-estimated-cost.png)

The **FROM** tab shows the price that will be fully charged as it covers reserved resources. The **TO** tab shows the maximum possible price if all nodes in the environment are going to fully consume all resources up to the scaling limit during the whole period.

{{%tip%}}**Tip:** Hover over the pricing widget to view extended details on the estimated cost calculation:

![extended details on environment cost](17-extended-details-on-environment-cost.png){{%/tip%}}

If needed, you can click on the links under the widget for additional information on [how pricing works](/pricing-model/) and [what is charged at the platform](/chargeable-resources/).

3\. Lastly, provide a name for your environment and click the **Create** button to proceed.

![environment name](18-environment-name.png)

That's all! In a few minutes, your new environment will appear on the dashboard.

![created environment in dashboard](19-created-environment-in-dashboard.png)

Now, you are ready for [application deployment](/deployment-guide/) and further use of your cloud environment.

## What's next?

* [Deploy Application](/deployment-guide/)
* [Application Configuration](/configuration-file-manager/)
* [Share Environment](/share-environment/)