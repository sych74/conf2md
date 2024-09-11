---
draft: false
title: "Release Notes 4.6/4.6.2"
aliases: "/release-notes-46/"
seoindex: "index, follow"
seotitle: "Release Notes 4.6/4.6.2"
seokeywords: ""
seodesc: "In this document, you will find all of the new enhancements and visible changes included in the PaaS & CaaS 4.6 and 4.6.1/2..."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.6/4.6.2

*This document is preliminary and subject to change.*

In this document, you will find all of the new enhancements and visible changes included in the **PaaS & CaaS 4.6** and **4.6.1 /2** releases:

* [Features](#feat)
* [Improvements](#impr)
* [Bug Fixes](#fix)

For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Features
[Reselling Model](#reselling)  
<a href="#tutorial" id="reselling">Renewed Inbuilt Tutorial</a>{{%back%}}{{%/back%}}


## Reselling Model
Nowadays, the reselling approach gains more and more popularity among large hosting vendors, since at a certain stage of growth it becomes harder to provide the high quality services within the whole area of influence due to the resources' dissipation. And one of the ways to ensure the better local presence with a sufficient level of hosting services' provision is to lease out a part of hardware capabilities to smaller companies for being resold to end-users.

Such a model brings benefits for all of the types of the platform users:

* *for primary hosting services providers* - cooperative work on advertising and end-users' support can help to spare a part of company resources; simultaneously, this allows to expand the zone of influence without any quality losses and decrease user's problems' resolution time, resulting in a higher service appeal
* *for resellers* - simpler and cheaper way to start own business, leveraging the preliminary configured and tested hardware with the ready-for-usage platform already installed inside
* *for end-users* - due to competitors races, the broader variety of vendors for choice allows to decide on the exactly required Cloud hosting service with a better concern (price, support, additional services, etc.)

So, keeping in pace with modern tendencies, the platform implements a new reselling solution within the 4.6 release. Being inbuilt to the default platform functionality, it allows to speed up and simplify the resellers' addition process, making it much more smoother.

After a new reseller creation, the dedicated platform becomes accessible under the allocated domain name. Herewith, a set of standard settings will be copied from the parent hosting installation, for the new sub-platform to be delivered as a ready-to-use solution. Nevertheless, resellers can adjust the provided platform's settings (excluding the hardware, marketplace and localization management possibilities, which are to be handled by primary hosting provider) up to their needs.<a id="tutorial"></a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}

## Renewed Inbuilt Tutorial
With an aim to increase the comprehension of the platform pricing system and to give new users better insights on the provided benefits, the inbuilt dashboard's tutorial was enhanced with a short presentation. Within these slides, the most crucial advantages of PaaS & CaaS are visualized in an interactive way:

* *The Benefits of DevOps Platform* - list of the most prominent features with clarifying illustrations, that are displayed upon hovering over a particular point; in addition, clicking on a particular item will redirect you to the corresponding documentation page
* *Pricing Advantage of Public Cloud* - this slide reveals the general concept of the truly fair &ldquo;pay-as-you-go&rdquo; [dynamic pricing](/pricing-model), provided by the platform, comparing it with the commonly applied at other vendors &ldquo;pay-for-limits&rdquo; one
* *Save Money with Smart Pricing* - here we show in details how the charging is performed, being based on the actually consumed resources amount instead of paying for whole scaling limit; a special **Estimated cost** line to the right allows to choose different time period for the approximate cost calculation

{{%tip%}}**Note:** In the confines of this update, such time period (*hour*, *day*, *month*) [switcher for pricing](#ui-pricing) was also added to the default environment topology wizard for better clarity and ability to predict the estimated expenses.{{%/tip%}}

After you get acquainted with the presented basic information, the interactive step-by-step dashboard guidance will help you to create your very first environment and deploy an example &ldquo;Hello World&rdquo; application to it. The whole process will take just a few minutes, giving a better understanding of the product you are going to work with.  

The introductory tutorial is to be started automatically for each Platform user on the first signing in (herewith, due to update, the presentation part will be also shown once for already existing users) or, if required, can be called again by selecting the **Help &gt; Show Tutorial** option at the top pane.<a id="impr"></a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}

## Improvements
[Docker Containers Support Enhancements](#docker)  
[Triggers Enhancements](#triggers)  
[UI Improvements](#ui)  
[API Amendments](#api)  
[New PHP Auto-Configurations Workflow](#php-auto-configs)  
[Swap Domains Amendment](#swap-domains)  
[Twisted Update for Gateway](#twisted)  
[Timeout for the GIT Processes with Expect](#expect-timeout)  
<a href="#software" id="docker">Software Stack Versions</a>{{%back%}}{{%/back%}}


## Docker Containers Support Enhancements
[Scaling & Monitoring Triggers Support](#docker-triggers)  
[Favorite Docker Images](#docker-favorite)  
<a href="#docker-linking" id="docker-triggers">Linking Amendments for Multiple Containers (4.6.1)</a>  
[HTTP Port Auto-Redirect Control (4.6.2)](#docker-port-redirect)<a href="#docker-linking"></a>   
  
  
#### Scaling & Monitoring Triggers Support  
Continuously improving the Docker containers' integration to the platform, our team strives to make their usage inside the Cloud as simple and comfortable as possible. Thus, this time we've extended the range of supported stacks for special monitoring triggers with Docker-based solutions. In such a way, the corresponding [automatic horizontal scaling](/automatic-horizontal-scaling) and [load alerts](/environment-triggers) functionality became available for Docker containers (including the [newly implemented](#triggers) within this release possibilities), and can be handled just in the same way as for the rest of the nodes.

<a href="/automatic-horizontal-scaling" target="_blank" id="docker-favorite">More info</a>
{{%right%}}[Back to the list of Docker Containers Support Enhancements](#docker){{%/right%}}

#### Favorite Images

With an aim to make the usage of the platform in general and Docker containers in particular more convenient and user-friendly, we've added a special tab for your most favorite images to the dedicated Docker section at both [environment wizard](/setting-up-environment#docker) and [Marketplace](/marketplace#dockers) frames. Here, you can to store any image for being easily accessible, so it can be consequently deployed in no time.

The process of image addition to the list of favorites is fairly simple - just find the template you like (either within the *Search* or *Custom* tab), hover over it, and click on the star icon in the upper-right corner of the expanded plank. The star sign will become permanently highlighted to mark that this Docker container is included to the ***Favorites*** tab, whilst the repetitive clicking on it will remove an image from the corresponding list.

Herewith, information on the elected images is to be stored either in browser's *localStorage* (commonly supported by most of them) or, if this functionality is unavailable, inside *sessionStorage* (in this case, the data will be lost once the corresponding tab is closed).



<a href="/dockers-management" target="_blank" id="docker-linking">More info</a>

{{%right%}}[Back to the list of Docker Containers Support Enhancements](#docker){{%/right%}}

#### Linking Amendments for Multiple Containers (4.6.1)

In the confines of the platform 4.6.1 update, a number of improvements were applied to the [Dockers linking](/docker-links) procedure, aimed to make it more explicit while operating with several same-typed nodes.

For now, when linking a layer with multiple containers inside (i.e. for the server that was [scaled horizontally](/multi-nodes)), the number of links with different aliases - according to the ***{alias}_***, ***{alias}_1_***, ***{alias}_2_***, &hellip; , ***{alias}_N_*** format - are created. Here, the ***alias*** value is the one you've specified during the link addition, and ***N*** is equal to the amount of containers within a layer. Herewith, the first alias (i.e. the one without the digit at the end) is general and represents a common pointer to all layer nodes, where a particular one is chosen with the round robin mechanics upon requesting. The rest of the aliases are generated through the simple incrementation of the ending number and are assigned to each container separately.

Such denomination is used to differentiate [variables](/docker-variables) of separate containers, so that they can be adjusted severally. Also, upon linking, a number of separate records (according to the amount of containers in the layer the link was set from) for all of the abovementioned aliases are added to the **/etc/hosts** file and internal DNS database, which allows to resolve node's IP via the assigned names. 

<a href="/docker-links" target="_blank" id="docker-port-redirect">More info</a>
<p style="text-align: right;">[Back to the list of Docker Containers Support Enhancements](#docker)

#### HTTP Port Auto-Redirect Control (4.6.2)
By default, the platform automatically detects the ports, that are predefined to be listened by an application within the appropriate Docker image settings, and [applies the required redirects](/release-notes-40#dockers-port-redirect) to ensure container's accessibility right after the deployment. However, in some cases, such a behaviour is undesirable (e.g. to prevent the admin panel to be accessible from outside due to security reasons).  

Due to this, in the PaaS 4.6.2 release a special functionality was implemented, which allows to manually setup the required port *80* redirect right during the Docker container creation. For that, a special ***JELASTIC_EXPOSE*** [variable](/docker-variables) should be used, with the following values as possible:

* *0* or *DISABLED* or *FALSE* - to disable auto-redirect
* a number within the *1-65535* range - to define the required port for setting the corresponding redirect

Herewith, if any other value is stated, the auto-redirect functionality will work as usual

[More info](/docker-variables)

<p style="text-align: right;"><a href="#docker" id="triggers">Back to the list of Docker Containers Support Enhancements</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}

## Triggers Enhancements
[Tracking New Types of Resources](#triggers-types)  
<a href="#triggers-load-alerts" id="triggers-types">Load Alerts Improvements</a>  
[Auto Horizontal Scaling](#triggers-auto-scaling)  

#### Tracking New Types of Resources
Triggers at the platform represent a special monitoring tool, used to track the deviations in resource consumption. They allow to either warn you about reaching/coming close to the resource limit through the corresponding email notifications (with [load alerts](/environment-triggers)) and/or to automatically adjust the topology upon spikes/drop downs of the incoming load (by means of [automatic horizontal scaling](/automatic-horizontal-scaling)). And in the present release, a few new types of triggers were added, providing the ability to monitor *network*, *disk I/O* and *disk IOPS* usage. This allows to receive more complete information on your environments and ensures better control on consumption.

In addition, all of the operations with triggers (i.e. adding, editing, changing their state and deleting) were added for being detailed tracked and displayed via the **[Tasks](/dashboard-guide/#tasks)** dashboard panel.

Beside that, such triggers functionality was also implemented for [Docker containers](#docker-triggers), allowing to monitor the changes in their load just in the same way as for the rest of nodes at the platform.

<a href="/automatic-horizontal-scaling" target="_blank" id="triggers-load-alerts">More info</a>
{{%right%}}<a href="#triggers">Back to the list of Triggers Enhancements</a>{{%/right%}}

#### Load Alerts Improvements

In the current 4.6 release, the existing [load alerts](/environment-triggers) functionality was majorly updated in order to make it more handy and convenient in usage. Foremost, the new **Notification frequency** option was added to triggers' settings, which defines the interval for the repetitive messages to be sent. This allows to determine the importance of issues by your own, stating to receive alert notifications upon crucial points more often, whilst not being flooded with emails of minor severity.

The second amendment is a set of default alert triggers, added for the main resources' (i.e. *RAM*, *CPU*, *disk* and *inodes*) consumption monitoring. For now, each newly created node is delivered with a number of already configured load triggers, so you will be automatically notified in case the current application load almost exceeds the stated resource limit (herewith, the availability of this functionality and levels of consumption for notification at a particular PaaS installation depend on hosting provider settings). In such a way, it's ensured that you can properly react on time to cover the corresponding resources' usage spikes (for example, by rising the [scaling limit](/automatic-vertical-scaling)). However, if you don't want to get such notifications, it's still possible to disable triggers manually (or just to adjust their parameters) within the corresponding ***Monitoring > Load Alerts*** section of the environment **Settings** at dashboard
{{%tip%}}
**Coming soon:** The default load alert trigger for traffic monitoring is planned to be added within upcoming releases.
{{%/tip%}}

[More info](/environment-triggers)
{{%right%}}<a href="#triggers">Back to the list of Triggers Enhancements</a>{{%/right%}}

#### Auto Horizontal Scaling UX Update

The <i>**Monitoring &gt;** [Auto Horizontal Scaling](/automatic-horizontal-scaling)</i> section, accessible within the environment **Settings** menu, also got a great visual update in the confines of present PaaS release. According to the addition of [new types of triggers](#triggers-types), the appropriate three new tabs (namely - *Network*, *Disk I/O* and *Disk IOPS*) were added to the top pane, allowing to set automatic scaling based on these resources consumption.
As for the corresponding section's UI enhancements, borders of the **Add/Remove Nodes** panes are now highlighted in orange/blue respectively, that ensures better separation and perception. Beside that, we've added the enable/disable checkboxes right near these planks' names in order to simplify the control of triggers state. Also, another new field was added to settings plank, allowing to configure the upper/lower limit in percents (or in *KB/s* for the **Network** tab) through typing the exact number into it instead of moving the rollers to the right.

The graph section got a few visual updates too - in particular, the resource value scale was moved to the right, some labels were renamed and vertical zooming was disabled. All of these amendments allow to provide more plain output and simplify the usage of the platform auto horizontal scaling feature in general.

[More info](/automatic-horizontal-scaling)
{{%right%}}<a href="#triggers" id="ui">Back to the list of Triggers Enhancements</a>{{%/right%}}
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}

## UI Improvements

[Marketplace Enhancements](#ui-marketplace)  
[Renewed Wizard Notifications](#ui-notifications)  
[Wizard Pricing Section Update (4.6.1)](#ui-pricing)  

#### Marketplace Enhancements
In order to highlight the importance of the inbuilt platform [Marketplace](/marketplace) as a unique tool for simplifying the applications' delivery process, the appropriate dashboard tab it was previously displayed at has been moved to a separate dedicated frame in the present 4.6 release. In such a way, all of the available functionality can be fully displayed, making it easier to access and more convenient to use. Apart from that, a number of other improvements were applied to make the experience of Marketplace usage even better, in particular:

* the special **Favorites** tab was added to the ***Apps*** section, which is [similar](#docker-favorite) to the one, implemented for Docker containers. In this connection, each package got the corresponding **Add to (Remove from) Favorites** star-shaped switcher, which is shown within the expandable plank upon hovering over the particular application in Marketplace and at the installation confirmation frame;
* all of the apps' categories and assigned to them packages have been completely rearranged to apply better grouping and, in such a way, to shorten the amount of presented sections.

<a id="ui-notifications" target="_blank" href="/marketplace">More info</a>
{{%right%}}<a href="#ui">Back to the list of UI Improvements</a>{{%/right%}}

#### Renewed Wizard Notifications

Within the current release, the design of pop-up notifications at [environment wizard](/setting-up-environment) was actualized in order to match the current platform style. Texts of these messages were also thoroughly reviewed and edited to make them more plain, easier to perceive and to provide clarification on which actions are required/can be performed further

Beside of that, the comprised within these notifications links were moved to the appropriate action buttons (like **Contact us**, **Upgrade**, etc.). Such ones were integrated to all of the notifications about reaching the default [account limits](/quotas-system) for you to be able to negotiate restriction(s) removal (upon either account conversion to billing type or contacting your hosting provider's support).
{{%right%}}<a href="#ui">Back to the list of UI Improvements</a>{{%/right%}}

#### Wizard Pricing Section Update (4.6.1)

In order to improve the visualization of expected charges while building new environment's topology, the corresponding [Resources](/setting-up-environment#summary) section at the right part of environment wizard was majorly updated. First of all, for now it includes the designation of a cloudlet size at the very top of the frame, providing info on its resource equivalent (i.e. 128 MB of RAM and 200 MHz of CPU), which helps to avoid the possible confusion. The **From** and **To** lines below contain information on the amount of allocated *Reserved Cloudlets* and *Scaling Limit* (i.e. flexible cloudlets) for every environment layer (with the appropriate digits being varied in colors) and their sum for the whole environment. 

The **Estimated Cost** option a bit lower allows to switch between *hourly*, *daily* and *monthly* periods for the price calculation. Changing the option here is instantly reflected at the renewed resources scale, which represents data on the expected charges based on the number of stated cloudlets.

Herewith, information on the received discounts for both types of cloudlets was moved to the pop-up plank, which appears upon hovering over the above mentioned resources scale. This plank also provides the details on estimated costs for every node separately and a few useful links at the bottom, with the *How to track your spending *video guide and information on *Storage* and *Traffic* costs.

Beneath, you can find the additional data on the platform pricing - a small tip-box with a few advices on resource usage specifics, reference to the *Quotas & Pricing* frame and link to the *How Pricing Works* documentation page with details on its distinctions and proper appliance.

{{%right%}}[Back to the list of UI Improvements](#ui){{%/right%}}{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}

## API Amendments
In order to make the [platform API](https://www.virtuozzo.com/application-platform-api-docs/) usage (as well as [platform CLI](/cli)'s one) more convenient, it was decided to remove the case sensitivity for all the methods, their parameters and values in the present 4.6 Platform release. This allows to work with API a bit faster, since you don't need to check whether your input has a proper upper or lower register. Herewith, for those of developers who got used to the old style, we've left the possibility to specify the requests in any preferable form - this does not bring any difference except of better perception.

Also, the proper names for **intIp** and **extIp** parameters were updated with new values (***intIP*** and ***extIP*** respectively).

<a href="https://docs.jelastic.com/api/" target="_blank" id="php-auto-configs">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}

## New PHP Auto-Configurations Workflow

The platform uses a special solution for [PHP application servers' auto configuration](/php-auto-configuration), where one of the controlled parameters is a number of running processes. Previously, it was dynamically adjusted according to the volume of assigned resources. Within the 4.6 release, this flow has been changed to more profitable *ondemand* one, i.e. when processes are spawned only as they are actually required.

Moreover, the maximal amount of PHP workers is now configured to be equal to the number of physical CPU cores rather than being calculated based on the amount of allocated cloudlets. Since incrementation of workers count brings performance boost only in case currently all of them are not able to use the whole (100%) CPU powers, this newly applied approach allows to receive more efficient output, where all cores are in use and, at the same time, aren't besieged by redundant workers.

In such a way, for now the corresponding settings' values for PHP app servers are the following:

* ***Apache*** (**conf ><i>[httpd.conf](/php-application-server-config#ab)</i>**)
    * ServerLimit = *{cores_count}*
    * MaxClients = *{cores_count}*
    * StartServers *1*
    * MinSpareServers *1*
    * MaxSpareServers *3*
    * MaxRequestsPerChild *5000*
* ***NGINX*** (**etc > <i>[php-fpm.conf](/php-application-server-config#1)</i>**)
    * max_children = *{cores_count}*
    * m = *ondemand*
    * m.max_requests = *5000*
    * m.process_idle_timeout = *60s*

{{%tip%}}**Note:** that legacy Apache and NGINX containers (i.e. created before platform upgrade to 4.6 version) won't be affected by this amendment in order to not to accidentally interrupt their proper workability.{{%/tip%}}

<a target="_blank" href="/php-auto-configuration" id="swap-domains">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Swap Domains Amendment
The [swapping domains](/swap-domains) functionality provides the ability to perform an easy exchange of domain names, that are bound to different environments. This can come in handy in different cases, including handling of complex DevOps operations during [application lifecycle management](/how-to-manage-application-lifecycle/) (i.e. for switching between testing and production servers).

Though claiming to cause no downtime, the swap operation appears to include almost invisible time frame, when the old record at the platform [Shared Load Balancer](/shared-load-balancer)'s base is already deleted, whilst the new one has not been added yet. Requests, that arrive in this particular moment, will return the &ldquo;*host not found*&rdquo; response and won't be processed properly. In order to eliminate this functionality gap, operations of the corresponding DNS records' addition and removal were replaced with the procedure of their values update (i.e. switching), which allows to minimize the caused downtime so almost no one request will be lost.

<a href="/swap-domains" target="_blank" id="twisted">More info</a>

{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Twisted Update for Gateway

The platform uses the Twisted event-driven networking engine (its [Conch](http://twistedmatrix.com/trac/wiki/TwistedConch) module in particular) for implementation of nodes' accessing via [SSH Gateway](/ssh-overview) and terminal emulation. Within the current platform release, this tool's version was updated to the latest *15.5.0* one. Mainly, this was done for the Conch module to support the newest key exchange mechanisms, like:

* *the diffie-hellman-group-exchange-sha256 key exchange algorithm*
* *the diffie-hellman-group14-sha1 key exchange algorithm*
* *the hmac-sha2-256 and hmac-sha2-512 MAC algorithms*

This assures that SSH connection to the platform containers can be properly established by all of Platform users. The rest of changes and amendments, provided within Twisted of *15.5.0* version, can be found in its official [release notes](https://twistedmatrix.com/trac/browser/tags/releases/twisted-15.5.0/NEWS?format=raw).  
<a id="expect-timeout" target="_blank" href="/ssh-access">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Enlarged Timeout for GIT Processes
At the platform, all the interaction with remote Git repositories is handled with the help of special [Expect](http://expect.sourceforge.net/) extension. Among other functions, this tool provides the ability to control the timeouts of requests/responses for different VCS processes.

The previously used timeframe value for such operations' completion appeared to be too short (as, rarely, excess of this limit by some long-time post-merge hook processes could cause a failure, especially with the [auto-update](/git-svn-auto-deploy) interval stated too low). Therefore, in the PaaS 4.6 Platform version, the appropriate timeout value was increased from *10* to *60* seconds, ensuring that all of corresponding tasks will have enough time to be finished.

{{%tip%}}
**Coming soon:** This parameter is planned for being made customizable by users within the upcoming releases.
{{%/tip%}}
<a id="software" target="_blank" href="/git-svn-auto-deploy">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.6|PaaS 4.6.1
|---|---|---|
|***Tomcat 6***|6.0.44|6.0.44|
|***Tomcat 7***|7.0.67|7.0.67|
|***TomEE***|1.7.1|1.7.1|
|***Jetty 6***|6.1.26|6.1.26|
|***GlassFish 3***|3.1.2.2|3.1.2.2|
|***Java 6***|1.6.0_45|1.6.0_45|
|***Java 7***|1.7.0_79|1.7.0_79|
|***Java 8***|1.8.0_72|1.8.0_72|
|***MariaDB***|5.5.47 / 10.1.10|5.5.47 / 10.1.10|
|***MongoDB 2.6***|2.6.11|2.6.11|
|***MongoDB 3.0***|3.2|3.2|
|***MySQL***|5.6.29 / 5.7.10|5.6.29 / 5.7.10|
|***PostgreSQL 9***|9.5.1|9.5.2|
|***CouchDB***|1.6.1|1.6.1|
|***nginx***|1.8.1|1.8.1|
|***Maven***|3.3.9|3.3.9|
|***Centos 7***|7.2|7.2|
|***Memcached***|1.4.24|1.4.24|
|***Apache***|2.4.6|2.4.6|
|***NGINX PHP***|1.8.1|1.8.1|
|***NGINX Ruby***|1.8.1|1.8.1|
|***PHP 5.3***|5.3.29|5.3.29|
|***PHP 5.4***|5.4.45|5.4.45|
|***PHP 5.5***|5.5.32|5.5.32|
|***PHP 5.6***|5.6.18|5.6.18|
|***PHP 7***|7.0.3|7.0.3|
|***Ruby 1.9.3***|1.9.3-p551|1.9.3-p551|
|***Ruby 2.0.0***|2.0.0-p643|2.0.0-p643|
|***Ruby 2.1***|2.1.8|2.1.8|
|***Ruby 2.2***|2.2.4|2.2.4|
|***Ruby 2.3***|2.3.0|2.3.0|
|***Python 2.7***|2.7.11|2.7.11|
|***Python 3.3***|3.3.6|3.3.6|
|***Python 3.4***|3.4.4|3.4.4|
|***Python 3.5***|3.5.1|3.5.1|
|***Node.js***|0.10.42 / 0.12.10|0.10.42 / 0.12.10|
|***Node.js 4***|4.3.0|4.3.0|
|***Node.js 5***|5.6.0|5.6.0|

{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Bug Fixes

In the tables below, you can see the list of bug fixes in PaaS 4.6, 4.6.1 and 4.6.2:

{{%bug-fixes title="PaaS 4.6"%}}
**#**|**Description**
---|---
JE-19676|Improper redirect to the administration panel at the GlassFish 3 start page
JE-23010|Crash report appears when trying to create a VPS node under the account with this possibility being restricted
JE-23025|Error while deploying or creating VCS projects
JE-23042|Error while deploying from archive to the Apache PHP node
JE-23059|Crash report appears when trying to deploy any .zip package to PHP application server due to the *php-common-deploy.lib* being missed
JE-23060|Error after the second update of the VCS projects
JE-23281|The &ldquo;Image corrupted&rdquo; error occurs while removing the mounted Docker image
JE-23707|File manager doesn't work after the */bin* folder removal
JE-23736|Incorrect operation description in the Task manager after renaming */bin/bash* for Debian-based Docker images
JE-23835|The exported environment's manifest do not include the auto-deploy update parameters for VCS
JE-23848|Error while adding two same Docker images to the custom list
JE-23859|Possibility to add a node to the improper environment layer by means of the appropriate API request
JE-23895|Unability to add endpoint for Windows-based node with the enabled firewall
JE-24103|Incorrect record inside the */etc/passwd* file for Apache application server
JE-24320|Errors while enabling the *Pagespeed* module for Apache due to the inability to write files into the required folders
JE-24524|Unability to create new Ruby Rails apps at Apache/NGINX Ruby node after deletion of the default ones
JE-24531|Platform CLI methods can't be called from the subfolder without stating the full path to the *~/jelastic* subfolder
JE-24534|Crash report appears when trying to delete a VCS projects after it has being edited through the Configuration Manager
JE-24803|Crash report while trying to add an SVN project, if URL to it was specified with the right mouse button click &gt; Paste option
JE-24808|Domain names with the umlaut special characters match to domains without such ones
JE-24814|Readonly variables are displayed in *.bashrc* of the Ubuntu Docker template
JE-24815|Docker nodes are not added according to the corresponding auto-horizontal scaling settings
JE-24851|Legacy containers with PHP 7.0.1 have no option to switch to the latest 7.0.2 version
JE-24917|Some Docker images cannot be deployed due to the big-sized variables
JE-25052|Inability to establish the direct SSH connection to some Docker containers via SSH Gateway using the appropriate node ID
JE-25125|An error occurs while enabling the *mssql.so* module for Apache
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 4.6.1"%}}
**#**|**Description**
---|---
JE-23854|Marketplace frame size is not adapted for some resolutions
JE-25316|In some cases Custom SSL warning wizard notification appears even when the requirements are satisfied
JE-25675|Tutorial tooltip position isn't changed due to the changed wizard location
JE-25736|NodeGroup for some triggers becomes equal to NULL after 4.6 update
JE-25779|Freezing of the Docker container redeployment operation
JE-25837|External IP is saved as an variable within the */etc/jelastic/environment* file
JE-25847|Docker link alias name is transformed into uppercase in the */etc/hosts* file
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 4.6.2"%}}
**#**|**Description**
---|---
JE-13676|The &ldquo;*script not found*&rdquo; error occasionally appears during some of the account/environment management operations after platform upgrade
JE-21044|Unability to add/edit Maven projects in case of the compute node absence in the environment
JE-25284|Sometimes the *jelinit* service is run twice on the first container start for Ubuntu-based Docker images 
JE-26137|Overriding the predefined Docker images' TCP ports with the services already running at
JE-26224|Encoding of special characters within the add-on installation pop-up frame in case its manifest contains the *license.url *parameter
JE-26288|Sometimes, new environments are not displayed at dashboard after being successfully created
JE-26297|Docker container variables with the digit assigned to a node within alias should not be exported during linking
JE-26299|Java 7 should be set as the default engine version for Maven node while creation
JE-26437|Environment variables, that are defined within JSON and contain a part of other variables' names within their values, aren't initialized
{{%/bug-fixes%}}

{{%right%}}[Back to the top](#back){{%/right%}}