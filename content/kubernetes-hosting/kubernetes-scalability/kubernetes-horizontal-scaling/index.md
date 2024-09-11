---
draft: false
title: "Horizontal Scaling"
aliases: "/kubernetes-horizontal-scaling/"
seoindex: "index, follow"
seotitle: "Kubernetes Horizontal Scaling"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s horizontal scaling, kubernetes horizontal scaling, k8s automatic horizontal scaling, kubernetes cluster horizontal scaling, k8s horizontal pod autoscaler"
seodesc: "Find out about the horizontal scaling specifics of the Kubernetes Cluster, and the automatic scaling benefits the platform provides."
menu: 
    docs:
        title: "Horizontal Scaling"
        url: "/kubernetes-horizontal-scaling/"
        weight: 20
        parent: "kubernetes-scalability"
        identifier: "kubernetes-horizontal-scaling.md"
---

# Kubernetes Cluster: Horizontal Scaling

Horizontal scaling for the **Kubernetes Cluster** is represented via two implementations:

* *platform-managed [horizontal scaling](/horizontal-scaling)* - allows adding/removing Kubernetes nodes. Based on your needs, you can configure [scaling triggers](/automatic-horizontal-scaling#configure-triggers) to automate this process based on resource utilization.
* *Kubernetes-managed [Horizontal Pod Autoscaler](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)* - scales deployments up/down based on observed CPU utilization

With both of these horizontal scaling methods, Kubernetes Cluster always has nodes available (when needed) and healthy application pods.
{{%tip%}}**Tip:** An extended real case example (WordPress) on the ***[Kubernetes Cluster Scaling](https://www.virtuozzo.com/company/blog/scaling-kubernetes/)*** is provided within the linked article.{{%/tip%}}

## What's next?
* [Kubernetes Cluster Scaling](https://www.virtuozzo.com/company/blog/scaling-kubernetes/)
* [Horizontal Scaling](/horizontal-scaling)
* [Automatic Horizontal Scaling](/automatic-horizontal-scaling)
* [K8s Vertical Scaling](/kubernetes-vertical-scaling)
* [K8s Helm Integration](/kubernetes-helm-integration)


