---
draft: false
title: "Migrating to GlusterFS Cluster"
aliases: "/migrating-standalone-storage-to-cluster/"
seoindex: "index, follow"
seotitle: "Migrating to GlusterFS Cluster"
seokeywords: "storage, migrate data, standalone to cluster, standalone storage, glusterfs cluster, glusterfs storage, migrate to storage cluster, migrating to glusterfs, standalone storage to cluster"
seodesc: "Follow this guide to migrate from a standalone storage to the reliable storage cluster based on the GlusterFS network filesystem protocol. Instruction explains how to move data to a temporary server, recreate initial storage as a GlusterFS cluster, and move data back."
menu: 
    docs:
        title: "Migrating to GlusterFS Cluster"
        url: "/migrating-standalone-storage-to-cluster/"
        weight: 50
        parent: "data-storage-container"
        identifier: "migrating-standalone-storage-to-cluster.md"
---

# Migrating Standalone Storage to GlusterFS Cluster 

Currently, automatic conversion of the existing standalone storage into the GlusterFS cluster is not supported. You'll need to recreate the storage from scratch. We recommend creating a temporary *Storage* node in the extra layer, copy data, and remount any existing shares. Then, recreate the initial Storage node as a GlusterFS cluster and restore data and mount shares back. The instruction below will guide you through the process step-by-step.

1\. Locate the required environment in your platform dashboard and click the **Change Environment Topology** button.

![change environment topology button](01-change-environment-topology-button.png)

2\. Within the opened wizard, add a new **Shared Storage** node in the *Extra* layer. Click **Apply** to proceed.

![add temporary storage node](02-add-temporary-storage-node.png)

3\. Connect to your initial (source) *Storage* node via [SSH](/ssh-access/), e.g. using the built-in **Web SSH** client. Run the following command to [generate](/ssh-generate-key/) a keypair that will be used to interconnect two storages:

```
ssh-keygen -f ~/.ssh/storage
```

![generate SSH keypair](03-generate-ssh-keypair.png)

You can view the generated public key with the command below:

```
cat  ~/.ssh/storage.pub
```

![copy public key](04-copy-public-key.png)

Use the **Ctrl+Shift+С** or **Сmd+C** shortcut in the Web SSH panel to copy the key.

4\. Switch to your new *Shared Storage* node and connect to it via [SSH](/ssh-access/) as well. Insert public key from the previous step to the  ***~/.ssh/authorized_keys*** file using any preferred editor, for example:

```
vim ~/.ssh/authorized_keys
```

![add key to authorizedkeys file](05-add-key-to-authorizedkeys-file.png)

5\. Return to the source storage and copy required data to a new node via the ***rsync*** utility:

```
cd /data; rsync -az . {NEW_STORAGE_IP}:/data/ -e "ssh -i $HOME/.ssh/storage"
```

Here, the ***{NEW_STORAGE_IP}*** placeholder should be substituted with the internal IP address of your new storage that can be viewed in the dashboard.

![copy data between storages via rsync](06-copy-data-between-storages-via-rsync.png)

Confirm connection by typing "*yes*" when prompted. The operation may require some time that depends on the amount of copied data.

6\. [Remount](/mount-points/) application data from the initial to temporary storage.

* click the **Config** button next to our application server and **Unmount** the current Shared Storage
![unmount initial storage](07-unmount-initial-storage.png)

* next, create a new **Mount** to your temporary storage server
![mount temporary storage](08-mount-temporary-storage.png)

7\. Standalone Shared Storage can be replaced with a GlusterFS storage cluster in two steps:

* open the **Change Environment Topology** wizard, remove the appropriate storage node altogether, and **Apply** changes
![remove initial storage node](09-remove-initial-storage-node.png)

* access topology wizard once more and add Shared Storage node with the **Auto-Clustering** option enabled
![add GlusterFS cluster](10-add-glusterfs-cluster.png)

8\. Return data from the temporary storage server in the *Extra* layer to a new Shared Storage cluster with GlusterFS support. 

<u>*Repeat the 3-7 steps,*</u> using the temporary storage as source and master node of the GlusterFS cluster as target.

![mount GlusterFS cluster](11-mount-glusterfs-cluster.png)

9\. Remove the temporary storage from the *Extra* layer.

![remove temporary storage node](12-remove-temporary-storage-node.png)

That's all! Now, you have a GlusterFS cluster instead of the standalone storage node.


## What's next?

* [Shared Storage Container](/shared-storage-container/)
* [Mount Points](/mount-points/)
* [SSH Access](/ssh-access/)
* [Auto-Clustering of Instances](/auto-clustering/)