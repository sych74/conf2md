---
draft: false
title: "Release Notes 1.9"
aliases: "/users-release-notes19/"
seoindex: "index, follow"
seotitle: "Release Notes 1.9"
seokeywords: "paas, release, java, deploy, server, tomcat,apace, php, application, cloudlet, database, cloud, version"
seodesc: "You can find all the new features, enhancements and visible changes included in the platform 1.9 release: FTP support, TomEE support, MariaDB 10.0.0 support, Caching in NGINX, PBA integration and Pricing System."
---

# Virtuozzo Application Platform 1.9 Release Notes 

*This document is preliminary and subject to change.*

In this document you can find all the new features, enhancements and visible changes included in the **PaaS 1.9** release:

* [New Features](#a)
* [Fixes](#c)

For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs).


## <div id="a">New Features</div> 

* [FTP support](#3)
* [Software stacks versions](#s)
* [TomEE support](#4)
* [MariaDB 10.0.0 support](#x)
* [Caching in NGINX](#n)
* [PBA integration](#5)
* [Pricing System](#6)

Also 1.9 release includes the [PHP improvements](/release-notes-186) and other features added in previous releases.


## <div id="3">FTP support</div>
**File Transfer Protocol (FTP)** is a standard network protocol used to transfer files from one host to another over a TCP-based network.  
For secure transmission that hides (encrypts) the username and password, and encrypts the content, it is used FTP secured with SSL (**FTPS**).  

The platform supports both **FTP** and **FTPS**.

**FTP advantages:**

* fast sharing of files (applications and/or data),
* indirect or implicit use of remote computers,
* shielding from variations in file storage systems among hosts,
* reliable and efficient transfer of data etc.  

To benefit from FTP with the platform, you need to meet two **requirements**:

* to have FTP client installed (for example, FileZilla)
* to switch Public IP for the node in your environment

[More info](/ftp-ftps-support)
<p style="text-align: right;">[Back to the list of New Features](#a)</p>


## <div id="s">Software stacks versions</div>

The component templates are updated to the latest versions:

|Stack|Version|
|---|---|
|***Tomcat 6***|6.0.36|
|***Tomcat 7***|7.0.33|
|***TomEE***|1.5.1|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_38|
|***Java 7***|1.7.0_11|
|***MariaDB***|5.5.28a/10.0.0a|
|***MongoDB***|2.2.2|
|***MySQL***|5.5.29|
|***PostgreSQL***|8.4.14|
|***CouchDB***|1.2.0|
|***nginx***|1.2.6|
|***Maven***|3.0.4|
|***Centos 6***|6.3|
|***Memcached***|1.4.15|
|***Apache***|2.2.15|
|***NGINX PHP***|1.2.6|
|***PHP 5.3***|5.3.21|
|***PHP 5.4***|5.4.11|

[More info](/software-stacks-versions)
<p style="text-align: right;">[Back to the list of New Features](#a)</p>


## <div id="4">TomEE support</div>
Tomcat is  the most popular open source application server among our developers, but for those of you who need more enterprise-ready server, we added [TomEE](http://tomee.apache.org/apache-tomee.html).

[TomEE](http://tomee.apache.org/apache-tomee.html) is an all-Apache stack aimed at Java EE 6 Web Profile certification where Tomcat is top dog.
Apache TomEE provides application developers with the best technology stack that can be deployed to a simple Java EE container. This application server combines several enterprise projects including Apache OpenEJB, Apache OpenWebBeans, Apache OpenJPA, Apache MyFaces and more. In one word: Tomcat + Java EE = TomEE.

TomEE is a full-blown app server, but at the same time it stays simple and avoids architecture overhead. "Less is more" is the philosophy of Apache TomEE. It delivers Java EE 6 Web Profile in the simplest way possible. So, this application server runs without any additional runtime requirements or startup time for larger applications and it's compatible with most of Tomcat-aware and Tomcat-tested tools.

[More info](/tomee)
<p style="text-align: right;">[Back to the list of New Features](#a)</p>


## <div id="x">MariaDB 10.0.0 support</div>
[MariaDB 10.0](https://kb.askmonty.org/en/mariadb-1000-release-notes/) is the development version of **MariaDB**. It is built on the [MariaDB 5.5](https://kb.askmonty.org/en/what-is-mariadb-55/) series with backported features from MySQL 5.6 and entirely new features not found anywhere else. And now it is supported in the PaaS.

MariaDB 10.0.0 is an [Alpha](https://kb.askmonty.org/en/release-criteria/) release targeted on those who might want to test it. 

**Do not use alpha releases on production systems.**  
If you want to try **MariaDB 10.0** in the platorm, just add it as your database while creating your environment.

[More info](/connection-to-mariadb)
<p style="text-align: right;">[Back to the list of New Features](#a)</p>


## <div id="n">Caching in NGINX</div>

Caching in NGINX is the process of storing data in front of web servers. For example, the files a user automatically requests by looking at a web-page can be stored in your NGINX cache directory. When a user returns to a page he's recently looked at, the browser can get those files from the NGINX cache directory rather than the original server, saving time and traffic.

So caching improves performance while accessing to a resource in two ways:

* reduces the access time to the resource by copying it closer to the user.
* increases the resource building speed by reducing the number of accesses. For example, instead of building the homepage of your blog at each request, you can store it in a cache.

With the platform, you can use caching in both NGINX-balancer and NginxPHP server using */var/lib/nginx/cache* directory which was specially created for this purpose.

[More info](/nginx-caching)
<p style="text-align: right;">[Back to the list of New Features](#a)</p>


## <div id="5">PBA integration</div>
Now except **PBAS**, the platform offers one more Parallels billing solutions - **PBA (Parallels Business Automation)**. It is a more full-featured set of capabilities designed for larger hosting services that offer more services or larger-scale deployments.

**Parallels Business Automation** is the leading hosting and cloud services delivery system used by thousands of service providers worldwide, from the largest telecom operators in the world to top hosters and providers of vertical solutions. Parallels automation delivers a combination of great software, thousands of hosting and cloud services, and the expertise to help build a highly profitable business.

Integration with **Parallels Business Automation** provides many abilities, here are just some of them:

* ability to convert user from trial to paid right from the platform dashboard
* ability to refill PaaS account right from the platform dashboard
* more payment methods: except cards and paypal the payment can be made through diners club or through any bank using cash
* payment method management option (add, view,set default, delete)

* autorefill for direct payment plugins (Diners)

[More info](/oba-billing-system/)
<p style="text-align: right;">[Back to the list of New Features](#a)</p>

## <div id="6">Pricing System</div>
The platform offers a flexible system of pricing which is called **hybrid**. At the same time the price can be differentiated due to some specific conditions using the system of **tiers**.

**Hybrid pricing** is a combination of two pricing types when you can state two cloudlet  limits at the same time.

The first limitation is a **reserved** amount of resources. The payment for **reserved cloudlets** does not depend on the amount of actually consumed resources.  It depends on the first stated cloudlet limit. That means that you are going to pay for the stated amount of cloudlets each hour even if the environment consumes less.  
The second limitation is a **dynamic** amount of resources. That means that the first limit can be outsteped for the environment to be able to consume more resources but all extra cloudlets are going to be charged due to another tariff. At the same time instances are scaled automatically up and down, so you only pay for what is actually consumed over reserved amount.

In such a way you can state an appropriate amount of cloudlets you are ready to pay per hour on an ongoing basis and also some standby cloudlet number in case of resource consumption increase.

[More info](/pricing-system-user)
<p style="text-align: right;">[Back to the list of New Features](#a)</p>


## <div id="c">Fixes</div>

The following table lists the bug fixes in PaaS 1.9.

|      #      |Description|
|---|---|
|***JE-186***|702 error appeared while creating environment: Domain [xxxxxxx] not available.|
|***JE-921***|702 error appeared while creating environment: not authenticated (session [undefined] not exist)|
|***JE-4677***|Possibility to turn on HA on PHP tab after choosing NGINX application server|
|***JE-5129***|502 error appeared while replicating GF nodes|
|***JE-5527***|Error while cloning environment: {"result":504, "source":"server", "error": "HTTP transport error","statusText": "Gateway Time-out"}|
|***JE-5889***|Unbind happens after change of topology|
|***JE-5899***|Error while configuring MariaDB: {"result":99,"source": "JEL","error": "java.lang.StringIndexOutOfBoundsException: String index out of range: -1"}|
|***JE-5925***|Permission errors for various tmp directories and cache files after deploying CakePHP using NGINX|
|***JE-5930***|Incorrect days value in "your account destroyed" email notification|
|***JE-5958***|Error while converting through PBAS: "user [276] don't have any access rights to app [...]"}|
|***JE-5966***|Error occurs while deploying: {"result":502, "source":"server", "error": "HTTP transport error", "statusText":"Proxy Error"}|
|***JE-6024***|Error while uploading to the lib folder : java.lang.NullPointerExeption|
|***JE-6053***|Statistics for 2 app-servers is not shown|
|***JE-6065***|Wrong link to "Admin panel" for DB in German-language dashboard|
|***JE-6068***|Maven doesn't pass passwords with special signs (@,#,$)|
|***JE-6118***|Error while simultaneous uploading files to /opt/tomcat/lib: java.lang.NullPointerExeption|
|***JE-6140***|Error while updating context ROOT {"result":17, "error": "java.io.IOException: Timeout while waiting for data."}|
|***JE-6151***|"Your account has been deactivated" instead of "destroyed" in dashboard message for destroyed user|
|***JE-6196***|Error while deploying war archive: {"result":99,"error": "java.lang.NullPointerException", "source":"JEL"}|
|***JE-6206***|Error while trying to access a folder: {"result":2002, "error": "No such file or directory: '/opt/tomcat/temp/fileinstall-...'", "source":"JEL"}|
|***JE-6238***|java.lang.NullPointerException while getting files in file manager|
|***JE-6239***|java.lang.NullPointerException while restarting service|
|***JE-6302***|Wrong message while recovering password if email is stated incorrectly|
|***JE-6374***|NginxPHP doesn't apply settings after restart|
|***JE-6384***|Error while renaming context to "Root(": {"result ":99,"source": "JEL","error":  "java.util.regex.PatternSyntaxException: Unclosed group near index 27\n/opt/tomcat/webapps/ROOT(/*\n ^"}|
|***JE-6407***|Replicating nodes in environment reported an io error {"result":17,"error": "java.io.IOException: Timeout while waiting for data.", "methodName": "replicateNodes"}|
|***JE-6436***|java.lang.NullPointerException while stopping environment|
|***JE-6465***|Incorrect message in German language for suspended user|
|***JE-6792***|Error while uploading several lib-files to app-servers: "java.lang.NullPointerException"|
|***JE-6809***|Custom SSL doesn't work after changing environment topology in environment with GlassFish|
|***JE-6856***|Files don't appear in Config tab after uploading to the environment with Maven|
|***JE-6889***|An error occurs while trying to deploy file via URL: cannot verify SSL certificate|
|***JE-6922***|Dogado's letter "Your PaaS account was deactivated!" contains ${DAYS_COUNT} variable in the text|
|***JE-6957***|Error while trying to create a new file:  java.util.regex.PatternSyntaxException: Illegal repetition near index|
|***JE-7214***|Error while deploying tar.gz: "result":99, "error": "/bin/tar: z: Cannot open: No such file or directory\n/bin/tar: Error is not recoverable: exiting now", "source": "JEL","responses"|
|***JE-7330***|Error while deploying: {"result":99, "error":"mv: cannot move `/var/www/webroot/ROOT//public_html/ .settings' to a subdirectory of itself, `/var/www/webroot/ROOT// public_html/../.settings'"}|
|***JE-7352***|Error after changing topology: "result ":99,"source":"JEL", "error": "java.lang.RuntimeException: java.lang.RuntimeException: can't find env id after move node to [18126]", "params"|
|***JE-7445***|Error while deploying: mv: cannot stat `/var/www/webroot/drrenz//empty/*': No such file or directory|
|***JE-7452***|Error while deploying:  /bin/tar: /var/cache/downloads/: Cannot read: Is a directory /bin/tar: At beginning of tape|
|***JE-7585***|php-fpm.log should contain syntax errors instead of debug staff|
|***JE-7617***|Headers http_host and server_name are not peroxided properly|
|***JE-7648***|Ability to log in to the database without password (MySQL, MariaDB)|
|***JE-7650***|Error while trying to unbind custom domain: {"result": 2322, "error": "domain [www.***.com] not found.", "source":"JEL"}|
|***JE-7690***|SO file uploaded by the user can't be deleted {"result": 99,"error": "rm: cannot remove `/usr/lib64/php/modules/***.so': Permission denied"...}|
|***JE-7707***|Error  while deploy {"result":99, "error": "bad CRC 7891eee3 (should be 447b13ed)"}|
|***JE-7708***|Wrong logic of sending email notifications|
|***JE-7804***|Rename file using "/": {"result" :2333,"error": "Pathes are different.", "source":"JEL"}|
|***JE-7860***|Exceptions are logged in the wrong file of GlassFish server|