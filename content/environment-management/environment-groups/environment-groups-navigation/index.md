---
draft: false
title: "Navigation Across Groups"
aliases: "/environment-groups-navigation/"
seoindex: "index, follow"
seotitle: "Navigation Across Groups"
seokeywords: "cloud dashboard tags, env groups management, cloud environments ui labels, navigating cloud environment, labeling cloud environments, grouping cloud environments, cloud environment attach tags, cloud env groups"
seodesc: "Find out how to easily navigate between the multiple environment groups at the platform dashboard. Access a particular group through the attached tag to overview environments that belong to it."
menu: 
    docs:
        title: "Navigation Across Groups"
        url: "/environment-groups-navigation/"
        weight: 30
        parent: "environment-groups"
        identifier: "environment-groups-navigation.md"
---

# Navigation Across Environment Groups

Organizing applications into [environment groups](/environment-groups) allows to make your working process much more comfortable. This is achieved through setting special **Tags**, which are used for environment filtering and are displayed within the same-named column in the main user dashboard screen.

![environment tags](01.png)

You can switch and navigate between your environment groups with the following UI elements:

* [via the Tags column](#via-tags)<a href="#via-tags"></a>
* <a href="#via-env-groups" id="via-tags">via the Env Groups menu</a><a href="#via-env-groups"></a>

## Navigation via Tags

The **Tags** column lists all of the groups an environment belongs to - click on a particular tag in order to refer to the appropriate group.

![navigation via tags](02.png)

The required filtering will be applied automatically, whilst the selected group label will be displayed as a nesting element in the **Env Groups** navigation panel at the top.

![env groups navigation panel](03.png)

Herewith, the appropriate group name will be temporarily hidden within the **Tags** column (as you are inside already).

{{%tip%}}**Note:** In case the currently selected group contains further child items (i.e. [subgroups](/environment-groups-management#add-subgroup)), their list can viewed at the chosen group's [management menu](/environment-groups-management) within the top navigation panel.
![environment subgroups](04.png)
Just click on the string with such child group to open it.{{%/tip%}}

In order to cancel filtering and return back to the overall list of available <a id="via-env-groups"></a>environments, click on **Env Groups**.

## Navigation via Env Groups Panel

Upon expanding the main **Env Groups** menu at the top, you'll be shown the list of all environment groups within your account, including the comprised [subgroups](/environment-groups-management#add-subgroup) (if are any).

![env groups panel](05.png)

Clicking on a particular one will apply the corresponding filtering to your environment list.  
Additionally, here you are provided with two predefined sorting options which are based on the following parameters:

* **Shared with Me** - select this option to access the list of environments [shared](/share-environment) with your account
![shared environments](06.png)

{{%tip%}}**Note:** When hovering over **Shared with Me**, you'll see the list of collaboration owners you belong to; choosing a particular record here will display the environments that were shared to you by this person.
![shared with me](07.png)
And if selecting **Manage** at this submenu bottom, the **Account settings &gt; [Shared with Me](/share-environment#mng)** tab will be opened.{{%/tip%}}

* **Region** - use this option to filter environments based on the list of [environment regions](/environment-regions), available for your account
![environment regions](08.png)

Now, when you know how to easily navigate between different environment groups, check some additional possibilities provided for [group management](/environment-groups-management) at the platform dashboard.


## What's next?
* [Environment Groups Overview](/environment-groups/)
* [Environment Groups Managemen](/environment-groups-management/)
* [Environment Collaboration](/share-environment/)
* [Environment Regions](/environment-regions/)
