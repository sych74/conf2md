---
draft: false
title: "Cluster Troubleshooting"
aliases: "/kubernetes-troubleshooting/"
seoindex: "index, follow"
seotitle: "Kubernetes Troubleshooting"
seokeywords: "k8s, kubernetes, k8s cluster, kubernetes cluster, kubernetes logs, kubernetes troubleshooting, k8s cluster troubleshooting, kubernetes event tracking, k8s pod logs, kubernetes log analysis"
seodesc: "Learn how you can troubleshoot issues during the Kubernetes Cluster installation and while working with the cluster. Use log files and Kubernetes Dashboard web UI to analyze issues."
menu: 
    docs:
        title: "Cluster Troubleshooting"
        url: "/kubernetes-troubleshooting/"
        weight: 30
        parent: "managing-kubernetes"
        identifier: "kubernetes-troubleshooting.md"
---

# Kubernetes Cluster: Troubleshooting

The **Kubernetes Cluster** package is an extremely complicated product, which includes multiple steps required to set up the solution. Herewith, each action can fail due to various reasons, which should be analyzed to prevent problem occurrence in the future. Below, we'll overview the main troubleshooting steps during the different stages and for multiple log files:

* [K8s Installation](#install)
* <a href="#events" id="install">Events Tracking</a>
* [Pod Logs](#pod-logs)

### K8s Installation
Installation of a Kubernetes cluster is a complex but fully automated process, which already includes an error handling mechanism. The platform automatically processes the most common issues and shows their root cause directly in the dashboard. Herewith, for more complex issues, you can **Send Report** to the support team via the appropriate widget.
![kubernetes cluster installation error](01-kubernetes-cluster-installation-error.png)

Such a report includes installation logs, error messages, and all other debug information required.

Also, the package automatically verifies all of the cluster components after installation. The relevant details can be viewed via the ***/var/log/k8s-health-check.log*** file on the master node. A dedicated utility script checks the health of the following components: *Weave CNI Plugin*, *Ingres Controller*, *Metrics Server*, *Kubernetes Dashboard*, *Node Problem Detector*, *Monitoring Tools*, *Remote API*, *NFS Storage*, *Sample App*.

If the health checker fails to verify the *Running* status of a component, the appropriate notification will be displayed in the installation success frame. Herewith, such a warning is not always caused by the cluster malfunction (e.g. deployments can be still in progress). You can run the ***kubectl get pods --all-namespaces*** command to check the pods' state.<a id="events"></a> If all of them are *Running*, your cluster is doing just fine. Otherwise, contact platform support and attach K8s related logs from the **/var/log** directory.


### Events Tracking
You can use *kubectl* or *Kubernetes Dashboard* to track and analyze events for the particular or all namespaces at one (the sufficient permissions are required):


* **Events** in *Kubernetes Dashboard*
![kubernetes dashboard events](02-kubernetes-dashboard-events.png)

* example output from the ***kubectl get events -n $namespace*** command
<a id="pod-logs"></a>![kubectl get events](03--kubectl-get-events.png)

### Pod Logs
After scheduling pod(s) to run on a free node, you can follow the appropriate logs via:

* *Kubernetes Dashboard* - navigate to the ***pod*** page and click the **Logs** button in the top right corner
* *kubectl* - utilize commands for the [pods management](https://kubernetes.io/docs/reference/kubectl/cheatsheet/#interacting-with-running-pods)

For example, these logs can help find the root cause of the &ldquo;*Back-off restart failed container*&rdquo; event for your pods.

## What's next?
* [K8s Cluster Access](/kubernetes-cluster-access)
* [K8s Access Control](/kubernetes-access-control)
* [K8s Cluster Upgrade](/kubernetes-upgrade)


