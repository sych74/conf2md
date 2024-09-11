---
draft: false
title: "Persistent Volume Claim"
aliases: "/kubernetes-persistent-volume-claim/"
seoindex: "index, follow"
seotitle: "Kubernetes Persistent Volume Claim"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, kubernetes persistent volumes claim, k8s cluster persistent volume claim, persistent volume claim, persistent volume, kubernetes cluster volumes"
seodesc: "Find out about the specifics of working with the persistent volume claims in the Kubernetes Cluster. The platform automatically provisions persistent volume for the default StorageClass."
menu: 
    docs:
        title: "Persistent Volume Claim"
        url: "/kubernetes-persistent-volume-claim/"
        weight: 20
        parent: "persistent-data"
        identifier: "kubernetes-persistent-volume-claim.md"
---

# Kubernetes Cluster: Persistent Volume Claim

Anytime your application pod needs access to the *Persistent Volume* (PV), a dedicated *[PersistentVolumeClaim](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#persistentvolumeclaims)* (PVC) with a specific amount of storage and particular access mode is requested. The platform does not restrict PVCs in any way (including [creation](https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/#create-a-persistentvolumeclaim)). However, there are a few things that you should take into consideration when working with the persistent volume claims:

* if you specify a *StorageClass* other than the default ***[jelastic-dynamic-volume](/kubernetes-volume-provisioner)*** one, PV should be created in advance
* when several pods should use the same PV, ensure that it supports *ROX* or *RWX* [AccessMode](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#access-modes)


## What's next?
* [Shared Storage Container](/shared-storage-container)
* [K8s Volume Provisioner](/kubernetes-volume-provisioner)
* [K8s Custom Storage](/kubernetes-custom-storage)


