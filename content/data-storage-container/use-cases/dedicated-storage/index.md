---
draft: false
title: "Dedicated Container"
aliases: ["/dedicated-storage/", "/data-container-storage/"]
seoindex: "index, follow"
seotitle: "Dedicated Storage"
seokeywords: "data storage, data storage container, sharing data, external storage, share files, dedicated data storage, dedicated storage, export files, storage container, dedicated storage benefits"
seodesc: "Use the Dedicated Storage Container to share files across multiple containers, environments or even between platforms. Beside that, you can configure your storage to export data externally anywhere over Internet. "
menu: 
    docs:
        title: "Dedicated Container"
        url: "/dedicated-storage/"
        weight: 40
        parent: "use-cases"
        identifier: "dedicated-storage.md"
---

# Dedicated Storage Container

For more complex and loaded applications, it is worth to centralize your shared data within a single container to get more simple and flexible exports' management (including access permission control - e.g. read-only for one node type and read-write for another).  

In confines of the platform, a [Shared Storage Container](/shared-storage-container/) is recommended to be used for sharing files across multiple layers or even environments of a single account. It is specially optimized for data storing (i.e. is focused on performance and provides the enlarged disk space amount).

![dedicated container storage](01-dedicated-container-storage.png)

Apart of that, upon using a separate Shared Storage Container, you get the following benefits:

* Since storage here represents an independent container, its occasional high loading can be properly handled without influence on general application performance (as it might happen during load peaks in case a single node fulfils several "roles").
* Upon the necessity, you can painlessly remove everything except the required data (i.e. leaving just a storage being included to environment) and start over with your project from the scratch. The majority of common environment settings (e.g. internal domain and sharing permissions) will be left unchanged, which highly simplifies project re-integration.
* Storing data apart makes it easier to handle several [project clones](/clone-environment/) (i.e. environments), dedicated for different application lifecycle stages (e.g. separate ones for development, testing and production).
* Mount folder with your DB's [scheduled backups](/database-backups/) to your storage container for making backups automatically kept on the remote server and, in such a way, improve the overall data safety during software upgrades.

In addition to actually data storing, such a structure can be also efficiently utilized in case you need to share some common configuration files, that are to be used by nodes on different layers and/or environments.

Your Shared Storage Container can be also used as an external storage, i.e. you can export data from the platform to be available over the Internet.

![export data from platform](02-export-data-from-platform.png)

In such a way, you can share some content for the required third-party service or another developer (providing him with personal access permissions) or, generally, get a quick access to your data from any point with the platform-hosted NFS server.

By using this option, you can even build your own intercloud sharing solution and/or operate with the same data from different PaaS installations - find out the required [NFS server configurations](/configure-external-nfs-server/) for such an implementation within the linked guide.


## Learn how to:

* Operate [Shared Storage Container](/shared-storage-container/)
* Add [mount points](/mount-points/) to access data in remote folder
* [Export data](/storage-exports/) from one node to another
* Configure container as an [external NFS storage](/configure-external-nfs-server/)
* Connect [external NFS storage](/external-nfs-storage/)