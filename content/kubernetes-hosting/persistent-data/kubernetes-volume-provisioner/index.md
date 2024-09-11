---
draft: false
title: "Volume Provisioner"
aliases: "/kubernetes-volume-provisioner/"
seoindex: "index, follow"
seotitle: "Kubernetes Volume Provisioner"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s persistent volumes, kubernetes volumes provisioning, kubernetes persistent volumes, k8s nfs storage, k8s volumes provisioning, k8s persistent volume claim"
seodesc: "Learn about persistent volume provisioning in the Kubernetes Cluster. The platform provides an option to create NFS storage, which automates persistent volume management inside the Kubernetes Cluster."
menu: 
    docs:
        title: "Volume Provisioner"
        url: "/kubernetes-volume-provisioner/"
        weight: 10
        parent: "persistent-data"
        identifier: "kubernetes-volume-provisioner.md"
---

# Kubernetes Cluster: Volume Provisioner

**Kubernetes Cluster** implements persistent data with the help of *[Persistent Volumes](https://kubernetes.io/docs/concepts/storage/persistent-volumes/)* (PV) and *[Persistent Volume Claims](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)* (PVC). **PV** is storage provisioned by an administrator, which is similar to Volumes but with lifecycle independent of any individual pod. **PVC** is a request for the PV storage with a specific size and access mode.

The platform allows automatically configure NFS volume provisioner during [installation](/kubernetes-cluster-installation). Such a solution automatically provision a persistent volume each time PVC is created. Thus, there is no need to set up PVs with desired *AccessMode* or *[StorageClass](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class)* manually.

![kubernetes cluster add nfs storage](01-kubernetes-cluster-add-nfs-storage.png)

{{%tip%}}**Tip:** The platform implementation of the NFS volume provisioner for the Kubernetes Cluster package uses a dedicated [Shared Storage Container](/shared-storage-container). You can find it in the environment topology.

![kubernetes cluster volumes provisioning](02-kubernetes-cluster-volumes-provisioning.png)

The ***jelastic-dynamic-volume*** is a default *StorageClass* in Kubernetes Cluster. Herewith, all data is stored in the **/data** directory.{{%/tip%}}

## What's next?
* [K8s Helm Integration](/kubernetes-helm-integration)
* [Shared Storage Container](/shared-storage-container)
* [K8s Persistent Volume Claim](/kubernetes-persistent-volume-claim)
* [K8s Custom Storage](/kubernetes-custom-storage)


