---
draft: false
title: "Swap Public IPs"
aliases: "/cli-ip-swap/"
seoindex: "index, follow"
seotitle: "Swap Public IPs"
seokeywords: "cli, cli tutorial, cli guide, swap public ip, swap external ip, move public ip, move external ip, swap ip, move ip, cli swap ip, exchange addresses, cli move ip, ip exchange, change node address, swap external addresses, public ip exchange"
seodesc: "Learn how to simplify your project&#8217;s lifecycle management with the swap public IPs CLI method. Move or exchange external IP addresses between two nodes of your PaaS account with ease using platform CLI."
menu: 
    docs:
        title: "Swap Public IPs"
        url: "/cli-ip-swap/"
        weight: 11
        parent: "platform-cli"
        identifier: "cli-ip-swap.md"
---

# CLI Tutorial: Public IPs (External Addresses) Swap

The operation of [public IPs](/public-ip/) swap can come in handy for routing of the incoming requests to the required environment or application. It may be especially useful when, for example, switching testing and production environments.

The appropriate ***SwapExtIps*** CLI method gives you the ability to exchange external IP addresses between two containers. In case only one node has a public IP, it will be moved (reassigned) to the second instance. The method can work with nodes of the same or different environments but only in the confines of a single account.

As usual, the operation requires just a single line of code for being executed:
```bash
~/jelastic/environment/binder/swapextips --envName {env_name} --sourceNodeId {source_node_id} --targetNodeId {target_node_id} [--sourceIp {source_ip}] [--targetIp {target_ip}]
```

Here, the following parameters should be specified:

* ***{env_name}*** - name of the environment, where the transferred external IP is currently attached
* ***{source_node_id}*** - identifier of the node from the stated environment, which IP should be swapped/moved
* ***{target_node_id}*** - ID of the target node (can belong to any environment on the account)
* ***{source_ip}*** and ***{target_ip}*** - optional parameters for two specific addresses to be swapped (if not specified, all external IPs from source node are transferred to the target and vice versa)

![CLI swap external IP](01-cli-swap-external-ip.png)

{{%note%}}**Notes:**  

* Before using the ***SwapExtIps*** CLI method, please make sure that the source and destination nodes (environments) are running and belong to the same [region](/environment-regions/).
* *<u>Before the PaaS 5.8 release,</u>* this method does not support IPv6 and works with IPv4 only.
* *<u>Before the PaaS 6.0 release,</u>* IP swap fails if an environment has a [bound](/custom-domains/#how-to-bind-domain-to-environment) custom domain.
* The process may cause short-term unavailability of the corresponding Public IP address(es) (up to 10 seconds).
* If you need to swap two specific addresses between nodes with [multiple IPs](/multiple-public-ip/) on each one, please contact the Support Team for assistance. Support of such cases is currently under development and will be implemented in future releases.
* The following node types will be automatically restarted to start listening on the new addresses after the operation: *GlassFish*, *Apache PHP*, *Apache Ruby*, *NGINX PHP*, *NGINX Ruby*.
* Based on the comprized services, a manual restart may be required for the *[Elastic VPS](/vps/)* and custom *[Docker containers](/docker-container-deploy/)* to adapt for the IP address change.
* We recommend rechecking the *[Access via SLB](/shared-load-balancer/#deny-access-via-shared-load-balancer)* state for both nodes after swapping IPs.{{%/note%}}

In a few minutes, your IPs will be exchanged between the specified nodes, and the details will be provided in the operation response.

Now, as you caught the idea on how to work with our CLI, you can proceed to the environment management automation. For example, by creating corresponding scripts for the frequently used operations' chains.
The full information on all of the available commands and methods can be found within the [platform API](https://www.virtuozzo.com/application-platform-api-docs/) documentation.


## What's next?

Other examples of CLI usage are listed below:

* [environment creation](/cli-create-environment/)
* [environment start/stop](/cli-environment-control/)
* [environment cloning](/cli-clone-environment/)
* [environment migration](/cli-environment-migration/)
* [server scaling](/cli-scaling/)
* [Docker container redeploy](/cli-container-redeploy/)
* [Docker volumes](/cli-docker-volumes/)
* [mount points](/cli-mount-points/)
* [VCS projects deployment](/cli-vcs-deploy/)