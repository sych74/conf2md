---
draft: false
title: "Release Notes 2.4"
aliases: "/release-notes-24/"
seoindex: "index, follow"
seotitle: "Release Notes 2.4"
seokeywords: "paas, paas release notes, paas version, 2.4 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the platform 2.4 release."
---

# Virtuozzo Application Platform 2.4
*<div id="start">This document is preliminary and subject to change.</div>*

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS 2.4** release:

* [Features](#feat)  
* [Improvements](#impr)  
* [Bug Fixes](#fix)  

<a id="feat"></a>
For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs).


## Features
[Environment Transferring](#a)
[Automatic Horizontal Scaling](#b)
[Load Alerts](#c)  
<a id="a" href="#njs">Node.js Hosting</a>  
[Marketplace Apps Expanding](#d)  


## Environment Transferring
Within the 2.4 PaaS release, we present one more outstanding and often requested feature - environment transferring. Now, you can move any environment you own to another PaaS account . As a result, a new environment's owner will receive it &ldquo;as is&rdquo;, i.e. with all custom configurations and applications deployed.  
This feature can be very useful if, for example, you need to provide your customer with a preconfigured and production-ready application, or just move all of your projects to a new account.
Such an operation is rather simple and works in the following way:

* the first user should initiate the transfer: click **Settings** button next to the desired environment, navigate to the ***Change owner*** section and enter e-mail of a required new owner (second user)
* when transfer form is submitted, the second user will receive an email request for transferring
* after request confirmation, the environment transfers and appears at the dashboard of a new owner. Simultaneously, it disappears from the old owner's dashboard and becomes unshared from all the users that had access to it

Environment transferring is available only for billing users by default. Navigate to the appropriate documentation to find out more details.<a id="b"></a>  
[More info](/environment-transferred)  
{{%right%}}[Back to the list of Features](#feat){{%/right%}}
  


## Automatic Horizontal Scaling
Starting with the current PaaS version (2.4), we provide a new feature of automatic horizontal scaling.  As a result, you can configure automatic addition/removal of application server nodes, depending on the resource usage of your application.  
You can set how many nodes and under what conditions they should be added or removed with a help of tunable triggers. Navigate to the **Settings &gt; Monitoring &gt; Auto Horizontal Scaling** section of a particular environment.  
Here, you can configure two types of triggers (for adding and removing nodes) depending on the CPU or RAM usage. A configured trigger will be applied to the environment's compute node.
The percentage bar is used for defining the levels of cloudlets consumption, which activate the triggers. You also need to define the following parameters in Add and Remove Node panels:

* **For at least:** the period of time the resource usage should be below/above the stated percentage before trigger execution
* **Scale to:** the maximum amount of nodes that can be removed/added in the environment
* **nodes by:** how many nodes should be removed/added at once when trigger is executed


The graph near the percentage bar shows the statistics on the resource consumption level of your environment. It contains information on the application's performance during the last week and can be easily disaggregated by selecting the required period of time from the drop-down list above it.  
You can also receive email notifications for horizontal scaling events. This option is enabled by default (you can disable it). You will receive a corresponding notification each time when any of your triggers is executed. It contains the information on the current cloudlet's consumption level and number of nodes added/removed. In addition, this information can also be seen in the **Settings &gt; Monitoring &gt; Logs** section.  
Detailed information on automatic horizontal scaling can be found in <a href="/automatic-horizontal-scaling" id="c">Automatic Horizontal Scaling</a> document.

[More info](/automatic-horizontal-scaling)  
{{%right%}}[Back to the list of Features](#feat){{%/right%}}
  


## Load Alerts
To monitor your application's load and the amount of resources it requires, you can configure a set of automatic notification triggers. They are executed if the usage of a particular resource type is above/below the stated value (%) during an appropriate time period. As a result, user will get  an email notification  about your application's load change.  
Previously we used an automatic alert system to notify that your environment was running out of resources. Within current release this notification system has been disabled. At the same time all the previous configurations are applied to the new system by means of triggers.

The notification triggers can be configured in the **Settings &gt; Monitoring &gt; Load Alerts** section of the required environment. In the opened tab, select **Add** button to set up a new alert.
Here you should define the values in the following fields:

* **Name**  -name of the notification trigger
* **Node Type** - type of the environment's node (you can apply trigger to any existing node)
* **Whenever** - type of resources that will be monitored by trigger: *Cloudlets (Memory, CPU), Memory, CPU, Storage* (disk space amount), and *Inodes*
* **Is** - condition for trigger invocation/execution based on if the resource consumption should be above/below the stated percentage
* **For at least** - time period before trigger execution during which it remains invoked due to the stated condition

You can set any number of triggers you require.
Note that if the environment is shared with other users, then they will also receive the configured alert notifications. The information on triggers execution history can also be seen in the **Settings &gt; Monitoring &gt; Logs** section.
Detailed information on setting load notification triggers can be found in the <a href="/environment-triggers" id="njs">Load Alerts</a> document.

[More info](/environment-triggers)  
{{%right%}}[Back to the list of Features](#feat){{%/right%}}
  


## Node.js Hosting  

Since we've presented the <a target="_blank" href="/release-notes-22#c">Cartridges packaging format</a> support in PaaS 2.2 release, we continue to improve this functionality and extend the <a target="_blank" href="/supported-cartridges">list of stack templates</a>.  
Current PaaS version also includes Node.js application hosting support. Note that it will be available only if your hosting provider enables it by means of the appropriate cartridge adding.
Default Node.js cartridge provides Node.js 0.10 version with a corresponding application server. Applications can be deployed from *tar*, *tar.gz*, *tar.bz2*, *zip* packages or directly from the GIT/SVN repository across multiple Node.js nodes. In-built NPM package manager is used for Node.js modules installation and automatic code dependencies resolving with the help of [NPM registry](https://www.npmjs.org/).    
Also the support of supervisor is included. It can be used for managing application processes and automatic project's on fly redeploy in case some changes have been made in its code.<a id="d"></a>  

[More info](/deploy-nodejs-archive-url)  
{{%right%}}[Back to the list of Features](#feat){{%/right%}}
  


## Marketplace Apps Expanding
Marketplace is one of the platform's distinguishing features, allowing you to deploy and install previously packaged applications in just a few clicks, including automatic creation of the appropriate environment, with all required nodes and configurations.  
Current PaaS version includes a significant extension of Marketplace content. Together with our partner Softaculous, we've prepared for you almost 100 new packaged applications, ready for automatical installation.  
The list of available applications, divided into the appropriate categories, can be seen at our new [Marketplace site page](https://www.virtuozzo.com/application-platform/marketplace/) or <a href="/marketplace" id="impr">via your dashboard</a> (by clicking the **Marketplace** button in the top toolbar).

[More info](https://www.virtuozzo.com/application-platform/marketplace/)  
{{%right%}}[Back to the list of Features](#feat){{%/right%}}
  


## Improvements
[Ability to Change FTP-addon Password](#i)  
[Java Client Library: Usage Samples](#j)  
[Billing History Button Visibility](#k)  
[Auto-Refill Behavior](#l)  
[New Branding and Mobile App Improvements](#n)  
[Default Cloudlets Limits Update](#o)  
<a href="#ssv" id="i">Software Stack Versions</a>


## Ability to Change FTP-Addon Password
With the 2.4 release, you can change the password of FTP-addon installed at your environment. Using a custom password (instead of one which was automatically generated and sent to you via email) while FTP-addon installation or password resetting, highly improves your application's security.  
Your FTP password can be changed via SSH. [Generate](/ssh-generate-key) an SSH key and [add](/ssh-add-key) it to your account. After that, [access](/ssh-access) the container with the installed FTP-addon via SSH.  
Execute the following command  inside the container:
***sudo /usr/bin/passwd jelastic-ftp***  
Next, just enter and confirm your new password. Now you can use it for accessing your environment via FTP protocol.<a id="j"></a>

[More info](/ftp-ftps-support#pass)  
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}
  


## Java Client Library: Usage Samples
We've prepared a number of samples on using the platorm Java Client Library. With their help, you can automate various actions pertaining to your application lifecycle management, for example: creating an environment, changing its status, deleting, restarting nodes, deploying applications, etc.  
The complete list of samples and instructions on Platform Client Library usage can be found at our [API](https://www.virtuozzo.com/application-platform-api-docs/) documentation, in the **Java Sample** tab at the top panel.<a id="k"></a>  

[More info](https://www.virtuozzo.com/application-platform-api-docs/)  
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}
  


## Billing History Button Visibility
The environments' panel in the dashboard displays various information about existing environments: name, status, deployed applications, current resources usage, etc. While hovering over the particular environment, you can see an additional **Billing history** button which appears in the ***Usage*** column.

After clicking it, the tab with detailed information on the charges applied for this environment resource usage is shown. You can specify the desired start/end dates and the time period interval for billing data viewing.

Now this **Billing history** button is permanently displayed with no need to hover over environment in the list. Such a small but important UI improvement will facilitate billing data access, especially for new users.<a id="l"></a>  
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}
    


## Auto-Refill Behavior
While using platform resources, you can set automatic refilling of the balance not to perform this manually every time when it is required. This can be enabled by using "*Refill my account automatically if my balance falls below {credit}"* option while one of the manual replenishments.

Within current release, the behavior of auto-refill process has been changed. So now, when you enable the abovementioned option, the immediate automatic funding is not performed as it can cause double refillment - automatic and the one you have already initiated manually.

The platform billing system checks your balance at the beginning of every hour (just after applying charges for resource usage) and performs replenishment, only in case there were no orders created (by you or auto-refilling system) within the period of time, stated by hoster.
<a id="n"></a>
In addition, all the payments performed on behalf of auto-refill system are denoted with a special comment in the payment order.

[More info](/billing-system)  
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}
  


## New Branding and Mobile App Improvements
Recently we've launched a new corporate web-site with a complete redesign of our logo and other materials. Our intent is to emphasise our new enterprize style, as well as simplifying your perception and comprehension of all of the benefits you receive, while working with such a unique PaaS.  

Restyling has also affected our IOS Mobile App as an integral part of PaaS. In addition to a new design, the current application version includes several UX improvements and the ability to create a new account.
  
For now, just after opening the app, you'll see a field for entering your email and two buttons: **Login** and **Signup**. By clicking on *Login,* you'll be redirected to the sign in form, with a list of hosting providers the entered email is registered at. Choosing the *Signup* button will lead you to the signup form, with drop-down list of available hosting providers. Just enter your password, confirm it in the pop-up frame, and click *Signup*.<a id="o"></a>
{{%right%}}<a href="#impr">Back to the list of Improvements</a>{{%/right%}}



## Default Cloudlet Limits Update
Within the current platform release, the default cloudlet limits for all the nodes have been changed. This is reflected on the position of Reserved and Scaling Limit cloudlets sliders just after adding a node to the environment.  
We've investigated the optimal resource amount required for correct work of each node, and, as a result, provided the following default values:
  
<table align="center" class="table table-bordered table-condensed table-list"><colgroup><col width="160"><col width="90"><col width="130"><col width="90"><col width="130"></colgroup><tbody><tr><th rowspan="2" style="text-align: center;" align="center" valign="middle"><br>Node Name</th><th colspan="2" style="text-align: center;"><span>Expert Wizard Mode</span></th><th colspan="2" style="text-align: center;"><span>Basic Wizard Mode</span></th></tr><tr><th style="text-align: center; background-color: #3baaff;"><span>Reserved</span></th><th style="text-align: center;"><span>Scaling Limit</span></th><th style="text-align: center;"><span>Reserved</span></th><th style="text-align: center;"><span>Scaling Limit</span></th></tr><tr><td><span>Tomcat, Jetty</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>6</span></td><td style="text-align: center;"><span>2</span></td><td style="text-align: center;"><span>2</span></td></tr><tr><td><span>TomEE</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>8</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;">4</td></tr><tr><td><span>GlassFish</span></td><td style="text-align: center;"><span>6</span></td><td style="text-align: center;"><span>16</span></td><td style="text-align: center;"><span>6</span></td><td style="text-align: center;"><span>6</span></td></tr><tr><td><span>Apache, NGINX</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>2</span></td><td style="text-align: center;"><span>2</span></td></tr><tr><td><span>NGINX-Balancer</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>4</span></td></tr><tr><td><span>Nginx-Ruby</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>6</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>6</span></td></tr><tr><td><span>Apache-Ruby</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>8</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>8</span></td></tr><tr><td><span>Apache-Python</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>8</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>8</span></td></tr><tr><th></th><th style="text-align: center;"></th><th style="text-align: center;"></th><th style="text-align: center;"></th><th style="text-align: center;"></th></tr><tr><td><span>MySQL, MariaDB</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>6</span></td><td style="text-align: center;"><span>2</span></td><td style="text-align: center;"><span>2</span></td></tr><tr><td><span>PostgreSQL, MongoDB</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>8</span></td><td style="text-align: center;"><span>2</span></td><td style="text-align: center;"><span>2</span></td></tr><tr><td><span>CouchDB</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>2</span></td><td style="text-align: center;"><span>2</span></td></tr><tr><th></th><th style="text-align: center;"></th><th style="text-align: center;"></th><th style="text-align: center;"></th><th style="text-align: center;"></th></tr><tr><td><span>Memcached</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>4</span></td><td style="text-align: center;"><span>2</span></td><td style="text-align: center;"><span>2</span></td></tr><tr><td><span>VPS</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>8</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>8</span></td></tr><tr><td><span>Maven</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;"><span>16</span></td><td style="text-align: center;"><span>1</span></td><td style="text-align: center;">16</td></tr></tbody></table>
  
<a id="ssv"></a>
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}
  


## Software Stack Versions
The component templates are remained the same as in the previous release:

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

{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}


## Bug Fixes
In the tables below, you can see the list of bug fixes in PaaS 2.4:

{{%table weight="100 450"%}}
#|Description
---|---
JE-16686|Some packages at Marketplace return "Application not found" error 
JE-16486|Unable to connect via SSH Gateway if public SSH key contains whitespace at the end
JE-16452|User's SSH key, generated with more than 2k bits, is being truncated when stored to the database
JE-16331|Absence of stop/start actions in Jetty 8/9 cartridges' logs
JE-16251|GetList method for CentOS 6 node returns NullPointerException
JE-16250|Enabled debug mode while accessing cartridge container via SSH
JE-16205|While IPTABLES redirecting from 80 to 8080 for Neo4J cartridge with enabled firewall, all the packages from resolver are dropped
JE-16106|GetEngineList method doesn't work with 'all' parameter
JE-16083|Wrong error message while trying to edit/unlink user, that left the collaboration earlier
JE-16076|While connecting via SSH gateway, entering a wrong number in menu leads to the quitting from container
JE-16020|Incorrect ownership of /var/www/webroot directory for NGINX-Ruby node
JE-16011|GetTemplates method doesn't work with 'all' parameter
JE-15981|Unable to open configuration manager after switching to the Java 8 version for legacy containers
JE-15544|&ldquo;No context&rdquo; error after Jetty8 context double renaming
JE-15234|GetProject method should be unavailable after substitutional deploy via DeployApp method
JE-15209|After file renaming an old name is shown in pop-up save confirmation window
JE-15199|After stopping and cloning an environment with Jetty cartridge node it becomes running again
JE-14761|Deployment failure for Maven node if auto update interval is less than period of time deployment process lasts
JE-13435|Upload status in config manager is not changed after notification about file size excess
JE-12736|Wrong behavior while creating a file with the name longer than 256 characters
{{%/table%}}
{{%right%}}[Back to the top](#start){{%/right%}}