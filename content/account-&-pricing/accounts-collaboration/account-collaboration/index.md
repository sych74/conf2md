---
draft: false
title: "Account Collaboration"
aliases: ["/account-collaboration/", "/account-collaboration-deprecated/"]
seoindex: "index, follow"
seotitle: "Account Collaboration Overview"
seokeywords: "collaboration, account collaboration, share environments, collaboration overview, primary account, collaboration members"
seodesc: "Organize interaction between all team members with the account collaboration feature that allows you to share environments."
menu: 
    docs:
        title: "Collaboration Overview"
        url: "/account-collaboration/"
        weight: 10
        parent: "accounts-collaboration"
        identifier: "account-collaboration.md"
---

# Account Collaboration

Every large project is a result of the joint effort of multiple people. However, different team members working in a single account is not an efficient workflow that can cause numerous problems (including security issues). The platform provides a reliable ***account collaboration*** feature that greatly facilitates joint development and management, ensuring successful and efficient collaboration.

The core idea is pretty straightforward - one user (*primary account*) hosts all the necessary environments and can share required components with required permissions to others (*collaboration members*). The most distinct benefits of the process are efficient resource utilization and extreme management flexibility. There is no need to create environment duplicates for different members - the platform's collaboration allows sharing required instances to as many users as needed. Complete control over the shared management permissions makes the feature suitable for most of the existing use cases.

![account collaboration scheme](01-account-collaboration-scheme.png)

The **primary account** has full access to all hosted environments regardless of whether they are shared or not (including ones created by collaboration members). It is responsible for managing collaboration and its members - inviting users, adjusting shared components, specifying [roles and permissions](/collaboration-roles-policies/), etc. However, be aware that all charges for the shared environments (including actions performed by collaborators) are applied to this account.

**Collaboration members** are accounts that have accepted a collaboration invite from the *primary account*. The members are not charged for the shared environments and can work with them just as with regular ones. However, the list of allowed actions is defined and managed by the primary account (or other collaborators with the appropriate permission).

If provided with sufficient permissions, a member can create new environments on the primary collaboration account. In such a case, limitations ([quotas](/quotas-system/)) of the primary account will be considered, allowing to bypass any restrictions of the member's account. Once again, all charges for the environment usage will be applied to the primary account.

{{%note%}}**Note:** After leaving the collaboration, the member will no longer have access to any shared environments on the primary account, including ones created by them.{{%/note%}}


## What's next?

- [Collaboration Roles & Policies](/collaboration-roles-policies/)
- [Create Collaboration](/collaboration-create/)
- [Collaboration User Experience](/collaboration-user-experience/)
- [Share Environment](/share-environment/)