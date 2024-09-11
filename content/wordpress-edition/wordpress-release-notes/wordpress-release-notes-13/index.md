---
draft: true
title: "WordPress PaaS 1.3"
aliases: "/wordpress-release-notes-13/"
seoindex: "index, follow"
seotitle: "WordPress PaaS 1.3"
seokeywords: "wordpress hosting, wordpress package, wordpress cluster, wordpress paas, wordpress release notes, wordpress paas version, wordpress 1.3 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the Virtuozzo Application Platform for WordPress 1.3 release."
menu:
    docs:
        title: "WordPress PaaS 1.3"
        url: "/wordpress-release-notes-13/"
        weight: 50
        parent: "wordpress-release-notes"
        identifier: "wordpress-release-notes-13.md"
---

# Virtuozzo Application Platform for WordPress 1.3

*This document is preliminary and subject to change.*

In this document, you will find all the new features, enhancements, and visible changes included in the **WordPress PaaS 1.3** release.

The general scope of changes is the same as for the [Virtuozzo Application Platform (DevOps PaaS) 7.3](/release-notes-73/) release. All the differences are highlighted in the list below.

Improvements <u>*not included*</u> in the WordPress PaaS 1.3:

- [Ubuntu 22 Support](/release-notes-73/#ubuntu-22-support)


## Fixes Compatible with Prior Versions

Below, you can find the fixes that were implemented in the Virtuozzo Application Platform for WordPress 1.3 release and also integrated into previous platform versions by means of the appropriate patches.


{{%table3 title="Virtuozzo Application Platform for WordPress 1.3"%}}
**#**|**Compatible from**|**Description**
---|:---:|---
WP-184|any|Long environment names should be validated in the installation dialog
WP-166|1.0|LiteSpeed server cache is configured incorrectly when the *multisite* option is enabled
{{%/table3%}}


## Bug Fixes

In the table below, you can see the list of bug fixes applied to the platform starting from Virtuozzo Application Platform for WordPress 1.3 release:

{{%bug-fixes title="Virtuozzo Application Platform for WordPress 1.3"%}}
**#**|**Description**
---|---
JE-33215|An error occurs when backing up the containers during the dashboard operation
JE-51538|Slow response of the *GetEnvs* API method for environments with many external domains
JE-62454|Incorrect escaping for special characters in the environment variables
JE-62943|An error occurs if the manually created firewall set has the same name as any of the system ones
JE-62985|The platform CLI is not supported on the *Java 8* engine
JE-63031|Mandatory *appid* parameters are marked as optional in the API documentation
JE-63049|Unhandled error for the *getTemplates* API when an unknown type is specified in parameters
JE-63586|Incorrect dashboard fonts when working on the *Linux* OS
{{%/bug-fixes%}}