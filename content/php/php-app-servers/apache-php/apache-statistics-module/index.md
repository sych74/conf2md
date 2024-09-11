---
draft: false
title: "Apache Statistics Module"
aliases: "/apache-statistics-module/"
seoindex: "index, follow"
seotitle: "Apache Statistics Module"
seokeywords: "statistics, module,"
seodesc: "The statistics (or status) module provides an interface to view your server's statistics."
menu: 
    docs:
        title: "Apache Statistics Module"
        url: "/apache-statistics-module/"
        weight: 60
        parent: "apache-php"
        identifier: "apache-statistics-module.md"
---

# Apache Statistics Module
The **statistics** (or **status**) **module** provides an interface to view your server's statistics. 

### Enabling statistics module
In the platform, the **statistics** module is disabled by default. You can activate this module following the instruction:


* Click **Config** button for your Apache server.
* The required ***status_module*** is loaded by default, so navigate to the **/etc/httpd/conf** folder and open the ***httpd.conf*** file. Add the following code:  
```apache
ExtendedStatus On  
<Location /statistics/>  
SetHandler server-status  
####### Security configuration ####################  
####### Basic auth config should follow here ######  
###################################################  
</Location>  
```

![apache statistics module 1](1.png) 
 **Note:** you can use any other context for your statistics location (in our case we have */statistics/*).

* Save the changes and restart **Apache**.
* Click **Open in browser**. Add the location name to the link.  
*http://{env_name}.{hoster_domain}/{location_name}/* 

 In the opened window the statistics of the server will be shown. 

### Setting up security configuration
* Generate hash from your password. For that you can use any **htpasswd tool** or online service (for example, [http://www.htpasswdgenerator.net/](http://www.htpasswdgenerator.net/)).
* Create simple text file with previously generated hash.
* Click **Config** button for your Apache server.
* Upload the created file to the **/var/www/webroot/ROOT** folder.
* In the **/etc/httpd/conf** folder open the ***httpd.conf*** file.

 Instead of:
```apache
####### Security configuration ####################
####### Basic auth config should follow here ######
###################################################
```
Add the following code:

```apache
AuthName "Statistics area"
AuthType Basic
AuthBasicProvider file
AuthUserFile /var/www/webroot/ROOT/.htpasswd
Require valid-user
```

![apache statistics module 2](2.png) 

* Save the changes and restart **Apache**.
* Click **Open in browser**. Add the location context to the link.</li></ol>*http://{env_name}.{hoster_domain}/{location_name}/* 

 In the opened window you'll be requested to log in with your credentials. Use the credentials you stated while generating the hash to see the statistics of the server.


## What's next?
* [Add Apache Modules](/add-apache-modules/)
* [Apache WebDav Module](/apache-webdav-module/)
* [Name-Based Virtual Host in Apache]()