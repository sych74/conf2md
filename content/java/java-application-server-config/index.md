---
draft: false
title: "Java App Server Configuration"
aliases: "/java-application-server-config/"
seoindex: "index, follow"
seotitle: "Java App Servers Configuration"
seokeywords: "configuration file, server path, configure application, application settings, java settings, configure tomcat, open directory, configure war, jetty configs, glassfish configuration, tomcat cron, configure keys, server lib, configure each node"
seodesc: "Here is a list of all configurations can be applied to the Java application servers (Tomcat, TomEE, Jetty, Glassfish) as well as all files these configurations can be performed in. "
menu:
    docs:
        title: "Java App Server Configuration"
        url: "/java-application-server-config/"
        weight: 40
        parent: "java"
        identifier: "java-application-server-config.md"
---

# Java Application Server Configuration

To perform the necessary configurations, press the **Config** button next to your application server. In the case you have **several application servers** you can configure them together or separately. To do this follow the steps:

1\. Open the drop-down menu at the top of the configuration tab. It includes the list of all of the app servers in your environment.

![java application server config list of app servers](list-of-app-servers.png)

2\. Choose the one you need and make the configurations.

3\. To apply the changes:

* only for the chosen server - click **Save only for current instance** button from drop-down menu
* for all the servers - click **Save**

![java application server config save for current](save-for-current.png)

{{%note%}}**Note**: If you create/rename a file or folder in the Configuration manager, this will be applied only in the list of the chosen node. You can't save this change for all of the app servers available in the environment. If you want to also create/rename the file or folder in the other servers you need to do this manually.{{%/note%}}

<a id="back"></a>

Below you will see the list of the configuration files available for editing in the Java application servers:

* [Tomcat](#tomcat)
* [TomEE](#tomee)
* [GlassFish](#glassfish)
* [Jetty](#jetty)

To get more information on which settings can be changed in the provided config folders, use the appropriate descriptions:

* [server](#server)
* [home](#home)
* [webapps/work](#webapps--work)
* [JAVA_HOME](#java_home)
* [lib](#lib)
* [cron](#cron)
* [keys](#keys)
* [contexts](#contexts)
* [server_lib](#server_lib)
* [apps](#apps)


## SERVER

The main Java servlet container configurations are performed in the files, located in the ***server*** folder.

Using the following config files, you can perform the actions listed below (these are just some examples):

- ***<u>context.xml</u>*** - configure [session replication via Memcached](/replication-memcached/)
- ***<u>web.xml</u>*** - configure [remote access via WebDav](/remote-access-via-webdav/)
- ***<u>server.xml</u>*** - enable [Multiple Domains](/multiple-domains-tomcat-server/)
- ***<u>variables.conf</u>***
  - configure memory settings for your java containers by stating your custom [GC](https://www.virtuozzo.com/company/blog/garbage-collection/), [-Xmx](https://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/jrdocs/refman/optionX.html#wp999528), [-Xms](http://www.oracle.com/technetwork/java/javase/gc-tuning-6-140523.html) parameters (use standard parameters stating each at the new line):
  ```
  -Xmx< size >m
  -Xms< size >m
  ```
  - set your custom [system properties](/java-options-arguments/) for your [Tomcat, TomEE, Jetty](/environment-variables-tomcat-jetty/) or [GlassFish](/custom-environment-variables/):
  ```
  -Dvar1=value1 -Dvar2=value2
  -Dmy.var3=/my/value
  ```
  - configure [JavaAgent interceptor](/javaagent/)
  - enable [remote debugging](/remote-debugging/):
  ```
  -Xdebug
  -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address={port_number}
  ```

{{%note%}}**Note** This file is available only for **Tomcat** and **TomEE** application servers. For configuring a **GlassFish** server, use the *Admin Panel*.{{%/note%}}

![java application server config 9](9.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## HOME

If you need to use any custom files/folders for configuring your application you can download/create them in the **home** directory which is used as a storage in your Java server.

As a result you can make configurations specifying the path to your downloaded/created files in the ***variables.conf*** file (*server* folder).

![java application server config home](home.PNG)

{{%tip%}}**Note:** Although the server's directory, which refers to this folder, can be named *temp* for some servers, it is never automatically cleaned by the platform system.{{%/tip%}}

{{%right%}}[Back to the list](#back){{%/right%}}


## WEBAPPS / WORK

The **webapps** (for Tomcat/TomEE) and **work** (for Jetty) folders are used for storing the unpacked application deployed to the environment.

![java application server config 1](1.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## JAVA_HOME

The **JAVA_HOME** folder contains the java config files and libs. Here, you can edit java settings and upload additional java libraries.

![java application server config java home](java-home.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## LIB

The **lib** folder is used for storing default and uploading custom **jar** libraries.

![java application server config lib](lib.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## CRON

App servers include a **cron** folder with the config file, where cronjobs can be configured.

Detailed information on Cronjob configuration can be found in the [Setting Up a Cronjob](/cron-job/) document.

![java application server config 4](4.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## KEYS

The **keys** directory is used as a location for uploading any private key which is needed for your application.
Generate the key, save it as a simple file and upload to the **key** folder.

It can be used for different cases by simply stating the path to your key:

```
/var/lib/jelastic/keys/{key_file_name}
```

![java application server config java key](java-key.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## CONTEXTS

The **contexts** folder contains XML config files for each deployed context. All of these files are open for editing.

![java application server config context](context.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## SERVER_LIB

The **server_lib** folder is the GlassFish config directory with all available server libraries.

![java application server config serverlib](serverlib.png)

<p align="right"><a href="#app_server">Back to the list</a></p>


## APPS
The **apps** TomEE folder is used for storing the unpacked EE application deployed to the environment.

![java application server config apps](apps.png)

{{%right%}}[Back to the list](#back){{%/right%}}


## Tomcat

Folder|File|Path
---|---|---
conf|catalina.policy<br>catalina.properties<br>context.xml<br>jaspic-providers.xml<br>jaspic-providers.xsd<br>jelastic-ha.xml<br>jelastic-ssl.xml<br>logging.properties<br>server.xml<br>tomcat-env.sh<br>tomcat-users.xml<br>tomcat-users.xsd<br>variables.conf<br>web.xml|/opt/tomcat/conf
temp||/opt/tomcat/temp
webapps||/opt/tomcat/webapps
latest||/usr/java/latest
lib||/opt/tomcat/lib
cron|tomcat|/var/spool/cron
keys||/var/lib/jelastic/keys

{{%right%}}[Back to the list](#back){{%/right%}}


## TomEE

Folder|File|Path
---|---|---
[server](#server)|catalina.policy<br>server.xml<br>catalina.properties<br>tomcat-users.xml<br>context.xml<br>web.xml<br>variables.conf<br>logging.properties<br>tomee.xml<br>system.properties|/opt/tomcat/conf/
[home](#home)||/opt/tomcat/temp
[webapps](#webapps--work)||/opt/tomcat/webapps
[apps](#apps)||/opt/tomcat/apps
[JAVA_HOME](#java_home)||/usr/java/default
[lib](#lib)||/opt/tomcat/lib
[cron](#cron)|tomcat|/var/spool/cron
[keys](#keys)||/var/lib/jelastic/keys

{{%right%}}[Back to the list](#back){{%/right%}}


## GlassFish

Folder|File|Path
---|---|---
[server](#server)|default-web.xml<br>domain.xml<br>domain.xml.bak<br>domain.xml.orig<br>local-password<br>logging.properties<br>logging.properties.orig<br>login.conf<br>server.policy<br>sun-acc.xml<br>wss-server-config-1.0.xml<br>wss-server-config-2.0.xml|/opt/glassfish3/glassfish/domains/<br>domain1/config
**gfcluster-config** (in *server* folder)|logging.properties|/opt/glassfish3/glassfish/domains/<br>domain1/config/gfcluster-config
[home](#home)||/opt/glassfish3/temp
[JAVA_HOME](#java_home)||/usr/java/latest
[server_lib](#server_lib)||/opt/glassfish3/glassfish/lib/
[cron](#cron)|glassfish|/var/spool/cron
[keys](#keys)||/var/lib/jelastic/keys

{{%right%}}[Back to the list](#back){{%/right%}}


## Jetty

Folder|File|Path
---|---|---
[server](#server)|jdbcRealm.properties<br>jetty-ajp.xml<br>jetty-bio.xml<br>jetty-jaas.xml<br>jetty-jmx.xml<br>jetty-logging.xml<br>jetty-plus.xml<br>jetty-rewrite.xml<br>jetty-setuid.xml<br>jetty-sslengine.xml<br>jetty-ssl.xml<br>jetty-stats.xml<br>jetty.xml<br>login.conf<br>login.properties<br>realm.properties<br>spnego.properties<br>variables.conf<br>webdefault.xml|/opt/jetty/etc
[home](#home)||/opt/jetty/home
[contexts](#contexts)||/opt/jetty/contexts/
[work](#webapps--work)||/opt/jetty/work
[JAVA_HOME](#java_home)||/usr/java/latest
[lib](#lib)||/opt/jetty/lib
[cron](#cron)|jetty|/var/spool/cron
[keys](#keys)||/var/lib/jelastic/keys</td></tr></tbody></table>

{{%right%}}[Back to the list](#back){{%/right%}}


## What's next?

* [Tomcat Server](/tomcat/)
* [TomEE](/tomee/)
* [Jetty](/jetty/)
* [GlassFish](/glassfish/)
* [Database Configuration](/database-configuration-files/)