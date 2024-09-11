---
draft: false
title: "Access Control"
aliases: "/kubernetes-access-control/"
seoindex: "index, follow"
seotitle: "Kubernetes Access Control"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s access control, kubernetes cluster access control, share kubernetes access, role-based access control, k8s manage access"
seodesc: "Find out how to manage access in your Kubernetes Cluster and how to share access to the particular actions only."
menu:
    docs:
        title: "Access Control"
        url: "/kubernetes-access-control/"
        weight: 20
        parent: "managing-kubernetes"
        identifier: "kubernetes-access-control.md"
---

# Kubernetes Cluster: Access Control

Kubernetes manages access to the cluster via [RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) (Role-Based Access Control). By default, you have a token that belongs to a **[ServiceAccount](https://kubernetes.io/docs/reference/access-authn-authz/service-accounts-admin/)** with the *cluster-admin* role.

If you need to share access to the Kubernetes cluster with other users, it is recommended to create separate **ServiceAccounts** with the required [Roles and RoleBindings](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings). Such a flow helps to manage allowed actions manually (e.g. to *create namespaces*, *deployments*, *services*, *ingresses*, etc.).

{{%note%}}**Notes:**

- Kubernetes RBAC system is not aligned with PaaS accounts. Any user with SSH access to the master node can utilize the pre-configured *kubectl* tool with its *cluster-admin* role. Due to this specific, [environment sharing](/share-environment) over the platform functionality may expose sensitive information.
- The [platform firewall](/custom-firewall/) feature does not work with the Kubernetes Cluster, as the rules are managed dynamically by Kubernetes itself.
{{%/note%}}

## What's next?

* [K8s Cluster Access](/kubernetes-cluster-access)
* [K8s Cluster Troubleshooting](/kubernetes-troubleshooting)
* [K8s Cluster Upgrade](/kubernetes-upgrade)


