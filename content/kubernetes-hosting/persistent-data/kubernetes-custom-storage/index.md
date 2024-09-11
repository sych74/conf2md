---
draft: false
title: "Custom Storage"
aliases: "/kubernetes-custom-storage/"
seoindex: "index, follow"
seotitle: "Kubernetes Custom Storage"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s cluster storage, kubernetes custom storage, k8s nfs storage, kubernetes cluster custom storage, kubernetes storage backend,  k8s cluster custom storage"
seodesc: "Find out  which storage options are available for the Kubernetes Cluster. Use the automated NFS storage solution or implement a custom storage for your particular needs."
menu: 
    docs:
        title: "Custom Storage"
        url: "/kubernetes-custom-storage/"
        weight: 30
        parent: "persistent-data"
        identifier: "kubernetes-custom-storage.md"
---

# Kubernetes Cluster: Custom Storage

Currently, the only automated option for storage backend is the [volume provisioner](/kubernetes-volume-provisioner) based on the NFS storage. It can be selected via the package installation wizard. We recommend sticking to this option when working with the Kubernetes Cluster.
![kubernetes cluster add nfs storage](01-kubernetes-cluster-add-nfs-storage.png)

{{%tip%}}**Tip:** An additional option for the *Gluster-based storage* will be implemented in the future [package versions](/kubernetes-cluster-versions).
{{%/tip%}}
If the default NFS storage does not suit your needs, it is possible to use any other preferred storage backend for your Kubernetes Cluster. You can contact the platform support to discuss the available options and to help you with the implementation.


## What's next?
* [Shared Storage Container](/shared-storage-container)
* [K8s Volume Provisioner](/kubernetes-volume-provisioner)
* [K8s Persistent Volume Claim](/kubernetes-persistent-volume-claim)
* [Automatic Vertical Scaling](/automatic-vertical-scaling)


