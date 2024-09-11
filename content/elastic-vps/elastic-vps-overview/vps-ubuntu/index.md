---
draft: false
title: "Ubuntu VPS"
aliases: ["/vps-ubuntu/", "/elastic-vps-ubuntu/"]
seoindex: "index, follow"
seotitle: "Ubuntu VPS"
seokeywords: "ubuntu vps full access, ubuntu vps hosting, ubuntu vps root, ubuntu vps, ubuntu server vps, ubuntu vps server, ubuntu hosting vps, ubuntu vps ssh, elastic vps, vps ubuntu distribution, ubuntu vps root access, ubuntu vps root hosting, ubuntu 16.04 vps, ubuntu vps container, ubuntu vps root permissions, ubuntu elastic vps"
seodesc: "Run a virtual private server built on top of Ubuntu distribution with full root permissions guaranteed. Get your own reliable Elastic VPS hosted within a few minutes inside the platform. "
menu:
    docs:
        title: "Ubuntu VPS"
        url: "/vps-ubuntu/"
        weight: 30
        parent: "elastic-vps-overview"
        identifier: "vps-ubuntu.md"
---

# Elastic Ubuntu VPS

{{%imageLeft%}}![Ubuntu VPS logo](01-ubuntu-vps-logo.png){{%/imageLeft%}}

**[Ubuntu](https://www.ubuntu.com/)** appears to be one of the most popular operating systems for running virtual private servers inside the Cloud. Being built over the Debian Linux distribution, Ubuntu shares its commitment to principles of open-source software and offers continually developing solutions with flexible, secure, and versatile performance capabilities.

At the platform, Ubuntu-based Elastic VPS is delivered with all the functionality of an [independent virtual machine](/vps/) (like security guarantees, cost efficiency, and root permissions granted), combining it with the Ubuntu's reliable and robust ecosystem.


## Ubuntu VPS Hosting

With the platform, Ubuntu VPS installation represents an entirely automated process, performed in a matter of minutes.

Log into your platform dashboard and open the topology wizard by clicking the **New Environment** button. Within the dialog, enable the *VPS* section at the bottom left corner and select the ***Ubuntu*** template from the expendable options list.

![ubuntu vps topology wizard](02-ubuntu-vps-topology-wizard.png)

Adjust the rest options (cloudlet limits, [number](/horizontal-scaling/) of server instances and name for your environment) and click the **Create** button.

{{%note%}}**Note:** Working with **VPS** presupposes usage of [external IP](/public-ip/) addresses (one per instance), which are automatically attached to the corresponding container(s).{{%/note%}}

That's it! Your fully isolated virtual server is ready to work so that you can proceed with the required software and services set up.

For quick access to container file system, an appliance of some basic configurations and tracking logs via comprehensive UI use the platform dashboard [inbuilt tools](/vps-configuration/#inbuilt-tools). For the more advanced Ubuntu VPS management, consider connecting to virtual private server via [SSH Gate](/vps-ssh-gate/) or [Public IP address](/vps-public-ip/).


## What's next?

* [Elastic VPS Overview](/vps/)
* [CentOS VPS](/vps-centos/)
* [Windows VM](/win-vm/)
* [VPS Access via SSH Gate](/vps-ssh-gate/)
* [VPS Access via Public IP](/vps-public-ip/)