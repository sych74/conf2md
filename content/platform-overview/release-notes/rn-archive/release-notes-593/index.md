---
draft: false
title: "Release Notes 5.9.3"
aliases: ["/release-notes-593/", "/release-notes-592/"]
seoindex: "index, follow"
seotitle: "Release Notes 5.9.3"
seokeywords: "paas, paas release notes, paas version, 5.9.3 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the platform 5.9.3 release."
---

<a id="back"></a>

# Virtuozzo Application Platform 5.9.3

*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included to the **PaaS 5.9.3** release.

{{%rn-new%}}
{{%rn-item url="#litespeed-license-plans"%}}
## LiteSpeed License Plans
Implemented support of multiple LiteSpeed license plans and the corresponding management add-on
{{%/rn-item%}}

{{%rn-item url="#password-reset-enhancement"%}}
## Password Reset Enhancement
A new secure flow to recover account password
{{%/rn-item%}}

{{%rn-item url="#simultaneous-installation-for-multiple-auto-clusters"%}}
## Simultaneous Installation for Multiple Auto-Clusters
Added support of multiple auto-clusters installation in parallel
{{%/rn-item%}}

{{%rn-item url="#batch-mode-for-mount-operations"%}}
## Batch Mode for Mount Operations
Implemented batch mode for the *NFS mount/unmount* operations to speed up operations
{{%/rn-item%}}

{{%rn-item url="#iptables-for-bridge-interfaces-in-containers"%}}
## Iptables for Bridge Interfaces in Containers
Added kernel flag to allow packets to be checked by the *iptables* rules when going through the bridge interfaces
{{%/rn-item%}}

{{%rn-item url="#cloud-scripting-improvements"%}}
## Cloud Scripting Improvements
Integrated engine improvements to boost performance and added new functionality to enhance the user experience
{{%/rn-item%}}
{{%/rn-new%}}

{{%rn-changed%}}
{{%rn-item url="#ui-improvements"%}}
## UI Improvements
* relocated region icons for better clarity and support for the environment with prolonged names
* redesigned/reviewed error pages, and added new pages for specific issues
* added info about specifics of the default ports traffic proxying
* created a new *Collaboration* section in the Marketplace
{{%/rn-item%}}

{{%rn-item url="#container-stop-operation-optimization"%}}
## Container Stop Operation Optimization
Refactored code to speed up the container stop operation operation
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
Bug fixes implemented in the current release and integrated to the previous platform versions through the appropriate patches
{{%/rn-item%}}

{{%rn-item url="#bug-fixes"%}}
## Bug Fixes
List of fixes applied to the platform starting from the current release
{{%/rn-item%}}
{{%/rn-fixed%}}

<style><!--
.changes-container{position:relative;padding-top:30px;padding-bottom:10px;padding-left:120px;border-top:1px solid #ddd}.changes-container:first-child{padding-top:0}.changes-container:first-child:before{top:15px}.changes-container:before{font-size:22px;position:absolute;top:45px;left:5px;width:110px;padding-top:42px;text-align:center;background-repeat:no-repeat;background-position:top}.changes-container>div{line-height:1.9;overflow:auto;margin-bottom:10px;padding:14px 20px;color:#282828;border-radius:3px}.changes-container>div:after{display:table;clear:both;content:""}.changes-container>div h6{font-size:18px;margin:0 0 16px}.changes-container>div .changes-more{position:relative;float:right;text-decoration:none}.changes-container>div .changes-more:after{margin-left:5px;content:">>"}.changes-container.changes-container--new:before{content:"New";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDozOEQ2OURDQjJDNDUxMUU4OEFDM0Q0OUYzRjVDQTUwMiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDozOEQ2OURDQzJDNDUxMUU4OEFDM0Q0OUYzRjVDQTUwMiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjM4RDY5REM5MkM0NTExRTg4QUMzRDQ5RjNGNUNBNTAyIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjM4RDY5RENBMkM0NTExRTg4QUMzRDQ5RjNGNUNBNTAyIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+NUw/0AAAAnNJREFUeNrMmE1oE0EYhjdLIz1IBDG1JdRqEdGCYPojqQgeWjA5xDYHpWBKPYhQaE+lLZTeTBHEq/bkpTUIIil6Mf6c0lLxUigShd6CBrTWHtQWD9L0/ei3MAzJmp2dDXnhgQy7M/Nmfr75Zn3Gq0eGBvnAGRAHN8A5cBj8Ae/AM/AG/JQrlqKjVXXQoMHkZfAcHC/zjMwOMqQX4DbYctqJ6cLgIbAEliuYLKcB8AMMOe1MdUQbwTpPt4qegtMg5eWIUp0VFyYt3QXDXhqdAl2GHi34svPNOozSbm4FvaAbnAf3DL16ArOu1miEd2mT4a36AI3qN5URTYL3NTBpaVBl6lvAolFbDasYnTVqr0tYp0G7tVrO6B2PzPwFWZvnm+A7zCaA+T+jPk3HqqwtXu8xGj2b9+idDPgMs012Rkv8z3RqF5wFv7mcr6IOHSZFmD1ZyWiIzerSPzYpZk3jDo73jzDbKBuluPnVQYJRjcLgi7S7Uw7qU/b1+GBNHuSjJ0BB85RfATmh3A/eKrYVNHkD5RQqU6d+cARsSM+uS22GXZgkXSOjPaBNofJ9XoO/QKewCcc4kbbUDtZczk7S5IxbRSPC7x2+ftBh8VAKN3kNy6iLjCZU/yWYEMrbYE4oBygecpLtVgEyesxFAw/AzQo3gE/gqKaNWTSl8KGUT3KqZsnPmVdIYwTJkNHXGhqiK/Ekx0naOBc0h7o0xdEIj0C9atuKox80TL+Xipeio3smn+2xOjVJsXpVPOvz/HGgnkSXyGnrk4+YlLwEHR6c+U61ybfeGfG7lJwkU4A+BS6CW+Aql71WgT8PpSlq0JqUX9gXYACycXnWqP0g9wAAAABJRU5ErkJggg==)}.changes-container.changes-container--new>div{background-color:#e4ffee}.changes-container.changes-container--changed:before{content:"Changed";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDo0QzNGRThBNjJDNDUxMUU4QTcyREYwOUUwQ0JFM0M4QiIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDo0QzNGRThBNzJDNDUxMUU4QTcyREYwOUUwQ0JFM0M4QiI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOjRDM0ZFOEE0MkM0NTExRThBNzJERjA5RTBDQkUzQzhCIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOjRDM0ZFOEE1MkM0NTExRThBNzJERjA5RTBDQkUzQzhCIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+c2zvogAAAidJREFUeNrUmM0rBVEYxueOmywuWfj+VlIkFje6ZEeJ8rURRVnIn0DJjlL+BxuSkogiiQ0iCwpJ3boLX/nOggXJx/PqvTVNXWbeOXO7nvot7rlnznnmzHnnfc94tOUPTYE8oBg0gw5QAnzgBayDWbAGHs0XfjXpFidwbrQWzIF0C30XQR94sGtUd2AwHiyALYsmSa3gHnTancwrNJkADvlxSzQDisCo1QskK0rXbDswGdYI6HHT6ADwa2o06Vn5zFARTBTNOcw7eANHmlptgPq/guq3PRrgKE3T3FUdoFW9kTz6brAbBZNhtUn2aCaY0qKrHonRYS36qkFQpQJbRvsdTBgCWUzI5rV34BZm24H+l1GPgyQQBGXgminjNjuimJgHpzCb9pvRL74zickK8Gpoe+W2oGA8SiZXMFsQyWg2m7WjfVBuMmk0W859JOn9GGYTzEbpvXlpo8AIm6zmRBBJb9xHYpZKxQljZsoDZ4KBErnmtDrps3D/p+ocQJvCAXwu9TWrhYxWgnzhABTdT+A8Qo3Zyf89cV+pur1ccTtRMuOLsIq5ChKCn1a0XYt9JZHRlH9g9IqMXigaLM5im0TzZHRV0WBdpveyzm0qNE3v0QDXnrEqOlqn013vKXz8bqgVx5Sfcopye2OMmhwHO8Zcf8IfB2JJY2AwfOgzbv4lUCrM+Sp1x0XMkPFkai6ST0EhqAK9oIF/u60z/jw0DQ5oT5o7fAswAKxgepYzbixFAAAAAElFTkSuQmCC)}.changes-container.changes-container--changed>div{background-color:#def6ff}.changes-container.changes-container--fixed:before{content:"Fixed";background-image:url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACoAAAAeCAYAAABaKIzgAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyFpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQyIDc5LjE2MDkyNCwgMjAxNy8wNy8xMy0wMTowNjozOSAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIChXaW5kb3dzKSIgeG1wTU06SW5zdGFuY2VJRD0ieG1wLmlpZDpEM0FFMDgwQzJDNDUxMUU4Qjk2NUQ1RjM3QjZEQTIwQyIgeG1wTU06RG9jdW1lbnRJRD0ieG1wLmRpZDpEM0FFMDgwRDJDNDUxMUU4Qjk2NUQ1RjM3QjZEQTIwQyI+IDx4bXBNTTpEZXJpdmVkRnJvbSBzdFJlZjppbnN0YW5jZUlEPSJ4bXAuaWlkOkQzQUUwODBBMkM0NTExRThCOTY1RDVGMzdCNkRBMjBDIiBzdFJlZjpkb2N1bWVudElEPSJ4bXAuZGlkOkQzQUUwODBCMkM0NTExRThCOTY1RDVGMzdCNkRBMjBDIi8+IDwvcmRmOkRlc2NyaXB0aW9uPiA8L3JkZjpSREY+IDwveDp4bXBtZXRhPiA8P3hwYWNrZXQgZW5kPSJyIj8+p2cxQAAAAm5JREFUeNrMmN1LFFEYxmeHTfdChWRdM+xDEiG7XJQtRCKFKNDdINTCBS+68E5CUBDxpiDqIugP6MaPShHDuihCbyoUb4K09NpsQfy4KQ1M3fV5l3dgmMbdmXPObPvAD+brnHnmPfOe8874Uq98mgJRJzWgBbSBi6AI7IAZMAE+gO1/WrYnHd3Ar8BkA5gE5TbnyGyMIU2De2DL7U10CYMF4DX4dIxJO0XBJuhwezPRiAbAVx5uEb0E1eChlxGlNp8lTBp6AOJeGu0DYU2NhrVx/ZSjbM2S9XSyktkHe2BRU6tZ0Jwt+zO9oxHO0pDmrZoARXVdZOg7wXwOTBqKibyjFWBEwc0PwDL45eDauIjRQUmDf8BVUAgugUYHba4gqcqAq2Tal1yxKPESvE1Gv7louwG607nRnkxmiqhP0uRjk8kClyY1zokpsILohjIZTfFTiWrUtP0XzFleiTN8PJtq0g88rp8/zuhpcChhdNeyfwe8ZZMXwE+uqJwu70swG7AajfCwVUgYDVj2f4BWUMzz5AlQ6qI/qr6em42e5XlTRjfT75a9jMS4LdDvXUQ1qHMCfVRg8l2Wa+rAC8H+W/3cwTkPTF4Dv8FJ0MPXiarTzxW3apODXMapUpiG/pbE+mxnckixSVIJRTQouExO2xx/Cu57ULQkKKJrAg39nIS5MEmaIqPvBT/senlepOLjmYcmSWNUlEQUzKFeij6tyymiC4LDnytFqZLSuRC5kacmnxiFjbGEfuefA/mkR6Df+OgzFyVvQC1Y/c8Gqcy8DAbMX6bWIpmKiipQD7rAdd73Wqv8e2gMfLFW96QjAQYAvVZ8VxrR76cAAAAASUVORK5CYII=)}.changes-container.changes-container--fixed>div{background-color:#fef6e6}@media (max-width:479px){.changes-container{padding-top:80px!important;padding-right:10px;padding-left:10px}.changes-container:first-child:before{top:25px}.changes-container:last-child{margin-bottom:0!important}.changes-container:last-child:after{display:none!important}.changes-container:before{top:25px;left:auto;width:auto;margin-left:0;padding-top:6px;padding-left:55px;background-position:0 0}.changes-container.changes-container--changed,.changes-container.changes-container--fixed,.changes-container.changes-container--new{position:relative;margin-bottom:40px;border-bottom:0}.changes-container.changes-container--changed:after,.changes-container.changes-container--fixed:after,.changes-container.changes-container--new:after{position:absolute;right:0;bottom:0;left:0;display:block;height:1px;content:"";background-color:#dedede}.changes-container.changes-container--changed>div,.changes-container.changes-container--fixed>div,.changes-container.changes-container--new>div{padding:0;background-color:transparent}.changes-container.changes-container--changed .changes-more,.changes-container.changes-container--fixed .changes-more,.changes-container.changes-container--new .changes-more{line-height:1.4}.changes-container.changes-container--changed .changes-more:before,.changes-container.changes-container--fixed .changes-more:before,.changes-container.changes-container--new .changes-more:before{bottom:2px}.changes-container.changes-container--new{background:-webkit-gradient(linear,left top,left bottom,from(#e4ffee),to(transparent));background:-webkit-linear-gradient(top,#e4ffee,transparent);background:-o-linear-gradient(top,#e4ffee,transparent);background:linear-gradient(180deg,#e4ffee,transparent)}.changes-container.changes-container--changed{background:-webkit-gradient(linear,left top,left bottom,from(#def6ff),to(transparent));background:-webkit-linear-gradient(top,#def6ff,transparent);background:-o-linear-gradient(top,#def6ff,transparent);background:linear-gradient(180deg,#def6ff,transparent)}.changes-container.changes-container--fixed{background:-webkit-gradient(linear,left top,left bottom,from(#fef6e6),to(transparent));background:-webkit-linear-gradient(top,#fef6e6,transparent);background:-o-linear-gradient(top,#fef6e6,transparent);background:linear-gradient(180deg,#fef6e6,transparent)}}
--></style>


## LiteSpeed License Plans

**LiteSpeed** is a popular, high performance and low memory consumption [PHP web server](/litespeed-web-server/) and [load balancer](/litespeed-web-adc/). It is commercial software that requires developers to purchase a license for usage (or try out with a free starter plan). Herewith, the platform seamlessly integrates the cost of a license in accordance with the platform-distinctive [Pay-per-Use](/pricing-model/) principles and charges hourly a fraction of the total license cost. Such a structure allows you to opt-out of the deal or switch plans at any moment without any funds loss.

In the current 5.9.3 release, support of multiple new licenses was provided to give full control over the LiteSpeed instance. For this purpose, all of the LiteSpeed containers (including [LLSMP](/lemp-llsmp/)) are provided with the ***License Manager*** add-on.

![LiteSpeed license manager](01-litespeed-license-manager.png)

Add-on allows configuring license based on the following parameters:

* **Workers** - choose the number of workers, which indicates how many processes will be spawned to do general server work
* **Domains** - select the domains' limit (only refers to top-level domains), any domain that exceeds the specified limit will result in a 403 error
* **LiteMage** - enable or disable the *LiteMage Cache* (fast, full page caching solution that caches dynamic pages as static files). If activated, an additional **Options** field will appear allowing to choose between the *Starter*, *Standard*, and *Unlimited* plans (*1500*, *25000*, and *unlimited* [publicly cached objects](https://www.litespeedtech.com/products/litespeed-web-server/lsws-pricing/lsws-litemage-pricing#objects) respectively)

![configure LiteSpeed license](02-configure-litespeed-license.png)

At the bottom of the frame, you can see the cost of the current configuration. Click **Apply** to confirm changes and adjust your environment.

[More info](/litespeed-web-server/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Password Reset Enhancement

A new password reset flow was implemented in the platform 5.9.3 release. For now, after clicking on the **Reset Password** button and providing your email address, the platform will send you a confirmation email. The message has a button that redirects you (link automatically expires after three days) to the form where you can provide a new password. Additional information on the [password change and reset](/account-password-reset/) can be found in the documentation.

![reset password email](03-reset-password-email.png)

[More info](/account-password-reset/)

{{%right%}}[Back to the top](#back){{%/right%}}


## UI Improvements

* [Environment Region Icons](#environment-region-icons)
* [Error Pages Redesign](#error-pages-redesign)
* [Default Ports Proxying](#default-ports-proxying)
* [Collaboration Marketplace Section](#collaboration-marketplace-section)

{{%right%}}[Back to the top](#back){{%/right%}}

### Environment Region Icons

As the number of service hosting providers that support [multiple regions](/environment-regions/) increases, the feature gets more comprehensive feedback, allowing to improve it even further. In the current 5.9.3 PaaS release, the region icon was relocated from the environment **Name** column to the **Tags** one. Such a change serves two purposes:

* additional space within the **Name** column improves UX when working with prolonged environment names and [aliases](/environment-aliases/)
* region icon works as a label that helps to group environments, so it is rational to locate it among other [tags](/environment-groups-navigation/)

![environment region icon](04-environment-region-icon.png)

Also, clicking on the region icon now automatically filters an environment list by that particular region.

[More info](/environment-regions/)

{{%right%}}[Back to the list of UI Improvements](#ui-improvements){{%/right%}}

### Error Pages Redesign

The design of the platform default error pages was updated in the PaaS 5.9.3 release to match the latest corporate styles. Two new pages were created to help handle the ***504 Gateway Timeout*** and ***503 SSL Disabled Environment*** issues. The existing pages were also thoroughly reviewed to clarify the cause of each particular problem - the error description and recommended resolution steps were updated.

![error page redesign](05-error-page-redesign.png)

{{%right%}}[Back to the list of UI Improvements](#ui-improvements){{%/right%}}

### Default Ports Proxying

The platform provides several [ports](/container-ports/) that are open by default on all containers. These ports proxy traffic according to the following rules:

* ***80***, ***8080***, ***8686*** - proxies **HTTP** traffic to **HTTP** (*80* port)
* ***4848***, ***8443***, ***4901-4910*** - proxies **SSL** (HTTPS) traffic to **SSL**
* ***443*** - proxies **SSL** traffic is proxied to **HTTP** (*80* port)
* ***4949***, ***7979*** - proxies **SSL** traffic to **HTTP**

![default ports traffic proxying](06-default-ports-traffic-proxying.png)

In order to highlight that proxying rules are not the same for all ports, the appropriate information was added to the dashboard with the link to the corresponding documentation page.

[More info](/container-ports/)

{{%right%}}[Back to the list of UI Improvements](#ui-improvements){{%/right%}}

### Collaboration Marketplace Section

Due to the global pandemic situation, the collaboration applications have become increasingly popular. Such specialized tools can significantly reduce the negative effect of remote cooperation and hasten the establishment of a familiar workflow. Several applications within [platform Marketplace](/marketplace/) can help to keep people connected. In this 5.9.3 platform release, dedicated solutions were moved to a new **Collaboration** category. Currently, it includes three applications:

* *Rocket.Chat*
* *Jitsi Video Conferencing*
* *Mattermost Chat Service*

![marketplace collaboration section](07-marketplace-collaboration-section.png)

[More info](/marketplace/)

{{%right%}}[Back to the list of UI Improvements](#ui-improvements){{%/right%}}


## Simultaneous Installation for Multiple Auto-Clusters

The logic for creating environments that contain several **[auto-clusters](/auto-clustering/)** was improved to perform the relevant tasks in parallel. The enhancement also affects the packages installed via the **ON_ENV_INSTALL** [variable](/environment-variables/) (if several ones are provided). The exact speed boost depends on the particular topology and complexity of the installed auto-clusters/packages. For example, the *WordPress Cluster* solution from the Marketplace can be created approximately five minutes faster than it was in the previous PaaS releases.

{{%right%}}[Back to the top](#back){{%/right%}}


## Batch Mode for Mount Operations

The platform always strives to achieve maximum performance and regularly refactors code to implement new solutions and apply optimizations. In the current release, a batch mode was implemented for the [NFS mount/unmount](/mount-points/) operations. It allows performing actions in parallel, which provides a decent performance boost compared to the previous sequential mode. The batch mode is especially beneficial when a lot of simultaneous operations are requested (e.g. when working with the cluster solutions).

[More info](/mount-points/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Iptables for Bridge Interfaces in Containers

In the latest Linux kernel versions, new flags were added to either allow or forbid packets to be checked by the *iptables* rules when going through the bridge interfaces. Such functionality is critical for some solutions (for example, for the **portainer** GUI in the *[Docker Swarm](https://www.virtuozzo.com/company/blog/deploy-services-docker-swarm-cluster/)* package). The appropriate flags are automatically enabled in all platform containers to ensure the dependent services' operability (including platforms with versions preceding the 5.9.3).

{{%right%}}[Back to the top](#back){{%/right%}}


## Container Stop Operation Optimization

In the current 5.9.3 platform upgrade, the container stop action code was refactored and optimized, resulting in the notable speed up of the operation. The change ensures that container/service stop action is performed quickly and without delays, improving the user experience and general appeal of the platform.

{{%right%}}[Back to the top](#back){{%/right%}}


## Cloud Scripting Improvements

[Cloud Scripting](http://docs.cloudscripting.com/) is a programming language developed by the platform for application packaging, operation automation, and complex CI/CD flows integration. The following amendments were implemented for Cloud Scripting in the 5.9.3 platform release:

* **Rhino** JavaScript engine was updated to the latest version, resulting in a performance boost when working with the Cloud Scripting actions (e.g. JPS packages are created up to 40% faster).
* The ***[onBeforeInstall](https://docs.cloudscripting.com/creating-manifest/events/#onbeforeinstall_1)*** event was modified and now can be used with the add-ons (i.e. installations with *type: update*).
* Added a new ***permanent*** parameter for add-ons. If set as *true*, add-ons removal will be forbidden. The **Uninstall** button will be hidden on UI, and the *11043* error code will be returned via API.
* The ***force*** flag was implemented for the **UninstallApp** method. It is required to delete "*permanent*" add-ons and to force removal if the regular operation fails due to some error.
* Implemented the ***auto*** parameter (*\${event.params.auto}*), which is added for the [automatic horizontal scaling](/automatic-horizontal-scaling/) operations to distinguish them from the manual scaling.
* Automated the cloudlets' and nodes' count [values](https://docs.cloudscripting.com/creating-manifest/basic-configs/#nodes-definition) provisioning for the cases when the appropriate parameters were not defined explicitly. The algorithm takes into consideration account quotas, software requirements (e.g. for auto-clusters), and current values (for existing environments).
* Objects within the placeholders are serialized to JSON strings by default (i.e. without the [toJSON()](https://docs.cloudscripting.com/creating-manifest/placeholders/#42tojson) function).
* Implemented support of the ***[settings](https://docs.cloudscripting.com/creating-manifest/visual-settings/#custom-settings)*** placeholder for the ***extraNodes*** and ***recommended*** fields when configuring auto-cluster via JPS package. It allows passing the required settings from UI forms during the environment creation.
* The maximum allowed length for the text returned by the CS packages was enlarged to *16* MB.

{{%right%}}[Back to the top](#back){{%/right%}}




## API Changes

In the present 5.9.3 PaaS release, the [API documentation](https://www.virtuozzo.com/application-platform-api-docs/) was migrated to the new modern engine, which allows automating a version control process. New API docs are automatically generated as soon as the new platform release is prepared. The engine also helps to implement numerous optimization (e.g. improved links structure) and clarification (e.g. response deserialization) of the displayed information. If needed, it is possible to switch platform versions (via the drop-down list at the top of the website) to view API for that particular release.

![API documentation](08-api-documentation.png)

{{%tip%}}**Note:** A dedicated title page for the [API documentation](https://www.virtuozzo.com/application-platform-api-docs/) was created, allowing to switch between user and admin (authentication is required) methods. Also, all the corresponding links in the platform documentation and dashboard were updated.{{%/tip%}}

Below, you can find a list of all changes to the public API in the 5.9.3 platform version (compared to the preceding [5.8.2](/release-notes-582/#api-changes) ones):

* added a new force optional parameter for the ***[Uninstall](https://docs.jelastic.com/api/#!/api/marketplace.Jps-method-Uninstall)*** method from the **jps** service
* removed the ***GetHdNodeStat*** method from the **cluster** service

[More info](https://www.virtuozzo.com/application-platform-api-docs/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Fixes Compatible with Prior Versions

Below, you can find the fixes that were implemented in the PaaS 5.9.3 release and also integrated into previous platform versions by means of the appropriate patches.

{{%table3 title="PaaS 5.9.3"%}}
**#**|**Compatible from**|**Description**
---|:---:|---
JE-54324|3.3|The installation of the *Let's Encrypt* add-on overwrites existing cron tasks
JE-37519|5.0|The *Windows-based* nodes should not be shown via the SSH Gate
JE-53104|5.0|An error occurs when installing the *Let's Encrypt* add-on
JE-54346|5.0|An error occurs when installing the *Redmine* package
JE-52537|5.0.5|Problems with access to the admin panel on the new *HAProxy* nodes after resetting the password
JE-52703|5.0.5|The *Uninstall* option should not be available for the *Jenkins Clustrization* add-on
JE-52778|5.3|The *\$WEBROOT* variable is missing for the *Jetty* stack
JE-52786|5.3|The *\$WEBROOT* variable is missing for the *Python* stack
JE-52787|5.3|The *\$WEBROOT* variable is missing for the *NodeJS* stack
JE-52788|5.3|The *\$WEBROOT* variable is missing for the *Ruby* stack
JE-45313|5.3.2|*WildFly Cluster* ignores variables that are defined via the *variables.conf* file
JE-48491|5.4|Different display names for the *WordPress EE* package after installation and page refresh
JE-54406|5.4|An error occurs when deploying the *Gogs* project for Golang
JE-54833|5.4|An error occurs when restarting the *Golang* node with a deployed project
JE-51915|5.7|An error occurs when scaling *MariaDB Cluster* without ProxySQL node
JE-53737|5.8.1|The number of workers defined within the installation frame for the *Jenkins* package is ignored
JE-54084|5.8.1|Connection via the *Apache* load balancer with public IP fails after redeployment
JE-54241|5.8.1|The *compatibleVersionsFrom* label is absent in the *Jenkins* package
JE-54393|5.8.1|Workers are not cloned during the *Jenkins* cluster cloning
JE-54420|5.8.1|Icons for *Jenkins* should be in the *SVG* format
{{%/table3%}}

{{%right%}}[Back to the top](#back){{%/right%}}


## Software Stack Versions

The software stack provisioning process is independent of the platform release, which allows new software solutions to be delivered as soon as they are ready. Herewith, due to the necessity to adapt and test new stack versions, there is a small delay between software release by its respective upstream maintainer and integration into the platform.

The most accurate and up-to-date list of the certified [software stack versions](/software-stacks-versions/) can be found on the dedicated documentation page.

[More info](/software-stacks-versions/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Bug Fixes

In the table below, you can see the list of bug fixes applied to the platform starting from PaaS 5.9.3 release:

{{%bug-fixes title="PaaS 5.9.3"%}}
**#**|**Description**
---|---
JE-32816|Inviting yourself into collaboration should be validated on UI
JE-38799|Error when working with the reserved *Scratch* Docker image
JE-42201|Error when working with Docker images from the second and third hierarchy level of the registry
JE-42693|When connected to *SSH Gate*, the containers list disappears when the *Refresh* option is selected for the environment
JE-45673|Error during configuring *Auto-Clustering* for the existing *GlassFish* nodes
JE-45680|The errors related to the *personal access tokens* are not handled on the dashboard
JE-47141|The netmask for the internal interface is lost after using the *SwapIP* method
JE-47463|The *ExecCmdById* API method fails on the *Ubuntu 18.04* Docker image
JE-47604|The *openrc* package breaks the network in the *Alpine-based* containers
JE-49163|An error occurs when installing the *Auto-Scalable GlassFish Cluster* from the Marketplace
JE-49649|The *unfsd* process freezes during the Kubernetes redeploy
JE-49968|Unhandled error when handling cross-mounts
JE-50328|Container status should be checked before running the Docker setup procedure
JE-50993|Duplicated records for the common upstreams on the load balancers
JE-51506|Environment creation fails due to the "*Address already in use*" issue
JE-51535|Typo in the *RestoreDump* method example in the API documentation
JE-51775|Two error codes are returned upon the container redeploy failure
JE-52042|The volume folder is absent on the container after redeploy if the appropriate directory does not exist in the initial image
JE-52500|Incorrect alias is provided by default for the *extra* layers
JE-52598|An incorrect file is specified for error logs in the *my.cnf* config on the MySQL (MariaDB) containers
JE-52906|The *hidden* CS parameter does not work inside the *showIf* option
JE-53011|An error occurs when stopping a just created environment
JE-53041|The *Git auto check/deploy* options do not work with multiple projects on the same server
JE-53074|The marketplace packages selected for installation for a collaborator are still installed on the owner's account
JE-53182|The *Deploy Strategy* option is missing when deploying into the auto-clustering solution
JE-53283|Installed add-ons are not copied during the environment cloning
JE-53336|An incorrect error page is displayed for the *Gateway timeout* issue
JE-53347|Unhandled error when redeploying container that is locked by another process
JE-53355|Dependency packages cannot be installed on the *Debian 8 (Jessie)* containers
JE-53357|The Docker container start fails if the user's home directory does not exist
JE-53363|External IP is missing for the node after migration to another region
JE-53377|Response for some actions in the *Tasks* panel is missing if the task was expanded while still in progress
JE-53379|Price values are cropped on the *Refill* tab at the dashboard
JE-53380|An error occurs when installing a package with several nested add-ons
JE-53511|An error occurs during the rollback after the failed container redeploy
JE-53540|Incorrect notification pop-ups appear at the dashboard during the Kubernetes Cluster package upgrade
JE-53658|The *showmount* is not installed on the containers with the *rpcbind* utility
JE-53665|Hints for the tabs at the bottom of the dashboard should be displayed for the trimmed text only
JE-53666|The *Load Alerts* and *Auto Horizontal Scaling* tabs should be on par with other environment settings
JE-53677|Imprecise aggregation of the old *Billing History* data
JE-53692|Dependency packages are missing on the *Debian 10* based Docker containers
JE-53693|Dependency packages are missing on the Docker containers with the *multiarch-support* package requirement
JE-53776|An error occurs when importing a CS package with *NULL* action parameters
JE-53819|The "scale in" trigger does not work in accordance with the specified conditions
JE-53829|An error occurs during the *FTP* add-on installation
JE-53891|Corrupted values in the *response.out* and *globals* after the *Kubernetes Cluster* upgrade
JE-53910|An error occurs when changing the external IP addresses count
JE-53959|An error occurs upon removing a layer with any file (from that layer) opened in the dashboard's editor
JE-54020|The clone of the *Memcached* container has firewall rules for the nodes from the original environment
JE-54022|The clone of the *Memcached* container has firewall rules with internal IPs of the nodes from the original environment
JE-54028|Texts for some error pages should be improved
JE-54047|An error occurs when working with the firewall rules
JE-54154|An error occurs when creating *Jenkins* in the extra layer of the wizard
JE-54268|The VCS deployment *auto-update* option is disabled after containers redeploy
JE-54351|When deploying the *.ear* package to the same context as the existing *.war* one, the files from both archives are available
JE-54368|The after-installation notification is not displayed on the dashboard if the page was reloaded during the package installation
JE-54450|Docker containers from the custom registry cannot be created
JE-54594|Some parameters are not substituted in the Swap IP action in the dashboard's *Task* manager
JE-54602|*Ubuntu 20.04* containers cannot be connected via SSH
JE-54610|The file owner is changed upon adding a file to the Docker volume
JE-54687|The horizontal scaling element of the topology wizard is displayed incorrectly upon zooming in in the Firefox browser
JE-54794|When connected to *SSH Gate*, the containers list disappears when the *Refresh* option is selected for the environment
JE-54805|The *View Invoices* button does not work for the latest versions of the *Chrome* browser
JE-54814|Unhandled error when connected to *SSH Gate* and refreshing nodes list for the removed environment
JE-54843|The *GetEnvs* API call returns incorrect value for the *isInstalled* flag
JE-54844|An error occurs when adding a variable with a long numerical value
JE-54858|The registration form is displayed in the non-default language after redirection from the deployment confirmation link
JE-54887|The icon for the examples in API docs is broken
JE-55016|Firewall rules are empty for the VPS containers after creation
JE-55033|An error occurs when sharing multiple environments with a collaborator simultaneously
{{%/bug-fixes%}}

{{%right%}}[Back to the top](#back){{%/right%}}