---
draft: false
title: "Release Notes 4.9/4.9.2"
aliases: "/release-notes-49/"
seoindex: "index, follow"
seotitle: "Release Notes 4.9/4.9.2"
seokeywords: ""
seodesc: "In this document, you will find all of the new enhancements and visible changes included in the PaaS & CaaS 4.9 and 4.9.1-2..."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.9 / 4.9.2

*This document is preliminary and subject to change.*

In this document, you will find all of the new enhancements and visible changes included in the **PaaS & CaaS 4.9** and **4.9.1-2** releases:

* [Improvements](#improvements)
* [Bug Fixes](#bug-fixes)

For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Improvements
[Auto Horizontal Scaling for Docker (4.9) & All Certified Containers (4.9.1)](#docker-auto-scaling)  
[Delay for Multiple Containers Restart & Deploy](#sequential-restart-deploy)  
[Horizontal Scaling Support for Storage Container](#storage-container-scaling)  
[Limited Availability of Built-in SSL & Domain Binding Options](#ssl-domain-availability)  
[API Improvements](#api)  
[Software Stack Versions](#software){{%back%}}{{%/back%}}


## Auto Horizontal Scaling for Docker (4.9) & All Certified Containers (4.9.1)

Since Docker containers allow to handle almost any service inside, commonly it's rather hard to automatically predict which node type a particular instance belongs to (i.e. whether it's application server, DB, cache or storage server, etc.). In such a way, it's a user who defines a particular environment topology and decides which environment layer a container should be placed to.
 
Thus, in order to integrate the platform [automatic horizontal scaling](/automatic-horizontal-scaling) functionality support for Docker-based instances (previously available only for nodes in application server environment layer), the whole *Auto Horizontal Scaling* section was rebuilt. Now it allows to manually choose a particular node group, where automatic scaling should be applied. This can be done within the appropriate drop-down list in the top-left tools panel corner. Obviously, this list can be used only for Docker-based environments, as such selection has no point for the platform native containers, where compute node is always placed within the application server layer.

Beside that, some other amendments were implemented - now, upon switching to the *Auto Horizontal Scaling* section, you will see a table with all scaling triggers that have been applied to the environment. It provides information on the appropriate *Nodes* and layers names, with *Scaling in* (to remove nodes) and *Scaling out* (to add nodes) conditions you've specified. And the **Add**, **Edit**, **Remove** and **Refresh** buttons above this list allow to easily manage it.
 
{{%tip%}}**Note:** Each new Docker container, added to a layer upon the appropriate trigger execution (i.e. due to increased load), will be created from scratch (i.e. not being cloned from the existing one).{{%/tip%}}

<u><b>Starting with PaaS 4.9.1 release</b>,</u> automatic horizontal scaling can be applied to any environment layer, i.e. for all node types including the platform certified containers (previously, this was allowed for application server layer only).

Herewith, upon scaling out, new containers are created in the same way as during [manual adjustment](/multi-nodes) - i.e. for compute, load balancer and VPS environment layers each newly added instance will be cloned from the master one, and for the rest node types - created from scratch.

[More info](/automatic-horizontal-scaling){{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}



## Delay for Multiple Containers Restart & Deploy
When [scaling server out](/multi-nodes) within environment, you automatically gain the advanced availability for your application or service, handled inside it. This is ensured with the ***sequential restart & deploy*** mechanism. It's key point is to run the called process at nodes sequentially (i.e. one-by-one), so that when one container is undergoing the maintenance, the rest ones will remain accessible and operable. Such approach allows to perform various operations like *container restart*, *application [deployment](/deployment-guide)* (via both plain archive and VCS repo), *[Docker container update](/docker-update)* and *changing cloudlets amount* without the whole service downtime.

However, in some cases, your server instances may require some additional time to restore the full operability (for example, in order to sync sessions after restart). Thus, within the 4.9 PaaS version, this mechanism was supplemented with a special ***delay*** option, that allows to set a particular time frame between running consecutive operations at containers of a single layer.  In such a way, the appropriate procedure on each next node will be initiated only when the stated delay has passed after the same operation completion at the previous instance. The default value of such delay is *30 seconds*, but, if needed, it can be enlarged up to 5 minutes<a id="storage-container-scaling"></a>.

{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Horizontal Scaling Support for Storage Container
In confines of PaaS 4.9 release, the [horizontal scaling](/multi-nodes) feature availability was implemented for the [Dedicated Storage Container](/dedicated-storage-container) node type. So from now, you are able to handle various development scenarios that require several separate storage nodes. This allows to run some specific applications and/or achieve data redundancy.

Storage containers number can be changed through the environment wizard central pane, just as for the rest of the platform nodes. Herewith, each Storage container, added during this operation, is created from scratch (so it won't include any copied data from the already existing nodes). This ensures that you won't pay for the unrequired disk space consumption and allows to compose the exact data structure you need.
In case of opposite operation (i.e when decreasing the nodes number), the last created container will be removed from the layer. So before performing this, <u>please ensure</u> it does not contain any substantial data.

[More info](/multi-nodes)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Limited Availability of Built-In SSL & Domain Binding Options

Starting with the current platform upgrade, the **Built-In SSL** (for establishing [secure connection](/built-in-ssl/) to environment with no external domain) and **Custom Domain** options (for domain [binding](/custom-domains) and [swap](/swap-domains) functionality) will be provided only for *billing* users by default. So, you need to [upgrade](/upgrade-refill-account) your account for being granted the corresponding permissions. Herewith, hosting service <a id="api"></a>providers got the ability to control availability of this functionality on their own.
{{%tip%}}**Note:** This innovation does not refer to the [Custom SSL](/custom-ssl) availability.{{%/tip%}}

{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## API Improvements
[Review & Update of Method Descriptions](#api-methods-description)  
[&ldquo;Get&rdquo; Methods for Docker Volumes](#api-get-volumes)  
[GetStats Output Clarification](#api-getstats)  


#### Review & Update of Method Descriptions 

In order to improve [platform API](https://www.virtuozzo.com/application-platform-api-docs/) usage experience, within 4.9 PaaS release each API method was thoroughly rechecked for proper naming and presence of detailed description on what it actually performs.

Particularly, methods with &ldquo;*docker*&rdquo; string in denomination were renamed to use the &ldquo;*container*&rdquo; label instead. Also, all method overviews were rechecked and updated to fix minor inaccuracies and provide clear and comprehensive descriptions. Similarly, the detailed explanations were added for all of the comprised data objects.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}

#### &ldquo;Get&rdquo; Methods for Docker Volumes
To ensure comfortable interaction with Docker containers via [platform API](https://www.virtuozzo.com/application-platform-api-docs/), a pair of new dedicated API methods were added. To be more specific, they are aimed to retrieve information on mounted [Docker volumes](/docker-volumes):

* ***GetContainerVolumesById*** - returns the list of all Docker volumes for the specified container
* ***GetContainerVolumesByGroup*** - outputs the same data for master (i.e. initially created) node of a  particular environment layer

Integration of such methods allows to easily get specific volumes information, without the necessity to examine the overall environment response (i.e. data received with the *GetEnvInfo* call).

[More info](/docker-volumes)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}

#### GetStats Output Clarification

The platform ***GetSumStat*** and ***GetStats*** [API methods](https://www.virtuozzo.com/application-platform-api-docs/) are commonly used to retrieve statistics on average resources consumption by a particular environment during the specified period.

To make response on this methods' call easier for perception, a new *cloudletsUsed* parameter was added to their output. Herewith, it represent equivalent to the already used *chanksUsed* one (which will be still included to response for compatibility reasons), but can be easier identified by name.
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.9/4.9.1-2|
|---|---|
|***Tomcat 6***|6.0.44|
|***Tomcat 7***|7.0.70|
|***TomEE***|7.0.0|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_79|
|***Java 8***|1.8.0_102|
|***MariaDB***|5.5.51 / 10.1.16|
|***MongoDB 2.6***|2.6.11|
|***MongoDB 3.0***|3.2.1|
|***MySQL***|5.6.32 / 5.7.14|
|***PostgreSQL***|9.5.4|
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
|***PHP 5.6***|5.6.25|
|***PHP 7***|7.0.10|
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
{{%right%}}<a href="#improvements">Back to the list of Improvements</a>{{%/right%}}


## Bug Fixes

In the tables below, you can see the list of bug fixes in PaaS 4.9/4.9.1-2:

{{%bug-fixes title="PaaS 4.9"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-27119|Incorrect display of autocompleted *user/password* fields for reinstalled FTP Users add-on
JE-27369|Environments with identical aliases can't be chosen as Traffic Distributor endpoints
JE-27866|Inability to clear Search field within *File manager* and *Import &gt; JSON* editor 
JE-28132|Unhandled error for file uploading via FTP if specified link does not contain proper FTP credentials 
JE-28305|Incorrect display of some elements within the *Quotas and Pricing* dashboard window
JE-28306|Improper border color for the *Phone* combo-box within the account Upgrade frame
JE-28323|During file uploading via Configuration Manager, the *Processing...* label appears before the same-named file override has been confirmed
JE-28378|The main Memcached container service can be stopped by *OOM killer* if the allocated RAM amount is set &lt;= 128 MiB
{{%/table%}}
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 4.9.1"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-28924|Incorrect Docker nodes linking, if the */etc/host* file contains lines with 2 or more spaces
JE-29071|Admin panel is inaccessible for the *GlassFish 3* node with Java 6 engine enabled
JE-29114|Unhandled error while adding endpoint to VPS with Public IP only
{{%/table%}}
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 4.9.2"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-29414|After cloning, the newly created environment may contain nodes that were previously removed from the source environment
{{%/table%}}
{{%/bug-fixes%}}

{{%right%}}[Back to the top](#back){{%/right%}}