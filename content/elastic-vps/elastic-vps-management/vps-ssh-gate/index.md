---
draft: false
title: "Linux VPS Access via SSH Gate"
aliases: ["/vps-ssh-gate/", "/vps-jelastic-gate/", "/vps-jelastic-gateway/"]
seoindex: "index, follow"
seotitle: "SSH Access to VPS"
seokeywords: "ssh access vps, virtual private server ssh root, virtual private server ssh connection, virtual private server ssh, vps ssh protocol, ssh connect to virtual private server, vps ssh access, connect to vps with ssh, ssh connect to vps windows, vps ssh connect putty"
seodesc: "Access your virtual private server over SSH protocol by means of SSH Gate functionality. Learn how to launch SSH connection based on the used operating systems, namely Linux, MacOS, BSD and Windows. "
menu: 
    docs:
        title: "Linux VPS Access via SSH Gate"
        url: "/vps-ssh-gate/"
        weight: 20
        parent: "elastic-vps-management"
        identifier: "vps-ssh-gate.md"
---

# Linux VPS Access via SSH Gate

In order to manage the required software inside your Elastic VPS container, you need to connect to it via SSH protocol. A connection can be performed through the dedicated [SSH Gate](/ssh-overview), which provides a single access point to configure all environments and servers within your account remotely.
{{%tip%}}**Note:** For the *Windows VPS* management, utilize the [remote desktop protocol](/win-rdp-access) (RDP) support.{{%/tip%}}

The process of [SSH access](/ssh-access) to the Elastic VPS nodes is the same as for any other container on the platform but provides full root access.

* ***[Web SSH](/web-ssh-client)***

A one-click connection to your VPS container from the platform dashboard without any configuration required.
![elastic vps web ssh access](01-elastic-vps-web-ssh-access.png)

* ***[SSH Gate](/ssh-gate-access)***

An SSH connection to VPS from the console on your local machine. Access is based on your custom SSH key pair.
{{%tip%}}**Note:** If you haven't established a connection via SSH Gate before, you'll need to perform the following steps beforehand:

* [generate](/ssh-generate-key) an SSH key pair
* [add your public SSH key](/ssh-add-key) to the dashboard
{{%/tip%}}
![elastic vps access via ssh gate](02-elastic-vps-access-via-ssh-gate.png)

In case you prefer to operate your VPS container with the help of external SSH tools, consider establishing [access via Public IP](/vps-public-ip) address. Regardless of the chosen approach, the provided functionality and management capabilities are the same.


## What's next?
* [Elastic VPS Overview](/vps/)
* [VPS Configuration](/vps-configuration/)
* [Linux VPS Access via Public IP](/vps-public-ip/)
* [Windows VPS Access via RDP](/win-rdp-access/)