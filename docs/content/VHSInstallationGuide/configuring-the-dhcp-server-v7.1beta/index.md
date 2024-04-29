---
draft: false
title: "Configuring the DHCP Server v7.1Beta"
aliases: "/configuring-the-dhcp-server-v7.1beta/"
seoindex: "index, follow"
seotitle: "Configuring the DHCP Server v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Configuring the DHCP Server v7.1Beta"
        url: "/configuring-the-dhcp-server-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "configuring-the-dhcp-server-v7.1beta.md"
---
# Configuring the DHCP Server v7.1Beta

To configure the DHCP server, do the following:

1.  Make sure the DHCP server package is installed:

    ``` java
    # yum install dhcp
    ```

2.  Add the following lines to the file `/etc/dhcp/dhcpd.conf` (or `/etc/dhcpd.conf`):

    -   For installation on BIOS-based client servers:

        ``` java
        next-server <TFTP_server_IP_address>;
        filename "/pxelinux.0";
        ```

    -   For installation on EFI-based client servers:

        ``` java
        next-server <TFTP_server_IP_address>;
        filename "/grubx64.efi";
        ```

3.  Start the DHCP server if you installed it in step 1:

    ``` java
    # systemctl start dhcpd.service
    ```

    Or restart the existing DHCP server:

    ``` java
    # systemctl restart dhcpd.service
    ```


