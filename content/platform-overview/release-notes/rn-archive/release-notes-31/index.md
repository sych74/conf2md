---
draft: false
title: "Release Notes 3.1"
aliases: "/release-notes-31/"
seoindex: "index, follow"
seotitle: "Release Notes 3.1"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included in the PaaS 3.1."
---

<a id="back"></a>

# Virtuozzo Application Platform 3.1

*This document is preliminary and subject to change.*

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS 3.1** release:

* [Features ](#feat)
* [Improvements](#impr)
* [Bug Fixes](#fix)

<a id="feat"></a>
For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Features
[Docker Standard Support](#docker)  
 [Windows Containers Beta Support](#windows)   
[Environment Export and Import](#exp-imp)  
[GIT Authorization by SSH Keys](#git-ssh)   
<a href="#websockets" id="docker">WebSockets Support</a>  
[Support of IDN and gTLD Domain Names](#idn-gtld)  


## Docker Standard Support

The platform is steadily extending the range of integrated technologies, keeping up with and outpacing the newly appeared technical solutions in the field of the hosting industry. The current PaaS 3.1 version proves its &ldquo;Unlimited PaaS&rdquo; appellation once again and brings one more significant feature - Docker standard support.

**Docker** is a special technology for automation of deployment processes and applications' management inside environments. It allows packaging of the necessary app or service with all its dependencies into a container, that can be easily transferred to any Linux-based x86-64 platform with support of cgroups and namespaces isolation by its kernel. Such kind of isolation is required for running a number of independent containers on a single instance, saving resources and providing advanced flexibility for developers. 

The PaaS team has implemented the integration of two leading technologies: Dockers and Parallels Cloud Server, which is used for container-based virtualization. This innovation is intended to give our users the possibility to create containers based on Docker templates for applications with microservices architecture pattern. Both technologies work with the same kernel isolation mechanisms ensuring that all the required processes of Docker standard are covered similarly to the native implementation, saving all the inherent benefits. Such a combination is distinguished by high effectiveness in solving the task of application delivery and simultaneously provides orchestration and management for hosting applications in the cloud.

As a result of this consolidation, the Docker's board was integrated to both the environment topology wizard (as a separate tab) and the platform's Marketplace section at the dashboard (alongside the one-click JPS application's panel). It includes three tabs: 

* *Quick Start* with a set of most popular templates
* *Search on Docker Hub*, which allows finding of the necessary template at the central Docker Registry Hub
* *Custom*, where you can add and manage your own templates from the custom registries

Installing the desired software can be done just in a few clicks - find the required template, choose it to be deployed, select the necessary tag from the list of automatically fetched ones and specify the preferable name of your new environment (or apply the template addition to the existing one). Also, the environment wizard provides you with a special graphic tool for adjusting some basic [configurations](/docker-configuration) at your Docker container, such as environment variables' and ports' settings, linking containers or specifying the file that should be run on its startup. Once the creation of the defined images is confirmed, you'll see your environment contains a new **Docker** server with the chosen template(s) deployed. Each of the templates represents an independent and isolated PCS container with the provided full root access to it via SSH.

More information on interaction with Dockers is presented in the [Dockers Management](/dockers-management) document.

**Note:**

* The availability of the Docker hosting services at a particular platform depends on the chosen hosting provider's settings.
* Currently, the billing history for containers with Docker templates is displayed for the whole environment, but not for the separate nodes in it. This function will become available in the next PaaS release.

[More info](/dockers-overview)

<a href="#feat" id="windows">Back to the list of Features</a>


## Windows Containers Beta Support
Another important milestone in the platform evolution, presented in the 3.1 release, is implementation of the Windows containers' beta support, which provides developers and ISV companies with an ability to host the web services, that are run on Windows operating system, inside the cloud. Within the confines of this prominent feature, the following servers became available at the newly added .NET programming language tab in the environment wizard:


* **Internet Information Services** (**IIS**) **8.0** application server for handling .NET apps, which supports both Microsoft's .NET framework and ASPX scripts. Besides manual package deployment through the dashboard, your project can be published directly from the Microsoft Visual Studio by means of a WebDeploy tool (the detailed instruction will be provided shortly). For more information, read the [IIS 8 Application Server](/iis8) and [.NET Projects Deployment](/deploy-dotnet-archive-url) documents.
* **Microsoft 2012 SQL Server** (Express edition), intended for storing your data and managing SQL databases with the help of Microsoft SQL Server Management Studio. It combines the benefits of broad functionality, feature completeness and inclusion of many useful extra options like analytics, performance monitoring, etc. More information can be found in the corresponding [document](/connection-to-mssql).
* **Windows VPS** server with the pure Windows Server 2012 OS (and 2008 version optionally) installed. [Windows VPS hosting](/win-vps) at the platform provides all the simplicity of a virtual private server, together with the availability of the cloud, and the embedded Server Manager will help you to configure your virtual machine in a way you need through setting the appropriate roles and features. <u>Take into consideration:</u> due to the fact that Windows OS is a proprietary software and can't be distributed freely (i.e. requires the license to be applied to the platform), you can be charged for running such containers (price per hour) according to your hosting provider's tariffs.

Each Windows-based node's virtual desktop can be [accessed](/win-rdp-access) via the **Remote Desktop Protocol**, either with the help of the integrated Guacamole HTML5 client or using your preferred local RDP tool. Every container is fully insulated from the others and runs a separate software copy, thus it can be managed and configured independently. 

**Note** that the availability of the Windows/.NET hosting services at a particular platform depends on the chosen hosting provider's settings.
{{%right%}}<a href="#feat" id="exp-imp">Back to the list of Features</a>{{%/right%}}



## Environment Export and Import
From the very beginning of the platform development, we provided developers with real freedom of choice: no proprietary APIs, no necessity to adjust your applications' code before hosting and a wide variety of stacks and features available. Since one of the preceding versions, we've also implemented the [Environment Transferring](/environment-transferred) feature, allowing you to transfer environments between different accounts within the confines of a single hosting provider's platform.

The current PaaS release includes one more feature, which exempts our customers from any lock-in: **Environment Export/Import**. It provides easy migration of the hosted applications between different platforms. For that, you just need to export your environments and import them to the preferred platform. These operations will take just a few minutes to be completed. During the export, all of the information about the environment (i.e. its topology settings, deployed applications, links to the archives with configurations and private data it contains, etc.) is packed into a single *.json* file. After that, you can simply download and import the received file to the target platform, and shortly you'll receive an identical same-named and ready-to-work environment.

In the case the identical environment copy is not needed for the further work, the required for export data can be chosen beforehand (for example, excluding private data in DBs, custom configurations, etc.). You can create as many exported copies of your environments as you need, wherein all of them will be stored in the disk space, charged according to the chosen hosting provider's tariffs.

Environment export/import is available only for billing and post users by default. The detailed information on this feature can be found in the [Environment Export and Import](/environment-export-import) document.

<a href="/environment-export-import" target="_blank" id="git-ssh">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## GIT Authorization by SSH Keys
The platform provides [multiple ways of application deployment](/deployment-guide): via archive, URL, using version control systems (GIT/SVN) or through the integrated plugins.

From the current release, you are able to gain the additional security while working with your remote GIT project by means of establishing the SSH connection to it, directly from your PaaS account. It also provides the ability to work with those GIT repositories, which are located at the private servers instead of common web-based hosting services for projects like GitHub, Bitbucket etc. 

All you need to do is to generate a pair of SSH keys, put the public key to the system or server the desired repository is placed at and upload the corresponding private key to your platform dashboard. For that we've added a separate **Settings > SSH Keychain > Private** dashboard section, where you can store your private SSH keys.

While adding a remote GIT repository to your environment, you'll see a new ***Use authentication*** checkbox option added to the **Add project** window. After its selection, a custom set of fields for authorization data specification will appear. There, on par with the basic password authentication, you can choose the SSH access type. The secured connection to the required remote repository can be established after entering the appropriate SSH link to your project and selecting the required previously added private SSH key from the corresponding drop-down list.

Summing it up, with this feature you receive the highly protected interaction with one of the most popular version control systems and get an ability to clone and/or update your projects, hosted at the platform, directly from your GIT repositories via SSH.

See the detailed information in the [SSH Access to Git Repository](/git-ssh) document.

<a href="/git-ssh" target="_blank" id="websockets">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## WebSockets Support

WebSockets is a prominent client-server technology, which allows you to establish  a continuous full-duplex TCP socket connection between client and server. Communication over this TCP-based protocol results in a rapid interaction and ensures streaming through proxies and firewalls, both upstream and downstream at once.

The new 3.1 PaaS version provides you with an advanced and improved WebSockets support. This technology has been integrated to the platform [Shared Resolver](/shared-resolver) and [NGINX-balancer node](/http-load-balancing), so for now, you can use it even without external IP address attached to your app server (e.g. [Java](/websockets-java) or [Apache/NGINX](/websockets-apache-nginx)). 

As another way, you can just enable the load-balancer server in front of your application, making it the entry point of the environment and getting rid of any additional configurations (check out the corresponding [instruction](/websockets)). Over and above, this server can be also used for easy overriding the default settings with your custom ones, e.g. changing the listeners port numbers.

In addition, within this feature implementation, we've added a new **proxy_wstunnel_module** [module](/apache-nginx-modules) to the default Apache server build. Integrating this module provides your WebSockets applications, written in PHP, Ruby or Python and hosted within this application server (without the external IP address attached), to be run and accessed via a necessary port. This is achieved by means of proxying the variety of ports, used by your WebSockets apps, to a single one, used by Shared Resolver (*80 *for HTTP and *443* for HTTPS). 

<a href="/websockets" target="_blank" id="idn-gtld">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## Support of IDN and gTLD Domain Names
In the current platform release we've implemented one more requested and important feature - Internationalized Domain Name (IDN) and Generic Top-Level Domain (gTLD) support.

* **IDN**s are domain names, represented with Unicode characters (which amount is considerably bigger than the traditionally used ASCII ones) by means of implicit conversion to the standard view with the help of [Punycode](https://en.wikipedia.org/wiki/Punycode). This allows the platform users from all over the world to use their native language (i.e. a variety of symbols besides the previously available Latin characters, e.g. Cyrillic letters or Chinese hieroglyphs) while setting the environment names and [aliases](/environment-aliases). Such names will be correctly displayed throughout the dashboard and while accessing an account via the [SSH console](/ssh-access). In addition, for now you can easily bind the external IDN to your environment, following the same [workflow](/custom-domains) as for the usual custom domain names.
* **gTLDs** are top-level domains maintained by the Internet Assigned Numbers Authority (IANA) and originally intended for being used by particular types of organizations and companies. Their integration to the platform provides you with the possibility to [bind](/custom-domains) such domain names (ended with the suffix like *.org*, *.academy*, *.best*, etc.) to your environments.

More details with the appropriate use cases can be found in our [documentation](/tld-idn-domain).

<a href="/tld-idn-domain" target="_blank" id="impr">More info</a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## Improvements
<a href="#vps">Elastic VPS without Public IP</a>  
[FTP Enhancements](#ftp)[GlassFish 4 & WildFly 8 Advanced Usability](#cartridge-usability)  
[GIT Auto-Resolve Conflict Option](#git-option)[Blocked HTTP Usage for API](#api)  
[Timezone Updates](#timezone)  
[Inner System Amendments](#inner)  
[Documentation Redesign](#docs)  
<a href="#ux" id="vps">UX Improvements</a>  
[Software Stack Versions](#software)  


## Elastic VPS without Public IP
[Elastic Virtual Private Server](/vps) represents a special bare virtual machine, intended to meet any developers' needs regarding their applications' hosting, as it can be configured for running any desired server software and has the privacy of a separate physical computer. VPS hosting in the platform is made possible by means of using a highly qualitative CentOS server with the Public IP address attached, for this server to be operated as a fully isolated and secured container with a single entry point.
Nevertheless, within the current (3.1) platform version we've added the possibility for hosting providers to optionally allow the creation of a Virtual Private Server without the obligatory external IP enabled for particular users. This can be caused, for example, by the necessity to establish a special infrastructure, which is partially closed for accessing from outside of your environment.

**Note** that this improvement is not available by default due to security reasons, thus, if it is highly required for your app's hosting, you need to contact your hosting provider's support and request the enabling of this function. 

After that, if your request is granted, you'll be allowed to detach the Public IP address for your VPS server while creating an environment or while changing the topology settings for an existing one. Access to such a server should be performed [via the SSH Gateway](/vps-ssh-gate/), wherein you still receive the root administration permissions for its managing.
{{%right%}}<a href="#impr" id="ftp">Back to the list of Improvements</a>{{%/right%}}



## FTP Enhancements
Supporting a variety of different technologies, the platform also provides an ability to work with your deployed application's files via [FTP](/ftp-ftps-support), which is represented in the form of a pluggable module. Here are a few changes that have been implemented to this module within the PaaS 3.1 release:

* While working with your application via FTP, you are also able to ensure the security of the transmitted content and access credentials with the help of SSL (i.e. use the FTPS protocol). For this, the SSL certificates are required, which are automatically generated inside the container during the FTP-addon installation. Starting with the current platform version, the expiration term of these certificates has been changed and for now, they will remain active for 5 years in all the newly created containers with this addon installed.
* The range of available open ports for FTP's passive mode has been limited to *50000-50099* in order to increase the platform's security.

<a id="cartridge-usability"></a>{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## GlassFish 4 & WildFly 8 Advanced Usability
Since one of the preceding versions, the platform provides [cartridges packaging format](/cartridges-overview) support, allowing hosting providers to enlarge the amount of software stacks, available within a managed platform, with additional ones. For that, we offer a set of already [prepared cartridges](/supported-cartridges), that are continuously enhanced and can be added to the platform by a hoster.

Recently, the usability of the [GlassFish 4](/glassfish4) and [WildFly 8](/wildfly) cartridges has been improved through adding special redirect rules to the platform [Shared Resolver](/shared-resolver) infrastructure component. As a result, for now you are not obliged to attach the external IP address to a particular node for accessing its admin console. Just select the **Open in browser** button next to the required instance and choose the *Administration Console* link (for WildFly) or the go to the *Administration Console* string (if using GF). After that, you'll be automatically redirected to the ***https://{env_host}:4949/console*** or ***https://{env_host}:4848*** address respectively, where you simply need to specify your admin credentials, previously received via email, and start working.

Beside that, a new default environment variable variable, named ***$HOME***, has been added to both cartridges' settings. Its value contains a full path to a new user-dedicated folder with the same **home** name, which can be accessed through the dashboard's Configuration Manager. This directory is intended for being used as storage for your custom properties files, as all the configurations they contain are automatically read by the system.

**<a id="git-option"></a>Note** that the availability of these cartridges and the abovementioned new functionality depends on your hosting provider's settings.
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## GIT Auto-Resolve Conflict Option
While deploying your application, located at the remote GIT repository, into the platform, you can note that one more option (besides the [Authentication](#git-ssh) one) has been added to the ***Add project*** dialog frame - **Auto resolve conflict**. Though enabled by default, its state can be switched with the help of the corresponding check-box.

This option represents an analogue of the *git reset --hard* command. It is used to prevent the occurrence of merge conflicts during further project updates, which can take place if the same file has been modified in both the remote repository and your project, hosted at the platform. If such an issue arises, this contradictory file will be updated according to its repository version (which is considered as the correct one), discarding the locally made changes. 

**Note:** Do not disable this option if you don't know exactly what you are doing. 
<a id="api"></a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Blocked HTTP Usage for API
[Cloud API](https://www.virtuozzo.com/application-platform-api-docs/) is an integral part of the platform, aimed for allowing developers to automate the different actions that take place during the application lifecycle, and get even more platform possibilities by integrating with other services.

From the release of the platform 3.1, using an API can be performed through the secured HTTPS protocol only. Please, adjust your scripts according to this amendment, otherwise they won't be applied to the platform, due to the forbidden connection.

<a href="https://docs.jelastic.com/api/" target="_blank" id="timezone">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Timezone Updates
All Java and PHP application servers, available within the platform, include special timezone packages, which are responsible for providing the information about the history of local time in many representative locations around the globe and the current timezone rules for software, running inside a container. These packages have been updated in the abovementioned servers' builds within 3.1 PaaS release, so all the newly created containers will contain the most recent timezone data. In addition, let's consider some specifics of this update for particular programming languages:


* **for Java**
Timezone information inside Java compute nodes is provided within the **TZdata** package, which has been updated to its most recent *2014j* version. Also, we've integrated a new **TZUpdater** tool to these servers, which is intended for keeping the timezone data inside a container up-to-date according to its periodical changing. This gives you an ability to update the timezone rules for the legacy containers by means of establishing the [SSH connection](/ssh-access) to the required one and executing the ***java -jar /usr/java/utils/tzupdater.jar -u*** line inside it. In order to check the current TZdata package version for the desired server, run the ***java -jar /usr/java/utils/tzupdater.jar -V*** command in just the same way.
* **for PHP**
Besides updating of the corresponding timezone rules, for now each PHP application server includes a new editable *date.timezone* parameter inside the ***php.ini*** file. By default, its value is set to the UTC zone usage, but it can be easily substituted with any other time zone from the [list](ttp://php.net/manual/en/timezones.php) of the supported ones. 

**Note** that for applying these changes, your server should be restarted. 
<a id="inner"></a>{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Inner System Amendments

* <a href="#inner-db-import" id="inner-db-import">Increased DB Size Limit for Import</a>
* [Optimized SSH-Gate CPU usage](#inner-gateway)


* ### Increased DB Size Limit for Import
One of the most commonly used solutions for passive increasing the application's information security is regularly making backups of the data, stored within its database(s). Subsequently, such saved DB dumps can be easily imported to the necessary server in the case of an unexpected database failure (the platform documentation provides a set of instructions on how this can be done for a particular database: [MySQL](/dump-import-export-to-mysql), [MariaDB](/dump-import-export-mariadb), [PostgreSQL](/dump-postgres) and [MongoDB](/dump-import-export-to-mongodb)).  
Herewith, if a particular storage contains a large amount of data, you could experience some problems while trying to recover it through the phpMyAdmin panel of the target MariaDB or MySQL server, due to the existing limits on the uploaded file's size. Thus, in order to remove such an inconvenience, the maximum allowed size of the file, uploaded through the [Shared Resolver](/shared-resolver) infrastructure element (i.e. for DB nodes without the IP address attached) has been increased to 512 MB (though it can differ according to a particular hosting provider's settings).  
In addition, the default values of both ***max_execution_time*** and ***max_input_time*** settings for MySQL/MariaDB containers have been changed from *600* to *1200* seconds and the ***default_socket_timeout*** value was increased from *60* to *600* seconds (however, they are available for adjusting through the **etc > php.ini** file of your DB server). In such a way, the process of uploading won't be interrupted due to the reason the response time is over.
<a id="inner-gateway"></a>{{%right%}}[Back to the list of Inner System Amendments](#inner){{%/right%}}


* ### Optimized SSH-Gate CPU usage
While using [SSH Gateway](/ssh-overview), some of our users could rarely experience a low connection performance and even a connection failure, due to the exceeded timeout. This is caused by the high CPU load during the time some another user is transferring a big amount of data through the gateway.  
Therefore, our developers have optimized the CPU usage for increasing the gateway's bandwidth. We've also improved the mechanism of outdated SSH sessions closing after the data has been transferred, in order to release the untenanted resources. Both of these amendments will make the process of working with your projects via SSH more rapid and productive.
<a id="docs"></a>{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Documentation Redesign
Due to a steady progress in the platform's development, the amount of documents with numerous features and possibilities described is continuously enlarged, as well as the amount of tutorials and different how-to guides. This resulted in a decrease of our documentation's usability, as it appears to be quite difficult to find the desired document amongst all of the provided useful information. 

In such a situation, the obvious decision was to do a complete restructuring of our docs. Moreover, to make it even more clear, perceptive and usable, the [main documentation page](https://www.virtuozzo.com/application-platform-docs) has been completely redesigned. For now, it represents the Developer's Center, where you can find the separate blocks with the key instructions listed and divided into the appropriate sections. If you are looking for a particular document, you can use either the common for all browsers *Find on page* option (wherein the matched text on a page will be highlighted) or the search box above the blocks (herewith you'll be redirected to a new tab with the search results).  

And one more amendment - when navigating to the necessary document, you will notice that the left-hand categories menu does not include the whole documentation list, but just the block-related sections. Instead of that, a new Developer's Center button has appeared above this menu, which leads back to the main docs page with the complete list of available sections. In such a way, displaying only the related documents helps users to keep focus on the necessary information.

We hope that you will like our new combination of fresh-looking design with easy and clear navigation - visit [www.virtuozzo.com/application-platform-docs](https://www.virtuozzo.com/application-platform-docs) to try it out.
<a id="ux"></a>{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## UX Improvements

* [Live Refresh for Log Files](#ux-logs)  
* [Configuration Files Availability via SSH](#ux-ssh)  
* <a href="#ux-marketplace" id="ux-logs">Database Clusters within Marketplace</a>  
* [UI Amendments](#ux-interface)  

* ### Live Refresh for Log Files
Log files are the main source of the most important information regarding what has happened to your environment. They can be reached by means of selecting the appropriate same-named button next to the required node or set of nodes, wherein each node type has a particular set of log files available.  
In order to make the logs monitoring even more convenient, we've added the **Auto refresh** option for it, which is enabled by default. This ensures that the currently opened log files are refreshed every 3 seconds and in such a way, removes any delay or necessity to refresh them manually in order to get the up-to-date information.   
It can be especially useful while running some development or testing procedures, as with this amending improvement, you'll never miss the newly appeared error or any other crucial process that occurred inside your environment.  
For disabling or enabling the Auto Refresh, tick the appropriate line in the ***Refresh*** drop-down list above the log output window.
<a href="/view-log-files/" target="_blank" id="timezone">More info</a><a id="ux-ssh"></a>
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}


* ### Configuration Files Availability via SSH
One of they ways to securely manage the servers inside your environment is to perform the desired operations through the [SSH protocol](/ssh-overview). Nevertheless, previously the possibilities of such an interaction were partially limited due to an unavailability to edit the configuration files commonly accessed via the dashboard, from inside a container. This was caused by the fact these files are owned by the ***root*** system user, while all the operations inside the container are performed on behalf of the default ***jelastic*** user, which is used for establishing the SSH connection to any node from the users side.  
Thus, striving to increase the usability of working with your servers via the console, we've extended the permissions for the default ***jelastic*** user by adding it to a special **ssh-access** users' group, members of which are granted the full read/write access to the abovementioned configuration files. Such changes make the process of your environment settings' customization through SSH much more powerful, but take notice of the actions you perform, as some unintentional misconfiguration can cause a whole environment failure.<a id="ux-marketplace"></a> So remember that more power, brings more responsibility.
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}


* ### Database Clusters within Marketplace
Setting a database cluster is the commonly used solution for increasing DB performance, ensuring failover protection and heightening data security. Besides the step-by-step instructions on manual clusters' configuring (that are available in our documentation inside the *Databases* section), the platform also provides you with the one-click cluster installation options for setting a master-slave replication between a pair of the most popular supported DB servers: MySQL, MariaDB, PostgreSQL and MongoDB. This is achieved by means of preparing the preconfigured cluster templates and packaging them with the help of [JPS](/jps).

Striving to facilitate accessing these packages and making it easier for users to find them, we've added a separate **Clustered DBs** section to our Marketplace [site page](https://www.virtuozzo.com/application-platform/marketplace/?filter=clusters) and the same-named [dashboard section](/marketplace). In order to get the ready-to-use database cluster inside the cloud within a few minutes, just hover over the desired solution, click on the appeared **Install** button and either enter your email address into the corresponding field (if working with the site) or specify the name for a new environment (if choosing via the dashboard). The platform will take care of everything else - from the automatic environment creation with the appropriate set of nodes to the deployment of a cluster itself inside.<a id="ux-interface"></a> All you need to do is to check the admin credentials you've received via email and start using all the benefits the data replication provides. 
{{%right%}}[Back to the list of UX Improvements](#ux){{%/right%}}


* ### UI Amendments
Here are a few interface enhancements that our developers have implemented to the platform dashboard within the 3.1 release in order to make its usage more practical:

* For now the **Open in browser** button is available for each application server node in the [set of the same-type](/multi-nodes) ones (but not as it was previously for only the parent node). This gives you an ability to to open the desired server's main page or admin panel directly through the dashboard, which can be especially useful in the case of different servers' configuration.
* In order to emphasize an importance of the **SSL option** using and its mission to protect your environment with the deployed application inside, the corresponding section in the *Environment Topology* wizard has been moved to the top part of this frame. Herewith, for now, it is indicated with an open lock icon, which becomes closed upon [enabling the SSL feature](/secure-sockets-layer). Simultaneously, its activation will highlight the topology border with a green-colored rim in order to ideate the enabled fortification of your environment from the external interception.<br class="kix-line-break">
<a id="software"></a>{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Software Stack Versions
The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 3.1|
|---|---|
|***Tomcat 6***|6.0.43|
|***Tomcat 7***|7.0.57|
|***TomEE***|1.7.1|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45 |
|***Java 7***|1.7.0_71|
|***Java 8***|1.8.0_25|
|***MariaDB***|5.5.41 /10.0.15|
|***MongoDB***|2.6.6|
|***MySQL***|5.7.5|
|***PostgreSQL 8***|8.4.22|
|***PostgreSQL 9***|9.4|
|***CouchDB***|1.6.1|
|***nginx***|1.6.2|
|***Maven***|3.2.5|
|***Centos 6***|6.6|
|***Memcached***|1.4.22|
|***Apache***|2.2.15-39|
|***NGINX PHP***|1.6.2|
|***NGINX Ruby***|1.6.2|
|***PHP 5.3***|5.3.29|
|***PHP 5.4***|5.4.36|
|***PHP 5.5***|5.5.20|
|***PHP 5.6***|5.6.4|
|***Ruby 1.9.3***|1.9.3-p551|
|***Ruby 2.0.0***|2.0.0-p498|
|***Ruby 2.1***|2.1.5|
|***Ruby 2.2***|2.2.0|
|***Python 2.7***|2.7.6|
|***Python 3.3***|3.3.5|
|***Python 3.4***|3.4.0|
|***Node.js***|0.10|
{{%right%}}<a href="#impr" id="fix">Back to the list of Improvements</a>{{%/right%}}



## Bug Fixes
In the tables below, you can see the list of bug fixes in PaaS 3.1 and 3.1.1/2:

{{%bug-fixes title="PaaS 3.1"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-17696|Password to the remote repository can't be changed for the already built Maven project
JE-18023|Python applications can be deployed to the custom context via API request
JE-18026|Unable to read the GeoLiteCountry.dat file for Apache-PHP through the configuration manager
JE-18187|Automatic deployment for Maven projects does not work
JE-18210|502 Bad Gateway error while trying to open an environment with both HA Nginx LB and Built-in SSL enabled
JE-18287|Environments are duplicated during the app's installation through Marketplace
JE-18295|While creating several environments via Marketplace, the pop-up installation frame become frozen
JE-18333|The &ldquo;Server could not be contacted&rdquo; warning appears in 10 minutes after a file has been uploaded to the Deployment Manager
JE-18540|Mismatches in API documentation &gt; Methods description
JE-18634|Ruby project's addition from the remote repository fails due to the &ldquo;Timeout while waiting for data&rdquo; error
JE-18740|Public SSH key can't be used for connection if it contains a comment with spaces
JE-18752|The &ldquo;413 Request Entity Too Large&rdquo; error appears while importing MySQL dump file larger than 100 MB
JE-18828|If balance is refilled, the new cash amount is not displayed until the page is refreshed
JE-19245|JPS package name mismatch in the &ldquo;successful installation&rdquo; frame for Cyclos4 Pro
JE-19520|Changed settings in the standalone.xml file for WildFly are restored to default values after the server is restarted
JE-20114|Auto Horizontal Scaling: incorrect logic for nodes' addition/removal
{{%/table%}}
{{%/bug-fixes%}}

<br class="Apple-interchange-newline">

{{%bug-fixes title="PaaS 3.1.1/2"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-20252|Sometimes page content is blocked by a browser while accessing a Windows RD through Guacamole
JE-20256|Actions, required for the environment import operation, are blocked by some browsers
JE-20282|An error occurs while trying to import the environment with cyrillic characters in its name
JE-20339|Environments with VPS and/or Maven build node are not exported properly
JE-20357|Debian 8 Docker<sup>&reg;</sup> templates can't be deployed
JE-20360|An error occurs while trying to install the Docker<sup>&reg;</sup> image, located at the custom registry of the private Central Hub account
JE-20371|Success installation text is missed for the JPS packages with no ID specified in the manifest
JE-20375|Unable to upload a package with cyrillic characters in its name to the dashboard
JE-20494|The &ldquo;Exported files are not available&rdquo; error occurs while trying to import an environment with Memcached
JE-20501|External billing system exception while trying to upgrade an account with special symbols in its email
JE-20715|Improper default security settings for MongoDB instances: authentication is disabled
JE-20725|DNS address is not present by default in the internet options of Windows nodes
JE-20969|Unable to deploy an application using direct URL to the JSON manifest (3.1.2)
JE-20970|The authentication at the custom Docker<sup>&reg;</sup> repository fails if its link contains &ldquo;/&rdquo; at the end (3.1.2)
{{%/table%}}
{{%/bug-fixes%}}
{{%right%}}[Back to top](#back){{%/right%}}
