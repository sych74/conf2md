---
draft: false
title: "Exporting Data for Sharing"
aliases: "/storage-exports/"
seoindex: "index, follow"
seotitle: "Exporting Data for Sharing"
seokeywords: "export data, data storage container, data storage server, storage exports, check exports, shared files, exporting data, sharing data, shared storage"
seodesc: "Learn how to share directories between instances inside your PaaS account. Use the dedicated Exports section in the dashboard to export folders and manage existing export records."
menu:
    docs:
        title: "Exporting Data for Sharing"
        url: "/storage-exports/"
        weight: 20
        parent: "data-sharing"
        identifier: "storage-exports.md"
---

# Exporting Data for Sharing

{{%imageLeft%}}![data export icon](01-data-export-icon.png){{%/imageLeft%}}

The platform provides extended support for [data sharing](/data-storage-container/) between instances inside of the same account. The dedicated UI panels are available in the dashboard to simplify the required export from a server (described in this guide) and [mount on client](/mount-points/) operations. You only need to perform either of these actions, and the platform will automatically apply the correlated configuration on the appropriate second instance.

So, let's overview how you can [share directories](#directory-export) on your containers and how to manage all of the [container's exports](#managing-exports).


## Directory Export

You can share any directory inside your container with any other node at your account.

{{%tip%}}**Note:** In case you need to [export data externally](/configure-external-nfs-server/) (i.e. to the server outside of your PaaS account), follow the linked guide to configure exports manually.{{%/tip%}}

1\. Open the [configuration manager](/configuration-file-manager/) for your storage (i.e. where files are physically located), switch to the ***Exports*** section, and click the **Export** button at the top pane.

![create new export](02-create-new-export.png)

2\. The appropriate ***Export Directory*** tab will be opened.

![configure new export](03-configure-new-export.png)

Here, you'll need to specify the following information:

* **From NFS** - choose the required node inside the current environment layer via the drop-down list
* **Path** - type an absolute path to the exported folder (or choose it from your favorites)
* **To Container(s)** - select target layer from the automatically fetched list of environments on your account
* **Path** - provide a path to the location through which the shared data should be available on the target node(s)
* **Mount to all nodes** - use this switcher to set the same mount for the whole layer (disable to mount to a single node)
* **Read Only** - turn the switcher on to restrict editing of the exported data at client node(s) (by default, the *read & write* permissions are provided)  

Click **Add** to proceed.

{{%tip%}}**Tip:** The same form can be accessed directly from the node's [file manager](/configuration-file-manager/), using the appropriate **Export** option in the folder's context menu:

![export folder from file manager](04-export-folder-from-file-manager.png)
{{%/tip%}}

3\. In a moment, this exported folder will appear in the list.

![list of exports](05-list-of-exports.png)

That's all! During the operation, the appropriate [mount point](/mount-points/) on the target node(s) is configured automatically by the platform so that you can immediately start working with your shared data without any additional steps required.


## Managing Exports

Beside [exporting directories](#directory-export), the **Exports** section allows managing existing records.

1\. All directories shared from this container to any node on the same platform are displayed here (the [externally](/configure-external-nfs-server/) exported data won't be shown).

![navigate to the exported directory](06-navigate-to-the-exported-directory.png)

You can quickly jump to any of the exported folders by hovering over the required record and selecting the **Navigate to directory** option from the ***Additionally*** list.

2\. In order to get the exact location and target node details for the exported directories, expand the appropriate record.

![view export target nodes](07-view-export-target-nodes.png)

The following information can be found here:

* **Name** - shows stack name and ID of the node(s), where the exported folder is mounted (hover over for additional details on the appropriate environment or to unmount this record via the ***Additionally*** list)
* **Client Path** - provides a path to the folder, where shared data can be accessed at the remote node
* **Permission** - displays access permissions for the corresponding client (*rw* - read-write; *ro* - read-only)

3\. At the tools panel above the list, you can find several buttons, which are intended to help you with managing your exports on the current container.

![manage exports](08-manage-exports.png)

* with the **Export** option, you are able to [share any directory](#directory-export) inside the container with any other node at your account
* the **Unmount** button stops data sharing with the selected client node

![unmount export](09-unmount-export.png)

After confirmation, the corresponding record will be removed from the list, and the appropriate data will become unavailable at the chosen instance.

* the **Configuration** button redirects to the ***etc/exports*** file, where you can check and, if needed, manually edit the list of exports (shared folders, client addresses, additional parameters)

![exports configuration file](10-exports-configuration-file.png)

{{%note%}}**Note:** If working in the confines of your PaaS account, all of the required export configurations are automated. Manual adjustment of this file is only needed for [external exports](/configure-external-nfs-server/).{{%/note%}}

* you can **Refresh** the list with the same-named button to get the most recent shares state
* the **Documentation** button on the far right of the panel redirects to the current documentation page

For any additional configuration, you can use the built-in [file manager](/configuration-file-manager/) or connect to a node over [SSH](/ssh-access/).

{{%tip%}}If you face any issues while exporting data for sharing, feel free to appeal for our technical experts' assistance at [Stackoverflow](https://stackoverflow.com/questions/tagged/jelastic).{{%/tip%}}


## What's next?

* [Data Storage Overview](/data-storage-container/)
* [Shared Storage Container](/shared-storage-container/)
* [Mount Points](/mount-points/)
* [External NFS Server Configuration](/configure-external-nfs-server/)