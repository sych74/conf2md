---
draft: false
title: "PXE Installation v7.1Beta"
aliases: "/pxe-installation-v7.1beta/"
seoindex: "index, follow"
seotitle: "PXE Installation v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "PXE Installation v7.1Beta"
        url: "/pxe-installation-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "pxe-installation-v7.1beta.md"
---
# PXE Installation v7.1Beta

This section explains how to install Virtuozzo Hybrid Server over network using a Linux-based preboot execution environment (PXE).

You can install Virtuozzo Hybrid Server over network in one of the two modes:

-   **Attended**. This mode is very much the same as installing Virtuozzo Hybrid Server from a DVD. The key difference is that the distribution files are delivered over network. In this mode, you will need to configure installation options manually. The attended mode can be used to install Virtuozzo Hybrid Server on a small number of servers.

-   **Unattended**. In this mode, Virtuozzo Hybrid Server installer uses a kickstart file with instructions on how to configure the server and install Virtuozzo Hybrid Server and requires no interaction on your part. The unattended mode can be recommended to automate Virtuozzo Hybrid Server installation on a large number of servers.

In a nutshell, the PXE network installation procedure involves these steps:

1.  Make the Virtuozzo Hybrid Server distribution available over network by configuring the HTTP, TFTP, and DHCP servers.

2.  Create a kickstart file if unattended installation is planned.

3.  Boot the client server from network and install Virtuozzo Hybrid Server in one of the two modes.

-   [Preparing for PXE Installation](.Preparing_for_PXE_Installation_v7.1Beta)
-   [Preparing a Kickstart File](.Preparing_a_Kickstart_File_v7.1Beta)
-   [Launching Installation](.Launching_Installation_v7.1Beta)


