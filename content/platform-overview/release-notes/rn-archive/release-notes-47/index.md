---
draft: false
title: "Release Notes 4.7/4.7.2"
aliases: "/release-notes-47/"
seoindex: "index, follow"
seotitle: "Release Notes 4.7/4.7.2"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included in the PaaS & CaaS 4.7 and..."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.7 / 4.7.2

*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS & CaaS 4.7** and **4.7.1-2** releases:

* [Features](#features)
* [Improvements](#improvements)
* [Bug Fixes](#bug-fixes)

For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Features
[Data Storage Container](#data-storage-container)  
<a href="#container-limits" id="data-storage-container">Actualization of Limits for Existing Containers</a>
{{%back%}}{{%/back%}}


## Data Storage Container
In the confines of PaaS 4.7 release, we are glad to present so much-awaited by lots of our customers feature - **Data Storage Container**. It represents a special type of node, intended for the part of data it comprises (named *volume*) to be shared with other server(s). This allows to benefit on better projects organization and advanced data handling possibilities, like:

* *no redundant data duplications* - just share the files among the instances they are required at
* *simplified management* - one set of configurations for multiple nodes
* *data preservation* - ensure safety of your data during application updates through storing it apparently
* *funds saving* - single data copy implies lower disk space consumption and therefore lower costs

Data storage implementation at the platform assumes usage of the network file system (**NFS**) on the storage node (server) to provide export of volumes to the remote hosts (clients). In order to set the communication and route requests between such containers, the remote procedure call (**RPC**) utility is used. Actually, the whole procedure is performed in two steps: at the first one, the data is exported (shared) from the storage container to some other instance, and at the second - the appropriate directory is mounted at a client. 

And in order to ensure the best experience while leveraging this feature, the new [Storage-dedicated node](/data-storage-container) type has been implemented. It has a number of benefits for data storing compared to the rest of container types, such as depended software being pre-installed and enlarged amount of allocated disk space (whilst its exact amount depends on a particular hosting provider's settings and can vary for different account types).

Beside that, the developed solution is applicable to all of the platform native container templates, as well as for Docker-based ones - the appropriate functionality can be accessed through the upgraded [file manager](/application-configuration) and the renewed [Docker volumes](/docker-volumes) configuration section. Herewith, the whole process is completely automated, so that you only need to add a [mount point](/mount-points) through the corresponding form. All of the further required operations (including installation of the necessary software) will be done by the platform automatically. In such a way, any container can be easily treated as either storage or client upon the necessity.

[More info](/data-storage-container)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Actualization of Limits for Existing Containers
There exists a number of limitations, which are defined by hosting service provider (e.g. limit on amount of nodes within a layer or environment, server size, network bandwidth, etc.) for each account type. They are always read and considered during the new containers creation, but, previously, their change (e.g. while upgrading an account) has not influenced the already created environments (so-called legacy ones).

Thus, during the 4.7 Platform upgrade maintenance activities, all of the existing containers will be automatically patched to match the required thresholds. Moreover, the new quotas' appliance flow was implemented, so that for now the changes made by your provider will affect not only the new containers, but all of the related ones. Herewith, if this should result in decreasing of the available disk space amount at a particular instance, the special pre-check procedure is performed, aimed to ensure that no data will be lost and at least 5GB of free disk space will remain free. Otherwise, i.e. if a new value does not meet these requirements, the quota will stay unchanged, ensuring normal container's work, so you can be confident that no a single file will be lost due to this novelty. 

As for the rest of limits, including *cloudlets per container* threshold, their alteration is applied without any pre-checks. So if you presuppose some limits changing for your old containers, it might be worth to review the appropriate apps performance after the upgrade (e.g. through the [Statistics](/view-app-statistics) section) and adjust the topology accordingly (for example, [add more nodes](/multi-nodes) for all of the requests to be processed properly).

In such a way, from now on, the new values will be instantly applied to all of your containers just after being modified (both manually by your provider or being caused by some automatic processes). In particular, this improves your experience when upgrading an account to paid version, as the enlarged limitations are to be applied to environments you've created during trial period without the necessity to re-create them<a id="improvements"></a>.
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Improvements
[Dockers Integration Enhancements (4.7 / 4.7.1)](#docker)  
[UI/UX Updates](#ui)  
[API Alias for VCS Projects Denomination](#api-vcs-projects-alias)  
[Import File Types](#import-types)  
[External Traffic Triggers](#traffic-triggers)    
[Git Module Update](#git-update)  
[New Defaults for Apache PHP (4.7.2)](#apache-php-defaults)  
[Software Stack Versions](#software)
{{%back%}}{{%/back%}}


## Dockers Integration Enhancements
[Default Entry Point](#docker-entry-point)  
[Revised & Concretized Error Messages](#docker-error-massages)   
[Volumes Path Validation](#docker-volumes)  
[Automatic Addition of Volumes during Mounting (4.7.1)](#docker-volumes-for-mounts)<a href="#docker-volumes"></a>  


#### Default Entry Point
Docker containers are usually provisioned with the predefined run options, used to determine their behaviour on the start. However, sometimes the *Entry Point* for the executing application is not mentioned within the image manifest.

So, starting with the 4.7 PaaS version, if the corresponding value is *nil* or *null* (i.e. not defined) the Platform will automatically substitute it with the default ***/bin/sh -c*** entry point. Within the appropriate [Run Config](/docker-run) section of the **Docker containers settings** frame, such one will be shown dimmed to mark that it's just a placeholder, which can be easily changed to any required custom value.

[More info](/docker-run)
{{%right url="#docker" text="Back to the list of Dockers Integration Enhancements"%}}{{%/right%}}

#### Revised & Concretized Error Messages 
Once some issue occurs during the Docker container creation, it can be hard to find out which problem it was caused by. Due to this, within the current release, we've reviewed and analyzed all of the appropriate error messages (i.e. which appear at the dashboard in such situations) for them to be more explicit and to correctly point to the root of the happened issue.

Such improvement ensures you won't be mislead by the common problem description and will learn what has actually occurred instead - i.e. whether this concerns network connection failure or usage of unsupported OS version, some temporary technical issue or authentication failure, etc. In such a way, the issue could be easily resolved<a id="docker-volumes"></a>.
{{%right url="#docker" text="Back to the list of Dockers Integration Enhancements"%}}{{%/right%}}

#### Volumes Path Validation
Previously, the semicolon &ldquo;***;***&rdquo; character was used by internal platform system processes (such as *addvolume*, *update* and *setup*) while working with [Docker volumes](/docker-volumes) as a sign to separate different volumes' paths. Thus, if being specified during the new volume addition within the corresponding ***Docker container settings*** dashboard UI frame, it had to be validated as an unallowed symbol.

Starting with the present Platform release, the appropriate system services were properly rewritten in order to get rid of such a semicolons-bounded processing. So for now the corresponding character is allowed to be used while designating Docker volumes' mounting within *Local Filesystem*<a id="docker-volumes-for-mounts"></a>.
{{%right url="#docker" text="Back to the list of Dockers Integration Enhancements"%}}{{%/right%}}

#### Automatic Addition of Volumes during Mounting (4.7.1)
In order to automatically spread the existing [Mount Points](/mount-points) (i.e. created via [Config Manager](/application-configuration)) across all the newly added nodes during [horizontal scaling](/multi-nodes) of Docker containers, previously it was needed to declare the appropriate volume at the initial (master) node of the layer manually (so subsequently its settings could be automatically copied by the system). Thus, in confines of the 4.7.1 Platform upgrade, the corresponding enhancement was implemented - for now, each mount operation (performed for Docker-based environment with the *Mount to all nodes* flag being enabled) includes an additional step of the relevant volume creation.

In such a way, while increasing the Docker containers count, mount points will be automatically cloned for new nodes of the appropriate layer, so that you do not need to perform this manually after each scaling operation.
{{%right url="#docker" text="Back to the list of Dockers Integration Enhancements"%}}{{%/right%}}
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## UI/UX Updates
[Renewed Configuration Manager](#ui-config-manager) 
[Updated Environment Sharing Workflow](#ui-env-sharing)  
[New Account Limits](#ui-account-limits)  
[Triggers Names in Task Panel](#ui-triggers-names)  
[Logs UI Amendments](#ui-logs)  
[MiB - New Memory Consumption Unit](#ui-mib)  
[Hierarchy for Resource Usage Displayment](#ui-resources-hierarchy)  


#### Renewed Configuration Manager
Within the current 4.7 PaaS release, the major update was implemented to the in-build platform [Configuration Manager](/application-configuration). For now, within the left (menu) part, you can notice 3 new main sections appeared: *Root*, *Mount Points* and *Exports*. The last two ones are devoted to the [data storage container](#data-storage-container) feature, while the first directory gives an access to the container's file system, i.e. its **ROOT** folder. 

Below these elements, you can find a special ***Favorites*** section, intended for storing shortcuts to the items you are mostly interested in (so you can easily access folders and files that are oftenly used). Depending on the container-driven technology, the following content is shown here by default:

* for native platform containers - list of the folders you have used to work with (i.e. that were normally shown within Config manager before the current PaaS upgrade)
* for Docker containers - all of locally mounted volumes (both predefined within the appropriate image manifest and customly added ones)

Nevertheless, if needed, this list can be easily adjusted on your own (i.e. through removing the existing items and/or addition of the new ones). Herewith, excluding an item from this list does not implies its physical deletion - you still can access any of them through the corresponding *Root* section.

When switching to it, you'll see the file system tree in the right-hand part of the manager, with the path string and the **Actions for the current directory** expandable list above. These options provide the following functionality:
 
* easily switch between the nested within path directories by simply clicking on any of them. Also, here you can specify the destination folder manually by typing its full location - the appropriate input field appears upon clicking on the empty space wherever at the path bar
* the action list contains a number of functions for the selected directory management, e.g. content refresh, new item creation, addition to the favorites, mounting or deletion

The file tree itself for now provides the additional information on the file size, its last modification date and type (be aware that only the *regular file* type can be edited - for that, just double-click on it or use the corresponding **Open** action). Each opened element is shown within a separate sub-tab so you can switch between them without closing the previous one, which makes it much more convenient to explore the file system. Herewith, the new **Search** option became available for the file's view/edit mode, which allows to easily find the needed information, whilst the additional *Match case* and *Regex* search options will help you even more.

[More info](/application-configuration)
{{%right url="#ui" text="Back to the list of User Interface Update"%}}{{%/right%}}


#### Updated Environment Sharing Workflow
Environment sharing functionality represents a part of the [account collaboration](/account-collaboration) feature, that allows to organize access to a single environment from different accounts. In the current release, it was amended to ensure more simple accounts management. So for now, when an owner [shares an environment](/share-environment) (available to be performed through the environment **Settings > Account Management** section), the following operations will be performed depending on the current accounts' collaboration state:
 
* ***owner and user aren't in collaboration*** - the specified user receives the "*Invite to link account*" email with the confirmation link. Upon clicking on it, the platform dashboard is opened (whilst the appropriate account will be automatically registered if it doesn't exist yet) with the owner's environment being already displayed. Herewith, a user won't receive the additional "*Access to environment(s) has been granted*" email, while owner still gets the "*Invitation has been confirmed*" one 
* ***owner and user are in collaboration*** - the entered email address will appear in the list at the owner's dashboard after the page with it is refreshed, whilst the appropriate user will receive the "*Access to environment(s) has been granted*" email. By clicking on the link within it, the dashboard will be automatically opened, with the owner's environment being already displayed

[More info](/share-environment)
{{%right url="#ui" text="Back to the list of User Interface Update"%}}{{%/right%}}


#### New Account Limits
In order to keep you informed on the existing account limitations, all of them are gathered within the corresponding ***Account Limits*** tab of the **[Quotas & Pricing](/resource-consumption#3)** information frame. Within the PaaS 4.7 release, it was complemented with a few new records due to the number of new features being implemented. Namely, the added parameters are: *Maximum disk space per node*, *Maximum disk space per storage node* and *External network bandwidth*. 

As usual, all of these values are regulated by your hosting provider and can vary depending on your account type. Beside that, the new **Contact Us** button has appeared below the list in order to make it easier for you to negotiate the current limits incrementation in case of necessity<a id="ui-triggers-names"></a>.
{{%right url="#ui" text="Back to the list of User Interface Update"%}}{{%/right%}}

#### Triggers Names in Task Panel
As a part of the platform dashboard interface, [Tasks panel](/dashboard-guide/#tasks) is used to quickly analyze the recent actions made on account, which, obviously, should be completely clear for your understanding. Thus, in the current Platform upgrade, the related to the triggers' usage records within this section were complemented with the appropriate triggers names.

Such an update becomes especially useful if considering the number of default [load alerts](/load-alerts) triggers, that are automatically set for each new environment starting from the [4.6 PaaS version](/release-notes-46#triggers-load-alerts). So for now, in case of necessity to manage them, you will know exactly which one to work with. Beside that, triggers within the [automatic horizontal scaling](/automatic-horizontal-scaling) section got their own ***hs-add-{env_name}*** and ***hs-remove-{env_name}*** names, so their addition or some settings' changing will be reflected in Task Panel accordingly.

[More info](/dashboard-guide/#tasks)
{{%right url="#ui" text="Back to the list of User Interface Update"%}}{{%/right%}}

#### Logs UI Amendments
With an aim to improve server logs perception, a number of updates was applied to the corresponding dashboard section. The most significant change here is implementation of two log's viewing modes: ***Tail*** and ***Pages***, which can be switched with the corresponding buttons at the top pane.

The **Tail** mode is used by default and is based on the auto-refresh feature, which ensures delivering of the most recent information on your environment every few seconds. This allows to track different real-time processes (e.g. installation or update) right during their execution. 

Upon switching to the **Pages** mode, you'll get access to the whole logged info that is being splitted into pages, whilst the navigation pane at the bottom allows to switch between them (one-by-one or through typing the appropriate page number). In this case, if you need to get the latest data, the file should be refreshed manually using the corresponding button right next to the navigation keys.

Among other improvements are:

* when switching between the same-typed nodes (i.e. for the [horizontally scaled](/multi-nodes) server), the currently shown log file will be opened for the destination node as well 
* container restart won't cause the logs tab closing - the connection will be re-established once the server is up again
* also, we've improved the compatibility of logs displayment in different browsers, standardized clarification message for an empty log and fixed a bunch of other minor bugs

[More info](/view-log-files)
{{%right url="#ui" text="Back to the list of User Interface Update"%}}{{%/right%}}

#### MiB - New Memory Consumption Unit
From now, the platform will utilize two types of units for the memory consumption measurement: **MiB** ([mebibyte](https://en.wikipedia.org/wiki/Mebibyte)) and **MB** ([megabyte](https://en.wikipedia.org/wiki/Megabyte)). The difference between them is all about math:

* 1 MiB = 1024 KiB (and similarly, 1 KiB = 1024 Bytes)
* 1 MB = 1000 KB (1 KB = 1000 Bytes)

So in order to avoid any miscalculations, be aware that starting with the current release, the MiB unit will be used for RAM calculation, whilst MBs - for traffic and disk space measurement. Due to this novelty, the appropriate computation logic and naming were applied everywhere at the dashboard. Obviously, the appropriate recalculations were also implemented for all of the corresponding quotas' values and network tariffs. 

Herewith, consider that the new memory calculation flow is to be applied to environments only after the 4.7 Platform upgrade, i.e. this change won't affect the previously gathered [billing data](/consumed-resources#billing).

[More info](/cloudlet)
{{%right url="#ui" text="Back to the list of User Interface Update"%}}{{%/right%}}

#### Hierarchy for Resource Usage Displayment
Striving to improve perception of resource allocation to environments, a small visual update was applied to the **Usage** column at our [dashboard](/dashboard-guide/). From now on, the smallest environment components (i.e. *containers*) have the tiniest hard disk and cloudlets icons before these parameters values, whilst the next for the size block - *layer* - has them a bit bigger (to represent that it can consist of several nodes and thus the appropriate resources values are combined). And *environments*, as a top of hierarchy, have the biggest resource icons, which values represent the overall resource usage. In such a way, this helps to percept the displayed topology and separate elements' resource consumption a bit easier.
{{%right url="#ui" text="Back to the list of User Interface Update"%}}{{%/right%}}
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## API Alias for VCS Projects Denomination
Usage of different version control systems (VCS) for project development and management is a widely spread solution, thus interaction with such services should be as simple and clear as possible. However, since the platform uses the *context* label for the deployed applications, this may rarely cause a little confusion, as at VCS it's commonly has the *project* denomination.

Due to this, in the present 4.7 release, the related to interaction with version control systems [platform API](https://www.virtuozzo.com/application-platform-api-docs/) methods got a slight improvement, aimed to avoid these terms' misleading. For now, the ***project*** parameter within the VCS API calls can be substituted with the ***context*** one as equal. Such new label can be applied for the following methods: *CreateProject*, *DeleteProject*, *EditProject*, *GetProject* and *Update*.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Import File Types
As one of the ways to create a new environment, the platform supports usage of the specially composed JSON files, that contain description of the required topology and/or application to be hosted, representing a kind of deployable &ldquo;environment image&rdquo;. Such images can be utilized through various platform features, like [import](/environment-export-import#import) (used, in the most cases, to restore the previously [exported](/environment-export-import#export) environment), one-click [installation widgets](/application-manifest/) (to deploy a new solution) or [add-ons](/marketplace#add-ons) (aimed to patch the already set up environment with some additional software).

Currently, in order to complement and extend the ability to use such environment templates (which, in particular, are highly convenient in confines of various automation processes' and DevOps scenarios' implementation), the import flow has been updated to support the ***.jps*** file type. Similarly to *.json*, it will be uploaded and, consequently, automatically executed on the Cloud to build the environment, described within it.

Also, to completely fulfil this feature, one more additional extension is now supported by the platform - ***.cs***, which stands for *source code*. Being written in C#, it is associated with the [.NET language](/deploy-dotnet-archive-url) and allows the corresponding type of environments to be automatically created and managed (obviously, if such are available at the current platform).

[More info](/environment-export-import#import)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## External Traffic Triggers
With an aim to make environments' network usage monitoring more efficient (and considering the [recently extended](/release-notes-46#triggers) triggers' functionality), this time we've added a new **Network (out ext.)** trigger for load alerts. This was dictated by the necessity to track the external traffic loading, which usage rate could not be correctly measured within the common **Network (out ext + in ext.)**, as incoming traffic is not limited (and not charged) by the platform. In addition, for the *Network (out ext.)* trigger, it became possible to measure loading not only in ***Mbps***, but also in percentage considering the network [bandwidth limit](#ui-account-limits), specified for the current account.

Based on that, a new automatic [load alert](/load-alerts) has been added to their default set, so each newly created container will contain an additional network trigger with the following conditions stated:

*network (out ext.) is &gt; 90% for 10 minutes (with 12 hours frequency)*

This allows to inform you upon the traffic usage is coming close to external network consumption limit, so you can react on the issue in time. Moreover, such a trigger type is now also used within the [automatic horizontal scaling](/automatic-horizontal-scaling) functionality, allowing to automatically increase the limit (through spreading load between the existing and newly added nodes) without any manual interferences.

[More info](/load-alerts)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Git Module Update
Within the current release, those platform servers that are able to interact with remote Git repositories (i.e. all of the non Java-based application servers and [Maven](/java-vcs-deployment/) build node) were patched to use RPM builds with the latest version of Git software, namely: *git-1.8.3.1-6.el7_2.1* and *perl-Git-1.8.3.1-6.el7_2.1*.

Such an update was forced by the recently discovered <a href="https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2016-2315" target="_blank" rel="nofollow">CVE-2016‑2315</a> vulnerability, which has been successfully fixed in the confines of the abovementioned releases. And as for all of the containers, which will be created after the 4.7 Platform upgrade, obviously they will use these new packages automatically<a id="apache-php-defaults"></a>.
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## New Defaults for Apache PHP (4.7.2)
In confines of the 4.7.2 Platform upgrade, a new flow of the optimal parameters' calculation for [Apache PHP](/apache) application server was implemented. It implies considering of CPU capacity of used hardware and amount of the available for a container resources. Such an approach brings maximum efficiency during this server usage. Here, the following formula is used:

***MaxClients** = **ServerLimit** = min(**{server_RAM}** / 30MiB, **{cores_count}** * 5)*

Due to this statement, both ***[MaxClients](/php-auto-configuration#maxclients_apache)*** and ***[ServerLimit](/php-auto-configuration#serverlimit_apache)*** values are stated equal according to the lower value among one of them, i.e.: 

* allocated to the node amount of RAM, divided by 30;
* cores number of hoster's physical server the container is placed at, multiplied in 5 times.

In such a way, the abovementioned parameters will dynamically change based on the amount of allocated cloudlets, but won't grow over the used hardware limits. 

Beside that, the ***[MaxRequestsPerChild](http://httpd.apache.org/2.0/mod/mpm_common.html#maxrequestsperchild)*** parameter for now is equal to *500* instead of the previously used *5000* value. In case you'd like to change this value to your custom one, this can be done through the corresponding ***[httpd.conf](/php-application-server-config#ab)*** file (do not forget to [Disable Automatic Configs Optimization](/php-auto-configuration#disable) beforehand).
{{%tip%}}**Note:** that legacy Apache PHP containers (i.e. created before platform upgrade to 4.7.2 version) won't be affected by this amendment in order to not to accidentally interrupt their proper workability.{{%/tip%}}

[More info](/php-auto-configuration#apache)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.7-4.7.2|
|---|---|
|***Tomcat 6***|6.0.44|
|***Tomcat 7***|7.0.67|
|***TomEE***|1.7.4|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_79|
|***Java 8***|1.8.0_92|
|***MariaDB***|5.5.47 / 10.1.10|
|***MongoDB 2.6***|2.6.11|
|***MongoDB 3.0***|3.2|
|***MySQL***|5.6.29 / 5.7.12|
|***PostgreSQL 9***|9.5.2|
|***CouchDB***|1.6.1|
|***nginx***|1.8.1|
|***Maven***|3.3.9|
|***Centos 7***|7.2|
|***Memcached***|1.4.24|
|***Apache***|2.4.6|
|***NGINX PHP***|1.8.1|
|***NGINX Ruby***|1.8.1|
|***PHP 5.3***|5.3.29|
|***PHP 5.4***|5.4.45|
|***PHP 5.5***|5.5.36|
|***PHP 5.6***|5.6.22|
|***PHP 7***|7.0.7|
|***Ruby 1.9.3***|1.9.3-p551|
|***Ruby 2.0.0***|2.0.0-p643|
|***Ruby 2.1***|2.1.8|
|***Ruby 2.2***|2.2.4|
|***Ruby 2.3***|2.3.0|
|***Python 2.7***|2.7.11|
|***Python 3.3***|3.3.6|
|***Python 3.4***|3.4.4|
|***Python 3.5***|3.5.1|
|***Node.js***|0.10.42 / 0.12.10|
|***Node.js 4***|4.3.0|
|***Node.js 5***|5.6.0|
{{%right%}}<a href="#improvements">Back to the list of Improvements</a>{{%/right%}}


## Bug Fixes

In the tables below, you can see the list of bug fixes in PaaS 4.7, 4.7.1 and 4.7.2:

{{%bug-fixes title="PaaS 4.7"%}}
**#**|**Description**
---|---
JE-21528|Success installation pop-up for Dripstat and ManageCat add-ons is empty if the dashboard is restarted during the process
JE-23221|Search field for Marketplace should skip spaces at the beginning and end of the entered phrase
JE-23404|Displayed timestamp for the statistic graphics in dashboard is shifted on one minute ahead comparing to the server response
JE-23471|During the log file refresh, its content within the corresponding section should be re-loaded as well
JE-23631|The Apply button won't become active upon using Reset to default in Run Config for Docker containers
JE-23889|Only one of the app servers is up after cloning environment with GlassFish 3
JE-23980|Help links for CLI methods are not relevant for the Platforms under 4.0 version
JE-23989|There is no help link for some of the CLI methods
JE-23990|The Learn more button within the notification about custom SSL unavailability is not working 
JE-24149|Backend fetch fails for Varnish load balancer when the first compute node is stopped
JE-24157|The VPS section is being displayed within the Change Topology frame even as this option is unavailable
JE-24251|CLI method for external IPs swap cause unhandled error if there is no Public IP address attached to environment
JE-24514|Possibility to create files and directories with the already existing names for Docker containers
JE-24758|Rarely, long environment names are splitted in two lines within the Deploy frame
JE-24820|After environment creation, the *crond* process is started with a long delay for Mongo 2.6 node
JE-24822|The *conf.d* folder is absent in Configuration Manager for the Nginx-Ruby instances
JE-25035|The Reset to default button within the Run config frame is active for the just created Docker containers based on the Alpine OS
JE-25046|Incorrect database version is installed for MongoDB 3.0.3
JE-25071|Data within the Docker containers' pseudo filesystem should not be validated
JE-25072|Same descriptions for some actions with triggers during automatic horizontal scaling
JE-25286|Incorrect warning message for the failed authorization during private Docker container creation
JE-25289|VCS Ruby project added after the old one removal is down till the manual service restart
JE-25292|The More details link to repository should not be available for private Docker containers
JE-25343|FTP add-on could not be installed on the legacy containers
JE-25354|Volume path for Docker containers should be validated
JE-25465|The settings panel remains available during the export operation being initiated
JE-25738|Engine version for the legacy Ruby containers can not be switched to 2.1.5 and 2.2.3 ones
JE-25782|Wrong iptables redirect for the exported Node.js environment after server restart
JE-25833|VCS project requirements are not installed for Python nodes during update from repository
JE-25850|The jelinit process is missing in autostart for some Docker containers
JE-25916|Incorrect data grouping by month in Billing history for time zones with negative offset value
JE-26043|Improper display of the pointing line for the fixed cloudlets pricing in Topology Wizard for new users
JE-26057|Incorrect default cloudlets values for the Docker's tab in pricing section of Topology Wizard
JE-26065|The Detailed Cost frame of the Topology Wizard should fit the screen size, when a lot of Docker containers are added to the Extra layer
JE-26126|The hint message the for Quotas & Pricing link in Topology Wizard is displayed on top of the corresponding pop-up window
JE-26128|In some cases Topology Wizard is not closed upon pressing the *Esc* button on keyboard
JE-26216|If there is no active layer in Topology Wizard, free cloudlets are not considered while calculating the estimated price
JE-26341|Error while trying to renew SSL certificate at environments with HAProxy load balancer
JE-26394|Docker-based environment topology can not be changed via CLI without volumes parameter being specified
JE-26432|Environment name is not fully visible within the Clone environment frame
JE-26454|Health check probe made by Varnish load balancer fails if there is a redirect on the backend host
JE-26504|Custom ports are not redirected on the Docker containers based on Alpine template
JE-26505|Uppercase letters in environment URL should be converted to lowercase
JE-26563|Yum packages are not installed for the *oraclelinux:6.x* Docker images
JE-26575|Incorrect yum version for *oraclelinux:6.x* Docker images
JE-26630|New volumes are not added after Docker container redeploy operation
JE-26817|The dcache value is not being recalculated after the allocation of a new amount of cloudlets
{{%/bug-fixes%}}


{{%bug-fixes title="PaaS 4.7.1"%}}
**#**|**Description**
---|---
JE-27064|Mount operations with space symbol in the client or server paths result an error
JE-27093|Mount operations with some special symbols (*&, ( ), =, [ ]*) in the client or server paths result an error
JE-27121|Docker images, based on *CentOS 6* and *Debian 7* distributions, cannot be treated as NFS clients (i.e. do not support the [mounting](#data-storage-container) operation)
JE-27159|Mounted data is not available on the *CentOS 6*-based Docker images after container restart
JE-27226|Mounted data becomes unavailable after the Dedicated Storage Container migration to a different hardware node
JE-27251|Mounted data is not available at the awakened from hibernation environment
JE-27261|In case an environment includes several mount points, the appropriate data won't be available on the cloned environment
JE-27286|*Run Command* for Docker containers is executed without considering environment variables
{{%/bug-fixes%}}


{{%bug-fixes title="PaaS 4.7.2"%}}
**#**|**Description**
---|---
JE-26611|Networking service is not started on *Alpine*-based Docker containers with attached non-local mounts after the node restart
JE-27308|*Run.log* could not be read on some Docker containers due to the dependent packages being missed
JE-27333|Mounted through mount points data is not available after the *Alpine*-based Docker containers restart
{{%/bug-fixes%}}
{{%right%}}[Back to the top](#back){{%/right%}}