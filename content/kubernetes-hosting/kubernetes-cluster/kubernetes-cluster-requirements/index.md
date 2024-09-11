---
draft: false
title: "System Requirements"
aliases: "/kubernetes-cluster-requirements/"
seoindex: "index, follow"
seotitle: "Kubernetes Requirements"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s system requirements, kubernetes system requirements, k8s minimum requirements, kubernetes development cluster, kubernetes production cluster"
seodesc: "Find out about available topology options for the Kubernetes Cluster package and the minimum requirements for each one."
menu: 
    docs:
        title: "System Requirements"
        url: "/kubernetes-cluster-requirements/"
        weight: 20
        parent: "kubernetes-cluster"
        identifier: "kubernetes-cluster-requirements.md"
---

# Kubernetes Cluster: System Requirements

**Kubernetes Cluster** package may not be available in some [regions](/environment-regions) due to the hardware specifics of the particular platform. In such a case, please contact your hosting provider support.

The minimum and optimal consumption of RAM, CPU, and storage depends on the cluster size, installed components, active workload, etc.

**Resources<sup>[1]</sup>**|**Development Cluster<sup>[2]</sup>**|**Production Cluster<sup>[3]</sup>**
---|---|---
*Cloudlets*|14|33
*RAM & CPU*|1.4 GiB RAM, 419 MHz CPU|3.6 GiB RAM, 947 MHz CPU
*Storage<sup>[4]</sup>*|5.65 GB|15.01 GB

{{%tip%}}**Note:** 
* ***[1]*** Measurements were performed on the bare *development* and *production* clusters without any additional load. Thus, the specified values are minimum system requirements, which can be much higher for the loaded clusters (especially production one).
* ***[2]*** *Development cluster* topology - one master, one worker, one storage node, no monitoring tools, sample *Hello World* deployment.
* ***[3]*** *Production cluster* topology - API balancer, three masters, two workers, one storage node, monitoring tools, sample *Hello World* deployment
* ***[4]*** Fast disks are critical for *etcd* (key-value storage used by K8s) performance, while slow *etcd* may lead to cluster instability due to failed workloads. Useful links: [Disk Requirements](https://etcd.io/docs/v3.5/op-guide/hardware/#disks), [Benchmark Information](https://etcd.io/docs/v3.5/op-guide/performance/#benchmarks), [How to Run Benchmark](https://github.com/etcd-io/etcd/tree/master/tools/benchmark), and [Download Benchmark](https://app-artifacts.s3.eu-central-1.amazonaws.com/kubernetes/tools/etcd-benchmark-3.5.tar.gz).
{{%/tip%}}

Herewith, the *development cluster* is recommended only as a **sandbox environment**. For **production purposes**, a highly available topology with multi-masters is the preferred option. Next, based on the expected load, the required number of workers can be added manually, or the appropriate [automatic horizontal scaling](/automatic-horizontal-scaling) can be configured. Adding more master nodes makes sense only if there is a significant number of requests coming from clients (*kubectl*, *dashboard*, *continuous integration* job, *K8s-native* applications, etc.).


## What's next?

* [Kubernetes Overview](/kubernetes-cluster/)
* [K8s Cluster Installation](/kubernetes-cluster-installation/)
* [K8s Cluster Versions](/kubernetes-cluster-versions/)
* [K8s Cluster Access](/kubernetes-cluster-access/)