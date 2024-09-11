---
draft: false
title: "Container Firewall"
aliases: ["/custom-firewall/", "/setting-custom-firewall/"]
seoindex: "index, follow"
seotitle: "Container Firewall"
seokeywords: "configure access container firewall, configure firewall ruby app server, custom firewall cloud, configure container firewall security, firewall management cloud environment, ruby app server firewall management, node.js app server firewall management, configure container firewall in cloud, paas environment firewall settings, container firewall php app server, container firewall, firewall management gui, container firewall python app server, paas environment firewall management, container firewall ssh, firewall restrict access, cloud environment firewall management, container firewall ui, container firewall java app server, configure firewall node.js app server, paas firewall container"
seodesc: "The container firewall feature provides an additional protection for your environments by managing all of the incoming requests through the list of specified rules. Configure firewall to allow desired and block undesired connections."
menu: 
    docs:
        title: "Container Firewall"
        url: "/custom-firewall/"
        weight: 40
        parent: "external-access-to-applications"
        identifier: "custom-firewall.md"
---

# Container Firewall Rules Management

The platform **Container Firewall** feature provides a possibility to control your nodes availability both from inside and outside of the PaaS. It analyzes various parameters (e.g. incoming request source, protocol, target node port, etc.) to flexibly manage access to your containers through setting the necessary connection rules.

![firewall and isolation illustration](01-firewall-and-isolation-illustration.png)

{{%tip%}}**Tip:** If you want to restrict access between the environments on a single account, it can be automatically configured via the [Network Isolation](/environment-isolation/) feature.{{%/tip%}}


## Container Firewall Management via Platform UI

Each node at the platform (excluding custom [Docker](/container-types/)- and [Windows](/iis8/)-based containers) is provisioned with a set of firewall rules, which can be reviewed and managed through an intuitive graphical user interface. The appropriate section can be accessed by clicking on the **Settings** button next to the required environment and selecting the **Firewall** menu item.

{{%tip%}}**Note:** The availability of the *Container Firewall* UI depends on your particular hosting provider settings. If you don't have this section, please contact your platform support and request feature activation for your account.{{%/tip%}}

![firewall environment settings](02-firewall-environment-settings.png)

Here, the following tabs are available:

* ***Overview*** - provides general information on the feature, allows to change *Firewall State* (which is enabled for all containers by default) and shows *Isolated Env Groups* the current environment is included to
* ***Inbound Rules*** - allows managing incoming requests (not listed ones are denied by default)
* ***Outbound Rules*** - allows controlling outgoing connections (not listed ones are allowed by default)

### Default Firewall Rules

When you create a new container, the platform automatically fills the *Inbound* and *Outbound Rules* sections with some records, required for the proper container operability.

{{%tip%}}**Tip:** These rules are automatically fetched based on the ***EXPOSE*** ports from the same-named variable in the [image's dockerfile](/building-custom-container/), check the linked guide for more details on building Docker images for the platform.{{%/tip%}}

![container firewall inbound rules](03-container-firewall-inbound-rules.png)

Here, rules are grouped by layers and have the next structure:

* the very first record is gray-colored (i.e. non-editable/obligatory), has the highest priority (*1*) and allows platform infrastructure to access container(s) from:
    * *platform orchestrator* to manage all operations inside (password reset, configs generation, CS scripts execution, SSH key generation, etc.)
    * *SSH Gate* and *Web SSH* to provide access to the appropriate services
    * *Shared Load Balancers* to allow connection to the container without public IP
* the default (stack-related) and user-added (either by an environment owner or collaborators) rules
{{%tip%}}**Note:** Apply changes to the default rules only in case you know exactly what you are doing, since these records are required to ensure proper stack-specific functionality and to provide particular features support (e.g. to allow *SSH*, *HTTP*, *HTTPS* or *FTP* connections).{{%/tip%}}
* another non-editable gray record (always the last one due to the lowest priority of *65535*) blocks any incoming connection, which is not allowed via the above-mentioned rules

While working with the container (e.g. adding mount points, installing FTP add-on, etc.), the list of default firewall rules can be automatically complemented by the platform according to the new requirements. Herewith, each default record is added with a 10-points priority step, allowing to insert custom rules in between.

### Adding Container Default Rules

If needed (e.g. for the [automation solutions](/jps/)), you can use the ***OPEN_INBOUND_PORTS*** [environment variable](/environment-variables/) to define custom ports, which should be opened via container firewall during the appropriate nodes' creation.

1\. Click **New Environment** in the dashboard, select the required software stack, and navigate to the ***[Variables](/container-variables/)*** configuration frame.

![container variables](03.1-container-variables.png)

2\. Provide a new ***OPEN_INBOUND_PORTS*** variable in the following format:

```
"OPEN_INBOUND_PORTS": "{port1}, {port2}, ... , {portN}"
```

Here, ***{portN}*** is a particular port (*1234*) or range (*33062-34000*), which will be exposed within the inbound firewall rules (via both *tcp* and *udp* protocols) after container creation.

![inbound ports variable](03.2-inbound-ports-variable.png)

{{%tip%}}**Note:** Changes due to the ***OPEN_INBOUND_PORTS*** variable are applied just once during nodes' installation. Consequently, the [firewall rules](#rules-management) should be managed manually.{{%/tip%}}

3\. You can check your firewall rules after creation.

![custom default firewall rules](03.3-custom-default-firewall-rules.png)

{{%tip%}}**Tip:** Below, you can check an example on how to set this variable via [Cloud Scripting](https://docs.cloudscripting.com/creating-manifest/basic-configs/#environment-variables):

```yaml
jpsType: install
name: OPEN_INBOUND_PORTS env variable
nodes:
  nodeType: apache2
  nodeGroup: cp
  env:
    OPEN_INBOUND_PORTS: 3306, 33061, 33062
```
{{%/tip%}}
    
### Rules Management

For convenient management of the already existing firewall rules and providing the new ones, the tools panel above the list contains a set of buttons, namely: *Add*, *Edit*, *Remove*, *Disable* (*Enable*) and *Refresh*.

![firewall rules management buttons](04-firewall-rules-management-buttons.png)

When adding a new firewall rule, the following parameters should be defined:

* **Nodes** - to select the required environment layer
* **Name** - to provide a name for this record (can be expanded to select from the commonly used presets)
* **Protocol** - to set the required protocol type (*TCP*, *UDP* or *TCP/UDP*)
* **Port Range** - to define a particular port (e.g. *80*) or their range (e.g. *1024-2048*) to be opened/closed for connection; leave this field blank to apply the rule to *all* ports
* **Source** - to select the request source:
    * *Custom IP Address(es)* - a comma-separated list of IPv4/IPv6 addresses and CIDR blocks (e.g. *10.0.0.1,10.0.0.0/24*)
    * predefined ranges - *All*, *All IPv4*, *All IPv6*, *Local Network*, *Internet (Public Access)*
    * *Environment Nodes* - node type (layer) from any environment on an account (subsequently, this rule is automatically complemented/diminished with the required IPs when the appropriate layer is scaled in/out)
* **Priority** - to set a rule priority (where rules with lower values are applied first)
* **Action** - to define the required action upon receiving the matching request (either *allow* or *deny*)

![add new inbound rule](05-add-firewall-rule.png)

Subsequently, if meeting the necessity to **Edit** any default or custom rule, you'll be able to adjust all of the above-described parameters except the *Nodes* field (i.e. target layer cannot be switched). Also, for the testing purposes, you can temporarily disable particular rules and reapply them later on with the appropriate **Disable/Enable** buttons. The **Refresh** button can come in handy to update the list of rules after some server adjustment (e.g. its topology change) without the necessity to restart the whole server.


## Firewall Use Cases

Access to your nodes can be controlled based on such request parameters as its source node's IP address, connection protocol, port and so on. In the guide below, we'll consider a simple example of blocking access to a container for a particular IP address, applied via either:

* [User Interface](#restrict-access-via-user-interface)
* [SSH connection](#restrict-access-via-ssh)

{{%tip%}}**Note:** Before following this instruction, ensure that the appropriate container is provided with a [Public IP](/public-ip/) address.{{%/tip%}}

Also, when preparing some container lifecycle automation solution, you may need to apply the required firewall changes via [platform API](#setting-rules-via-jelastic-api) - examine the list of the appropriate methods within the linked reference.

### Restrict Access via User Interface

So, as it was partly shown above, the platform provides a pretty easy-to-use and powerful GUI to manage container firewall directly via the dashboard.

1\. To access the appropriate control panel, click the **Settings** button next to the required environment and switch to the **Firewall** section within the opened tab.

![add new inbound rule](06-add-new-inbound-rule.png)

Select the **Inbound Rules** tab and click on the **Add** button (obviously, to manage external container traffic, you need to choose the **Outbound Rules** tab instead; herewith, all rule parameters are similar to the ones described below).

2\. In the opened ***Add Inbound Rules*** form you can configure a new condition for the incoming requests' processing by a container.

![firewall rule to deny access from ip](07-firewall-rule-to-deny-access-from-ip.png)

To deny a connection from a particular IP (according to our suggested use case example), fill in the fields as follows:

* **Nodes** - chose a container to restrict access to (*tomcat* in our case)
* **Name** - input any desired rule name (e.g. *my-rule*)
* **Protocol** - select a required protocol (*TCP*)
* **Port Range** - deny access to all ports by leaving this field *blank*
* **Source** - choose the *Custom IP Address(es)* option and type the necessary IP in the appeared **IP Address Range** field (*111.111.111.111*)
* **Priority** - set the appropriate priority for this record (e.g. *900* to be applied before the default rules)
* **Action** - select the *Deny* option  

Click **Add** to save and automatically apply your rule.

3\. Now, when trying to connect to your node from the specified *111.111.111.111* IP address, a user will be shown the following page:

![prohibited connection](08-prohibited-connection.png)

This way you can deny access to your containers from any IP address.

### Restrict Access via SSH

Alternatively, you can configure firewall rules for your container via terminal when accessing the node through [SSH Gate](/ssh-gate/).

{{%note%}}**Note:** Although most of the firewall configurations can be performed via the dedicated user interface, management via SSH is more flexible (for example, allows configuring NAT redirects). Herewith, such rules won't be displayed in the UI list but will be of higher priority.{{%/note%}}

1\. The simplest way to access node via SSH is to call the appropriate **[Web SSH](/web-ssh-client/)** option directly from the platform dashboard - click the same-named button next to the required node. Once connected, check the ***/etc/jelastic/metainf.conf*** file to ensure that container firewall is turned on:

```
cat /etc/jelastic/metainf.conf
```

![checking firewall setting via ssh](09--checking-firewall-setting-via-ssh.png)

Here, the ***FIREWALL_ENABLED*** parameter should be equal to &ldquo;*1*&rdquo;. If not, contact your hosting provider and request enabling of firewall protection for your account.

2\. Next, you need to modify the ***/etc/sysconfig/iptables-custom*** file (e.g. with a *vim* editor):

![edit iptables file with custom rules](10--edit-iptables-file-with-custom-rules.png)

{{%tip%}}**Note:** The ***/etc/sysconfig/ip6tables-custom*** file should be used when working with the IPv6 rules.{{%/tip%}}

3\. Declare the required firewall rules using the *iptables-save* tool format. For example, the following code should be used to deny access from a particular IP (e.g. *111.111.111.111*):

```
filter
:INPUT DROP [0:0]
:FORWARD DROP [0:0]
:OUTPUT ACCEPT [0:0]
-I INPUT -s 111.111.111.111 -p tcp -m state --state NEW -m tcp --dport 1111 -j DROP
COMMIT
\#
```

![iptables file to deny access from ip](11-iptables-file-to-deny-access-from-ip.png)

4\. Use the next command to apply your custom firewall settings to the list of container default rules:

```
sudo /usr/bin/jem firewall fwstart
```

![apply custom firewall rules](12-apply-custom-firewall-rules.png)

5\. Now, you can check the list of the currently operating firewall rules for your container by executing the following command:

```
sudo jem firewall list {table} {options}
```

Here:  

* ***{table}*** - specifies the target iptable (*filter*, *nat*, *mangle*, *raw*)
* ***{options}*** - lists [iptable parameters](https://linux.die.net/man/8/iptables), which should be applied

![view all firewall rules](13-view-all-firewall-rules.png)

Your custom rule is placed after the default ones, denying access to your node from the *111.111.111.111* IP address.

### Setting Rules via Platform API

In some cases (e.g. for custom scripts, automatizations, etc.), you may need to configure firewall rules through the code. To do this, you can use the appropriate methods from the **environment > Security** section in the [platform API](https://www.virtuozzo.com/application-platform-api-docs/) documentation:

* ***AddRule*** - creates a new rule
* ***AddRules*** - adds several rules
* ***EditRule*** - changes parameters of an existing rule
* ***GetRules*** - shows a list of rules for the environment
* ***RemoveRule*** - deletes a rule
* ***RemoveRules*** - removes several rules
* ***SetFirewallEnabled*** - switches on the firewall
* ***SetRuleEnabled*** - enables an existing rule
* ***SetRules*** - replaces existing rules

This way, managing your *Сontainer Firewall* allows you to control the availability of nodes on your account effectively and to increase applications security significantly (by filtering desired and undesired connections).


## What's next?

* [Network Isolation](/environment-isolation/)
* [Shared Load Balancer](/shared-load-balancer/)
* [Public IP](/public-ip/)
* [Endpoints](/endpoints/)