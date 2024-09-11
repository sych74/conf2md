---
draft: false
title: "Release Notes 2.2"
aliases: "/release-notes-22/"
seoindex: "index, follow"
seotitle: "Release Notes 2.2"
seokeywords: "paas, paas release notes, paas version, 2.2 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the PaaS 2.2 release."
---

# Virtuozzo Application Platform 2.2
*<div id="top">This document is preliminary and subject to change.</div>*

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS 2.2** release:

* [Features ](#feat)  
* [Improvements](#impr)  
* [Bug Fixes](#fix)  

<a id="feat"></a>For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs).


## Features

* [SSH Access](#a)  
* [Platform API](#b)  
* [Cartridges Support](#c)  
* [Ruby Hosting](#d)  
* <a href="#e" id="a">Accounts Collaboration</a>  

## A. SSH Access
**SSH** **(Secure Shell Handler)** is a protocol used to connect securely to a remote container and execute the required commands. SSH commands are encrypted and secure: client/server connection is authenticated using a digital certificate, and passwords are protected by being encrypted.

To make SSH access available in the platform, a new infrastructure component was added to the core - **SSH Gateway**. SSH Gateway contains a unique application that accepts users' connections from the internet and then transmits these connections to the desired container, using an internal network.

The authentication procedure in SSH Gateway is divided into two independent parts: 

* connection from end user to Gateway (external authentication) 
* connection from Gateway to users' container (internal authentication)

Both parts of the authentication procedure are based on a standard SSH protocol, using public/private keypairs.
With SSH Gateway, you can easily access:

* **the whole account** where you can navigate across your environments and containers using an interactive menu without extra authentication
* **separate containers directly** while working with them remotely via additional tools (e.g. Capistrano) or using SFTP and FISH protocols

While accessing containers via SSH, you receive all required permissions and additionally can manage the main services with **sudo** commands.
In addition, we provide support of **SFTP **(Secure File Transfer Protocol) by implementing the threaded daemon for SFTP connections processing. It lets you access, manage and transfer files directly to the container via SSH gateway, and in such a way, ensures data security.

One more available secure network protocol is **FISH **(Files transferred over Shell protocol). It is supported by a number of popular FTP-clients and file managers (e.g. Midnight Commander, Konqueror, lftp, Krusader, etc.) and permits access and securely manage a container's file system using RSH commands.<a id="b"></a>

Navigate to the [SSH documentation](/ssh-overview) to read the instructions on SSH key adding and container accessing.
[More info](/ssh-overview)
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## B. Platform API
**Platform API** lets developers automate a set of actions required for an application's lifecycle and extend our platform functionality, by combining other services. Using our API, you can programmatically create environments, deploy apps and perform other tasks that could be earlier accomplished only via the platform's dashboard, but not limited to them.   
[Platform API](https://www.virtuozzo.com/application-platform-api-docs/) follows REST principles. REST API determines a set of functions which can be requested by a developer, who then receives a response. The interaction is performed via [HTTP protocol](http://tools.ietf.org/html/rfc2616). The advantage of such a method, is a wide extension of the HTTP protocol. That's why REST API can be used with almost any programming language.  
All requests of API methods are GET or POST HTTP-requests to the URL, with a set of parameters:

***http://<a href="/paas-hosting-providers/" target="_blank">[hoster-api-host]</a>/1.0/***

The type of URL that should be used, is stated in the description of each method.  

Every request should contain a set of the mandatory parameters. There are some additional parameters required for a particular function. Such parameters are stated in the documentation about this function.  

The text value of the parameters should be provided in UTF-8 code. The sequence of the parameters in the request is not important.

<a id="c"></a>The response for all API functions is given in [JSON](http://en.wikipedia.org/wiki/JSON) format. An example of the result is described in the documentation of the method.  

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right%}}[Back to the list of Features](#feat){{%/right%}}





## C. Cartridges Support
The platform supports OpenShift's cartridge model with its [PaaS](https://jelastic.com/solutions/) offering, making it easier for independent software vendors (ISVs) to offer core services in multiple platforms and for a wider array of cloud ecosystems and marketplaces.

Cartridge standardization is an essential element for next-generation cloud infrastructures and enables ISVs to focus on providing real value to customers, instead of spending resources coding for multiple platforms. This results in a broader choice of tools and applications.

Cartridge is an advanced packaging format. It is represented with existing OpenShift cartridges' specifications and extended with the platform configurations, to provide more complex functionality. This enables integrating extra middleware, databases, and services into the platform and making them available to PaaS developers building applications. This open standard for technology packaging and deployment, reduces the need for companies to repackage their technology for different cloud platforms, making it easier and faster to offer their solutions to PaaS users and developers.

There is a set of already prepared cartridges that can be added to the platform from the [Templates repository](https://github.com/jelastic-public-cartridges?tab=repositories) by hoster. For now the following cartridges are available:

* Python WSGI 2.7, 3.3, 3.4 
* Redis 2.6
* Neo4j 1.9
* Cassandra 1.2.5
* Jetty 9.1.3
* Jetty 8.14
* JBoss 7.0

Also hoster can package and configure own cartridges, upload them to the repository and make available for you. In such a way, the number of available application servers, databases, etc, can be greatly increased.

Also the tabs with new programming languages are added to the environment topology wizard. The list of supported languages is extended with Python, Node.js and Mono. These tabs are inactive and presented as a marketing point for advertizing future support of new engines.

<a id="d"></a>Python engine is already available. We provide three Python versions (2.7, 3.3 and 3.4) and one application server (Apache + mod_wsgi bundle) by default. Note that Python applications hosting will be available for you only after hoster enabled it.


{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## D. Ruby Hosting

Within the PaaS 2.2 release we announce a support of Ruby applications hosting. The reason behind the platform and Ruby hosting cooperation is that we have a very similar philosophy - "simple in appearance, but complex inside". Developers call Ruby a beautiful, artful language. And yet, it's handy and practical. The same applies with the platform's intuitive dashboard panel and a wide range of complex features.  
Enjoy the benefits of the balance between simplicity and power with the platform and Ruby on Rails. Ruby application servers are available at the Ruby tab, which was added to the environment topology wizard alongside Java and PHP. For now, the following application servers are available:

* **Apache2 + Passenger**
A custom dynamic *mod_passenger.so* module for Apache was developed. It is included in the **modules** folder while Ruby environment creation and is enabled by default.

* **NGINX + Passenger**
NGINX server version was updated and it was recompiled with in-built Passenger module. 

* **Nginx + Puma**
* **Nginx + Unicorn**

Below are the main Ruby features supported by the platform:

* four Ruby versions: 1.9.2-p320, 1.9.3-p545, 2.0.0-p451, 2.1.1
You can choose the one you need while creating the environment and easily switch between them afterwards. For detailed instruction, see the [Ruby Versions](/ruby-versions) document.

* roject deployment via archive/URL  The guide on Ruby application deployment can be found in the [Upload and Deploy Your Ruby Application](/deploy-ruby-archive-url) document.

* application deployment directly from GIT/SVN
To see how to do this, read the [Ruby deployment via GIT/SVN](/ruby-git-svn) document.

* three types of deployment: *Production*, *Development *and *Testing*
<a id="e"></a>You can choose the necessary one while creating the environment.

[More info](/dashboard-guide/)
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## E. Account Collaboration
Based on numerous requests from our customers, in PaaS 2.2 release we present a new outstanding feature - account collaboration. The main idea is to let big organizations create one primary account, where all necessary environments are running, and to share certain or all activities with other accounts (e.g. members of development team). 

All accounts of an organization are interconnected in such a way, to enable *collaboration*. Any user (regardless if they are registered at the platform) can join (i.e. should be invited by a primary user) or leave an organization's collaboration.

Within this concept we define two types of accounts:

* primary
* user
The **primary** one is the organization's main billing account. A primary user can manage the list of other collaboration users, their permissions within collaboration, the list of shared environments, etc. All of the charges for using environments shared in collaboration are applied to this primary account.

A collaboration **user** can work with the shared environments of the primary billing account as with his own. In other words, a user can deploy applications, change configurations, read log files, view statistics, etc. The exception, is that a user cannot clone or delete this shared environment. 

A user's ability to change an environment's topology and access it via SSH, is regulated by the primary account owner, when the particular environment is shared.

A user can also be allowed to create new environments on the primary collaboration account. In this case, there will not be any restrictions for a trial user while setting up the environment (e.g., number of cloudlets available). All of the charges for such environment usage will be applied to the primary account. 

<a id="impr"></a>Note: that after leaving the collaboration, the user will no longer have access to this environment.

[More info](/account-collaboration)
{{%right%}}[Back to the list of Features](#feat){{%/right%}}


## Improvements

* [JDK8 Support](#k)
* [NAXSI Module Support in NGINX](#l)
* [Marketplace](#m)
* [PHP Security Improvements](#n)
* [PHP PEAR Support](#o)
* [Increased Timeout During Deploy](#p)
* <a href="#q">Upgrade Window Improvements</a>
* [Widgets Redesign](#r)
* [Hash Signs in the Context Names](#hash)
* <a href="#ssv" id="k">Software Stack Versions</a>


## A. JDK8 Support
Java is an object-oriented and class-based programming language with a great number of developers collaborating on it, across the world. In PaaS version 2.2, we added support of the new Java 8 version, released on March 18, 2014. Java 8 includes features for productivity, ease of use, improved polyglot programming, security and improved performance.

Choosing this new version is available in the environment topology wizard within the Java versions drop-down list, alongside Java 6 and Java 7. <a id="l"></a>As for the previous versions, Java 8 can be applied to all Java application servers, available at the platform: Tomcat, TomEE, GlassFish and Jetty. 

[More info](/java-6-and-7)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## B. NAXSI Module Support in NGINX
**NAXSI** is an open-source, high performance and low rules maintenance web-application firewall for NGINX. NAXSI abbreviation means Nginx Anti Xss & Sql Injection. This module is used to protect web applications from attacks like SQL Injections, Cross Site Scripting, Cross Site Request Forgery, Local & Remote file inclusions.

Within the PaaS 2.2 release, NAXSI module was integrated to both NGINX balancer and NGINX-PHP nodes. <a id="m"></a>For now, you can use its various features by means of specifying the necessary functions in the NGINX configuration files and in such a way, improve your application's security.

{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## C. Marketplace
Within the 2.2 release, we present a new **Marketplace** feature - a distinguishing solution for packaging and providing already prepared applications with the help of the platform [Packaging Standard](/jps). Such apps can be deployed and installed in just a few clicks, including automatic creation of the appropriate environment, with all required nodes and configurations. 
Currently, the list of the available applications can be accessed by clicking the **Marketplace** button, which is located in the top toolbar next to the *Create environment* button.

<a id="n"></a>The platform provides a set of already preconfigured application packages and also provides hosters with an opportunity to add and publish their own ones.

[More info](/marketplace)
<a id="si"></a>{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## D. PHP Security Improvements
To make PaaS hosting even more secure for your applications, we've made some changes in the default configurations of [PHP](/php-security-settings) and [Apache application server](/apache-security-configurations). Applied modifications are listed below.

For Apache's **httpd.conf** configuration file:  

* *TraceEnable Off* line added. It disables the echo-reply of the server in response to a user's request, as this reply can be received by someone else, except the user.
* *ServerTokens* parameter's value was changed to *Prod*. It means that we forbid the server to send the information about OS version and enabled modules in response to requests.
* *ServerSignature* parameter's value was changed to *Off*. This removes the inscription containing the server version on the server's error pages.

For **php.ini** file of both Apache and NGINX-PHP:

* *<a id="o"></a>expose_php* value was changed to *Off*. Such a value hides the extended information about the PHP version used in HTTP response.  

[More info](/apache-security-configurations)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## E. PHP PEAR Support
As PaaS version 2.2 provides the ability to access the necessary container via SSH, it became necessary to add a support of **PHP PEAR** (PHP Extension and Application Repository) utility. It's a kind of PHP software code repository, which contains a number of PHP extensions available. You can [choose the one](http://pear.php.net/packages.php) you need and easily install it to your PHP container.

To perform the installation, you need to get the [SSH access](/ssh-access) to your environment and navigate inside the desired PHP container (Apache-PHP or NGINX-PHP application server). After that, you should run the following command in the SSH console:

***pear install \<package>***

where ***package*** is a name of the desired PHP package, chosen from the repository.

Package will be downloaded and installed to the container. <a id="p"></a>You are also able to upgrade the installed package or delete it, in the case it is no longer needed.

To find more information about available PEAR commands, read the [Manual](http://pear.php.net/manual/en/guide.users.commandline.installing.php).

{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## F. Increased Timeout During Deploy
Deploying large applications, especially written in the Ruby programming language, can take a rather long time. <a id="q"></a>In order to avoid deploy failure due to timeout, we increased the period of time the system waits for deployment completion to 90 minutes.

Note that hoster can change the default value if it is required.
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## G.Upgrade Window Improvements
While upgrading an account, you have to fill in a special **Upgrade** form with a range of required data. The usability of this form has been improved by means of adding the scroll option, thus it became more convenient to fill in the fields, especially in the case form includes some additional ones. 

<a id="r"></a>Also Australian users got an ability to choose their state or major mainland territory while providing the info for upgrade - after selecting Australia in the Country drop-down list one more State field appears.

{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## H. Widgets Redesign
We continue to implement our new corporate style to the numerous elements that represent PaaS. In this release, we've improved the design of our one-click installation widget.  
For now, while preparing the installation widget, you can customize all of its elements, e.g. choose widget's color from the set of predefined ones or change the labels text.  
The detailed instruction on creating and setting up your own widget can be found in [ Installation Widget](/application-manifest/) document.

[More info](/application-manifest/)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## I. Hash Signs in the Context Names
In PaaS version 2.2, we've added support of hash signs in the context names for Java applications. Before deploying the application, entered by user context passes through validation. It consists of custom rules for each type of server. The following table shows the list of changed application servers' rules which now allow the mentioned signs in context text: 

Application Server|Signs Allowed
---|---
Tomcat 6, TomEE|#
Tomcat 7|#, ##

This improvement allows users to enjoy all of the benefits of the parallel deployment feature, available for Tomcat 7 server. <a id="ssv"></a>It means a user can deploy and run a few application versions with the same context path. Versions can be added or removed without the server restarting and, therefore, avoiding application downtime. More info on using parallel deployment can be found [here](http://tomcat.apache.org/tomcat-7.0-doc/config/context.html#Parallel_deployment). 
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}

## J. Software Stack Versions

The component templates are updated to the latest versions in the 2.2 PaaS release:

{{%table weight="100 450"%}}
|Stack|PaaS 2.5|
|---|---|
|***Tomcat 6***|6.0.39|
|***Tomcat 7***|7.0.53|
|***TomEE***|1.6.0|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_51|
|***Java 8***|1.8.0_132|
|***MariaDB***|5.5.36/10.0.10|
|***MongoDB***|2.6.0|
|***MySQL***|5.6.17|
|***PostgreSQL 8***|8.4.21|
|***PostgreSQL 9***|9.3.4|
|***CouchDB***|1.5.0|
|***NGINX***|1.5.12|
|***Maven***|3.2.1|
|***Centos 6***|6.4|
|***Memcached***|1.4.15|
|***Apache***|2.2.15-29|
|***NGINX PHP***|1.5.12|
|***NGINX Ruby***|1.5.12|
|***PHP 5.3***|5.3.28|
|***PHP 5.4<a id="fix"></a>***|5.4.26|
|***PHP 5.5***|5.5.10|
|***Ruby 1.9.2***|1.9.2-p320|
|***Ruby 1.9.3***|1.9.3-p545|
|***Ruby 2.0.0***|2.0.0-p451|
|***Ruby 2.1.1***|2.1.1|
|***Python 2.7***|2.7.6|
|***Python 3.3***|3.3.5|
|***Python 3.4***|3.4.0|
{{%/table%}}
[Back to the list of Improvements](#impr)


## Bug Fixes

In the tables below, you can see the list of bug fixes in PaaS 2.2:

{{%table weight="100 450"%}}
|**#**|**Description**|
---|---
JE-10641|Auto-refill is displayed as enabled even when the associated payment method is no longer available
JE-11295 |Ruby: error after changing application context
JE-12256|Error while upgrading account due to the invalid checksum
JE-12296|Ruby: "Gemfile not found&rdquo; error after deployment was interrupted by context renaming
JE-12452|Error while uploading application package via FTP link
JE-13585|Free diskspace validation during deploy to Apache causes java.io.IOException: Timeout while waiting for data
JE-13719|Shared environments are counted in environments limit of shared with user
JE-13809|Error while trying to upload/rename file with &lsquo; character in its name
JE-13858|'result: 99; file already exists' error while trying to rename the same file identically in two different configuration manager tabs 
JE-13879|NGINX jem procedures for old containers are too long and cause IOExceptions
JE-13897|Incorrect chars instead of cyrillic letters in names of uploaded to Configuration manager files
JE-14044|Wrong error code for 'No free disk space' error during deploy
JE-14059|Incorrect error message while swapping domains between existing and deleted environments
JE-14189|Incorrect displaying of time in action log after Jetty restarting
JE-14305|Ruby: Context with deployed app can't be deleted
JE-14308|Error while trying to create file or directory in the webroot folder of Ruby-apache2 server
JE-14329|Ruby: Ruby on rails separate process is handled by Ruby engine instead of Passanger
JE-14330|Ruby: awsc3 gem is not working
JE-14331|Ruby engine is compiled without static massive project
JE-14332|Ruby is not working with SVN gem's
JE-14341|Ruby: Bundle installation is not running if gemfile version is &lt;1.2.0
JE-14347|Ruby: Gem in environment is not cleaned after new gemfile deploying
JE-14349|Ruby: Custom gems are loaded after their deletion and node's restarting
JE-14762|Error while deploying application from repository
JE-14876|Refilling balance by payment method doesn't work
JE-14891|Fixed size of the first refilling payment
{{%/table%}}

<p style="text-align: right;"><a href="#back">Back to top</a></p>