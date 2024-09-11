---
draft: false
title: "Configuration Tools"
aliases: ["/container-configuration/", "/docker-configuration/"]
seoindex: "index, follow"
seotitle: "Container Configuration"
seokeywords: "container configuration tools, container configuration, container setup, container layer settings, container settings, container preconfigurations, configuration tools, configure container, adjust container, container file manager, container logs, container ssh, ssh to container"
seodesc: "Configure variables, links, volumes, ports and run options for your Docker containers right through the platform dashboard. Learn how to manage the main Docker container settings with a bundle of supplementary tools like in-built file manager, logs tracking mechanism and SSH connection."
menu:
    docs:
        title: "Configuration Tools"
        url: "/container-configuration/"
        weight: 10
        parent: "container-configuration"
        identifier: "container-configuration.md"
---

# Container Configuration

The platform provides a possibility to manage all main aspects of containers lifecycle directly through a [dashboard](/dashboard-guide/). It supports a number of various tools, intended to help you to configure your environments:

* [settings wizard](#container-layer-settings-wizard)
* [embedded file manager](#configuration-file-manager)
* [log files](#log-files)
* [SSH access ](#ssh-access-to-container)


## Container Layer Settings Wizard

The platform integrated the special **Docker layer settings** dialog frame to the topology wizard to adjust some of the most commonly required container settings without the necessity to access it via SSH. Simultaneously powerful and user friendly, it gives you the ability to configure your containers in the most easy and comfortable way.

So, to start with, you need to access the above-mentioned frame. There are two ways this can be done through:

* *via topology wizard* - click on the **New Environment** button and [add the needed container(s)](/setting-up-environment/) or hit the **Change Environment Topology** button for the already created environment.
![topology wizard layer configuration](01-topology-wizard-layer-configuration.png)
Then choose a container that needs to be tuned and select the appropriate ***Configuration*** section at the bottom (circled in the image above).
{{%tip%}}**Tip:** With the platform, any container can be preconfigured even before being created - the necessary data is automatically fetched from image manifest upon accessing the configuration wizard.{{%/tip%}}

* *directly from the dashboard* - hover over your environment layer, click on the gear icon and pick one of the quick access options from the expanded list
![dashboard layer settings](02-dashboard-layer-configurations.png)

After that, the **Docker layer settings** window will appear:

![layer settings window](03-layer-settings-window.png)

As you can see, it contains 5 separate sections with the next settings options (follow the appropriate guide below for the section you are interested in):

* [Variables](/container-variables/)
* [Links](/container-links/)
* [Volumes](/container-volumes/)
* [Ports](/container-ports/)
* [Run Config](/container-run-configuration/)


## Configuration File Manager

The in-built **[configuration file manager](/configuration-file-manager/)** is designed to manage the files inside your container (including the ones, that are available and/or exported by means of [Shared Storage Container](/data-storage-container/) functionality). The appropriate tab can be opened by clicking on the **Config** button next to the necessary node (or the whole layer):

![configuration file manager](04-configuration-file-manager.png)

It includes 4 main sections:

* ***Root*** (File Manager) - gives you an easy access to container local filesystem, where you can operate the comprised data and instance settings within the corresponding configuration files
* ***Mount Points*** - list of folders, that are physically stored on a remote node but can be used at a current container through [mounting the directories](/mount-points/) with required data
* ***Exports*** - list of folders, which are shared with other nodes, i.e. are [exported](/storage-exports/) to be available at the remote instances whilst being stored locally
* ***Favorites*** - commonly used files and folders to have a quick and simple access to (you can manually mark any custom ones as favorites)

{{%tip%}}**Tip:** In case the appropriate environment layer includes multiple same-type containers, you can easily switch between them directly inside the manager by choosing the required one within the corresponding drop-down list at the top pane (circled in the image above).{{%/tip%}}

In such a way file manager, allows to take the full control over container file system with no extra tools required. However, be aware of what you are modifying, as in case something will get broken, the changes you've applied couldn't be automatically reverted.


## Log Files

Another section of the platform dashboard, which may help you to manage your projects, is **Logs**. Here, the data on all aspects of your containers lifecycle is gathered, which may come in handy while troubleshooting and/or debugging your applications or services.

![node log manager](05-node-log-manager.png)

{{%tip%}}**Note:** The list of shown log files and directories depends on a particular [software stack](/software-stacks-versions/) and can vary.{{%/tip%}}

The log files inside a container are automatically rotated, so when any of them reaches the size of *50 MB*, it is automatically compressed and moved to the dedicated ***rotated_logs*** directory. To view such archives (if necessary), you need to enter the appropriate container [via SSH](/ssh-access/) and download them for examining locally. The compressed logs are stored for 7 days, after which they will be automatically removed, being considered as an obsolete data.


## SSH Access to Container

If you prefer to manage your containers via terminal, you can easily connect to any of them [via SSH](/ssh-access/), no matter whether has it the external IP address attached or not. Once connected, you get a true freedom for managing your instances through executing the necessary operations directly from your local machine.

In addition, the platform is supplied with the dedicated [CLI client](/cli/), which allows to handle the vast majority of operations, required for your applications lifecycle management, by means of a set of special scripts. Herewith, the structure of the commands this could be accomplished through is completely similar to the [platform API](https://www.virtuozzo.com/application-platform-api-docs/) hierarchy, so you can easily get used to the client.


## What's next?

* [Container Types](/container-types/)
* [Container Redeploy](/container-redeploy/)
* [Custom Container SSH Access](/custom-container-ssh-access/)
* [CLI Client](/cli/)