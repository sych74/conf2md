---
draft: false
title: "Master Container"
aliases: "/master-container-storage/"
seoindex: "index, follow"
seotitle: "Master Container Storage"
seokeywords: "shared storage, data storage container, master container storage, sharing files on layer, master storage container, data storage"
seodesc: "Find out the details on storing data in the initial (master) container of node group and sharing it among all instances of a layer. Provide the same content to all layer members without the complexity of file synchronization implementation."
menu: 
    docs:
        title: "Master Container"
        url: "/master-container-storage/"
        weight: 20
        parent: "use-cases"
        identifier: "master-container-storage.md"
---

# Storing Data in Master Container

The master container type of data storing becomes the most efficient, when you don't need to export files on different environments but face the necessity to share your data in the confines of a single node layer.

In such a case, you do not require a separate storage container and can use the initial (master) node of the layer as your storage server. E.g. if your application uses some pool of images on compute nodes, you can just share the folder for the whole layer. This ensures availability of the same content at all containers and, simultaneously, eliminates the necessity to synchronize and keep this data copy at each node.

![master container storage](01-master-container-storage.png)

So, this way, you get rid from data duplications, lowering disk space consumption, which also reduces overall environment cost. Moreover, as a separate Storage node is not used here (since everything is kept within layer's master container), no additional environment elements (and thus funds) are required to implement this structure.


## Learn how to:

* Add [mount points](/mount-points/) to access data in remote folder
* [Export data](/storage-exports/) from one node to another
* Keep files safe in [local container filesystem](/local-filesystem-storage/)
* Assign [additional storage role](/compound-container-storage/) to any container