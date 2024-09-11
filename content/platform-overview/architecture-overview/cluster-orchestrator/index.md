---
draft: false
title: "Cluster Orchestrator"
aliases: "/cluster-orchestrator/"
seoindex: "index, follow"
seotitle: "Cluster Orchestrator"
seokeywords: ""
seodesc: "Cluster Orchestrator (Infrastructure Node) is a set of internal components for managing resources, processing requests, and supporting PaaS system maintenance."
menu: 
    docs:
        title: "Cluster Orchestrator"
        url: "/cluster-orchestrator/"
        weight: 20
        parent: "architecture-overview"
        identifier: "cluster-orchestrator.md"
---

# Cluster Orchestrator

**Cluster Orchestrator** (Infrastructure Node) is a set of internal components for managing resources, processing requests, and supporting PaaS system maintenance. 

For high availability, the platform is running on **two infrastructure nodes**. With a help of synchronization each server is running as an independent identical copy of the platform infrastructure.

The components of infra node are running in a separate virtual Virtuozzo Containers for Linux on CentOS and are responsible for:

* Provisioning
* Templates configuration and clustering binding
* Environment's lifecycle management
* Applications deployment
* Scalability management
* Handling requests via Shared Resolver
* Logs and statistics
* Billing
* Business analysis tools
* Monitoring and health checking

The platform includes the number of subsystems, which perform the abovelisted operations.


## What's next?

* [What is Platform-as-a-Service](/what-is-paas-and-caas/)
* [PaaS Cluster Overview](/cluster-overview/)
* [Infrastructure Level](/infrastructure-level/)