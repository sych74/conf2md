---
draft: false
title: "Hardware Specifications"
aliases: "/hardware-specifications/"
seoindex: "index, follow"
seotitle: "Hardware Specifications"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Hardware Specifications"
        url: "/hardware-specifications/"
        weight: 10
        parent: "get-started"
        identifier: "hardware-specifications.md"
---
# Hardware Specifications

To run an OnApp installation, set up one Control Panel server, at least two compute resource servers and one backup server. These server instances are required to handle your environment as follows: 

-   **Control Panel Server 
    **
    The Control Panel server hosts the OnApp user interface and database and handles all cloud management processes. You do not need to set up a separate database server for your OnApp installation. OnApp provides full compatibility of Control Panel UI with Google Chrome and Firefox web browsers where JavaScript is enabled. 
-   **Compute Resource Servers 
    **The** **compute resource servers provide CPU, RAM, and storage resources for applications and virtual servers that you or your users run in the cloud. A certain amount of CPU and RAM on each server is reserved for a compute resource (hypervisor) and the storage controller system. The remaining resources are available for allocation to virtual servers. You can set up at least two compute resource servers and scale out based on your needs. 
    **
    **
-   **Backup Server **
    **
    **The backup server stores virtual server backups and templates from which you can create virtual servers. It also handles disk-related transactions, such as provisioning virtual servers, taking backups, and resizing disks. The backup server may be optional for a staging environment. However, it is critical for an environment running production workloads. The backup server should include a backup storage volume that can be a local disk array or a mounted SAN/NAS storage. 

This document provides hardware suggestions and recommendations for the minimum size of servers you can use to set up each server in your environment. 

-   [**Control Panel Server**](#tabs-6e7dc3a7-c3cd-49d6-b273-b73429d8e409-1)
-   [**Compute Resources Server**](#tabs-6e7dc3a7-c3cd-49d6-b273-b73429d8e409-2)
-   [**Backup Server**](#tabs-6e7dc3a7-c3cd-49d6-b273-b73429d8e409-3)
-   [**Network Hardware**](#tabs-6e7dc3a7-c3cd-49d6-b273-b73429d8e409-4)
-   [**Local Storage**](#tabs-6e7dc3a7-c3cd-49d6-b273-b73429d8e409-5)

To set up a Control Panel server, you can use hardware with the following specifications:

**Processor**

8 Cores CPUs
lntel Xeon e5-2640 v3 or similar

**Memory**

64+ GB DDR4 RAM

**Disks**

2 x 500 GB SSD

**RAID**

RAID 1

**Network Interfaces**

2 x 1 Gbps+

To set up a compute resource server, you can use hardware with the following specifications:

**Processor**

8 Core CPUs
Intel Xeon e5-2640 v3 or similar

**Memory**

64 GB DDR4 RAM

**Disks**

2-4 x 500 GB - 1 TB SATA/SAS/SSD (for VS storage)
1 x 500+ GB NVMe (for caching)

**RAID**

PCIe Gen3
PERC H730 1 GB Cache or similar
Pass-through / JBOD Mode

**Network Interfaces**

2 x 1 Gbps+ and 2 х 10 Gbps+

To set up a backup server, you can use hardware with the following specifications:

**Processor**

8 Core CPUs
Intel Xeon e5-2620 v3 or similar

**Memory**

32+ GB DDR4 RAM

**Disks**

12 x 2 TB SAS

**RAID**

RAID 5/6/10

**Network Interfaces**

1 x 1 Gbps+ and 2 х 10 Gbps+

To set up a network, you can use hardware with the following specifications:

2 x High performance switches with 48 x 10 GbE and 4 x 40 GbE ports.

If you want to use local storage, the following requirements are recommended to implement:

-   At least one dedicated partition on each compute resource.
-   A separate disk from the primary OS drive is recommended*.*


