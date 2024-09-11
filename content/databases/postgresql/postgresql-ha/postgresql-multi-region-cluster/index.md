---
draft: false
title: "PostgreSQL Multi-Region Cluster"
aliases: "/postgresql-multi-region-cluster/"
seoindex: "index, follow"
seotitle: "PostgreSQL Multi-Region Cluster"
seokeywords: "postgresql cluster, multi region cluster, postgresql high availability, multi region postgresql, postgresql multi region cluster, primary secondary topology, postgresql cluster entry point"
seodesc: "Learn about the higly available PostgreSQL Multi-Region Cluster package, which is available for automatic installation from the platform Marketplace."
menu:
    docs:
        title: "Multi-Region Cluster"
        url: "/postgresql-multi-region-cluster/"
        weight: 20
        parent: "postgresql-ha"
        identifier: "postgresql-multi-region-cluster.md"
---

# PostgreSQL Multi-Region Cluster

**PostgreSQL Multi-Region Cluster** is a pre-packaged solution that automatically creates an advanced, highly available database cluster on top of platform-managed stack templates.


## Database Cluster Topology

The [PostgreSQL Multi-Region Cluster](https://github.com/jelastic-jps/postgres-multiregion) package uses the only officially supported PostgreSQL Cluster topology - **Primary-Secondary**. However, one more secondary node is added for disaster recovery. As a result, the final topology is *Primary-Secondary-Secondary*.

<img src="01-postgresql-multi-region-cluster.svg" alt="PostgreSQL multi-region cluster" width="300" >

Additionally, the package includes a highly available [Pgpool-II Load Balancer](https://www.pgpool.net/mediawiki/index.php/Main_Page) layer to distribute requests and manage PostgreSQL replication topology.

The sum of these implementations ensures out-of-box high availability and failover for the database cluster. It is ensured on the data center level – the database is accessible even if one of the regions becomes unavailable.


## Cluster Installation

1\. Find the ***PostgreSQL Multi-Region Cluster*** application (the **Clusters** section or use the **Search** field) in the platform [Marketplace](/marketplace/).

![PostgreSQL multi-region marketplace](02-postgresql-multi-region-marketplace.png)

2\. In the opened installation window, specify the following data:

- **Version** - select the preferred PostgreSQL version
- **Environment** - provide a name for [grouping](/environment-groups/) your database cluster environments
- **Create separate environment group** – tick to [isolate](/environment-isolation/#private-network-isolation) the environment group
- **PostgreSQL Regions** - choose platform regions where the cluster environments will be deployed. Note that regions order matters, as the first one will be the Primary server and the others will be Secondary
- **Pgpool-II enabled** – enable to add load-balancing, monitoring, and management node (*Pgpool-II*) in front of database nodes in each region
- **Pgpool regions** - choose platform regions where the load balancing nodes will be deployed

![install PostgreSQL multi-region cluster](03-install-postgresql-multi-region-cluster.png)

Click **Install** when ready.

3\. The installation process can take several minutes. After the completion, you’ll see the success window and receive emails with all the appropriate data, like entry point details and access credentials.

To easily view all the related environments, you can switch to the group specified in the previous step (*pgcluster* in our case).

![PostgreSQL cluster group](04-postgresql-cluster-group.png)

4\. The default entry point for your multi-region cluster is a leader *Pgpool-II* node (the one deployed into the first region). If it fails, you can use any other *Pgpool-II* node using either [hostname](/container-dns-hostnames/#hostnames-for-specific-containers) or IP address.

![PostgreSQL multi-region cluster environments](05-postgresql-multi-region-cluster-environments.png)

In case your client software supports multiple entry points, you can set up all of them in a connection string to ensure automatic failover.


## What's next?

* [Create DB Server](/database-hosting/)
* [Remote Access to PostgreSQL](/remote-access-postgres/)
* [Java Connection to PostgreSQL](https://www.virtuozzo.com/company/blog/java-connection-to-postgresql/)
* [PHP Connection to PostgreSQL](/connection-to-postgresql-for-php/)
* [PostgreSQL Replication](/postgresql-database-replication/)
* [Dump Import/Export to PostgreSQL](/dump-postgres/)