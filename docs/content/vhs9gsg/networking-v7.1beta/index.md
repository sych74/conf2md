---
draft: false
title: "Networking v7.1Beta"
aliases: "/networking-v7.1beta/"
seoindex: "index, follow"
seotitle: "Networking v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Networking v7.1Beta"
        url: "/networking-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "networking-v7.1beta.md"
---
# .Networking v7.1Beta

An OnApp Cloud installation requires four separate networks that are Management, Appliance, Storage, and Provisioning network.

The networks should be separated either physically, using different switches, or with VLANs. If you experience MAC address flapping across ports because a switch does not support the balance-rr mode, you can set up separated VLANs per each bond pair for the switch. 

The following scheme illustrates how networks handle your cloud environment. For more details on the role and configuration of each network, see the sections below. 

![](attachments/194479517/195790097.png)

## Management Network

------------------------------------------------------------------------

**
**

The management network serves as a route for communication between the Control Panel server, compute resources, and backup servers. The management network should always be a default gateway.

The management network should be a local network behind a gateway device capable of bridging traffic to the Internet to allow servers to perform tasks such as DNS resolution, NTP, and operating system updates. If the gateway has a DHCP service for allocating private IP addresses, this service must be disabled.

You must open the 443 port for outgoing connections to the OnApp Licensing Server. The Control Panel server needs to have incoming traffic allowed to ports 80/443 & 30000-&gt;40000. This should be configured at the gateway with incoming NAT. If your gateway device doesn't support it, a network can also be an external network. However, always use a firewall at the gateway to block all incoming traffic except for the ports listed above.

Since the management network serves as a route for communication between the Control Panel server, compute resources, and backup servers, the stability of this network is critical. Consider bonding to introduce network-level redundancy; the network bandwidth should be at least 1 Gbit.

If your management network is behind a firewall, ensure that ports 22/80/443/30000-40000 are open to the Control Panel server and port 22 for all other servers. The 30000-40000 ports are not required if you are going to use an HTML5 console as the console proxies over port 80 or 443.

## Appliance Network

------------------------------------------------------------------------

The appliance network is used for all virtual servers' network traffic. OnApp bridges the appliance NIC and assigns virtual interfaces to it when virtual servers are provisioned or additional network interfaces are added to virtual servers via OnApp UI or API. Since OnApp manages the public interface, the public NIC requires a blank config. 

``` java
/etc/sysconfig/network-scripts/ifcfg-ethX
ONBOOT=no
BOOTPROTO=none
```

You should configure your network interface file accordingly. You don't need to add any configurations to this NIC, such as subnet, gateway, or IP address details. The NIC could either be a standard physical interface (for example, eth1) or a bonded interface (for example, bond1). It cannot be a sub-interface (for example, eth1:1) or a VLAN sub-interface (for example, eth1.101). Take it into consideration when designing your compute resources to ensure you have a physical NIC available. The appliance network bandwidth should be at least 1 Gbit. Consider bonding on the appliance network to introduce redundancy at the network level. 
Configuring a switch trunk port is a preferred method because it gives you additional flexibility and security. Alternatively, you can configure a switch access port. In the latter case, you don't need to specify a VLAN when adding a range to OnApp. To use multiple appliance VLANs, connect your appliance network to switch ports that are configured in a VLAN trunk mode. It provides your cloud with the flexibility to offer private VLANs to users in the future. If you choose multiple appliance VLANs, associate your VLAN with a subnet when adding a range to OnApp.

## Storage Network

------------------------------------------------------------------------

### External Storage

The storage network enables a connection between storage devices (for example, SANs) and compute resources. The type of network depends on which kind of connectivity your primary storage requires. For example, if you use iSCSI or ATAoE, set up an Ethernet network. If your SAN has fibre connectivity, the storage network is a fiber network. 

The stability of the storage network is critical. Always make redundancy your primary concern when designing this network. See the [Centralized Storage (SAN)](.Storage_v7.1Beta) section for more details. 

There are the following requirements for the storage network that you need to follow: 

-   The storage network must be a local network.
-   The storage network should run at least 10 Gbit FibreChannel or InfiniBand to achieve the best performance.
-   We strongly recommend that you avoid NICs using Broadcom chipsets on the storage network due to known issues surrounding iSCSI and TCP offload in the Linux kernel modules. 
-   To achieve better performance and redundancy over 1 Gbit, consider NIC teaming/bonding and LACP or MPIO over multiple subnets.
-   If your primary storage network is running over Ethernet, then a switch connecting compute resources to SAN must support jumbo frames: the storage network on compute resources and SAN(s) must have MTU set to 9000 to optimize performance.

### Virtuozzo Storage

Refer to the [Virtuozzo Storage Administrator's Guide](index) and the [Virtuozzo Storage Administrator's Command Line Guide](index) for requirements and detailed information on Virtuozzo Storage.

## Provisioning Network

------------------------------------------------------------------------

The provisioning network is used to transfer backup and template data between the provisioning server and the primary storage volumes. The network is used to transfer large sets of data, so we recommend that it runs at least 1 Gbit. It is preferable for you to consider 10 Gbit, FibreChannel, InfiniBand, or aggregated 1 Gbit links for maximum throughput.

## External Network Connectivity

------------------------------------------------------------------------

The following table provides an overview of communications between the OnApp Control Panel server and external networks.

| Source    | Destination                                        | Port   | Description                                                                     |
|-----------|----------------------------------------------------|--------|---------------------------------------------------------------------------------|
| OnApp CP  | [licensing.onapp.com](http://licensing.onapp.com/) | 443    | For Control Panel server to communicate with the OnApp licensing dashboard.     |
| OnApp CP  | Public Internet                                    | 25     | For email notifications that are sent outbound from OnApp Control Panel server. |
| End Users | OnApp CP                                           | 80/443 | For users to access the OnApp web interface over the HTTP or HTTPS protocol.    |

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [onapp\_networks.png](attachments/194479517/195790097.png) (image/png)

