---
draft: false
title: "Release Notes 1.9.2"
aliases: ["/release-notes-192/", "/release-notes192/"]
seoindex: "index, follow"
seotitle: "Release Notes 1.9.2"
seokeywords: "git svn auto deploy, sso integration, cleverbridge billing system, mobile application, search box, improvement, nginx update, java update, platform features"
seodesc: "See the description of the new features implemented and presented with PaaS 1.9.2 Release version. At the end of the notes you can also see the list of bugs fixed by our developers in this version."
---

# Virtuozzo Application Platform 1.9.2 Release Notes

*This document is preliminary and subject to change.*

<i>**Note:** More info due to each feature will be added in the nearest future.</i>  
In this document you can find all the new features, enhancements and visible changes included in the **PaaS 1.9.2** release:

* [New Features](#a)
* [Security issues](#u)
* [Improvements](#d)
* [Fixes](#f)

For detailed information on using any of the platform features, please refer to the [users' documentation](https://jelastic.com/docs).


## <div id="a">New Features</div> 

* [GIT & SVN Auto-deploy](#1)
* [SSO integration](#3)
* [Cleverbridge billing system integration](#4)
* [Platform Mobile App](#5)
* [How do I..? search box](#6)
* [Software Stack Versions](#7)


## <div id="1">GIT & SVN Auto-deploy</div>

To greatly increase your productivity as a developer, the platform provides you with the possibility to set periodical **automatic deployment** of your project based on the changes you've committed via GIT/SVN repository.

You can work in GIT/SVN without ever leaving it. Simply update your code, make a commit and all of the changes in your VCS project will be automatically pushed to your production environment after a specified interval of time.

To set automatic updates of your project due to your commits in GIT tick the **Check and Auto-deploy Updates** checkbox in the **Add project** window and specify the interval for checking in minutes.

That's all! Just make a small configuration while adding your project to the platform and continue working with your code through GIT/SVN without even coming back to our dashboard again, being sure that everything is up-to-date on your production automatically!

[More info](/automatical-project-update)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="3">SSO integration</div>

**Single Sign On (SSO)** is intended to simplify the processes of balance refilling and opening of support tickets for all billing customers, if a hosting provider has a custom billing system.

If your hoster has in-house billing system and you want to open a support ticket (*Help > Contact Support*) or to refill account (*Balance > Refill balance*) the one-time link particularly for your request will be generated. With this link you'll be redirected to the requested Hoster's Portal or Billing panel sub-page respectively and automatically logged in without necessity to enter your credentials.
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="4">Cleverbridge billing system integration</div>

**Cleverbridge** is an online billing system based on the SaaS model. It's hosted externally from a hosting provider and built upon multi-tenancy architecture. 
Cleverbridge provides a single access point to all payment processing centers. That is why you can choose any payment method convenient for you among a wide range of available payment systems.

The processes of convertion and refilling is performed through the platform dashboard. This provides you with a sufficient convenience while working. You don't need to leave the platform dashboard, to investigate some other systems admin panels or to remember any extra credentials. Just do all the needed steps via our user-friendly UI.
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="5">Platform Mobile App</div>

Keep in touch with your hosting using the **Platform Mobile App**! It was developed to ease the stress of everyday life and to boost your workday productivity. For now our app is available for **iPhone 4, 4S, 5** and **iPad 2, 3, 4G**.

Install the **Platform Mobile App** from the Apple Store and log in to your PaaS account for the ability to trace and change the state of your environments and to keep track of your balance, right from your mobile device. The interface of the app was made to be intuitive and user-friendly, so you can easily figure out how to use it within seconds.

[More info](/mobile-app)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="6">How do I..? search box</div>

If you have any questions on using our platform you can use the "How do I..?" search box, right in the dashboard. Simply enter the question you are interested in and you'll be redirected to the list of appropriate platform documents which may help you.

[More info](/dashboard-guide/)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="7">Software stack versions</div>

The component templates are updated to the latest versions:

|Stack|Version|
|---|---|
|***Tomcat 6***|6.0.37|
|***Tomcat 7***|7.0.39|
|***TomEE***|1.5.2|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_25|
|***MariaDB***|5.5.31/10.0.3|
|***MongoDB***|2.4.5|
|***MySQL***|5.5.32|
|***PostgreSQL 8***|8.4.17|
|***PostgreSQL 9***|9.2.4|
|***CouchDB***|1.3.1|
|***nginx***|1.4.1|
|***Maven***|3.0.5|
|***Centos 6***|6.4|
|***Memcached***|1.4.15|
|***Apache***|2.2.15-28|
|***NGINX PHP***|1.4.1|
|***PHP 5.3***|5.3.27|
|***PHP 5.4***|5.4.17|
|***PHP 5.5***|5.5.0|

[More info](/software-stacks-versions)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="u">Security Issues</div>

1. [NGINX Update](#21)
2. [Java6/7 Update](#22)   
  
* <div id="21"><u><b>NGINX Update</b></u></div>

*<u>CVE-2013-2028</u>*

A stack-based buffer overflow might occur in a worker process while handling a specially crafted request, potentially resulting in arbitrary code
execution.
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}

* <div id="22"><b><u>Java6/7 Update</u></b></div>

*<u>CVE-2013-1569, CVE-2013-2383, CVE-2013-2384 , CVE-2013-2420</u>*  
Unspecified vulnerability in the Java Runtime Environment (JRE) component in Oracle Java SE 7 Update 17 and earlier, 6 Update 43 and earlier, and 5.0 Update 41 and earlier allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors related to 2D.

*<u>CVE-2013-2432</u>*  
Unspecified vulnerability in the Java Runtime Environment (JRE) component in Oracle Java SE 7 Update 17 and earlier, 6 Update 43 and earlier, 5.0 Update 41 and earlier, and JavaFX 2.2.7 and earlier allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors related to 2D.

*<u>CVE-2013-2434</u>*  
Unspecified vulnerability in the Java Runtime Environment (JRE) component in Oracle Java SE 7 Update 17 and earlier and JavaFX 2.2.7 and earlier allows remote attackers to affect confidentiality, integrity, and availability via unknown vectors related to 2D.
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}


## <div id="d">Improvements</div>

The following table lists the improvements in PaaS 1.9.2

|    #    |Description|
|---|---|
|***JE-7593***|Ability to deploy [PHP projects from GIT](/php-git-svn) repository with submodules/dependencies added|
|***JE-8808***|Modules mod_security and mod_geoip added to [Apache and NginxPHP](/apache-nginx-modules) templates|
|***JE-8814***|Full access to the [conf.d](/application-configuration#1) folder via dashboard is provided|
|***JE-9511***|"Forgot password" link is added to the requesting password dialog box which appears while environment deletion|
|***JE-9968***|The possibility to look through GIT/SVN pull [logs](/view-log-files/) via dashboard is implemented. Also these logs are available via FTP|
|***JE-10257***|Special signs (such as #) in the context names are allowed|
|***JE-10292***|Ability to configure memory settings for java containers by changing GC, -Xmx, -Xms parameters via *variables.conf* (configs -&gt; server)|
|***JE-10343***|[FTP feature](/ftp-ftps-support) for databases is added|
|***JE-10518***|/etc/nginx/conf.d, /var/lib/pgsql/data and /opt/jetty/contexts [catalogs](/application-configuration) shared in dashboard|
|***JE-10701***|Script for MongoDB backup|
|***JE-10853***|Login form was redesigned|
|***JE-10860***|[Php 5.5.0](/php-versions) support added|
|***JE-10955***|File [/etc/php.ini](/application-configuration#2) shared for all DB|
|***JE-11125***|[Action logs](/task-panel-cloud-hosting-in-jelastic) added for file manager|


## <div id="f">Fixes</div>

The following table lists the bug fixes in PaaS 1.9.2

|#|Description|
|---|---|
|***JE-11511***|Stopped environment does not rebind IP if it was slept|
|***JE-11228***|Logrotation doesn't work for Nginx instance|
|***JE-11178***|Maximum characters for name is 26 instead of 32|
|***JE-11123***|JEM returned not formatted (not JSON) error message for maven container|
|***JE-10990***|Refactoring SleepTrialInactiveJob|
|***JE-10809***|Dhclient is missing at centos-jelastic-6-x86_64 OS template|
|***JE-10801***|Change minimum allowed balance quota|
|***JE-10659***|Absent log rotation in Memcached node|
|***JE-10616***|Cloudlet Usage is not displayed for shared environment|
|***JE-10542***|Message {"result":1,"source":"JEL","error":"Failed to start "} appears because of absence of firewall metadata in the container|
|***JE-10469***|Tomcat fails to start|
|***JE-10463***|Remove Context {"result":5000,"error"Numerical result out of range","source":"JEL"}|
|***JE-10405***|eAccelerator built for wrong version of php|
|***JE-10359***|Cronjob first line is inapporopriate|
|***JE-10349***|Wrong password while installing FTP into old container|
|***JE-10301***|com.jelastic.api.server.billing.extern.pba.exception.GatewayException: code -1 base64 decoded message: Password of this length should contain more different characters.|
|***JE-10285***|Sometimes on all productions 502 handler falls|
|***JE-10249***|Environment state is not saved if exception occures during sleep process|
|***JE-10198***|Error while registering invalid card (Credit Card Number is invalid.)|
|***JE-10129***|SynchEnvsJob does not have actual state during execution|
|***JE-9975***|PBAS bridge error processing overdue invoice|
|***JE-9868***|User nginx can not create file in cache|
|***JE-9851***|Account Information in PBAS is displayed incorrectly|
|***JE-9849***|Add credit card pop-up - com.jelastic.api.server.billing.extern.exception.FieldInvalidFormatException|
|***JE-9827***|If migration through pva-agent API fails we need to execute hard ONLINE migration|
|***JE-9799***|PBAS Session TTL behaviour is invalid|
|***JE-9760***|Mongodb authentication failed|
|***JE-9745***|Periodically custom domains show Host_Not_Found page|
|***JE-9566***|Pentaho queries leads to DB overloading|
|***JE-9423***|Post billing users recieve emails about refill|
|***JE-9283***|Post billing customers get messages "Your PaaS account needs to be refilled!"|
|***JE-8842***|Wrong redirect port in server.xml|
|***JE-8816***|Internal zone contained 2 records for always.lumatagroup.ru|
|***JE-8768***|mv: '/opt/tomcat//webapps//dream.war' and '/opt/tomcat//webapps/dream.war' are the same files|
|***JE-8518***|Magento JPS doesn't work properly|
|***JE-7322***|uploadfiles - 1704, org.hibernate.LazyInitializationException: illegal access to loading collection|
|***JE-6523***|Uploading files to "modules" dir failed: {"result":8,"error":"Permission denied."..."path":"/usr/lib64/php/modules","script":"UploadFiles"}}|
|***JE-5278***|Wrong deactivation emails for trial users|