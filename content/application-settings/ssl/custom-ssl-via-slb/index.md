---
draft: false
title: "Custom SSL via SLB"
aliases: "/custom-ssl-via-slb/"
seoindex: "index, follow"
seotitle: "Custom SSL via SLB"
seokeywords: "custom ssl, ssl without ip, shared load balancer ssl, ssl api, custom ssl api, bind ssl, bind ssl api, platform ssl, configure ssl, configure ssl without ip, shared balancer ssl, custom ssl via slb, external domain ssl"
seodesc: "Configure custom SSL for your environment without the necessity to attach the external IP address. Use the straightforward API methods to upload your SSL certificates to the platform and bind it to required external domains."
menu: 
    docs:
        title: "Custom SSL via SLB"
        url: "/custom-ssl-via-slb/"
        weight: 40
        parent: "ssl"
        identifier: "custom-ssl-via-slb.md"
---

# Custom SSL via Shared Load Balancer (SLB)
The platform provides multiple possibilities to configure SSL for the environments. The available options depend on the particular topology and target domains:

* environments with public IP as an entry point can utilize the *[Let's Encrypt SSL](/lets-encrypt-ssl)* and *[Custom SSL](/custom-ssl)* options to automatically secure connection to any domain attached
* the *[Built-In SSL](/built-in-ssl/)* option allows to automatically configure SSL for the base domain of the environment without public IP
* in case SSL should be set up for custom domains on the environment without external IP the *Custom SSL via SLB* feature can be used

The latter solution is mainly aimed for the platform installations on top of the *[Azure](https://www.virtuozzo.com/application-platform-ops-docs/azure-hybrid)* or *[Google](https://www.virtuozzo.com/application-platform-ops-docs/paas-on-google-cloud)* hardware (i.e. without additional external IPs). Let's overview it in more details.


## Configure Custom SSL via SLB

The feature is designed to give an ability to set up Custom SSL certificates without obligatory [external IP](/public-ip) attached to the entry point of the environment. As the first step of this approach, a private key, the domain certificate and, optionally, intermediate certificate are uploaded to the platform database. Next, the data is synced across the cluster of [Shared Load Balancers](/shared-load-balancer). The selection between the SSL certificates on SLB is performed over SNI.

[Server Name Indication](https://en.wikipedia.org/wiki/Server_Name_Indication) (SNI) is an extension to the TLS protocol, which ensures that clients send a name of the domain they request. SNI allows server to provide a certificate with the correct domain even in the case when a full list of hostnames cannot be known in advance.

Currently, all the configurations are performed via API (the UI support will be implemented in the future releases):

* ***[GetSSLCerts](https://docs.jelastic.com/api/#!/api/environment.Binder-method-GetSSLCerts) (session, [ids])*** - lists all certificates for the current user (or the ones specified in the *ids* parameter)
* ***[AddSSLCert](https://docs.jelastic.com/api/#!/api/environment.Binder-method-AddSSLCert) (session, key, cert, [interm])*** - uploads private key, domain certificate, and intermediate certificate to the platform database (can be provided via links or as a parameter body)
* ***[EditSSLCert](https://docs.jelastic.com/api/#!/api/environment.Binder-method-EditSSLCert) (session, id, [key], [cert], [interm])*** - updates the specified certificate (to delete intermediate certificate use "*\**", "*null*", or "*none*" as a value)
* ***[RemoveSSLCerts](https://docs.jelastic.com/api/#!/api/environment.Binder-method-RemoveSSLCerts) (session, ids)*** - removes the specified certificates (use "*\**" to select all); assigned certificates cannot be deleted and should be unbound first
* ***[BindSSLCert](https://docs.jelastic.com/api/#!/api/environment.Binder-method-BindSSLCert) (session, envName, certId, [entryPoint], [extDomains])*** - binds specified SSL certificate to environment or, if *SLB* is set as *entyPoint*, binds it on SLB to the listed external domain names
* ***[UnbindSSLCert](https://docs.jelastic.com/api/#!/api/environment.Binder-method-UnbindSSLCert) (session, envName, [extDomains])*** - unbinds SSL certificate from the environment or, if the *extDomains* parameter is provided, from the listed custom domains on SLB
* ***[BindExtDomains](https://docs.jelastic.com/api/#!/api/environment.Binder-method-BindExtDomains) (session, envName, extDomains, [certId])*** - binds custom domain names to the environment and, if the *cetId* parameter is provided, installs the appropriate certificate on SLB
* ***[GetExtDomains](https://docs.jelastic.com/api/#!/api/environment.Binder-method-GetExtDomains) (session, envName)*** - lists custom domains attached to the environment

{{%note%}}**Note:** The maximum number of custom SSL certificates attached via SLB is limited per account with the ***slb.customssl.maxcount*** [quota](https://www.virtuozzo.com/application-platform-ops-docs/quotas-list) (50 for billing, 5 for trial users by default) to prevent the feature abuse.{{%/note%}}
So, to attach custom SSL to the environment without public IP through the SLB, you need to upload your certificates to the platform database (***AddSSLCert***) and bind it to the new or existing custom domains (***BindExtDomains*** or ***BindSSLCert*** respectively).



## What's next?
* [Secure Sockets Layer](/secure-sockets-layer)
* [Built-In SSL](/built-in-ssl)
* [Custom SSL](/custom-ssl)
* [Let's Encrypt SSL](/lets-encrypt-ssl)
* [Shared Load Balancer](/shared-load-balancer)