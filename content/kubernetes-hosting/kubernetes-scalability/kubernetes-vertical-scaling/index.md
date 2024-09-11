---
draft: false
title: "Vertical Scaling"
aliases: "/kubernetes-vertical-scaling/"
seoindex: "index, follow"
seotitle: "Kubernetes Vertical Scaling"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s vertical scaling, kubernetes vertical scaling, k8s automatic vertical scaling, kubernetes cluster vertical scaling, k8s vertical pod autoscaler"
seodesc: "Learn about the vertical scaling specifics of the Kubernetes Cluster, and the automatic scaling benefits the platform provides."
menu: 
    docs:
        title: "Vertical Scaling"
        url: "/kubernetes-vertical-scaling/"
        weight: 10
        parent: "kubernetes-scalability"
        identifier: "kubernetes-vertical-scaling.md"
---

# Kubernetes Cluster: Vertical Scaling

Vertical scaling for the **Kubernetes Cluster** is represented via two implementations:

* *platform-managed [automatic vertical scaling](/automatic-vertical-scaling)* - allows dynamically allocating resources for the Kubernetes nodes, which are used (and charged) only when they are needed
* *Kubernetes-managed [Vertical Pod Autoscaler](https://cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) (beta)* - adjusts pod memory/CPU requests and limits on the go

The combination of PaaS vertical scaling and VPA can help minimize resource utilization and thus reduce cluster maintenance costs. In addition, it makes deployments highly available and fault-tolerant.
{{%tip%}}**Tip:** An extended real case example (WordPress) on the ***[Kubernetes Cluster Scaling](https://www.virtuozzo.com/company/blog/scaling-kubernetes/)*** is provided within the linked article.{{%/tip%}}

## What's next?
* [Kubernetes Cluster Scaling](https://www.virtuozzo.com/company/blog/scaling-kubernetes/)
* [Automatic Vertical Scaling](/automatic-vertical-scaling)
* [K8s Horizontal Scaling](/kubernetes-horizontal-scaling)
* [K8s Cluster Access](/kubernetes-cluster-access)


