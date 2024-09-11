---
draft: true
title: "Elastic Ubuntu VPS"
aliases: "/elastic-vps-ubuntu/"
seoindex: "index, follow"
seotitle: "Elastic Ubuntu VPS"
seokeywords: "vps hosting, ubuntu vps, elastic vps, elastic ubuntu vps, ubuntu vps installation, ubuntu server, ubuntu private server, ubuntu virtual private server, create ubuntu vps"
seodesc: "Get a virtual private server on top of the Ubuntu operating system in a few minutes. Utilize full root permissions and a powerful dashboard for managing your elastic server."
menu:
    docs:
        title: "Ubuntu Elastic VPS"
        url: "/elastic-vps-ubuntu/"
        weight: 20
        parent: "elastic-vps-topologies"
        identifier: "elastic-vps-ubuntu.md"
---

# Elastic Ubuntu VPS

{{%imageLeft%}}![Ubuntu VPS logo](01-ubuntu-vps-logo.png){{%/imageLeft%}}

**[Ubuntu](https://www.ubuntu.com/)** appears to be one of the most popular operating systems for running virtual private servers inside the Cloud. Being built over the Debian Linux distribution, Ubuntu shares its commitment to principles of open-source software and offers continually developing solutions with flexible, secure, and versatile performance capabilities.

At the platform, Ubuntu-based Elastic VPS is delivered with all the functionality of an independent virtual machine (like security guarantees, cost efficiency, and root permissions granted), combining it with Ubuntu’s reliable and robust ecosystem.


## Ubuntu VPS Installation

1\. Click the **New Environment** button at the top of the dashboard.

![new environment button](02-new-environment-button.png)

2\. Within the opened wizard, select the required OS for your Elastic VPS server (**Ubuntu** in our case).

![Ubuntu VPS wizard](03-ubuntu-vps-wizard.png)

Here, the following configuration options are available before the installation:

- ***Vertical Scaling per Node*** - configure the upper and lower resource limits for [automatic vertical scaling](/automatic-vertical-scaling/)
- ***Horizontal Scaling*** - set the required [number of same-type nodes](/horizontal-scaling/)
- ***Disk Limit*** - allocate required disk space quantity
- ***Sequential restart delay*** - set a delay between restart operation on different nodes (required to ensure availability of at least one server when restarting scaled VPS)
- ***Access via SLB*** - allow or deny access to your VPS via the platform's [Shared Load Balancer](/shared-load-balancer/#deny-access-via-shared-load-balancer)
- ***Public IP*** - add [public IP](/public-ip/) (IPv4 or IPv6) for external access
- ***Region*** - select the target [region](/environment-regions/)
- ***Environment Name*** - set the environment name within the platform domain

Click **Create** to proceed.

3\. In a few minutes, your VPS instance will be created.

![Ubuntu VPS dashboard](04-ubuntu-vps-dashboard.png)

That's all! You can start managing your VPS server right away with a built-in [Web SSH](/web-ssh-client/) client or check the after-creation email for additional access information.


## What's next?

- [Elastic Hosting Platform](/virtuozzo-elastic-hosting-platform/)
- [CentOS Elastic VPS](/elastic-vps-centos/)
- [Debian Elastic VPS](/elastic-vps-debian/)
- [VzLinux Elastic VPS](/elastic-vps-vzlinux/)
- [Elastic Windows VM](/elastic-windows-vm/)
- [Elastic VPS Billing](/elastic-vps-billing/)