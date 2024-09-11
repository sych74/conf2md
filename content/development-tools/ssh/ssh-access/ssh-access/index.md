---
draft: false
title: "Overview"
aliases: "/ssh-access/"
seoindex: "index, follow"
seotitle: "SSH Access"
seokeywords: "access to container via web ssh, access via ssh client to node, ssh access to container via web-based client, access to container in cloud via web ssh, ssh web client, cloud container ssh access, ssh access to container via terminal, ssh access to container, access to container using ssh key, ssh access to node in cloud, ssh access to node from browser, ssh connections comparison, ssh access to container in cloud, ssh access to container from browser, access via ssh client to container, connection with ssh key pair, paas ssh access"
seodesc: "Find out about the possible ways to access PaaS account via SSH protocol. Get the general overview and comparison of the connection through SSH Gate and via the platform Web SSH client."
menu:
    docs:
        title: "Overview"
        url: "/ssh-access/"
        weight: 10
        parent: "ssh-access"
        identifier: "ssh-access.md"
---

# SSH Access

The platform supports access via SSH in one of the following ways:

- ***[Web SSH](/web-ssh-client/)*** - An access to a separate node within your environment, which is based on the *user's session*; connection is initiated upon clicking the **Web SSH** button next to the desired environment in dashboard<a id="direct-access"></a> (which allows to connect from anywhere over Internet, using just a browser).

- ***[SSH Gate](/ssh-gate-access/)*** - Such connection type is based on the *SSH key pair* usage and allows access to either [whole PaaS account](/ssh-gate-access/#ssh-access-to-platform-account) or just a [particular container](/ssh-gate-access/#direct-access-to-container); it provides the substantial level of security, connecting only instances with **private SSH key** that matches the appropriate **public key**, stored within your Platform account settings.

![PaaS SSH access options](01-ssh-access-options.png)

After accessing node via SSH using any of the above-described methods, you can start managing your container.


## What's next?

* [SSH Overview](/ssh-gate/)
* [Web SSH Access](/web-ssh-client/)
* [SSH Gate Access](/ssh-gate-access/)
* [SSH Management](https://www.virtuozzo.com/company/blog/ssh-to-container/)
* [SSH Protocols](/ssh-protocols/)
* [Capistrano](/ssh-capistrano/)