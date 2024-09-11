---
draft: false
title: "Release Notes 6.3.2"
aliases: "/release-notes-632/"
seoindex: "index, follow"
seotitle: "Release Notes 6.3.2"
seokeywords: "paas, paas release notes, paas version, 6.3.2 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the platform 6.3.2 release."
---

<a id="back"></a>

# Virtuozzo Application Platform 6.3.2

*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included to the **PaaS 6.3.2** release.

{{%rn-changed%}}
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


## Fixes Compatible with Prior Versions

Below, you can find the fixes that were implemented in the PaaS 6.3.2 release and also integrated into previous platform versions by means of the appropriate patches.

{{%table3 title="PaaS 6.3.2"%}}
**#**|**Compatible from**|**Description**
---|:---:|---
JE-60688|3.3|The *Mattermost* application does not work (the "*502 Server is Down*" error) after installing from the platform Marketplace
JE-60768|5.0.5|Outdated repositories are listed in the old tags of the NGINX-based nodes
{{%/table3%}}

{{%right%}}[Back to the top](#back){{%/right%}}


## Software Stack Versions

The software stack provisioning process is independent of the platform release, which allows new software solutions to be delivered as soon as they are ready. However, due to the necessity to adapt and test new stack versions, there is a small delay between software release by its respective upstream maintainer and integration into the platform.

The most accurate and up-to-date list of the certified [software stack versions](/software-stacks-versions/) can be found on the dedicated documentation page.

[More info](/software-stacks-versions/)

{{%right%}}[Back to the top](#back){{%/right%}}


## Bug Fixes

In the table below, you can see the list of bug fixes applied to the platform starting from PaaS 6.3.2 release:

{{%table3 title="PaaS 6.3.2"%}}
**#**|**Affected Versions**|**Description**
---|:---:|---
JE-59816|-|An error occurs during environment creation
JE-60420|-|An error occurs when executing scripts via launcher on the *GlassFish* nodes
JE-60956|-|Incorrect PaaS version value in the downloadable *OpenAPI* files
JE-61053|6.3|Custom environment variables are not set on the images based on the *alpine* OS template
{{%/table3%}}

{{%right%}}[Back to the top](#back){{%/right%}}