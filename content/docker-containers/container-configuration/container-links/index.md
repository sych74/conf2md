---
draft: false
title: "Links"
aliases: ["/container-links/", "/docker-links/"]
seoindex: "index, follow"
seotitle: "Linking for Containers"
seokeywords: "link containers, configure container linking, containers linking, configure containers, link container layers, containers interaction, container settings links, container links"
seodesc: "Find out how to link a pair of containers within a single environment. The embedded GUI tool in a form of configurations wizard will help you to perform this just in a few clicks."
menu: 
    docs:
        title: "Links"
        url: "/container-links/"
        weight: 30
        parent: "container-configuration"
        identifier: "container-links.md"
---

# Links

The **Links** section is intended to establish connection between the containers placed at different layers of a single environment.

After such connection is set, a container will be able to work with [environment variables](/container-variables) of the linked image (herewith, the imported properties can be recognized by a specified prefix). Below, we'll provide a step-by-step example of containers linking.

1\. Click the **Add** button and fill in the appeared fields:

* **Node** - select the required layer of the current environment using the drop-down list
* **Alias** - type a connection alias (*LB* in our case). Subsequently, it will be used as a prefix for the variables imported to the current container(s) from the layer chosen in previous field

![add linking layer settings](01-add-linking-layer-settings.png)

{{%tip%}}**Tip:** Upon linking containers, the platform also adds the corresponding DNS record (with the name identical to the used alias) to the platform DB. In such a way, you can refer to a particular container from inside of these two environment layers not just over its IP address or *NodeID*, but also specifying the assigned alias with counter, i.e. <i>{alias_name}_**N**</i>.

*For example*, after linking with *DB* alias, you can ping specific containers at the appropriate layer as &ldquo;*db_1*&rdquo;, &ldquo;*db_2*&rdquo;, etc while working with platform internal network via [SSH Gateway](/ssh-overview). Herewith, if using common layer alias (i.e. without counter, &ldquo;*db*&rdquo; in our case), the system will use Round-Robin algorithm to choose any container within the defined node group.{{%/tip%}}

2\. After that click **Save** to confirm linking settings. You can link as many different node groups to a single layer as you require.

{{%tip%}}**Note:** 
* all the stated connections will take effect only after selecting the **Apply** buttons for this frame and, if needed, for the whole topology wizard
* **be aware** that the linked nodes <u>will be restarted</u> for the new settings to be applied (causing a short downtime of the involved containers)
{{%/tip%}}

3\. You always can **Edit** or **Remove** the unnecessary link with the corresponding buttons at the top pane of the *Docker layer settings* frame.

![edit remove layer settings](02--edit-remove-linking-layer-settings.png)

When updates are applied, you can check the results by switching to the *[Variables](/container-variables)* section (where the newly imported parameters will be listed).


## What's next?

* [Container Configuration](/container-configuration/)
* [Variables](/container-variables/)
* [Volumes](/container-volumes/)
* [Ports](/container-ports/)
* [Run Config](/container-run-configuration/)