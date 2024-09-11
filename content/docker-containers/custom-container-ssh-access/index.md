---
draft: false
title: "Custom Container SSH Access"
aliases: ["/custom-container-ssh-access/", "/docker-ssh-access/"]
seoindex: "index, follow"
seotitle: "Custom Container SSH Access"
seokeywords: "container ssh access, custom container ssh, docker ssh access, ssh to container, container terminal, container command line, access container via terminal, container ssh"
seodesc: "Learn how to establish the SSH connection to custom container for performing any specific operations. Make any required configurations via command line with the full root access granted."
menu: 
    docs:
        title: "Custom Container SSH Access"
        url: "/custom-container-ssh-access/"
        weight: 70
        parent: "docker-containers"
        identifier: "custom-container-ssh-access.md"
---

# Custom Container SSH Access

Since custom containers don't have the embedded GUI for their management, the most common way to take the full control over such an instance is connecting to it under the SSH protocol and perform any desired operations inside using the corresponding terminal commands.

{{%tip%}}**Note:** With the PaaS, the majority of the required configurations can be performed directly through the dashboard without the necessity to use SSH, thanks to the following tools:

* [Container Configurations](/container-configuration/) - allows to customize the main container settings (like variables, volumes, linking, run options, opened ports, etc.)
* [Configuration Manager](/container-configuration/#configuration-file-manager) - provides the full root access to the container's file system, allowing to operate with all of the comprised files

In addition, you can leverage the platform-dedicated [CLI client](/cli/), which provides the advanced remote management for all types of environments and nodes and allows to automate your app's lifecycle via scripts.{{%/tip%}}

SSH connection to a container can be established in two ways:

* through the SSH Gateway as for any other environment. The flow will be the following:
    * [generate](/ssh-generate-key/) an SSH keypair
    * [add your public SSH key](/ssh-add-key/) to the dashboard
    * [access your account](/ssh-access/) via SSH protocol

* or, if you don't want to use SSH keys, you need to attach the [public IP](/public-ip/) address to the required node and perform the next steps:
    * open your **terminal** emulator
    * enter the ***ssh [username]@[hostname]*** string, where the **username** is your login, and hostname is the Public IP address (you receive these credentials via email everytime a new container is created or added to the environment)
    * specify the requested **password** (can be found in the email also)

Once you've entered your container, you can perform any required configurations, thanks to the full root permissions granted.

{{%tip%}}**Note:** If you've faced any problems during establishing the connection, check the firewall rules for your container and ensure it has the *openssh* server running.{{%/tip%}}


## Reset Password

In case you've forgotten your container's credentials or lost/deleted the appropriate email, you can restore them at any time - simply choose the **Reset password** option within the expandable ***Additional*** list (the gear icon) for the necessary node (or set of them):

![reset custom container password](01reset-pass-new.png)

As a result, you'll receive a new password via email and can use it for operating your container(s).


## What's next?

* [SSH Access](/ssh-gate/)
* [Custom Containers Deployment](/custom-containers-deployment/)
* [Container Configuration](/container-configuration/)
* [Container Redeploy](/container-redeploy/)
* [Public IP](/public-ip/)
