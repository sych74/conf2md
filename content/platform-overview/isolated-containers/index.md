---
draft: false
title: "Isolated Containers"
aliases: ["/isolated-containers/", "/isolated-containers-migration/"]
seoindex: "index, follow"
seotitle: "Isolated Containers"
seokeywords: "container, live migration, isolated containers, migration between nodes, automatical scaling, virtual machine, hardnode, physical server, resources scaling, virtualization"
seodesc: "See the basis of the platform architecture: all the instances are independent isolated containers located on the different physical servers."
menu: 
    docs:
        title: "Isolated Containers"
        url: "/isolated-containers/"
        weight: 60
        parent: "platform-overview"
        identifier: "isolated-containers.md"
---

# Isolated Containers

All of the instances in the environment (like databases, application servers, etc.) are isolated containers located on different hosts.

Three main reasons why the platform provides individual role-based servers are:

* [live migration](#isolated-containers-live-migration)
* [high availability](#high-availability-for-applications)
* [security](#security-of-isolated-containers)


## Isolated Containers Live Migration

In some cases, as your application starts requesting more and ***more resources***, the physical server running your node might not be able to provide the required resources. In this case, the platform can perform a ***live migration*** of the node to another host within 30 seconds.

![containers live migration to another server](01-containers-live-migration-to-another-server.png)

During that migration, the application keeps working being [scaled vertically](/automatic-vertical-scaling/). As an application scales within a server, other applications can be migrated to another server to make room. Live migration allows platform to deliver all the needed resources for applications without restarting containers and causing application downtime. In addition, it can be used during maintenance or other planned downtime to perform automated evacuation of containers from a physical server.

Also, you can add ***more instances*** to your environment using [horizontal scaling](/horizontal-scaling/), not having to worry if there is ***enough space*** on the host. The platform chooses the host with an appropriate amount of free space and relocates your server, in order to offer high-quality performance to each of your nodes.


## High Availability for Applications

The platform provides the **highest availability** by distributing containers of one environment evenly on different physical servers (Hardware nodes). This is done with the help of anti-affinity groups configured to specify that certain containers should never run on the same physical server.

![containers high-availability](02-containers-high-availability.png)

As a result, the platform eliminates any risk of application downtime if one of the physical servers has any issues with performance.


## Security of Isolated Containers

The platform uses the ***virtualization*** method to run multiple containers simultaneously on a single host. These containers are ***fully isolated*** with no risk of interfering with one another. If the security of any container at the hardware node is compromised, the rest of the containers are left unaffected.

{{%note%}}**Note:** Since each instance within the platform represents an isolated container, it can't be reached from another node with a simple *localhost:port_number* or *127.0.0.1:port_number* reference - the corresponding container hostname or private/[public](/public-ip/) IP address should be used instead (for example, this could be required to interconnect your application with a database instance).{{%/note%}}


## What's next?

* [What is PaaS & CaaS](/what-is-paas-and-caas/)
* [Automatic Vertical Scaling](/automatic-vertical-scaling/)
* [Setting Up Environment](/setting-up-environment/)
* [PaaS Cluster Overview](/cluster-overview/)
* [Cluster Access Levels](/cluster-access-levels/)