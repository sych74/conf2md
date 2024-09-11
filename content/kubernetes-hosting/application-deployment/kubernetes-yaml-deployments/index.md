---
draft: false
title: "YAML Deployments"
aliases: "/kubernetes-yaml-deployments/"
seoindex: "index, follow"
seotitle: "Kubernetes YAML Deployments"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, kubernetes yaml deployment, k8s yaml json deployment, deploy k8s application, deploy application with yaml, kubernetes dashboard deploy application, kubectl deploy yaml application"
seodesc: "Find out about Kubernetes deployments with YAML (JSON). Use the .yaml or .yml files to declare the list of intended actions for an application deployment at Kubernetes Cluster and apply this YAML file."
menu: 
    docs:
        title: "YAML Deployments"
        url: "/kubernetes-yaml-deployments/"
        weight: 20
        parent: "application-deployment"
        identifier: "kubernetes-yaml-deployments.md"
---

# Kubernetes Cluster: YAML Deployments

Kubernetes natively supports deployments from both JSON and YAML files. However, among the community, YAML is a more frequent option and can be considered a standard.

Deployment from YAMLs is somewhat similar to the [Helm](/kubernetes-helm-integration) charts - the ***.yaml*** or ***.yml*** file provides object definition or a list of objects. Herewith, it can be directly applied in *Kubernetes Dashboard* or with the *kubectl* command-line tool without any additional software installation.

![kubernetes dashboard deploy application with yaml](01-kubernetes-dashboard-deploy-application-with-yaml.png)

When working over *kubectl*, use the ***[apply](https://kubernetes.io/docs/reference/kubectl/cheatsheet/#apply)*** command with the correct path to your deployment YAML file:

```bash
kubectl apply -f /path/to/deployment.yaml
```
On the other hand, the benefit of the [Helm](/kubernetes-helm-integration) charts is advanced flexibility (support of the conditions, replacements, parameters, etc.).


## What's next?
* [K8s Helm Integration](/kubernetes-helm-integration)
* [K8s Internal Networking](/kubernetes-internal-networking)
* [K8s Exposing Services](/kubernetes-exposing-services)
* [K8s Creating Ingresses](/kubernetes-creating-ingresses)


