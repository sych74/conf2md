---
draft: false
title: "Internal Networking"
aliases: "/kubernetes-internal-networking/"
seoindex: "index, follow"
seotitle: "Kubernetes Internal Networking"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, kubernetes internal networking, k8s internal access, kubernetes services internal access, kubernetes cluster networking, k8s internal services access"
seodesc: "Kubernetes Cluster automatically manages internal networking, allowing to access Kubernetes services directly by their names without any additional actions required. "
menu: 
    docs:
        title: "Internal Networking"
        url: "/kubernetes-internal-networking/"
        weight: 30
        parent: "application-deployment"
        identifier: "kubernetes-internal-networking.md"
---

# Kubernetes Cluster: Internal Networking

Internal networking configuration within the **Kubernetes Cluster** is an entirely automated process, which is based on the [K8s Services](https://kubernetes.io/docs/concepts/services-networking/service/). The CNI plugin creates and configures an overlay network, which allows providing all pods with the IP addresses.

Also, Kubernetes supports direct access to services by their names, so there is no need for any service discovery mechanism. For example, your application server can connect to the database using its DNS name, which will be resolved as a required internal IP. Herewith, you only need to create a [service](https://kubernetes.io/docs/concepts/services-networking/service/) object with the correct selector.

The **Kubernetes Cluster** is provided with the *Hello World* deployment, service, and [ingress](/kubernetes-creating-ingresses) by default (unless custom deployment option was selected during the [installation](/kubernetes-cluster-installation)). You can examine this default application to understand the concept of the Kubernetes service better.


### Platform DNS Name Resolution inside PODs

Kubernetes cluster uses *CoreDNS* to resolve internal Kubernetes DNS names. It is automatically defined in the ***/etc/resolv.conf*** file of each pod. Also, CoreDNS utilizes the platform nameservers, which allows establishing direct access between the K8s Cluster and other containers inside the platform.

*<u>For example,</u>* if you have an environment with a database in the platform and want to connect to it from your Kubernetes pod, you need to use the "***${nodeId}-${envName}.${platformDomain}***" hostname and default port for your database (*3306* for MySQL, *5432* for Postgres, etc.).

However, you need to create an [endpoint](/endpoints) to connect to such a database from outside of the platform.


## What's next?
* [K8s Helm Integration](/kubernetes-helm-integration)
* [K8s YAML Deployments](/kubernetes-yaml-deployments)
* [K8s Exposing Services](/kubernetes-exposing-services)
* [K8s Creating Ingresses](/kubernetes-creating-ingresses)


