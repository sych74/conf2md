---
draft: false
title: "Shared Load Balancer"
aliases: ["/shared-load-balancer/", "/shared-resolver/"]
seoindex: "index, follow"
seotitle: "Shared Load Balancer"
seokeywords: "shared load balancer, load balancing, public ip, ip, resolver request, nginx proxy server, entry point"
seodesc: "Find out what is shared LB, which processes all incoming requests to the environment, and its benefits/limitations comparing with public IP."
menu: 
    docs:
        title: "Shared Load Balancer"
        url: "/shared-load-balancer/"
        weight: 10
        parent: "external-access-to-applications"
        identifier: "shared-load-balancer.md"
---

# Shared Load Balancer

The platform utilizes several **Shared Load Balancer** (SLB) infrastructure components to process all incoming requests (except direct connections via [public IP](/public-ip/)) sent to the hosted environments. SLB is an **NGINX proxy server** that connects the client-side (browser, for example) and your applications deployed to the platform.

![shared load balancer overview](01-shared-load-balancer-overview.png)

So, Shared Load Balancers process requests from outside the platform and navigate them over the internal network to connect to the required applications. SLB is also limited to 50 simultaneous connections per the request's source address to prevent *DDoS attacks*.

To ensure the platform's high availability, it uses **several synchronized Shared Load Balancers** (placed at different hosts) for handling requests simultaneously. All of them work with the same data storage so that they are fully interchangeable if one of the instances goes down.

![shared load balancer high availability](02-shared-load-balancer-high-availability.svg)

As a result, there can be several entry points for users' environments, and the incoming load can be efficiently distributed.

{{%tip%}}**Note:** We recommend using **SLB** for your ***dev*** and ***test*** environments. As for ***production*** environments, which are intended to handle high traffic, it is more appropriate to use your own **[public IP](/public-ip/)** for getting and processing the requests. Also, it allows you to apply several additional options to your application, making it more secure (e.g. with [Custom SSL](/custom-ssl/)) and responsive (through attaching [Custom Domain](/custom-domains/)).

![public IP vs share load balancer](03-public-ip-vs-share-load-balancer.png)
{{%/tip%}}


## Backend Health Check with Shared Load Balancer

The platform **Shared Load Balancer** performs constant servers' health checkups, utilizing the [NGINX upstream check module](https://github.com/yaoweibin/nginx_upstream_check_module) with the following settings for that:

```
check interval=15000 rise=2 fall=3 timeout=2000 default_down=false;
```

In such a way, all containers are considered "up" after SLB starts. Then the system verifies nodes' availability every 15 seconds. If no response is received from a container within 2 seconds, such checkup is regarded as failed. Three consecutive fails mark a node as "down" and two successful checks in a row - as "up".

{{%tip%}}**Tip:** If an environment has several backends (application servers), the [dedicated load balancer nodes](/load-balancing/) are automatically added to manage traffic and perform health checks.{{%/tip%}}


## Deny Access via Shared Load Balancer

The platform provides a predefined option to disable external access to environment nodes from SLB. It prohibits access to containers over their default domain names with a single click (without public IP addition and firewall adjustment). An option is available as the **Access via SLB** toggle in the topology wizard.

![access via SLB](04-access-via-slb.png)

{{%tip%}}**Note:** The platform automatically disables **Access via SLB** for the layer after adding a **Public IP**. Such configs are recommended to provide the highest security level for your application. However, in case of necessity, you can re-enable *Access via SLB* to use both options simultaneously.{{%/tip%}}


The option is ***enabled*** for each layer by default, which ensures the following behavior:

- nodes are accessible from the Shared Load Balancer via environment domain names using the default ports (*80*, *8080*, *8686*, *8443*, *4848*, *4949*, *7979*)
- the **Open in Browser** button opens the appropriate service (e.g. database admin panel)
- nodes' links are present in the emails (if needed)

You can manually ***disable*** the *Access via SLB* feature:

- nodes are inaccessible from the Shared Load Balancer - layer is isolated from the SLB
- the pages accessible via the **Open in Browser** button in the dashboard return the *403 Forbidden* error instead of the intended service
- nodes' links are excluded from the emails
- access via [SSH](/ssh-access/) and through [endpoints](/endpoints/) is <u>*not affected*</u>

For better visibility, layers with the disabled SLB access are provided with the appropriate label in the dashboard.

![no SLB access label](05-no-slb-access-label.png)

Connecting to such nodes via the default URL will return the following error page instead of the default service:

![403 forbidden access](06-403-forbidden-access.png)

Below, we've prepared some of the most frequent use case examples for the feature:

- close public access via SLB to nodes that are intended for internal access only (e.g. databases)
- forbid access via SLB to nodes with public IP address attached and custom domain configured
- configure topology that allows connection via environment load balancer but prohibits access via direct URL to containers

In general, you can use the *Access via SLB* option for your ***development*** and ***testing*** environments. However, we recommend disabling the feature for the application in ***production*** and using [public IP](/public-ip/) with a [custom domain](/custom-domains/) instead.


## What's next?

* [Load Balancing](/load-balancing/)
* [Public IP](/public-ip/)
* [Endpoints](/endpoints/)
* [Isolated Containers](/isolated-containers/)