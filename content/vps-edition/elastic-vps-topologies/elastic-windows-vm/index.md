---
draft: true
title: "Elastic Windows-VM"
aliases: "/elastic-windows-vm/"
seoindex: "index, follow"
seotitle: "Elastic Windows VM"
seokeywords: "vm hosting, windows vm, elastic vm, elastic windows vm, windows vm installation, windows server, windows private server, windows virtual machine, create windows vm"
seodesc: "Get a virtual machine on top of the Windows operating system in a few minutes. Utilize full administrator permissions and a powerful dashboard for managing your elastic server."
menu:
    docs:
        title: "Windows Elastic VM"
        url: "/elastic-windows-vm/"
        weight: 50
        parent: "elastic-vps-topologies"
        identifier: "elastic-windows-vm.md"
---

# Elastic Windows VM

{{%imageLeft%}}![Windows VM logo](01-windows-vm-logo.png){{%/imageLeft%}}

**[Windows](https://www.microsoft.com/)** hosting support allows developers and ISV companies to host web applications and services that are run on the Windows operating system. Platform combines the functionality of a Virtual Machine with the availability of the Cloud to complement the strength of the operating system. Windows Server is the platform for building an infrastructure of connected applications, networks, and web services, from the workgroup to the data center.

In this guide, we'll show how to create a Windows VM server and the VMs hosting specifics compared to the regular VPS containers used on the platform.

{{%note%}}**Note:** The availability of the Window VMs on the platform depends on the particular service hosting provider settings.{{%/note%}}


## Windows VM Installation

1\. Click the **New Environment** button at the top of the dashboard.

![new environment button](02-new-environment-button.png)

2\. Within the opened wizard, select the required OS for your Elastic VPS server (**Windows VM** in our case).

![Windows VM wizard](03-windows-vm-wizard.png)

Here, the following configuration options are available before the installation:

- ***Resources*** - choose from the available fixed plans for your virtual machine (hover over the price icon to view all the available tariffs)
- ***Disk Limit*** - allocate required disk space quantity
- ***Sequential restart delay*** - set a delay between restart operation on different nodes (required to ensure availability of at least one server when restarting scaled VMs)
- ***Access via SLB*** - allow or deny access to your VPS via the platform's [Shared Load Balancer](/shared-load-balancer/#deny-access-via-shared-load-balancer)
- ***Public IP*** - add [public IP](/public-ip/) (IPv4) for external access
- ***Region*** - select the target [region](/environment-regions/)
- ***Environment Name*** - set the environment name within the platform domain

Click **Create** to proceed.

3\. In a few minutes, your VM instance will be created.

![Windows VM dashboard](04-windows-vm-dashboard.png)

{{%tip%}}**Tip:** You can find additional information on managing your [Windows VMs](/win-vm/) in the linked guide.{{%/tip%}}

That's all! You can start managing your VPS server right away with a built-in [RDP](/win-rdp-access/) client or check the after-creation email for additional access information.


## What's next?

- [Elastic Hosting Platform](/virtuozzo-elastic-hosting-platform/)
- [CentOS Elastic VPS](/elastic-vps-centos/)
- [Ubuntu Elastic VPS](/elastic-vps-ubuntu/)
- [Debian Elastic VPS](/elastic-vps-debian/)
- [VzLinux Elastic VPS](/elastic-vps-vzlinux/)
- [Elastic VPS Billing](/elastic-vps-billing/)