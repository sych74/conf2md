---
draft: false
title: "Built-In SSL"
aliases: ["/built-in-ssl/", "/jelastic-ssl/"]
seoindex: "index, follow"
seotitle: "Built-In SSL"
seokeywords: "ssl, secure sockets layer, secure sockets layer certificate, ssl certificates, web server ssl certificate, ssl wildcard certificate, wildcard ssl certificate, https connection, data encryption, data encryption"
seodesc: "Learn how to use the platform built-in wildcard SSL certificates to secure your website. Establish a connection with your web server over HTTPS and get the enterprise-level data encryption standard."
menu:
    docs:
        title: "Built-In SSL"
        url: "/built-in-ssl/"
        weight: 20
        parent: "ssl"
        identifier: "built-in-ssl.md"
---

# Built-In SSL Certificates

**Built-in wildcard SSL** by the platform is an excellent solution for those who are searching for a quick and reliable way to secure their website.  
The built-in SSL certificate (can be referred to as ***{hosterName} SSL*** in the dashboard) offers:

* **Convenient Management** - configured and working SSL with a single click in the topology wizard
* **Fast Validation** - domain level verification, including your site check and security seal issuing, is performed in a matter of minutes
* **Enterprise-Level Data Encryption** - the strength provided by built-in SSL certificates makes your customers feel comfortable with their security

So, to get the **built-in SSL certificate**, perform the following simple steps:

1\. Log into your platform dashboard and open the topology wizard through clicking the **New Environment** button at the top-left corner (or by selecting the **Change Environment Topology** icon next to the existing environment).

![PaaS main buttons](01-paas-main-buttons.png)

2\. In the opened topology wizard, [set up your environment](/setting-up-environment) up to your needs, then switch to the **SSL** section at the top-left part of the frame and enable the built-in SSL with the appropriate switcher.

![platform built-in SSL](02-platform-built-in-ssl.png)

{{%note%}}**Note:** Built-in SSL is not compatible with [public IP](/public-ip) address attached to your servers and is applied to the specified environment name domain only (e.g. *my-project.jelastic.com* for the image above).{{%/note%}}
To initiate your environment installation, click the **Create** button (or **Apply** to adjust the existing one).

Now, upon clicking the **Open in Browser** button for this environment, you'll see that communication with it is performed over the *HTTPS* protocol.


## What's next?

* [Custom SSL](/custom-ssl/)
* [Let's Encrypt SSL](https://www.virtuozzo.com/company/blog/free-ssl-certificates-with-lets-encrypt/)
* [Self-Signed Custom SSL](/self-signed-ssl/)
* [Security Configs for Applications with NGINX Balancer](/nginx-balancer-security/)