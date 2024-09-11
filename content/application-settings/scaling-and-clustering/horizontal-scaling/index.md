---
draft: false
title: "Horizontal Scaling"
aliases: ["/horizontal-scaling/", "/app-server-scaling/", "/cache-server-scaling/", "/database-server-scaling/", "/docker-container-scaling/", "/load-balancer-scaling/", "/multi-nodes/", "/storage-container-scaling/", "/vps-scaling/", "/app-server-horizontal-scaling/", "/cache-server-horizontal-scaling/", "/database-server-horizontal-scaling/", "/docker-container-horizontal-scaling/", "/load-balancer-horizontal-scaling/", "/storage-container-horizontal-scaling/", "/vps-horizontal-scaling/"]
seoindex: "index, follow"
seotitle: "Horizontal Scaling"
seokeywords: "horizontal scaling, multi nodes, sever scaling, server horizontal scaling, servers scaling in cloud, cloud increase instance count, cloud horizontal scaling, horizontal scaling in cloud, horizontal scaling in paas, server nodes count, cloud multi nodes, cluster scaling in cloud, app scaling high availability, containers scaling, containers horizontal scaling, nodes scaling, nodes horizontal scaling"
seodesc: "Learn how to scale your platform servers horizontally and discover this feature implementation specifics on the hardware level. Get some additional tips and tweaks on the horizontal scaling usage and how to automate it."
menu: 
    docs:
        title: "Horizontal Scaling"
        url: "/horizontal-scaling/"
        weight: 20
        parent: "scaling-and-clustering"
        identifier: "horizontal-scaling.md"
---

# Horizontal Scaling inside the Cloud: Multi Nodes

With the platform, hosting of your applications becomes truly flexible. In addition to [automatic vertical scaling](/automatic-vertical-scaling/), the platform also lets you increase/decrease the number of servers in your environment manually or [automatically](/automatic-horizontal-scaling/).

The process of manual scaling is fairly simple - open the environment topology wizard and use the appropriate "**+**" and "**-**" buttons or type the required number in the central panel. Also, you can use the slider, which automatically appears upon making any adjustment.

![topology wizard horizontal scaling](01-topology-wizard-horizontal-scaling.png)

{{%tip%}}**Tip:** 
* you can automate horizontal scaling based on incoming load with the help of [tunable triggers](/automatic-horizontal-scaling/)
* you can use the initial (master) node of the layer as your [storage server](/master-container-storage/) for sharing data within the whole layer
* in case of scaling in (i.e decreasing the nodes number), the last container added to the layer is the first one to be removed (unless it is [selected explicitly](#managing-nodes-within-layer))
{{%/tip%}}

Next, you can select the required [scaling mode](#scaling-modes) from the appropriate drop-down list. Also, for additional details refer to the [horizontal scaling specifics](#horizontal-scaling-specifics) section below.


## Scaling Modes

Starting with the 5.5 platform version, the preferred scaling mode can be selected for new environments during creation, as well as adjusted for the existing ones through the topology wizard:

* ***Stateless*** - simultaneously creates all new nodes from the base image template
* ***Stateful*** - sequentially copies file system of the master container into the new nodes

![scaling modes](02-scaling-modes.png)

The first option is comparatively faster, while the second one automatically copies all custom configurations. Herewith, during the initial layer creation, all of the nodes are created simultaneously to speed up the process (even for the ***stateful*** mode, as no customization has been applied yet).

While using the ***stateless*** mode, be aware of the following features absence on the new nodes within the layer:

* **deployments** - the existing project contexts won't be transferred
* **custom SSL** - SSL certificates and configs won't be copied
* **mount points** - custom [mounts](/mount-points/) will be moved only if the appropriate [volume](/container-volumes/) is configured
* **add-ons** - any [add-ons](/marketplace/) installed on the layer won't be available

{{%note%}}**Tip:** The transfer of custom files for the ***stateless*** mode can be done manually or configured via the [Cloud Scripting](https://docs.cloudscripting.com/) automation (e.g. using the *onBefore-* and *onAfterScaleOut* events).{{%/note%}}

Based on these peculiarities, the platform recommends (and applies by default) the ***stateful*** scaling mode for the *load balancer*, *application server*, and *VPS* stacks. In case of necessity, you can manually redefine the scaling mode for your nodes at any time via topology wizard.


## Horizontal Scaling Specifics

The maximum number of the same-type servers within a single environment layer depends on a particular hosting provider settings (usually this limit stands for 16 nodes). You can check the exact value within the **Quotas & Pricing > [Account Limits](/quotas-system/)** information frame.

All newly added servers are created at different hardware nodes, providing advanced reliability and high-availability.

![horizontal scaling high-availability](03-horizontal-scaling-high-availability.png)

Each environment node group (layer) is provided with the dedicated name, which, if needed, can be manually adjusted. In case there are several instances inside, layer name will be complemented with the ***xN*** label (where ***N*** is the actual nodes number).

Having several same-type nodes within a layer enables their synchronous management. Thus, all containers can be simultaneously [configured](/container-configuration/), inspected for logs and statistics, [restarted or redeployed](/container-redeploy/) through the corresponding icons.

![scaled nodes management](04-scaled-nodes-management.png)

In order to operate with a particular container separately, expand the layer's string to see the full list of its nodes. Each of these containers is an isolated instance, which has a unique ***Node ID*** and can be accessed/configured apart from others. Herewith, the layer master node can be easily located due to the dedicated icon.

![nodes in scaled layer](05-nodes-in-scaled-layer.png)

To facilitate interaction with numerous servers of the same type, the platform also allows marking a particular node with the appropriate label, e.g. to define master and slave instances in a DB cluster.

Just double-click at the default ***Node ID: xxx*** value (or hover over it to reveal a special pencil icon) and specify the desired alternative name.

![aliases for scaled nodes](06-aliases-for-scaled-nodes.png)

More information on this labeling feature can be found in the [Environment Aliases](/environment-aliases/) document.

While scaling different types of stacks, consider the following specifics:

* upon scaling the application server instance, the load balancer node will be automatically added to the environment topology
* if enabling the [high-availability](/session-replication/) option for application server, the obligatory required NGINX load balancer cannot be scaled horizontally (if several nodes of NGINX were available before, they will be automatically downscaled to a single instance)
* upon scaling VPS nodes, each one is provided with a separate [public IP](/public-ip/) address attached
* [Maven](/java-vcs-deployment/) is the only node, which cannot be scaled horizontally (as there is no point in such operation)

Now, you know how easy it is to horizontally scale instances in the platform and aware of the operation specifics. Also, feel free to configure an [automatic nodes scaling](/automatic-horizontal-scaling/) to smoothly overcome high load spikes without overpaying for unused resources.


## Managing Nodes within Layer

The platform provides a simple nodes management, where you just need to specify the required number of containers in a layer. Herewith, the removal process is done in the order opposite to the addition - i.e. the most recent containers are removed first. In case you need to delete some specific node, you can select the required one via:

* the ***Horizontal Scaling*** section in topology wizard - accessible using the **Change Environment Topology** button next to the required environment
![nodes management wizard](07-nodes-management-wizard.png)

* the dedicated ***Scaling Nodes*** form in the dashboard - accessible using the **Additionally > Scaling Nodes** option next to the layer or **Additionally > Delete** next to the particular node
![delete node dashboard](08-delete-node-dashboard.png)

In the **Scaling Nodes** window, you can perform the following actions:

1\. Add new nodes to the layer, using the **+** or **Add New Node** buttons.

![scaling nodes add](09-scaling-nodes-add.png)


{{%tip%}}**Tip:** 
* In case a **[high availability](/session-replication/)** option is enabled for the layer (available for the *Tomcat* and *TomEE* application servers only), the nodes are added and removed in pairs.
* The new nodes' icons represent the scaling mode of the layer - empty container for *stateless* and filled one for *stateful*.
{{%/tip%}}

2\. Remove instances with the **-** and **Delete** (upon hovering over particular node) buttons.

![scaling nodes delete](10-scaling-nodes-delete.png)

{{%tip%}}**Tip:** 
* The first node in the list is a so-called "*master*" of the layer (highlighted with a special icon) and can only be removed alongside the whole layer.
* You can **Undo Deletion** of the existing node during configuration. However, after applying changes, the instance will be deleted permanently.
![undo node deletion](11-undo-node-deletion.png)
{{%/tip%}}

3\. At the bottom of the frame, a redirect to the *[Automatic Horizontal Scaling](/automatic-horizontal-scaling/)* section can be found.

![auto scaling redirect](12-auto-scaling-redirect.png)

If any adjustments are made in the form, you'll need to confirm the redirect via pop-up (as any unsaved changes are discarded).

4\. When applying changes, the platform automatically notify you about all the potentially harmful actions that will be performed with your environment (if any). The list includes:

* nodes restart notice
* layers and separate nodes removal reminder
* impact on existing NFS mounts

![confirm changes](13-confirm-changes.png)

Before proceeding, ensure that the listed points won't affect your application, and any crucial data (from the removed nodes) is safely backed up.


## What's next?

* [Automatic Horizontal Scaling](/automatic-horizontal-scaling/)
* [Automatic Vertical Scaling](/automatic-vertical-scaling/)
* [Container Configuration Tools](/container-configuration/)
* [Environment Aliases](/environment-aliases/)
* [Public IP](/public-ip/)