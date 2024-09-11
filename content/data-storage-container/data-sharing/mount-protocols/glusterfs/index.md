---
draft: false
title: "GlusterFS Mount Protocol"
aliases: "/glusterfs/"
seoindex: "index, follow"
seotitle: "GlusterFS Mount Protocol"
seokeywords: "glusterfs, mount protocol, glusterfs mount protocol, gluster native, glusterfs specifics, glusterfs storage, glusterfs shared storage, glusterfs mounts, glusterfs exports"
seodesc: "The platform provides GlusterFS mount protocol support when sharing data between instances on the same account."
menu: 
    docs:
        title: "GlusterFS"
        url: "/glusterfs/"
        weight: 20
        parent: "mount-protocols"
        identifier: "glusterfs.md"
---

# GlusterFS

**[GlusterFS](https://docs.gluster.org/en/latest/)** is a network filesystem protocol for distributed cloud storage. The distinctive features of the GlusterFS are reliability, failover, and scalability. It works based on the free *FUSE* software interface and thus does not require any additional servers for metadata (unlike other distributed file systems, e.g. *[Lustre](https://www.lustre.org/)* and *[Ceph](https://ceph.io/)*).

Compared to the **[NFS](/nfs/)** protocol supported at the platform, GlusterFS is renowned for its advanced reliability. The protocol operates with multiple servers and is recommended for cases that require high concurrency, high performance of the write operations, and failover recovery in case of necessity. You can learn more about the [architecture implementation](https://docs.gluster.org/en/latest/Quick-Start-Guide/Architecture/) of this solution from the official documentation.

The platform provides **Gluster Native** client support <u>*starting from the 6.1 release*</u> and on the [Shared Storage Cluster](/shared-storage-container/#shared-storage-auto-cluster) only:

- **all containers** (except *alpine-based* nodes) - Gluster Native client
- **Shared Storage Cluster** - Gluster Native client and server

{{%tip%}}**Tip:** Gluster Native is recommended for topologies where data safety must be ensured through backups and replication. However, for the performance-oriented topologies, the *[NFS](/nfs/)* protocol will suit better.{{%/tip%}}


1\. The platform implementation configures a **Replicated GlusterFS Volume** that overcomes data loss risk by storing exact copies of the data on all bricks (servers). Replicated volume is used for better reliability and data redundancy, as even if one brick fails, the data can still be accessed from replicas. You can learn more about how GlusterFS replication works in the platform by analyzing the corresponding [JPS manifest](https://github.com/jelastic-jps/glusterfs/blob/master/replication-logic.jps) file.

{{%note%}}**Note:** Do not confuse ***GlusterFS volumes*** with Docker ***[container volumes](/container-volumes/)*** available on the platform.{{%/note%}}

2\. The default GlusterFS settings are configured automatically and should not be changed manually. Configs include volume name ("*data*") and IPs of the appropriate servers.

3\. Consider the following limitation when sharing data with GlusterFS:

- shares do not work with sleeping environments and during the [live migration](/environment-regions-migration/#live-migration)
- custom volumes can be created via SSH but are <u>*not recommended*</u> due to limited functionality (e.g. scaling automation)

4\. When facing any issues with GlusterFS, you can check the **[Tasks Panel](/dashboard-guide/#tasks)** in the dashboard. Also, the following logs can provide some additional information:

- ***/var/log/glusterfs*** on the GlusterFS server
- run the ***journalctl*** command on the Shared Storage, custom Docker, or VPS containers

Follow the [mount points](/mount-points/) or [exporting data](/storage-exports/) guides to share files over the GlusterFS protocol.


## What's next?

* [Shared Storage Container](/shared-storage-container/)
* [Mount Points](/mount-points/)
* [Exporting Data for Sharing](/storage-exports/)
* [NFS](/nfs/)