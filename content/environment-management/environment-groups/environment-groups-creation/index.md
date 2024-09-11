---
draft: false
title: "Group Creation"
aliases: "/environment-groups-creation/"
seoindex: "index, follow"
seotitle: "Environment Groups Creation"
seokeywords: "label cloud environments by tags, cloud environments ui labels, attach tags to environment, cloud environment dashboard tags, cloud environment dashboard layout, attach tags to cloud environment, grouping cloud environments, env groups creation, cloud environment dashboard labels"
seodesc: "Learn how to create environment groups through attaching tags to environments at the dashboard. Use new groups to organize existing environments and to simplify your work."
menu:
    docs:
        title: "Group Creation"
        url: "/environment-groups-creation/"
        weight: 20
        parent: "environment-groups"
        identifier: "environment-groups-creation.md"
---

# How to Create Environment Group

Setting new [environment group](/environment-groups/) involves creation of a special tag, that subsequently can be attached to the required environment to logically mark it within the dashboard. You can use any naming paradigm that would be convenient for you - for example, if having *development*, *testing*, and *production* versions of a project, you can apply such tags to the corresponding environments to easily separate them.

So, to quickly create an environment group with only a few minutes notice, follow the next steps.

1\. Open your platform dashboard and click the **"+" (Create New)** button within the ***Env Groups*** panel at the top.

![create new group button](01.png)

{{%tip%}}**Tip:** Alternatively, you can access the same option via the expandable **Env Groups** menu:

* select the **Create New** point

![create new group menu](02.png)

* choose **Manage** and click on the **Add** button within the opened frame

![add environment group](03.png){{%/tip%}}

2\. The appropriate ***Add Group*** dialog box will be opened.

![add group dialog](04.png)

Specify the following data in order to create a new group:

* **Name** - type a name for your group (any letters, numbers and special characters can be used including space)
* **Parent Group** - optionally, specify nesting for the currently created group to be included to another one as a [subgroup](/environment-groups-management/#add-subgroups)
* **Environments** - select environments that should belong to the group (shared environments cannot be added to your personal groups); also, it is possible to create an empty group and [fill it up with environments](/environment-groups-management/#assign-group-to-environment) later on

{{%tip%}}**Tip:** To enhance visual recognition of groups within the dashboard, you can assign different color to each of them by clicking the circled button near group name.

![group associated color](05.png){{%/tip%}}

Once you are finished, click **Add**.

3\. The newly created group will be automatically selected and displayed as a new element on the top **Env Groups** navigation panel. The list of shown environments will be also filtered correspondingly.

![new environment group created](06.png)

Additionally, learn the ways you can [manage your environment groups](/environment-groups-management/) and quickly [navigate between them](/environment-groups-navigation/) within dashboard.


## What's next?

* [Environment Groups Overview](/environment-groups/)
* [Environment Groups Navigation](/environment-groups-navigation/)
* [Environment Groups Management](/environment-groups-management/)
* [Environment Isolation](/environment-isolation/)