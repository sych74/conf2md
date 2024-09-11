---
draft: false
title: "Collaboration User Experience"
aliases: ["/collaboration-user-experience/", "/collaboration-environments/", "/collaboration-environments-deprecated/"]
seoindex: "index, follow"
seotitle: "Collaboration User Experience"
seokeywords: "collaboration, account collaboration, share environments, collaboration user experience, collaboration management, working in collaboration, manage shared environments"
seodesc: "Learn the specifics of working with shared environments. Check allowed actions, view other collaborator tasks, and create environments and packages at another account."
menu:
    docs:
        title: "Collaboration User Experience"
        url: "/collaboration-user-experience/"
        weight: 40
        parent: "accounts-collaboration"
        identifier: "collaboration-user-experience.md"
---

# Collaboration User Experience

Once the [collaboration is established](/collaboration-create/), its members can start working with shared environments. In this guide, we'll go through all the peculiarities of the process.

1\. The shared environments can be easily distinguished from the regular ones via the dedicated icon and owner tag.

![shared environment](01-shared-environment.png)

2\. You can click the owner name label in the **Tags** column to quickly filter shared environments by *primary* account.

![environments filtered by owner](02-environments-filtered-by-owner.png)

3\. At the **[Env Groups](/environment-groups/) > Shared with Me** tab, you can see the complete list of shared environments and groups.

![shared environment groups](03-shared-environment-groups.png)

{{%note%}}**Note:** You cannot add shared environments to your personal groups.{{%/note%}}

Also, the whole groups' tree can be seen when managing environment groups.

![managing environment groups](04-managing-environment-groups.png)

4\. The management process for shared environments is the same as for regular ones. However, the primary account owner may restrict some of the options.

![restricted action for shared environment](05-restricted-action-for-shared-environment.png)

You can check the [role and list of allowed policies](/collaboration-roles-policies/) for shared resources at the account **Settings > Shared with Me** section.

![shared roles and policies](06-shared-roles-and-policies.png)

{{%tip%}}**Tip:** You can check roles for the specific [shared environment](/share-environment/) by going to the **Settings > Collaboration** section.

![environment collaboration settings](07-environment-collaboration-settings.png)

By default, collaboration members can see only themselves and cannot manage rights. However, such a possibility can be shared by the environment owner through the role with the  *Collaboration* policy.{{%/tip%}}

5\. The **Tasks** manager keeps track of all the actions performed with the shared environments and provides a custom icon for operations initiated by other accounts. Hover over this icon to view the email of the corresponding collaboration member.

![collaboration actions in tasks](08-collaboration-actions-in-tasks.png)

6\. If provided with the ability to create environments, you'll see the ***Environment Owner*** selection dialog after clicking the **New Environment** button at the top of the dashboard.

![select new environment owner](09-select-new-environment-owner.png)

Here, you can select an account and group to create your environment.

{{%tip%}}**Tip:** If you have permission to install packages from the [Marketplace](/marketplace/), the ***Owner*** field will be added to the installation window.

![marketplace package owner](10-marketplace-package-owner.png)
{{%/tip%}}

The limitations of the selected owner are automatically applied to the topology wizard or installation window (for [imported](/environment-import/) and Marketplace packages).

![environment owner in wizard](11-environment-owner-in-wizard.png)

{{%note%}}**Notes:**

- By default, collaboration members cannot see the pricing information, and only resource data is provided in the topology wizard (as it is shown in the image above). However, the environment owner can share this possibility through the *Cost Estimation / Billing History* policy.
- Collaborators receive email notifications about actions (load alerts, auto-scaling, password reset, etc.) they initiated but not about actions taken by other collaborators or an account owner.
{{%/note%}}

When creating on behalf of a different account, the topology wizard shows the appropriate environment owner at the bottom-left corner.


## What's next?

- [Collaboration Overview](/account-collaboration/)
- [Collaboration Roles & Policies](/collaboration-roles-policies/)
- [Create Collaboration](/collaboration-create/)
- [Share Environment](/share-environment/)