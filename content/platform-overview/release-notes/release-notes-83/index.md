---
draft: false
title: "Release Notes 8.3"
aliases: "/release-notes-83/"
seoindex: "index, follow"
seotitle: "Release Notes 8.3"
seokeywords: "paas, paas release notes, paas version, 8.3 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the Virtuozzo PaaS 8.3 release."
menu:
    docs:
        title: "Release Notes 8.3"
        url: "/release-notes-83/"
        weight: 29
        parent: "release-notes"
        identifier: "release-notes-83.md"
---

<a id="back"></a>

# Virtuozzo Application Platform 8.3

*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included to the **Virtuozzo PaaS 8.3** release.

{{%rn-new%}}
{{%rn-item url="#almalinux-9-base-os-image"%}}
## AlmaLinux 9 Base OS Image
Started a gradual process of transitioning certified software stacks to the *AlmaLinux 9* based images
{{%/rn-item%}}

{{%rn-item url="#subscription-improvements"%}}
## Subscription Improvements
Implemented new features for the subscription solution, including subscription update, migration, and disabling/enabling the *Auto Pay* option
{{%/rn-item%}}
{{%/rn-new%}}

{{%rn-changed%}}
{{%rn-item url="#action-initiator-for-emails"%}}
## Action Initiator for Emails
Extended the collaboration email notifications with the “*action initiator*” data to help with account activity tracking
{{%/rn-item%}}

{{%rn-item url="#api-changes"%}}
## API Changes
Listed all the changes to the public platform API in the current release
{{%/rn-item%}}

{{%rn-item url="#software-stack-versions"%}}
## Software Stack Versions
Actualized list of supported OS templates and software stack versions
{{%/rn-item%}}
{{%/rn-changed%}}

{{%rn-fixed%}}
{{%rn-item url="#fixes-compatible-with-prior-versions"%}}
## Fixes Compatible with Prior Versions
Bug fixes implemented in the current release and integrated into the previous platform versions through the appropriate patches
{{%/rn-item%}}

{{%rn-item url="#bug-fixes"%}}
## Bug Fixes
List of fixes applied to the platform starting from the current release
{{%/rn-item%}}
{{%/rn-fixed%}}

<style><!--
.changes-container{position:relative;padding-top:30px;padding-bottom:10px;padding-left:120px;border-top:1px solid #ddd}.changes-container:first-child{padding-top:0}.changes-container:first-child:before{top:15px}.changes-container:before{font-size:22px;position:absolute;top:45px;left:5px;width:110px;padding-top:42px;text-align:center;background-repeat:no-repeat;background-position:top}.changes-container>div{line-height:1.9;overflow:auto;margin-bottom:10px;padding:14px 20px;color:#282828;border-radius:3px}.changes-container>div:after{display:table;clear:both;content:""}.changes-container>div h6{font-size:18px;margin:0 0 16px}.changes-container>div .changes-more{position:relative;float:right;text-decoration:none}.changes-container>div .changes-more:after{margin-left:5px;content:">>"}.changes-container.changes-container--new:before{content:"New";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDozOEQ2OURDQjJDNDUxMUU4OEFDM0Q0OUYzRjVDQTUwMiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDozOEQ2OURDQzJDNDUxMUU4OEFDM0Q0OUYzRjVDQTUwMiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjM4RDY5REM5MkM0NTExRTg4QUMzRDQ5RjNGNUNBNTAyIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjM4RDY5RENBMkM0NTExRTg4QUMzRDQ5RjNGNUNBNTAyIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+NUw/0AAAAnNJREFUeNrMmE1oE0EYhjdLIz1IBDG1JdRqEdGCYPojqQgeWjA5xDYHpWBKPYhQaE+lLZTeTBHEq/bkpTUIIil6Mf6c0lLxUigShd6CBrTWHtQWD9L0/ei3MAzJmp2dDXnhgQy7M/Nmfr75Zn3Gq0eGBvnAGRAHN8A5cBj8Ae/AM/AG/JQrlqKjVXXQoMHkZfAcHC/zjMwOMqQX4DbYctqJ6cLgIbAEliuYLKcB8AMMOe1MdUQbwTpPt4qegtMg5eWIUp0VFyYt3QXDXhqdAl2GHi34svPNOozSbm4FvaAbnAf3DL16ArOu1miEd2mT4a36AI3qN5URTYL3NTBpaVBl6lvAolFbDasYnTVqr0tYp0G7tVrO6B2PzPwFWZvnm+A7zCaA+T+jPk3HqqwtXu8xGj2b9+idDPgMs012Rkv8z3RqF5wFv7mcr6IOHSZFmD1ZyWiIzerSPzYpZk3jDo73jzDbKBuluPnVQYJRjcLgi7S7Uw7qU/b1+GBNHuSjJ0BB85RfATmh3A/eKrYVNHkD5RQqU6d+cARsSM+uS22GXZgkXSOjPaBNofJ9XoO/QKewCcc4kbbUDtZczk7S5IxbRSPC7x2+ftBh8VAKN3kNy6iLjCZU/yWYEMrbYE4oBygecpLtVgEyesxFAw/AzQo3gE/gqKaNWTSl8KGUT3KqZsnPmVdIYwTJkNHXGhqiK/Ekx0naOBc0h7o0xdEIj0C9atuKox80TL+Xipeio3smn+2xOjVJsXpVPOvz/HGgnkSXyGnrk4+YlLwEHR6c+U61ybfeGfG7lJwkU4A+BS6CW+Aql71WgT8PpSlq0JqUX9gXYACycXnWqP0g9wAAAABJRU5ErkJggg==)}.changes-container.changes-container--new>div{background-color:#e4ffee}.changes-container.changes-container--changed:before{content:"Changed";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0QzNGRThBNjJDNDUxMUU4QTcyREYwOUUwQ0JFM0M4QiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0QzNGRThBNzJDNDUxMUU4QTcyREYwOUUwQ0JFM0M4QiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjRDM0ZFOEE0MkM0NTExRThBNzJERjA5RTBDQkUzQzhCIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjRDM0ZFOEE1MkM0NTExRThBNzJERjA5RTBDQkUzQzhCIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+c2zvogAAAidJREFUeNrUmM0rBVEYxueOmywuWfj+VlIkFje6ZEeJ8rURRVnIn0DJjlL+BxuSkogiiQ0iCwpJ3boLX/nOggXJx/PqvTVNXWbeOXO7nvot7rlnznnmzHnnfc94tOUPTYE8oBg0gw5QAnzgBayDWbAGHs0XfjXpFidwbrQWzIF0C30XQR94sGtUd2AwHiyALYsmSa3gHnTancwrNJkADvlxSzQDisCo1QskK0rXbDswGdYI6HHT6ADwa2o06Vn5zFARTBTNOcw7eANHmlptgPq/guq3PRrgKE3T3FUdoFW9kTz6brAbBZNhtUn2aCaY0qKrHonRYS36qkFQpQJbRvsdTBgCWUzI5rV34BZm24H+l1GPgyQQBGXgminjNjuimJgHpzCb9pvRL74zickK8Gpoe+W2oGA8SiZXMFsQyWg2m7WjfVBuMmk0W859JOn9GGYTzEbpvXlpo8AIm6zmRBBJb9xHYpZKxQljZsoDZ4KBErnmtDrps3D/p+ocQJvCAXwu9TWrhYxWgnzhABTdT+A8Qo3Zyf89cV+pur1ccTtRMuOLsIq5ChKCn1a0XYt9JZHRlH9g9IqMXigaLM5im0TzZHRV0WBdpveyzm0qNE3v0QDXnrEqOlqn013vKXz8bqgVx5Sfcopye2OMmhwHO8Zcf8IfB2JJY2AwfOgzbv4lUCrM+Sp1x0XMkPFkai6ST0EhqAK9oIF/u60z/jw0DQ5oT5o7fAswAKxgepYzbixFAAAAAElFTkSuQmCC)}.changes-container.changes-container--changed>div{background-color:#def6ff}.changes-container.changes-container--fixed:before{content:"Fixed";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpEM0FFMDgwQzJDNDUxMUU4Qjk2NUQ1RjM3QjZEQTIwQyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpEM0FFMDgwRDJDNDUxMUU4Qjk2NUQ1RjM3QjZEQTIwQyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkQzQUUwODBBMkM0NTExRThCOTY1RDVGMzdCNkRBMjBDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkQzQUUwODBCMkM0NTExRThCOTY1RDVGMzdCNkRBMjBDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+p2cxQAAAAm5JREFUeNrMmN1LFFEYxmeHTfdChWRdM+xDEiG7XJQtRCKFKNDdINTCBS+68E5CUBDxpiDqIugP6MaPShHDuihCbyoUb4K09NpsQfy4KQ1M3fV5l3dgmMbdmXPObPvAD+brnHnmPfOe8874Uq98mgJRJzWgBbSBi6AI7IAZMAE+gO1/WrYnHd3Ar8BkA5gE5TbnyGyMIU2De2DL7U10CYMF4DX4dIxJO0XBJuhwezPRiAbAVx5uEb0E1eChlxGlNp8lTBp6AOJeGu0DYU2NhrVx/ZSjbM2S9XSyktkHe2BRU6tZ0Jwt+zO9oxHO0pDmrZoARXVdZOg7wXwOTBqKibyjFWBEwc0PwDL45eDauIjRQUmDf8BVUAgugUYHba4gqcqAq2Tal1yxKPESvE1Gv7louwG607nRnkxmiqhP0uRjk8kClyY1zokpsILohjIZTfFTiWrUtP0XzFleiTN8PJtq0g88rp8/zuhpcChhdNeyfwe8ZZMXwE+uqJwu70swG7AajfCwVUgYDVj2f4BWUMzz5AlQ6qI/qr6em42e5XlTRjfT75a9jMS4LdDvXUQ1qHMCfVRg8l2Wa+rAC8H+W/3cwTkPTF4Dv8FJ0MPXiarTzxW3apODXMapUpiG/pbE+mxnckixSVIJRTQouExO2xx/Cu57ULQkKKJrAg39nIS5MEmaIqPvBT/senlepOLjmYcmSWNUlEQUzKFeij6tyymiC4LDnytFqZLSuRC5kacmnxiFjbGEfuefA/mkR6Df+OgzFyVvQC1Y/c8Gqcy8DAbMX6bWIpmKiipQD7rAdd73Wqv8e2gMfLFW96QjAQYAvVZ8VxrR76cAAAAASUVORK5CYII=)}.changes-container.changes-container--fixed>div{background-color:#fef6e6}@media (max-width:479px){.changes-container{padding-top:80px!important;padding-right:10px;padding-left:10px}.changes-container:first-child:before{top:25px}.changes-container:last-child{margin-bottom:0!important}.changes-container:last-child:after{display:none!important}.changes-container:before{top:25px;left:auto;width:auto;margin-left:0;padding-top:6px;padding-left:55px;background-position:0 0}.changes-container.changes-container--changed,.changes-container.changes-container--fixed,.changes-container.changes-container--new{position:relative;margin-bottom:40px;border-bottom:0}.changes-container.changes-container--changed:after,.changes-container.changes-container--fixed:after,.changes-container.changes-container--new:after{position:absolute;right:0;bottom:0;left:0;display:block;height:1px;content:"";background-color:#dedede}.changes-container.changes-container--changed>div,.changes-container.changes-container--fixed>div,.changes-container.changes-container--new>div{padding:0;background-color:transparent}.changes-container.changes-container--changed .changes-more,.changes-container.changes-container--fixed .changes-more,.changes-container.changes-container--new .changes-more{line-height:1.4}.changes-container.changes-container--changed .changes-more:before,.changes-container.changes-container--fixed .changes-more:before,.changes-container.changes-container--new .changes-more:before{bottom:2px}.changes-container.changes-container--new{background:-webkit-gradient(linear,left top,left bottom,from(#e4ffee),to(transparent));background:-webkit-linear-gradient(top,#e4ffee,transparent);background:-o-linear-gradient(top,#e4ffee,transparent);background:linear-gradient(180deg,#e4ffee,transparent)}.changes-container.changes-container--changed{background:-webkit-gradient(linear,left top,left bottom,from(#def6ff),to(transparent));background:-webkit-linear-gradient(top,#def6ff,transparent);background:-o-linear-gradient(top,#def6ff,transparent);background:linear-gradient(180deg,#def6ff,transparent)}.changes-container.changes-container--fixed{background:-webkit-gradient(linear,left top,left bottom,from(#fef6e6),to(transparent));background:-webkit-linear-gradient(top,#fef6e6,transparent);background:-o-linear-gradient(top,#fef6e6,transparent);background:linear-gradient(180deg,#fef6e6,transparent)}}
--></style>


## AlmaLinux 9 Base OS Image

Starting with the current 8.3 release, Virtuozzo Application Platform starts transitioning to the [software stacks](/software-stacks-versions/) based on the new ***AlmaLinux 9*** images (from the previously used *CentOS 7*). Such a change ensures support of all the up-to-date functionality, modern security standards, and compatibility with all the latest software solutions.

The transition process will be gradual and non-intrusive. It follows the next points:
- *<u>AlmaLinux 9 images are supported starting with the 8.3 platform version</u>* and won’t be available on the preceding versions.
- All the newly released stack versions will be based on AlmaLinux 9, so the whole pool of images will be seamlessly replaced with the new OS over time.
- Updates for the CentOS 7 based images will still be provided in case of critical patches and security issues.
- In the dashboard, tags based on the AlmaLinux 9 will be explicitly highlighted.
- [Redeployment](/container-redeploy/) from the CentOS 7 to the AlmaLinux 9 version of the stack can be performed without any setbacks. *<u>However, downgrading back to CentOS 7 is not supported.</u>*
- The up-to-date list of the [software stacks](/software-stacks-versions/) based on the AlmaLinux 9 image can be checked in the linked document.

![AlmaLinux image tags](01-almalinux-image-tags.png)

Alongside the AlmaLinux 9 image implementation, some new functionality is introduced, including updated key generation (*rsa-sha2-256* and *rsa-sha2-512* signatures support), updated Guacamole ([Web SSH](/web-ssh-client/)) client, and ***[nftables](https://netfilter.org/projects/nftables/)*** netfilter (replaces *iptables*). The *nftables* solution is a new recommended choice for firewall rules management. It offers unified and consistent syntax (contrary to the *xtables* utilities), high performance through maps and concatenations, and increased security as rules get translated into bytecode. At the same time, all the dashboard UI and API calls remain the same as before so that the management process is unchanged.

Other stack-related changes include an updated list of [supported OS distributions](/container-image-requirements/), including  **CentOS Stream 9** addition and **Debian 9** deprecation.

[More info](/software-stacks-versions/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Subscription Improvements

The recently implemented **[Subscription-Based Product](/subscription-products/)** solution was further improved in the current release to ensure the best experience for the customers. All the new changes are seamlessly integrated into the dedicated dashboard’s ***Subscription*** section.

![subscriptions new features](02-subscriptions-new-features.png)

One of the most requested features is the possibility to update the number of installations for the existing subscriptions. Starting with the 8.3 platform upgrade, the appropriate functionality was fully implemented. The update window is available using the new **Edit Subscription** option. Here, user can increase and decrease *Quantity* based on their need:

- Upon upgrade, an additional invoice will be automatically generated by the platform.
- In case of a downgrade (no less than the existing number of instances), the account’s balance will be recharged according to the subscription price and remaining billing period.

![edit subscription](03-edit-subscription.png)

Another new feature is the ability to switch subscription plan within the same product. This solution availability depends on the hosting provider. If available, you’ll see the corresponding **Switch Subscription** option for the required installation.

![switch subscription](04-switch-subscription.png)

Lastly the ability to enable/disable **Auto Pay** option was implemented, allowing to switch between automatic (with default payment method) and manual payment for the subscriptions.

![disabling auto pay](05-disabling-auto-pay.png)

[More info](/subscription-products/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Action Initiator for Emails

Virtuozzo Application Platform provides a powerful [collaboration functionality](/account-collaboration/) that allows multiple users to work on the same account. However, with high participants number and active development, it may become difficult to track all the actions performed by individuals and create confusion on whether the account is compromised. In order to help the tracking efforts, the email notifications were extended with the “action initiator” data. Depending on the operation, it can be the email address of the collaboration member or a reference to the internal trigger (e.g., [automatic horizontal scaling](/automatic-horizontal-scaling/)).

{{%right%}}[Back to the top](#back){{%/right%}}


## API Changes

Below, you can find a list of all changes to the public API in the 8.3 platform version (compared to the preceding [8.2.2](/release-notes-82/#api-changes) ones):

- Added new ***SetAutopay***, ***MoveProduct***, ***UpdateSubscription***, ***UpcomingInvoice***, and ***DiscardUpdateSubscription*** API methods due to [subscription](#subscription-improvements) changes.
- Added a new ***invalidateSessions*** parameter to all the password reset methods, which allows terminating all active user sessions (except the current one).

The API documentation's complete review has started in order to provide a comprehensive description of all the methods and their parameters. Currently, most of the ***billing*** and ***environment*** services have been updated. You can expect complete coverage over the course of several future releases.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Fixes Compatible with Prior Versions

Below, you can find the fixes that were implemented in the Virtuozzo Application Platform 8.3 release and also integrated into previous platform versions by means of the appropriate patches.

{{%table3 title="Virtuozzo Application Platform 8.3"%}}
**#**|**Compatible from**|**Description**
---|:---:|---
JE-65381|Any|The *${globals.password}* variable value is missing on the *Redis Cluster* after cloning
JE-66060|Any|*PostgreSQL* users created via *phpPgAdmin* cannot access the admin panel
JE-66252|Any|Login to *WebAdmin Console* fails for the *LiteSpeed/LLSMP* stacks after redeployment to the lower major version
JE-66503|Any|The *Multi-Regional Redis Cluster* package installation fails if the maximum allowed length is used for the provided domain name
JE-64453|3.3|An error occurs when installing the “*test*” version of the *Plesk* package from the platform Marketplace
JE-66406|3.3|The *Django* application is not working after installation from the platform Marketplace
JE-66259|5.0.5|An error occurs when installing the *Eclipse Vert.x Thin Jar Builder* package from the platform Marketplace
JE-66279|5.0.5|An error occurs when installing the *Nexus* package from the platform Marketplace
JE-66513|5.0.5|An error occurs when installing the *Open Liberty* application in the *Kubernetes cluster*
JE-66541|5.0.5|The custom *withExtIp* setting is not applied when installing the *Let’s Encrypt* add-on
JE-66590|5.0.5|An error occurs when installing the *Spring Boot Thin Jar Builder* package from the platform Marketplace
JE-66799|5.0.5|An error occurs when installing the *Oddo-Ce* package from the platform Marketplace
{{%/table3%}}

{{%right%}}[Back to the top](#back){{%/right%}}


## Software Stack Versions

The software stack provisioning process is independent of the platform release, which allows new software solutions to be delivered as soon as they are ready. However, due to the necessity to adapt and test new stack versions, there is a small delay between software release by its respective upstream maintainer and integration into Virtuozzo Application Platform.

The most accurate and up-to-date list of the certified [software stack versions](/software-stacks-versions/) can be found on the dedicated documentation page.

[More info](/software-stacks-versions/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Bug Fixes

In the table below, you can see the list of bug fixes applied to the platform starting from Virtuozzo Application Platform 8.3 release:

{{%table3 title="Virtuozzo Application Platform 8.3"%}}
**#**|**Affected Versions**|**Description**
---|:---:|---
JE-21315|3.2|Incorrect environment name in the successful migration pop-up if the name contains special characters
JE-33337|5.0.6|The upload limit warning message is absent if the uploaded file size is too large
JE-47088|-|An error occurs when logged in to the dashboard with the *Extended* token
JE-47315|-|The "*text input*" input method does not work in *Web SSH* client
JE-49993|5.7.7|Cannot reconnect to the *Web SSH* client after a container restart
JE-51930|-|The *access denied* error occurs when calling billing API methods using a token
JE-52137|5.7|Disconnected from *Web SSH* if switched to a different tab during the connection
JE-53323|-|The bind SSL/external domain actions are absent in the *Tasks* manager when working with the *Let’s Encrypt* add-on
JE-54683|-|Incorrect description for the *EditNodeGroup* method in the API documentation
JE-57190|-|Text from *Web SSH* that does not fit the screen width is copied with unnecessary line breaks
JE-59606|-|An error occurs when opening the topology wizard
JE-59773|-|The *MIME type* of the uploaded archives is identified incorrectly if its name contains spaces
JE-63283|-|The region icon tooltip is formatted incorrectly in the search menu
JE-63869|-|An error occurs when deploying a GitHub project with the "*/*" symbol in the branch name
JE-64138|-|An error occurs when uploading a file with the overwrite option via the file manager
JE-65380|8.2|An error occurs when opening the *Additionally* menu for nodes with the admin panel
JE-65402|any|Inconsistent firewall rules behavior on the *Memcached* node when working with containers with public IP
JE-65462|8.1|The search results are not displayed after long usage of the dashboard on accounts with many environments
JE-65786|-|The vertical scroll should appear for the *public keys* list if it does not fit the window
JE-65847|8.1|An error occurs when updating a project with the “*Auto resolve conflict*” option after the amended commit to the repo
JE-65875|-|The add-on installation window is not centered
JE-65917|-|Incorrect spelling in the error message
JE-65962|-|NFS storage is not stable with the *Kubernetes cluster*
JE-65988|-|Incorrect event names in the *SendEvent* API method description
JE-66072|-|An error occurs when working with *Object Browser* on the *Minio cluster*
JE-66100|-|API requests return an empty response instead of an error if the *platformUrl* parameter has a dot at the end
JE-66137|-|An incorrect host header is set during the external domain swap
JE-66300|-|The primary IP is changed when adding a second external IP address
JE-66413|-|The “*Got signal 13*” error occurs when adding a new node to the environment
JE-66421|-|An error occurs while getting the state of a custom Docker container during environment creation
JE-66458|-|The package installation error occurs when redeploying containers based on the *Debian 11* OS
JE-66758|-|The *bindSslCert* API method returns “*result: 0*” instead of the error when the incorrect *extDomains* parameter is specified
{{%/table3%}}

{{%right%}}[Back to the top](#back){{%/right%}}