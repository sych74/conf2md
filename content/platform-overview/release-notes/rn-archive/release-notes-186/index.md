---
draft: false
title: "Release Notes 1.8.6"
aliases: "/release-notes-186/"
seoindex: "index, follow"
seotitle: "Release Notes 1.8.6"
seokeywords: "release, ,java, deploy, server, tomcat, php, modules, application, cloudlet, cloud"
seodesc: "In this release notes you can find what was changed and added: more Apache2 and PHP modules, NGINX WebDav Module,  PHP accelerators etc."
---

# Virtuozzo Application Platform 1.8.6 Release Notes 

In this document you can find all the new features, enhancements and visible changes included in the **PaaS 1.8.6** release:

* [New Features](#a)
* [Fixes](#c)

For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs).


## <div id="a">New Features</div>

* <u>**More PHP modules**</u>

More PHP modules were added to the system.

Here is a full list of all PHP modules supported by the platform:

|||||
|---|---|---|---|
|bcmath<br>bz2<br>calendar<br>Core<br>ctype<br>curl<br>date<br>dba<br>dom<br>ereg<br>exif<br>fileinfo<br>filter<br>ftp<br>gd<br>gettext<br>gmp|gzip<br>hash<br>iconv<br>Imagick<br>imap<br>json<br>ldap<br>libxml<br>mbstring<br>mcrypt<br>memcache<br>memcached<br>mhash<br>mongo<br>mysql<br>mysqli<br>ncurses|odbc<br>openssl<br>pcre<br>PDO<br>pdo_mysql<br>pdo_pgsql<br>pdo_sqlite<br>pgsql<br>Phar<br>posix<br>Reflection<br>session<br>shmop<br>SimpleXML<br>snmp<br>soap<br>sockets|SPL<br>SQLite<br>sqlite3<br>standard<br>sysvsem<br>sysvshm<br>tokenizer<br>wddx<br>xml<br>xmlreader<br>xmlrpc<br>xmlwriter<br>xsl<br>zip<br>zlib|

[More info](/php-extensions)

* <u>**More Apache2 modules**</u>
    * **Statistics module**  
The **statistics** (or **status**) module provides an interface to view your server's statistics.  
In the PaaS, this module is disabled by default. You can activate this module following the instruction:
        * Click **Config** button for your Apache server. In the **conf** folder open *httpd.conf* file. Add the following code:
        ```nginx
        ExtendedStatus On
        <Location /statistics/>
        SetHandler server-status
        
        ####### Security configuration ####################
        ####### Basic auth config should follow here ######
        ###################################################
        
        </Location>
        ```
        * Save the changes and restart **Apache**.
        * Click **Open in browser**. Add the location name to the link.  
***http://{env_name}.{hoster_domain}/{location_name}/***  
In the opened window the statistics of the server will be shown.
[More info](/apache-statistics-module)
    * **WebDAV module**  
**Web-based Distributed Authoring and Versioning (WebDAV)** which is available in PaaS was invented in order to simplify the way you update websites.
To enable **WebDAV** module on your Apache server:
        * Click **Config** button for the server in your environment.
        * In the **conf** folder open httpd.conf file. Modify *VirtualHost* configuration by adding the following:
        ```apache
        <Directory />
            DAV on
        </Directory>
        ```
Also you can set the permissions you want by modifying directory configurations.
        * Save the changes and restart **Apache.**
Go to any WebDAV client. State there the host and connect to the server. As a result you'll see your files and will be able to configure them, update, add some new etc.  

[More info](/apache-webdav-module)

* ***NGINX WebDav Module***  
**Web-based Distributed Authoring and Versioning (WebDAV)** which is available in PaaS was invented in order to simplify the way you update websites.  
To enable **WebDAV** module on your NGINX server:
    * Click **Config** button for the server in your environment.  
    * In the **conf** folder open *nginx.conf* file. Modify configuration by adding the following strings as it is shown in the picture below:  
*dav_methods PUT DELETE MKCOL COPY MOVE;
dav_ext_methods PROPFIND OPTIONS;*
Using *nginx.conf* file you can set any other configurations for WebDav module.
    * Save the changes and restart **NGINX**.  
Go to any WebDAV client. State there the host and connect to the server. As a result youâÂÂÂÂÂÂÂll see your files and will be able to configure them, update, add some new etc.

[More info](/nginx-webdav-module)

* ***PHP accelerators***  
A **PHP accelerator** is a PHP extension designed to improve the performance of software applications written in the PHP programming language.

The most popular accelerators are built for **php5.4** and **php5.3** platforms:

* APC
* Xcache
* eAccelerator
* ZendGuardLoader (works with PHP 5.3 only)

The accelerators can be activated and configured in the php.ini file of the application server. 

[More info](/php-accelerators)


## <div id="c">Fixes</div>

The following table lists the bug fixes in PaaS 1.8.6.

|#|Description|
|---|---|
|***JE-6374***|NginxPHP doesn't apply settings after restart|
|***JE-6531***|Uploading .bz2  files to Deployment manager (by URL) is not permitted|
|***JE-6682***|In php.ini short_open_tag was set to OFF by default  Now it is set to ON for normal work of applications that has shorten type of tags like "< ? CODE ? >"|
|***JE-6712***|UTF-8 Encoding problem: added parameter URIEncoding="UTF-8" into < Connector ... / > section of file jelastic-ssl.xml|
|***JE-6759***|Wrong order while SSL certificate importing|
|***JE-6792***|"java.lang.NullPointerException" error appears after uploading several lib files to application servers|