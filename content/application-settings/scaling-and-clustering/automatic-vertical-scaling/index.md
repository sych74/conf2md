---
draft: false
title: "Automatic Vertical Scaling"
aliases: ["/automatic-vertical-scaling/", "/scaling-migration/"]
seoindex: "index, follow"
seotitle: "Automatic Vertical Scaling"
seokeywords: "scaling, vertical scaling, application autoscaling, application scaling, application vertical scaling, resources scaling, automatic vertical scaling, load-based scaling, scaling limit, dynamic resource allocation, ram cpu allocation"
seodesc: "Find out about the automatic vertical scaling feature by the platform, which dynamically provide the required amount of resources (RAM and CPU) based on your server current load with no manual intervention required."
menu:
    docs:
        title: "Automatic Vertical Scaling"
        url: "/automatic-vertical-scaling/"
        weight: 10
        parent: "scaling-and-clustering"
        identifier: "automatic-vertical-scaling.md"
---

# Automatic Vertical Scaling

The platform is the only Cloud PaaS which can automatically **scale any application**, both vertically and [horizontally](/automatic-horizontal-scaling/), making hosting of your applications truly flexible.

**Automatic vertical scaling** is made possible by the platform's ability to dynamically change the amount of allocated to server resources (RAM and CPU) according to its current demands, with no manual intervention required. This feature guarantees you never overpay for unused resources and saves your time due to eliminating the necessity of handling the load-related adjustments or architectural changes.


![Pay-per-Use pricing](01-pay-per-use-pricing.png)

You simply decide the maximum limit you are ready to consume and the platform automatically defines the optimal amount of resources required for your app, tracking the incoming load in real time.

<iframe width="1665" height="695" src="https://www.youtube.com/embed/tRY2mDjZFT4" title="How to save money on cloud hosted apps with the Virtuozzo Application Platform" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


## How It Works

So, the key idea of automatic scaling is fairly simple - as soon as an application's load grows, the platform simply makes additional resources available to it; and when the load goes down again, the resources get reduced by the platform automatically.

Herewith, the resources are allocated immediately without delays or negative impact on your application, which can be seen within the next video:

<iframe width="1665" height="695" src="https://www.youtube.com/embed/1d9BRcls5wQ" title="Automatic Scaling and Pay-per-User Pricing - Virtuozzo Application Platform" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

{{%tip%}}**Tip:** The vertical scaling feature is applicable for any type of instance in environment (i.e. application server, database, load balancer, Docker container, Elastic VPS, cache instance and build node).{{%/tip%}}

As you could observe within the video above, the platform measures resources in special units called **cloudlets**, which provide you with a superior granularity while scaling. A [cloudlet](/cloudlet/) is roughly equivalent to 128 MiB RAM and 400Mhz CPU core.

![cloudlet resources](02-cloudlet-resources.png)

There are two types of cloudlets available: **reserved** and **dynamic**.

* The **Reserved** ones are used to define the amount of resources you expect your application will certainly consume and you pay for them irrespective of actual usage. However, they are charged with lower price compared with dynamic ones.
* **Dynamic** cloudlets defines the amount of resources your application can access, based on necessity. You pay for them only in the case of real consumption.

Automatic vertical scaling is performed within the confines of the stated dynamic cloudlets number. You are able to choose your scalability limits with the appropriate settings and, in such a way, effectively put caps on the budget you are ready to spend, preventing unexpected or high bills.

![automatic vertical scaling](03-automatic-vertical-scaling.png)

You can combine the usage of both cloudlet types in different ways, following the most suitable for you [pricing model](/pricing-model/).


## Adjusting Resource Limits

A newly created environment receives a certain amount of cloudlets. Resource consumption depends on the type and quantity of your software stacks. Upon being added to the environment, each stack receives the default number of allocated cloudlets according to the optimal resource amount, required for its proper workability.

{{%accordion title="Click to see default cloudlet values for some popular stacks."%}}

|Node Name|Reserved|Scaling Limit|
|---|:---:|:---:|
|Tomcat, Jetty|1|6|
|TomEE|1|8|
|GlassFish|6|16|
|Apache, NGINX|1|4|
|NGINX-Balancer|1|4|
|Nginx-Ruby|1|6|
|Apache-Ruby|1|8|
|Apache-Python|1|8|
|NodeJS|4|8|

|Node Name|Reserved|Scaling Limit|
|---|:---:|:---:|
|MySQL, MariaDB|1|6|
|PostgreSQL|1|6|
|MongoDB|1|8|
|CouchDB|1|4|

|Node Name|Reserved|Scaling Limit|
|---|:---:|:---:|
|Memcached|1|4|
|VPS|1|16|
|Maven|1|16||

{{%/accordion%}}

If you would like to change these values and scale your environment, the maximum number of available resources (cloudlets) can be increased/decreased manually through the **Environment topology** wizard. For that, use the cloudlet sliders in the *Vertical Scaling* section of its central pane.

![environment wizard](04-environment-wizard.png)

{{%tip%}}**Note:** If changing the scaling limit (i.e. the number of the dynamic cloudlets) for the existing *application server*, *database* or *cache* nodes, the corresponding layer will be restarted. Herewith, the appropriate warning will be displayed directly in the topology wizard:

![adjust cloudlets restart warning](05-adjust-cloudlets-restart-warning.png)
{{%/tip%}}

You can use the automatically gathered [statistics](/view-app-statistics/) to check the consumption level for the last month and set the amount of resources according to it. And in the case your application becomes highly popular and a single server's capacity is not enough, feel free to scale it horizontally by means of increasing the number of nodes [manually](/horizontal-scaling/) or configure a set of [triggers for automatic horizontal scaling](/automatic-horizontal-scaling/) of your application server.


## What's next?

* [Automatic Horizontal Scaling](/automatic-horizontal-scaling/)
* [Horizontal Scaling](/horizontal-scaling/)
* [Isolated Containers](/isolated-containers/)