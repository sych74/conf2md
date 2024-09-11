---
draft: false
title: "Compound Container"
aliases: "/compound-container-storage/"
seoindex: "index, follow"
seotitle: "Storing Data in Compound Container "
seokeywords: "data storage, shared storage, data storage container, compound container storage, storage role, data sharing, storing data in container, storing data, storage functionality"
seodesc: "Assign an additional storage role to any existing container to make it suitable for simple data sharing. Such a compound container provides data storage functionality without complicating your project topology."
menu: 
    docs:
        title: "Compound Container"
        url: "/compound-container-storage/"
        weight: 30
        parent: "use-cases"
        identifier: "compound-container-storage.md"
---

# Storing Data in Compound Container

The platform provides a possibility to treat any node at account as a data storage server, i.e. assign it an additional storage role beside the main native one. Using such a kind of compound containers suits best for handling simple projects.

![storage in existing node](01-storage-in-existing-node.png)

In this way, you can leverage the shared storage functionality without the redundant complication of your environment topology due to a separate node inclusion. And complementary utilization of a server, which presence is necessary due to its role but which is not very loaded, generally, helps to save money compared to the dedicated Shared Storage Container use.

Also keep in mind, that local files can be retrieved by an application much more faster in contrast to when they are accessed via network. So, for example, if you have two nodes with one of them distributing some static content and another one - just pushing it out upon the request, the best solution will be to set up a storage on the first container to ensure faster distribution and prevention the network from being bottleneck.


## Learn how to:

* Add [mount points](/mount-points/) to access data in remote folder
* [Export data](/storage-exports/) from one node to another
* Store data within [master layer container](/master-container-storage/)
* Use [dedicated container](/dedicated-storage/) for data storing