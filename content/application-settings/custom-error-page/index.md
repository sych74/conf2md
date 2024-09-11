---
draft: false
title: "Custom Error Page"
aliases: "/custom-error-page/"
seoindex: "index, follow"
seotitle: "Custom Error Page"
seokeywords: "error page, custom error, custom error page, make own error page, error message, customize error message, error page nginx"
seodesc: "When any error occurs, a particular default error page is opened depending on the problem. Your custom error page can be configured via NGINX balancer enabled in your environment."
menu: 
    docs:
        title: "Custom Error Page Settings"
        url: "/custom-error-page/"
        weight: 110
        parent: "application-settings"
        identifier: "custom-error-page.md"
---

# Custom Error Page Settings via NGINX Balancer

When an error occurs within a particular environment (e.g. when trying to access non-existing page), a default error page for the server is opened. For example:

![Tomcat default error page](01-tomcat-default-error-page.png)

You can substitute this error page with a custom one to provide end-users with more specific instructions and leave email to contact you. Below, we'll show how to configure a custom error page using the NGINX load balancer added to your environment:

1\. Go to your platform dashboard, find the NGINX load balancer in your environment and click the **Config** button next to it.

![NGINX balancer config button](02-nginx-balancer-config-button.png)

2\. In the opened configuration manager tab navigate to the **/etc/nginx/conf.d** folder and create or upload your custom error page.

![create custom error page](03-create-custom-error-page.png)

3\. For this tutorial we'll use the following ***error.html*** file:

![example custom page](04-example-error-page.png)

4\. Then navigate to the **/etc/nginx** directory and copy content of the ***nginx-jelastic.conf*** file and paste it into the ***nginx.conf***, replacing the *include /etc/nginx/nginx-jelastic.conf;* line (circled in the image below).

![edit nginx.conf file](05-edit-nginx-conf-file.png)

Now, you are able to specify all the required configurations.

5\. Find the ***server*** section of the pasted configs and substitute the default *error_page* settings with the following strings:
```nginx
error_page 403 404 500 502 503 504 /error.html;
proxy_intercept_errors on;
```

![error page configurations](06-error-page-configurations.png)

6\. Next, scroll a little bit lower and adjust the error page parameters within **location** subsections:
```nginx
location /error.html {
    root   /etc/nginx/conf.d;
    internal;
}

location / {
    if ($cookie_SRVGROUP ~ group|common) {
        proxy_pass http://$cookie_SRVGROUP;
        error_page 403 404 500 502 503 504 = /error.html;
    }
    if ($cookie_SRVGROUP !~ group|common) {
        add_header Set-Cookie "SRVGROUP=$group; path=/";
    }
    proxy_pass http://default_upstream;
    add_header Set-Cookie "SRVGROUP=$group; path=/";
}

location @rescue {
    proxy_pass http://$cookie_SRVGROUP;
    error_page   500 502 503 504 = error.html;
}

location @recycle {
    proxy_pass http://default_upstream;
    add_header Set-Cookie "SRVGROUP=$group; path=/";
}
```

![error page location settings](07-error-page-location-settings.png)

7\. In case of using [SSL](/secure-sockets-layer/) for your website (i.e. for connections over HTTPS), some additional configurations are required (otherwise go to the *9th* step of this guide). Add the following lines to the **servers** section of the ***/etc/nginx/conf.d/ssl.conf*** file:
```nginx
proxy_intercept_errors on;
location /error.html {
                    root   /etc/nginx/conf.d;
 }
```

![configure ssl.conf file](08-configure-ssl-conf-file.png)

8\. Also, you need to adjust the ***/etc/nginx/conf.d/ssl.upstreams.inc*** file. Find the next condition and change it as follows:
```nginx
if ($cookie_SRVGROUP ~ group|common) {
                   proxy_pass http://$cookie_SRVGROUP;
                   error_page 403 404 /error.html;
                   error_page   500 502 503 504 = @resque;
}
```

![adjust SSL upstreams file](09-adjust-ssl-upstreams-file.png)

9\. Don't forget to **Restart** NGINX server to apply all changes.

![restart NGINX balancer nodes](10-restart-nginx-balancer-nodes.png)

10\. That's it! Try to access any non-existing page within your domain.

![custom error page](11-custom-error-page.png)

{{%note%}}**Note:** If the server with pre-configured custom error pages or the whole environment is not reachable, a platform-wide default error page will be displayed, e.g.:

![PaaS default error page](12-paas-default-error-page.png)

You cannot modify such notifications for your environments.{{%/note%}}


## What's next?

* [Configuration File Manager](/configuration-file-manager/)
* [Application Lifecycle Management](/how-to-manage-application-lifecycle/)
* [NGINX Balancer Configuration](/nginx-balancer-config/)
* [Secure Sockets Layer](/secure-sockets-layer/)