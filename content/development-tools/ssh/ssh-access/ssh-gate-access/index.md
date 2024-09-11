---
draft: false
title: "SSH Gate"
aliases: ["/ssh-gate-access/", "/ssh-local-client/"]
seoindex: "index, follow"
seotitle: "Access via SSH Gate"
seokeywords: "access via ssh client to node, using ssh key for connect to node, using ssh key for access to node, access container with ssh key, cloud container ssh access, ssh access to container via terminal, access to container using public ssh key, ssh access to container, using ssh key for connect to container, ssh access to node in cloud, ssh access to container in cloud, access to container using private ssh key, access via ssh client to container, ssh access via local client, connection with ssh key pair"
seodesc: "Learn about SSH connection with a local SSH client application. Connect to your platform account (or directly to the required node using its ID) via SSH Gate to gain a possibility of a remote container management."
menu: 
    docs:
        title: "SSH Gate"
        url: "/ssh-gate-access/"
        weight: 30
        parent: "ssh-access"
        identifier: "ssh-gate-access.md"
---

# Access via SSH Gate
In order to establish connection via SSH Gate, you need to [generate SSH key pair](/ssh-generate-key) and to [add public key](/ssh-add-key) to your account at the dashboard (if needed, read the linked step-by-step guides for assistance).

Next, get an SSH connection string for your account by clicking the **Settings** button at the top panel of the dashboard.
![account settings button](01-account-settings.png)

In the opened **Account settings** window, the **SSH Keys > SSH Connect** tab will be opened by default. Here, you can see information required for accessing an account, including an SSH connection string (circled in the image below).
![account settings ssh connect information](02-ssh-connect-info.png)

{{%tip%}}**Tip:** Within the right part of the section you can establish [Web SSH](/web-ssh-client) connection to any node directly in browser.{{%/tip%}}

Now,<a id="account"></a> you can access either [whole PaaS account](#account) or just a [particular container](#container) with your local SSH client.

## SSH Access to Platform Account
Depending on your OS, you need to perform the following steps:

* ***Linux/MacOS/FreeBSD***

Open your terminal and execute the SSH connection string.
![ssh access via terminal](03-ssh-access-terminal.png)

* ***Windows***

Download and run your SSH client ([PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) as an example). 

Navigate to the **Session** tab in the left-hand list and fill in the **Host Name (or IP address)** and **Port** fields in accordance with your SSH connection string.
![ssh access with PuTTY client](04-ssh-access-putty.png)

{{%note%}}**Note:** In order to add your private SSH key with PuTTY, download and run [Pageant](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html) tool, click the **Add Key** button and choose the appropriate SSH key file.
![add private ssh key with pageant](05-add-private-key-pageant.png){{%/note%}}

1\. Once connected, you will see a list of [environment groups](/environment-groups) (with a number of containers within provided in brackets) and ungrouped environments available for your account. Select the required point by entering the appropriate number.
![PaaS account via SSH](06-cloud-account-ssh-.png)

{{%tip%}}**Note:** Only *running* environments can be accessed.{{%/tip%}}

2\. After selecting an environment, you'll see a full list of its containers, which are grouped by layers. Herewith, the master node (required for clustering, scaling, cloning, etc.) is designated with the *[M]* mark.
![connect environment via SSH](07-cloud-environment-ssh.png)

Also,<a id="container"></a> each container is provided with **nodeid**, **LAN IP**, **WAN IP** and **Alias** data. In order to access the required node just enter its number.


## Direct Access to Container
You can "jump" directly to the necessary container, skipping the steps of choosing the appropriate environment and node. Just state the appropriate container ID (can be seen at the dashboard next to the corresponding node) at the beginning of the connection string. 
![node ID](08-node-id.png)

For example, in order to access the Tomcat container, which is shown in the image above, you should add the *36864-* prefix to the default account connection string in the following way:
```bash
ssh 36864-4701@gate.jelastic.com -p 3022
```
Such a possibility can be useful for automatization scripts or for setting up application configurations (for example, [Capistrano](/ssh-capistrano)).


## What's next?
* [SSH Overview](/ssh-gate/)
* [Generate SSH Key](/ssh-generate-key/)
* [Add SSH Key](/ssh-add-key/)
* [Web SSH](/web-ssh-client/)
* [SSH Management](https://www.virtuozzo.com/company/blog/ssh-to-container/)