---
draft: false
title: "Volumes"
aliases: ["/container-volumes/", "/docker-volumes/"]
seoindex: "index, follow"
seotitle: "Containers Volumes"
seokeywords: "containers volumes, add data volume, store container data, add volume, add custom volume, container volume, configure container volumes, store data in volume, view volumes container, volume storage for containers"
seodesc: "See how to leverage container volumes to securely store your data during the node lifecycle. With the platform configuration wizard for containers, you are able to view the list of default volumes and add your own ones."
menu: 
    docs:
        title: "Volumes"
        url: "/container-volumes/"
        weight: 40
        parent: "container-configuration"
        identifier: "container-volumes.md"
---

# Volumes

The **Volumes** tab contains the list of mounted at the current container data volumes, which are designed to persist the data independently of the container lifecycle. They are displayed in a view of paths to the appropriate mounted points inside a node:

![volumes layer settings](01--volumes-layer-settings.png)

Storing data within volumes allows different internal operations (e.g. [redeploying](/container-redeploy/) the container to another tag version) to be performed without affecting or losing the data. Such volume content preservation provides a high level of integrity for your data.

Below, we'll consider how to add a custom volume for your container and types of [data mounting](/mount-points/) the platform provides - at a **Local Filesystem**, separate dedicated **Data Container**, layer **Master Container** or **External NFS Server**.


## Operating Custom Volumes

By default, the predefined volumes (i.e. which are determined within the appropriate template settings and are automatically set during container creation) are shown in the **Docker layer settings > Volumes** frame. 

Beside that, you have an ability to mount and manage your custom volumes, placed either locally, at other instance on a platform or any external server. For that, follow the steps below.

1\. Select the **Add** button above the list to see four tabs, named in accordance to the types of volumes you are able to create:

* ***[Local Filesystem](/local-filesystem-storage/)*** - the specified directory will be used as a local storage, intended to persist the data independently of the current container lifecycle (as well as by any other node)
![add local filesystem volume](02--local-filesystem-volumes.png)

* ***[Data Container](/mount-points/)*** - this type of volume allows to mount data from any other layer within your account
![add data container volume](03--data-container-volumes.png)

* ***[Master Container](/mount-points/)*** - data, stored within such volume, is physically placed at the initially created node of the layer (so-called "master node") and is automatically shared with all of the rest instances within this layer
![add master container volume](04--master-container-volumes.png)

* ***[External Server](/mount-points/)*** - this option is intended to mount data from the external NFS server (either your custom third-party storage or [container at another platform](/configure-external-nfs-server/))
![add external server volume](05--external-server-volumes.png)

When all the parameters for the chosen mount type are specified (the details can be observed within the linked guides), click **Add** to finish the configuration.

2\. With the **Edit** option at the top pane (or through double-clicking on the corresponding record), you can change some settings for the already existing volumes:

![edit container volume](06--edit-contaoner-volumes.png)

Here, the **Local Path** is unchangeable value, but you still can switch the mounting method (by moving to a different tab) and/or adjust the access permissions (with the **Read Only** switcher).

Do not forget to **Apply** the changes you've made.

3\. In case your custom volume is not needed anymore, it can be easily unmounted by choosing the corresponding string and clicking on the **Remove** button above.

{{%note%}}**Notes:**

- before deletion, make sure the appropriate volume does not contain any substantial data, as it will be permanently removed
- the predefined (i.e. default) volumes can't be deleted (whilst still being available for editing)
- if you want to remove volume but keep the [mount point](/mount-points/), untick the *Unmount path* checkbox
{{%/note%}}

![remove container volume](07--remove-container-volumes.png)

Confirm your decision within the appeared pop-up frame.

After that, don't forget to **Apply** all your changes with the corresponding button at the general *Docker layer settings* window and, if required, within the topology wizard (in case of modifying the already existing environment).


## What's next?

* [Container Configuration](/container-configuration/)
* [Variables](/container-variables/)
* [Links](/container-links/)
* [Ports](/container-ports/)
* [Run Config](/container-run-configuration/)