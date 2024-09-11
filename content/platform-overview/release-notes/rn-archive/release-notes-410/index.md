---
draft: false
title: "Release Notes 4.10"
aliases: "/release-notes-410/"
seoindex: "index, follow"
seotitle: "Release Notes 4.10"
seokeywords: "paas, paas release notes, paas version, 4.10 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the PaaS 4.10 release."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.10

*This document is preliminary and subject to change.*  
In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS & CaaS 4.10** release:

* [Features](#features)
* [Improvements](#improvements)
* [Bug Fixes](#bug-fixes)

<a id="features"></a>
For detailed information on using any of the platform features, please refer to the [users' documentation](/).


## Features
[Environment Groups](#environment-groups)  
[Embedded Auto-Balancing & Failover Protection for Multiple Environment Entry Points](#auto-balancing-failover-protection)  
[Ability to Use Only Fixed or Flexible Pricing Model Separately](#pricing-models){{%back%}}{{%/back%}}


## Environment Groups
Environment Groups is a new management entity, which facilitates operating multiple environments though attaching special tags and applying filtering on their base. Being mainly aimed to help in structuring large amount of created (or [shared](/account-collaboration) with an account) environments, this feature can be also helpful in smart administrating of even a couple of [applications](/paas-components-definition/#application).

The process of such groups creation is based on attaching custom tags, so that separate environments can be filtered by one or more attributes (e.g. stack type, project relation, development stage, etc.). If needed, each division can be parted further into smaller subdivisions, as well as each environment can belong to multiple groups, which makes this approach truly flexible and versatile.
For this feature implementation, several major changes were applied to the user dashboard:

* a special navigation panel was added right above the environment list, where the currently displayed environment group is shown (with the full list of parent divisions if are any)
* clicking on the **Env Groups** button will display the expandable list with a tree of all created groups and separate options to show environments within a particular [region](/environment-regions) or only the shared ones. Also, it includes buttons to **Create New** and to **Manage** groups
* the new ***Tags*** column was added to the list of environments, allowing to examine the attached labels, as well as to easily edit them with the corresponding pencil icon (displayed upon hovering over)


The above-described dashboard updates also caused a few minor UI adjustments to complement the feature. Namely, the main operations buttons (i.e. **Create Environment**, **Import** and **Marketplace**) were moved to the top pane, whilst the *<How do I..?>* field was hidden under the expandable **Help** menu. Additionally, all these interactive elements (i.e. buttons and menus) were redesigned to match the new style.

{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Embedded Auto-Balancing & Failover Protection for Multiple Environment Entry Points
In order to ensure high availability of applications, as one of the most crucial points for majority of developers, the automatic traffic balancing between multiple backends through [Shared Load Balancer](/shared-load-balancer) was implemented. With such integration, load is shared evenly across several load balancer instances of a single environment (implying it was preliminary [scaled horizontally](/load-balancer-scaling)) even without attaching [Public IP](/public-ipv4) address to each container.

Upon requesting environment, the existence of the corresponding domain-dedicated *upstream* configuration on the Shared Balancer instance is checked. In case such section is absent, it will be created automatically based on environment entrypoint list, received from the appropriate request to the platform database. Herewith, in order to keep entry points list up-to-date, the upstream section is automatically removed, if some action affects the corresponding environment domain:

* load balancer node is added or scaled horizontally
* entry point container is removed from the topology
* environment is [hibernated](/resources-utilization)
* environment is [migrated in offline mode](/environment-regions-migration#offline)

Additionally, a number of special modules were added to Shared Load Balancers, they are called each time request is proxied to environment:

* *upstream* - evenly distributes traffic across the available entry points
* *sticky* - applies the default [sticky sessions](https://bitbucket.org/nginx-goodies/nginx-sticky-module-ng/overview) behavior for the connections (excluding the browser cookie name, which is set to the custom *slb_route* one)
* *healthcheck* - verifies backends availability 

[More info](/shared-load-balancer)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Support of Only Fixed & Only Flexible Pricing Models
The platform implements the most versatile [hybrid pricing model](/pricing-model), which allows you to gain [discounts](/automatic-discounts) based on the amount of reserved resources and, at the same time, do not pay for the unused capacities. And starting with the current PaaS 4.10 version, hosting providers also got the ability to implement different kinds of pricing model,  either making it obligatory to pay for the whole amount of reserved resources or implementing the completely pay-for-usage approach.

This way, from now you can notice the following distinctions while setting the amount of resources for your servers, depending on a particular platform preferences: 

* ***fixed*** - model where you pay for the whole predefined amount of cloudlets and/or disk space
Disables *Scaling Limit* slider in the *Vertical Scaling* wizard section and displays fixed price in the *Estimated Costs* details (including Storage cost for the whole specified limit).
* ***flexible*** - based on paying only for actually used capacities in confines of the set limit, whilst not providing discounts for the preliminary reserved resources
Hides the *Reserved Cloudlets* scroller and calculates *Estimating Cost* in a range from 1 cloudlet up to the specified *Scaling Limit*. The consumed disk space is also charged according to the pay-as-you-go approach.
* ***hybrid*** - benefits on mixing of the fixed and flexible options

Maintains the same behaviour as before - both reserved and dynamic cloudlets can be used, with the storage being charged according to the hosting provider settings (i.e. for either preliminary reserved or dynamically allocated space).

[More info](/pricing-model)
{{%right url="#features" text="Back to the list of Improvements"%}}{{%/right%}}


## Improvements
[Configurable Disk Limit for All Containers](#configurable-disk-limit)  
[YAML Format Support for JPS Import](#yaml-jps-support)  
[Pre-Check of Account Limits during JPS Installation](#account-limits-precheck)  
[Ability to Download Files via Server Configuration Manager](#files-download)  
[Detection of Docker Image Supportability by OS Type](#docker-image-os-type)  
[UI/UX Improvements](#ui-improvements)  
[New AddProject API Method Types for VCS Deploy](#addproject-vcs)  
[Exposed 8443 Port at Shared LB to Process Secure Requests](#exposed-8443-port)  
[Software Stack Versions](#software){{%back%}}{{%/back%}}  


## Configurable Disk Limit for All Containers
Striving to make containers even more customizable, the current 4.10 PaaS upgrade includes possibility to set the amount of available disk space for any container. Such tuning can be applied through topology wizard during environment creation or its topology change. Just click or hover over the *Disc Limit* value in the middle part of the frame to adjust it for all nodes on a layer either via slider or through typing the desired amount of space (in GB) manually.

Additionally, the *Estimated Cost* section (shown in the right part of the topology wizard) was updated to reflect the price for disk space usage according to the specified limit. Hover over to see more details: spends for the currently consumed space (starting with 1 GB for bare server) are included to the minimal &ldquo;*FROM*&rdquo; cost, while the maximum available &ldquo;*TO*&rdquo; price is calculated assuming the whole allocated disk space will be in use. Also, if you try to set amount of space over the allowed limit, the appropriate notification will be shown right above the wizard:

* *trial users* will be encouraged to [upgrade account](/upgrade-refill-account)
* *billing users* will be proposed to send a request to the Platform support team

{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## YAML Format Support for JPS Import
[YAML](http://www.yaml.org/) is a popular data serialization language, designed to be human-readable and make code easier to percept due to its slim and flexible structure. Starting with the current PaaS upgrade, the YAML syntax support was integrated to be used during [JPS packages](/jps) import to a platform (in addition to the default JSON format).
To highlight this possibility implementation, the UI part of the **[Import](/environment-import)** frame got some small updates:

* the **JSON** tab was renamed to **JPS**, so that it does not imply usage of just a single format for now
* a hint for the **JPS** tab input field was added (which is displayed when the form is empty yet), saying that you can *&ldquo;Input your JSON or YAML code here&rdquo;*

[More info](/environment-import)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Pre-Check of Account Limits during JPS Installation

[JPS](/jps) is a highly efficient tool for application delivery and automation. In the current 4.10 release it received a notable update, aimed to improve user experience greatly. For now during any solution installation from JPS manifest a special verification is performed, aimed to ensure that a package can be properly deployed and specified topology won't exceed any of the current [account limitations](/quotas-system).  
For that, the following limitations are analyzed:

* access to the [Public IP](/public-ipv4), [High Availability](/isolated-containers-migration#b) and [Built-In SSL](/built-in-ssl/) options
* maximum server size in cloudlets
* maximum number of nodes per layer
* access to the [VPS](/vps) hosting
* ability to operate VPS with internal IP
* maximum number of environments that can be created on an account

If all of these account quotas match the demand of a package, the installation process will proceed as usual, opening the appropriate confirmation window. And in case of verification failure, the corresponding frame will inform you about which limit(s) are exceeded.

Herewith, if an issue can be fixed by converting account to the billing type, the appropriate **Upgrade trial account** button will be shown; otherwise, you will be proposed to contact **Support** for assistance or to negotiate enabling of the required functionality.

[More info](/jps)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Ability to Download Files via Server Configuration Manager
Within the PaaS 4.10 version, the new ability to download files directly from [Configuration Manager](/application-configuration) was implemented for all of the supported container types. Such possibility simplifies project management via dashboard UI by allowing to freely transfer files between containers in a Cloud and your local machine.

The appropriate *Download* option was integrated to the file context menu (i.e. the expandable ***Additionally*** list, opened with the *gear* icon). In a moment, the system will generate a temporary downloading link and automatically run this operation, whilst otherwise you will be shown the appropriate error message.

[More info](/application-configuration)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Detection of Docker Image Supportability by OS Type
Currently, the platform implementation of [Docker containers support](/dockers-overview) is focused on operating with Linux-based images only. Thus, starting with the present platform upgrade, each called *Docker manifest* file is automatically checked for the appropriate OS type usage. In case it utilizes any operating system that is different from the Linux one, the platform will automatically interrupt creation of such container, providing you with the relevant *"Not supported OS template"* warning message.

[More info](/docker-supported-distributions)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## UI/UX Improvements
[Remembering Wrap State for JSON in JPS Editor](#json-wrap-state)  
[Instant Update of Environment Topology within UI after Auto Scaling](#instant-topology-update)  
[Disabling VPS without Private IP for Adding Endpoint](#vps-endpoint-addition)  
[Added Close Button for Minimized Installation Frame](#minimized-installation-frame)  


#### Remembering Wrap State for JSON in JPS Editor
Striving to improve user experience while operating [JPS packages](https://www.virtuozzo.com/application-platform-ops-docs/jps), the PaaS team has implemented an update to the built-in **JPS** code editor, available via the ***[Import](/environment-import)*** frame. For now, the system automatically detects whether YAML or JSON code format is used and, in the latter case, stores the chosen *wrap* option state in the browser *localstorage*.

With this improvement, you can stick to the preferred code view for it to be automatically applied each time the **Import** frame is opened. It is especially convenient while testing the developed packages, as this process implies repeating opening of the editor to apply the required tuning. Herewith, the *wrap* option is automatically disabled for [YAML](#yaml-jps-support) in order not to corrupt its syntax.

[More info](/environment-import)
{{%right url="#ui-improvements" text="Back to the list of UI Improvements"%}}{{%/right%}}

#### Instant Update of Environment Topology within UI after Auto Scaling
[Automatic horizontal scaling](/automatic-horizontal-scaling) is a popular platform feature, aimed to adjust the number of server nodes based on incoming load through attaching new instances upon spikes of activity and removing them when resources are idling. Such changes are performed automatically according to configurable trigger conditions, allowing to edit topology without necessity for you to be involved in this process directly.

In order to make auto scaling results visible in environment list within the main dashboard screen right after the changes are applied, the corresponding data should be pulled from a platform. This is automatically done when a you perform some operations within PaaS UI. But in case of inactivity, such topology adjustment may not be displayed, keeping you unaware on the changes made (whilst email notification is sent anyway). So, in the 4.10 platform upgrade, an additional periodic topology check up (once per 30 seconds) was implemented to compare the displayed environment topology with the actual one. Herewith, the [Tasks](/dashboard-guide/#tasks) list in the corresponding panel at the dashboard bottom will be updated as well, providing you with info on the most recent scaling events occurrence.

Also, in confines of this improvement, the **Automatic Horizontal Scalling** button was added to the [Statistics](/view-app-statistics) section for Docker containers (in the same way it's already available for the rest of node types). This allows to quickly open the appropriate settings panel in order to add or tune scaling triggers  according to the observed load data.

[More info](/automatic-horizontal-scaling)
{{%right url="#ui-improvements" text="Back to the list of UI Improvements"%}}{{%/right%}}


#### Disabling VPS without Private IP for Adding Endpoint

In order to improve user experience while working with [VPS containers](/vps), the [endpoints](/endpoints) functionality was adjusted to automatically validate nodes without internal IP attached. So, for now, such containers will be shown inactive in the appropriate list during endpoint addition. This change allows not to mislead you, as commonly virtual private servers in the platform represent the completely isolated units and should be managed through [SSH Gate](/vps-ssh-gate/) or attached [Public IP](/vps-public-ip) (or, for Windows VPS, via [remote desktop protocol](/win-rdp-access)).

[More info](/endpoints)
{{%right url="#ui-improvements" text="Back to the list of UI Improvements"%}}{{%/right%}}

#### Added Close Button for Minimized Installation Frame

While installing a [JPS solution](/jps) (either from [Marketplace](/marketplace), [one-click widget](/application-manifest/) or through [importing](/environment-import) your custom one), the corresponding frame pop-ups to track the process and display the results when it's finished. This window can be minimized with the corresponding button at the top-right corner, allowing to continue operating with dashboard.

And starting with the current Platform version, collapsed form of this frame can be also quickly **Closed** with the appropriate icon, eliminating the necessity to expand it into the full view beforehand. So in case of active UI usage or when having multiple simultaneous installations running, you can manage such processes more convenient.
{{%right url="#ui-improvements" text="Back to the list of UI Improvements"%}}{{%/right%}}
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## New *AddProject* API Method Types for VCS Deploy
With an aim to improve Java VCS projects management via [API](https://www.virtuozzo.com/application-platform-api-docs/), the ***AddProject*** method was divided into two separate calls - ***AddProjectWithCreds*** and ***AddProjectWithKey***. Correspondingly to the names, these operations allow to add projects from a private Git or SVN repository using either login / password authentication or [SSH key](/git-ssh) check up. Such divisioning provides less confusion and shortens the number of parameters to consider. Herewith, the full backward compatibility is provided, allowing to operate with both new methods and the old one.
Also a number of other small changes were implemented regarding this operation to provide a better user experience:

* parameters sequence for all of the *AddProject* methods was rearranged to group the obligatory ones at the beginning and leave optional arguments at the end
* names and descriptions of some parameters were updated to make them more clear
* the two newly added methods utilize the *targetEnv* parameter instead of the *env* one to provide better clarity and avoid possible confusion with the *envName* one

<a href="/api" target="_blank" id="exposed-8443-port">More info</a>
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Exposed 8443 Port at Shared LB to Process Secure Requests

Many of [Docker containers](/dockers-overview) with Java application server inside utilize *8443* port as the default one for establishing secure HTTPS connection. Within confines of the present 4.10 PaaS release, it was exposed via Platform [Shared Load Balancers](/shared-load-balancer), allowing HTTPS requests to access the required container even without the [Public IP](/public-ipv4) address being attached to it.

For example, such implementation simplifies access to the admin panel for Java application servers (like *GlassFish*) which are deployed inside custom Docker containers.

[More info](/shared-load-balancer)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.10|
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
|***Ruby 2.2******|2.2.5|
|***Ruby 2.3***|2.3.1|
|***Python 2.7***|2.7.12|
|***Python 3.3***|3.3.6|
|***Python 3.4***|3.4.5|
|***Python 3.5***|3.5.2|
|***Node.js***|0.10.46 / 0.12.15|
|***Node.js 4***|4.26 / 4.3.0 / 4.5.0|
|***Node.js 5***|5.1.1 / 5.6.0|
|***Node.js 6***|6.5.0|

<p style="text-align: right;" gt="" a="" href="#improvements"><a href="#back">Back to the top</a></p>


## Bug Fixes

In the table below, you can see the list of bug fixes in PaaS & CaaS 4.10:

{{%bug-fixes title="PaaS 4.10"%}}
**#**|**Description**
---|---
JE-28075|Incorrect validation of some special characters during Mount Point path addition
JE-28984|Topology Wizard is displayed improperly if its loading is interrupted with the *Esc* button
JE-29292|Incorrect endpoints data is shown within the *GetEnvInfo* CLI call output
JE-29972|Default shell is missing for *jboss/wildfly* Docker image
JE-30011|MongoDB container is not launched properly in a cloned environment
JE-30344|A long alias name overlaps region icon
JE-30493|Node layer associated icon is missing within the *Add Endpoint* tab in a full screen mode
JE-30494|The default name of a new directory is not changed within the path bar of the Config Manager
JE-30550|Environment created via the NetBeans IDE is added alongside with its unidentified copy in dashboard
JE-30587|Folder with subdirectories is not removed from the Config Manager upon deletion
JE-30603|An error occurs during undeploying context on the *Tomcat8* container  
JE-30670|An environment with cyrillic symbols in a name can not be imported after export
JE-30775|Invalid *Loading Value* is displayed for the Network trigger within the *Events History* sections
{{%/bug-fixes%}}
{{%right%}}[Back to the top](#back){{%/right%}}