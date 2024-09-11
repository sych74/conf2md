---
draft: false
title: "NGINX PHP"
aliases: ["/nginx-php/", "/nginx/"]
seoindex: "index, follow"
seotitle: "NGINX PHP"
seokeywords: "nginx, nginx php, nginx configuration, nginx httpd, nginx server, php application server, php hosting, create nginx, nginx php server, install nginx php, nginx application server, php application server, configure nginx php, nginx fastcgi"
seodesc: "Find out about the PHP applications hosting at the platform with the help of the NGINX server. Create a new NGINX PHP application server and configure it up to your needs."
menu:
    docs:
        title: "NGINX PHP"
        url: "/nginx-php/"
        weight: 10
        parent: "nginx-php"
        identifier: "nginx-php.md"
---

# NGINX PHP

{{%tip%}}The *NGINX PHP* stack is [HTTP/3](/http3/) ready with the feature support enabled by default since the *1.16.1* release for PHP *7.2.26*, *7.3.13*, *7.4.1* versions and above. However, a [public IP address](/public-ip/) is required to bypass the Shared Load Balancer and work directly with the server over HTTP/3.{{%/tip%}}

**[NGINX](https://nginx.org/en/)** is a fast and lightweight HTTP server, which is widely used by developers across the world. It is highly customizable due to the modular structure, which simultaneously allows utilizing just the required functionality, ensuring efficient resource usage.

The platform customizes and optimizes NGINX to provide it as a PHP application server fully compatible with the platform functionality. Compared to the [Apache PHP](/apache-php/), it is more suitable for handling websites with static content, but due to the FastCGI support can process complex scripts as well.

{{%tip%}}**Note:** This template utilizes a modern ***systemd*** initialization daemon.{{%/tip%}}

To create NGINX server for PHP application hosting, follow the steps in the detailed instruction below.

1\. Log into the platform dashboard and click the **New Environment** button to access the topology wizard.

![new environment button](01-new-environment-button.png)

2\. On the **PHP** engine tab, choose ***NGINX*** as your application server and configure other parameters (like [cloudlets](/automatic-vertical-scaling/) or [environment region](/environment-regions/)) up to your needs.

![nginx php topology wizard](02-nginx-php-topology-wizard.png)

Click **Create** to proceed.

3\. After creation, click **Open in Browser** next to the NGINX server:

![nginx php open in browser](03-nginx-php-open-in-browser.png)

4\. You will see the server's ***phpinfo*** data by default.

![nginx phpinfo start page](04-nginx-phpinfo-start-page.png)

The next step will be to [deploy](/deployment-guide/) your PHP application.


## NGINX Configuration

While using NGINX as an application server, there are some restrictions on the size of uploaded files to the application. You can make the next configurations to adjust it:

1\. Hover over the NGINX application server and click the appeared **Config** button.

![nginx php config button](05-nginx-php-config-button.png)

2\. Within the opened [configuration file manager](/configuration-file-manager/), locate and adjust the ***/etc/nginx/nginx.conf*** file by adding the following string to the *http* section:

```
client_max_body_size 50m;
```

![adjust nginx conf file](06-adjust-nginx-conf-file.png)

You can set any required value instead of the *50MB* used in the example above.

{{%note%}}**Note:** Regardless of the setting above, if working via the platform inbuilt file manager, you are limited to the upload size of 150MB (may vary based on the hosting provider settings). To operate larger files, you need to attach [public IP](/public-ip/) and use own manager (for example, you can utilize the [FTP add-on](/ftp-ftps-support/)).{{%/note%}}

3\. **Save** the made changes and apply them by clicking the **Restart Nodes** button.

![nginx php restart nodes](07-nginx-php-restart-nodes.png)

Learn more about the PHP servers configuration via the appropriate guides:

* [PHP Dev Center](/php-center/)
* [PHP Extensions](/php-extensions/)
* [PHP Accelerators](/php-accelerators/)
* [PHP Auto Configurations](/php-auto-configuration/)


## What's next?

* [NGINX Security Configurations](/nginx-security-configurations/)
* [NGINX Modules](/nginx-modules/)
* [NGINX WebDav Module](/nginx-webdav-module/)
* [Caching in NGINX App Server](/caching-nginx-server/)