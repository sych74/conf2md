---
draft: false
title: "Configuring the HTTP Server v7.1Beta"
aliases: "/configuring-the-http-server-v7.1beta/"
seoindex: "index, follow"
seotitle: "Configuring the HTTP Server v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Configuring the HTTP Server v7.1Beta"
        url: "/configuring-the-http-server-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "configuring-the-http-server-v7.1beta.md"
---
# Configuring the HTTP Server v7.1Beta

To configure the HTTP server to deliver Virtuozzo Hybrid Server distribution files over the network, do the following:

1.  Make sure the HTTP server package is installed and the service is running. For example:

    ``` java
    # yum install httpd
    # systemctl start httpd.service
    ```

2.  Copy the contents of your Virtuozzo Hybrid Server installation DVD or ISO image to a directory on the HTTP server (for example, `/var/www/html/vz`). The directory must have the `r-x` access permissions so that client server(s) can boot from this location (for example, `/vz`) over the network. To set access permissions to the `/var/www/html/vz` directory, run:

    ``` java
    # chmod 755 /var/www/html/vz
    ```


