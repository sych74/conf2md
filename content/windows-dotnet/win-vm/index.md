---
draft: false
title: "Windows Server VM"
aliases: ["/win-vm/", /win-vps/, "/elastic-windows-vm/"]
seoindex: "index, follow"
seotitle: "Windows Server VM"
seokeywords: "windows, windows 2019, windows 2022, virtual machines, windows vm, windows server, windows paas, windows vm hosting, windows server vm, create windows vm, windows vm managing"
seodesc: "The platform offers Windows-based environments hosting via the virtual machines (VM). Learn how to create and manage Windows Server VM using the platform's dashboard."
menu:
    docs:
        title: "Windows Server VM"
        url: "/win-vm/"
        weight: 20
        parent: "windows-dotnet"
        identifier: "win-vm.md"
---

# Windows Server VM

The platform integrates support of the virtual machines (VMs), which allows offering Windows Server hosting. In this guide, we'll show how to create a Windows VM server and the VMs hosting specifics compared to the regular containers used on the platform.

{{%note%}}**Note:** The availability and version of the Window VMs (e.g., *Windows Server 2019* or *2022*) on the platform depends on the particular service hosting provider settings.{{%/note%}}


## Creating Windows VM

1\. Click the **New Environment** button at the top of the dashboard to open the topology wizard. Expand the VPS section to locate the Windows server (the *VM* label helps separate the option from containers).

![Windows VM topology wizard](01-windows-vm-topology-wizard.png)

2\. Only fixed resources are available for virtual machines, so when a VM is selected, the wizard's central part is adjusted. Here, you can choose from several predefined plans using the slider. Hover over the price icon to view all the available tariffs for the VM.

![Windows VM resource plans](02-windows-vm-resource-plans.png)

Also, note that the *[horizontal scaling](/horizontal-scaling/)* and *IPv6* options are not available for virtual machines.

3\. If VM is added to the topology, an additional ***VM Resources*** line appears in the right part of the wizard (just below the cloudlets information for containers).

![VM resources and cost](03-vm-resources-and-cost.png)

The cost of the *VM Resources* is always fixed regardless of the actual consumption of the VMs. Click **Create** to proceed with environment creation.


## Managing Windows VM

1\. VMs are highlighted with a dedicated ***VM*** label and custom icon in the **Usage** column (as the cloudlets-shaped one is not suitable).

![VM label and resources icon](04-vm-label-and-resources-icon.png)

{{%tip%}}**Tip:** You can hover over the **Usage** column for a comprehensive overview of the current consumption or refer to the node **[Statistics](/view-app-statistics/)** for detailed analysis.

![VM current resource consumption](05-vm-current-resource-consumption.png){{%/tip%}}

2\. Some [node's function icons](/dashboard-guide/#function-icons-for-each-instance) for VM are a bit different compared to containers. The following options are available:

- **Add-Ons** - installs available pluggable modules (e.g. *Env Start/Stop Scheduler*)
- **Restart Node(s)** - restarts a VM
- **Statistics** - shows real-time and historical VM's resource consumption
- **Remote Desktop** - connects via RDP using the web client and resets RDP password
- **Additionally** - lists additional options, like node's info

![VM function icons](06-vm-function-icons.png)

{{%note%}}**Note:** The **[clone](/clone-environment/)** and **[migration](/environment-regions-migration/)** options are automatically disabled for environments with VMs.

![VM clone disabled](07-vm-clone-disabled.png){{%/note%}}

Let's overview these options in detail.

3\. **Statistics** are collected in the same way as for containers. However, CPU is measured in *%* for VM (instead of *MHz*).

![VM statistics monitoring](08-vm-statistics-monitoring.png)

4\. All the actual configurations and application management are performed via RDP. Use the appropriate **Remote Desktop** menu to:

- **Open in Browser** - connects to the Windows Server over the RDP using the Guacamole web client, which allows managing server directly in a browser
- **Reset RDP Password** - resets and resends password of the Windows Administrator user
- **Info** - displays a short instruction on the remote desktop connection via local RDP client
- **RDP link** - shows a link for connection via local RDP client

![VM node remote desktop options](09-vm-node-remote-desktop-options.png)

5\. In addition to the built-in web client, you can connect using any preferred local RDP application. Connect to VM based on its entry point:

* If created <u>*without external IP*</u>, an [endpoint](/endpoints/) is created automatically and can be used for RDP connection
![Windows VM endpoint for RDP](10-windows-vm-endpoint-for-rdp.png)

* If a <u>*public IP is attached*</u>, you can use it directly as VM's host

![Windows VM remote desktop connection](11-windows-vm-remote-desktop-connection.png)

Use administrator credentials from email to authenticate and start managing your Windows Server.

6\. The *vCPU* and *Memory* for VM are billed as one tariff, while *Disk*, *Network*, and *Options* are billed separately, just as for containers.

![Windows VM billing history](12-windows-vm-billing-history.png)

That's all you need to manage Windows VM in the platform. Refer to the official [Microsoft documentation](https://docs.microsoft.com/en-us/windows-server/) for information on the server management itself.


## What's next?

* [.NET Core (Beta)](/net-core/)
* [Windows RD Access](/win-rdp-access/)
* [Windows Roles & Features](/win-vps-roles-features/)