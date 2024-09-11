---
draft: false
title: "Release Notes 5.0.5/5.0.7"
aliases: "/release-notes-505/"
seoindex: "index, follow"
seotitle: "Release Notes 5.0.5/5.0.7"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the PaaS & CaaS 5.0.5/5.0.7."
---

<a id="back"></a>

# Virtuozzo Application Platform 5.0.5/5.0.7

*This document is preliminary and subject to change.*
In this document, you will find all of the new features, enhancements and visible changes included to the **PaaS & CaaS 5.0.5-7** releases:

* [Features & Updates](#features-updates)
* [Bug Fixes](#bug-fixes)

{{%tip%}}
This Platform version also includes features and improvements, implemented within the [PaaS 4.10](/release-notes-410) intermediate release.
{{%/tip%}}
<a id="features-updates"></a>
For detailed information on using any of the platform features, please refer to the [users' documentation](/).


## Features & Updates

[Cloud Scripting Engine](#cloud-scripting-engine)  
[Support of Native Docker Containers](#native-docker-containers)  
[Conversion of Certified Stacks into Docker Templates](#certified-stacks-conversion)  
[OOM Killer Alerts](#oom-killer-alerts)  
[Warning While Importing JPS from Unknown Source](#jps-import-from-unknown-source)  
[Software Stack Versions Grouping in Topology Wizard (5.0.6)](#software-grouping-in-wizard)  
[Deployment of WAR Archives into Spring Boot via Dashboard (5.0.6)](#war-ear-deployment-for-spring-boot)  
[Software Stack Versions](#software){{%back%}}{{%/back%}}


## Cloud Scripting Engine

[Cloud Scripting](http://docs.cloudscripting.com/) (CS) is a powerful platform-developed solution for advanced automation of repetitive DevOps tasks, complex CI/CD flows and clustering configurations. Generally, it allows to predefine complex environments provisioning and their behaviour upon changeable conditions through interconnecting different [platform API](https://www.virtuozzo.com/application-platform-api-docs/) methods into operation chains. In such a way, Cloud Scripting represents a unique programming language that is optimised for Cloud hosting to simplify development and significantly reduce the implementation cost of managed services.

Representing a highly versatile tool, Cloud Scripting provides access to a wide range of automation options and tuning possibilities. They are implemented by composing a manifest file in JSON or YAML format, which describes the logic of what should happened during the application lifecycle or performed in response to a particular event. When prepared, CS code can be easily executed by [importing](/environment-import) it to the Platform and, upon the necessity, edited on a fly through the embedded JSON/YAML editor with auto formatting, errors review and debugging possibilities.

To start working with CS and to build your own custom solutions, read through the appropriate Cloud Scripting documentation. The following points may be of a major interest and importance to get started:

* [Basic Configs](http://docs.cloudscripting.com/creating-manifest/basic-configs/) - learn the minimum basis of any JSP manifest
* [Actions](http://docs.cloudscripting.com/creating-manifest/actions/) - define the required environment configurations and application behavior with a set of prescribed procedures
* [Events](http://docs.cloudscripting.com/creating-manifest/events/) - automate application workflow by binding actions to particular application lifecycle events
* [Custom Scripts](http://docs.cloudscripting.com/creating-manifest/custom-scripts/) - integrate your own scripts, written in either *Java*, *Javascript* or *PHP*, to subsequently execute them within containers
* [Visual Settings](http://docs.cloudscripting.com/creating-manifest/visual-settings/) - customize your package visual layout
* [Placeholders](http://cloudscripting.demo.jelastic.com/creating-manifest/placeholders/) - specify automatically substituted parameters to fetch the required data on environment topology, server settings, user account, etc during solution installation

Also, we recommend to examine [JPS Collection](https://github.com/jelastic-jps) and get some real case examples on what you can achieve with Cloud Scripting.
[More info](http://docs.cloudscripting.com/)
 {{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## Support of Native Docker Containers

In the present 5.0.5 PaaS version, platform starts support of Docker Community Edition hosting, with full compatibility to native Docker ecosystem. This implies that a one can deploy any containerised Docker-powered application inside the Cloud, at the same time leveraging all the inherent platform advantages like out-of-box automated scaling (both [vertical](/automatic-vertical-scaling) and [horizontal](/automatic-horizontal-scaling) ones), [pay-for-use pricing](/pricing-model) approach with [granular resource allocation](/cloudlet), ability to [choose hardware](/environment-regions) and [collaborate on a project](/account-collaboration) with other team members, etc.

To accomplish this, the platform provides two basic prepackaged solutions:

* standalone [Docker Engine](https://github.com/jelastic-jps/docker-native/tree/master/docker-engine) - can be operated as a separate instance or connected to the already existing Swarm cluster (as either *manager* or *worker* node)
* [Docker Swarm](https://github.com/jelastic-jps/docker-native/tree/master/docker-swarm) cluster - allows to set up cluster of Docker Engines with the configurable number of *manager* and *worker* nodes

Both these solutions can be effortlessly installed via [platform Marketplace](/marketplace) and include options for automatic deployment of the required service just during the creation. Upon installation, the created instance(s) can be accessed from your desktop for further management through both [Docker Machine](https://docs.docker.com/machine/overview/) or [SSH Gate](/ssh-gate).

Herewith, take into consideration that a Platform should contain an [environment region](/environment-regions) with [Virtuozzo 7](https://virtuozzo.com/products/virtuozzo/) virtualization being integrated for running native Docker containers in the platform. This technology support was also implemented within the current release, thus the appropriate hardware availability depends on your hosting provider currently. Consequently, it will be provided within all the platform partners.
{{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## Conversion of Certified Stacks into Docker Templates

Within the current 5.0.5 PaaS upgrade, platform starts the process of certified software stacks transition to dockerized containers, following the global trend of this technology adoption. Such implementation does not limit any of the existing native templates' functionality and even enlarges it with the inherent [Docker containers support](/dockers-overview) possibilities in the platform.

As one of the main advantages gained, this novelty simplifies delivery of new stack versions, which can be performed by a cluster administrator at any time by means of the corresponding Docker image tag addition. In such a way, availability of the most recent software is not bound to a particular platform upgrade anymore, whilst it's developer who decides whether the update is required and when to perform it (by means of the inbuilt [Docker container redeployment](/docker-update) functionality). This allows to resolve any vulnerability or security issue almost immediately after the official fix is provided and ensures much more flexibility during development.  
Currently, the following stacks were converted for being treated as Docker containers: *NGINX* load balancer, *Maven*, *Memcached*, *Apache PHP*, *NGINX PHP*, *Tomcat 6/7/8*, *TomEE*, *MySQL 5.6/5.7*, *MariaDB 5/10* and *Varnish*. All such dockerized templates are packaged, proven and fully managed by PaaS team. The remaining software stacks will be consequentially modified within future PaaS releases.  
In order to support this feature integration, a number of changes were applied to the dashboard UI:

* set of [function icons](/dashboard-guide/#instance) for such instances was extended with the additional Docker-dedicated ones (i.e. to access [redeployment](/docker-update) option and list of [configuration tools](/docker-configuration))
* list of engine versions in topology wizard was substituted with a number of appropriate template tags, allowing to select the required combination of software stack/engine version simultaneously (this approach was additionally improved within PaaS 5.0.6)
* [Docker configuration tools](/docker-configuration) buttons were added to be shown when the corresponding servers are chosen within wizard frame
* new ***/etc/jelastic/redeploy.conf*** file, aimed to list files and folders that should be kept during redeploy, is automatically created and added to the *Favorites* section within container [File Manager](/docker-configuration#file-manager)


Take into consideration that all abovementioned newly created containers will be built upon Dockerized templates for now, whilst the already existing servers will also remain fully operable due to backward compatibility.
 {{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## OOM Killer Alerts

The Out-of-Memory (OOM) killer is a special job for Linux-based OS, aimed to suspend the currently unimportant processes in case of a strict lack of the free RAM memory and release it for more prioritized services. The selection of the process to be killed is made based on principles of losing the minimal amount of work done and simultaneous recovering larger amount of memory. The platform utilizes OOM killer tool in all containers by default, allowing them to continue functioning even when the RAM limit is reached.

In the current 5.0.5 PaaS release, the dedicated monitoring flow was implemented, which allows to track the OOM killer activity. This functionality is optional, thus its availability is controlled by a hosting provider. If enabled, all newly created containers will be supplied with the corresponding *OOM killer* [load alert](/load-alerts). It will track the running processes interruptions and send email notification with details to the corresponding user when such are observed. The default frequency for such notifications is one hour, but it can be manually tuned up to desired period (including immediate reports) within alert settings. 
Such emails contain table with all the essential information you need to be aware of in case some important service has been affected:

* *Process Name*
* *Process ID*
* *Server*
* *Node ID*
* *Time*


Also, it provides reference to the list of possible causes and advices on solving the occured issue. Generally, upon receiving the OOM killer notification, we recommend to consider optimization of your project memory consumption and/or attach more resources through the [automatic vertical](/automatic-vertical-scaling) / [horizontal scaling](/automatic-horizontal-scaling).

In addition, the [Events History](/load-alerts#history) tab was updated to support the OOM killer monitoring implementation. Here, tools panel at top was moved into separate section in order to include the newly added filters (by *Nodes* and by *Trigger*), whilst details on the logged events are now shown upon hovering over a particular record.

[More info](/load-alerts)
 {{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## Warning While Importing JPS from Unknown Source

When [importing](/environment-import) a JPS package which is provided by third parties, you need keep in mind that versatile CS features include possibilities of custom scripts inclusion, fetching user data, etc so this operation is performed on your own risk. In order to keep you aware of this, the appropriate validation was added to the **[Import](/environment-import) &gt; URL** frame. For now, specified for import link is automatically compared with the list of trusted sources (e.g. [JPS Collection](https://github.com/jelastic-jps)). In case the match was not found, a special warning message will be displayed: *Please ensure the manifest source is trusted to avoid malefactors impact*. {{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## Software Stack Versions Grouping in Topology Wizard (5.0.6)
The platform delivers various [software stacks](/software-stacks-versions) and their actual versions for the majority of widely used releases. Due to such versatility and its continuous enlarging, the current 5.0.6 Platform version includes improved grouping of stacks within topology wizard. From now on, servers with several major versions available (e.g. *Tomcat 6*, *Tomcat 7*, *Tomcat 8* and *Tomcat 9*) are shown as a single option, whilst hovering upon it expands the list of available templates to choose.

Additionally, a number of other wizard UI changes were applied to support this enhancement:

* list of engines, that was previously shown upon hovering over the application server element at the left-hand panel, has been removed (whilst still being available alongside with other container settings in the central part of the frame)
* scrolling mechanism for the long stack lists was changed from a side slider to *up* and *down* buttons at the top and bottom of the list
* for [dockerized templates](#certified-stacks-conversion), a pencil icon was added next to the label with server stack name & version in the middle part of the wizard; it is displayed only in the editing topology mode and allows to easily **Change** template **version** by launching the [redeployment](/docker-update) frame right from the wizard

[More info](/software-stacks-versions)
{{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## Deployment of WAR Archives into Spring Boot via Dashboard (5.0.6)
Recently, the list of available [software stacks](/software-stacks-versions) within the platform was extended with a new *Spring Boot* Java application server. Designed for simple hosting of production-ready Spring applications and console Java utilities, it was automatically integrated to all platforms of 4.10 version and higher. And in confines of 5.0.6 Platform upgrade, its functionality was enhanced to support deployment of ***.war*** packages right via the platform dashboard. So, for now such Java archive types can be used as an application source (alongside with the *.jar*, *.tar.gz* and *.zip* ones), allowing to [deploy Java projects](/upload-deploy-application) into Spring Boot containers manually with the platform comprehensive GUI.
{{%tip%}}**Note:** For the preceding PaaS versions with Spring Boot stack template support, the same operation of ***.war*** archives deployment can be performed via [API](https://www.virtuozzo.com/application-platform-api-docs/).{{%/tip%}}

{{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:


|                        Stack                        |                        PaaS 5.0.5-7                        |
|---|---|
|***Tomcat 6***|6.0.48|
|***Tomcat 7***|7.0.73|
|***TomEE***|7.0.2|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_79|
|***Java 8***|1.8.0_112|
|***MariaDB***|5.5.54 / 10.1.21|
|***MongoDB 2.6***|2.6.11|
|***MongoDB 3.0***|3.2.1|
|***MySQL***|5.6.34 / 5.7.16|
|***PostgreSQL***|9.5.5|
|***CouchDB***|1.6.1|
|***nginx***|1.10.1|
|***Maven***|3.3.9|
|***Centos 7***|7.2|
|***Memcached***|1.4.24|
|***Apache***|2.4.6-40|
|***NGINX PHP***|1.10.1|
|***NGINX Ruby***|1.10.1|
|***PHP 5.3***|5.3.29|
|***PHP 5.4***|5.4.45|
|***PHP 5.5***|5.5.38|
|***PHP 5.6***|5.6.28|
|***PHP 7***|7.0.13|
|***PHP 7.1***|7.1.0|
|***Ruby 1.9.3***|1.9.3-p551|
|***Ruby 2.0.0***|2.0.0-p643|
|***Ruby 2.1***|2.1.9|
|***Ruby 2.2***|2.2.5|
|***Ruby 2.3***|2.3.1|
|***Python 2.7***|2.7.12|
|***Python 3.3***|3.3.6|
|***Python 3.4***|3.4.5|
|***Python 3.5***|3.5.2|
|***Node.js***|0.10.46 / 0.12.15|
|***Node.js 4***|4.26 / 4.3.0 / 4.5.0|
|***Node.js 5***|5.1.1 / 5.6.0|
|***Node.js 6***|6.5.0|
 
{{%right url="#features-updates" text="Back to the list of Features & Updates"%}}{{%/right%}}


## Bug Fixes

In the table below, you can see the list of bug fixes in PaaS & CaaS 5.0.5, 5.0.6, and 5.0.7:

{{%bug-fixes title="PaaS 5.0.5"%}}
**#**|**Description**
---|---
JE-30961|Cropped $PATH variable for users with* /bin/sh* and */bin/dash* shell in Debian-based Docker containers
JE-30965|The Dripstat licence key is not automatically fetched during the repeated add-on installation to another environment
JE-30972|Wrong background color for *Refresh* button in platform Marketplace when hovering over
JE-31131|The *Setting disk size* task is displayed in Task manager as an ongoing action without its actual performing when changing environment topology  
JE-31155|Inability to create environment with MSSQL database container 
JE-31187|Expanded *Regions* menu remains displayed after topology wizard is closed with Escape button
JE-31243|Installation of package from Marketplace continues despite of the previous step failure
JE-31256|The default stack for *VPS* section in all topology wizard tabs is set to Windows VPS instead of the CentOS-based one
JE-31316|The *Storage* server disk size limit is applied to other containers
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.0.6"%}}
**#**|**Description**
---|---
JE-28718|Within *Endpoints *section, the *Remove* and *Edit* buttons remain active after record edition though none of them is selected
JE-30722|Files do not appear in the destination folder after being uploaded or created via File Manager in large numbers at once 
JE-31018|Firewall is not available after enabling the corresponding user quota for an earlier created environment
JE-31541|The Cloud Scripting engine does not process relative links for the *Install* package type
JE-31569|Mount points added from storage to application server in Docker containers are not available after restarting the application server layer
JE-31612|No icon is displayed for NGINX-PHP application server
JE-31642|Infotip for the *Sequential restart delay* option does not appear in the wizard
JE-31647|The *Regions* list for a cloned environment is empty in the wizard 
JE-31689|Сustom data is processed if injected into the HTML body of a JPS source with a trusted base URL
JE-31695|The Docker* Tags* list is not displayed for custom images after the deployment/redeployment procedures
JE-31707|GUI elements sometimes flicker within the topology wizard
JE-31760|Tags of the dockerized software stacks do not change after redeployment, if the *Keep volumes data* option is disabled
JE-31813|The environment can be reached over HTTPS after switching Built-in SSL *off* and visa versa 
JE-31820|Inability to export environment with a native software stack from the VZ7 region 
JE-31823|The *Disk Limit* size remains unchanged after adjusting it via the topology wizard
JE-31854|Placeholders are not substituted within the email message, informing about the successful environment migration 
JE-31925|The MySQL phpMyAdmin web interface is accessed over HTTP instead of HTTPS after logging in
JE-31953|The undeployment of context fails for the Tomcat 8 custom stack
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.0.7"%}}
**#**|**Description**
---|---
JE-31891|Jetty 9 stack template is shown separately from the rest of this server versions in topology wizard
JE-32070|Placeholders with non-default values in Cloud Scripting packages can not be resolved
JE-32092|The *${env.url} *placeholder in Cloud Scripting packages can not be resolved
JE-32134|Environments with .*NET* application server can not be cloned
JE-32197|When importing JPS manifest from trusted repository, HTML elements in package's after-install success message are displayed as plain text
{{%/bug-fixes%}}
{{%right%}}[Back to the top](#back){{%/right%}}

