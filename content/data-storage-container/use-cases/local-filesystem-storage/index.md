---
draft: false
title: "Local Filesystem"
aliases: "/local-filesystem-storage/"
seoindex: "index, follow"
seotitle: "Local Filesystem Storage"
seokeywords: "shared storage, data storage container, local filesystem storage, persistent storage, local volume, docker storage, docker volume, local storage, save data"
seodesc: "Learn about storing data in a persistent local filesystem volume, which, when working with Docker containers, allows to protect files during different lifecycle operations."
menu: 
    docs:
        title: "Local Filesystem"
        url: "/local-filesystem-storage/"
        weight: 10
        parent: "use-cases"
        identifier: "local-filesystem-storage.md"
---

# Storing Data in Local Filesystem

This kind of storage is used to persist the data, which needs to be kept during container lifecycle, but is not required to be shared across other nodes. If drawing an analogy, basically it's kind of a folder you create inside a server. Commonly, it's not implied that the data such a folder contains should be kept during different maintenance processes. But in confines of [Docker Standard Support](/container-types/) at the platform, creating a local volume in such a container represents an highly efficient way to protect your data (e.g. during the [redeploy](/container-redeploy/) operation).

![local filesystem storage](01-local-filesystem-storage.png)

Among the main advantages of local file system storage type, can be admitted simplicity of data control and its full local availability (as no network issue can affect its accessibility). Such storage can be used, for example, to save log files, which you don't want to be erased, or for your load balancer's configuration files, in order to not to lose the existing nodes' linking structure.


## Learn how to:

* Add [mount points](/mount-points/) to access data in remote folder
* [Export data](/storage-exports/) from one node to another
* Store data within [master layer container](/master-container-storage/)