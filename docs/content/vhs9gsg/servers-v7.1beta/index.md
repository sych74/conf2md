---
draft: false
title: "Servers v7.1Beta"
aliases: "/servers-v7.1beta/"
seoindex: "index, follow"
seotitle: "Servers v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Servers v7.1Beta"
        url: "/servers-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "servers-v7.1beta.md"
---
# .Servers v7.1Beta

When you are finished with networks and storage, you can proceed with setting up the following servers: 

-   [Control Panel Server](#id-.Serversv7.1Beta-control_panel)
-   [Backup Server](#id-.Serversv7.1Beta-backup_server)
-   [Compute Resource Servers](#id-.Serversv7.1Beta-compute_resource)

##### **Installation Requirements**

There are some requirements for server installation that you need to follow:

-   We recommend installing AlmaLinux 9 for Control Panel servers and Virtuozzo Hybrid Server 9 for backup servers and compute resource servers.
-   Full root access: please do not create the user *onapp* since it is created as a part of the RPM installation.

For the list of all requirements, see [Software Specifications](.Software_Specifications_v7.1Beta).

## Control Panel Server

------------------------------------------------------------------------

The Control Panel server is absolutely critical to the stability and performance of the cloud. There are a few things to consider when selecting hardware for this server. When your production workloads grow, you need to add more compute resources and SANs, which puts more load on your Control Panel. Selecting the right hardware at the beginning is important and helps to avoid downtime during upgrades later down the line.

The Control Panel server may experience a high load on MySQL as you add more compute resources, so a fast disk array and lots of memory are recommended. For more details, see the [Hardware Specifications](.Hardware_Specifications_v7.1Beta) section. If you have the Control Panel server specifications in mind, you can send them to your OnApp integrations specialist for review.

The minimum recommended `root` partition size during the installation of Control Panel is 60 GB.

## Backup Server

------------------------------------------------------------------------

A backup server stores virtual server backups and templates. It is also responsible for processing any disk transactions running in your cloud, such as provisioning virtual servers, taking backups, or resizing disks. 
The backup server must hold a backup storage volume. It can be a local disk array or can be mounted via NFS or iSCSI from a back-end storage node. Note that the backup volume should not be presented from the same physical hardware that presents the primary storage volume to the compute resources.

Unlike primary storage, performance is not so essential here. So there is less need for RAID10 or a high volume of spindles. You can consider a RAID level that provides more space as opposed to redundancy and performance: RAID5 or RAID6 is usually ideal for the backup volume. When configuring SAN, take into consideration that larger block size is recommended owing to the nature of the data being stored on this array.

Backup storage is used to hold very large files so we recommend that it's at least 1.5 - 2x larger than the primary storage volume(s) available in the cloud. Additional backup servers can be added to your cloud as needed. In the traditional/centralized SAN configuration, you have to bind all your data stores to a backup server. The volume groups of each data store based on SAN must be shared with the backup server.

## Compute Resource Servers

------------------------------------------------------------------------

Compute resources are where virtual servers run in your cloud. A small amount of compute resource CPU, memory, and disk resources is reserved for the OnApp engine: the remainder is available as virtual resources to allocate to virtual servers.

If you use a centralized SAN, then the virtual server disks run on that SAN, and the compute resource's disk is used to boot the compute resource and run the OnApp engine. Performance here is not critical but we recommend introducing some redundancy: RAID1 SATA/SAS would be perfect. If you use integrated SAN, you should factor more disks into your compute resource spec to enable the creation of a distributed SAN using those disks. If you choose not to run a centralized SAN, it is possible to have storage running locally on compute resources, though you lose the ability to failover from compute resource to compute resource: this is not recommended for an optimal cloud setup.

When you build your hardware, it's important to take into consideration the specifications of the primary components that will be virtualized: RAM and CPU. Note that you can oversell CPU cores in OnApp, but not RAM. RAM is a dedicated resource so the physical limitation to how many virtual servers you can fit on a single compute resource is limited by the amount of RAM installed on that compute resource. Another limitation to consider is that the compute resource CPU is a shared resource: the physical cores are shared among virtual servers running on a compute resource. Do not overload the compute resource with too many virtual servers, as it can stretch the available CPU time and degrade the performance of all servers on that compute resource.

It's also important to note that too many virtual servers could potentially saturate the SAN NICs on the compute resource, which can introduce instability and performance loss to virtual servers.

In the [Networking](.Networking_v7.1Beta) section, you can see that OnApp requires at least four NICs on the compute resources. Note that this does not take into consideration any bonding or multipath configurations, which we recommend for any production setup on most if not all of our networks. You should consider bonding on the management network and multipath on the storage network(s) to improve stability and performance.

You must have Intel-VT or AMD-V enabled in the BIOS of all compute resources to enable you to provision Windows-based virtual servers on your OnApp cloud.


