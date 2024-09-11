---
draft: false
title: "Environment Isolation"
aliases: "/environment-isolation/"
seoindex: "index, follow"
seotitle: "Environment Isolation"
seokeywords: "environment isolation php app server, container network isolation, container network isolation in cloud, php environment isolation in cloud, private network isolation ruby app server, environment network isolation in account, environment node isolation in cloud, environment network isolation cloud, java app server environment isolation in cloud, ruby environment isolation in cloud, node.js app server environment isolation, private network isolation app server, automatic network isolation in cloud, container private network isolation, containers interconnection isolation, environment isolation python app server, nodejs environment isolation in cloud, ruby app server environment isolation, private network isolation php app server"
seodesc: "The Network Isolation feature automatically separates accounts on the platform from interconnecting and allows to put environments into the dedicated secure groups to isolate different applications within the account."
menu: 
    docs:
        title: "Environment Isolation"
        url: "/environment-isolation/"
        weight: 110
        parent: "environment-management"
        identifier: "environment-isolation.md"
---

# Environment Network Isolation

{{%note%}}This feature availability depends on the particular hosting provider settings.{{%/note%}}

The **Network Isolation** feature manages the default access rules between environments inside a single PaaS installation (i.e. connectivity over the internal network).

![request handling with firewall and isolation](01-request-handling-with-firewall-and-isolation.png)

This way, each internal connection between nodes on the platform needs to pass the proper check-up before being allowed. Namely, it is verified that the requesting and requested environments belong to the same isolated group.

{{%tip%}}**Tip:** Additionally, the connectivity of nodes can be restricted by the [container firewall](/custom-firewall/) rules, which represent a more flexible solution that is suitable for both internal and external access management.{{%/tip%}}


## Private Network Isolation

If the **Network Isolation** feature is enabled on the platform, all accounts are isolated from each other by default. In such a case, the connection between environments on different user accounts can be established only if configured explicitly on both ends.

Additionally, the feature allows developers to isolate [groups of environments](/environment-groups/) within a particular account. Just turn on the ***Network Isolation*** switcher in the **Add/Edit Group** frame.

![enable isolation for environment group](02-enable-isolation-for-environment-group.png)

The platform automatically unites the containers' internal addresses into a dedicated IP set for each isolated group. This allows controlling access between nodes (i.e. if IPs are within the same set - interconnection is permitted, and if not - denied). The platform automatically detects all the related changes under your account (e.g. environment removal, [nodes scaling](/horizontal-scaling/), etc.) to keep *IP sets* up-to-date. 

While managing *Network Isolation*, you should consider the following peculiarities:
- isolation can be enabled for the top-level group only (i.e. not for [subgroups](/environment-groups-management/#add-subgroups))
- environment groups with enabled isolation are provided with a custom shield icon ({{%icon%}}![isolated group icon](03-isolated-group-icon.png){{%/icon%}} ) for better recognition
- [shared environments](/share-environment/) can not be included into isolated groups by collaborators
- this feature is not suitable to limit the access to your containers from outside of the platform (e.g. via [public IP](/public-ip/))


## Using Network Isolation

Summing all this up, *Network Isolation* is a useful and user-oriented feature aimed to prevent undesired access to your environments. Commonly, it’s a good practice to isolate your [applications](/paas-components-definition/#application) from each other. For example:

* If you need to share access to your application or database with a third-party employee or company, you’ll be sure that containers inside the isolated group won’t be accessible via the platform's internal network

* If you are [cloning](/clone-environment/) an initially isolated project, it will be protected from the clone’s influence (e.g. if your copied project inherited a "hardcoded" database access, it will be disabled by the network Isolation feature so that the actual production data could not be changed)

This way, the *Network Isolation* feature can separate projects on a single account and prevent undesired interconnections between them.


## What's next?

* [Environment Groups](/environment-groups/)
* [Container Firewall](/custom-firewall/)
* [Shared Load Balancer](/shared-load-balancer/)
* [Public IP](/public-ip/)
* [Endpoints](/endpoints/)
