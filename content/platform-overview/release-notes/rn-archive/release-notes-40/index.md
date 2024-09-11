---
draft: false
title: "Release Notes 4.0/4.1"
aliases: "/release-notes-40/"
seoindex: "index, follow"
seotitle: "Release Notes 4.0/4.1"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included in the PaaS 4.0 and 4.1."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.0/4.1
*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS 4.0** and **4.1** releases:

* [Features](#feat)  
* [Improvements](#impr)  
* [Bug Fixes](#fix)  

<a id="feat"></a>For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Features
[Docker&reg; Containers Support Amendments](#dockers)  
[Platform CLI Client](#cli-client)  
<a href="#centos7" id="dockers">CentOS 7 Support</a>{{%back%}}{{%/back%}}

## Docker&reg; Containers Support Amendments
[UI Redesign](#dockers-ui)  
[HTTP Entry Point](#dockers-entry-point)  
[Horizontal Scaling](#dockers-scaling)  
[Volumes Support](#dockers-volumes)  
[Container Redeploy (Update)](#dockers-redeploy)  
[Custom Domains Support](#dockers-custom-domain)  
[Logs & Configurations](#dockers-logs-configs)  
<a href="#dockers-port-redirect" id="dockers-ui"><span>Automatic Ports’ Redirect</span></a>  
[Improved Run Command Handling](#dockers-run)
<a href="#dockers-daemon"></a>

#### UI Redesign
Several important enhancements were applied to the **Docker** tab interface at the topology wizard window in order to improve the visualisation and integrate support of the newly added functionality: 

* For now, the section to the left allows you to build the proper environment structure, composed with the required Docker containers, through placing them within the appropriate environment layers.

* The ***Select Container*** frame (the former *Add Container* one) was integrated with the topology wizard and now by default it comprises only two tabs for image selection (through *Searching* over the Registry Hub or adding your *Custom *one), which were completely redesigned. Meanwhile, the *Quick Start* section became optional, so currently its availability depends on a particular hosting provider's settings.

* Also, for now, only one type of the Docker image can be selected within the confines of the single layer - nevertheless, any of them can be [scaled horizontally](#dockers-scaling) just as any other platform instance. And in case multiple different types of images are required, they can be added through the *Extra* section, which automatically expands the topology with a new layer each time you include a new Docker template to it. 

* The most common container settings were relocated to the new *Configuration* section at the bottom of the wizard and expanded with the new *[Volume](#dockers-volumes)* option, where the mounted at the current container data storages are listed. Also, these configurations can be quickly accessed under the *Additionally* list next to the appropriate image layer at the dashboard's environment list.

<a href="/dockers-management" target="_blank" id="dockers-entry-point">More info</a>
{{%right%}}[Back to the list of Docker Amendments](#dockers){{%/right%}}

#### HTTP Entry Point
Starting with the PaaS 4.0 version, each Docker-based environment is provided with its own entry point (i.e. domain name). Thus, for now not just separate containers can be accessed (as previously, via the direct link or external IP attached), but a whole environment (via the embedded [Shared Load Balancer](/shared-load-balancer)) as well. 

So, if it is required to get the domain name for the environment with Docker containers, an image should be added to its ***App. Servers*** and/or ***Balancing*** ***layer*** (otherwise, i.e. if you don't fill any of them, the domain won't be attached). Subsequently, upon navigating to the bound address, a Docker image from the corresponding section will be opened.

Such an implementation ensures the additional support of some of useful and commonly demanded features - for example, it allows to:

* [scale horizontally](#dockers-scaling) the same-typed containers within a layer
* bind [custom domain names](#dockers-custom-domain) to the Dockerized apps
* [swap domains](/swap-domains) between environments

<a id="dockers-scaling"></a>In such a way, for now you can treat the Docker-based environments in the most beneficial and familiar way, just like any others, i.e. composed with standard stacks ones.

{{%right%}}<a href="#dockers">Back to the list of Docker Amendments</a>{{%/right%}}


#### Horizontal Scaling
In order to extend the Docker-based environments' functionality and improve the experience while their usage, the current 4.0 release brings the support of the [horizontal scaling](/multi-nodes) feature for Docker containers. So, for now, any of them can be multiplied within the confines of the corresponding environment layer. Same as for other wizard tabs, this can be easily applied via the central section of the **Environment Wizard** using the **+/-** buttons.

The implemented scaling workflow is also the similar, i.e.: for each newly added container, depending on the template's type, either the very initial master node will be duplicated (for application servers and load-balancers)<a id="dockers-volumes"></a> or a new one will be created (for all of the rest of stacks). In case of decreasing the amount of containers for such a scaled instance, the last added will be removed.

{{%right%}}<a href="#dockers">Back to the list of Docker Amendments</a>{{%/right%}}


#### Volumes Support
The new 4.0 PaaS version includes the support of Docker volumes - the dedicated mounted locations, intended to persist the container's data independently of the application lifecycle. This allows to perform different operations with container (e.g. [redeploy](#dockers-redeploy) it with another tag version) without loosing the data it already contains.

Implementing this functionality resulted in addition of the new same-named section within the *Docker container settings* frame, where the predefined volumes (if such were declared within the corresponding image manifest) are listed by default. Beside that, you can easily add custom volumes through specifying the path to the location it should be mounted at. Physically, each such declared storage is placed inside the dedicated **/volumes** directory within the container's root. Herewith, any custom volume can be removed at any time upon it becomes unnecessary, while the predefined ones are considered as obligatory ones and thus can't be deleted.

In order to find out the details on Docker volumes management, please refer to the corresponding [guide](/docker-volumes).

<a href="/docker-volumes" target="_blank" id="dockers-redeploy"><span>More info</span></a>
{{%right%}}<a href="#dockers">Back to the list of Docker Amendments</a>{{%/right%}}


#### Container Redeploy (Update)
The majority of Docker templates are rapidly developed, thus, evolving over the time, the new tags (versions) of the image are continuously presented. And here comes the problem of upgrading the existing Dockerized applications and services up to the desired releases without losing the existing configurations.

In the present platform release such mechanism was implemented, allowing you to redeploy any of the already created Docker-based containers with another tag applied. During such an operation, all the inherent configurations and settings (including custom variables and linking between nodes) will be saved, thus you won't need to redefine any of them. Surely, all the data stored within the [volumes](#dockers-volumes) won't be affected too.

This option can be called through clicking the **Redeploy container(s)** button within the template's context menu (which is shown upon hovering over a particular instance or layer) at the dashboard or through the pencil icon next to the current tag version at the *Change environment topology* window. Within the appeared redeployment frame, you can select the desired image version for the chosen container(s) to be updated with, and, if operating with multiple nodes, to enable the ***Sequential deployment*** switcher. In the latter case, containers within the selected layer will be updated sequentially, one by one, allowing the corresponding service remain available during this procedure. Otherwise, all of them will be redeployed at once, causing the temporary downtime of your app.

Right after the process is finished, you'll see the success notification at the top-right corner of the dashboard with the **Show Logs** button. Upon clicking on it, the corresponding *redeploy log* tab will appear, with the complete information on the performed actions and their duration for all of the containers displayed.

<a href="/docker-update" target="_blank" id="dockers-custom-domain"><span>More info</span></a>
{{%right%}}<a href="#dockers">Back to the list of Docker Amendments</a>{{%/right%}}


#### Custom Domains Support

The newly implemented ability to operate an environment, that is composed of a set of Docker containers, via a single [HTTP entry point](#dockers-entry-point) (i.e. the common domain name attached) can be complemented by binding a [custom domain name](/custom-domains) to it for getting even better usage experience. This operation can be accomplished in a matter of minutes right through the dashboard, in a completely similar way as for any other environment type - i.e. by means of the dedicated *Custom Domains* section of the environment's ***Settings***. As a result, you get the possibility to run and poses your Dockerized apps as a production-ready solution.

<a href="/custom-domains" id="dockers-logs-configs" target="_blank"><span>More info</span></a>
{{%right%}}<a href="#dockers">Back to the list of Docker Amendments</a>{{%/right%}}


#### Logs & Configurations
With an aim to simplify the Docker containers management, within the current PaaS 4.0 release we've adjusted the following functionality to be available directly through the dashboard:

* for now you can access all the data and configuration files inside your container through pressing the appropriate *Config* button for the required node/group of nodes. Herewith, you are provided with the full root access for the comprised files' edition, just like when entering your container [via SSH](/docker-ssh-access).
* the most crucial information on your container's state is now available within *Logs* - the corresponding tab can be opened using the same-named button next to the required container(s). Also, viewing this data is automatically proposed after any container is created (with the *Show Logs* button within the appropriate dashboard notification). Herewith, though the list of available log files can vary depending on a particular image settings, the ***run.log*** file will be automatically opened first (if present), as usually it is intended to store the information on the appeared errors.

<a href="/docker-configuration#other" target="_blank" id="dockers-port-redirect">More info</a>
{{%right%}}<a href="#dockers">Back to the list of Docker Amendments</a>{{%/right%}}

#### Automatic Ports' Redirect
Depending on a particular Docker image specifics, it can be run on some custom port so that application inside can't be accessed without the Public IP attached or a special manual adjustment performed. In order to get rid of such an inconvenience, starting with the 4.0 PaaS version, the platform automates these configurations and adds the required redirect to the *iptables* list by itself, so that the corresponding application becomes available over the embedded [Shared Load-Balancer](/shared-load-balancer) without any manual interventions required.

In order to implement such a scenario, a special script was written and integrated to be executed after each Docker container launch. It tracks the ports, that are listened by application on the TCP level at the container start up and separates the ones, which are commonly used by standard services (e.g. SSH, mail, databases, etc.). After that, all of the incoming requests are redirected to the remaining port (or, in case several of them have left, the first one in the list is used).

In such a way, an application becomes available through the shared balancer just after the deployment is finished.

<a href="/docker-ports" target="_blank" id="dockers-run"><span>More info</span></a>
{{%right%}}<a href="#dockers">Back to the list of Docker Amendments</a>{{%/right%}}

#### Improved Run Command Handling
Traditionally, Docker containers use CMD instruction in order to set the command to be executed by default on each startup. Usually, it is run through the *&lsquo;/bin/sh -c'* entrypoint, so if CMD (or **Run Command**, as it's named at our dashboard) is set, for example, to *&lsquo;bash'*, the actually executed string is *&lsquo;/bin/sh -c bash'*. However, for some specific purposes, it may be required to change the default entrypoint and substitute it with some custom executor to run the given command.

For now, such procedure can be handled using the *Entry Point* field, which was added to the **Run Config** section of the ***Docker container settings*** frame alongside the *Run Command* one. Specifying the desired custom values within these parameters allows to configure any required startup operation. Additionally, upon editing these settings, a special **Reset to default** button will appear, so you'll be always able to negate any undesired changes, returning their initial state.

[More info](/docker-run)
<a href="#dockers" id="cli-client">Back to the list of Docker Amendments</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}


## Platform CLI Client

With an aim to simplify the account management for developers, we are glad to present the platform-dedicated command-line interface (**CLI**) client, designed to easily handle almost all of the operations, initially available only through the dashboard, remotely. Also, it allows you to monitor, control and automate your application's lifecycle by writing and applying the corresponding scripts and, in such a way, extend the default platform possibilities.

The CLI client for the platform can be obtained with just a single line of code, that should be executed via your terminal:

*curl -s ftp://ftp.jelastic.com/pub/cli/jelastic-cli-installer.sh | bash*

This command runs a simple script, which will download and install the client to the dedicated **jelastic** folder at your **home** directory. Next, it will add the required record to the *PATH* variable within the ***.bash_profile*** file for the platform methods to be easily executable. The structure of CLI folders and scripts inside represents the hierarchy of the [platform API](https://www.virtuozzo.com/application-platform-api-docs/), that results in a complete similarity of the corresponding working process. In such a way, the API-familiar users can get used to the client much more faster, while others are able to learn two ways of account management at a time.

On the first method's call you'll be requested for the desired platform's URL (in the *http://app.<a href="/paas-hosting-providers/" target="_blank">{hoster_domain}</a>* format) and your account credentials. Consequently, when the authentication is passed successfully, the information on your actual user session will be saved to the ***.config/jelastic.properties*** file. If it's required to change the currently used platform or account, the corresponding *~/jelastic/users/authentication/signin* method should be called with the new login information as parameters.

<a href="/cli-client" target="_blank" id="centos7">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}


## CentOS 7 Support
The platform always tries to keep up with the most current and stable stack versions, therefore, in the present release we are glad to introduce you the major update of the platform basic OS template for all containers to the latest ***CentOS 7*** version.

Generally, the most noticeable amendment in the seventh release compared to the previous sixth one is a new initialization daemon - the default *SystemV Init* startup scripts were replaced with the more concurrent *Systemd* (System Management Daemon) solution. *Init* was the first commercial solution and currently is the most popular one, while the *systemd* is more recent and was designed to overcome the known shortcomings. For example, it removes the serial processes flow structure (i.e. when a new task starts only after the last one was successfully finished and loaded into the memory), which often results in delays and long booting time. Instead, *systemd* starts all processes in parallel, improving the processing speed and computational power.

To learn the rest of new distribution's specifics, refer to the official [web site](https://www.centos.org/), where the complete list of the performed changes with their detailed descriptions can be found.


In order to implement the latest version of CentOS at the platform, the new *centos-jelastic-7* operating system template was created (based on the similar one from Odin, but, obviously, with the needed stuff included only). As a result, all the RPMs for software stacks templates were rebuilt (except the *PostgreSQL 8* database, which was removed, because it's no longer supported under CentOS 7).

Surely, the [CentOS VPS](/vps) container template was updated to the latest *7th* version too. Just as before, you can get the fully isolated and secured virtual private server through the ***VPS*** topology section at the environment wizard. In addition, to improve its usage experience while its usage and simplify the management, we've added the ability to configure VPS directly through the dashboard's *Configuration Manager* (just as it could be previously done for the rest of stacks, but with the full root permissions granted) and view the information on its operability via *Logs*.

<a href="/vps" target="_blank" id="impr">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}


## Improvements
[Setting Custom Firewall Rules](#custom-firewall)  
[PageSpeed Module for Apache](#pagespeed)  
[UX Improvements](#ux)  
[PostgreSQL Package for Python](#postgresql-python)<a href="#swap-space"></a>  
[Redirects' Autoresolve](#redirects)  
[Engine Versions Update (4.1)](#engines)<a href="#redirects"></a>  
<a href="#software" id="custom-firewall">Software Stack Versions</a>{{%back%}}{{%/back%}}


## Setting Custom Firewall Rules
In some specific cases, it may be required for the special firewall restrictions (i.e. which are not declared within default container settings) to be set within your nodes. Previously, the iptables rules' management could be performed at the hosting provider's side only, but starting with the present release, you've got the possibility to apply the desired changes for the newly created containers by yourself.

{{%tip%}}**Note:** that for this operation to be performed, you need to ensure the appropriate container's firewall is already enabled. For that, access its */etc/jelastic/metainf.conf* file [via SSH](/ssh-access), where the ***FIREWALL_ENABLED=1*** string should be present. Otherwise, send the corresponding request to your hosting provider and re-create a container after it's satisfied.{{%/tip%}}

Such custom ip-rules should be declared and stored within special dedicated file, named ***iptables-custom*** and located within the **/etc/sysconfig** directory. So, the flow is the following:

* access the required container [via SSH](/ssh-access) and open the above mentioned file
* declare the required rules using the *iptables-save* tool's format, for example:  
<i>*filter  
-I INPUT 1 -j ACCEPT -s 111.111.111.111  
COMMIT  </i>

*  enable custom firewall with the next command:  
*sudo /usr/bin/jem firewall fwstart*

The currently applied rules can be checked using the following command:  

*sudo /usr/bin/jem firewall list [ filter | nat | mangle ] [iptables options]*

In such a way, you can make and apply changes to your containers' firewall settings without the additional assistance from hoster's side.

<a href="/custom-firewall" target="_blank" id="pagespeed">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## PageSpeed Module for Apache
Striving to give you the best possible experience, the platform continues to integrate the time-tested and proven to be worthy solutions as the default opportunities. In the current release it's a [PageSpeed](https://developers.google.com/speed/pagespeed/module/) module, developed by Google. It became really popular due to the noticeable performance boost it ensures by means of numerous in-build optimization filters.

Being added to the default Apache build, this module is disabled by default, but can be easily activated. For that, you just need to navigate to the **conf.d &gt; <i>pagespeed.conf**</i> file using the embedded *Configuration Manager* for your Apache server, and uncomment the following lines (the appropriate module version will be chosen automatically based on the currently used server version):

*   LoadModule pagespeed_module /usr/lib64/httpd/modules/mod_pagespeed.so*  
*   LoadModule pagespeed_module /usr/lib64/httpd/modules/mod_pagespeed_ap24.so*  

After these changes are saved and the server is restarted, the module will be activated and start to work, reducing the incoming requests' processing <a id="ux"></a>latency.
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## UX Improvements
[Installation Widgets Improved Usability](#ux-widget)  
[Billing History Detalization](#ux-billing)  
[Automatic Export Disabling](#ux-export)  
[Marketplace UI Changes](#ux-marketplace)  
[ZDT Deployment Amendments](#ux-zdt)  
<a href="#ux-auto-resolve" id="ux-widget">Auto-resolve Conflicts Logging</a>    
[Maven Plugin Update](#ux-maven)  


#### Installation Widgets Improved Usability
The [one-click installation widgets](/application-manifest/) represent an extremely easy and effective way of app's distribution. Within the current release, the general widgets concept undergone some notable changes in order to match the newly appeared requirements for their functionality, namely:


* Due to the greatly enlarged number of alternative PaaS installations, hosted by various service providers in close locations, the geoIP method, previously used for the automatic selection of the most suitable platform, appear not to always bring the desired result. Thus, we've added a special configuration pane, which is displayed at the bottom of the widget upon hovering over it. It contains an expandable list of all of the available hosting service providers, with their logos, countries and platform versions. Just as before, the geographically closest one will be proposed by default, while installations without the registration possibility are automatically excluded from this list.</li>
* Using the special **URL** button at the right part of the new widget, it became possible to copy the direct link to the app manifest. Subsequently, if already having the account, you can easily deploy the corresponding application right through the dashboard by specifying this URL within the **[Import](/environment-export-import#import)** frame or through executing the appropriate API method, i.e. by adding link to the platform address in the following format:  
*https://app.<a href="/paas-hosting-providers/" target="_blank">{hoster_domain}</a>?manifest=<b>{manifest_url}*</b>  
* The last enhancement is the confirmation dialog, which appears just before the installation is started in both of the above described cases. It allows not only to cancel the deployment, but also to set the desired environment name and choose the preferable environment region.

In order to define whether to use the new type of widget, the ***data-hoster-select*** parameter is used (*1* - to enable, *0* - to disable). In addition, it could be supplemented with the ***data-keys*** option to limitate the proposed hosting Platforms list, so the only declared here providers will be shown.

{{%tip%}}**Note:** New widget currently works with the <i>&ldquo;modern&rdquo; **data-theme**</i> parameter only.<a id="ux-billing"></a>
{{%/tip%}}
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}

#### Billing History Detalization
In order to provide more complete information on account charges, in the current 4.0 release we've added the [billing history](/consumed-resources#billing) detalization based on the separate nodes consumption, rather than on the group's of the same-typed instances. This was driven by the reason that nodes within an environment layer oftenly could be loaded not equally, thus their costs can differ.

Due to this, for now the billing history is shown separately for each node in the environment by default. However, if such a detalization is not required, it can be disabled with the corresponding ***Group by node*** switcher, appeared within the **Billing history** tab settings.

<a href="/consumed-resources#billing" target="_blank" id="ux-export"><span>More info</span></a>
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}

#### Automatic Export Disabling
The platform [Environment Export and Import](/environment-export-import) feature is a great solution for transferring applications between different PaaS installations. However, currently this opportunity is not provided for the containers of the certain types (namely, Docker- and Windows-based ones), thus the export option was automatically disabled for the environments with such nodes comprised. 

So, for now, when you navigate to the *Settings* tab for any of your running environments, the presence of the available for transfer elements is automatically checked. And if the result shows, that there isn't a single such node, the *Export* section's options become dimmed with the corresponding warning message (highlighted in red for the better visibility) shown above to mark this feature <a id="ux-marketplace"></a>unavailability. 
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}

#### Marketplace UI Changes
In the current Platform update, the [Marketplace](/marketplace) dashboard section has received a few minor improvements, intended to make all the provided functionality easily accessible and convenient for usage:

* first of all, the corresponding ***Marketplace*** drop-down list at the top pane of the dashboard was removed, leaving only the same-named button. When clicked on, it leads to the appropriate *Marketplace* tab with the **Apps** expandable section (formerly named as *Applications*) active. Just as before, it contains the categorized list of the applications, that were preconfigured in the most beneficial way specially for the platform and can be installed in a few clicks. 
* a bit lower, the new **Add-on** section appeared. Obviously, all the add-on packages can be found here, which makes them much more easier to be found and implemented. 
* the last section, which provides the ability to add the required Docker template to an environment, was renamed to **Containers**, while providing the same functionality as before.

<a href="/marketplace" target="_blank" id="ux-zdt"><span>More info</span></a>
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}

#### ZDT Deployment Amendments
The recently added [Zero DownTime Deployment](/php-zero-downtime-deploy) feature for PHP apps continues to being developed and polished. So in the confines of the 4.0 release it got two major updates:


* *improved VCS autoupdate handling* - the default ZDT scenario for deployment from VCS using the [autoupdate](/git-svn-auto-deploy) option makes the periodical redeployment operations and ensures the application availability during them. But in case the iteration interval is set rather low, the frequent updates may badly affect the server capabilities due to the high I/O load. Thus, the method behaviour was improved and for now it performs the preliminary changes check up, comparing the current project's revision ID with the previous one (stored in the project properties). If there is a difference, which means some update was committed to the repository, the redeployment will be called; otherwise, ZDT won't perform any operations to save your resources.
* *logs for ZDT operations* - the list of logs files for PHP application servers (both Apache and NGINX) was extended with the additional ***deploy*** section. It contains the detailed data on all of the deployment-connected operations, including the ones, performed by ZDT module. Here you can explore the information on permission edits, context, directories and files modifications, symlink switching, ownership changes, overall deployment results, etc. Note that this logs section isn't shown within the list by default, but will be instantly displayed upon any record is written down (i.e. after a single ZDT deployment is <a id="ux-auto-resolve"></a>performed).
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}


#### Auto-resolve Conflicts Logging
The **auto-resolve conflicts** option, which is used for the VCS deployment type and represents an analogue of the *git reset --hard* command, is intended to prevent the occurrence of conflicts while projects updates. In case any such issue arises, the contradictory file is changed according to its repository version, discarding the locally made changes. 

With an aim to clarify how this option works and, generally, to show the complete information on the handled VCS deployments (both manual and automatic ones), in the current PaaS release the corresponding data started to be stored within the newly added ***vcs_autoresolve*** log file. Namely, it provides the information on the most recent repository revision (i.e. ID of the lastly committed repo modification with the corresponding comment) and on all crucial actions, performed in order to solve the appeared encounters. All of the listed records are followed with the appropriate timestamps. 

**Note** that this logs section appears only after any record is written to it, i.e. upon the deployment operation with the *auto-resolve conflicts* option enabled was <a id="ux-maven"></a>run. 
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}


#### Maven Plugin Update
[Maven](https://maven.apache.org/) is a popular software tool, that allows to build and manage Java-powered projects. Being tightly integrated to the platform by means of the specially developed external [plugin](/java-vcs-deployment/), it can be easily added to any of your Java projects through the ***pom.xml*** configuration file. Performing this gives you the opportunity to deploy this project to your Cloud environment just with a single command, executed via the local terminal.

Within the confines of the present 4.0 release, the plugin for Maven got a little update, aimed to improve its usability. According to it, only the five last project builds, uploaded by the plugin to the *Deployment Manager*, are stored. So, when the sixth such file is added, the oldest one is automatically removed. Herewith, this operation does not influence the packages, that were added manually or with the help of any other tool. Such an approach results in avoiding the mess within the list of the available packages, simultaneously releasing the space these unrequired builds consume, and, therefore, reducing the spends on disk usage.

[More info](/java-vcs-deployment/)
{{%right%}}<a href="#ux" id="postgresql-python">Back to the list of UX Improvements</a>{{%/right%}}
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## PostgreSQL Package for Python
In order to improve the Python [cartridge](/cartridges-overview) interaction with the PostgreSQL DB and to solve the problems with the &ldquo;***pg_config missing***&rdquo; error, the list of its default RPM packages was extended with the new ***postgresql-devel*** one. In addition, this ensures the support of some additional tools, e.g. *psycopg* - the most popular adapter for the Python programming language and PostgreSQL database joint work.

The included package contains the basic DB client, some manual pages with the supported by PostgreSQL commands listed, and a number of utility programs for the proper database work maintenance. The full list of files and their descriptions can be found at the official <a id="redirects"></a>database [documentation](http://www.postgresql.org/9.4/static/index.html).
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Redirects' Autoresolve

The unpack module, which is implicated in various platform processes (from the environments' import to a simple *curl* commands handling), has received a slight update in the current 4.0 PaaS release - support of the ***-L*** (*--location*) flag, which is now enabled by default. This means that upon receiving the report from the destination server, which says that the required page was moved to a different host, the request will be tried again for this new location. If executing the appropriate command manually, the amount of such redirects can be limited by the corresponding *--max-redirs* option.

In case the request contains the authentication data, the credentials will be provided for the initial host only. This won't allow the malefactors to intercept your login and password information, providing a sufficient level of <a id="engines"></a>security.
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Engine Versions Update (4.1)

The regular programming languages engines' renovation, provided within each platform release, brought the following updates this time:

* The greatest leap was done for the **NodeJS** app server, as for now it could be run over the ***4.2*** version (the previously available one was *0.12*). Such a versions gap was caused by the reason that the *1.x* - *3.x* releases have been implemented as a part of the [io.js](https://iojs.org/en/) fork only, while being eventually merged within the unified *4th* release. The new available features and notable changes of the last Node.js version can be explored [here](https://nodejs.org/en/blog/release/v4.0.0/).
* Another newly added engine version is ***Python 3.5***, which is now distributed [alongside the legacy ones](/python-versions). It delivers a bunch of new features, as well as some security improvements and bug fixes - for the precise details, please, refer to the official [documentation](https://docs.python.org/3.5/whatsnew/3.5.html).
* One more update covers the usage of the most recent ***Ruby 2.2*** engine. The exact new version is *2.2.3*, which replaced the preceding *2.2.2* one.

As usual, the complete list of the software stacks-related changes, included to the current PaaS release, can be viewed within the corresponding <a href="#software" id="software"><span>section</span></a>.
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Software Stack Versions
The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.0|PaaS 4.1|
|---|---|---|
|***Tomcat 6***|6.0.43|6.0.43|
|***Tomcat 7***|7.0.62|7.0.62|
|***TomEE***|1.7.1|1.7.1|
|***Jetty 6***|6.1.26|6.1.26|
|***GlassFish 3***|3.1.2.2|3.1.2.2|
|***Java 6***|1.6.0_45 |1.6.0_45|
|***Java 7***|1.7.0_79|1.7.0_79|
|***Java 8***|1.8.0_45|1.8.0_45|
|***MariaDB***|5.5.42 / 10.0.17|5.5.42 / 10.0.17|
|***MongoDB 2.6***|2.6.10|2.6.10|
|***MongoDB 3.0***|3.0.3|3.0.3|
|***MySQL***|5.6.24 / 5.7.7|5.6.24 / 5.7.7|
|***PostgreSQL 8***|incompatible|incompatible|
|***PostgreSQL 9***|9.4.4|9.4.4|
|***CouchDB***|1.6.1|1.6.1|
|***nginx***|1.8.0|1.8.0|
|***Maven***|3.3.3|3.3.3|
|***Centos 6***|7.1|7.1|
|***Memcached***|1.4.24|1.4.24|
|***Apache***|2.4.6|2.4.6|
|***NGINX PHP***|1.8.0|1.8.0|
|***NGINX Ruby***|1.8.0|1.8.0|
|***PHP 5.3***|5.3.29|5.3.29|
|***PHP 5.4***|5.4.43|5.4.43|
|***PHP 5.5***|5.5.27|5.5.27|
|***PHP 5.6***|5.6.11|5.6.11|
|***Ruby 1.9.3***|1.9.3-p551|1.9.3-p551|
|***Ruby 2.0.0***|2.0.0-p643|2.0.0-p643|
|***Ruby 2.1***|2.1.5|2.1.5|
|***Ruby 2.2***|2.2.2|2.2.3|
|***Python 2.7***|2.7.10|2.7.10|
|***Python 3.3***|3.3.6|3.3.6|
|***Python 3.4***|3.4.3|3.4.3|
|***Python 3.5***|-|3.5.0|
|***Node.js***|0.10 / 0.12|0.10 / 0.12|
|***Node.js 4***|-|4.2|

{{%right%}}<a href="#impr" id="fix">Back to the list of Improvements</a>{{%/right%}}


## Bug Fixes
In the tables below, you can see the list of bug fixes in PaaS 4.0 and 4.1:

{{%bug-fixes title="PaaS 4.0"%}}
**#**|**Description**
---|---
JE-13344|The embedded MongoDB backup script creates an empty archive if the authentication fails for server version &gt;=2.6
JE-19954|Load alerts for the removed nodes remain active
JE-20460|Unable to access the data within dashboard tabs after downloading the Custom SSL certificate files from dashboard
JE-20471|The &ldquo;Unable to connect to the database server&rdquo; error occurs while opening the cloned\imported environment with PowerDNS
JE-20487|Incorrect subject of the russian email notification about the automated NGINX-balancer node addition to the WordPress cluster package
JE-21018|Incorrect network settings (internal IP) for the migrated Docker-based server with external IP
JE-21097|Long delay before starting download the project build over 100 MB, uploaded to the dashboard via Maven plugin
JE-21113|The *Build&Deploy* Maven operation fails for the cyrillic-named environments
JE-21123|Incorrect error message if no free disk space left in a container during the deployment process
JE-21175|Ability to set odd number of nodes within the auto-horizontal scaling settings for app server with High-Availability enabled
JE-21349|Wrong RDP link for the Windows 2012 node with external IP enabled
JE-21381|The access permissions for the main nodes' configuration files are reset after the appropriate service restart via SSH
JE-21498|Inability to access the MongoDB 3.0 admin panel with new credentials after resetting the password
JE-21573|Absence of the *Task Manager* records for the linking and setting environment variables actions, applied to a Docker containers
JE-21574|The automatic redirection of listened ports to the resolver's port 80 does not work properly for Node.js
JE-21731|The [scroll lock](/release-notes-33#logs-scroll-lock) option does not work for the log files with more than two pages of records
JE-21811|Building project via Maven with the auto-update interval set to 1 minute isn't started within 5 minutes for the environment in default region due to the wrong resolver configuration
JE-21886|Wrong validation for the remote VCS project link
JE-21889|Missed FTP addon installer for the MongoDB 2.6 node
JE-21909|The Dockerized services could not be run if the appropriate container's start script does not refer to "/bin:/usr/bin:/sbin:/usr/sbin"
JE-21962|Wrong parsing of the Docker image environment variables' values with white spaces
JE-21971|The *Task Manager* records are duplicated/erased because of the repetitive reading log action, run due to the logs' auto-refresh option enabled
JE-21983|The started with "ROOT" folders are removed during the ZDT-handled project redeployment to the ROOT context with the ZDT option already disabled
JE-22030|The &ldquo;DNS can not resolve the hostname&rdquo; exception is hand out during starting/stopping the GlassFish 4 service via SSH
JE-22059|The &ldquo;Can not detect OS version&rdquo; error occurs while trying to deploy the *fedora:latest* Docker image
JE-22060|Unable to establish SSH connection to the Docker container with the Fedora of the 20/21 version deployed
JE-22083|Old alias name for the imported environment after its cloning
JE-22123|Unable to deploy the dockerized *Debian* image due to the &ldquo;Can not detect OS version&rdquo; error
JE-22339|The previously deployed contexts within a single environment become inactive after refreshing the dashboard and deploying one more app
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 4.1"%}}
**#**|**Description**
---|---
JE-23400|An error occurs while trying to clone environment with two GlassFish 3 servers, located at the non-default environment region
JE-23556|The logs' preview for Docker containers is not cleaned up after switching to another file
JE-23570|Names of the uploaded to Docker or VPS container files with the *&ldquo;**$&rdquo;* symbol are truncated
JE-23571|The &ldquo;\&rdquo; character is added to the file name with the &ldquo; *'* &rdquo; symbol while uploading it to Docker or VPS container
JE-23576|An error occurs while trying to create the file with &ldquo; ' &rdquo; or &ldquo; ` &rdquo; symbol in the name inside a Docker or VPS container
JE-23579|Unhandled error for operations' failure due to the user-performed renaming of the main system Docker directories or files
JE-23580|The *Container is not running* error appears while trying to restart a Docker node during its log tab is loading
JE-23586|Unhandled errors for the *Renaming is not permitted* and *Can't execute command at a non-running container* exceptions at Docker and VPS containers
JE-23588|Ability to enable the ZDT option while deployment to the non-ROOT context 
JE-23594|The import operation fails if the uploaded manifest doesn't contain the *"categories":"export"* parameter
JE-23597|An error occurs while trying to delete the Docker's log file during its auto-refreshing
JE-23598|File with special symbols in name remains present in Docker container after being deleted, whilst is not shown in the file manager
JE-23608|One of the two required configuration files at the NGINX load balancer's *conf* folder is missed depending on the chosen environment topology
JE-23609|Presence of the *Config* and *Log* buttons for the Windows-based VPS nodes
JE-23623|Files of the project, deployed to the Tomcat 8 or Glassfish 4 app servers, are missed during the export/import operation
JE-23624|An error occurs while trying to redeploy a Docker container with white space in the volume's name
JE-23626|The same log file can't be viewed at different environments simultaneously
JE-23633|Improper validation of the *restrictedPaths* property within Docker container manifest causes crashing while some images' creation
JE-23653|Inability to connect to legacy environment via FTP after installing the appropriate add-on to it 
JE-23654|The newly created files and folders within IIS8 nodes in different environments of the same user are shared
JE-23661|Absence of the *Show Logs* button at the appropriate pop-up notification after deploying a Docker image via Marketplace
JE-23673|Path hints are not displayed for the newly created items within file manager for Docker/VPS containers
JE-23674|Absence of the directory name length validation for Docker and VPS containers
JE-23678|Unhandled exception while trying to view logs for the stopped Docker-based environment
JE-23679|Missed *mysql-community-libs-compat* default package for the MySQL 5.7 server
JE-23683|The *Remove* button remains enabled in case of selecting multi records within *Docker container settings* frame
JE-23686|Empty *resolv.conf* file for the deployed *unigeocloud/ubuntu-vnc-novnc-qgis210* Docker image
JE-23706|Unhandled error while trying to access the renamed binary file via Docker file manager
JE-23712|An error occurs while trying to rename several folders, that were created simultaneously
JE-23713|An exception appears while trying to perform any action with Docker container folders via file manager and refreshing the root directories tree at the same time
JE-23720|Unhandled error while uploading a file to Docker container via the embedded file manager if this operation is not permitted
JE-23721|The uppercase characters in Docker volume name are turned to lowercase while its addition
JE-23730|Unhandled error while trying to rename log file at the Docker-based container
JE-23740|Number of workers is not equal to the number of physical cores for the Apache-Python node
JE-23763|The password expiration flag is not reset after its recovering for the MySQL 5.7 node
{{%/bug-fixes%}}

{{%right%}}[Back to the top](#back){{%/right%}}
