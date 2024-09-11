---
draft: false
title: "Release Notes 4.8"
aliases: "/release-notes-48/"
seoindex: "index, follow"
seotitle: "Release Notes 4.8"
seokeywords: "paas, paas release notes, paas version, 4.8 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the PaaS 4.8 release."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.8

*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS & CaaS 4.8** release:

* [Features](#features)
* [Improvements](#improvements)
* [Bug Fixes](#bug-fixes)

For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Features
<a href="#traffic-distributor" id="traffic-distributor">Traffic Distributor Add-On</a>{{%back%}}{{%/back%}}


## Traffic Distributor Add-On
[Traffic Distributor](/traffic-distributor) is a powerful solution, developed by PaaS team to provide smart requests routing and load distribution between a pair of applications (environments). It is delivered by means of the dedicated [Add-on](/marketplace#add-ons) package (available through the platform [Marketplace](/marketplace) board within *Apps &gt; Dev & Admin Tools* section). The distributor itself represents a separate environment with NGINX load balancer server and a special add-on installed on top of it.

During Traffic Distributor installation, you are provided with a number of options to comprehensively configure it up to your needs. Here, you are able to select hosts to route the requests between, state traffic ratio, amount of balancer nodes, etc. But the main option here is choosing the required [routing method](/traffic-routing-methods) according your purposes, where 3 options are available:

* *[Round Robin](/round-robin-traffic-routing)* - the most straightforward distribution type, used to route each new request to a particular backend based on specified server weights
* *[Sticky Session](/sticky-sessions-traffic-routing)* - this routing type is based on &ldquo;sticking&rdquo; each user to a specific backend (according to the set servers' weights) which will process all their requests until the corresponding user session, created on the first app visit, expires
* *[Failover](/failover-traffic-routing)* - allows to set the standby server in addition to the primary one in order to ensure application availability even during one of the environments is down

Right after succesfull installation, Traffic Distributor will immediately start routing traffic between chosen backends according to the specified parameters. Still, any of the defined during installation settings can be subsequently [easily changed](/traffic-distributor-installation#reconfigure) through the corresponding *Configure* option (to access it, just click on the ***Add-ons*** icon for NGINX load balancer in the distributor-dedicated environment). 

There is a broad range of scenarios to effectively use Traffic Distributor with your project. Starting with the advanced workloads balancing and gaining additional high availability for a cluster, to the far more complex implementations (e.g. to apply advanced [failover protection](/failover-protection), [blue-green updates](/blue-green-deploy) or to perform [A/B testing](/ab-testing)).

[More info](/traffic-distributor)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Improvements
[Docker Container's DNS Aliases for nodeId](#docker-nodeid-alias)  
[JPS Import Improvements](#jps-import)  
[Increased SSH Gateway Performance](#ssh-gateway-performance)  <a href="#opcache-deactivation"></a>  
[Export Directory Dialog for File Manager](#export-directory)  
[Default Memory Configs Optimization for Java Containers](#java-memory-optimization)  
[File Manager Improvements](#file-manager)  
[Software Stack Versions](#software)  

[Back to the top](#back)  


## Docker Container's DNS Aliases for nodeId
Since the present PaaS 4.8 version, all newly created [Docker containers](/dockers-overview) are provided with a DNS record, named according to its *nodeId*. Such an alias allows to refer to your Docker container via automatically assigned node identifier while working with the platform internal network via [SSH Gateway](/ssh-overview).

The exact alias name looks like ***node{ID_number}***, where ***{ID_number}*** - a unique numeric identifier for the node (it can be also seen at your user dashboard). As an example, this string can be used with such commands as *ping*, *host*, *dig*, etc (like *ping node58316*)<a id="jps-import"></a>.
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## JPS Import Improvements

The platform [import](/environment-export-import#import) is a highly popular feature which, in particular, allows to install [JPS packages](/application-manifest) (i.e. file with an environment or add-on description - its topology, configuration, application to be deployed, etc.) directly through the dashboard. This time, in order to simplify new packages delivery, the already existing abilities to insert JPS manifests with local file or via direct URL were complemented with a new possibility to specify manifest content right during the import operation through the embedded JSON editor. This option is now available within the same-named tab of the **Import** window, where you can paste your code and edit it on fly or write a completely new one from the scratch.

Platform JSON editor is complemented with basic editing tools, needed for comfortable work with code - find out the buttons at the top pane:

* ***format JSON*** - automatically sets the proper indentation and line feeds
* ***wrap lines*** - brakes lines upon reaching frame border
* ***search*** - allows to easily find the needed information, including additional *Match case* and *Regex* search options

Once pasted, your code is automatically parsed for errors, which, if detected, will be marked with a red cross before the corresponding line (hover over it for additional information). Also, your JSON file is safely retained in browser local storage, so you can freely close **Import** frame without losing the stored data to continue your work with dashboard, and return to coding later on.

With an aim to make **Import** more notable and easier to access, this option was placed to the top of the tools dashboard pane alongside with the **Create environment** button. 

[More info](/environment-export-import#import)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Increased SSH Gateway Performance
In the PaaS 4.8 upgrade, a major update has been applied to the platform [SSH Gateway](/ssh-overview), with the multi-threads support implementation as a main point. Another big change was a great optimization boost, that speeds up such operations as downloading, uploading and file copying in dozens of times. Apart from that, CPU load during these processes was optimized for being highly cut down, whilst added multi-threading support ensures absence of the additional performance dropdowns, as it will be proportional to the current threads count.

Also, the [Add SSH Key](/ssh-add-key) form (for both public and private keys) at user's dashboard was slightly updated to make it a bit more clearer. In particular, each uploaded SSH keyfile is now displayed with additional info on its fingerprint and unique ID, allowing to differentiate and find the required one easier<a id="export-directory"></a>.
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Export Directory Dialog for File Manager

Striving to simplify [Data Storage Container](/data-storage-container) management, this time we've implemented new possibility of sharing directories right from the source node's Configuration Manager. This eliminates the necessity to switch to the target container to add the required [mount point](/mount-points). 

So, once the manager is opened, the appropriate new form can be accessed via the ***[Exports](/storage-exports)*** menu section (with the same-named button at the top tools panel inside) or directly from the file tree (within the gear icon's context menu) of any node. In the opened ***Export Path From*** tab the following options will help you to specify the necessary data:

* **From NFS** - drop-down list of containers within current environment layer to select the one the directory should be exported from
* **Path** - type in full path to the exported folder (or choose it among favorite ones)
* **To Container(s)** - specify target container to share the directory with using drop-down list of all nodes (in all environments) on your account
* **Path** - path to the location at the chosen target container the shared data should be available at 
* **Mount to all nodes** - use this switcher to set the same mounts for being added to all nodes within the destination layer
* **Read Only** - turn the switcher on to restrict editing of the exported data at client node(s) (by default, the *read & write* permissions are provided)

In this way, now you are able to quickly share the data in both directions, i.e. either from source or target container. Herewith, in order to properly handle this functionality at Docker-based containers, both shared directory paths (i.e. at its source and target nodes) are automatically added as [volumes](/docker-volumes). This ensures that the shared data will be protected during Docker container lifecycle operations (e.g. [redeploy](/docker-update)) at any of them<a id="java-memory-optimization"></a>.
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Default Memory Configs Optimization for Java Containers
In order to improve performance of Java-powered containers (including [cartridge-based](/cartridges-overview)  ones), a new optimized flow for the main memory configurations generation was implemented.

In particular, this considers the **MaxHeapSize** (*Xmx*) and **MaxPermSize** parameters' values:

* The first setting sets the maximum amount of memory that can be used by Java objects within a container. For now this value is calculated as 80% of total container's RAM. 
* As for the second parameter, it defines the maximum space for the compiled Java classes, initiating execution of the [garbage collection](/garbage-collector-overview) mechanism when it is overflowed. Herewith, *MaxPermSize* is automatically defined only for that Java containers, which are run over 6 or 7 engine versions and with allocated amount of RAM &gt; *800 MiB*. In all other cases (i.e. if container's scaling limit is less than 7 [cloudlets](/cloudlet) or it uses Java 8) this parameter is omitted. The actual value of the *MaxPermSize* setting is calculated based on *Xmx* memory amount divided by ten, but can't be set greater than maximum of *256 MiB*. 
* Also some changes were applied to the GC selection algorithm - the details can be revealed within the newly integrated [Java memory configuration script](https://github.com/jelastic-jps/java-memory-agent/blob/master/scripts/memoryConfig.sh).

In such a way, container's memory configurations are dynamically changed due to the amount of allocated resources, which provides the best optimization for your Java containers at the platform<a id="file-manager"></a>.
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## File Manager Improvements

The platform [configuration manager](/application-configuration) provides easy access to container filesystem right through the dashboard, allowing to apply some common configurations via browser with no additional tools involved. Herewith, it is constantly updated to provide even better user experience.

So, in confines of the present platform upgrade such amendments were applied to it:

* Since tracking and logging of the performed actions in [task panel](/dashboard-guide/#tasks) represent an important part of user experience, currently it was improved to show the proper file name for the *create*, *delete*, *rename*, *read* and *save *file operations, performed through configuration manager.
* From now on, while performing uploading through Config manager, the platform correctly detects whether the transferred file already exists and, if it does, automatically triggers the overwrite dialog. Herewith, you can either confirm replacement or abort operation.
* Lastly, a new improved flow is now used to check whether the accessed file is text or not (i.e. to define whether it's content should be displayed inside file manager and be available for editing). It allows to examine file more precisely, preventing a rare issue of the incorrect type determination<a id="software"></a>.
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:

|                        Stack                        |                        PaaS 4.8                        |
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
|***nginx***|1.8.1|
|***Maven***|3.3.9|
|***Centos 7***|7.2|
|***Memcached***|1.4.24|
|***Apache***|2.4.6-40|
|***NGINX PHP***|1.8.1|
|***NGINX Ruby***|1.8.1|
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
|***Node.js 4***|4.3.0|
|***Node.js 5***|5.6.0|
<p style="text-align: right;"><a href="#improvements">Back to the list of Improvements</a></p>


## Bug Fixes

In the table below, you can see the list of bug fixes in PaaS 4.8:

{{%bug-fixes title="PaaS 4.8"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-19102|The already shared with *view* rights environment can be re-shared for the same user
JE-26900|Incorrect link for automatic horizontal scaling in dashboard
JE-26950|Incorrect *Loading Value* rounding for *Network *load alert trigger
JE-26995|New or edited variables are not added/changed at the linked Docker containers
JE-27021|Improper validation of the &ldquo;.&rdquo; symbol during the custom Docker image addition
JE-27059|Rarely, the environment creation action is duplicated 
JE-27069|Master Container tab in the *Add Mount Point* section should be disabled for Maven node
JE-27070|File manager becomes inaccessible if external NFS-server with mounted data is not available
JE-27092|The *samyroad/atlassian-jira-software:latest *Docker image can not be started
JE-27113|The Apply button for FTP Users add-on is active even if no change was done
JE-27125|The *gitlab/gitlab-ce* Docker image can not be installed
JE-27154|Incorrect description for the *Permission denied* error in Task Manager
JE-27155|Duration of the export operation in Environment status differs from the same in Task manager
JE-27156|An error occurs while saving changes for all instances in a folder, mounted as Master Container
JE-27350|Improper symlinks handling during the Data Storage Container mount operation
JE-27410|An error appears when trying to access Add-Ons board for the already removed from the platform cartridge
JE-27416|Incorrect validation error message for too long environment names in topology wizard
JE-27425|An error occurs while trying to read *.jsp *file through the file manager
JE-27440|Empty database dump is exported via phpPgAdmin for Postgresql node
JE-27571|Text files can not be edited via File Manager for legacy containers (based on CentOS 5)
JE-27777|Crash report appears for Docker containers with &ldquo;{&rdquo; and &ldquo;}&rdquo; characters in environment variables names
JE-27809|High availability option is displayed for the Tomcat 8 cartridge, which has been already disabled at a platform
JE-27868|Environment can work over HTTPS even without SSL being enabled
JE-27973|Direct connection to container via SSH Gateway doesn't work after environment migration
JE-28056|The *cachethq/docker* Docker image can not be started
JE-28081|Environment actions menu disappears after passing the Welcome tutorial
{{%/table%}}
{{%/bug-fixes%}}

{{%right%}}[Back to the top](#back){{%/right%}}