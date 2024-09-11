---
draft: false
title: "Release Notes 7.1"
aliases: "/release-notes-71/"
seoindex: "index, follow"
seotitle: "Release Notes 7.1"
seokeywords: "paas, paas release notes, paas version, 7.1 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the platform 7.1 release."
menu: 
    docs:
        title: "Release Notes 7.1"
        url: "/release-notes-71/"
        weight: 40
        parent: "release-notes"
        identifier: "release-notes-71.md"
---

<a id="back"></a>

# Virtuozzo Application Platform 7.1

*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included to the **PaaS 7.1** release.

{{%rn-new%}}
{{%rn-item url="#send-message-api-with-ip-authorization"%}}
## Send Message API with IP Authorization
Added two new API methods that can send email notification to container owner using IP authorization (without user session)
{{%/rn-item%}}
{{%/rn-new%}}

{{%rn-changed%}}
{{%rn-item url="#info-for-environment-clone-dialog"%}}
## Info for Environment Clone Dialog
Added notification to the *Clone Environment* dialog that manual adjustment may be needed due to IP addresses and hostnames changes
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

## Send Message API with IP Authorization

In the current 7.1 PaaS release, two new API methods were implemented for sending email notifications from the container to its owner. These methods provide automatic authentication based on the container IP address so that user session (password and login) is not required. Such implementation significantly simplifies notification of the container owner based on the events inside the node, which allows automating various scenarios that previously were difficult in realization.

Both new methods are part of the **environment > node** service:
- ***SendEvent*** - sends a predefined event using IP authorization 
  - **eventName** - the name of the required event; currently, the following values are supported:
    - *SEND\_NOTIFICATION* - sends an email notification to the node owner
    - *OOM\_KILLER* - sends a message after *OOM Killer* invocation
    - *CUSTOM\_NODE\_EVENT* - a user-defined custom event
  - **params** - JSON object with parameters for Cloud Scripting
- ***SendNotification*** - sends an email notification to the node owner using IP authorization
  - **name** - title of the message
  - **message** - body of the message

The platform already utilizes these new methods to provide proper notification about changes in containers - for example, automatic notifications due to [smart recovery after the OOM error](/auto-configuration/). Developers can benefit from the implementation by extending their custom packages with automatic notification of the container owner based on some specific condition.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Info for Environment Clone Dialog

The **[Clone Environment](/clone-environment/)** is a powerful platform feature that allows you to create an identical copy of the existing environment. For example, it can be helpful during development to create a separate instance of the project where tuning and adjustments can be safely tested without affecting existing customers. However, when utilizing the feature, users should be aware that the IP addresses and hostnames of the clone will differ from the initial environment (i.e. manual re-adjustment of these values may be required). To ensure better awareness of the fact, such information was added to the ***Clone Environment*** dialog.

![01-clone-environment-dialog.png](01-clone-environment-dialog.png)

[More info](/clone-environment/)

{{%right%}}[Back to the top](#back){{%/right%}}


## API Changes

Below, you can find a list of all changes to the public API in the 7.1 platform version (compared to the preceding [7.0](/release-notes-70/#api-changes) ones).

Two new API methods were added to the **environment > node** service, implementing a simplified flow to [notify the container owner](#send-message-api-with-ip-authorization) (using IP authorization instead of user session):

- ***SendEvent*** - sends a predefined notification based on the specific event inside a container
- ***SendNotification*** - sends a custom email notification to the node owner

[More info](https://www.virtuozzo.com/application-platform-api-docs/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Fixes Compatible with Prior Versions

Below, you can find the fixes that were implemented in the PaaS 7.1 release and also integrated into previous platform versions by means of the appropriate patches.

{{%table3 title="PaaS 7.1"%}}
**#**|**Compatible from**|**Description**
---|:---:|---
JE-46279|any|An error occurs when installing the *Minio Cluster* package from the Marketplace
JE-57935|any|Errors and warnings during the *LiteSpeed* and *LLSMP* stacks restart are displayed incorrectly
JE-58694|any|When using the prepackaged *Jitsi* application, all users are disconnected upon any user being kicked or if the moderator leaves
JE-58696|any|When using the prepackaged *Jitsi* application, audio and video are not working in conferences with multiple users
JE-61742|any|An error occurs when installing the *IOTA Nodes* application
JE-59897|3.3|An error occurs when installing the *Liferay* prepackaged application from the Marketplace
JE-60685|3.3|The prepackaged *Odoo* application is down after the application server restart
JE-61879|3.3|An error occurs when installing the *BitNinja* add-on on the *LEMP* stack
JE-61887|3.3|Credentials are displayed in one line in the success pop-up for the *IOTA Nodes* application
JE-61951|3.3|The *BitNinja* add-on is not supported on some templates
JE-60272|5.0|An error occurs when installing the *JMeter* JPS package 
JE-61334|5.0|Incorrect credentials are sent via email for the *OpenVPN* application from the Marketplace
JE-46294|5.0.5|The *Elytron* subsystem is unavailable on the *WildFly* nodes after creation
JE-47222|5.0.5|The *HTTP/2* is not supported on some versions of the *Apache PHP* application servers
JE-48295|5.0.5|The */var/lib/jelastic/backup* directory is missing on the *MongoDB* database containers
JE-49577|5.0.5|The *yum install* command is not working on the *MongoDB* database containers
JE-49762|5.0.5|Errors in logs after restarting the *MongoDB* database containers
JE-50064|5.0.5|The *Let's Encrypt* add-on installation breaks symlinks in the *Python* application servers
JE-50130|5.0.5|The *Node.js* restart hangs if called during the add project operation
JE-50413|5.0.5|Incorrect response for the *jem service start/stop/restart/reload* commands on the VPS nodes
JE-50463|5.0.5|Incorrect template version in the *metainf.conf* file for the *NGINX PHP* servers
JE-50472|5.0.5|Incorrect path for the *backup* shortcut on the *MongoDB* nodes
JE-50633|5.0.5|Empty template version in the *metainf.conf* file for the *Percona* servers
JE-50709|5.0.5|The *JavaEngine* server based on *OpenJDK 14* is down after deploying an application
JE-50890|5.0.5|Warnings about the deprecated *ssl* directive are present in the *NGINX* load balancer logs
JE-50935|5.0.5|Incorrect access permissions to the */var/log/redis/redis.log* file on the PHP-based application servers
JE-52064|5.0.5|Incorrect regex for deleting upstreams from load balances
JE-52160|5.0.5|*GlusterFS cluster* is not operable after downgrading (redeploying to a lower version)
JE-53278|5.0.5|*Jetty* servers are not accessible after installing the *Let's Encrypt* add-on
JE-55725|5.0.5|Incorrect permissions for the */usr/java* directory on the *JavaEngine* stack with the *Dragonwell JDK*
JE-56570|5.0.5|Invalid *mbstring* module configuration options in the *php.ini* file
JE-56705|5.0.5|Incorrect error message for the unsuccessful *Storage* node restart
JE-56927|5.0.5|An error occurs when installing the *GitLab* package from the Marketplace
JE-57013|5.0.5|The */var/log/haproxy/haproxy.log* file is not rotated via logrotate on the *HAProxy* stack
JE-57468|5.0.5|An error occurs when disabling SSL on the *Varnish* stack 
JE-57764|5.0.5|An error occurs when adding new nodes to the *MySQL* cluster
JE-57994|5.0.5|The *Ruby* application is down if installing *Let's Encrypt* after removing the *FTP* add-on
JE-58326|5.0.5|An error occurs when deploying an application on the *GlassFish* stack 
JE-58733|5.0.5|The *btmp* and *wtmp* files are not rotated via logrotate on the *CentOS VPS* stack
JE-59396|5.0.5|Incorrect repository details on the *NGINX PHP* stacks
JE-59914|5.0.5|The "*cannot change locale*" error occurs when connecting to the node via the SSH gate
JE-60016|5.0.5|Custom SSL is unavailable on the *Varnish* nodes after redeploy
JE-60446|5.0.5|Password information is missing in the email for the cloned *PostgreSQL Cluster* environment
JE-60662|5.0.5|Incorrect permissions for the */etc/logrotate.d/nginx* file on the *NGINX* load balancer stack
JE-61807|5.0.5|An error occurs when deploying an application to the *Apache Ruby* stack
JE-52987|5.3.2|Some instances of the *WildFly auto-cluster* clone are broken
JE-52990|5.3.2|Removed worker instances are displayed in the *WildFly DAS* node
JE-53722|5.3.2|Auto-clustering is not properly removed when deleting all *WildFly* nodes from the topology
JE-54454|5.3.2|An error occurs when undeploying application from *WildFly Cluster* after removing the public IP address
JE-55418|5.3.2|The *WildFly* application is down when enabling auto-clustering after redeployment from the old version to the one with the feature support.
JE-57872|5.3.2|An error occurs when restarting *WildFly* nodes after adjusting the *STANDALONE_MODE_CONFIG* variable
JE-60691|5.3.2|An error occurs when installing the *WildFly Cluster* prepackaged solution from the Marketplace
JE-61605|5.3.2|An error occurs when deploying an application to the *WildFly* stack with *JDK 17*
JE-61959|5.4|An error occurs when installing the *MySQL Cluster* package from the Marketplace
JE-51972|5.5|*Payara Cluster* servers are down after restarting the environment
JE-52337|5.7|An error occurs when cloning an environment with the *WildFly auto-cluster*
JE-53610|5.7|An error occurs if removing worker nodes while logged into the *WildFly DAS* admin panel
JE-53691|5.7|After environment migration, instances are displayed as stopped or broken in the *WildFly DAS* admin panel
JE-54530|5.7|The maximum number of environments on the account should be verified when installing the *Magento Standalone* package
JE-50427|5.7.2|The *404 Not Found* error is displayed for the *LLSMP* applications deployed to the non-root context
JE-50842|5.7.2|Warnings in the *phpMyAdmin* panel for the *LLSMP* stack
JE-50924|5.7.2|Errors in the admin panel after the *LiteSpeed/LLSMP* node creation
JE-51141|5.7.2|The *phpMyAdmin* folder is not available via FTP on the *LEMP/LLSMP* nodes
JE-57337|5.7.2|The firewall is not working on the *LiteSpeed ADC* stack
JE-55672|5.7.4|The *GlusterFS Replication* add-on should not be removable after configuring *GlusterFS Cluster*
JE-57739|5.7.4|*LiteSpeed ADC* admin panel is not available via *IPv6*
JE-58575|5.7.4|The *force_kill* function works incorrectly on the *LiteSpeed ADC* stack
JE-62173|5.7.4|An error occurs when installing the *TimeZone* add-on on the *Ubuntu* and *Debian VPS* stacks
JE-52065|5.8|Two controller nodes are added to the *Extra* layer when creating *WildFly auto-cluster* via the topology wizard 
JE-52988|5.8|The dashboard should display a button to access the *WildFly DAS* admin panel on the layer level (not for a separate node)
JE-54090|5.8|An error occurs when creating the *WildFly auto-cluster*
JE-56167|5.8|An error occurs when installing the *Jenkins* instance via the topology wizard
JE-61169|5.8|Unclear UI for the *Elastic Beats* add-on installation frame
JE-61170|5.8|Errors in CS logs after the *Elastic Beats* add-on installation
JE-61177|5.8|Incorrect permissions for the */etc/heartbeat* folder after the *Elastic Beats* add-on installation
JE-61846|5.8|After the *Elastic Beats* add-on deletion, the */etc/heartbeat* folder is not entirely removed
JE-61641|7.0|An error occurs when installing the *CDN* add-on
JE-61765|7.0|If installed by a collaborator, the *Open Liberty* application is created without the *Storage* node
{{%/table3%}}

{{%right%}}[Back to the top](#back){{%/right%}}


## Software Stack Versions

The software stack provisioning process is independent of the platform release, which allows new software solutions to be delivered as soon as they are ready. However, due to the necessity to adapt and test new stack versions, there is a small delay between software release by its respective upstream maintainer and integration into the platform.

The most accurate and up-to-date list of the certified [software stack versions](/software-stacks-versions/) can be found on the dedicated documentation page.

[More info](/software-stacks-versions/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Bug Fixes

In the table below, you can see the list of bug fixes applied to the platform starting from PaaS 7.1.1 and 7.1.2 releases:

{{%table3 title="PaaS 7.1.1"%}}
**#**|**Affected Versions**|**Description**
---|:---:|---
JE-43124|5.5|The disk IOPS value is not calculated on the containers
JE-45740|-|The sendmail application is not available in containers
JE-50964|5.8|The redeploy operation should check for enough disk space inside the container
JE-51106|5.8|Exports records and iptables rules are not removed when unmounting a folder with the "*+*" symbol in the path
JE-52664|-|The site cannot be reached after the *FTP* add-on installation on the *GlassFish/Payara* containers
JE-55234|5.9.4|An error occurs when redeploying the *Ubuntu VPS 10.04* container 
JE-59950|-|An incorrect launcher is used for entrypoint commands in custom containers
JE-60719|6.3|An error occurs when transferring an environment to a user outside of the collaboration
JE-60795|7.0|An error occurs when transferring an environment to a user in a "*pending acceptance*" collaboration status
JE-61892|-|Invalid *pgrep* option error occurs when creating containers
JE-61942|-|An unhandled error occurs when deploying a damaged archive to the PHP environment
JE-62156|7.0|Incorrect wizard behavior when adding a template that does not correspond with the selected layer
{{%/table3%}}

{{%table3 title="PaaS 7.1.2"%}}
**#**|**Affected Versions**|**Description**
---|:---:|---
JE-62378|7.0|The "*`*" character is not properly escaped when defined in the container variables
JE-62393|-|Permissions issue when installing JPS to the owner account as a collaboration member
{{%/table3%}}

{{%right%}}[Back to the top](#back){{%/right%}}