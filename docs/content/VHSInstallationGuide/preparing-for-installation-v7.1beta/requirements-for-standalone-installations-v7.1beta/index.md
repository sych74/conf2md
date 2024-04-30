---
draft: false
title: "Requirements for Standalone Installations v7.1Beta"
aliases: "/requirements-for-standalone-installations-v7.1beta/"
seoindex: "index, follow"
seotitle: "Requirements for Standalone Installations v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Requirements for Standalone Installations v7.1Beta"
        url: "/requirements-for-standalone-installations-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "requirements-for-standalone-installations-v7.1beta.md"
---
# Requirements for Standalone Installations v7.1Beta

The recommended hardware requirements for running Virtuozzo Hybrid Server 9 as a standalone installation are as follows:

-   x86-64 platform with hardware virtualization support: Intel VT-x (with “unrestricted guest”) or AMD Virtualization (tested only on AMD EPYC).

    To check if the Intel processor supports the “unrestricted guest” feature: 1) Download `vmxcap.py` from <https://github.com/qemu/qemu/blob/master/scripts/kvm/vmxcap>, 2) Run `python vmxcap.py | grep -i unrest`. The result must be yes.

-   CPUs: at least 4 cores, a 64-bit processor is required for running 64-bit guest operating systems.
-   RAM: 4 GB or more.
-   HDD: the minimal required disk size is the sum of the minimal /vz and root partitions, as well as the swap size:

    ``` java
    min_hdd_size = min_vz_size + min_root_size + swap_size
    ```

    Where `min_root_size` is 12 GiB, `min_vz_size` is 30 GiB, and `swap_size` depends on the RAM size. 

-   SSD (optional): at least 30 GiB (at least 32 GiB with `/boot`).
-   Network: an Ethernet network adapter and a valid IP address.

The actual number of virtual servers you can run on a physical server and their performance depend on resources they will consume.

## System Limits

------------------------------------------------------------------------

The table below lists the current hardware limits for Virtuozzo Hybrid Server 9 servers.

| Hardware | Theoretical | Certified |
|----------|-------------|-----------|
| RAM      | 64 TB       | 1 TB      |
| HDD      | 1 EB        | 50 TB     |


