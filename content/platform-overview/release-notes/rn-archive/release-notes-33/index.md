---
draft: false
title: "Release Notes 3.3/3.3.1"
aliases: "/release-notes-33/"
seoindex: "index, follow"
seotitle: "Release Notes 3.3/3.3.1"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included in the PaaS 3.3/3.3.1."
---

<a id="back"></a>

# Virtuozzo Application Platform 3.3 / 3.3.1
*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS 3.3 / 3.3.1** releases:

* [Features](#feat)  
* [Improvements](#impr)  
* [Bug Fixes](#fix)  

<a id="feat"></a>For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Features
[Multiple Environment Regions](#multi-regions)  
<a href="#endpoints" id="multi-regions"><span>Endpoints</span></a>  
[I/O Usage Monitoring & Updated Statistics](#io-statistics)  


## Multiple Environment Regions
Providing impressive flexibility, today platform starts to remove the geographical constraints of cloud hosting, making it truly universal through giving hosting service providers the possibility to aggregate various types of hardware within the confines of a single platform. Being named **regions**, each of such hardware sets may have a different capacity, pricing and location, allowing you to:

* choose between higher quality or more cost affordable hardware due to storage tiering
* easily migrate environments between regions in order to instantly adapt to new conditions and requirements
* achieve higher availability through distributing your applications among several regions in different datacenters throughout the globe, simultaneously working with a single platform and account

The preferred region for your project's hosting (in case your hosting provider have added several) can be easily chosen through the dashboard - just expand the drop-down list of the available locations in the top right corner of your environment wizard. Every region is supplemented with a short description, intendent to reveal its main specifics, and the appropriate tiny icon, which can differentiate, for example, the actual geographical location of the corresponding hardware. The full information and pricing details for each of the regions can be found within the **Quotas & Pricing** frame (accessible through selecting the same-named item of the **Balance** dashboard menu or clicking on the ***More details&hellip;*** string at the bottom of the region's list).

Using the abovementioned list, you can either specify the hardware set for your new environment or migrate the existing one (in case this ability is allowed by your hosting provider) to another location due to a more preferable hardware capacity, pricing policy or physical location. Such environment migration is an extremely powerful tool, that can help you to benefit in both cost and productivity - for example, you can choose cheaper hardware for the development/testing stages and subsequently migrate your production-ready application to the hardware with the best parameters, just before the release.

The corresponding dialog frame can be accessed through either selecting the ***Migrate...*** item within the list of regions while changing your environment topology or navigating to the environment **Settings &gt; Migration** section. Herewith, two different relocation modes are provided, which availability depends on the current and chosen target regions:

* **live migration** - available only between those hardware sets, which belongs to the same datacenter (such target regions are marked with the ***LM*** label). This type of migration allows to move your environment without any additional configurations or restarting the containers in it and ensures that your customers won't face any downtime during this operation. 
* **offline migration** - allowed to be performed between any regions. In contrast to the &ldquo;live&rdquo; mode, in this case your environment will be shut down for the whole period of its relocation. In addition, most likely it will undergo some modifications (as this mode is implied to be used for migration to another datacenter) like changing the nodes' IP-addresses and, optionally, switching an environment to the new domain name (if it differs from the current region's one). Thus, after the migration is completed, some manual configurations may be required to restore the normal operability of your application - all of the required information will be additionally sent to you via email.
{{%tip%}}**Note:** that costs for the usage of resources and options may vary in different regions, thus it's recommended to get acquainted with the appropriate new pricing model in advance, as it will be applied automatically after the relocation is done.{{%/tip%}}

The complete guides on [managing regions](/environment-regions) and performing environment [migration](/environment-regions-migration) in particular can be found within the corresponding linked documents.

<a id="endpoints" target="_blank" href="/environment-regions">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## Endpoints
The &ldquo;Endpoints&rdquo; term at the platform refers to the newly implemented feature of TCP/UDP mapping via the Shared Gateway, which became available within the 3.3 PaaS version. It is dedicated to significantly simplify the PaaS instances' collaboration with third-party tools and resources by providing the direct connection links (over either raw TCP or UDP protocol) without the mandatory [Public IP](/public-ipv4) address attached to the corresponding node. 

The list of **Endpoints** can be managed within the environment's **Settings** section under the same-named menu point. Depending on the nodes your environment includes, you can see some preconfigured endpoints here (like RDP links for the Windows-based containers) and also have an ability to **Add** some custom ones. During this operation, the following parameters should be specified: 

* **Node** - select a container of the chosen environment (using the drop-down list) the endpoint will be added for
* **Name** - either specify the title for a new endpoint or select one of the preconfigured options (note that some instances, like DBs, may have some special protocols/ports listed in accordance to the functionality they handle)
* **Private port** - local port that will be used for mapping (it's substituted automatically in case the predefined *Name* was selected)
* **Protocol** - select either TCP or UDP

The rest of the fields, i.e. **Public port** and **Access URL**, will be configured automatically by the platform.

You are able to add as many custom endpoints as it's allowed for your account (this limit depends on your hosting provider) using the tool panel at the top, or **Edit** / **Remove** the already existing ones by means of the same-named buttons ibid.

{{%tip%}}**Note:** that for linking functionality to work properly with the [VPS](/vps) and [Docker&reg;](/dockers-management) containers, the corresponding private ports (stated during the endpoint addition) at these nodes should be opened by an owner manually.{{%/tip%}}

To get the detailed information on managing Endpoints and to find out the corresponding use cases, refer to our [documentation](/endpoints).

<a target="_blank" href="/endpoints" id="io-statistics">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## I/O Usage Monitoring & Updated Statistics
Statistics monitoring is an easy but powerful tool, that helps to manage environments smartly. The information, provided by the platform in-built statistics module, covers all the billable resources' consumption, so it can help to adjust the topology according to your needs and to cut the spends greatly. In the current PaaS 3.3 release the **Statistics** section, which can be accessed through selecting the same-named button next to the necessary node of an environment, has been completely redesigned and improved to show an even greater amount of information, where the main amendment implemented became the addition of the very common and popular storage measurement method - monitoring of the **Input/Output Operations per Second** amount. 

Now, inside the ***Disk*** statistics' section (formerly known as *HDD*), in addition to the amount of data stored by a node (presented in *Mb* at the left vertical axis), the containers' I/O usage is displayed (the second axis to the right of the graph with the *input operations per second* unit). 
{{%tip%}}**Note:** that currently IOPS statistics for the Windows-based nodes is not provided.{{%/tip%}}

Obviously, the more operations that are handled - the higher the system load is. Thus, to avoid the hardware efficiency degradation, their amount is limited - the corresponding I/O usage threshold (defined by the chosen hosting provider) can be seen at the same ***Disk*** statistics' chart, being marked with a red dotted line. Reaching this point implies that the performance of your container can be negatively affected, so it is needed to enlarge the number of servers used or to optimize the application itself (you can set the appropriate [load alert](/environment-triggers) for being additionally notified about this).

To find more information on the I/O statistics usage, refer to the [corresponding](/view-app-statistics#io-usage) guide.

Besides that, the whole Statistics section has undergone a few more changes, like: 

* all four graphs were complemented with a line, which displays the corresponding resource's limit, herewith:
    * ***CPU*** and ***RAM*** limits are defined based on the cloudlets amount you've allocated for a node
    * ***Network*** and ***Disk*** limits depend on your hosting provider settings
* measurement units were moved to the popup legend
* numerical values are rounded with a new algorithm now, which makes them easier for perception

In such a way, every resource type, consumed by your environment, can be monitored with the improved usability and level of clarity. Find more information on the resources' usage tracking in our [documentation](/view-app-statistics).

<a href="/view-app-statistics" target="_blank" id="impr"><span>More info</span></a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## Improvements
[Zero Downtime Deployment for PHP (3.3 / 3.3.1)](#zdt)  
[New Style for One-Click Installation Widgets](#widget-style)  
[Pre-Installation Access to Docker&reg; Container Settings (3.3.1)](#pre-install-settings)<a href="#widget-style"></a>  
[Platform API Refactoring (3.3.1)](#api-refactoring)  
[Scroll Lock for Logs Auto-Refresh (3.3.1)](#logs-scroll-lock)<a href="#widget-style"></a>  
[Software Stack Versions](#software)  


## Zero Downtime Deployment for PHP (3.3/3.3.1)
The absolute majority of production environments need to be accessible to customers at any time, and the most common problem here is the process of project re-deployment (update). Usually, it is solved with the help of additional software (Capistrano, Fabric, etc.), but their integration is rather complicated and may require extra resources or even instances, as well as the valuable time spent for configuring these tools.

Obviously, a better solution is required, and such was [proposed](https://codeascraft.com/2013/07/01/atomic-deploys-at-etsy/) for PHP applications, run on the top of Apache, by the father of this programming language and simultaneously our technical advisor - Rasmus Lerdorf. The way the deployment process is managed, described in the linked article, was taken as a basis for the platform Zero Downtime Deployment mechanism implementation.

The core of this solution is in using a special requests' redirector, called *symlink *(symbolic link). Each time the deployment process is run (including the initial one), the corresponding app's files are stored in a separate server folder, where the name includes the timestamp it was created at. This allows the deployment process to be completed without influencing the actual application version and customers, that are currently working with it. Once installation is finished, the abovementioned symlink switches to a new project folder, so all the newly received requests will be redirected to it for now. Herewith, the previous app version remains stored at the server, ensuring that all the &ldquo;old&rdquo; users' sessions will stay active to be eventually fully processed without interruption. 
{{%tip%}}**Note:** that only two latest package versions are stored, while the older ones will be removed automatically during further deployments. Still, a particular folder can be simply renamed to avoid being erased.{{%/tip%}}

As you can see, PHP zero-downtime deployment at the platform does not require any additional actions or resources, except the doubled disk space needed for the second project copy (which, nevertheless, can be easily released manually when all the &ldquo;old&rdquo; requests are processed). In such a way, you won't experience any inconvenience, while the benefits of this new approach are obvious.

The improvement described above was integrated to both PHP application servers' templates - ***Apache*** (by means of the ***mod_realdoc*** module addition, which controls the symlink behaviour) and ***NGINX-PHP*** (though applying special configurations to the *nginx.conf* file). In such a way, this functionality is automatically ensured (regardless of the deployment source used - [archive](/whole-project-deploying) or [VCS](/php-git-svn)) at all of the new and already existing Apache or NGINX-PHP instances.

<u>*And starting with PaaS 3.3.1 version*</u>, the ZDT deployment feature availability is additionally controlled by your hosting provider. Also, you've got an ability to define whether you'd like to apply it through ticking the corresponding checkbox (with a link to the detailed information on this feature for comprehending its functionality) during your PHP app deployment to the ROOT context. Herewith, if a project source represents a VCS repository, this choice will be remembered and used for all the further [auto-updates](/git-svn-auto-deploy) of an application, until the ZDT option is disabled manually.

[More info](/php-zero-downtime-deploy)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## New Style for One-Click Installation Widgets
The [installation widgets](/application-manifest/) become an important part of the platform invitation policy, representing a very flexible and powerful solution for applications' distribution. Such a widget can be easily prepared and placed at the required page for users to sign up and deploy the corresponding app within the platform, in just one-click. 

Among the attributes a widget is configured with, the **data-theme** one is responsible for its visualization, allowing a choice from several available color schemes (*flat-blue*, *flat-purple*, *flat-orange*, *flat-green*). And recently this default styles' palette was extended with a new widget type, which is design to match the continuously evolving platform branding style. It could be enabled for all the new or already existing one-click installation widgets through stating the ***modern*** value for the abovementioned **data-theme** parameter to make your widget look much more presentable.  
[More info](/application-manifest/)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Pre-Installation Access to Docker Container Settings (3.3.1)
While [working with Docker containers](/dockers-management) at the platform, you are supplied with specific information on their most common settings and can configure them directly through the environment wizard. But if the required template is just chosen for installation, normally it needs to be downloaded first (if working with the central registry hub) to provide all the required information about the corresponding environment variables and other startfile configurations. Thus, while adding a new Docker image, you used to have the empty fields instead of the required data at the [container settings frame](/docker-configuration). Of course, you can already specify the necessary settings at this stage (and they will be applied as expected during the image installation and, in case of matching the default ones, will overwrite the default values). However, the problem here is that you can hardly predict the used parameters beforehand for setting them appropriately.

So, in order to deal with this hurdle, the platform-developed daemon for maintenance on Docker templates has been updated in the confines of the current 3.3.1 platform version. For now, all the abovementioned information is automatically fetched within the image manifest once you've entered the appropriate frame (i.e. the *Docker container settings* one) via the topology wizard. As a result, you can browse, edit and apply any necessary parameters even without downloading the image itself.

[More info](/docker-configuration)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Platform API Refactoring (3.3.1)
In order to improve your experience quality while working with [platform API](https://www.virtuozzo.com/application-platform-api-docs/), we've performed substantial refactoring (i.e. restructuring the existing code without changing its original behavior) for making it more clear, logical, and easier to understand. As a part of this refinement, the new altnames (alternative names) for some API parameters were added - you can find a couple of such improvement examples for the **AddNode** method below:

* ***registryUser*** altname for ***dockerHubUser***
* ***registryUrl*** altname for ***dockerHubUrl***
* ***registryPassword*** altname for ***dockerHubPassword***
* ***dockerRunCmd*** altname for ***dockerRunArgs***

All the newly added altnames represent aliases for their original names, so the complete backwards compatibility is ensured. Thus, all the already written integrations via our API remain operative without the necessity to obligatorily update them (until you'd like to get shorter and clearer code).

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Scroll Lock for Logs Auto-Refresh (3.3.1)
Viewing the [log files](/view-log-files/) at the platform is supplied by a special *Auto refresh* option, aimed to help you in tracking your instances' activities in a &ldquo;live&rdquo; mode, i.e. without significant delays. For that, the most actual data on all of the actions that occurred is output within the appropriate frame, being continuously updated. However, this can cause some inconvenience, when, for example, there is too much information being received simultaneously or if you require some time to analyze the obtained results, while the information of interest has left far behind.

That's why we've implemented a small amendment, which, however, is intended to improve the usability of this information source greatly. According to it, when you suddenly notice some important data among the received strings, you just need to scroll up a bit for the current frame's position to be locked. Herewith, the most recent information will continue gathering implicitly, allowing you to consider the required records in more details. And upon returning the frame's scroller to the bottom edge, it will automatically resume following the newly received information as usual.

[More info](/view-log-files/)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Software Stack Versions
The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 3.3|PaaS 3.3.1|
|---|---|---|
|***Tomcat 6***|6.0.43|6.0.43|
|***Tomcat 7***|7.0.61|7.061|
|***TomEE***|1.7.1|1.7.1|
|***Jetty 6***|6.1.26|6.1.26|
|***GlassFish 3***|3.1.2.2|3.1.2.2|
|***Java 6***|1.6.0_45 |1.6.0_45|
|***Java 7***|1.7.0_79|1.7.0_79|
|***Java 8***|1.8.0_45|1.8.0_45|
|***MariaDB***|5.5.42 / 10.0.17|5.5.42 / 10.0.17|
|***MongoDB 2.6***|-|2.6.10|
|***MongoDB 3.0***|3.0.2|3.0.2|
|***MySQL***|5.6.24 / 5.7.7|5.6.24 / 5.7.7|
|***PostgreSQL 8***|8.4.22|8.4.22|
|***PostgreSQL 9***|9.4.1|9.4.1|
|***CouchDB***|1.6.1|1.6.1|
|***nginx***|1.8.0|1.8.0|
|***Maven***|3.3.3|3.3.3|
|***Centos 6***|6.6|6.6|
|***Memcached***|1.4.24|1.4.24|
|***Apache***|2.2.15-39|2.2.15-39|
|***NGINX PHP***|1.8.0|1.8.0|
|***NGINX Ruby***|1.8.0|1.8.0|
|***PHP 5.3***|5.3.29|5.3.29|
|***PHP 5.4***|5.4.41|5.4.42|
|***PHP 5.5***|5.5.25|5.5.26|
|***PHP 5.6***|5.6.9|5.6.10|
|***Ruby 1.9.3***|1.9.3-p551|1.9.3-p551|
|***Ruby 2.0.0***|2.0.0-p643|2.0.0-p643|
|***Ruby 2.1***|2.1.5|2.1.5|
|***Ruby 2.2***|2.2.2|2.2.2|
|***Python 2.7***|2.7.6|2.7.6|
|***Python 3.3***|3.3.5|3.3.5|
|***Python 3.4***|3.4.0|3.4.0|
|***Node.js***|0.10 / 0.12|0.10 / 0.12|

{{%right%}}<a href="#impr" id="fix">Back to the list of Improvements</a>{{%/right%}}



## Bug Fixes
In the tables below, you can see the list of bug fixes in PaaS 3.3 and 3.3.1:

{{%bug-fixes title="PaaS 3.3"%}}
**#**|**Description**
---|---
JE-15522|The unhandled error appears during Maven authentication failure
JE-16675|Improper default WebSockets configuration for the NGINX-balancer/NGINX-PHP servers
JE-18079|Internal DNS server is restricted to access the Memcached node because of the insufficient firewall rules inside
JE-19407|Domain names with &lsquo;_' symbol are allowed
JE-19843|Ability to set a float value for the cloudlets' amount at the topology wizard
JE-19885|The same list of environment variables is written for a few times for cartridges 
JE-19945|Ability to view exported files for the deleted environment
JE-19990|Improper path to the custom context after it is renamed to ROOT
JE-20105|Incorrect displaying of the Auto Horizontal Scaling dashboard section after exiting the Full Screen mode
JE-20136|Error while trying to restart the slave node of the GlassFish 3 cluster
JE-20242|Error while trying to enable HA in an environment with the already disabled non-NGINX balancer
JE-20318|Authentication for Maven can't be disabled
JE-20322|Unable to deploy Java project with &lsquo;_' symbol in the context name
JE-20417|The &ldquo;URL is not valid&rdquo; error appears while trying to add the VCS project with username specified inside a link
JE-20474|Incorrect validation while trying to add VCS project with the space in URL
JE-20485|Ability to set the amount of resources smaller than the minimal requirements are via the topology wizard
JE-21091|Unhandled error for accounts in collaboration with different Export/Import permissions
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 3.3.1"%}}
**#**|**Description**
---|---
JE-19468|Ability to add an environment variable with {} characters for Docker&reg; image causes an error while trying to edit the container settings
JE-19958|The alignment position of engines' drop-down list varies for different tabs within the topology wizard
JE-20116|The &ldquo;Invalid action limits&rdquo; error occurs if the newly set Scale up/down value matches the previously used value of the opposite one
JE-21386|The 2.2.2 Ruby engine version is missed in the topology wizard
JE-21417|Files of the deployed project are not present at all instances after importing an environment with multiple application servers
JE-21434|Information about VPS is missed while exporting an environment with it
JE-21595|Incorrect message within Task Manager record while resetting the password for the set of VPS or Docker&reg; nodes
JE-21653|In case Docker&reg; image settings were not requested before its creation, an array with exposed ports is displayed as a single variable instead of being divided into separate ones
JE-21725|Missed validation of environment variables names during their addition or editing for Docker&reg; containers
{{%/bug-fixes%}}
{{%right%}}[Back to the top](#back){{%/right%}}