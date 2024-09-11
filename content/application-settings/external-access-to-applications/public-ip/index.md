---
draft: false
title: "Public IP"
aliases: ["/public-ip/", "/public-ipv4/"]
seoindex: "index, follow"
seotitle: "Public IP"
seokeywords: "public ip, ipv4, ipv6, external ip, ip address, ipv4 ipv6 paas, ipv6 cloud, ip addresses allocation, attach ip address, container ip address, container external ip, allocate ip address, external ipv4, ipv4 cloud, ipv6 hosting, external ipv6, ipv4 hosting, ipv6 for cloud hosting, ipv4 for cloud hosting"
seodesc: "Learn how to attach the Public IP addresses (either IPv4 or IPv6) to any container for more secure and effective work with your production environments. Benefit on the Public IP depended features such as FTP, WebSockets, database dumps import/export, remote debugging and SSL."
menu:
    docs:
        title: "Public IP"
        url: "/public-ip/"
        weight: 20
        parent: "external-access-to-applications"
        identifier: "public-ip.md"
---

# Public IP

The platform provides users with [Shared Load Balancer](/shared-load-balancer/) (SLB) as a default single entry point for all of the hosted applications, located on the hardware nodes. However, for the production environments, it is recommended receiving and processing the requests via **Public IP** address(es) that form a direct connection between the Internet and a specific container. Compared to the access over SLB, such approach ensures more secure and effective interaction.

![public IP vs shared load balancer](01-public-ip-vs-shared-lb.png)

Public IP can be attached to any software stack in your environment (except, [Memcached](/memcached/) node), representing a more stable solution with less risk to be affected by other applications. Also, it opens access to such features as [FTP add-on](/ftp-ftps-support/), [Custom SSL](/custom-ssl/), [remote debugging](/remote-debugging/) from IDE, [WebSockets](/websockets/), etc.

The platform supports two versions of the [Internet Protocol](https://en.wikipedia.org/wiki/Internet_Protocol):

* ***Internet Protocol version 4 (IPv4)*** is the fourth revision in the development of the IP and the first version of the protocol to be widely deployed
* ***Internet Protocol version 6 (IPv6)*** is the most recent IP version, which is an evolutionary upgrade of IPv4 and is designed to fulfill the need of more addresses, provide better multicast routing and simplify processing by routers

In order to bind an external IP address to the required node, you need to enable (or [set the required number](/multiple-public-ip/) of) *Public IPv4* / *Public IPv6* within the central part of the **topology wizard** window.

![wizard add public IP](02-wizard-add-public-ip.png)

{{%note%}}**Notes:**

- Enabling Public IPv4 turns off the [Access via SLB](/shared-load-balancer/#deny-access-via-shared-load-balancer) option by default. It may cause a temporary (a few minutes) disruption in environment access due to the DNS cache.
- In case of attaching external IPs for the [horizontally scaled](/horizontal-scaling) nodes, each container within the layer will be supplied with its own set of addresses.{{%/note%}}

To find and manage the allocated IPs in the existing environment, expand the appropriate ***node*** string in the environment topology list.

![dashboard manage external ip addresses](03-dashboard-manage-external-ip-addresses.png)

Here, upon hovering over IPs, you can get access to the following functionality:

* **Copy to Clipboard** - copies the appropriate address in one click
* **Attach/Detach IP(s)** - allows adjusting a number of public IPs (both IPv4 and IPv6)
* **Detach IP** - removes a particular address

{{%tip%}}**Notes:**

* The public IP is a paid option, which is charged for every hour of its usage. The exact price is defined by your particular hosting service provider and can be found at the **[Quotas & Pricing](/resource-consumption/#how-much-do-resources-cost) > Pricing > Options** frame of the dashboard.
* If you have public IP enabled for any node in your environment, you can't use the [swap domains](/swap-domains/) functionality for it. Consider utilizing the [swap Public IPs](/cli-ip-swap/) API instead.
* If working with [multiple public IPs](/multiple-public-ip/), the very first external address attached (of each IPv4 and IPv6 types) is considered a ***primary*** one and can only be deleted last. It is used for both incoming and outgoing traffic, while the rest of IPs can only receive it.
{{%/tip%}}


## What's next?
* [Shared Load Balancer](/shared-load-balancer/)
* [Endpoints](/endpoints/)
* [Custom Domains](/custom-domains/)
* [Secure Sockets Layer](/secure-sockets-layer/)
* [FTP/FTPS Support](/ftp-ftps-support/)
* [Multiple Domains with Public IP](/multiple-domains/)