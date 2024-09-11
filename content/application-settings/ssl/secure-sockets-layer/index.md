---
draft: false
title: "Secure Sockets Layer"
aliases: ["/secure-sockets-layer/", "/secure-java-encryption-and-decryption/"]
seoindex: "index, follow"
seotitle: "Secure Sockets Layer"
seokeywords: "ssl, secure sockets layer, ssl certificates, web ssl certificates, web server ssl certificate, ssl web certificate, ssl connection, secure connection, security protocol, ssl security protocol"
seodesc: "Find out what Secure Sockets Layer is and how to use SSL certificates to establish a secure connection for your web server, which encrypts all information moving to and from your website."
menu: 
    docs:
        title: "Secure Sockets Layer"
        url: "/secure-sockets-layer/"
        weight: 10
        parent: "ssl"
        identifier: "secure-sockets-layer.md"
---

# Secure Sockets Layer (SSL)

**SSL (Secure Sockets Layer)** is the standard security protocol for establishing an encrypted connection between a web server and a browser. This technology ensures that data exchange remains private, i.e. cannot be intercepted by a third-party. Such protection is essential when transferring confidential information like credit card transactions, login credentials, etc.

SSL encrypts the data with the help of two keys - public (can be known to everyone) and private (known to the recipient of the transmissible message only) ones. When configured on a web server, SSL allows using HTTPS protocol (over the *443* port) instead of the default HTTP one to access its content.

To establish an SSL connection, a web server requires an **SSL Certificate** to be installed, which digitally binds a cryptographic key to a holder's details and site hostname. Usually, such a certificate needs to be verified by a trusted authority (or check out the [Self-Signed SSL](/self-signed-ssl)), which makes it reliable and ensures that any connection to your site or application is performed without issues.

The platform gives you an opportunity to choose between three available SSL solutions:

* [Built-In SSL Certificates](/built-in-ssl) - enables an already trusted platform Built-In SSL certificate, avoiding any additional checks and save your time on the certificate validation
{{%note%}}**Note:** This solution is not compatible with [public IP](/public-ip) address attached to your servers and is applied to the default environment domain name only (i.e. with the hoster's domain at the end).{{%/note%}}
* [Let's Encrypt SSL Certificates](https://www.virtuozzo.com/company/blog/free-ssl-certificates-with-lets-encrypt/) - installs a pre-configured add-on managed by the platform to greatly simplify and automate the process of issuing (from the free and open Let's Encrypt certificate authority) and integration of trusted SSL certificates
* [Custom SSL Certificates](/custom-ssl) - allows to manually configure everything for your certificate (e.g. generate it, providing your custom domain name, select preferred Certificate Authority for validation, etc.)


## What's next?
* [Shared Load Balancer](/shared-load-balancer/)
* [Public IP](/public-ip/)
* [Custom Domain Names](/custom-domains/)
* [Container Firewall](/custom-firewall/)