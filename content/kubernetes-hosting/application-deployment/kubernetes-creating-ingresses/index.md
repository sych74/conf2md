---
draft: false
title: "Creating Ingresses"
aliases: "/kubernetes-creating-ingresses/"
seoindex: "index, follow"
seotitle: "Kubernetes Creating Ingresses"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, k8s creating ingress, kubernetes cluster ingresses, k8s cluster ingress controller, traefik ingress controller, haproxy ingress controller, nginx ingress controller"
seodesc: "Ingresses in the Kubernetes Cluster configures external access to the services and provides numerous features out-of-the-box (SSL, auth, routing, etc.)."
menu: 
    docs:
        title: "Creating Ingresses"
        url: "/kubernetes-creating-ingresses/"
        weight: 50
        parent: "application-deployment"
        identifier: "kubernetes-creating-ingresses.md"
---

# Kubernetes Cluster: Creating Ingresses

**[Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/)** is a Kubernetes Cluster load balancer that manages external access to the services, provides SSL termination and name-based virtual hosting. It is managed via a set of rules (*spec*) that are matched against all incoming requests.
{{%tip%}}**Tip:** Compared to the service expose via *[NodePort](/kubernetes-exposing-services)*, ingress is a more powerful but also more complicated option. It is most useful when you need to expose multiple services under the same IP address. Additionally, ingresses are managed by a controller, which provides numerous features out-of-the-box (SSL, auth, routing, etc.).
{{%/tip%}}
Ingresses in **Kubernetes Cluster** are managed by [Traefik](https://docs.traefik.io/v1.7/user-guide/kubernetes/) ingress controller by default, with the [HAProxy](https://github.com/jcmoraisjr/haproxy-ingress) and [NGINX](https://github.com/kubernetes/ingress-nginx) options available in the upcoming 1.15.5 [package version](/kubernetes-cluster-versions). It watches objects, parses specs/annotations, and translates them into redirect rules.

{{%tip%}}**Note:** 
It is not possible to change the selected ingress controller via the Kubernetes management add-on or some other automation tool after the installation. The operation can still be performed manually, feel free to contact support if you need assistance.
{{%/tip%}}

An ingress spec is a combination of a path rule, a backend service, and a port. For example, your ingress may look as follows:

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  labels:
    app: myapp
  name: myapp
  annotations:
    kubernetes.io/ingress.class: traefik
    ingress.kubernetes.io/secure-backends: "true"
    traefik.frontend.rule.type: PathPrefixStrip
spec:
  rules:
  - http:
      paths:
      - path: /myapp
        backend:
          serviceName: myapp
          servicePort: 8080
```
This example exposes the *myapp* service, which is bound to the *8080* port on a path of your Kubernetes environment default domain with the */myapp* suffix (i.e. *https://${envName}.${platformDomain.com}/myapp*). For additional information on the ingress rules configuration (including path- and subdomain-based routing), refer to the [official documentation](https://kubernetes.io/docs/concepts/services-networking/ingress/#ingress-rules).


## What's next?
* [K8s Helm Integration](/kubernetes-helm-integration)
* [K8s YAML Deployments](/kubernetes-yaml-deployments)
* [K8s Internal Networking](/kubernetes-internal-networking)
* [K8s Exposing Services](/kubernetes-exposing-services)
* [K8s Volume Provisioner](/kubernetes-volume-provisioner)


