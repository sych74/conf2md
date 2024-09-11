---
draft: false
title: "GlassFish Clustering"
aliases: ["/glassfish-clustering/", "/glassfish-server-clustering/"]
seoindex: "index, follow"
seotitle: "GlassFish Clustering"
seokeywords: "glassfish, glassfish application server, glassfish cluster, glassfish clustering, gf cluster, glassfish administrative domain, das glassfish, glassfish replication, glassfish session replication, session replication, glassfish scaling"
seodesc: "Here is a tutorial on how to set up and configure GlassFish clustered environment in order to get the highly reliable hosting with replication."
menu: 
    docs:
        title: "GlassFish Clustering"
        url: "/glassfish-clustering/"
        weight: 30
        parent: "glassfish"
        identifier: "glassfish-clustering.md"
---

# GlassFish Clustering in the Cloud
**[GlassFish](/glassfish)** is an open-source enterprise level application server with high reliability and performance, which can run any Java EE project. It provides your application with full clustering capability and has a wide range of additional functions.

With the platform, you can use GlassFish not just as a separate server for hosting your Java applications, but also as a highly-available clustered instance with full replication. Let's see how to easily setup GlassFish cluster within the platform in two different ways:

* [automated installation via JPS](#auto-deploy)
* [manual deployment](#manual-deploy)

## GlassFish Cluster Automatic Deployment via JPS Package
Get your GlassFish cluster up and running in just a few minutes using one-click installation option.
<div data-manifest="https://github.com/jelastic-jps/glassfish/blob/master/manifest.jps" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app" data-hoster-select="1">
</div>  

The process of [app installation via widget](/app-packaging) is simple - just click the **Get It Hosted Now** button, type your email and get the cluster hosted while skipping the steps of manual installation.
  
GlassFish clustered solution, installed with this option, is built on top of [Docker containers](/dockers-overview). Such implementation provides additional reliability by operating each node, predefined cluster architecture (i.e. *Load Balancer*, *Worker Nodes*, *Domain Administration Server*), as an isolated instance. Herewith, [HAProxy](https://hub.docker.com/r/jelastic/haproxy-managed-lb/) Docker image is used as *Load Balancer* and [GlassFish](https://github.com/jelastic-jps/glassfish) template serves as a base for *Worker nodes* and *DAS*.

![JPS GlassFish Cluster on Docker](1.png)

In order to gain a better insight into this package installation and management, refer to the [GlassFish Cluster with Automatic Load Balancing](https://www.virtuozzo.com/company/blog/how-to-configure-glassfish-cluster-with-automatic-load-balancing/) page.

{{%tip%}}**Tip:** 
* if your service is not so much visited yet, you can give a try to a JPS package with a [non-clustered GlassFish](https://github.com/jelastic-jps/glassfish) solution
* take a look at [JPS Collection](https://github.com/jelastic-jps), where other numerous pre-configured solutions are stored for you and can be easily installed to the Platform in one click<a id="manual-deploy"></a>{{%/tip%}}

## GlassFish Cluster Manual Deployment

In case you want to gain the complete control over your GlassFish cluster configuration and deployment, the given below instruction can come in handy. It includes description of the main GF cluster configuration specifics and the way it can be implemented within the platform.

In accordance to the native GlassFish clustering architecture, it uses concept of an **administrative domain**. Such administrative domains consist of **clusters** and **instances**, which are managed using **Domain Administration Server** (DAS).

![glassfish clustering](2.png)

For central repository management you can use the **Admin Console**, interactive GUI which supports all available GlassFish features. **Group Management Service** (GMS) provides information about clusters, and DAS, as it was mentioned above, is responsible for managing Java instances in the administrative domain.

### Sessions Replication in GlassFish: How Does It Work?

![glassfish replication](3.png)

Instances in each cluster are paired up. In the case main instance in the cluster fails, all users on this instance are automatically redirected to the second instance in the cluster. Wherein end-users will not see any changes: the replicated instance has all of the sessions of the failed instance. If occasionally both instances in a cluster fail, users are just switched to another cluster. For such switching the platform uses **NGINX-balancer**. It handles and shares all the requests between clusters and instances based on the load and availability.

Also you are provided with a complete scaling system: with [horizontal](/multi-nodes) and [vertical scaling](/automatic-vertical-scaling) size and number of clusters can be easily changed manually or automatically due to the load increasing or decreasing.

To get your own GlassFish high-available clustered environment in the platform just pick up GlassFish as your application server and increase the number of nodes as it is shown in the picture.

![glassfish hosting](4.png)

Don't forget to enable **High Availability** feature: it will pair up all the nodes to create the cluster(s).

That's all the configurations you need! Just click **Create** button and in a minute you'll get highly reliable environment with the instance replication inside each cluster and the cluster replication inside the environment.

## What's next?
* [Cluster in the Cloud](/cluster-in-cloud/)
* [GlassFish](/glassfish/)
* [GlassFish Auto-Clustering](https://www.virtuozzo.com/company/blog/glassfish-payara-auto-clustering-cloud-hosting/)
* [JDBC Connection Pool](/jdbc-connection-pool/)

<script>
    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.async = true;
        js.src = "//go.jelastic.com/widgets.js";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'jelastic-jssdk'));
</script>
