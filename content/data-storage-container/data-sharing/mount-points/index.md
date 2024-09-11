---
draft: false
title: "Mount Points"
aliases: ["/mount-points/", "/mount-master-container/", "/mount-data-container/", "/mount-external-server/"]
seoindex: "index, follow"
seotitle: "Mount Points"
seokeywords: "shared storage, data storage container, mount points, mount data, share files, data storage usage, data storage client"
seodesc: "Learn how you can mount data from the data storage server to any platform container. Mount files from the master container on layer, any data storage container on the platform or external NFS server."
menu:
    docs:
        title: "Mount Points"
        url: "/mount-points/"
        weight: 10
        parent: "data-sharing"
        identifier: "mount-points.md"
---

# Mount Points

<img src="01-mount-points-icon.png" alt="mount points icon" style="float: left; height: 175px; padding: 15px;">

**Mount points** is a data-sharing functionality between instances inside of the same account. It is initiated <u>*from the client*</u> and creates a connection that allows accessing and operating <u>*data on the server*</u> as if it were local files. The platform provides a comfortable UI for this operation directly in the built-in [Configuration Manager](/configuration-file-manager/). Just in a few clicks, define remote directories that are physically located on other nodes but should be accessible at the current container.

{{%tip%}}**Tip:** The same operation can be initiated <u>*from the server*</u>. It is called **[Exporting Data](/storage-exports/)** - learn more in the linked document.{{%/tip%}}

When creating a mount point, the platform supports two client protocols - **[NFS](/nfs/)** and **[GlusterFS Native](/glusterfs/)**. The first one is available for all containers on the platform and is relatively faster. In contrast, the second one is a unique feature of the [GlusterFS cluster](/shared-storage-container/#shared-storage-auto-cluster), which is recommended for high concurrency, high performance of the write operations, and failover.

1\. So, in order to mount data to a container, click the **Config** button next to the chosen container or layer. In the opened tab, switch to the ***Mount Points*** section within the menu to your left and click the **Mount** button.

![create new mount](02-create-new-mount.png)

2\. The opened form provides the following three operation types:

- **Data Container** - accessing data from the node on the same account
- **Master Container** - sharing data across nodes of the same layer within the current environment
- **External Server** - accessing data from the remote server outside of the PaaS account

![configure mount point](03-configure-mount-point.png)

3\. After selecting the necessary operation type, provide other details as follows:

- **Mount Point** - path to a local folder the mounted content will be displayed at

{{%note%}}**Notes:**
- if the specified directory doesn’t exist, it will be created automatically
- path can’t start with */proc*, */dev*, */sys*, */run* or be equal to the following: */*, */bin*, */lib*, */lib64*, */lib32*, */usr*, */usr/bin*, */usr/sbin*, */usr/lib*, or */usr/lib64* (this list may vary based on your provider’s settings){{%/note%}}


- ***Data Container***
  - **NFS Server** - expandable list of nodes on your account which can be used as a data storage container
  - **Remote Path** - the required directory location at a remote container (you can either type it manually or choose one of the favorite paths on that node from the automatically fetched drop-down list)
  {{%tip%}}**Note:** If *GlusterFS cluster* is selected as a **Server**, you can also choose the preferred **Client Type** protocol for the mount. *[NFS](/nfs/)* is recommended for the performance-oriented topologies, while *[Gluster Native](/glusterfs/)* ensures data safety through backups and replication.{{%/tip%}}

- ***Master Container***
  - **NFS Server** - the master node of the layer is selected automatically
  - **Remote Path** - same folder as specified in **Mount Point** field is used (will be shared among all nodes of a layer)

- ***External Server***
  - **NFS Server** - external IP of the data storage server or its [custom domain](/custom-domains/) name
  - **Remote Path** - exported files location on NFS server

- **Mount to all nodes** - switcher to set the same mounts to be added for all nodes within a layer, including those that could be added in the future (automatically enabled for the **Master Container** type)
- **Read Only** - turn the switcher on to restrict the mounted data editing at client nodes (by default, the *read & write* rights are provided)

Click **Add** to proceed.

{{%tip%}}**Note:** If not a dedicated [Shared Storage Container](/shared-storage-container/) has been chosen as a data container, a brief one-time delay (up to a few minutes) may occur due to the required NFS software installation.{{%/tip%}}

4\. In a moment, your mount point will be created and added to the list. So, you can either **Navigate to directory** (double click on the corresponding record) or **Unmount** it when it becomes unnecessary.

![manage existing mount](04-manage-existing-mount.png)

5\. Upon navigating inside, you'll see the same content as on your remote server.

![switch between nodes](05-switch-between-nodes.png)

Based on the mount configurations, the remote content can be editable from the client or not, as well as available for all layer's nodes or just one. You can switch between nodes using the drop-down list at the left-hand menu (circled above).

{{%note%}}**Take into consideration** that in order to be editable (i.e. if clients are granted RW rights), the folder on the server should have the appropriate permissions for the client's user (the default user names may vary for different servers - e.g. *root* and *jelastic*).

If needed, connect to your storage server via [SSH](/ssh-access/) and execute the following commands to adjust the rights:

```
chown {uid}:{gid} {path}
```

Here:

- ***{uid}*** - user ID, which can be found in the ***/etc/passwd*** file
- ***{gid}*** - group identifier, that is shown within the ***/etc/group*** file
- ***{path}*** - path to the directory or file you’d like to change the permissions for

![edit access permissions](06-edit-access-permissions.png)
{{%/note%}}

The platform mount points provide a great number of [scenarios and possibilities](/data-storage-container/) for advanced data structuration and control.


## What's next?

* [Data Storage Overview](/data-storage-container/)
* [Shared Storage Container](/shared-storage-container/)
* [Exporting Data for Sharing](/storage-exports/)
* [NFS](/nfs/)
* [GlusterFS](/glusterfs/)