---
draft: false
title: "Exposing Services"
aliases: "/kubernetes-exposing-services/"
seoindex: "index, follow"
seotitle: "Kubernetes Exposing Services"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, expose services, expose kubernetes services, exposing k8s services, nodeport k8s service, endpoint for kubernetes service, kubernetes nodeport"
seodesc: "Find out how to expose Kubernetes services for external access in the platform. Configure the NodePort service type on the Kubernetes side and create an appropriate endpoint on the platform side."
menu: 
    docs:
        title: "Exposing Services"
        url: "/kubernetes-exposing-services/"
        weight: 40
        parent: "application-deployment"
        identifier: "kubernetes-exposing-services.md"
---

# Kubernetes Cluster: Exposing Services

While components of your application can communicate with each other by [service names](/kubernetes-internal-networking/) using the internal network, external connections require additional configurations.

Kubernetes supports three service types to establish an internal and external connections to application:

- [ClusterIP](#clusterip)
- [NodePort](#nodeport)
- [LoadBalancer](#loadbalancer)


## ClusterIP

The ***ClusterIP*** service is the default K8s service. It makes application accessible by other applications within K8s cluster. No external access provided.

Simple *ClusterIP* service example:

```
kind: Service
apiVersion: v1
metadata:
  name: nginx1
  namespace: test
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
    - port: 80
```


## NodePort

The most basic way to establish an external connection to a service is to expose it via ***[NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#nodeport)*** directly. As the name implies, this type of service opens a specific port on the nodes, any traffic sent to this port is forwarded to your service. By default, the *nodePort* for your service is selected randomly from the *30000-32767* range.

{{%note%}}**Note:** This method has several downsides that should be considered when configuring the Kubernetes Cluster (one service per port, restricted range of ports, etc.). As a result, the *NodePort* service type can be used for the demo or other temporary applications. However, the production solutions usually require more complex configuration with ingresses and LoadBalancer service options. Follow our guide(s) to create verified configurations for your application and put in production:

- *[Ingresses](/kubernetes-creating-ingresses/)*
- *[Using Public IPs in Kubernetes Service](https://www.virtuozzo.com/company/blog/kubernetes-public-ip-address/)*
{{%/note%}}

Here is an example of the *NodePort* type service configuration:

```
kind: Service
apiVersion: v1
metadata:
  name: nginx1
  namespace: test
  labels:
    run: nginx
spec:
  type: NodePort
  selector:
    run: nginx
  ports:
    - port: 80
      targetPort: 80
```

If needed, a particular *nodePort* can be selected for your service. For example, the following code can be used to configure a redirect from the *30984* port:

```
  ports:
    - port: 80
      targetPort: 80
      nodePort: 30984
```
      
{{%note%}}**Note:** Manually provided *nodePort* value should be from the allowed range (*30000-32767*) and unique (to prevent collision with other services).{{%/note%}}

In case [public IP](/public-ip/) is attached to the Kubernetes worker nodes, no additional actions are required.

Otherwise, the obtained port should be exposed from the platform side. Navigate to the Kubernetes environment **Settings > Endpoints** and click **Add**. In the opened frame, provide the following data:

* ***Node*** - choose any worker node from the list
* ***Name*** - set any preferred endpoint name
* ***Private Port*** - provide the *nodePort* from the previous step
* ***Protocol*** - select the *TCP* option

![endpoint to expose kubernetes service](01-endpoint-to-expose-kubernetes-service.png)

Click **Add** to confirm. It may take up to a few minutes for the platform to expose a port and redirect requests to the *NodePort* service.


## LoadBalancer

The service ***[LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer)*** type is the commonly used way to provide a service on the Internet. It requires the public IP attached to any worker node. 

Keep in mind that with *LoadBalancer* type all traffic is directly forwarded to the service with no filtering, routing, etc. The **port** parameter is an incoming *port* on the Internet which the service  maps to a targetPort on the application side.

For example:

```
kind: Service
apiVersion: v1
metadata:
  name: nginx1
  namespace: test
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 8080
```


## What's next?

* [K8s Helm Integration](/kubernetes-helm-integration/)
* [K8s YAML Deployments](/kubernetes-yaml-deployments/)
* [K8s Internal Networking](/kubernetes-internal-networking/)
* [K8s Creating Ingresses](/kubernetes-creating-ingresses/)