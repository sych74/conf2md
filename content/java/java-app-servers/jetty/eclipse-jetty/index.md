---
draft: false
title: "Jetty Server"
aliases: ["/eclipse-jetty/", "/jetty/", "/jetty-overview/"]
seoindex: "index, follow"
seotitle: "Eclipse Jetty"
seokeywords: "jetty, eclipse jetty, jetty java, jetty creation, jetty server, java application server, java hosting, create jetty, jetty java server, install jetty java, eclipse jetty server, jetty application server, java jetty server, java jetty installation"
seodesc: "Find out how to get a ready-to-go Eclipse Jetty application server for Java hosting in the cloud. Create a new environment with Jetty open source Java Servlet Container, which supports asynchronous server and client implementations of the HTTP, Websocket and SPDY protocols."
menu:
    docs:
        title: "Jetty Server"
        url: "/eclipse-jetty/"
        weight: 1
        parent: "jetty"
        identifier: "eclipse-jetty.md"
---

# Eclipse Jetty

**[Eclipse Jetty](https://www.eclipse.org/jetty/)** is an open source Java-based HTTP (web) server, which provides the latest Java Servlet API, HTTP/2 protocol, WebSocket support and more. Jetty is widely used within various projects and products (both in development and production) due to the following features:

* *open source and commercially usable*
* *flexible and extensible*
* *asynchronous*
* *small footprint*
* *enterprise scalable*

{{%tip%}}**Note:** This template utilizes a modern ***systemd*** initialization daemon.{{%/tip%}}

To get an Eclipse Jetty application server at the platform, you need to:

1\. Access your PaaS account and click **New Environment** button at the top.

![new environment button](01-new-environment-button.png)

2\. Within the opened topology wizard, switch to the ***Java*** tab and pick **Jetty** as your application servers:

![topology wizard Eclipse Jetty server](02-topology-wizard-eclipse-jetty-server-.png)

Adjust other settings up to your needs (e.g. [vertical](/automatic-vertical-scaling/) and [horizontal](/horizontal-scaling/) scaling or [public IPs](/public-ip/)) and click **Create**.

3\. Once the environment is created, you can click the **Open in Browser** button next to it.

![Jetty server open in browser button](03-jetty-server-open-in-browser-button.png)

A Jetty server home page will be opened in a new browser page:

![Jetty application server home page](04-jetty-application-server-home-page.png)

As you can see the Eclipse Jetty server is up and running, so you can proceed to the [application deployment](/deployment-guide/).


## What's next?

* [Jetty Environment Variables](/jetty-variables/)
* [Jetty Security](/jetty-security/)
* [Java App Server Configuration](/java-application-server-config/)
* [Deployment Guide](/deployment-guide/)