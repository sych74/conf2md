---
draft: false
title: "Share Environment"
aliases: ["/share-environment/", "/share-environment-deprecated/"]
seoindex: "index, follow"
seotitle: "Share Environment"
seokeywords: "collaboration, account collaboration, share environments, environment direct access, direct sharing, environment collaboration settings, environment collaboration roles, environment access level"
seodesc: "See how to share a specific environment directly. Manage roles assigned to environments, view permissions, access level, and collaboration status."
menu: 
    docs:
        title: "Share Environment"
        url: "/share-environment/"
        weight: 20
        parent: "environment-management"
        identifier: "share-environment.md"
---

# Share Environment

**Environment Sharing** is a particular case of the [account collaboration](/account-collaboration/) feature - when you want to give access or some functionality of your account to other users. The only difference is that you need to share just a single environment.

Check a quick summary of the feature for better understanding:

- environment *owner* has complete control over the environment
- *collaborators* can only perform actions allowed by the *owner* (through the assigned [roles](/collaboration-roles-policies/))
- only the *owner* is charged for the shared environment

In order to share an environment, select it and go to the **Settings > Collaboration** tab. Here, you can see a list of all existing collaborators (if any) that have access to the current environment.

![environment collaboration settings](01-environment-collaboration-settings.png)

{{%tip%}}**Tip:** When accessing this tab as a collaborator, you can only check your own role for the current shared environment. However, the environment owner can share access and management possibilities through the *Collaboration* policy (cannot edit own roles).

![shared environment collaboration settings](02-shared-environment-collaboration-settings.png)
{{%/tip%}}

1\. The table provides detailed information on access to the current environment. You can find all the required data in the following four columns:

- **Name** - lists emails of collaboration members that have access to the environment. Hover over to see the current member's management options (*Edit* or *Remove* direct access).
- **Roles** - shows the exact access roles for the current environment per collaborator. Hover over for the combined list of policies from all roles.

![policies for all roles](03-policies-for-all-roles.png)

- **Access Level** - shows the highest access level for the current environment. Hover over for more details. Information on the [access level algorithm](/collaboration-roles-policies/#roles-assigning-algorithm) can be found upon hovering over the column header.

![collaboration access level](04-collaboration-access-level.png)

- **Status** - provides the collaboration status of the member (*active*, *pending acceptance*, *left*, *suspended*). The icon color at the start of each record also represents status.

2\. Click the **Add** button at the top of the tools panel to provide <u>*direct*</u> access to the environment. Here, you need to provide the following data:

- ***Member*** - select an existing collaboration member or click the **Invite Member** option to provide email addresses
- ***Roles*** - choose at least one role from the list (if needed, click the **Create New Role** option to add a new one)

![environment direct access dialog](05-environment-direct-access-dialog.png)

{{%tip%}}**Tip:** When inviting a new member, the flow is similar to the one described in the **[Create Collaboration](/collaboration-create/)** guide. The user receives an invitation email and can accept or reject it.

![direct access for new user](06-direct-access-for-new-user.png)
{{%/tip%}}

3\. You can select an existing record in the list to **Edit** assigned <u>*direct*</u> roles or **Remove** <u>*direct*</u> direct access to the current environment.

![manage direct access](07-manage-direct-access.png)

{{%note%}}**Note:** After removing direct access, the environment can still be available for the member through other access types, e.g. if the environment belongs to the shared group.{{%/note%}}

You can click the **Account Collaboration** button (displayed for the environment owner only) at the top-right of the tools panel to go to the **User Settings > Collaboration > Shared by Me** section and perform more complex customizations.


## What's next?

- [Collaboration Overview](/account-collaboration/)
- [Collaboration Roles & Policies](/collaboration-roles-policies/)
- [Create Collaboration](/collaboration-create/)
- [Collaboration User Experience](/collaboration-user-experience/)