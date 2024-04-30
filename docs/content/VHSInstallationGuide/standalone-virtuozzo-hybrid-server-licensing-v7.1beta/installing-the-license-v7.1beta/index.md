---
draft: false
title: "Installing the License v7.1Beta"
aliases: "/installing-the-license-v7.1beta/"
seoindex: "index, follow"
seotitle: "Installing the License v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Installing the License v7.1Beta"
        url: "/installing-the-license-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "installing-the-license-v7.1beta.md"
---
# Installing the License v7.1Beta

Virtuozzo Hybrid Server requires that a different license be installed on each server. You can activate a license during or after the installation. In the latter case, you can install a license from a product key, an activation code, or a license file.

If your Virtuozzo Hybrid Server node cannot access the Internet directly, you can activate a license via a proxy server.

## Using a Proxy Server to Activate Licenses

------------------------------------------------------------------------

When a direct Internet connection is impossible, you can specify an HTTP proxy to access the Key Administration (KA) server through. To do that, add the HTTP proxy information to the `/etc/vz/vz.conf` file as follows:

``` java
HTTP_PROXY="http://<host>:<port>/"
HTTP_PROXY_USER="<username>"
HTTP_PROXY_PASSWORD="<password>"
```

Note the following:

-   You may need to create `/etc/vz/vz.conf`.

-   The proxy server must have port 5224 approved for SSL traffic.

-   The `vzlicutils `package is required for license auto-updating to work. If the package is not installed on your system for some reason, you can install it manually with `yum`. To enable license auto-updates after installing the package, launch the `vzlicmon` service with `systemctl start vzlicmon`. The service will show as `/usr/sbin/vzlicmonitor` in the running processes list.

Once the access to the proxy server is configured, proceed to install the license.

Virtuozzo Hybrid Server licenses are updated automatically by default. A few days before the current license expires, the `vzlicmon` service (a part of the `vzlicutils` RPM package) attempts to contact the Virtuozzo KA server over the Internet and obtain a new license.

## Installing the License from Product Keys, Activation Codes, or License Files

------------------------------------------------------------------------

To install a license from a product key or an activation code, run the `vzlicload -p` command or the `vzlicload -f` command to install from a license file. For example:

``` java
# vzlicload -p <key_or_code>

# vzlicload -f <license_file>
```

When you install a product key or activate a code, a license file is generated and installed on the server in the `etc/vz/licenses/` directory. The difference between the product key and activation code is that the code needs to be activated online, so the server must be connected to the Internet. To activate the code, the installation tool accesses the Key Authentication (KA) licensing server and transmits the specified activation code to it. The KA server generates a license file, sends it back, and the license file is installed on the server automatically.


