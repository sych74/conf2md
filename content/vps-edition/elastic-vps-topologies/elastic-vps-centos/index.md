---
draft: true
title: "Elastic CentOS VPS"
aliases: "/elastic-vps-centos/"
seoindex: "index, follow"
seotitle: "Elastic CentOS VPS"
seokeywords: "vps hosting, centos vps, elastic vps, elastic centos vps, centos vps installation, centos server, centos private server, centos virtual private server, create centos vps"
seodesc: "Get a virtual private server on top of the CentOS operating system in a few minutes. Utilize full root permissions and a powerful dashboard for managing your elastic server."
menu:
    docs:
        title: "CentOS Elastic VPS"
        url: "/elastic-vps-centos/"
        weight: 10
        parent: "elastic-vps-topologies"
        identifier: "elastic-vps-centos.md"
---

# Elastic CentOS VPS

{{%imageLeft%}}![CentOS VPS logo](01-centos-vps-logo.png){{%/imageLeft%}}

**[CentOS](https://www.centos.org/)** (Community ENTerprise Operating System) is a free community-driven project, with open source code delivered from RHEL Linux distribution.

Due to continuous community contribution, CentOS offers enterprise-level stability strengthened by robust performance and represents a reliable, low-maintenance, secure option for running virtual private servers.

## CentOS VPS Installation

1\. Click the **New Environment** button at the top of the dashboard.

![new environment button](02-new-environment-button.png)

2\. Within the opened wizard, select the required OS for your Elastic VPS server (**CentOS** in our case).

![CentOS VPS wizard](03-centos-vps-wizard.png)

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

![CentOS VPS dashboard](04-centos-vps-dashboard.png)

That's all! You can start managing your VPS server right away with a built-in [Web SSH](/web-ssh-client/) client or check the after-creation email for additional access information.


## What's next?

- [Elastic Hosting Platform](/virtuozzo-elastic-hosting-platform/)
- [Ubuntu Elastic VPS](/elastic-vps-ubuntu/)
- [Debian Elastic VPS](/elastic-vps-debian/)
- [VzLinux Elastic VPS](/elastic-vps-vzlinux/)
- [Elastic Windows VM](/elastic-windows-vm/)
- [Elastic VPS Billing](/elastic-vps-billing/)