---
draft: false
title: "Release Notes 4.9.5"
aliases: "/release-notes-495/"
seoindex: "index, follow"
seotitle: "Release Notes 4.9.5"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included in the platform..."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.9.5

*This document is preliminary and subject to change.*
In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS 4.9.5** release:

* [Features](#features)
* [Improvements](#improvements)
* [Bug Fixes](#bug-fixes)

<a id="features"></a>
For detailed information on using any of the platform features, please refer to the [users' documentation](/).


## Features
[Tomcat 9 Support](#tomcat9)  
[Ubuntu Support for Elastic VPS](#ubuntu-vps)  
[Export/Import for Docker & Windows Containers](#docker-windows-export-import)  
<a href="#back" id="tomcat9">{{%back%}}{{%/back%}}</a>


## Tomcat 9 Support
**Tomcat 9** (*alpha* stage currently) represents the latest release of the Apache Tomcat application server, which includes multiple changes and bug fixes (see the <a href="http://tomcat.apache.org/tomcat-9.0-doc/changelog.html#Tomcat_9.0.0.M15_(markt)" target="_blank" rel="nofollow">official changelog</a> for details). Among the most notable treats, it runs only *Java 8* engine and implements *Servlet 4.0* version. Also, Tomcat 9 utilizes the latest Java specifications: *JSP Spec 2.4*,* EL Spec 3.1* and *WebSocket Spec 1.2* (the [exact versions](http://tomcat.apache.org/whichversion.html) may be changed after the stable release). All of this ensures smooth and comfortable user experience during your Java apps development.  
The platform delivers Tomcat 9 in a form of [OpenShift-based cartridge](/cartridges-overview) and was integrated to all Platforms starting from PaaS 4.2 version. Herewith, similar to the rest of custom stacks, its availability at every particular cluster installation depends on hosting service provider settings.

[More info](/tomcat8-9)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Ubuntu Support for Elastic VPS

[Elastic Virtual Private Server](/vps) represents a bare independent virtual machine. Extending the number of supported OS distributions for this kind of stack, the present PaaS upgrade includes provision of the platform-certified ***Ubuntu*** template for VPS hosting. The exact version of delivered OS distribution is the latest stable [Ubuntu 16.04](https://wiki.ubuntu.com/XenialXerus/ReleaseNotes/16.04) release. This allows you to get all the functionality of isolated scalable VPS, simultaneously enhanced with Ubuntu performance capabilities.

Just as the rest of virtual private servers, Ubuntu-based VPS instance can be created right through the corresponding *VPS* section of the environment wizard. Herewith, unlike [CentOS](/vps-public-ip) and [Windows-based](/win-vps) VPS instances, this stack doesn't provide the inbuilt web interface for its management. Thus, all of the configurations should be applied through connecting to a node via SSH, where the full root permissions are granted.

[More info](/vps-ubuntu)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Export/Import for Docker & Windows Containers
In confines of PaaS 4.9.5 release, the [environment export/import](/environment-export-import) feature support was implemented for Docker- and Windows-based containers. From now on, you can effortlessly move environments containing such instances across [hosting partners](https://www.virtuozzo.com/application-platform-partners/) platforms.  
Similarly to the Storage, VPS and Maven nodes, both Docker and Windows containers are created from scratch when migrated (in accordance to the exported environment topology). Herewith, imported containers won't include any custom data (i.e. the appropriate *Private Data* and *Configuration File* options are disabled for selection within export frame). So, if needed, you should apply the corresponding changes and integrate the needed data manually afterwards.

The main [Docker containers settings](/docker-configuration) (such as *variables*, *links*, *local volumes *and* run configs*) will remain applied to containers at a new environment location. They are set the same for all instances within the appropriate environment layer based on the master node settings.

{{%tip%}}**Note:** Currently, exported environment copies with [mount points](/mount-points) from other environments or external sources can not be imported to a different PaaS installation. This possibility will be implemented in future releases.{{%/tip%}}

Also, while moving Docker container that was deployed from a [custom registry](/docker-custom-registry), the authentication data (username and password) won't be transferred due to security reasons. Thus, in order to successfully import such environment, you need to preliminary specify these credentials within the appropriate exported manifest file.

[More info](/environment-export-import)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Improvements
[Extended Custom SSL Support](#custom-ssl)  
[Increased IO Performance for Dedicated Storage Container](#storage-container-kernel-nfs)  
</a>[Logging of Collaborators Actions](#collaborators-actions-logging)  
[UI/UX Improvements](#ui-improvements)  
</a>[API Improvements](#api)  
[Engines & Supported OS Updates](#stack-updates)  
[Software Stacks Versions](#software){{%back%}}{{%/back%}}


## Extended Custom SSL Support
PaaS 4.9.5 release includes extension of the list of servers, that support ability to attach [custom SSL](/custom-ssl) certificates, with a number of custom stacks. Namely, *GlassFish 4*, *Tomcat 8 *and *Tomcat 9* templates were updated (*Jetty 9* will be added shortly). So, the appropriate newly created containers will support automatic appliance of the HTTPS traffic encryption directly via user dashboard (whilst the already existing containers won't be patched to get this possibility).
 
In case any of the above mentioned stacks is not available at a Platform you use, appeal to your hosting provider and request its addition.

[More info](/custom-ssl)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Increased IO Performance for Dedicated Storage Container

In the current 4.9.5 Platform upgrade, another major update was applied to the [Dedicated Storage Container](/dedicated-storage-container) in order to implement usage of more fast and optimized *Kernel Based NFS* server instead of the *FUSE* one. This grants notable boost of server performance,  increasing efficiency and user-appeal of the solution.

The new functionality will be automatically provided for the newly created Storage containers. In order to update the existing ones, the corresponding environment should be entirely stopped and then started again (i.e. not through just restarting a particular node) to apply the required changes.

[More info](/dedicated-storage-container)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Logging of Collaborators Actions

The platform [account collaboration](/account-collaboration) is substantial and highly valued by developers feature, as it allows to access a single environment from different accounts (e.g. organization units). Herewith, provided privileges can be tuned for each user separately by assigning one of the roles: *viewer* with general access permissions and *admin* with ability to change environment topology and full SSH access.

Starting with 4.9.5 PaaS version, environment owner is provided with information on all actions, applied to it by other collaboration participants. This is ensured with a special ***User*** column, added to the [Tasks manager](/dashboard-guide/#tasks) dashboard panel. It is shown only for owners (creators) of shared environments and provides email of the collaborator the changes were made by.

[More info](/account-collaboration)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## UI/UX Improvements
[File Manager](#file-manager)  
[Task Panel](#task-panel)  
[JPS Import Examples](#import-examples)  

#### File Manager

The platform [configuration manager](/application-configuration) provides an easy access to the container file system through the dashboard. This allows to apply some common configurations right via your browser with no additional tools required.  
Here are a few improvements that were implemented to configuration manager within the current platform upgrade in order to make it even more user-friendly:

* the path string above filesystem tree is now displayed without **ROOT** at the beginning, in such a way designating the location relatively to this main directory
* location of the currently selected file or folder is automatically added to the path bar at the top, allowing to easily define where it's placed and copy path to it
* the *Additionally *actions list was complemented with the new **Copy Path** option, that will add it to the clipboard
* the **return** option (in a view of backward arrow) was added to the beginning of file list, allowing to move one level up within file tree
* for the opened files, the **Refresh** button was moved to the left (next to the **Search** one), while the full file path is now displayed within the remaining panel part

[More info](/application-configuration)
{{%right url="#ui-improvements" text="Back to the list of UI Improvements"%}}{{%/right%}}

#### Task Panel

As a part of the dashboard interface, [Tasks panel](/dashboard-guide/#tasks) is used to monitor and analyze actions performed by the platform. Obviously, the displayed here data should be easily perceived. Thus, for now the list won't jump up to display the currently ongoing action during scrolling down and exploring other tasks, granting better user experience.

Also, some changes were applied to the minimized Tasks panel mode (can be enabled with the doubled down arrow at the top-right corner of the section). Upon this panel folding, the remained single row will show the following information according to the amount of active actions:

* *multiple tasks* - shows the number of currently performed actions (e.g. *5 active tasks*)
* *one task* - gives description for this ongoing action (e.g. *Adding Nginx 1.10 node to {environment name}*)
* *no tasks* - displays the idle status label (i.e. *No active tasks*)

[More info](/dashboard-guide/#tasks)
{{%right url="#ui-improvements" text="Back to the list of UI Improvements"%}}{{%/right%}}


#### JPS Import Examples

The platform [import](/environment-import) is a highly demanded feature that allows to install any [JPS package](/application-manifest) (i.e. JSON manifest file with environment or add-on description) right through the dashboard. This time, in order to improve the package delivery process, the new ***Examples*** link was added to the **Import** frame. 

Upon selecting it, you will be redirected to the [JPS Collection](https://github.com/jelastic-jps) page, which offers numerous ready-to-go packages and add-ons. This way, you can find the most suitable solution according to your needs or just explore them for being used as a basis for your own sample.

[More info](/environment-import)
{{%right url="#ui-improvements" text="Back to the list of UI Improvements"%}}{{%/right%}}
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## API Improvements
[&ldquo;Get&rdquo; Methods for Maven Build Node](#api-get-maven)  
[Returning Node Domain Name as Part of Endpoint Data](#api-endpoint-domain)  

#### &ldquo;Get&rdquo; Methods for Maven Build Node
The PaaS 4.9.5 release also includes new ***GetProjects*** [API](https://www.virtuozzo.com/application-platform-api-docs/) method, aimed to simplify remote Java VCS projects management. This request allows to fetch list of all projects, added to a Maven build node, and operates the following parameters:

* ***session*** *(string)* - is used to check user authentication
* ***envName*** *(string)* - selects the target environment
* ***nodeGroup*** *(string)* - points to the environment layer (use the &ldquo;*build*&rdquo; one)
* ***nodeId*** *(integer)* - numerical identifier of the container

Also, another ***GetProjectInfo*** method was supplemented with a new ***projectName*** parameter, which allows to get information about the project by its name, shown in the dashboard (rather than only by its unique ID, which should be additionally fetched with the *GetProjects*, *getEnvs* or *getEnvInfo* method).

[More info](/java-vcs-deployment/)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}

#### Returning Node Domain Name as Part of Endpoint Data

In the present 4.9.5 PaaS release, responses of the API methods that provide information on attached [endpoints](/endpoints) were extended with additional field. It was added to return the corresponding node(s) *domain* name alongside with the information on listened public and private ports. 

Namely, the ***AddEndpoint*** request and, in case of the attached endpoints presence, responses for the ***GetEnvInfo*** and ***GetEnvs*** calls were enhanced. This allows to get the whole node access URL much easier through combining domain name with the corresponding public port value.

[More info](/endpoints)
{{%right url="#api" text="Back to the list of API Improvements"%}}{{%/right%}}
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Engines & Supported OS Updates
The regular software stacks renovation, performed upon each Platform release, this time includes the following notable updates:

* the major ***PHP 7.0*** version was updated to the *[7.0.13](http://php.net/ChangeLog-7.php#7.0.13)* release, which replaced the preceding *7.0.10* one to fix the number of bugs and security issues
* the most recent ***PHP 7.1*** engine was integrated to Platform as well, providing numerous improvements and major features that can be explored within official [documentation](http://php.net/manual/en/migration71.php)
* [](http://php.net/manual/en/migration71.php)to support out-of-box interconnection between ***Apache Python*** application server and ***PostgreSQL*** database, we've added the dedicated *postgresql-devel* package to the appropriate app server template
{{%tip%}}**Note:** This improvement is compatible since 4.6 PaaS version, so all newly created Python containers at such platforms will include the *postgresql-devel *package. If being needed for the legacy (i.e. the already existing) servers, it still should be installed manually.{{%/tip%}}
* the latest releases of *Fedora 25* and *Ubuntu 17.04* were added to the list of [supported OS](/docker-supported-distributions) for Docker containers

As usual, the full list of the most recent software stack versions, included to the present PaaS release, can be checked within the corresponding [section](#software) below.
<p style="text-align: right;"><a href="#improvements" id="software">Back to the list of Improvements</a>


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.9.5|
|---|---|
|***Tomcat 6***|6.0.48|
|***Tomcat 7***|7.0.73|
|***TomEE***|7.0.2|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_79|
|***Java 8***|1.8.0_112|
|***MariaDB***|5.5.51 / 10.1.16|
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

{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Bug Fixes

In the table below, you can see the list of bug fixes in PaaS 4.9.5:

{{%bug-fixes title="PaaS 4.9.5"%}}
**#**|**Description**
---|---
JE-13842|*JSON parse exception* status appears during file upload in case of receiving an empty response
JE-26579|Directory with a file, which includes double quotes ***"*** symbol in its name, is displayed as empty in the *File Manager* directory tree
JE-28790|Incorrect error message text for building project failure via *Maven*
JE-28807|Legacy *php-mysql* libraries for the MySQL 5.7 server version
JE-28829|Inability to read the previously opened in Configuration Manager file in case its name starts with double underscore "__"
JE-28851|Sometimes, the *Additionally* menu can not be opened for image files
JE-28884|Unhandled error while deploying a broken project to GlassFish 4
JE-28888|Private network routes are missing after migrating environment with external IP attached
JE-28906|Environment containers are accessed over HTTPS even with Built-in SSL being disabled
JE-28952|Access to directory with a file, which includes double quotes ***"*** symbol in its name, is denied within the *File Manager* directory tree
JE-28997|Incorrect description for some processes in the Tasks Panel during Let's Encrypt add-on installation
JE-29075|Incorrect error message while trying to add Docker image based on the unsupported OS template
JE-29077|Rarely, account can be charged for broken or deleted environments
JE-29082|The *Favorites* section within node Configuration Manager tab is not available for collaboration users without the *Change topology/SSH access* permissions being granted
JE-29110|White block appears at the top left corner of the dashboard during its loading
JE-29133|Container migration to another region in *live* mode fails in case the *vzctl* process is active on this moved instance
JE-29222|An error occurs while trying to deploy some specific Java and PHP projects via Deployment manager
JE-29357|The *webroot/ROOT* directory owner in the imported environment differs from the original one in case it was exported without *Private Data*
JE-29466|Incorrect order of public and private IPs in the IP address list after swapping external IPs between two environments
JE-29507|Incorrect output for platform CLI methods, run with the *--silent* property
JE-29511|Empty space appears next to the *Status* tab upon *Task Panel* being reseized
JE-29518|The *Full screen* button is displayed over the Tasks Panel if it superimpose Deployment Manager
JE-29553|Folders within *Favorites* section in Configuration Manager are displayed in lowercase
JE-29583|The *Date* column within *Task Panel* is displayed with artifacts upon zooming it in browser tab
JE-29589|Files with size greater than 1 GB can not be transferred by NFS server
JE-29596|Context redeploy at *Tomcat 8* application server causes container corruption
JE-29599|Inability to use CLI methods, implemented within preceding Platform minor release
JE-29672|Incorrect error message appears while adding Docker volume from the unavailable external server
JE-29695|Unhandled error while trying to delete an environment that was already removed by cluster admin
JE-29705|Some buttons at the dashboard are highlighted with yellow frame upon being clicked
JE-29706|The *Name* column within the *Docker Variables* section is displayed with artifacts upon zooming it in browser tab
{{%/bug-fixes%}}{{%back%}}{{%/back%}}