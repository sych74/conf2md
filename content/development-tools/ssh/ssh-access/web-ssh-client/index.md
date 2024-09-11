---
draft: false
title: "Web SSH"
aliases: "/web-ssh-client/"
seoindex: "index, follow"
seotitle: "SSH Access via Web Browser"
seokeywords: "access to container via web ssh, access via ssh client to node, ssh access to container via web-based client, access to container in cloud via web ssh, ssh web client, cloud container ssh access, web ssh terminal, ssh access to container, access to container using ssh key, ssh access to node in cloud, ssh access to node from browser, ssh access to container in cloud, ssh access to container from browser, access via ssh client to container, web ssh client cloud"
seodesc: "A convenient web interface embedded into the platform dashboard for remote containers management directly in browser. Click the Web SSH button for instant access to any node within your cloud account."
menu: 
    docs:
        title: "Web SSH"
        url: "/web-ssh-client/"
        weight: 20
        parent: "ssh-access"
        identifier: "web-ssh-client.md"
---

# SSH Access via Web Browser

The platform allows you connect to any container directly through the browser by means of the **Web SSH** client, without the necessity to generate dedicated SSH key pair or apply any other additional configurations.

Just click the **Web SSH** button next to the required layer or a particular node for the tab with terminal emulator to be opened:
![Web SSH direct connection](01-web-ssh.png)

Using the options in the tools panel above the editor window, you are able to: 

* switch between nodes of the [horizontally-scaled](/horizontal-scaling) layer, choosing a particular one within the **Node ID** drop-down list 
* open one more tab with connection to the current container by clicking on the **Duplicate Session** option (this allows to perform several simultaneous operations on a single node, e.g. to tail logs in one terminal window and to manage an application itself in another one)

Also, web SSH client is provided with the embedded shortcuts for convenient management (their list can be also viewed by hovering over the keyboard icon in the top-right corner of the tab):

* **Copy** (Ctrl + Shift + C)
* **Paste** (Ctrl + V)
* **Settings** (Ctrl + Shift + Alt) - allows to configure emulator, e.g to switch the input method, manually change the clipboard text, etc

Now, you can start managing your container via SSH (for example, set custom variables, change firewall settings, etc.).


## What's next?
* [SSH Overview](/ssh-gate/)
* [SSH Access](/ssh-access/)
* [SSH Gate Access](/ssh-gate-access/)
* [SSH Management](https://www.virtuozzo.com/company/blog/ssh-to-container/)
* [SSH Protocols](/ssh-protocols/)