---
draft: false
title: "Storage"
aliases: "/storage/"
seoindex: "index, follow"
seotitle: "Storage"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Storage"
        url: "/storage/"
        weight: 10
        parent: "get-started"
        identifier: "storage.md"
---
# Storage

The installation requirements to storage vary depending on a storage strategy that you plan to deploy. In this document, you can find information on how to implement the following storage solutions: 

-   [Centralized Storage (SAN)](#Storage-centralized_storage)
-   [StorPool Storage](#Storage-storpool)

## Centralized Storage (SAN)

------------------------------------------------------------------------

The primary storage is critical to your cloud, and your SAN has a huge impact on the performance of the whole platform. OnApp offers you a lot of flexibility in your primary storage technology. OnApp supports each solution capable of presenting a block device to compute resources. It could be, for example, FiberChannel, SCSI or SAS HBA, iSCSI or ATAoE, or an InfiniBand HCA controller, since all of them present the block device directly. OnApp does not support services, such as NFS for primary storage, because they preset a filesystem but not the block device.

Beyond a block device type, there are three main things to consider in your SAN design: the host, fabric, and storage components. You need to think about each very carefully and pay particular attention to performance, stability, and throughput when designing your SAN.

##### **Fabric Components - Network Fabric Between Compute Resources and SANs**

Take into consideration redundancy and whether you need to design a fault-tolerant switching mesh to coincide with your multipath configurations at the host and SAN ends. You must think about future growth. As you add more compute resources and SANs to the cloud, you must be able to grow the physical connectivity without downtime on the Storage Network.

##### **Host Components - Compute Resource Connectivity to Storage Network**

Ensure that your Ethernet or HBA drivers are stable in this release. We recommend that you test this thoroughly before handing over to OnApp to deploy your cloud on your infrastructure. Take into consideration the throughput and whether the connectivity on compute resources are suitable for the virtual servers they will be running.  A bottleneck here will cause major performance issues. Consider adding multiple HBAs or NICs if you plan to run a redundant switching mesh (see the Fabric section) as bonding or multipath will be required, unless the redundancy is built into the physical switch chassis (for example, failover backplanes).

##### **Storage Components - SAN Chassis, Controllers, and Disk Trays**

You must take into consideration the physical capacity that is required to build a storage of a necessary size. It gives you a good idea of the size of disks you will be adding to the array and the RAID level you will choose. As a general rule, more spindles in the array will give you better performance: you should avoid using a small number of large disks, or you will start to see I/O bottlenecks as you make increasing use of the storage in the future. Think about the physical storage hardware and whether you will use SATA, SAS, or SSD. This will have a great impact on the I/O capabilities of the array.

It's also a good idea to consider RAID levels carefully and look into the advantages and disadvantages of each. We recommend RAID10. Although you will lose 50% of your capacity, you will see good performance for both read and write, which is important for primary storage. RAID10 will also give you much better redundancy on the array.

Controller caching is another issue to consider. You should always aim to have both read and write caching. If you are looking at write caching, you should also look at battery backups for the write cache. Some controllers also support SSD caching which can be a great advantage. As with the host components, you should also take your HBA and Ethernet connectivity into consideration to ensure you have both the redundancy and throughput required for your cloud infrastructure.

## StorPool Integration

------------------------------------------------------------------------

OnApp provides and maintains integration with StorPool, whereas each VS disk becomes a separate volume in the StorPool storage system. 

OnApp with StorPool can be deployed in two modes - hyperconverged and standalone. 

-   In the hyperconverged mode, StorPool storage servers are running on the OnApp hypervisors (compute resources) to pool the disks together to make a datastore that will be managed in its entirety by StorPool.
-   In the standalone mode, StorPool storage servers are deployed on dedicated servers. In this case, StorPool block device drivers still need to be installed on the OnApp hypervisors and backup nodes, so they are able to access the StorPool storage and consume volumes.

With the StorPool integration, it is possible to get control over each individual volume, in terms of monitoring and data placement. To be able to use StorPool in the cloud, you need to install the StorPool storage system first. For details, refer to [StorPool](https://docs.onapp.com/in/storpool).


