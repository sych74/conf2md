---
draft: false
title: "Starting Installation v7.1Beta"
aliases: "/starting-installation-v7.1beta/"
seoindex: "index, follow"
seotitle: "Starting Installation v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Starting Installation v7.1Beta"
        url: "/starting-installation-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "starting-installation-v7.1beta.md"
---
# Starting Installation v7.1Beta

Virtuozzo Hybrid Server can be installed from:

-   IPMI virtual drives

-   USB drives (see [Preparing for Installation from USB Storage Drives](preparing-for-installation-from-usb-storage-drives-v7.1beta))

-   PXE servers (see [Installation Using PXE](pxe-installation-v7.1beta) for information on installing Virtuozzo Hybrid Server over the network)

    In Virtuozzo Hybrid Server 9, time synchronization via NTP is enabled by default using the `chronyd` service. If you want to use `ntpdate` or `ntpd`, stop and disable `chronyd` first.

To start the installation, do the following:

1.  Configure the server to boot from the chosen media.

2.  Boot the server and wait for the welcome screen.

3.  Choose **Install Virtuozzo Hybrid Server**.

## Enabling Forced Detection of SSDs

------------------------------------------------------------------------

Certain solid-state drives (SSDs) may not be autodetectable by the installer. It may result in issues when you create or join Virtuozzo Storage clusters. To avoid this problem, you can force the installer to identify the required drives as SSDs by doing the following:

1.  Choose the required installation option and press **E** to edit it.

2.  Add `ssd_hack=sd[,...]` at the end of the line starting with `linux /images/pxeboot/vmlinuz`. For example:

    ``` java
    linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=<VZ9_ISO_image> quiet ip=dhcp \
    ssd_hack=sdb,sdc
    ```

3.  Press **Ctrl-X** to load the selected installation option.

The installer should identify the specified drives as SSDs.

## Changing the Swap Size Calculation Method

------------------------------------------------------------------------

Virtuozzo Hybrid Server requires that a swap partition be created on the system disk during installation. The size of this partition depends on the RAM size. If automatic partitioning is used, the swap size is calculated as follows:

-   If the RAM size is 4-8 GB, the swap size equals the RAM size.

-   Otherwise, the swap size is half the RAM size.

Such a method is beneficial for memory overcommit scenarios. If, however, overcommit is not required, you can use the old method of calculating the swap size:

-   If the RAM size is 4-8 GB, the swap size equals the RAM size.

-   If the RAM size is 8-64 GB, the swap size is half the RAM size.

-   Otherwise, the swap size is 32 GB.

To have the installer use the old method while it partitions the disks automatically, boot to the welcome screen and do the following:

1.  Choose the required installation option and press **E** to edit it.

2.  Add `smallswap` at the end of the line, starting with `linux /images/pxeboot/vmlinuz`. For example:

    ``` java
    linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=<VZ9_ISO_image> quiet ip=dhcp smallswap
    ```

3.  Press **CTRL-X** to start booting the chosen installation option.

## Installing on USB Drive

------------------------------------------------------------------------

Aside from regular disks, you can install Virtuozzo Hybrid Server on a 64 GB+ USB drive. In this case, however, you will still need to place the swap partition on a regular HDD/SSD drive. It is recommended to store logs on a syslog server.

To have a USB drive recognized as an installation destination, configure the installer as follows:

1.  Choose the required installation option and press **E** to edit it.

2.  Add `allow_usb_hdd` at the end of the line starting with `linux /images/pxeboot/vmlinuz`. For example:

    ``` java
    linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=<VZ9_ISO_image> quiet ip=dhcp \
    allow_usb_hdd
    ```

    If you chose to install Virtuozzo Hybrid Server with GUI, add `expert` to this line.

3.  Press **Ctrl-X** to load the selected installation option.

4.  On the installer’s **INSTALLATION DESTINATION** screen, select the USB drive as system, select **I will configure partitioning** at the bottom, and click **Done** and then **OK** to proceed to the **MANUAL PARTITIONING** screen.

5.  On the **MANUAL PARTITIONING** screen, select the swap partition in the list, click **Modify** on the right, and select an HDD or SSD drive to place the swap on.

6.  Click **Done**, then **Accept Changes** to return to the main installer screen and configure other options as usual.


