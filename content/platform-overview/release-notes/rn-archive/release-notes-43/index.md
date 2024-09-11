---
draft: false
title: "Release Notes 4.3/4.4"
aliases: "/release-notes-43/"
seoindex: "index, follow"
seotitle: "Release Notes 4.3/4.4"
seokeywords: ""
seodesc: "In this document, you will find all of the new enhancements and visible changes included in the PaaS 4.3 and 4.4."
---

# Virtuozzo Application Platform 4.3 / 4.4
*This document is preliminary and subject to change.*

In this document, you will find all of the new enhancements and visible changes included in the **PaaS 4.3** and **4.4** releases:

* [Improvements](#impr)
* [Bug Fixes](#fix)

<a id="impr"></a>For detailed information on using any of the platform's features, please refer to the [users' documentation](/).


## Improvements
[External IPs Swap via CLI](#ip-swap)  
[PHP 7 Support (4.3 / 4.4)](#php7)  
[MongoDB Driver for PHP Update](#mongo-php-driver)  
[PHP Modules List Refactoring (4.3 / 4.4)](#php-modules)  
[OpenSSL Update](#openssl-update)  
[Node.js Engine Update](#nodejs-update)  
<a href="#software" id="ip-swap"><span>Software Stack Versions</span></a>  
{{%right%}}[Back to the top](#back){{%/right%}}


## External IPs Swap via CLI
In the current Platform update, the functionality of [platform CLI](/cli) was complemented with a new method, that allows to swap external IP addresses among two nodes or, in case one of them does not have its own Public IP bounded, to transfer an address to another instance. Herewith, this operation can be handled for any nodes within the confines of a single account, i.e. even for the ones, that belong to different environments or run different services. So, in order to accomplish this, just a single line of code should be run:
```bash
~/jelastic/environment/control/swapextips --envName  {env_name} --srcnodeid  {src_node_id} --dstnodeid {dst_node_id}
```

This command requires the following values to be specified within the highlighted parameters:

* ***{env_name}*** - name of the environment, which comprises the server with Public IP you'd like to swap/move
* ***{src_node_id}*** - the exact ID of the node (from the stated environment) the required Public IP is attached to
* ***{dst_node_id}*** - ID of the target node (can belong to any environment at your account)

It will take a few minutes for all the necessary operations to be completed. 

{{%tip%}}**Note:** This process may cause a short-term unavailability of the corresponding Public IP address(es), for approximately ~8-10 seconds.{{%/tip%}}

After that, you'll be shown the details on current IPs of the stated nodes within the method output.

{{%tip%}}**Note:** that while swapping, nodes of the following types will be automatically restarted for the necessary changes to be applied: *GlassFish*, *Apache-PHP*, *Apache-Ruby*, *NGINX-PHP*, *NGINX-Ruby*. This is required for forcing the corresponding services to start listening on new IPs.

Herewith, if operating with *[VPS](https://www.virtuozzo.com/application-platform-ops-docs/vps)* or *[Docker](/dockers-management)* containers, you have to define the necessity of the appropriate instance restart on your own and perform it manually if needed (as it depends on a particular service, running inside). In such a way, you can be sure that the operation of IPs swap won't cause the unrequired downtime of your app.{{%/tip%}}

<a href="/cli" target="_blank" id="php7">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## PHP 7 Support (4.3 / 4.4)
A new major version of PHP server-side scripting language, that takes almost two years for being developed and polished, have been finally released under the **PHP 7** name. Being based on the refactored Zend Engine called *PHPNG* (PHP Next Generation), it shows a significant capacity boost compared to the legacy versions. This allows to increase your PHP applications' performance in up to 2 times just through upgrading the server's engine version it is running on.

Also, the great emphasis was made on the language syntax enhancements - namely, removal of the previous versions' deprecated functionality and simultaneous improvement of language consistency. The detailed information on new features and backward incompatibility issues can be examined at the official [Migrating from PHP 5.6.x to PHP 7.0.x](http://php.net/manual/en/migration70.php) document. 

As for the specifics of PHP 7 integration at the platform, this resulted in the following changes of the supported modules' list for the nodes, running on this engine version:

* ***removed*** - *mysql* (deprecated, use *mysqli* instead)
* ***added*** - *gearman*, *[mongodb](#mongo-php-driver)* (to be used instead of *mongo* one)
* ***currently unavailable for PHP 7*** (will be added upon being developed) - *event*, *intl*, *mysqlnd_ms*, *mysqlnd_qc*, *ncurses*, *solr*, *solr2*, *xcache*

At the platform dashboard, the newest [version of PHP](/php-versions) engine can be found alongside the preceding ones (namely - PHP 5.3, 5.4, 5.5 and 5.6) for being selected during the environment creation or while changing its topology.

<u>*The PaaS 4.4 release*</u> is delivered with the latest PHP *7.0.2* engine, which includes a number of [security and bug fixes](http://www.php.net/ChangeLog-7.php#7.0.2), whilst PaaS 4.3 provides the *7.0.0* PHP version. In addition, the next changes in the in-built PHP modules' list were implemented:

* provided support of the previously unavailable for PHP 7 extensions: *gearman*, *intl*, *solr*, *solr2*, *oauth*, *gmp* (for legacy PHP containers on the top of CentOS 5 distribution)
* with an aim to simplify the migration of the already existing applications to the newest engine version, the rebuilt and adjusted *mysql* module (excluded within the preceding 4.3 version) was appended 
* several new extensions were added for all of the provided PHP versions, namely: *pdo_dblib*, *pdo_oci*, *pdo_odbc*, *readline*, *recode*, *sysvmsg*, *enchant*, *odbc*. See the details [below](#php-modules-44).

<a href="/php-versions" target="_blank" id="mongo-php-driver"><span>More info</span></a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## MongoDB Driver for PHP Update
In order to work with the MongoDB database, PHP requires a special low-level driver, that was recently updated. Thus, in the present 4.3 PaaS release, the new *[mongodb.so](https://github.com/mongodb/mongo-php-driver)* module was added to the pool of extensions, provided for PHP app servers by default. Herewith, the deprecated driver (*[mongo.so](https://github.com/mongodb/mongo-php-driver-legacy)*) still remains available to ensure support of the already launched applications, built on its basis; however, we recommend to consider the latest driver version for your new projects, whilst taking into the consideration that both these modules implement different API, so the existing libraries, that use the legacy driver, should be rebuilt for working with the new one.

Just as before, in order to establish the connection between your PHP application server and MongoDB node, the appropriate module should be [enabled](/connection-to-mongodb-for-php#module) beforehand. This can be performed directly within the dashboard by entering the app server **Configs**, uncommenting the required extension within the **etc > <i>php.ini**</i> file and restarting the node in order to apply new settings.

<a href="/connection-to-mongodb-for-php" target="_blank" id="php-modules"><span>More info</span></a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## PHP Modules List Refactoring (4.3 / 4.4)
The platform provides the most popular and frequently used PHP modules out-of-box, i.e. they are included to the default PHP application servers' builds. Such embedded basis allows to launch most of the applications on fly, without any code changes required. 

However, as the number of extensions is constantly growing, it was decided to shorten the list of active modules to the several most commonly used ones, while the rest of them became disabled by default (i.e. became &ldquo;dynamic&rdquo;). In such a way, the amount of consumed memory at a bare server reduces, being revealed from the unrequired services running, while any of the necessary modules still can be enabled manually in a few easy steps. As a result, all the newly created PHP app server containers will be launched cleaned up, with a lower level of default resource consumption and more flexible extensions' configurability.

* The list of modules, that were removed from the active ones and became dynamic, can be seen {{%accordion title="here."%}}
||||
|---|---|---|
|*bz2.so<br>calendar.so<br>curl.so<br>dba.so<br>dom.so<br>exif.so<br>fileinfo.so<br>ftp.so<br>gettext.so<br>gmp.so<br>iconv.so<br>inotify.so<br>json.so<br>mbstring.so<br>mcrypt.so*|*mongodb.so<br>mysqlnd_ms.so<br>mysqlnd_qc.so<br>mysqlnd.so<br>oauth.so<br>openssl.so<br>pcntl.so<br>pdo_firebird.so<br>pdo_mysql.so<br>pdo_pgsql.so<br>pdo.so<br>pdo_sqlite.so<br>phar.so<br>posix.so<br>pspellso*|*rar.so<br>shmop.so<br>simplexml.so<br>sqlite3.so<br>svn.so<br>sysvsem.so<br>sysvshm.so<br>tidy.so<br>tokenizer.so<br>wddx.so<br>xmlreader.so<br>xmlwriter.so<br>zip.so<br>zlib.so*|
{{%/accordion%}}

{{%tip%}}**Note:** that in case of switching engine version to the newly added [PHP 7](#php7) one for legacy PHP containers (i.e. that were created before 4.3 Platform upgrade and, thus, include old version of the configuration file), you may require to manually re-define the necessary modules from the list above within the ***php.ini*** file. For that, use the line of the following type:  
<i>extension = **{extension_name}**.so</i>
{{%/tip%}}

The complete list of modules (both in-built and dynamic ones) is specified at the dedicated documentation [page](/php-extensions) and within the introductory comments of the **etc > <i>php.ini**</i> configuration file. Further, at the same file, each dynamic extension has its own section, where it can be enabled (through simple uncommenting of the corresponding string) and configured if needed.<a id="php-modules-44"></a>

Physically, all modules are located at the dedicated **modules** server folder, where you can also upload your custom extensions and consequently [activate](/php-extensions#add) them via the same *php.ini* file.

<u>*Within the 4.4 Platform release,*</u> a bunch of new modules were implemented for all of the provided PHP engines, namely: *pdo_dblib.so*, *pdo_oci.so*, *pdo_odbc.so*, *readline.so*, *recode.so*, *sysvmsg.so*, *enchant.so* and *odbc.so*.

Also, the *ZendGuardLoader.so* extension support was added for PHP 5, both of the provided 5.5 and 5.6 versions (previously, it was available for the 5.3 / 5.4 PHP engine only).

<a href="/php-extensions" target="_blank" id="openssl-update">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## OpenSSL Update
**[OpenSSL](https://www.openssl.org/)** is an open source toolkit, that implements Secure Sockets Layer (SSL) and Transport Layer Security (TLS) network protocols. The *openssl* command-line tool is pre-installed at all platform containers and can be used for handling various security-related operations, like public/private keys management, SSL/TLS client-server testing, etc.

Recently, the substantial security update has been implemented for all of the currently supported OpenSSL versions, intended to fix a number of revealed [vulnerabilities](https://www.openssl.org/news/secadv/20151203.txt). Due to this fact, the current platform release provides the throughout update of OpenSSL packages at all containers (including the already existing ones) to their latest versions, provided for CentOS (as it is used as a basic OS template for all platform containers):

* ***for centos 6*** (i.e. for containers, created before [4.0 platform upgrade](/release-notes-40#centos7)) - *openssl-1.0.1e-42.el6.x86_64.rpm*, *openssl-devel-1.0.1e-42.el6.x86_64.rpm*
* ***for centos 7*** - *openssl-1.0.1e-42.el7.9.x86_64.rpm*, *openssl-devel-1.0.1e-42.el7.9.x86_64.rpm*, *openssl-libs-1.0.1e-42.el7.9.x86_64.rpm<a id="nodejs-update"></a>*

{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Node.js Engine Update
**Node.js** is a popular open source cross-platform lightweight runtime, implemented on the top of the Chrome's V8 JavaScript engine. At the platform, Node.js hosting is provided based on the [cartridge packaging model](/cartridges-overview) and offers an easy way to build the highly performant, scalable network applications. 

Commonly, the Node.js packages are dependent on OpenSSL (as it is linked to binaries during build process), which receives some security fixes recently. Thus, with an aim to prevent the possible malfunctions and vulnerabilities use, another [Node.js patch-level update](https://nodejs.org/en/blog/vulnerability/december-2015-security-release-update/) was released, which also includes some other security defects elimination (like threats of service denials and out-of-bounds access)

Striving to ensure the highest level of security for our users, the abovementioned patch was applied to all of the provided Node.js engine versions (namely: 0.10.41, 0.12.9, 4.2.3) within the platform upgrade to 4.3.

<a href="https://www.virtuozzo.com/application-platform-ops-docs/nodejs-hosting" target="_blank" id="software">More info</a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Software Stack Versions
The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.3|PaaS 4.4|
|---|---|---|
|***Tomcat 6***|6.0.44|6.0.44|
|***Tomcat 7***|7.0.62|7.0.62|
|***TomEE***|1.7.1|1.7.1|
|***Jetty 6***|6.1.26|6.1.26|
|***GlassFish 3***|3.1.2.2|3.1.2.2|
|***Java 6***|1.6.0_45|1.6.0_45|
|***Java 7***|1.7.0_79|1.7.0_79|
|***Java 8***|1.8.0_45|1.8.0_45|
|***MariaDB***|5.5.42 / 10.0.17|5.5.42 / 10.0.17|
|***MongoDB 2.6***|2.6.10|2.6.10|
|***MongoDB 3.0***|3.0.3|3.0.3|
|***MySQL***|5.6.24 / 5.7.7|5.6.24 / 5.7.7|
|***PostgreSQL 9***|9.4.4|9.4.4|
|***CouchDB***|1.6.1|1.6.1|
|***nginx***|1.8.0|1.8.0|
|***Maven***|3.3.3|3.3.3|
|***CentOS***|7.1|7.1|
|***Memcached***|1.4.24|1.4.24|
|***Apache***|2.4.6|2.4.6|
|***NGINX PHP***|1.8.0|1.8.0|
|***NGINX Ruby***|1.8.0|1.8.0|
|***PHP 5.3***|5.3.29|5.3.29|
|***PHP 5.4***|5.4.45|5.4.45|
|***PHP 5.5***|5.5.30|5.5.31|
|***PHP 5.6***|5.6.16|5.6.17|
|***PHP 7***|7.0.0|7.0.2|
|***Ruby 1.9.3***|1.9.3-p551|1.9.3-p551|
|***Ruby 2.0.0***|2.0.0-p643|2.0.0-p643|
|***Ruby 2.1***|2.1.5|2.1.5|
|***Ruby 2.2***|2.2.3|2.2.3|
|***Python 2.7***|2.7.10|2.7.10|
|***Python 3.3***|3.3.6|3.3.6|
|***Python 3.4***|3.4.3|3.4.3|
|***Python 3.5***|3.5.0|3.5.0|
|***Node.js***|0.10.41 / 0.12.9|0.10.41 / 0.12.9|
|***Node.js 4***|4.2.3|4.2.3|

{{%right%}}<a href="#impr" id="fix">Back to the list of Improvements</a>{{%/right%}}


## Bug Fixes
In the table below, you can see the list of bug fixes in PaaS 4.3:

{{%bug-fixes title="PaaS 4.3"%}}
**#**|**Description**
---|---
JE-24113|The list of available tags is retrieved not via daemon while a custom Docker image addition
JE-24123|Unability to add custom Docker image in case a maintainer name includes the &ldquo;_&rdquo; symbol
JE-24165|The CentOS 7-based Docker images do not work properly if including the packages, that depend on *systemd-container* daemon
{{%/bug-fixes%}}
{{%right%}}[Back to the top](#back){{%/right%}}