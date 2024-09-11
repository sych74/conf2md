---
draft: false
title: "Release Notes 1.9.3"
aliases: "/release-notes-193/"
seoindex: "index, follow"
seotitle: "Release Notes 1.9.3"
seokeywords: "platform gc agent, zend opcache extension, php workers, mod security module, mongodb backups, http transport error, whmcs integration"
seodesc: "See the details on the new features and improvements developed and presented within release of new PaaS 1.9.3 version."
---

# Virtuozzo Application Platform 1.9.3
<a id="top"></a>
*This document is preliminary and subject to change.*  
* **Note:** More info due to each feature will be added in the nearest future. 

In this document you can find all the new features, enhancements and visible changes included in the **PaaS 1.9.3** release:

* [Features and Improvements](#fi)
* <a href="#fix" id="fi">Bug Fixes</a>

For detailed information on using any of the platform features, please refer to the [users' documentation](https://jelastic.com/docs).


## Features and Improvements
* <a href="#a">Scalability and Performance Improvements</a>
* [Database Improvements](#b)
* [HTTP Transport Error](#c)
* <a href="#d" id="a">Billing Improvements</a>
* <a href="#e" id="agc">Site Redesign</a>
* <a href="#f">Saving Config Edits Automatically</a>
* [Hosting Provider Resolution for Mobile Application](#g)
* [Software Stack Versions](#ss)


## A. Scalability and Performance Improvements

## Java
#### Platform GC Agent</span>

<b>Garbage collection</b> (GC) is a form of automatic memory management. The garbage collector attempts to reclaim garbage, or memory occupied by objects that are no longer in use by the program. As a result, you can reduce your costs by not paying for unused resources.

In order to release reserved memory, but at the same time unused **RAM** by JVM to OS, the platform uses a special **Garbage Collector agent**.

Platform GC agent is enabled for all newly created Java application servers.

It works only for two kinds of Garbage Collection:

**-XX:+UseParNewGC** (if -Xmx &lt; 8000m)
**-XX:+UseG1GC** (if -Xmx >= 8000m)These parameters can be customized but if you specify any other GC manually, then calling full GC will be disabled.

By default, the Garbage Collection process is run every **15 minutes** (beginning from every JVM start) to force the release of unused application memory. The period of checks can be changed based on your requirements. You can also switch to debug mode.

***-javaagent:/var/lib/jelastic/java/jelastic-gc-agent.jar=debug=true,period=900***

This solution is unique and originally devised by PaaS engineers to improve your application memory management and as a result, to reduce the RAM usage.
{{%right%}}[Back to the list of Features and Improvements](#fi){{%/right%}}

## PHP

* <a href="#d1" id="d1">Zend OPcache</a>
* [Change the Number of Workers Automatically](#d2)
* <a href="#d3">Custom Settings of mod_security</a>

#### 1. Zend OPcache
[Zend OPcache](http://ua1.php.net/opcache) is now enabled by default, which results in a performance improvement of up to 40%. Zend OPcache speeds up PHP execution by opcode caching and optimization.

Apache and Nginx (php: 5.3, 5.4, 5.5) include OPcache extension enabled via **etc > php.ini**:  
***zend_extension=/usr/lib64/php/modules/opcache.so***

The default size and other OPcache settings can be configured via the **php.ini** file by changing the following parameters:

* **opcache.enable=1**
enable/disable OPcache extension

* **opcache.memory_consumption=64**
set the amount of memory to use (megabytes)

* **opcache.interned_strings_buffer=8**
set the amount of memory to be used for storing internal strings (e.g. classnames)

* **opcache.max_accelerated_files=4000**
the maximum number of files to be cached

* **opcache.revalidate_freq=60**
the frequency of checking file timestamps for changes to the shared memory storage allocation

* **opcache.fast_shutdown=1**
enable/disable a fast shutdown sequence for accelerated code

* **opcache.enable_cli=1<a id="d2"></a>**
enable/disable the OPcache for the CLI version of PHP

[More info](/php-extensions)
{{%right%}}[Back to the list of PHP improvements](#php){{%/right%}}

#### 2. Change the Number of Workers Automatically

The number of workers for processing PHP requests is increased automatically in an Apache server depending on the cloudlet amount you stated for it.
To check this, click **Config** for your Apache app server and navigate to the **conf > httpd.conf** file.  
Find and remember the **Max Clients** value. After that, change the topology of your environment by increasing or decreasing the cloudlet limit for your server.
Return to the **conf > httpd.conf** file. As you can, see the number of **Max Clients** has increased/decreased.  
<a id="d3"></a>
Note that this function will be disabled if you remove the following string from the **httpd.conf** file:  
#Jelastic autoconfiguration mark

[More info](/php-application-server-config#ab)
{{%right%}}[Back to the list of PHP improvements](#php){{%/right%}}

#### 3. Custom Settings of mod_security

[mod_security](http://www.modsecurity.org/) is a super handy Apache module which provides such abilities as simple filtering, URL and Unicode encoding validation, auditing, null byte attack prevention, upload memory limits, server identity masking, built in chroot support and many more.  
This module is available in the platform by default and can be configured via **conf.d > mod_security.conf** file.  
Here, you can edit the default configurations or add your own custom settings.<a id="b"></a>
For example, you can add additional ModSecurity Rules. For this, you simply need to upload your custom rule to the **modsecurity.d** folder. It will be automatically activated by the ***Include modsecurity.d/<i>.conf**</i> string available in the **conf.d > mod_security.conf** file by default.

[More info](/apache-security-configurations)
{{%right%}}[Back to the list of PHP improvements](#php){{%/right%}}


## B. Database Improvements

* [Shared MyAdmin-jel.conf, phpPgAdmin and couchdb.conf files](#e1)
* <a href="#e2" id="e1">Killing Processes for Releasing RAM</a>
* [Backup of Several MongoDB Databases](#e3)
* [Changes in Database Default Configurations](#e4)

#### 1. Shared MyAdmin-jel.conf, phpPgAdmin and сouchdb.conf files
Starting with this release, you have access to the **MyAdmin-jel.conf** (for MariaDB and MySQL), **phpPgAdmin** (for PostgreSQL) and **couchdb.conf** (for CouchDB) files. They are located in the **conf.d** folder.<a id="e1"></a><a id="e2"></a>  
These files can be edited in order to set appropriate criteria for allowing or denying access by IP address or domain to the application with the database on an Apache web server level.

[More info](/database-configuration-files)
{{%right%}}[Back to the list of Database improvements](#b){{%/right%}}

#### 2. Killing Processes for Releasing RAM
When your environment lacks RAM, the processes with high memory consumption are killed by OOM killer to release the resources. The order of disabling the processes is specified by OOM conditions.
<a id="e3"></a>  
Now the ***oom_score_adj*** is used to make less essential processeses killed primarily (httpd processes). Only if more RAM is still needed to be released, the MySQL processes are going to be killed.
{{%right%}}[Back to the list of Database improvements](#b){{%/right%}}

#### 3. Backup of Several MongoDB Databases

Making backups is a rather important part of the development process as a guarantee of your data security and integrity. The platform lets you schedule your database backups so you can always restore the last copy of your information in case of occasional data loss. For this, we provide a special backup script for databases, which you can configure based on your own needs.  
<a id="e4"></a>In this release we've improved the MongoDB database backup script. For now, you can use it for backing up several databases. Just specify the necessary configurations as it is described in the [MongoDB Databases Backup](/mongo-backup-restore) instruction.

<a href="/mongo-backup-restore">More info</a>
{{%right%}}[Back to the list of Database improvements](#b){{%/right%}}

#### 4. Changes in Database Default Configurations<span style="color: #333333;">
In this release, the following default configurations for all databases were changed in the **php.ini** file as follows:  
***upload_max_size = 1024MB***  
***post_max_size = 1024MB***  
***max_execution_time = 600***  
***max_input_time = 600<a id="e5"></a>***<a id="c"></a>

This results in the ability to upload big dumps. Such changes are implemented to all new and earlier created containers, except the containers with your custom settings, i.e. if you configured these parameters manually based on your requirements.
{{%right%}}[Back to the list of Database improvements](#b){{%/right%}}


## C. HTTP Transport Error
While performing any actions in the platform dashboard, (like creating an environment, app deploying, building a project, restarting your app etc.) you could possibly face the problem of a ***HTTP transport error*** arising due to some Internet issues. As a result of the disconnection, the action you have started would be fully stopped and you would have to start everything again.
 
<a id="c"></a><a id="d"></a><a id="d"></a><a id="mi"></a><a id="d"></a>
Now the situation is radically improved. <a id="epsi"></a>The disconnection will simply suspend the process which is already started until the connection is reestablished. After that, the last request will be reinitiated and the process completed, without the need to create any additional settings.<a id="epsi"></a><a id="epsi"></a>
{{%right%}}[Back to the list of Features and Improvements](#fi){{%/right%}}


## D. Billing Improvements

* <a href="#ubhd" id="ubhd">Updated Billing History Display</a>
* <a href="#wijbs" id="ubhd">WHMCS Integration with the Billing System</a>

#### 1. Updated Billing History Display
Using the **Billing history** option, you can monitor the charges applied for consumed resources. To make this even more convenient, we have modified the way of presenting the billing data.  

Here, you can specify the desired start / end dates and the time period interval to view your billing data. The billing history is displayed by time period, with the corresponding charges to the right. Use the {{%icon%}}![plus button](plus-button.png){{%/icon%}}
icon to expand the view to reveal additional details about resource usage.  

The data is grouped by the environments. Each environment in the list can be expanded to see the information about charges applicable to each server within the environment. The servers of the environment are listed in alphabetical order. After them, the Public IP and SSL are listed and their price is stated, if they are enabled in the environment.

In the **Billing history** table you can see the number of fixed and flexible cloudlets consumed, the amount of paid traffic and the sum charged for each type of server or service (Public IP and SSL).<a id="wijbs"></a>

The total charges between the selected dates are calculated for you at the very bottom of the list.
[More info](/charged-resources#2)


#### 2. WHMCS Integration with Billing System

In this release, we implemented one more billing system &ndash; **WHMCS**. It is a universal billing hosting-oriented solution with an intuitive, user-friendly interface and broad functionality. WHMCS supports its extension using new add-on modules. We have also implemented a dedicated Add-on Module, written in PHP.

With WHMCS, you can choose between a wide range of payment methods. Processing of your payments, as well as managing the list of orders and invoices, is available right in the platform dashboard. You are also able to navigate directly to your WHMCS billing panel from the dashboard, without the necessity to enter your credentials.

<a id="e"></a>To evaluate all of the benefits of WHMCS usage, you simply need to sign up for a PaaS account via a web hosting provider in your region and upgrade your account to to the full version. To see the list of hosting providers with the WHMCS billing solution installed, navigate to the [Billing System](/billing-system) document.

[More info](/whmcs-integration#e)
{{%right%}}[Back to the list of Features and Improvements](#fi){{%/right%}}

## E. Site Redesign
Recently we've launched our new corporate web-site with a complete redesign of our logo and other materials. For now, it completely reflects platform's new positioning as a combination of two cloud's most transformative technologies - Platform-as-a-Service (PaaS) and Infrastructure-as-a-Service (IaaS).

The new PaaS site is optimized for enterprises, hosting service providers OEMs and developers. More detailed information about each market solution can be found in the corresponding sections of our site:

* [PaaS for Enterprise](https://jelastic.com/solutions/jelastic-for-enterprise/)
* [PaaS for OEMs](https://jelastic.com/solutions/jelastic-for-oems/)
* [PaaS for Hosting Service Providers](https://jelastic.com/solutions/jelastic-for-hosting/) 
* [PaaS for Developers](https://jelastic.com/solutions/jelastic-for-developers/)

Find useful tips in our redesigned documentation (Hosting Center) and at the new Video page. Stay updated with our Blog posts and News & Events. <a id="f"></a>Keep in touch with the platform <a id="h"></a>community via StackOverflow where our forum was moved in order to dramatically improve the experience of providing assistance with various technical questions from our customers.<a id="h"></a>
Feel free to leave your feedback about our new site, in order to improve it even more.
{{%right%}}[Back to the list of Features and Improvements](#fi){{%/right%}}


## F. Saving Config Edits Automatically
While saving the changes in any config file, you are asked to confirm this action.
We've added the line ***&ldquo;Do not show this dialog again&rdquo;*** to the confirmation window. Tick this option and as a result, all future edits will be saved automatically without asking for confirmation.<a id="g"></a>
This setting will be applied for all types of config files, in all of your environments.

[More info](/application-configuration)
{{%right%}}[Back to the list of Features and Improvements](#fi){{%/right%}}


## G. Hosting Provider Resolution for Mobile Application
Hosting Provider Resolution is now implemented for the platform mobile application which helps to automate the process of accessing the dashboard of the required hosting provider.
When you enter your account credentials to access the dashboard via the Mobile app, a special service checks the availability of this account at every hosting provider. Checking is performed via attempting to log in to every hosting provider and collecting sign in statuses (if an account is available or not). After this procedure, all of the collected information is transferred back to your mobile application.

As soon as the information is received by the mobile application, you will be automatically signed into the dashboard of the hosting provider you are registered at with the provided credentials. In the case that there are several matches (i.e you are registered at several hosters with the same credentials) you will be asked to choose the desired one from the available list.<a id="ss"></a>

<a id="s"></a>After selecting a particular hosting provider, this choice will be remembered and in future you will be logged into this provider by default without the necessity to enter your credentials again.
{{%right%}}<a href="#fi">Back to the list of Features and Improvements</a>{{%/right%}}


## H. Software Stack Versions

The component templates are updated to the latest versions:

|Stack|Version|
|---|---|
|***Tomcat 6***|6.0.0.37|
|***Tomcat 7***|7.0.47|
|***TomEE***|1.5.2|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_45|
|***MariaDB***|5.5.34 / 10.0.6|
|***MongoDB***|2.4.8|
|***MySQL***|5.5.34|
|***PostgreSQL 8***|8.4.18|
|***PostgreSQL 9***|9.3.1|
|***CouchDB***|1.5.0|
|***nginx***|1.4.3|
|***Maven***|3.0.5|
|***Centos 6***|6.4|
|***Memcached***|1.4.15|
|***Apache***|2.2.15-29|
|***NGINX PHP***|1.4.3|
|***PHP 5.3***|5.3.27|
|***PHP 5.4<a id="fix"></a>***|5.4.21|
|***PHP 5.5***|5.5.5|

[More info](/software-stacks-versions)
{{%right%}}[Back to the list of Features and Improvements](#fi){{%/right%}}


## Bug Fixes

In the tables below you can see the lists of the bug fixes in PaaS 1.9.3. They are grouped due to the following categories:

* [Java](#bug-java)
* [PHP](#bug-php)
* [Ruby](#bug-ruby)
* [Billing & Billing history tracking](#bug-billing)
* [JEM](#bug-jem)
* <a href="#bug-env" id="bug-java">Resolving & Access to the containers (environments) issues</a>
* [User account & session issues](#bug-user)
* [Emailing issues](#bug-email)
* [Platform statistics](#bug-stat)
* [Platform dashboard](#bug-dashboard)
* [Others](#bug-others)


### JAVA

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-13545 |Rewrite-handler is added to new Jetty build 
JE-12079|Cloning environments, changing topology and evacuating to other nodes may fail due to the short timeout setting
JE-12012|Java applications of a certain size can not be deployed, because of timeout in the deployment verification function, which was increased from 40 sec to 3 minutes
JE-11965|Application cannot be deployed with Maven plug-in 
JE-11926|Cloned container with enabled public IPv4 has invalid routes. In some cases it causes timeouts during WAR files deploy
JE-11887|Ability to deploy archive with "root" context as independent project
JE-11877|Autodeploy for SVN projects does not work
JE-11725|Running environment fails due to timeout expiration
JE-11638|If you add VCS project with already existing name, the old one will be overwritten
JE-10826|GlassFish support was improved. Fixed bug relates to cloning GlassFish environment<a id="bug-php"></a>
JE-10794|Impossible to establish remote connection to EJB with GlassFish
JE-8891|Incorrect displaying of HelloWorld application hosted in environment with SSL
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}

### PHP

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-12267|Apache can return 502 error page when doing DB import due to restricted configuration<a id="bug-ruby"></a>
JE-12010|Memcached module error in PHP environments
JE-7492|PHP version of HelloWorld package includes Java word in social networks sharing
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}

### RUBY

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-14351|Gem list is not updating from rubygems.org
JE-14343|Custom SSL problems in Ruby
JE-14341|Fixing Gemfile parsing
JE-14340|Full gem support with dependencies added
JE-14336|Fixing restart problems
JE-14332|Support of SVN gem sources
JE-14327|Fixing Ruby auto deploy process. Environment stuck on production.
JE-12250|JAVA application servers are displayed instead of Ruby servers for ruby-only user groups
JE-11774 |Cron file &ldquo;ruby&rdquo; is absent
JE-11492 |Add project checkbox 'check out' is cutted
JE-11491 |Incorrect permission in folder 'webroot': buttons 'delete' and 'rename' is blocked<a id="bug-billing"></a>
JE-11330 |Can deploy to Ruby environment only English localized projects
JE-12124|No response via https for environments with Custom SSL
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}


### BILLING & BILLING HISTORY TRACKING

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-9842|In billing history, one month is now counted due to correct calendar month days, not just 30 days constant
JE-9756|No costs consumption for SSL and IPv4 usage is displayed in billing history
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}

### JEM

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-13431 |Checkout to branch in git wasn't applied after initial clone operation, but only after first update 
JE-11565|In case the newly deployed VCS project overwrote the same named earlier deployed project, the auto-update functionality could not be disabled
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}

### RESOLVING & ACCESS TO CONTAINERS (ENVIRONMENTS) ISSUES

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-13227|Custom SSL certificates and keys are left in the cloned environment
JE-12656|Wrong environment URL in email if Built-in SSL is enabled
JE-12118|Each database server now has logs directory available through FTP
JE-10828|Validation for external domains binding from internal zone added
JE-8858|Wrong VDS hostname: centos5 instead of centos6<a id="bug-user"></a>
JE-8080|After installing app from the package manager the email without link to environment is received
JE-1227|User can get &ldquo;Cannot lock the Container&rdquo; error when stopping environment or doing other manipulations in a Dashboard, due to lack of synchronization between container functions
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}

### USER ACCOUNT & SESSION ISSUES

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-12021|Upgrade trial account tab doesn't appear after clicking the appropriate button
JE-11732|&ldquo;Email is already registered&rdquo; error while trying to sign up unregistered user
JE-10070|Incorrect "contact support" link in login screen when account is suspended
JE-9707|Auto-authentication link to change topology wizard periodically doesn't work
JE-8583|Message about account creation at the Sign Up form isn't refreshed after language changing
JE-8271|Creation\editing of environment ends with error in the case user's session became invalid<a id="bug-email"></a>
JE-7934|Changing password during environment creation causes 702 error (session crashing)
JE-6151|"Your account has been deactivated..." dashboard error message for the destroyed user
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}


### EMAILING ISSUES

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-12285|Emails are not sent after the update
JE-11793|Users are receiving &ldquo;Out of resources&rdquo; notification in language other than they selected in Dashboard<a id="bug-jca">
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}


### PLATFORM STATISTICS

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-11698|Node's CPU statistics at dashboard summarize the usage instead of aggregation
JE-11683|Running out of resources notifications are sent for unused environments<a id="bug-dashboard"></a>
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}

### PLATFORM DASHBOARD

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-11966|Float menus at dashboard are unavailable while environment is under some action
JE-11771|Inability to copy the informational URLs at dashboard wizard
JE-11769|Can change cloudlet limits for turned off nodes at the topology wizard
JE-11501|Button for nodes selecting is blocked after upload in config manager
JE-11372|Action log line about saved changes in file doesn't appear after saving, only after refresh
JE-9211|After deletion the archive became invisible even if the method has not returned the response<a id="bug-others"></a>
JE-8917|Sub folders with the same name are not displayed in Config Manager after refreshing
JE-5194|Now the archive can't be deployed to the environment if any actions are performed with it
{{%/table%}}
{{%right%}}<a href="#fix">Back to the list of Bug Fixes</a>{{%/right%}}

### OTHERS

{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-12310|Can't refresh environment state due to the transaction confusion
JE-12075|Spare output was suppressed from actions.log which was throwing from the system after NGINX restart
JE-11864|Incorrect FTP uninstall process
JE-11610|Error while starting environment which was manually stopped
{{%/table%}}

{{%right%}}<a href="#top">Back to the top</a>{{%/right%}}