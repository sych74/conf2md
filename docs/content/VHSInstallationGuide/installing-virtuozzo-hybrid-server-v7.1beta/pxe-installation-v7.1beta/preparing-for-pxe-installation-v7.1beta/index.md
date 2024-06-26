---
draft: false
title: "Preparing for PXE Installation v7.1Beta"
aliases: "/preparing-for-pxe-installation-v7.1beta/"
seoindex: "index, follow"
seotitle: "Preparing for PXE Installation v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Preparing for PXE Installation v7.1Beta"
        url: "/preparing-for-pxe-installation-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "preparing-for-pxe-installation-v7.1beta.md"
---
# Preparing for PXE Installation v7.1Beta

You will need the following servers to install Virtuozzo Hybrid Server over network using PXE:

-   A TFTP server that will provide an environment for network boot.

-   An HTTP or FTP server that will provide the Virtuozzo Hybrid Server distribution files.

-   A DHCP server that will provide network configuration for other servers.

-   One or more client servers where Virtuozzo Hybrid Server will be installed. The client servers must meet the requirements described in [Preparing for Installation](.Preparing_for_Installation_v7.1Beta). In addition, they must have network cards with PXE support.

Unless they already exist in your infrastructure, the TFTP, HTTP (FTP), and DHCP servers can share the same physical machine.

This chapter describes how to configure each of the required servers for PXE installation of Virtuozzo Hybrid Server (on the example of a RHEL-like OS, for example, CentOS 7).

-   [Configuring the TFTP Server](configuring-the-tftp-server-v7.1beta)
-   [Configuring the HTTP Server](configuring-the-http-server-v7.1beta)
-   [Configuring the DHCP Server](configuring-the-dhcp-server-v7.1beta)
-   [Configuring Client Servers](configuring-client-servers-v7.1beta)


