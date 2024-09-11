---
draft: false
title: "Shared Storage Container"
aliases: ["/shared-storage-container/", "/storage-node/", "/dedicated-storage-container/"]
seoindex: "index, follow"
seotitle: "Shared Storage Container"
seokeywords: "data storage container, storage server, dedicated storage container, storage node, dedicated storage, nfs storage, storage management, storage control, shared storage, store data, export data, paas storage"
seodesc: "Find out details on Shared Storage Container and advantages for data storing it provides. Get an assistance on the Storage container deployment and management."
menu: 
    docs:
        title: "Shared Storage Container"
        url: "/shared-storage-container/"
        weight: 20
        parent: "data-storage-container"
        identifier: "shared-storage-container.md"
---

# Shared Storage Container

**Shared Storage Сontainer** is a special type of node, designed for data storing. Compared to other managed containers, it provides a number of the appropriate benefits:

* ***NFS and Gluster Native (FUSE) client types*** for data mounting
  * **[NFS](/nfs/)** - straightforward file system protocol, designed for accelerated processing and high performance
  * **[Gluster Native (FUSE)](/glusterfs/)** - reliable file system protocol with automatic replication of the mounted data, designed for data backup and failover (consumes more CPU/disk than NFS)
* ***NFSv4 Support*** instead of *NFSv3* on other managed stacks, ensures improved performance (especially for a large number of files), stronger security, support of the [FUSE](https://github.com/libfuse/libfuse) directories export, and more.
{{%tip%}}**Note:** Any platform-managed container can receive mounts over the fourth version of the protocol, but only Shared Storage Container can export data over NFSv4.{{%/tip%}}
* ***[Auto-Clustering](/auto-clustering/)*** option automatically configures a reliable storage cluster, ensuring data safety. In case of failure of one or several nodes, the *AutoFS* client automatically switches to the working instances on the next read/write operation attempt.
* ***Enlarged Disk Space*** compared to other common-purposed nodes is provided for Shared Storage Container, allowing to work with bigger data volumes. The particular value depends on your service provider's settings and can vary based on the account type.
* ***Optimized Performance*** due to all the necessary software being preinstalled (e.g. *NFS & RPC* for NFSv4, *[GlusterFS](https://www.gluster.org/)* for auto-clustering) and the default features of the platform (elastic vertical and horizontal scaling, efficient pay-as-you-use pricing model, comfortable UI with file exports and mount points support, etc.)

![shared storage container illustration](01-shared-storage-container-illustration.png)

And below we'll consider how to set up such Shared Storage server inside the platform, some tips on its management, and use case specifics:

* [Storage Container Creation](#storage-container-creation)
* [Shared Storage Auto-Cluster](#shared-storage-auto-cluster)
* [Storage Container Management](#storage-container-management)


## Storage Container Creation

To create a new Shared Storage Container, enable the corresponding ***Storage*** section at the topology wizard. This option is available for all engine types, including *Docker* containers.

![shared storage topology wizard](02-shared-storage-topology-wizard.png)

In the middle part of the wizard, you can provide additional configurations for your Shared Storage. The exact amount of provided storage space can be adjusted via the *Disk Limit* field. The platform can automatically configure a [reliable storage cluster](#shared-storage-auto-cluster) (instead of separate nodes) if you enable the ***Auto-Clustering*** switcher. Also, in case of necessity, [public IP](/public-ip/) addresses can be attached to the nodes (both IPv4 and IPv6).

{{%tip%}}**Tip:** Since this container type was specially developed to be used as a data storage server, you need to consider some specifics about its configuration:

* although RAM & CPU are not the primary resources of the storage, they are still consumed by the node due to operating over networks (the particular amount depends on load)
* if the maximum value of disk space per storage node is not enough, please contact your hosting provider's support team and request the corresponding account limit enlargement
* node pricing mainly depends on the amount of disk space in use (not the limit) and external network traffic (check these resources cost at **[Quotas & Pricing](/resource-consumption/#how-much-do-resources-cost) > Pricing > Disk Space** or **Traffic**){{%/tip%}}

Click **Create** when ready.


## Shared Storage Auto-Cluster

Upon enabling **[Auto-Clustering](/auto-clustering/)** switcher for the Shared Storage Container in topology wizard, the platform automatically configures a *replicated volume* (replicates files across bricks in the volume). Such a solution is implemented based on the pre-installed *[GlusterFS](https://www.gluster.org/)* RPM packages and is intended for environments where high-reliability is critical.

![storage auto-clustering](03-storage-auto-clustering.png)

{{%tip%}}**Tip:** Consider the following specifics:

* Currently, automatic conversion of the existing standalone storage into the GlusterFS cluster is not supported. Follow the manual [migration guide](/migrating-standalone-storage-to-cluster/).
* Shared Storage auto-clustering requires the latest [Virtuozzo 7](https://www.virtuozzo.com/products/vz7.html) virtualization used on the [environment region](/environment-regions/) (depends on your hosting provider)
* storage auto-cluster requires 3 or more nodes and cannot be disabled after creation
* scaling is performed with two nodes step to maintain working quorum{{%/tip%}}

During creation, the GlusterFS volume is mounted into the **/data** folder and is accessible over NFSv4 protocol. Consequently, when [mounting](/mount-points/) from/to your storage cluster, it is managed as a single component (i.e. not a collection of separate storage containers). In case of failure of one or several nodes, the *AutoFS* client (that is used in application containers by default) automatically switches to the working instances on the next read/write operation attempt.

![storage NFS mounts](04-storage-nfs-mounts.png)

{{%tip%}}**Tip:** If facing the [split-brains error](https://docs.gluster.org/en/latest/Troubleshooting/resolving-splitbrain/) (i.e. storage cannot determine which copy in the replica is the correct one), follow the linked troubleshooting guide to resolve the issue.{{%/tip%}}

### Use Cases Peculiarities

The storage cluster based on the Gluster software is [suitable for the most solutions](https://gluster.readthedocs.io/en/latest/Install-Guide/Overview/#is-gluster-going-to-work-for-me-and-what-i-need-it-to-do). However, some cases benefit from the *GlusterFS & NFS* usage more than others.

<u>*Recommended*</u> use cases:

* when the GlusterFS storage is mostly used to read data (not write), e.g. WordPress or Magento websites, shared resource for media content data
* if the application that performs write operations to GlusterFS storage can handle exceptions and perform retry attempts in case of an error

<u>*Not recommended*</u> use cases:

* Gluster does not support so-called "structured data", so do not use Shared Storage for SQL databases. However, using GlusterFS to backup and restore a database would be fine
* NFS is not suitable for applications with heavy IO operations and, in case of a node failure during the write operation, can even lead to data corruption

Some general examples of the storage usage are described in the [Dedicated Storage](/dedicated-storage/) documentation.


## Storage Container Management

Right after creation, you can immediately proceed to the container configuration. Below, we'll show several basic actions that may be useful for you to get started:

1\. For the most common operations with your storage, the built-in [configuration file manager](/configuration-file-manager/) can be used. For more complex management, you may prefer to work with some third-party tool (use the connection details from the **SFTP / SSH Gate** tab circled in the image below).

![storage file manager](05-storage-file-manager.png)

{{%tip%}}**Tip:** For files sharing with other instances within the platform or external servers, the appropriate ***[Mount Points](/mount-points/)*** and ***[Exports](/storage-exports/)*** tabs can be used.{{%/tip%}}

2\. [SSH access](/ssh-access/) (either via the *web* or *local* SSH client) can be established to get full control over your storage server.

![Web SSH connection to storage](06-web-ssh-connection-to-storage.png)

3\. If you want to use your Shared Storage Container as an external server (i.e. not only within the current PaaS installation) - enable the [public IP](/public-ip/) option to make it accessible from outside. Follow instructions in the dedicated [NFS server configurations](/configure-external-nfs-server/) guide.

![storage public IP](07-storage-public-ip.png)

The IP address(es) attached to *Shared Storage* can be viewed through expanding the appropriate node in the dashboard.

4\. When stopping or deleting an environment, the platform automatically checks for the mounts configured on the comprised nodes and provides **Details** on instances affected by the action in the confirmation frame.

![NFS mount dependencies](08-nfs-mount-dependencies.png)

{{%tip%}}**Note:** The *live migration* option is not available for [migration of environments](/environment-regions-migration/) with Shared Storage containers. So, to check the nodes affected by the temporary unavailability of the storage, use the appropriate *availability of the components* link circled in the image below.

![shared storage migration](09-shared-storage-migration.png){{%/tip%}}

That's all! For now, as you know the main points on your Shared Storage Container handling, feel free to proceed and fill it with the required content.

{{%tip%}}If you experience any problem with Shared Storage Container deployment, configuration or usage, feel free to appeal to our technical expert's assistance at [Stackoverflow](https://stackoverflow.com/questions/tagged/jelastic).{{%/tip%}}


## What's next?

* [Data Storage Overview](/data-storage-container/)
* [Mount Points](/mount-points/)
* [Exporting Data for Sharing](/storage-exports/)
* [External NFS Server Configuration](/configure-external-nfs-server/)