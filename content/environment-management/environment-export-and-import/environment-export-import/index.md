---
draft: false
title: "App Migration between Clouds"
aliases: "/environment-export-import/"
seoindex: "index, follow"
seotitle: "App Migration between Clouds"
seokeywords: "export, import, environment export import, migrate application, move application, change cloud, migrate project, environment json manifest, convert environment, move environment, migrate to another platform"
seodesc: "Move your environments from one PaaS installation to the different platform without any limitations using the Environment Export / Import feature. Create and download .json file with your exported environment description in order to consequently import it at another installation."
menu: 
    docs:
        title: "App Migration between Clouds"
        url: "/environment-export-import/"
        weight: 10
        parent: "environment-export-and-import"
        identifier: "environment-export-import.md"
---

# Environment Export/Import: How To Migrate Application between Clouds

{{%imageLeft%}}![environment export / import](01-environment-export-import.png){{%/imageLeft%}}

[PaaS & CaaS](https://www.virtuozzo.com/company/blog/what-is-paas-platform-as-a-service-types-explained/) is designed to provide a real freedom of choice to developers: no proprietary APIs, no necessity to adjust your applications' code before hosting, a wide variety of stacks and features available. And one of the key options that exempts our users from any lock-in is the **Environment Export / Import** feature.

It allows to easily migrate hosted applications across [available PaaS installations](https://www.virtuozzo.com/application-platform-partners/) (i.e. hosting provider platforms). In such a way, you are able to switch to the most suitable platform according to your current preferences (e.g. due to platform versions differentiation or pricing systems distinctions) at any time.

To accomplish this, you need to:

* [export](/environment-export/) your environment from PaaS installation it is currently hosted at
* [import](/environment-import/) it to the preferred target platform

{{%tip%}}**Notes:** 

* Currently, the ***Environment Export*** feature exports only topology information. The imported environment will be created from scratch without any custom data inside.
* ***Environment Export / Import*** feature to work properly, the initial hosting provider's platform should have the *7979* port opened, which is intended to be used for downloading environment source files during the import operation. Thus, depending on a particular provider's configurations, exported environments from some of our partners' platforms may be not available for importing at other PaaS installations.
* You can also use the [Environment Transferring](/environment-transferred/) option for moving your projects between different accounts of a single hosting provider platform, without the necessity to export/import them.{{%/tip%}}


## What's next?

* [Environment Transferring](/environment-transferred/)
* [Account Collaboration](/account-collaboration/)
* [Share Environment](/share-environment/)