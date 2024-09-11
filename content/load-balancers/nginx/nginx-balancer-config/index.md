---
draft: false
title: "NGINX Balancer Configuration"
aliases: "/nginx-balancer-config/"
seoindex: "index, follow"
seotitle: "NGINX Balancer Configuration"
seokeywords: "nginx configuration, balancer configuration, configuration files, nginx balancer node, configure balancer, tcpmaps, balancer settings, conf d, load balancing, balancer, nginx conf"
seodesc: "See the list of NGINX balancer node configuration files and folders that are available and the main settings you can setup within them."
menu: 
    docs:
        title: "NGINX Balancer Configuration"
        url: "/nginx-balancer-config/"
        weight: 30
        parent: "nginx"
        identifier: "nginx-balancer-config.md"
---

<a id="back"></a>

# NGINX Balancer Configuration

The following NGINX configuration files are available:

Folder|File|Path
---|---|---
[conf](#conf)|nginx.conf|/etc/nginx
[conf.d](#confd)||/etc/nginx/conf.d
[tcpmaps](#tcpmaps)|mappings.xmlf|/etc/nginx/tcpmaps

NGINX balancer is automatically added if you choose several app servers.


## CONF

For performing necessary configurations for NGINX balancer the ***nginx.conf*** file, located in **conf** folder, is used.

![NGINX balancer configuration file](01-nginx-balancer-configuration-file.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## CONF.D

With access to NGINX configs you can not only edit the existing files but also upload your own config files with custom settings to the **conf.d** folder.

![NGINX balancer custom conf.d settings](02-nginx-balancer-custom-confd-settings.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## TCPMAPS

The **tcpmaps** folder contains the ***mappings.xml*** file where you can set the redirection of the TCP balancing ports. There you need to specify the pair of ports: one to listen to and the other to redirect to.

You can find more information in the [NGINX Load Balancing](/nginx-load-balancer/) and [TCP Load Balancing](/tcp-load-balancing/) documents.

To set [caching in NGINX](/nginx-caching/) click on the link and follow the instruction.

![NGINX balancer TCP mappings](03-nginx-balancer-tcp-mappings.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## What's next?

* [Load Balancing](/load-balancing/)
* [Caching in NGINX](/nginx-caching/)
* [Memcached Configuration](/memcached-configuration/)
* [Custom Error Page Settings via NGINX Balancer](/custom-error-page/)