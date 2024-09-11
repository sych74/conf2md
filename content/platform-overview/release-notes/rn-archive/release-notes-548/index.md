---
draft: false
title: "Release Notes 5.4.8"
aliases: "/release-notes-548/"
seoindex: "index, follow"
seotitle: "Release Notes 5.4.8"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the platform 5.4.8 release."
---

<a id="back"></a>

# Virtuozzo Application Platform 5.4.8
*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included to the **PaaS 5.4.8** release.

{{%rn-new%}}
{{%rn-item url="https://docs.cloudscripting.com/"%}}
## Cloud Scripting Improvements
* A possibility to create JPS packages without a target environment
* New *skipNodeEmail* parameter to avoid sending notifications about adding new nodes to environment
* Environment name parameters now can be customized by changing *envname* field in manifest
* A new *dependsOn* property is added for the [*list*](https://docs.cloudscripting.com/creating-manifest/visual-settings/#list) and *[envname](https://docs.cloudscripting.com/creating-manifest/visual-settings/#envname)* fields, allowing to specify dependence of the values across fields
{{%/rn-item%}}
{{%/rn-new%}}

{{%rn-changed%}}
{{%rn-item url="#web-ssh"%}}
## Web SSH Performance Optimization
Improved performance of the Web SSH client through integration of the *PageSpeed* module
{{%/rn-item%}}

{{%rn-item url="#nfs"%}}
## Waiting for NFS Server during Mount Points Creation
Adding a timeout for a new mount point creation operations to allow NFS server to start up properly
{{%/rn-item%}}

{{%rn-item url="#container-packages"%}}
## Notification about Failed Installation of Packages in Containers
Notification after a custom Docker container creation, if some of the platform-required packages were not installed
{{%/rn-item%}}

{{%rn-item url="#centos"%}}
## CentOS VPS Adjustments
Removed legacy *anyterm* client from CentOS template due to Web SSH feature implementation
{{%/rn-item%}}

{{%rn-item url="https://docs.cloudscripting.com/"%}}
## Cloud Scripting Improvements
* The *onBefore-* and *onAfterResetNodePassword* events were renamed to *onBefore-* and *onAfterResetServicePassword* respectively
* The *onBefore-* and *onAfterResetContainerPassword* events were renamed to *onBefore-* and *onAfterResetNodePassword* respectively
{{%/rn-item%}}

{{%rn-item url="#email-templates"%}}
## Email Templates Update
Automatic protocol selection for platform links and text review for *custom Docker container* email template
{{%/rn-item%}}

{{%rn-item url="#ruby-bundler"%}}
## Suppressing Warning for Ruby Bundler
Hiding an irrelevant warning notification, while working with Ruby Bundler
{{%/rn-item%}}

{{%rn-item url="#software"%}}
## Software Stack Versions
Actualized list of supported OS templates and software stack versions
{{%/rn-item%}}

{{%/rn-changed%}}

{{%rn-fixed%}}
{{%rn-item url="#auto-refill"%}}
## Auto-Refill Adjustment
Auto-refill when the balance is below the specified amount of money should also consider account bonuses
{{%/rn-item%}}

{{%rn-item url="#bug-fixes"%}}
## Bug Fixes
List of fixes applied to the platform starting from the current release
{{%/rn-item%}}

{{%/rn-fixed%}}

<a id="web-ssh"></a>


<style><!--
.changes-container{position:relative;padding-top:30px;padding-bottom:10px;padding-left:120px;border-top:1px solid #ddd}.changes-container:first-child{padding-top:0}.changes-container:first-child:before{top:15px}.changes-container:before{font-size:22px;position:absolute;top:45px;left:5px;width:110px;padding-top:42px;text-align:center;background-repeat:no-repeat;background-position:top}.changes-container>div{line-height:1.9;overflow:auto;margin-bottom:10px;padding:14px 20px;color:#282828;border-radius:3px}.changes-container>div:after{display:table;clear:both;content:""}.changes-container>div h6{font-size:18px;margin:0 0 16px}.changes-container>div .changes-more{position:relative;float:right;text-decoration:none}.changes-container>div .changes-more:after{margin-left:5px;content:">>"}.changes-container.changes-container--new:before{content:"New";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDozOEQ2OURDQjJDNDUxMUU4OEFDM0Q0OUYzRjVDQTUwMiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDozOEQ2OURDQzJDNDUxMUU4OEFDM0Q0OUYzRjVDQTUwMiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjM4RDY5REM5MkM0NTExRTg4QUMzRDQ5RjNGNUNBNTAyIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjM4RDY5RENBMkM0NTExRTg4QUMzRDQ5RjNGNUNBNTAyIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+NUw/0AAAAnNJREFUeNrMmE1oE0EYhjdLIz1IBDG1JdRqEdGCYPojqQgeWjA5xDYHpWBKPYhQaE+lLZTeTBHEq/bkpTUIIil6Mf6c0lLxUigShd6CBrTWHtQWD9L0/ei3MAzJmp2dDXnhgQy7M/Nmfr75Zn3Gq0eGBvnAGRAHN8A5cBj8Ae/AM/AG/JQrlqKjVXXQoMHkZfAcHC/zjMwOMqQX4DbYctqJ6cLgIbAEliuYLKcB8AMMOe1MdUQbwTpPt4qegtMg5eWIUp0VFyYt3QXDXhqdAl2GHi34svPNOozSbm4FvaAbnAf3DL16ArOu1miEd2mT4a36AI3qN5URTYL3NTBpaVBl6lvAolFbDasYnTVqr0tYp0G7tVrO6B2PzPwFWZvnm+A7zCaA+T+jPk3HqqwtXu8xGj2b9+idDPgMs012Rkv8z3RqF5wFv7mcr6IOHSZFmD1ZyWiIzerSPzYpZk3jDo73jzDbKBuluPnVQYJRjcLgi7S7Uw7qU/b1+GBNHuSjJ0BB85RfATmh3A/eKrYVNHkD5RQqU6d+cARsSM+uS22GXZgkXSOjPaBNofJ9XoO/QKewCcc4kbbUDtZczk7S5IxbRSPC7x2+ftBh8VAKN3kNy6iLjCZU/yWYEMrbYE4oBygecpLtVgEyesxFAw/AzQo3gE/gqKaNWTSl8KGUT3KqZsnPmVdIYwTJkNHXGhqiK/Ekx0naOBc0h7o0xdEIj0C9atuKox80TL+Xipeio3smn+2xOjVJsXpVPOvz/HGgnkSXyGnrk4+YlLwEHR6c+U61ybfeGfG7lJwkU4A+BS6CW+Aql71WgT8PpSlq0JqUX9gXYACycXnWqP0g9wAAAABJRU5ErkJggg==)}.changes-container.changes-container--new>div{background-color:#e4ffee}.changes-container.changes-container--changed:before{content:"Changed";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0QzNGRThBNjJDNDUxMUU4QTcyREYwOUUwQ0JFM0M4QiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0QzNGRThBNzJDNDUxMUU4QTcyREYwOUUwQ0JFM0M4QiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjRDM0ZFOEE0MkM0NTExRThBNzJERjA5RTBDQkUzQzhCIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjRDM0ZFOEE1MkM0NTExRThBNzJERjA5RTBDQkUzQzhCIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+c2zvogAAAidJREFUeNrUmM0rBVEYxueOmywuWfj+VlIkFje6ZEeJ8rURRVnIn0DJjlL+BxuSkogiiQ0iCwpJ3boLX/nOggXJx/PqvTVNXWbeOXO7nvot7rlnznnmzHnnfc94tOUPTYE8oBg0gw5QAnzgBayDWbAGHs0XfjXpFidwbrQWzIF0C30XQR94sGtUd2AwHiyALYsmSa3gHnTancwrNJkADvlxSzQDisCo1QskK0rXbDswGdYI6HHT6ADwa2o06Vn5zFARTBTNOcw7eANHmlptgPq/guq3PRrgKE3T3FUdoFW9kTz6brAbBZNhtUn2aCaY0qKrHonRYS36qkFQpQJbRvsdTBgCWUzI5rV34BZm24H+l1GPgyQQBGXgminjNjuimJgHpzCb9pvRL74zickK8Gpoe+W2oGA8SiZXMFsQyWg2m7WjfVBuMmk0W859JOn9GGYTzEbpvXlpo8AIm6zmRBBJb9xHYpZKxQljZsoDZ4KBErnmtDrps3D/p+ocQJvCAXwu9TWrhYxWgnzhABTdT+A8Qo3Zyf89cV+pur1ccTtRMuOLsIq5ChKCn1a0XYt9JZHRlH9g9IqMXigaLM5im0TzZHRV0WBdpveyzm0qNE3v0QDXnrEqOlqn013vKXz8bqgVx5Sfcopye2OMmhwHO8Zcf8IfB2JJY2AwfOgzbv4lUCrM+Sp1x0XMkPFkai6ST0EhqAK9oIF/u60z/jw0DQ5oT5o7fAswAKxgepYzbixFAAAAAElFTkSuQmCC)}.changes-container.changes-container--changed>div{background-color:#def6ff}.changes-container.changes-container--fixed:before{content:"Fixed";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpEM0FFMDgwQzJDNDUxMUU4Qjk2NUQ1RjM3QjZEQTIwQyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpEM0FFMDgwRDJDNDUxMUU4Qjk2NUQ1RjM3QjZEQTIwQyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkQzQUUwODBBMkM0NTExRThCOTY1RDVGMzdCNkRBMjBDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkQzQUUwODBCMkM0NTExRThCOTY1RDVGMzdCNkRBMjBDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+p2cxQAAAAm5JREFUeNrMmN1LFFEYxmeHTfdChWRdM+xDEiG7XJQtRCKFKNDdINTCBS+68E5CUBDxpiDqIugP6MaPShHDuihCbyoUb4K09NpsQfy4KQ1M3fV5l3dgmMbdmXPObPvAD+brnHnmPfOe8874Uq98mgJRJzWgBbSBi6AI7IAZMAE+gO1/WrYnHd3Ar8BkA5gE5TbnyGyMIU2De2DL7U10CYMF4DX4dIxJO0XBJuhwezPRiAbAVx5uEb0E1eChlxGlNp8lTBp6AOJeGu0DYU2NhrVx/ZSjbM2S9XSyktkHe2BRU6tZ0Jwt+zO9oxHO0pDmrZoARXVdZOg7wXwOTBqKibyjFWBEwc0PwDL45eDauIjRQUmDf8BVUAgugUYHba4gqcqAq2Tal1yxKPESvE1Gv7louwG607nRnkxmiqhP0uRjk8kClyY1zokpsILohjIZTfFTiWrUtP0XzFleiTN8PJtq0g88rp8/zuhpcChhdNeyfwe8ZZMXwE+uqJwu70swG7AajfCwVUgYDVj2f4BWUMzz5AlQ6qI/qr6em42e5XlTRjfT75a9jMS4LdDvXUQ1qHMCfVRg8l2Wa+rAC8H+W/3cwTkPTF4Dv8FJ0MPXiarTzxW3apODXMapUpiG/pbE+mxnckixSVIJRTQouExO2xx/Cu57ULQkKKJrAg39nIS5MEmaIqPvBT/senlepOLjmYcmSWNUlEQUzKFeij6tyymiC4LDnytFqZLSuRC5kacmnxiFjbGEfuefA/mkR6Df+OgzFyVvQC1Y/c8Gqcy8DAbMX6bWIpmKiipQD7rAdd73Wqv8e2gMfLFW96QjAQYAvVZ8VxrR76cAAAAASUVORK5CYII=)}.changes-container.changes-container--fixed>div{background-color:#fef6e6}@media (max-width:479px){.changes-container{padding-top:80px!important;padding-right:10px;padding-left:10px}.changes-container:first-child:before{top:25px}.changes-container:last-child{margin-bottom:0!important}.changes-container:last-child:after{display:none!important}.changes-container:before{top:25px;left:auto;width:auto;margin-left:0;padding-top:6px;padding-left:55px;background-position:0 0}.changes-container.changes-container--changed,.changes-container.changes-container--fixed,.changes-container.changes-container--new{position:relative;margin-bottom:40px;border-bottom:0}.changes-container.changes-container--changed:after,.changes-container.changes-container--fixed:after,.changes-container.changes-container--new:after{position:absolute;right:0;bottom:0;left:0;display:block;height:1px;content:"";background-color:#dedede}.changes-container.changes-container--changed>div,.changes-container.changes-container--fixed>div,.changes-container.changes-container--new>div{padding:0;background-color:transparent}.changes-container.changes-container--changed .changes-more,.changes-container.changes-container--fixed .changes-more,.changes-container.changes-container--new .changes-more{line-height:1.4}.changes-container.changes-container--changed .changes-more:before,.changes-container.changes-container--fixed .changes-more:before,.changes-container.changes-container--new .changes-more:before{bottom:2px}.changes-container.changes-container--new{background:-webkit-gradient(linear,left top,left bottom,from(#e4ffee),to(#ffffff));background:-webkit-linear-gradient(top,#e4ffee,#ffffff);background:-o-linear-gradient(top,#e4ffee,#ffffff);background:linear-gradient(180deg,#e4ffee,#ffffff)}.changes-container.changes-container--changed{background:-webkit-gradient(linear,left top,left bottom,from(#def6ff),to(#ffffff));background:-webkit-linear-gradient(top,#def6ff,#ffffff);background:-o-linear-gradient(top,#def6ff,#ffffff);background:linear-gradient(180deg,#def6ff,#ffffff)}.changes-container.changes-container--fixed{background:-webkit-gradient(linear,left top,left bottom,from(#fef6e6),to(#ffffff));background:-webkit-linear-gradient(top,#fef6e6,#ffffff);background:-o-linear-gradient(top,#fef6e6,#ffffff);background:linear-gradient(180deg,#fef6e6,#ffffff)}}
--></style>


## Web SSH Performance Optimization
Within the present platform upgrade, the performance of the recently implemented [Web SSH](/web-ssh-client) feature was boosted. This was achieved by adding special **[PageSpeed](https://developers.google.com/speed/)** module, which automatically compresses data within requests, combines all scripts and css files into a single one (to reduce a number of requests), etc. As a result of such optimization, the authentication for Web SSH client is performed notably faster and the overall performance of the tool is improved.

[More info](/web-ssh-client)
{{% right %}}[Back to the top](#back){{% /right %}}


## Waiting for NFS Server during Mount Points Creation
In case a new [mount point](/mount-points) addition is called during NFS server unavailability (e.g. creation or restart), the appropriate error immediately occurs. In the current PaaS 5.4.8 version, a dedicated timeout was added before reporting an issue, which allows NFS to start up and process the request. Herewith, the operation is retried every 4 seconds for 5 times, giving a total of the additional 20 seconds for the mount point to be successfully created.

[More info](/mount-points)
{{% right %}}[Back to the top](#back){{% /right %}}



## Auto-Refill Adjustment
The platform auto-refill feature allows to configure regular payments to keep your account active and all of the comprised environments running. The available frequency (condition) options are: 

* *Weekly* (every Monday)
* *Monthly* (1st of each month)
* *Balance is less than* a specified sum

Starting with the current 5.4.8 PaaS upgrade, the latter option will additionally consider account bonuses. In such a way, an automatic refill is triggered only in case the combined value of the account balance and bonuses is less than the specified number<a id="container-packages"></a>.

{{% right %}}[Back to the top](#back){{% /right %}}


## Notification about Failed Installation of Packages in Containers
When creating a [custom Docker container](/dockers-overview), platform automatically installs a number of basic packages (e.g. *openssh-server*, *cron*, *curl*, etc.) to ensure a proper node operability within the platform. Herewith, depending on the selected image, the installation of certain packages may fail, resulting in the probable issues during this container management in the future. So, starting with the present 5.4.8 platform upgrade, in case of such a problem, the appropriate notification will be sent to the node owner, providing a list of not installed packages<a id="centos"></a>.

{{% right %}}[Back to the top](#back){{% /right %}}


## CentOS VPS Adjustments
**[CentOS](/vps-centos)** is a popular virtual private server and the platform provides a managed template of this software stack. Starting with the current 5.4.8 PaaS release, its in-built *anyterm* Web-based SSH client was completely removed from the template due to a newer, more powerful and convenient [Web SSH](/web-ssh-client) tool integration on the platform.

[More info](/vps-centos)
{{% right %}}[Back to the top](#back){{% /right %}}


## Email Templates Update

Within the present PaaS upgrade, the following adjustments were applied to some of the email notifications:

* the platform links within emails (e.g. in the ***Environment transfer request*** one) were tuned to correctly detect *http* or *https* protocol, utilizing the former one only in case the SSL is not configured for the current PaaS installation
* an email template for the [custom Docker containers](/dockers-overview) was adjusted to provide better clarity and greater usability:
    * credentials for SSH access were explicitly denominated as *SSH Login* and *SSH Password* to avoid any misunderstanding 
    * *Access URL* field was replaced with the *Host Name* one (i.e. node link without the protocol part), which is required more frequentl<a id="ruby-bundler"></a>y

{{% right %}}[Back to the top](#back){{% /right %}}


## Suppressing Warning for Ruby Bundler
The Apache Ruby and NGINX Ruby software stacks are provided with the [Bundler](https://bundler.io/) dependency manager out-of-box in the platform. It helps to comfortably manage your project dependencies and ensures the gems you need are present. While working with Bundler, a warning about running it under the root user was displayed. Message notified about the potential issues of such approach, which, in case of the platform, are irrelevant. So, in order to avoid confusion and unnecessary concerns, this warning was removed, allowing to provide a clearer response for operations with Bundler<a id="software"></a>.

{{% right %}}[Back to the top](#back){{% /right %}}


## Software Stack Versions

Check out the list of the most accurate software stacks for the current platform version:

|                        Stack                        |                        PaaS 5.4.8                        |
|---|---|
|*Apache Balancer*|2.4|
|*Apache PHP*|2.4.6|
|*Apache Python*|2.4|
|*Apache Ruby*|2.4.33|
|*Cassandra 2*|2.2.4|
|*Cassandra 3*|3.0|
|*CentOS 6 (VPS)*|6.8|
|*CentOS 7 (VPS)*|7.2|
|*Couchbase*|5.0.1|
|*CouchDB*|1.6.1|
|*Docker Engine CE*|18.03|
|*GlassFish 3*|3.1.2.2|
|*GlassFish 4*|4.1.2|
|*GlassFish 5*|5.0|
|*Golang*|1.10|
|*HAProxy*|1.8.12|
|*IIS*|8|
|*Jetty 6*|6.1.26|
|*Jetty 8*|8.1.17|
|*Jetty 9*|9.3.7|
|*MariaDB 5*|5.5.60|
|*MariaDB 10*|10.3.7|
|*Maven*|3.5.3|
|*Memcached*|1.5.8|
|*MongoDB 2*|2.6.11|
|*MongoDB 3*|3.4.0|
|*MSSQL*|2012|
|*MySQL*|5.7.22|
|*Neo4j*|1.9|
|*Neo4j 2*|2.3|
|*Neo4j 3*|3.2|
|*NGINX Balancer*|1.12.2|
|*NGINX PHP*|1.12.2|
|*NGINX Ruby*|1.14.0|
|*NodeJS 6*|6.14.1|
|*NodeJS 8*|8.11.3|
|*NodeJS 9*|9.11.1|
|*NodeJS 10*|10.6.0|
|*OrientDB*|1.7.4|
|*OrientDB 2*|2|
|*Payara 4*|4.1.2.181|
|*Payara 5*|5.182|
|*PerconaDB*|5.6|
|*PostgreSQL 9*|9.6.9|
|*PostgreSQL 10*|10.4|
|*Redis*|4.0.9|
|*Spring Boot*|2|
|*Tomcat 7*|7.0.88|
|*Tomcat 8*|8.5.31|
|*Tomcat 9*|9.0.8|
|*TomEE*|7.0.4|
|*Ubuntu (VPS)*|16.04|
|*Varnish 4*|4.1.8|
|*Varnish 5*|5.2.1|
|*Varnish 6*|6.0.0|
|*WildFly 10*|10.1.0|
|*WildFly 11*|11.0.0|
|*WildFly 12*|12.0.0|
|*WildFly 13*|13.0.0|
|*Windows (VPS)*|2012|

|**Engine**|**#**|
|---|---|
|*JDK*|1.6.0_45<br>1.7.0_79<br>1.8.0_172<br>9.0.4<br>10.0.1|
|*Open JDK*|1.7.0._181<br>1.8.0_171|
|*OpenJ9*|0.8.0-8u162-b12|
|*PHP*|5.3.<br>5.4.45<br>5.5.38<br>5.6.33<br>7.0.27<br>7.1.13<br>7.2.1|
|*Ruby*|2.2.10<br>2.3.7<br>2.4.4<br>2.5.1|
|*Python*|2.7.12<br>3.3.6<br>3.4.5<br>3.5.2|
|*Node.js*|6.14.1<br>8.11.3<br>9.11.1<br>10.6.0|
|.*NET*|4|
|*Go*|1.10<a id="bug-fixes"></a>|

<span></span>{{%back%}}{{%/back%}}




## Bug Fixes
In the tables below, you can see the list of bug fixes applied to the platform starting from PaaS 5.4.8-10 releases:

{{%bug-fixes title="PaaS 5.4.8"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-33950|Missing double quotes in the variable values of the custom Docker containers
JE-35528|The *actions log* tab should not be displayed for the custom Docker containers
JE-35750|The Public IP address is not attached to the new manager containers of the *Docker Swarm* package during horizontal scaling
JE-37252|Incorrect text formatting for some of the API method descriptions in documentation
JE-37475|The *incorrect docker manifest* error appears, when creating environment with URL as a label value
JE-37953|The *Variables* list in topology wizard should be reloaded upon selecting a different image tag
JE-38222|The *Export/Import* feature does not work over the IPv6 protocol
JE-39097|The JPS package deployment frame changes position during its settings adjustment
JE-39156|Collaborators with the *view* permissions can deploy into shared environment via archive / URL
JE-39413|The *MASTER_IP* variable should be automatically adjusted after environment migration
JE-39559|Typo in the "*File to download is too large*" error message
JE-39587|Environment variables with the *&* special symbol in value cannot be added to container
JE-39721|Error, while adding environment variables with some special symbols (i.e. *[ ] = &lt;*) to container
JE-39899|The custom Maven arguments for a particular project (i.e. specified with the *MAVEN_RUN_ARGS_{project}* variable) are not processed
JE-39944|The *MASTER_IP* variable should be automatically adjusted after environment migration for all nodes
JE-40139|The comma separator for the source IP addresses in the *container firewall* rules should be allowed
JE-40319|The *CTRL+V* shortcut does not work within Web SSH, if switched to different environment tab during connection
JE-40400|Environment cannot be created, if the *nodes* parameter in JPS manifest is not an array
JE-40437|The *jps.marketplace.install* API method cannot be authenticated using tokens
JE-40461|The *Variables* tab cannot be accessed after adding variable with the double quotation used twice
JE-40623|An environment becomes inaccessible via IPv4, if only IPv6 public address is assigned
JE-40655|An error occurs, if the container *CMD / Entry Point* commands include quotation
JE-40665|The *Ubuntu VPS* stack cannot be created
JE-40738|The URL in the JPS package *success* parameter is not replaced correctly
JE-40749|The *Source* value of the outbound firewall rule is displayed within the *Destination* field during edition
JE-40801|Incorrect behaviour during the environment region selection in JPS packages using the *region* and *targetRegions* parameters
JE-40873|Typo within the *502 Bad gateway* error page title
JE-40970|Error, while cloning environment via the *cloneEnv* API method
JE-40978|Custom parameters passed via the *marketplace.jps.Install* method in cloud scripting are not applied
JE-40990|The firewall should not be enabled during nodes scaling of the legacy environments without such a feature
JE-41049|The *grep* tool does not work on the *Alpine* Docker image after installation
JE-41070|The *wrong cloudlets counts* error appears, when creating a new environment
JE-41080|An error occurs during the trial account upgrade
JE-41099|Not all environment variables specified in Dockerfile are exported into custom container
JE-41191|There is extra space between lines, when pasting text copied from the *Web SSH* tab
JE-41278|The *GetEnvInfo* API method can not find environments with 33 symbols in name
JE-41291|Different environment variables for the Docker image build locally and created as custom container within platform
JE-41334|The custom SSL check up during environment topology adjustment should be performed based on the existing node(s) labels
JE-41356|An error with NGINX PHP node after restart due to incorrect *iptables* rules
JE-41392|The *CMD / Entry Point* command is not displayed within dashboard
JE-41402|The *eval* API method cannot be authenticated with tokens
JE-41484|The *CMD / Entry Point* command is not executed after container restart
JE-41511|An error, while installing two JPS packages with the same *ID* value
{{%/table%}}
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.4.9"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-40332|Automatic horizontal scaling does not work for nodes with public IP attached
JE-41605|An error, while restarting *Ruby* application server with the default *HelloWorld* package deployed
JE-41641|The currently opened *WebSSH* tab is disconnected after clicking the *Duplicate Session* button
JE-41733|The entry point link defined with the *startPage* Cloud Scripting parameter is processed incorrectly
{{%/table%}}
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.4.10"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-38962|The *JEM Docker aftercreate operation has failed* error occurs after Docker container creation
JE-40689|Prolonged redeploy time if the new container image has groups, which are absent in the group list of the current one
JE-41744|Failure during the NFS mount addition on the *BusyBox*-based containers (e.g. alpine)
JE-41746|Errors, while redeploying *alpine*-based containers
JE-42079|The aftercreate package installation is not called on the *alpine*-based containers
JE-42104|An error, while trying to remove node(s) without internal IP address from the scaled VPS layer
{{%/table%}}
{{%/bug-fixes%}}{{%back%}}{{%/back%}}

