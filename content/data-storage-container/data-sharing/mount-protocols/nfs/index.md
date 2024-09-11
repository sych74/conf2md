---
draft: false
title: "NFS Mount Protocol"
aliases: "/nfs/"
seoindex: "index, follow"
seotitle: "NFS Mount Protocol"
seokeywords: "nfs, mount protocol, nfs mount protocol, network file system, nfs specifics, nfs storage, nfs shared storage, nfs mounts, nfs exports"
seodesc: "The platform provides NFS mount protocol support when sharing data between instances on the same account."
menu: 
    docs:
        title: "NFS"
        url: "/nfs/"
        weight: 10
        parent: "mount-protocols"
        identifier: "nfs.md"
---

# NFS

**NFS** or **[Network File System](https://tools.ietf.org/html/rfc7862)** is a protocol designed to access files on the remote host over the computer network and operate them as if they were local files. It is a popular and widely spread standard that is available to everyone. 

NFS is a client-server application, which means that the NFS server should be installed on the host that provides shared disk space and NFS clients on the servers that gain access to the shared files.

The platform provides NFS support out-of-the-box for all containers (both client and server). The platform fully supports the third version of the protocol on all certified stacks. The fourth version is supported as a client only. NFSv4 server is implemented on the dedicated **[Shared Storage Container](/shared-storage-container/)**:

- **all containers** (except *alpine-based* nodes) - NFSv3 (client and server) and NFSv4 (client only)
- **Shared Storage** - NFSv3 (client and server) and NFSv4 (client and server)

{{%tip%}}**Tip:** NFS is recommended for the performance-oriented topologies, while *[Gluster Native](/glusterfs/)* ensures data safety through backups and replication.{{%/tip%}}

1\. The platform uses the following configurations when setting up NFS clients:

- **for NFS 3:** *nfsvers=3,nolock,udp,soft,timeo=120,retrans=20,\_netdev*
- **for NFS 4:** *nolock,soft,timeo=30,retrans=2,\_netdev*

2\. Take into consideration the following peculiarities of the data sharing with NFS at the platform:

- regular files cannot be exported (only directories)
- mounted directory cannot start with ***/proc***, ***/dev***, ***/sys***, ***/run*** or be equal to the following: ***/***, ***/bin***, ***/lib***, ***/lib64***, ***/lib32***, ***/usr***, ***/usr/bin***, ***/usr/sbin***, ***/usr/lib***, or ***/usr/lib64*** (this list may vary based on your provider’s settings)
- NFS shares do not work with sleeping environments and during the [live migration](/environment-regions-migration/#live-migration) 

3\. When facing any issues with NFS, you can check the **[Tasks Panel](/dashboard-guide/#tasks-panel)** in the dashboard. Also, the following logs can provide some additional information:

- **/var/log/messages** on the NFS server
- run the ***journalctl*** command on the Shared Storage, custom Docker, or VPS containers

Follow the [mount points](/mount-points/) or [exporting data](/storage-exports/) guides to share files over the NFS protocol.


## What's next?

* [Shared Storage Container](/shared-storage-container/)
* [Mount Points](/mount-points/)
* [Exporting Data for Sharing](/storage-exports/)
* [GlusterFS](/glusterfs/)
