---
draft: false
title: "NGINX WebDav Module"
aliases: "/nginx-webdav-module/"
seoindex: "index, follow"
seotitle: "NGINX WebDav Module"
seokeywords: "nginx, configuration, webdav module, server,"
seodesc: "WebDAV is turning into an important tool which was invented in order to simplify the way you update websites."
menu:
    docs:
        title: "NGINX WebDav Module"
        url: "/nginx-webdav-module/"
        weight: 40
        parent: "nginx-php"
        identifier: "nginx-webdav-module.md"
---

# NGINX WebDav Module

While setting up a website you can face the need to build some complicated method of viewing and updating the information on the site. There are lots of solutions - using a local copy, using a combination of HTTP and FTP tools to download the original and upload the changes etc. But also as an easy solution you can use **Web-based Distributed Authoring and Versioning (WebDAV)** which is available in the platform.

WebDAV is turning into an important tool which was invented in order to simplify the way you update websites.


## Enabling WebDAV Module for NGINX Server

1\. Click **Config** button for the server in your environment.

2\. In the **/etc/nginx** folder open the ***nginx.conf*** file. Modify configuration by adding the following strings as it is shown in the picture below:

```
dav_methods PUT DELETE MKCOL COPY MOVE;
dav_ext_methods PROPFIND OPTIONS;
```

![nginx webdav module 1](1.png)

3\. Save the changes and restart **NGINX**.

Using *nginx.conf* file you can set any other configurations for WebDav module. Follow the link ([https://nginx.org/en/docs/http/ngx_http_dav_module.html](https://nginx.org/en/docs/http/ngx_http_dav_module.html)) to find some additional useful information.


## Setting Up Security Configuration

1\. Generate hash from your password. For that you can use any **htpasswd tool** or online service (for example, [http://www.htpasswdgenerator.net/](http://www.htpasswdgenerator.net/)).

2\. Create simple text file with previously generated hash.

3\. Click **Config** button for your **NGINX** server.

4\. Upload the created file to the **/var/www/webroot/ROOT** folder.

5\. In the **/etc/nginx** folder open the ***nginx.conf*** file. Add the following strings:

```
auth_basic "Restricted area";
auth_basic_user_file /var/www/webroot/ROOT/.htpasswd;
```

![nginx webdav module 2](2.png)

6\. Save the changes and restart **NGINX**.

Finally you can go to any **WebDAV client**. State there the host (also your credentials if you set up security configuration) and connect to the server. As a result you'll see your files and will be able to edit them, update, add some new files etc.


## What's next?

* [NGINX Modules](/nginx-modules/)
* [Caching in NGINX App Server](/caching-nginx-server/)