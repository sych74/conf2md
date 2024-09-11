---
draft: false
title: "Cluster Upgrade"
aliases: "/kubernetes-upgrade/"
seoindex: "index, follow"
seotitle: "Kubernetes Upgrade"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s cluster upgrade, update kubernetes cluster, kubernetes cluster upgrade package, add-on for k8s upgrade, update k8s cluster add-on"
seodesc: "Find out how you can upgrade your Kubernetes Cluster to the latest version of the package. Use the pre-installed add-on to perform required changes."
menu: 
    docs:
        title: "Cluster Upgrade"
        url: "/kubernetes-upgrade/"
        weight: 40
        parent: "managing-kubernetes"
        identifier: "kubernetes-upgrade.md"
---

# Kubernetes Cluster: Upgrade Package

The platform actively develops the **Kubernetes Cluster** solution and regularly releases new [versions of the package](/kubernetes-cluster-versions). Herewith, you don't need to recreate the whole cluster from scratch to benefit on the new features and tools - the existing environment can be upgraded with a dedicated add-on.

Hover over the *Master* layer and click the appeared **Add-Ons** button. Then, in the opened section, select the **Upgrade** option for the ***Kubernetes Cluster Configuration*** add-on panel.

![kubernetes cluster upgrade add-on](01--kubernetes-cluster-upgrade-add-on.png)

Confirm an action via a pop-up, and the platform will perform an automatic update to the next version of the **Kubernetes Cluster**. If the latest version is already installed, the appropriate notification will appear on the dashboard.

![kubernetes cluster latest version update](02-kubernetes-cluster-latest-version-update.png)

{{%tip%}}**Tip:** Check the *[Kubernetes Versions](/kubernetes-cluster-versions)* documentation page to check the list of the currently available releases and their changelogs.{{%/tip%}}

## What's next?
* [K8s Cluster Access](/kubernetes-cluster-access)
* [K8s Access Control](/kubernetes-access-control)
* [K8s Cluster Troubleshooting](/kubernetes-troubleshooting)
* [Kubernetes Cluster Scaling](https://www.virtuozzo.com/company/blog/scaling-kubernetes/)


