---
draft: false
title: "CentOS VPS"
aliases: ["/vps-centos/", "/elastic-vps-centos/"]
seoindex: "index, follow"
seotitle: "CentOS VPS"
seokeywords: "centos hosting server, elastic virtual private server, centos vps root permissions, centos vps dashboard, elastic vps, vps hosting centos, centos virtual private server, centos virtual private server hosting, centos vps root hosting, centos vps environment, centos virtual private server cloud, centos virtual private server root"
seodesc: "Get a virtual private server on top of CentOS hosted inside the platform in just a few clicks. Operate a completely private and configurable Elastic VPS with full root permissions granted."
menu:
    docs:
        title: "CentOS VPS"
        url: "/vps-centos/"
        weight: 20
        parent: "elastic-vps-overview"
        identifier: "vps-centos.md"
---

# Elastic CentOS VPS

{{%imageLeft%}}![centos vps logo](01-centos-vps-logo.png){{%/imageLeft%}}

**[CentOS](https://www.centos.org/)** (Community ENTerprise Operating System) is a free community-driven project, with open source code delivered from RHEL Linux distribution.

Due to continuous community contribution, CentOS offers enterprise-level stability strengthened by robust performance and represents a reliable, low-maintenance, secure option for running virtual private servers.


## CentOS VPS Hosting

So, to effortlessly set up your own CentOS [Elastic VPS](/vps/) inside the platform, log in to your PaaS account and access environment topology wizard.

The appropriate instance (i.e., ***CentOS 6.8*** or ***CentOS 7.2***) can be found within the appropriate *VPS* section at the bottom left wizard corner (for the detailed installation guidance, refer to the [VPS Configuration](/vps-configuration/) page).

![create CentOS VPS](02-create-centos-vps.png)

{{%note%}}**Note:** By default, the **VPS** node is delivered with the automatically attached **[Public IP](/public-ip/)** address (one [per instance](/horizontal-scaling/)).{{%/note%}}

The platform provides a set of [inbuilt tools](/vps-configuration/#inbuilt-tools) for applying some basic settings to your VPS instance right via the dashboard UI. For more complicated configs, you'll need to access it via SSH - this can be accomplished through the [SSH Gate](/vps-ssh-gate/) or via any [3d-party software](/vps-public-ip/) (i.e., external SSH client) using Public IP address.

Once your virtual private server on top of CentOS is set up and properly configured, consider exploring the following example tutorials:

* [How to Run Java Console Application](/standalone-application/)
* [How to Set Up Mail Server Inside VPS](/adding-mail-server-vps/)


## What's next?

* [Elastic VPS Overview](/vps/)
* [Ubuntu VPS](/vps-ubuntu/)
* [Windows VM](/win-vm/)
* [VPS Access via SSH Gate](/vps-ssh-gate/)
* [VPS Access via Public IP](/vps-public-ip/)