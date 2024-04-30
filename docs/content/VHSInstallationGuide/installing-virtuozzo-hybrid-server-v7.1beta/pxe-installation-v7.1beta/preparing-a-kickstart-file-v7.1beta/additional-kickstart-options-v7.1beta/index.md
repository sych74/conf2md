---
draft: false
title: "Additional Kickstart Options v7.1Beta"
aliases: "/additional-kickstart-options-v7.1beta/"
seoindex: "index, follow"
seotitle: "Additional Kickstart Options v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Additional Kickstart Options v7.1Beta"
        url: "/additional-kickstart-options-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "additional-kickstart-options-v7.1beta.md"
---
# Additional Kickstart Options v7.1Beta

In addition to standard Linux kickstart options, Virtuozzo Hybrid Server provides a number of own options that you need to add to your kickstart file.

## General Options

------------------------------------------------------------------------

**key (mandatory)**

``` java
key <key>
```

Installs the Virtuozzo Hybrid Server product key on the server.

**%packages (mandatory)**

Specifies the package groups to install on the server:

-   `@base`, `@core`, mandatory, core Virtuozzo Hybrid Server packages.

-   `@vz`, mandatory, Virtuozzo Hybrid Server OS virtualization packages.

-   `@ps`, mandatory, Virtuozzo Hybrid Server hardware virtualization packages.

-   `@qemu`, mandatory, QEMU-related packages.

-   `@clustering`, optional, packages required for creating clusters from Virtuozzo Hybrid Server nodes.

-   `@vstorage`, optional, packages required for setting up Virtuozzo Storage clusters.

-   `@optional`, optional, additional packages not installed by default.

**cep (optional)**

``` java
cep [--agree|--agree-node|--disagree]
```

Sets participation in the Customer Experience Program.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Option</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><code class="docutils literal notranslate">--agree</code></p></td>
<td><div class="content-wrapper">
<p>Join the program with physical server and virtual environments. In this case, Virtuozzo Hybrid Server will periodically collect information about the configuration of your physical server and virtual servers and use it to improve the product to better fit your needs.</p>
<div>
<div>
<p>No private information like your name, e-mail address, phone number, or keyboard input will be collected.</p>
</div>
</div>
</div></td>
</tr>
<tr class="even">
<td><p><code class="docutils literal notranslate">--agree-node</code></p></td>
<td><div class="content-wrapper">
<p>Join the program with physical server only. In this case, Virtuozzo Hybrid Server will periodically collect information only about the configuration of your physical server and use it to improve the product to better fit your needs.</p>
<div>
<div>
<p>No private information like your name, e-mail address, phone number, or keyboard input will be collected.</p>
</div>
</div>
</div></td>
</tr>
<tr class="odd">
<td><p><code class="docutils literal notranslate">--disagree</code></p></td>
<td><p>Do not join the program.</p></td>
</tr>
</tbody>
</table>

**up2date (optional)**

Does the following:

1.  Configure the repositories with updates for Virtuozzo Hybrid Server software and templates.

2.  Check the repositories for available updates.

3.  Download and install the updated packages, if any, on the server.

Using this option, you can ensure that you have the latest Virtuozzo Hybrid Server software packages and templates right after the installation, without the need to manually check for updates.

**readykernel –disable-autoupdate (optional)**

Disables the automatic downloading and installation of the latest ReadyKernel patches for the current kernel. With automatic updating enabled by default, ReadyKernel will check for new patches daily at 12:00 server time. If a patch is available, ReadyKernel will download, install, and load it for the current kernel.

**prlnet (optional)**

``` java
prlnet --name <name> [--ip-scope-start <start_IP_addr> --ip-scope-end <end_IP_addr>]
       [--ip <adapter_IP_addr>[/<mask>]] [--dhcp-ip <DHCP_IP_addr>]
       [--dhcp-server <on|off>] [--dhcp6-server <on|off>]
       [--ip6-scope-start <start_IP_addr> --ip6-scope-end <end_IP_addr>]
       [--ip6 <adapter_IP_addr>[/<mask>]] [--dhcp-ip6 <DHCP_IP_addr>]
```

Defines the range of IP addresses (IPv4 and IPv6) the DHCP server will be able to allocate to virtual servers in the defined host-only network; virtual adapter IP address (IPv4 and IPv6) and subnet mask; DHCP server IP address (IPv4 and IPv6); and enables or disables the virtual DHCP server (DHCPv4 or DHCPv6).

If you omit one or more parameters, the following default values will be used:

-   `--ip-scope-start`: 10.37.130.1,

-   `--ip-scope-end`: 10.37.130.254,

-   `--ip`: 10.37.130.2/255.255.255.0,

-   `--dhcp-ip`: 10.37.130.1,

-   `--dhcp-server`: on,

-   `--ip6-scope-start`: fdb2:2c26:f4e4::,

-   `--ip-scope-end`: fdb2:2c26:f4e4::ffff,

-   `--ip6`: fdb2:2c26:f4e4::1/ffff:ffff:ffff:ffff::,

-   `--dhcp-ip6`: fdb2:2c26:f4e4::,

-   `--dhcp6-server`: on.


