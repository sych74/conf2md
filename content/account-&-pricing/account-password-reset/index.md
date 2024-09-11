---
draft: false
title: "Account Password Reset"
aliases: "/account-password-reset/"
seoindex: "index, follow"
seotitle: "Account Password Reset"
seokeywords: "password, password reset, account password reset, paas password reset, password recovery, reset password, restore password, change password, update password, password requirements"
seodesc: "Detailed overview of the password requirements, password change, and password reset flows for your platform account."
menu:
    docs:
        title: "Account Password Reset"
        url: "/account-password-reset/"
        weight: 35
        parent: "account-&-pricing"
        identifier: "account-password-reset.md"
---

# Account Password Reset

The platform makes sure that account passwords are regularly updated through the automatic deprecation mechanism. By default, passwords expire after 180 days (with several heads-up notifications) and need to be renewed to restore access to the account.

If you still retain access to your account, follow the [change password](#change-password) flow. If you've forgotten your current password or it has already expired, the platform provides a reliable and secure flow to [reset your password](#reset-password).


## Password Requirements

User accounts security is the top priority for the platform, so the following password requirements are enforced by default:

- the minimum length of 10 characters
- at least one symbol for each of the following categories: numbers, lowercase and uppercase letters, special characters
- must not repeat any of the previous passwords

![password requirements](01-password-requirements.png)

{{%note%}}**Note:** The exact requirements for each platform are defined by the appropriate service hosting providers and can vary from the default ones.{{%/note%}}


Also, we recommend configuring **[Two-Factor Authentication](/two-factor-authentication/)** for an additional layer of protection to drastically increase the account's security.


## Change Password

In order to update your PaaS account password, log in to the appropriate platform dashboard, and follow the steps below.

1\. Click on the menu with your login in the upper-right corner and choose the **Change Password** option.

![change password button](02-change-password-button.png)

2\. In the opened frame, fill in the fields with your current and new passwords and click the Change Password button.

![change password dialog](03-change-password-dialog.png)

In a moment, you'll be notified about operation success and receive the appropriate email as well.


## Reset Password

If you've lost access to your account, you can follow the password reset procedure to restore it.

1\. Go to the appropriate PaaS installation login page and select the **Reset Password** option from the list at the bottom-left corner of the form.

![account password reset](04-account-password-reset.png)

2\. Within the opened frame, you need to provide the email address of your account.

![email address for password reset](05-email-address-for-password-reset.png)

Click **Reset** for the platform to send you a link for password restoration.

3\. Check your inbox for the ***Confirm Account Password Reset*** email.

![password reset email](06-password-reset-email.png)

Click the **Reset Password** button to proceed with the operation.

{{%note%}}**Note:** For security reasons, the link remains valid for a short period only. If used after invalidation, the following message will be displayed.

![password reset expired](07-password-reset-expired.png)
{{%/note%}}

4\. In the opened form, you can set up a new password.

![account password reset form](08-account-password-reset-form.png)

That's all! You'll be redirected back to the dashboard, where you can log in using the new credentials.

![password changed](09-password-changed.png)

{{%tip%}}**Tip:** Also, you'll receive an email about the success of the password reset operation.

![password changed email](10-password-changed-email.png)
{{%/tip%}}


## What's next?

* [Account Registration](/account/)
* [Account Types](/types-of-accounts/)
* [Account Statuses](/account-statuses/)
* [Two-Factor Authentication](/two-factor-authentication/)
* [Personal Access Tokens](/personal-access-tokens/)
* [Accounts Collaboration](/account-collaboration/)