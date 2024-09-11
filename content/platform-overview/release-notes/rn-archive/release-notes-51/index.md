---
draft: false
title: "Release Notes 5.1/5.2"
aliases: "/release-notes-51/"
seoindex: "index, follow"
seotitle: "Release Notes 5.1/5.2"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the PaaS 5.1 and 5.2..."
---

<a id="back"></a>

# Virtuozzo Application Platform 5.1/5.2

*This document is preliminary and subject to change.*
In this document, you will find all of the new features, enhancements and visible changes included to the **PaaS 5.1** and **5.2** releases:

* [Features](#features)
* [Improvements](#improvements)
* [Bug Fixes](#bug-fixes)

For<a id="features"></a> detailed information on using any of the platform features, please refer to the [users' documentation](/).


## Features

[Transition of Platform Infrastructure into Docker Containers](#infrastructure-in-docker) 
[Optimized UX for Deployment, Tasks and Env Management Panels](#management-panel)  
[Billing History Data Export](#billing-history-export)  
[Auto Update of Dockerized Stack Templates](#dockerized-stacks-auto-update)  
[FTP Access to Storage Container](#ftp-acces-to-storage-container){{%back%}}{{%/back%}}


## Transition of Platform Infrastructure into Docker Containers

The [infrastructure node](/cluster-orchestrator) represents a set of internal components, responsible for performing all operations within the platform (e.g. managing resources, processing requests, supporting system maintenance, etc.). Starting with 5.1 PaaS release, all infrastructure modules are provisioned as [Docker containers](/dockers-overview), ensuring the following inherent benefits of this [containerization technology](https://www.docker.com/what-docker):

* *resource utilization* - allows to apply more lightweight solutions with lower resource consumption to run applications 
* *standardization and compatibility* - reduces risk to meet problems with resolving application dependencies or OS related issues, as Docker containers run in the same way on any hardware
* *isolation and security* - ensures infrastructure modules' insulation (so that containers can't affect host system or each other), which grants complete control over traffic flow and management

As a result of such transition, the Platform upgrade procedure was notably simplified and accelerated, allowing to deliver new platform features much more quicker.
[More info](/cluster-orchestrator)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Optimized UX for Deployment, Tasks and Env Management Panels

In order to simplify operating with multiple environments in the platform [dashboard](/dashboard-guide/), its user interface layout has been updated. For that, **Deployment Manager** and **Tasks** sections were merged into a single collapsible frame with the appropriate tabs being available at the bottom of the dashboard. If needed, this panel can be minimized to free more space for your environments list display, making it easier to access the required options.  
Also, upon working with a particular environment, a dedicated tab will be opened at the bottom of the above-mentioned frame (next to the default *Tasks* and *Deployment Manager* ones). Here, all available management operations for this environment (like *Settings*, *File Manager*, *Logs*, *Statistics*, etc.) are grouped, being opened into separate sub-frames within a single tab. Herewith, such additional environment-dedicated tabs can be closed if they are no longer needed, while *Tasks* and *Deployment Manager* ones are opened permanently.  
[More info](/dashboard-guide/)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Billing History Data Export
To help you with financial analysis of hosting spends, a possibility to download [billing history](/consumed-resources#billing) as a ***csv*** file was implemented within the current 5.1 Platform version. The appropriate **Download CSV** button was added to the **Billing history** section (for both per *environment* and per *account* options). In order to make the displayed data more clear  and to speed up its fetching, the following gradation was added for the **Interval** field:

* *hour* - can be used with 1 day period
* *day* - can be used with 7 days period
* *week* - can be used with 4 weeks period
* *month* - can be used with 1 year period
* *year* - can be used with 10 years period

Herewith, by shifting the data range (with the appropriate **Start** and **End** fields), you can get a granular  billing history info even for the oldest data. For example, to get statistics on daily spends from a year ago, specify a period with 7-day difference or less (e.g. from 01-01-2016 to 07-01-2016)<a id="dockerized-stacks-auto-update"></a>.
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Auto-Update of Dockerized Stack Templates
Within the current platform upgrade, a special *tags auto-update* option was implemented for [dockerized templates](/release-notes-505#certified-stacks-conversion). This feature is intended to regularly renew the lists of provisioned stack versions according to the latest updates within the central templates repository. As a result, new software releases become automatically available for you with almost no delay due to eliminating the necessity of hosting provider's manual intervention. Herewith, the update frequency and enabling of this feature in general depends on a particular platform settings.

In conjunction with the [latest tag](#ui-latest-tag) improvement, such tags auto-update approach allows to keep utilized server software actual - the delivered updatescould be easily integrated by means of the [Docker container redeploy](/docker-update) functionality<a id="ftp-acces-to-storage-container"></a>.
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## FTP Access to Storage Container
In order to make data management within [Storage container](/dedicated-storage-container) more comfortable, [FTP support](/ftp-ftps-support) was implemented for this type of node. Within the current 5.1 Platform release, FTP add-on was updated to enable its installation on Storage environment layer just as on any other one (load balancer, application server, etc.). Immediately after that, you can start [working over FTP](/ftp-ftps-support#c) with any prefered client application (e.g. FileZilla) to transfer files, read and download logs, edit configurations, synchronize folders content and so on.

[More info](/ftp-ftps-support)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Improvements
[UI/UX Improvements](#ui)  
[API Improvements](#api)  
[MySQL/MariaDB Security Enhancements](#mysql-mariadb-security)  
[Default Aliases for Container Hostname](#containers-hostname-aliases)[Master Node Environment Variables (5.2)](#master-node-variables)<a href="#containers-hostname-aliases"></a>  
[Fixes Compatible with Prior Versions](#compatible-fixes)  
[Software Stack Versions](#software)
{{%back%}}{{%/back%}}  


## UI/UX Improvements
[Latest Tag for Dockerized Stack Templates](#ui-latest-tag) 
[Basic Management Options within Empty Environment Group Layout](#ui-basic-options-for-empty-group)  
[Clarification on Port Settings for Docker Containers](#ui-port-settings-clarification)  

#### Latest Tag for Dockerized Stack Templates
To simplify operating with various software, all platform dockerized stacks were complemented with dedicated *latest* tags: per whole template (*tomcat:latest*, *mysql:latest*, etc.) and per each major stack version (*tomcat:7-latest*, *mysql:5.7-latest*, *mariadb:5-latest*). Herewith, the appropriate grouping is automatically applied to stack tags list within topology wizard:

* *if stack has several versions*, they will be shown in the expandable list with the *latest* tag at the top (hover over to see the exact version)
* *if stack has several minor versions of the same major one*, the appropriate record will be converted into a general view (e.g. *7.x.x*) with a list of exact minor releases and the corresponding latest tag (e.g. *7-latest<a id="ui-basic-options-for-empty-group"></a>*)

{{%right url="#ui" text="Back to the list of UI Improvements"%}}{{%/right%}}


#### Basic Management Options within Empty Environment Group Layout
With an aim to make dashboard UI more intuitive, background for an empty [environment group](/environment-groups) was updated with buttons on a number of common actions, which may be needed to get started with this feature. Namely, quick access was provided to the following operations:

* *[Create New Environment](/setting-up-environment)*
* *[Add Environment to This Group](/environment-groups-management#edit-group)*
* *[Deploy Solution from Marketplace](/marketplace)*

And for the case there are no environments within an account at all, the similar background was added to the dashboard start page. Herewith, the *[Collaborate on Shared Environment](/account-collaboration)* option is shown instead of the *Add Environment to This Group* one.
[More info](/environment-groups)
{{%right url="#ui" text="Back to the list of UI Improvements"%}}{{%/right%}}


#### Clarification on Port Settings for Docker Containers
By default, all [Docker containers](/dockers-overview) within the platform are provisioned with the following open ports: *80*, *8080*, *8686*, *8443*, *4848*, *4949* and *7979*. In case any other container port is needed to be accessed via Shared Load Balancer, the appropriate [endpoint](/endpoints) can be easily attached to the environment. Alternatively, [Public IP](/public-ipv4) can be used to get direct access to all container ports.  

To make such specifics more clear, the appropriate [Ports](/docker-ports) tab within the Docker container settings wizard was updated. For now, it provides a core information on default ports, endpoints / Public IP usage and has a special explanatory image to visualize ports behaviour, making it easier to percept.
[More info](/docker-ports)
{{%right url="#ui" text="Back to the list of UI Improvements"%}}{{%/right%}}


## API Improvements
[New *GetEnvs* Method with Pre-Sorted Response](#api-sorting-for-getenv)   
[*Set-* & *Get- ContainerEnvVars* Methods for Environment Layer](#api-containerenvvars-methods)    
[Support of Parameters Aliases within CLI Commands](#api-parameters-aliases-for-cli)  
[Updated Namespace for API Calls within Cloud Scripting](#api-namespace-for-cs-calls)


#### New *GetEnvs* Method with Pre-Sorted Response
The ***GetEnvsByCriteria*** is a new [API method](https://www.virtuozzo.com/application-platform-api-docs/) which allows to get information about all your environments whilst sorting them to simplify the perception. It uses a special ***criteria*** parameter (specified in JSON format) with the following options:

* ***order*** - can be assigned either *ASC* or *DESC* value to sort environments in ascending / descending order respectively
* ***orderField*** - sorts environments by either *status* (e.g. running, stopped) or *name*

In case of a big number of applications and projects being run on an account, this method can help to speed up and simplify the appropriate data fetching.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}


#### *Set-* & *Get- ContainerEnvVars* Methods for Environment Layer
In the present PaaS 5.1 release, two new [API methods](https://www.virtuozzo.com/application-platform-api-docs/) were added to help managing [environment variables](/docker-variables) in Docker containers and dockerized stacks. Both operations were designed to work with all the nodes within a layer:

* ***GetContainerEnvVarsByGroup*** - gets list of all the environment variables
* ***SetContainerEnvVarsByGroup*** - sets variable values for nodes of a particular type

In conjunction with the on-going conversion to the [dockerized templates](/release-notes-505#certified-stacks-conversion), these API methods will be especially useful, as they will become applicable for all platform-managed stacks.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}


#### Support of Parameters Aliases within CLI Commands
A lot of [API methods](https://www.virtuozzo.com/application-platform-api-docs/) in the platform have a number of aliases for their parameters (i.e. alternative names, which can be used on a par with original denominations). Usually, such variations appear due to steady API development, supporting legacy implementations and ensuring backward compatibility. For example, the frequently used *envName* parameter can be equally replaced with its previous *appid* or *domain* denominations, whilst *zdt* parameter name can be similarly substituted with the *atomicDeploy* string, and so on.

In the current 5.1 platform upgrade, support of such aliases was implemented for [platform CLI](/cli) as well (including the appropriate parameters designation within JSON files). This allows developers to operate with the same preferred parameter denominations when using both API and CLI.

[More info](/cli)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}


#### Updated Namespace for API Calls within Cloud Scripting
The platform [API documentation](https://www.virtuozzo.com/application-platform-api-docs/) provides examples on calling methods via HTTP using URL (***REST***) and through [Cloud Scripting](https://docs.cloudscripting.com/) (***Scripting***). In the current upgrade, namespace for the latter one was updated to a new format through substituting its *hivext* part with *jelastic* string. As an example, for now the following expression should be used when referring to VCS API requests - *jelastic.environment.Vcs.{method-name}*. Herewith, the former version (i.e. *hivext.environment.Vcs.{method-name}*) is considered outdated, although remaining operable for compatibility reasons.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## MySQL/MariaDB Security Enhancements
According to native *MySQL* and *MariaDB* implementation specifics, a one will see the appropriate directory content if accessing a page with no specified entry point on these servers via direct URL. In most cases, such behaviour should be avoided as it may reveal some sensitive data (e.g. backups, temporary or hidden files, etc.), which must not be exposed for clients. Thus, restriction on directory indexing was enabled for both MySQL and MariaDB stacks.

Another implemented improvement is automatic generation of self-signed certificates for MySQL/MariaDB nodes, which allows to establish encrypted *HTTPS* connection to their admin panels via [Public IP](https://www.virtuozzo.com/application-platform-ops-docs/public-ip-shared-resolver) right after instance creation, i.e. without any additional configurations being required<a id="containers-hostname-aliases"></a>.

{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Default Aliases for Container Hostname
When referring to a particular container, two formats of a hostname could be used in the platform internal DNS (with either hyphen or period as a separator):

* <i>node**{node_id}**-**{env_name}**.**{hoster_domain}**</i> - default record for all node types
* <i>node**{node_id}**.**{env_name}**.**{hoster_domain}**</i> - additional record for [Docker containers](/dockers-overview) (i.e. beside of the default common one)

where:

* ***{node_id}*** - unique container identifier
* ***{env_name}*** - internal environment domain (based on environment name, set during its creation)
* ***{hoster_domain}*** - domain name of a [platform](/paas-hosting-providers/) a node was created at

From now on, both of the above-specified records will be automatically added for each new container and can be used for refering to both native and Docker containers. Herewith, for the already existing containers, number of DNS records will remain the same<a id="master-node-variables"></a>.

{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Master Node Environment Variables (5.2)
When setting up an environment topology, the very first instance to be created on a particular environment layer is automatically considered as a *master*, i.e. the main one. For example, such initial container will be taken as a template for all layer nodes during [environment cloning](/clone-environment) or, in case [High-Availability](/session-replication) is enabled, applications will be deployed only to the master node. Starting with the 5.2 PaaS version, each newly created Docker container (and dockerized stack) is provisioned with the master node details for a layer it is placed at, which are defined within the appropriate [variables](/docker-variables):

* ***MASTER_ID*** - unique digit identifier (*Node ID*), e.g. *226501*
* ***MASTER_HOST*** - network address for referring to a master node, composed of container ID and environment name (without the Platform domain suffix), e.g. *node226501-my-app*
* ***MASTER_IP*** - master container internal IP address, e.g. *192.168.13.31*

Such implementation will help to identify master node much easier - for example, to discover a container where the data is actually stored when utilizing [master as a storage](/master-container-storage) for sharing data across the layer. Also, when packaging [clustered solutions](/cluster-in-cloud) via [JPS](/jps), these variables allows to prescribe the appropriate master node host and IP address fetching without an environment being actually created yet<a id="compatible-fixes"></a><a id="mobile-number-filtering"></a>.

{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Fixes Compatible with Prior Versions

Below, you can find lists of fixes which except of being implemented within PaaS 5.1 and 5.2 releases, have been also integrated to preceding platform versions by means of the appropriate patches:

{{%table3 title="PaaS 5.1"%}}
**#**|**Compatible from**|**Description**
---|---|---
JE-28966|2.5|The *File Synchronization* add-on can not be installed due to the deprecated CS format used in the manifest file
JE-27263|3.3|Error occurs, while installing the *Cyclos 4* package
JE-32240|3.3|Correcting default email settings for the *osTicket* package
JE-32739|3.3|Adjusting *File Synchronization* add-on to enable its installation on top of [dockerized stacks](https://www.virtuozzo.com/application-platform-ops-docs/dockerized-stack-templates)
JE-27140|4.2|Validation message clarification for the user name field in the *FTP Users* add-on
JE-25656|4.5|Crash report appears, while updating a *New Relic* add-on, which is installed on top of Apache PHP application server
JE-31739|4.8|Incorrect documentation link within the *Traffic Distributor* package description at the platform Marketplace
JE-29996|4.10|Support and integration of a new *Spring Boot* Java application server
JE-31252|4.10|Indication of environment groups and layers within SSH Gate menu at terminal
JE-31970|4.10|Making environments in the nested (child) environment groups being displayed within SSH Gate terminal menu
JE-32560|4.10|Shared environments can not be accessed by collaborators via SSH Gate, due to owner UID usage by SSH client
JE-32569|4.10|Ability to connect to nodes without internal IP via SSH Gate
JE-32721|4.10|Updating legacy VDS labeling for VPS nodes in SSH Gate terminal menu
JE-32722|4.10|Pre-sorting of containers by environment layer within SSH Gate terminal menu
JE-31155|4.10.2|Fixed issue with MSSQL node creation failure due to the password for *sa* user occasionally being not generated by the system
JE-31300|4.10.2|Sometimes platform CLI could not be installed due to Java exception
JE-26792|5.0.5|Fixed error during restarting dockerized *Varnish* load balancer stack
JE-31473|5.0.5|Crash report appears when installing the *TimeZone* add-on on top of dockerized stacks
JE-31553|5.0.5|The *Drupal* package from platform Marketplace can not be opened in browser due to incorrect Apache version
JE-31812|5.0.5|The */use/java/tzupdater.jar* file is absent within Java-based dockerized stacks (i.e. Tomcat and TomEE)
JE-31875|5.0.5|Incorrect permissions for the */var/spool/cron/nginx* file on the dockerized stack of Nginx PHP
JE-31910|5.0.5|The *logdb_bckp.log* file is not created after first backup procedure on the dockerized stack of MySQL 5.7
JE-32633|5.0.5|The *locale* command return errors after updating *glibc* on dockerized stacks
JE-32645|5.0.5|Unmasking *systemd-logind* to avoid warning messages in *var/log/messages*
JE-32679|5.0.5|Error message appears during successful *MySQL / MariaDB / Percona* databases restart
JE-32715|5.0.5|The *screen* session can not be opened, while connected to container with dockerized stack via SSH Gate
JE-32719|5.0.5|Updating tag label for *MariaDB 10* based on the actual database version
JE-32809|5.0.5|Forbidding directory listing on the dockerized PHP stacks after Git / SVN deploy
JE-32893|5.0.5|The dockerized *TomEE* stack can not be accessed via SSH Gate
{{%/table3%}}


{{%table3 title="PaaS 5.2"%}}
**#**|**Compatible from**|**Description**
---|---|---
JE-31984|4.10|Displaying environment topology changes after refresh in SSH Gate terminal menu
JE-32965|5.0.5|Adding system libraries, which are required for some dynamic extensions, to the PHP module
JE-32913|5.1|Updating permissions for the *keys* folder on the dockerized Varnish stack to allow file creation
JE-32967|5.1|Setting proper *Common Name* for the auto generated self-signed certificates on databases with Public IP
<a id="software"></a>
{{%/table3%}}
{{%right%}}[Back to the list of Improvements](#improvements){{%/right%}}


## Software Stack Versions

The most notable software stack updates in confines of PaaS 5.1 and 5.2 releases are:

* the legacy **Ruby** versions (namely **1.9.3**, **2.0.0** and **2.1**) are no longer maintained by the platform
* the latest **Ruby 2.4** release was added
* the **RHEL** OS [template support](/docker-supported-distributions) was implemented for Docker containers


This way, for now the list of the component templates versions is the following:

|Stack|PaaS 5.1/5.2|
|---|---|
|***Tomcat 6***|6.0.53|
|***Tomcat 7***|7.0.77|
|***Tomcat 8***|8.5.5|
|***TomEE***|7.0.3|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_79|
|***Java 8***|1.8.0_131|
|***MariaDB***|5.5.56 / 10.2.6|
|***MongoDB 2.6***|2.6.11|
|***MongoDB 3.0***|3.4|
|***MySQL***|5.6.36 / 5.7.18|
|***PostgreSQL***|9.5.5|
|***CouchDB***|1.6.1|
|***nginx***|1.10.1|
|***Maven***|3.5.0|
|***Centos 7***|7.2|
|***Memcached***|1.4.24|
|***Apache***|2.4.6-45|
|***NGINX PHP***|1.10.1|
|***NGINX Ruby***|1.12.0|
|***PHP 5.3***|5.3.29|
|***PHP 5.4***|5.4.45|
|***PHP 5.5***|5.5.38|
|***PHP 5.6***|5.6.28|
|***PHP 7***|7.0.13|
|***PHP 7.1***|7.1.0|
|***Ruby 2.2***|2.2.7|
|***Ruby 2.3***|2.3.4|
|***Ruby 2.4***|2.4.1|
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

In the table below, you can see the list of bug fixes in PaaS & CaaS 5.1 and 5.2:

{{%bug-fixes title="PaaS 5.1"%}}
**#**|**Description**
---|---
JE-19273|Parameters set by the *JAVA_OPTS* variable are not applied and not exported on Jetty 8 and JBoss 7 
JE-24012|Platform CLI client displays a login prompt, while a user is actually trying to sign out 
JE-26295|Platform API allows to add and edit a project with Maven where interval to check and auto-deploy updates has a negative value (less than 1 minute)
JE-27765|String index exception occurs while moving any file from the *~/jelastic* directory and running it with parameters via platform CLI 
JE-28497|Permissions to sub-directories differ from the ones to *ROOT *
JE-28536|Ability to execute the *BindSSL* API request for environment without Public IP or with unsupported node type
JE-28667|Unhandled error occurs while importing the corrupted JSON manifest from a local file
JE-28913|Member of collaboration with the *Viewer* permissions can delete log files on a shared environment
JE-28954|Member of collaboration with the *Viewer* permissions can deploy projects to an application server on a shared environment
JE-29435|Incorrect class names are provided for some API methods 
JE-29863|The *star* icon is displayed next to the level-up arrow after clicking *Refresh* in the Config Manager
JE-29876|Ability to create new MongoDB database and user with no access restrictions
JE-29943|Incorrect validation for right-to-left (RTL) text in domain names
JE-30064|Environment status is not changed after cloning
JE-30197|Unknown error occurs while creating a new environment
JE-30465|The *getdockerenvvars* and *getcontainerenvvars *API requests return an unknown error
JE-30567|Unhandled error occurs instead of a custom error when using custom buttons in Cloud Scripting add-on packages
JE-30685|Impossible to mount directory from environment with cyrillic symbols in the name
JE-31001|The *Enter* key doesn't work while adding new environment group or applying changes to the existing one if the cursor is out of the input field 
JE-31007|Improper behavior of the *Disk Limit* slider box in the wizard
JE-31019|The *Delete* button appears cropped for environments with long names and aliases in the *Add Group* dialog box
JE-31020|The environment status is not clear from the icon that appears while adding environment to a group
JE-31066|Unclear description on how to create a new environment group from the *+ Add to Env Group* dialog box
JE-31068|The *Groups* list remains displayed after pressing *Enter* to select a particular group
JE-31143|Inability to create or rename a file located in a directory that was earlier renamed
JE-31739|Invalid link to the *Routing Methods* page in the Traffic Distributor installation box 
JE-31872|Installation of the Cloud Scripting package with *Payara Micro Advanced Cluster* fails
JE-31892|Error appears while editing or removing a Git/SVN project deployed to the mounted context 
JE-31911|Backup script for MariaDB is not executed with the *dumpall *option
JE-31987|The *su root root* value is not returned from the *logrotate* config file on Fedora Docker image
JE-31997|Renaming a *child* environment group can make it disappear or cause an unknown error
JE-32037|No valid login shell is available for user in *run.log* on the RHEL-based Docker image
JE-32039|Incorrect *Disc Limit *set for some nodes
JE-32087|Error occurs while adding custom SSL certificate to the GlassFish-based environment
JE-32132|Some common vulnerabilities and exposures affecting the MySQL server 
JE-32140|Incorrect firewall rules for the dockerized stack template with Memcached 
JE-32161|Member of collaboration with the *Viewer* permissions can't access the *Mount Points* and *Exports* directories on a shared environment
JE-32168|Newly added variable is missing within the scaled nodes of a dockerized stack template
JE-32202|Account limits are exceeded while importing the Cloud Scripting package on an account with sufficient permissions
JE-32281|Failure to deploy EJB project to TomEE application server 
JE-32350|The *Scaling Limit* box appears cropped in the wizard for a deselected stack layer
JE-32377|The *High-Availability *button is present in the wizard for unsupported stack layers
JE-32394|The *sendmail* service is not available on a dockerized stack template
JE-32420|Member of collaboration with the *Viewer* permissions can't stop or start a shared environment
JE-32505|No active tasks are displayed in the *Tasks* panel while uploading an archive from a local file
JE-32507|HTTP transport error appears while uploading an archive with a size larger than allowed
JE-32538|Failure to install the Let's Encrypt add-on on Apache-PHP due to the broken *locale* identifiers
JE-32610|The *Redeploy containers* list for dockerized stacks includes tags that are not provisioned by the hosting provider 
JE-32664|Inability to redeploy dockerized containers in case a selected tag was repealed by a hosting provider but remains available within the source image on Docker Hub
JE-32792|Incorrect formatting of SSH connection string sent to a user via email
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.2"%}}
**#**|**Description**
---|---
JE-30851|Incorrect redirect from port *80* after the Node.js application server restart
JE-32293|Two external IPs are added, while attaching Public IP to the stopped container
JE-32720|Collaboration members can't change topology after being granted the sufficient permissions
JE-32749|Docker containers, which specify users via uid can not be created
JE-32751|Maven node fails, while building EJB project that contains a JAR file 
JE-32807|Environments, which are stuck in the Creating status, are not automatically removed
JE-32879|Inability to export data from *Storage* container 
JE-32901|Incorrect display of the *Actions* log tab after restarting node
JE-32907|Sometimes, the *ResetServicePassword*, *ResetNodePassword*, *RestartServices* and *RestartNodes* API methods don't respond
JE-32928|Error occurs while saving changes to a file, which contains pictograms via the Config manager
JE-32932|Error appears while creating environment with the MSSQL or IIS Windows-based stacks
JE-32939|Calling the API request with legacy *APPID* format fails
JE-32944|Topology wizard is not updated after switching from the Docker container tab
JE-32946|Owner can manage environment after transferring it to another account
JE-32968|Simultaneous creation of several environments fails due to SSL-related errors
JE-33002|Unhandled error occurs while adding mount point to a file
JE-33003|Session error appears while building project with Maven node
JE-33005|Archives with spaces and special symbols in name can not be deployed
JE-33012|Incorrect template names are displayed in the *Quotas & Pricing &gt; Software *tab
JE-33023|Rarely environments can not be created due to inability to connect to GitHub
JE-33024|Deployment to environment fails due to missed DNS records
JE-33068|The *Tasks* tab is empty after creating first environment on a new account during the *Welcome* tutorial
JE-33075|SSH Gate can not be access by users during Platform maintenance
JE-33100|SSL certificates uploaded via Deployment manager are displayed incorrectly
JE-33154|Email notification about account deactivation is not sent to users
JE-33178|Environment transfer request can not be resent after the previous one being cancelled
JE-33181|Email notification about account being destroyed is not sent to users
JE-33212|Content of the mounted folder is not available on the scaled GlassFish instances
{{%/bug-fixes%}}

{{%right%}}[Back to the top](#back){{%/right%}}