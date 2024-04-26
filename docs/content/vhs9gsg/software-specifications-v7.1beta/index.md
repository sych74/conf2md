---
draft: false
title: "Software Specifications v7.1Beta"
aliases: "/software-specifications-v7.1beta/"
seoindex: "index, follow"
seotitle: "Software Specifications v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Software Specifications v7.1Beta"
        url: "/software-specifications-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "software-specifications-v7.1beta.md"
---
# .Software Specifications v7.1Beta

The following table lists guest OS versions for compute resource, Control Panel, and backup servers.

| **Server **               | **Supported Versions**    |
|---------------------------|---------------------------|
| Compute Resource Server   | Virtuozzo Hybrid Server 9 |
| Control Panel Server      | AlmaLinux 9               |
| Backup Server             | Virtuozzo Hybrid Server 9 |

**Libvirt Versions**

The following table provides the libvirt versions compatible with your system, depending on the virtualization type and version.

**KVM**
CentOS 7.x (deprecated)
libvirt 3.9.0

**Requirements**

There are the following requirements for Control Panel, compute resource, and backup servers:

-   Install AlmaLinux 9 for Control Panel servers.
-   Install Virtuozzo Hybrid Server 9 for compute resources and backup servers.
-   The minimum running services are listed in the box:

    ``` java
    network    0:off    1:off    2:on    3:on    4:on    5:on   6:off 
    sshd       0:off    1:off    2:on    3:on    4:on    5:on   6:off
    ```

-   Configure the *network* with the ability to access [rpm.repo.onapp.com](http://rpm.repo.onapp.com/) and [templates.repo.onapp.com](http://templates.repo.onapp.com/).
-   Configure the *open ssh server* with the ability for users to access and log in to the box.
-   The **root** user must be available on the box and configured as a *root account*/ *root user*/ *superuser* with access to all files, commands/tools, and services on the system. Installers should be run under the **root**.
-   Ensure the *curl*, *rpm*, *yum, *and *grub *packages are installed on the system. The *grub *is a mandatory boot loader only for compute resources.


