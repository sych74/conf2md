---
draft: false
title: "Environment Aliases"
aliases: "/environment-aliases/"
seoindex: "index, follow"
seotitle: "Environment Aliases"
seokeywords: ""
seodesc: "Specifying the alias (alternative name) for an environment or a separate node can greatly facilitate the process of their management. It clarifies which item you are working with, so you'll never..."
menu: 
    docs:
        title: "Environment Aliases"
        url: "/environment-aliases/"
        weight: 70
        parent: "environment-management"
        identifier: "environment-aliases.md"
---

# Environment Aliases

Specifying the alias (alternative name) for an environment or a separate node can greatly facilitate the process of their management. It clarifies which item you are working with, so you'll never make a mistake while choosing the environment/node that needs to be adjusted.

This ability is especially useful while working with numerous nodes of the same type, possibly due to the [multi nodes](/horizontal-scaling/) feature. Let's consider this on the example of defining the master and slave nodes in a DB cluster.

1\. Select the necessary environment with a set of same-type nodes and expand the instances list:

![environment aliases instaces list](01-environment-aliases-instaces-list.png)

2\. Choose the node you would like to add the label for and click the **Set Alias** pencil pictogram next to it (or simply double-click on the **Node ID: xxx** string). Whatever you enter into the appeared input field, the value will be automatically saved.

![set aliases](02-set-alias.png)

3\. In the same way you can add a label for a whole environment (wherein the domain name will remain the same).

![environment label](03-environment-label.png)

Such a custom name will define the corresponding item in all the appropriate lists:

* at the dashboard
![environment aliases dashboard](04-environment-aliases-dashboard.png)

* in the [SSH](/ssh-gate/) console
![environment aliases SSH](05-environment-aliases-ssh.png)
![nodes aliases SSH](06-nodes-aliases-ssh.png)

Also, these labels are visible for other users [in collaboration](/account-collaboration/) and remain attached after environment's [cloning](/clone-environment/), [transferring](/environment-transferred/), etc.

Deleting the alias name anytime will return the default value.


## What's next?

* [SSH Gate](/ssh-gate/)
* [Horizontal Scaling](/horizontal-scaling/)
* [Share Environment](/share-environment/)
* [Clone Environment](/clone-environment/)