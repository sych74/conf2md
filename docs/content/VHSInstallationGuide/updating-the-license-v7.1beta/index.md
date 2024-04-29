---
draft: false
title: "Updating the License v7.1Beta"
aliases: "/updating-the-license-v7.1beta/"
seoindex: "index, follow"
seotitle: "Updating the License v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Updating the License v7.1Beta"
        url: "/updating-the-license-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "updating-the-license-v7.1beta.md"
---
# Updating the License v7.1Beta

You can use the `vzlicupdate` utility to update the license currently installed on the server. When executed, the utility tries to connect to the Key Authentication (KA) server, retrieve a new license, and install it on the server.

To update your license, do the following:

1.  Ensure the host where you wish to update the license is connected to the Internet.
2.  Run `vzlicupdate` on the server (your server must have at least one public IPv4 address).

By default, `vzlicupdate` tries to access the KA server at [ka.virtuozzo.com](http://ka.virtuozzo.com). However, you can explicitly specify what KA server to use using the `--server` option, for example, `vzlicupdate --server` `ka.server.com`.

## Switching License to a New HWID

------------------------------------------------------------------------

If your Virtuozzo Hybrid Server license has become invalid due to a changed HWID (for example, after adding or removing a network card), you can have the license switch to the new HWID as follows:

``` java
# vzlicupdate -t -a <activation_code>
```


