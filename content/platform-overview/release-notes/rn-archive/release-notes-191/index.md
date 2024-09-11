---
draft: false
title: "Release Notes 1.9.1"
aliases: "/release-notes-191/"
seoindex: "index, follow"
seotitle: "Release Notes 1.9.1"
seokeywords: "release 1.9.1, cloudlet, hosting, php, application server, database, configuration, version, update, scheduler cron, security issues update"
seodesc: "New Features in PaaS 1.9.1: Config manager improvement, PostgreSQL 9.2.4 support, CRON Scheduler, Scheduling database backups, Notification about running out of resources (Mem, CPU), Netbeans IDE Plugin, Software Stacks Versions"
---

# Virtuozzo Application Platform 1.9.1 Release Notes

*This document is preliminary and subject to change.*

In this document you can find all the new features, enhancements and visible changes included in the **PaaS 1.9.1** release:

* [New Features](#a)
* [Security issues](#u)
* [Fixes](#c)

For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs).


## <div id="a">New Features</div> 
* [Config manager improvement](#1)
* [PostgreSQL 9.2.4 support](#2)
* [CRON Scheduler](#3)
* [Scheduling database backups](#4)
* [Notification about running out of resources (Mem, CPU)](#5)
* [Netbeans IDE Plugin](#7)
* [Software Stacks Versions](#6)


## <div id="1">Config manager improvement</div>
Your environment consists of several application servers? In this case you can face the need to set some custom configurations for each of them separately.  
Now the platform provides you with such possibility.  
Just click the **Config** button for your application server. The list of configuration folders will be opened as usual.  
At the top of the opened tab now you can see a drop-down menu with a list of your servers. Choose the one you need and make the configurations. To apply the changes:

* only for the chosen server click **Save only for current instance** button from drop-down menu;
* for all the servers click **Save**.

In such a way you can choose whether you want to configure all the servers together or just some specific one. 

[More info](/application-configuration)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="2">PostgreSQL 9.2.4 support</div>

**PostgreSQL** is well positioned DB for building and running applications in the cloud. In the platform, we implemented a new 9.2.4 version that provides you with a number of long-expected features:

* ***Synchronous Replication***: enable high-availability with consistency across multiple servers
* ***Per-Column Collations***: support linguistically-correct sorting per database, table or column
* ***Unlogged Tables***: greatly improves performance for ephemeral data
* ***K-Nearest-Neighbor Indexing***: index on "distance" for faster location and text-search queries
* ***Serializable Snapshot Isolation***: keeps concurrent transactions consistent without blocking, using "true serializability"
* ***Writeable Common Table Expressions***: execute complex multi-stage data updates in a single query
* ***Security-Enhanced Postgres***: deploy military-grade security and Mandatory Access Control
* ***Foreign Data Wrappers***: attach and query other databases from PostgreSQL
* ***Cascading replication***: enables users to run even larger stacks of horizontally scaled servers
* ***JSON support***: query results can be returned as JSON data types
* ***Range Types support***: allow developers to create better calendaring, scientific, and financial applications
* Linear scalability to 64 cores, index-only scans, reductions in CPU power consumption, scalability and flexibility improvements etc.

More information about PostgreSQL 9.2.4 security fixes you can find in the *[Security Issues](#u)* block.

Also the **Posgis** module was enabled - a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL. Also it provides a list of additional features which you can find [here](http://postgis.net/).

[More info](/connection-to-postgresql)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="3">CRON Scheduler</div>

**Cron** is the time-based job scheduler. It gives an opportunity to schedule jobs to run periodically at certain times or dates. Cron is commonly used to automate system maintenance or administration.

In this release cron file was implemented to all compute and database nodes in the platform. You can run your programs at specified time with a help of scheduler, which receives your instructions and performs any tasks following derived scenarios.  
Earlier a cronjob could be configured in environment only using  virtual dedicated server (VDS). Now you can perform periodic tasks without necessity to add VDS.  
To set up cron just click **Config** button for your server. Open *{server_name}* file in **cron** folder and make all necessary settings.

To perform your script via cron upload it to **home** directory for your Java server, to directory with your application for the PHP server, or to **scripts** directory for your database.  
The detailed information on cron configuration is described in [Cronjob Setting](/cron-job) document. 

[More info](/cron-job)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="4">Scheduling database backups</div> 
Scheduled backups are data backup processes which proceed automatically on a scheduled basis without additional computer or user intervention. The advantage of using scheduled backups is obvious: instead of manual backups, a backup process can be run during off-peak hours when data is unlikely to be accessed, precluding or reducing the impact of backup window downtime.

With the platform, you can backup your database(s) or just some tables in it right from the configuration files. Open the file in the **cron** folder and make the needed settings by stating:

* frequency of the script evoking;
* the path to the default script (available for MariaDB and MySQL) or to your own (you can upload it to the ***scripts*** folder);
* your database username and password (you received them in the email after adding database to the environment);
* if you want to backup several databases or some separate tables, then enter their names separated by commas.

After that save your settings and wait the time of backup you've scheduled. Then navigate to **backup** folder where you can see **.bz2** files with all executed backups.

That's all! Now you can be sure that all your data is being saved periodically and can be restored or reused.

[More info](/scheduling-backups)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="5">Notification about running out of resources (Mem, CPU)</div>
While creating an environment you state the cloudlet limits for each node. In such a way the resources are limited and the spends are regulated.

When the traffic grows an application requests more resources for normal work. And if the limits stated by you is too low, this can lead to the failure in the app performance. For such cases the notification about running out of resources is implemented.  
If application resource (Memory or CPU) consumption reaches an appropriate threshold, you receive the email notifications with a suggestion to increase the cloudlet limit.
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="7">Netbeans IDE Plugin</div>

**NetBeans** is a free and open-source integrated development environment (IDE). It supports development of all Java application types (Java SE, Java ME, web, EJB and mobile applications) out of the box.

All the functions of the IDE are provided by modules, which allow **NetBeans IDE** to be extended. Each module provides a well defined function, such as support for the Java language, editing, support for the CVS or SVN versioning system. NetBeans IDE contains all the modules needed for Java development in a single download, allowing the user to start working immediately.  
PaaS team has created a [plugin](http://plugins.netbeans.org/plugin/48045/jelastic-cloud-platform-integration) for NetBeans development platform that simplifies the process of application management and development in PaaS.  
Using this plugin you can easily manage your environments, work with log files and contexts, develop and deploy your projects.

[More info](/deployment-guide/)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="6">Software stacks versions</div>

The component templates are updated to the latest versions:

|Stack|Version|
|---|---|
|***Tomcat 6***|6.0.36|
|***Tomcat 7***|7.0.37|
|***TomEE***|1.5.1|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_38|
|***Java 7***|1.7.0_11|
|***MariaDB***|5.5.30/10.0.1|
|***MongoDB***|2.4.1|
|***MySQL***|5.5.30|
|***PostgreSQL 8***|8.4.17|
|***PostgreSQL 9***|9.2.4|
|***CouchDB***|1.2.1|
|***nginx***|1.2.7|
|***Maven***|3.0.4|
|***Centos 6***|6.4|
|***Memcached***|1.4.15|
|***Apache***|2.2.15-26|
|***NGINX PHP***|1.2.7|
|***PHP 5.3***|5.3.23|
|***PHP 5.4***|5.4.13|

[More info](/software-stacks-versions)
{{%right%}}[Back to the list of New Features](#a){{%/right%}}


## <div id="u">Security Issues</div>
 
* [Fail2Ban](#20)
* [Migration to CentOS 6.4](#21)
* [Update of MongoDB to 2.4.1](#22)
* [Update of phpMyAdmin](#23)
* [Update of PHP to 5.4.13 and 5.3.23](#24)
* [PostgreSQL updated to 9.2.4 and 8.4.17](#25)

1. <div id="20"><b><u>Fail2Ban</u></b></div>  
**Fail2ban** is an intrusion prevention framework written in the Python programming language. It is able to run on POSIX systems that have an interface to a packet-control system or firewall installed locally (for example, iptables or TCP Wrapper).  
Generally **Fail2Ban** then used to update firewall rules to reject the IP addresses for a specified amount of time, although any arbitrary other **action** (e.g. sending an email) could also be configured. Out of the box jFail2Ban comes with **filters** for various services (apache, curier, ssh, etc.).  
**Fail2ban** is installed on the platform servers and used to block selected IP addresses that may belong to hosts that are trying to breach the system's security. Fail2ban operates by monitoring log files for selected entries and running scripts based on them. It bans any host IP that makes too many login attempts or performs any other unwanted action within a time frame defined by the administrator. After 3 attempts to connect to the container via SSH with incorrect credentials the IP-address of the user will be blocked.
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}

2. <span id="21"><u>**Migration to CentOS 6.4**</u></span>  
CentOS is an enterprise-class computing platform derived from sources freely provided to the public by Upstream OS Provider (UOP).  
CentOS was updated to 6.4 version due to the following reasons:  
    * a wide range of security improvements;
    * the latest version of VZ ostemplate is based on CentOS 6.4.
[More info](http://wiki.centos.org/Manuals/ReleaseNotes/CentOS6.4)
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}

3. <span id="22"><u>**Update of MongoDB to 2.4.1**</u></span>  
MongoDB is a scalable, high-performance, open source, document-oriented database. In this release the new MongoDB 2.4.1 version was implemented. It provides you with a number of new features, which you can see below.  
Update to the 2.4.1 version includes the following security improvements:
    * **Role Based Access Control and New Privilege Documents** - role based access control system that provides more granular privileges to MongoDB users. 2.4.1 also introduces a new format for documents in a database's *system.user* collection.</li>
    * **Enhanced SSL Support** - instances can optionally require clients to provide SSL certificates signed by a Certificate Authority.
[More info](http://docs.mongodb.org/manual/release-notes/2.4/#security-improvements)
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}

4. <span id="23">**<u>Update of phpMyAdmin</u>**</span>  
The platform updated phpMyAdmin to 3.5.7 version to solve a set of security issues with fetching the version information from a non-SSL site, which was vulnerable to a MITM attack.   
Earlier to display information about the phpMyAdmin version on the main page, a piece of JavaScript was fetched from the phpmyadmin.net website in non-SSL mode. In such a way a man-in-the-middle could modify this script on the wire to cause mischief.   
The updated version involves fetching a JSON file instead of JavaScript file that makes the process more secure. 
[More info](http://www.phpmyadmin.net/home_page/security/PMASA-2012-7.php)
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}

5. <span id="24">**<u>Update php to 5.4.13 and 5.3.23</u>**</span>  
PHP was updated to 5.4.13 and 5.3.23 versions in the platform. These update fixed about 15 bugs, including fixes for CVE-2013-1643 and CVE-2013-1635. 
**CVE-2013-1643**
The SOAP parser in PHP before 5.3.22 and 5.4.13 allows remote attackers to read arbitrary files via a SOAP WSDL file containing an XML external entity declaration in conjunction with an entity reference, related to an XML External Entity (XXE) issue in the soap_xmlParseFile and soap_xmlParseMemory functions. 
**CVE-2013-1635**
ext/soap/soap.c in PHP before 5.3.22 and 5.4.13 does not validate the relationship between the soap.wsdl_cache_dir directive and the open_basedir directive, which allows remote attackers to bypass intended access restrictions by triggering the creation of cached SOAP WSDL files in an arbitrary directory. 
[More info](http://www.php.net/ChangeLog-5.php)
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}

6. <span id="25">**<u>PostgreSQL 8.4.17 and 9.2.4</u>**</span>  
We implemented PostgreSQL 9.2.4 and  updated the current version of the database to 8.4.17. This update fixes a high-exposure security vulnerability, such as:
    * possibility for a connection request containing a database name that begins with "-" to be crafted, that could damage or destroy files within a server's data directory. Anyone with access to the port the PostgreSQL server listens on could initiate this request;
    * random numbers generated by contrib/pgcrypto functions were easy for another database user to guess;
    * possibility for an unprivileged user to run commands that could interfere with in-progress backups;
    * insecure passing of superuser passwords to a script;
    * usage of predictable filenames.
Add PostgreSQL node to your environment and experience all the benefits of the updated versions.  
[More info](http://www.postgresql.org/about/news/1456/)
{{%right%}}[Back to the list of Security Issues](#u){{%/right%}}


## <div id="c">Fixes</div>

The following table lists the bug fixes in PaaS 1.9.1

|#|Description|
|---|---|
|***JE-4723***|Ability to add external IP for trial account environment|
|***JE-4937***|Environments can't be loaded after signing in|
|***JE-8573***|Error sometimes appears while installing xWiki from JPS|
|***JE-8761***|"Undeploy failed" error while deleting context|
|***JE-8771***|SSL Connection Error while trying to log in admin page by HTTPS|
|***JE-8782***|When SSL is enabled a warning appears: WARNING: [SetAllPropertiesRule] Unknown macro: {Server/Service/Connector} Setting property 'Disabled' to 'true' did not find a matching property.|
|***JE-8859***|Can not upload nothing but .jar to lib folder|
|***JE-8876***|Container return error message: Warning:  --directory (-d) option is undocumented and no-op.  Use -rf for deleting non-empty dirs|
|***JE-8993***|502 - application down {Install applications using solutions}|
|***JE-9022***|Jetty app server does not delete old context automatically|
|***JE-9048***|Error appears while resetting MySQL password|
|***JE-9096***|Container returns error message after deploy: rmdir: /var/www/webroot/steins//index.php: Not a directory|
|***JE-9097***|Container returns error message: rmdir: failed to remove /var/www/webroot/api//aethas-api': Directory not empty|
|***JE-9100***|Container returns error message after deploy: /usr/lib/jelastic/libs/php-common-deploy.lib: line 70: [: missing `]'|
|***JE-9103***|Custom SSL works for ROOT context only in NginxPHP node|
|***JE-9242***|Authentication Failed error while cloning project by link with port number|
|***JE-9496***|Inability to awake sleeping environment by URL except App Server (entry point) link|