# Preparing for PXE Installation

You will need the following servers to install Virtuozzo Hybrid Server over network using PXE:

-   A TFTP server that will provide an environment for network boot.

-   An HTTP or FTP server that will provide the Virtuozzo Hybrid Server distribution files.

-   A DHCP server that will provide network configuration for other servers.

-   One or more client servers where Virtuozzo Hybrid Server will be installed. The client servers must meet the requirements described in [Preparing for Installation](.Preparing_for_Installation_v7.1Beta). In addition, they must have network cards with PXE support.

Unless they already exist in your infrastructure, the TFTP, HTTP (FTP), and DHCP servers can share the same physical machine.

This chapter describes how to configure each of the required servers for PXE installation of Virtuozzo Hybrid Server (on the example of a RHEL-like OS, for example, CentOS 7).

-   [Configuring the TFTP Server](.Configuring_the_TFTP_Server_v7.1Beta)
-   [Configuring the HTTP Server](.Configuring_the_HTTP_Server_v7.1Beta)
-   [Configuring the DHCP Server](.Configuring_the_DHCP_Server_v7.1Beta)
-   [Configuring Client Servers](.Configuring_Client_Servers_v7.1Beta)


