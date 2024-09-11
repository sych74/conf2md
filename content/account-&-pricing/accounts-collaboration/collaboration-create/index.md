---
draft: false
title: "Create Collaboration"
aliases: ["/collaboration-create/", "/collaboration-management/", "/collaboration-create-deprecated/", "/collaboration-management-deprecated/"]
seoindex: "index, follow"
seotitle: "Create Collaboration"
seokeywords: "collaboration, account collaboration, share environments, create collaboration, invite collaboration members, accept collaboration invite, manage collaboration"
seodesc: "Find out how you can share your environments with other accounts on the platform. Follow the steps to send and accept collaboration invites."
menu: 
    docs:
        title: "Create Collaboration"
        url: "/collaboration-create/"
        weight: 30
        parent: "accounts-collaboration"
        identifier: "collaboration-create.md"
---

# Create Collaboration

In order to create your own [collaboration](/account-collaboration/), you just need a billing PaaS account (**primary account**) that will invite additional customers/users (**collaboration members**). You can perform most collaboration-related operations via the dedicated section at the account settings panel.

Click the **Settings** button in the top-right corner of the dashboard.

![account settings button](01-account-settings-button.png)

Within the opened **User Settings** sections, you have the following two collaboration sub-sections:

- ***Shared by Me*** - collaboration options for the primary account, it has three tabs:
  - **Members** - manages a list of collaboration members (invite new users, suspend or remove existing ones, customize shared environments, groups, roles, etc.)
  - **Roles** - configures custom roles (list of allowed actions) from the available policies
  - **Policies** - lists the actions that can be added to a role
- ***Shared with Me*** - options for the collaboration members

![collaboration menu](02-collaboration-menu.png)

Now, follow the instructions below to set up a collaboration:

- [sent collaboration invite](#send-collaboration-invite) (as primary account)
- [accept collaboration invite](#accept-collaboration-invite) (as collaboration member)


## Send Collaboration Invite

Go to the account **Shared by Me** section on the *primary* account (the one where environments are actually hosted).

1\. If you haven't before, create at least one ***Role*** at the appropriate tab.

Provide the following information within the ***Add Role*** dialog:

- **Name** - type any desired name for a role
- **Description** - provide custom description (optional)
- **Policies** - select actions allowed for a role; use *search* to quickly locate required actions and *filter* to review only selected ones
- **Receive Load Alerts Notifications** - enable to allow collaboration members with this role to receive load alert notifications about shared items

![add collaboration role](03-add-collaboration-role.png)

You can learn more about **[Roles & Policies](/collaboration-roles-policies/)** at the dedicated guide.

2\. On the ***Members*** tab, click the **Invite** button.

Fill in the fields of the opened ***Invite Member*** dialog:

- **Email** - type in the address of the user you want to invite
- **Display Name** - provide a custom name for the invited user (optional)
- **Shared Items** - select separate items and categories (environments and groups) that you want to share with the member

![invite collaboration member](04-invite-collaboration-member.png)

{{%tip%}}**Tips:**

- you can assign several roles for a component - use **Ctrl** to select multiple options and **Alt** to replace all selected roles
- you can provide different roles for each (sub-)component
- hover over a role in the list to see a hint with all included policies
- if needed, you can ***Create New Role*** without closing the invite form
- you can manage [environment group](/environment-groups/) structure directly in the invite form - hover over the group and click the *gear* icon to select the required option (**Add**, **Edit**, **Remove**)
- to provide an ability to create environments at the account root (i.e. without any group), share the whole *Environments* category with a role that grants the appropriate permission
- if you need to [share a single environment](/share-environment/), it can be done from the appropriate environment configs
{{%/tip%}}

3\. The invited member will appear in the list in the ***pending acceptance*** state.

![collaboration pending acceptance](05-collaboration-pending-acceptance.png)

Now, you wait for the member to [accept the invitation](#accept-collaboration-invite). Any change to the invitation will be displayed at the **Members** tab. Also, you'll get the appropriate email notification about the user's decision.

4\. If needed, you can select a collaboration member to perform the necessary adjustments:

- **Edit** - to change shared components and permissions at any time
{{%note%}}**Note:** If a collaboration member was logged in during the adjustments, they might need to refresh the dashboard to view new shared possibilities.{{%/note%}}
- **Copy** - to share the same permissions with another user
- **Suspend / Activate** - to temporarily stop / restore sharing
- **Remove** - to terminate sharing and delete info about shared components and permissions

![manage collaboration member](06-manage-collaboration-member.png)

{{%tip%}}**Tip:** For convenience, terminated collaborations (including the case of members leaving on their own) are not removed entirely. The remaining record allows you to re-activate collaboration if necessary.

![re-invite collaboration member](07-re-invite-collaboration-member.png)
{{%/tip%}}


## Accept Collaboration Invite

Wait for the primary account to [send a collaboration invite](#send-collaboration-invite) for you.

1\. Check your email inbox for the invite. It should look as follows:

![collaboration invite email](08-collaboration-invite-email.png)

If interested, click the **View Invitation** button.

{{%note%}}**Note:** If not registered at the platform, the account for the current email address will be created automatically.{{%/note%}}

2\. After confirming via email, you will be redirected to the platform dashboard. Here, you'll see a dialog window that provides options to accept or reject the invitation.

![join collaboration dialog](09-join-collaboration-dialog.png)

You can close the dialog or cancel the operation to process it later at the account **Settings > Shared with Me** section.

![accept collaboration invite](10-accept-collaboration-invite.png)

3\. Once accepted, the member's dashboard will get and display new shared items.

![added to collaboration notification](11-added-to-collaboration-notification.png)

That's it! All shared items are now available to the collaboration member (with defined permissions).

![shared environment](12-shared-environment.png)

Check out the **[Collaboration User Experience](/collaboration-user-experience/)** guide to check the specifics of working in collaboration.


## What's next?

- [Collaboration Overview](/account-collaboration/)
- [Collaboration Roles & Policies](/collaboration-roles-policies/)
- [Collaboration User Experience](/collaboration-user-experience/)
- [Share Environment](/share-environment/)