---
draft: false
title: "Kubernetes Overview"
aliases: "/kubernetes-cluster/"
seoindex: "index, follow"
seotitle: "Kubernetes Overview"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s overview, kubernetes cluster overview, kubernetes benefits, k8s cluster benefits, k8s components, kubernetes cluster components"
seodesc: "Learn about Kubernetes hosting at the platform and the benefits of the pre-packaged Kubernetes Cluster implementation."
menu: 
    docs:
        title: "Kubernetes Overview"
        url: "/kubernetes-cluster/"
        weight: 10
        parent: "kubernetes-cluster"
        identifier: "kubernetes-cluster.md"
---

# Kubernetes Cluster Overview

**[Kubernetes (K8s)](https://kubernetes.io/)** is an open-source system designed to automate deployment, scaling, and management of microservices and containerized applications. A [pod](https://kubernetes.io/docs/concepts/workloads/pods/pod/), which is the central piece in the K8s model, is a set of Linux containers with shared network and storage. [Network plugins](https://kubernetes.io/docs/concepts/extend-kubernetes/compute-storage-net/network-plugins/) and [ingress controllers](https://kubernetes.io/docs/concepts/services-networking/ingress-controllers/) support internal and external load balancers, while [pluggable storage backends](https://kubernetes.io/docs/concepts/storage/storage-classes/#provisioner) automate data persistence. [Kubernetes kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/) orchestrates pods ensuring the cluster is always in a desired healthy state.

Installation of a Kubernetes Cluster, as well as network and storage configuration, is a tedious and error-prone process. The platform automates Kubernetes installation, configuration, updates, and supplies multiple additional Kubernetes services and cluster components:

* ***[Weave CNI](https://kubernetes.io/docs/concepts/cluster-administration/networking/#weave-net-from-weaveworks)*** plugin to enable internal networking
* ***[CoreDNS](https://coredns.io/)*** as internal DNS
* ***[Traefik](https://docs.traefik.io/user-guides/crd-acme/)*** ingress controller with pre-configured TLS for external access to services (with the *NGINX* and *HAProxy* options available since *1.15.5*)
* ***[NFS storage provisioner](https://docs.docker.com/ee/ucp/kubernetes/storage/use-nfs-volumes/)*** for automatic creation of [K8s volumes](https://kubernetes.io/docs/concepts/storage/volumes/) *(optional)*
* ***[Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)*** to manage and control the cluster via a modern and intuitive web client
* ***[Helm and Tiller](https://helm.sh/)*** for one-click deployment of hundreds of popular applications
* ***[K9s](https://github.com/derailed/k9s)***, ***[kubectx](https://github.com/ahmetb/kubectx)***, ***[popeye](https://github.com/derailed/popeye)***, and ***[stern](https://github.com/wercker/stern)*** command-line utilities to efficiently manage your cluster
* ***[Metrics server](https://github.com/kubernetes-incubator/metrics-server)***, ***[Prometheus](https://prometheus.io/)***, and ***[Grafana](https://grafana.com/)*** for monitoring your cluster and applications health *(optional)*
* ***[Jaeger](https://www.jaegertracing.io/)*** for monitoring and troubleshooting of the microservice-based distributed systems (*optional*, available since *1.15.5*)

Besides K8s specific features, traditional platform features are available too, e.g. [vertical](/kubernetes-vertical-scaling) and [horizontal scaling](/kubernetes-horizontal-scaling).

{{%tip%}}**Tip:** For more information, view the ***[Kubernetes Cluster Overview](https://www.virtuozzo.com/company/blog/kubernetes-cluster-scaling-pay-per-use-hosting/)*** article on our blog.{{%/tip%}}


## What's next?

* [Container Types](/container-types/)
* [K8s System Requirements](/kubernetes-cluster-requirements/)
* [K8s Cluster Installation](/kubernetes-cluster-installation/)
* [K8s Cluster Versions](/kubernetes-cluster-versions/)