---
draft: false
title: "Release Notes 1.8.2"
aliases: "/release-notes-1-8-2/"
seoindex: "index, follow"
seotitle: "Release Notes 1.8.2"
seokeywords: "database, server, tomcat, host, java, ajax ssh, glassfish, configuration"
seodesc: "In this document you can find all the new features, enhancements and visible changes included in the PaaS 1.8.2 release"
---

# Virtuozzo Application Platform 1.8.2 Release Notes

In this document you can find all the new features, enhancements and visible changes included in the **PaaS 1.8.2** release:

* [New Features](#a)
* [Changes](#b)
* [Fixes](#c)

For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs) (Features).


## <div id="a">New Features</div>

* **<big>Elastic VDS with root access</big>**
This feature lets the user have his own *dedicated virtual server* where the user can install his own software and perform mostly any system configurations and modifications which are needed. After creating VDS node user receives email with SSH credentials to log in remote secured shell. VDS template doesn't have any huge applications preinstalled, only packet manager configured to use most of the popular repositories. Any software installation on VDS should be done by user. Also VDS has light build-in Ajax SSH server running. This lets the user connect secured shell directly using web-browser. 
[More info](/VDS).

* **<big>Memcached node</big>**
*Memcached* is a general-purpose distributed memory caching system. It is often used to speed up dynamic database-driven websites by caching data and objects in RAM to reduce the number of times an external data source (such as a database or API) must be read.
[More info](/memcached/).

* **<big>Ability to create environment without compute node</big>**
This feature gives an opportunity to create environments without application logic nodes. For example one container with SQL or NoSQL database, or one VDS node etc.

* **<big>Baloon system</big>**
The prompts system, which allows users quickly to figure out with the dashboard interface.


## <div id="b">Changes</div>

* **<big>Topology UX modification (Simple/Expert modes)</big>** 
This feature provides the users with more flexible and simple way to create environments. New wizard now has two modes : *Basic* and *Expert*. In Basic mode you don't need to think about complex environment topology, you can just select database and application server. That will be quite enough for the first-time user experience. In Expert mode you can select and cofigure balancing, application logic, storage (cache, SQL and NoSQL nodes) and addons (build node, VDS and SSL).
[More info](/dashboard-guide/).

* **<big>Redesigned Hello World application</big>** 
*HelloWorld.war* is a demo application that user can deploy into environment and see that everything works fine. Now it is not so boring like "Hello World!" text. It tells user what to do next and has social buttons to spread the World about the platform.

* **<big>Sing-up block on blog</big>** 
Ability for users to register in the [blogs](https://www.virtuozzo.com/company/blog/) pages.

* **<big>Update templates to the latest versions</big>** 
The component templates are updated to the latest versions:

|||
|---|---|
|***Tomcat 6***|6.0.35|
|***Tomcat 7***|7.0.28|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2|
|***Java 6***|1.6.0u26|
|***Java 7***|1.7.0|
|***MariaDB***|5.5.25|
|***MongoDB***|2.0.5|
|***MySQL***|5.5.25|
|***PostgreSQL***|8.4.12|
|***CouchDB***|1.2.0|
|***nginx***|1.2.0|
|***Maven***|3|
|***Centos 5***|5.8|
|***Memcached***|1.4.13|

[More info](/software-stacks-versions).


## <div id="c">Fixes</div>

The following table lists the bug fixes in PaaS 1.8.2.

|      #      |Error|Description|
|---|---|---|
|***JE-1200***|{"result":99, "error":"sh: /opt/tomcat /conf  /tomcat-users.xml: Permission denied", "source":"JEL", "out":""}|Error while trying to edit Tomcat's configuration file: tomcat-users.xml|
|***OB-743***|psql: FATAL: no pg_hba.conf entry for host X.X.X.X|Missing parameter in pghba.conf file caused error during remote connection to PostgreSQL server using public IP.|
|***JE-1324***|{"result":0, "responses": [{"result":99,"error": "bash: -c: command not found", "source": "JEL","out":"", "nodeid":66008}]}|Using not direct link to file while .war(.ear) files uploading.|
|***JE-1406***|{"result":99,"error":"svn: OPTIONS of 'https:// dmitryshnyrev%40bitbucket.org /DmitryShnyrev/quiz': Could not resolve hostname dmitryshnyrev%40bitbucket.org': Host not found (https://dmitryshnyrev%40bitbucket.org)"}|Error appeared while trying to build git project via https://. <br>At that moment git projects' building was available only  via git:// |
|***JE-1406***|{"result":99, "error":"error: SSL certificate problem, verify that the CA cert is OK. Details: \nerror: 14090086:SSL routines: SSL3_GET_SERVER_CERTIFICATE: certificate verify failed while accessing https://......: HTTP request failed"}|Error appeared while trying to build git project via https://.<br>At that moment git projects' building was available only  via git://|
|***JE-2226***|{"result":99, "error": "sh: /opt /glassfish3 /glassfish /domains/domain1 /config  /domain.xml:  Permission denied", "source": "JEL", "out":""}|There was a restriction to edit the mentioned file under GlassFish configuration|
|***JE-2046***|{"result":99,"source":"JEL"}|Error while resetting passwords for Databases or Glassfish instances|
|***JE-1600***|External libs are not accessible from app deployed to Glassfish|External libs are not accessible from app deployed to Glassfish|
|***JE-160***|Maven: Create SVN project -&gt; change to Git project, build it and got error "fatal: Not a git repository: '/root /maven /projects_src  /123/.git'"|This error took place while changing project type from SVN to GIT and then building this project|