---
draft: false
title: "Release Notes 2.5"
aliases: "/release-notes-25/"
seoindex: "index, follow"
seotitle: "Release Notes 2.5"
seokeywords: "paas, paas release notes, paas version, 2.5 release"
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the platform 2.5 release."
---

# Virtuozzo Application Platform 2.5
<a id="back"></a><a id="back"></a><div id="start">*This document is preliminary and subject to change.*</div>

In this document, you will find all of the new features, enhancements and visible changes included in the **PaaS 2.5** release:

* [Features](#feat)  
* [Improvements](#impr)  
* [Bug Fixes](#fix)  

<a id="feat"></a>
For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs).


## Features
[Multi Nodes](#a)
<a href="#b" id="a">Marketplace Usability</a>
[Account Registration](#c)


## Multi Nodes
Horizontal application server scaling is the distinguishing platform feature, provided from the very beginning of its development. It allows you to increase/decrease the number of application servers your environment includes, in the case it is required due to the changes in application's load.

In the current PaaS release (2.5) you've got the ability to scale not just the application server only, but all the nodes in your environment: database, cache instance, VPS, even NGINX-balancer server. The only exception is Maven build-node (as there is no need to scale it).

All newly added nodes are created at different hardware nodes, ensuring even more reliability and high-availability.

You can perform horizontal scaling <a href="/multi-nodes">manually via the Change environment topology wizard</a>, or configure a [set of triggers](/automatic-horizontal-scaling) to automate this operation for your app server, depending on the application's resource consumption.
<a id="b"></a>  
[More info](/multi-nodes)  
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## Marketplace Usability
The complete redesign of our [Marketplace site page](https://www.virtuozzo.com/application-platform/marketplace/) in the previous release was followed by a significant usability improvement of the [Marketplace section](/marketplace) at the platform's dashboard. 

For now, clicking the **Marketplace** button at the top dashboard's panel will open a new tab with a list of more than one hundred applications, which can be automatically installed within an appropriate environment in just one click. 

All of the applications are divided into the corresponding categories, allowing you to choose among the provided solutions depending on your needs. In addition, we've added a Search box above the list of categories, aimed to facilitate the process of searching for a particular application among dozens of available ones.

After you've found the necessary app, simply click the **Install** button and specify the desired environment name. The platform will take care of everything else. In just a few minutes, you'll get a ready-to-work application.  
[More info](/marketplace)<a id="c"></a>
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## Account Registration
Since the current release, you can encounter a new experience while new account creation - obligatory account activation. This is an optional feature, that can be enabled by the chosen hosting provider. 

In this case, after submitting the sign up request, you'll be emailed a special link, which leads to a new activation form. There you should specify and confirm the desired password for your new account. Depending on the hoster's configurations, this form can also contain a captcha widget. 

Once all the required data is entered, submit the form, and you'll be automatically redirected to the platform dashboard, where you can sign in using the credentials you've specified and start working.

Note that dashboard remains inaccessible until you've activated your account, and, in such a way, completed the registration.

See the details in the [Account Registration](/account) document.<a id="impr"></a>  
[More info](/account)
{{%right%}}[Back to the list of Features](#feat){{%/right%}}



## Improvements
[UX Improvements](#d)  
[Environment Aliases](#e)  
[Console Tools](#f)  
[GIT Garbage Collector](#g)  
<a href="#h" id="d">PHP Improvements</a>  
[Software Stack Versions](#i)  


## UX Improvements
We are always mindful of our users and are continually striving to make the platform even more usable. The new PaaS 2.5 version is no exception - it includes a list of amending interface improvements:

* The platform is constantly rapidly developing, increasing the number of features and abilities available. Therefore, we've decided to hide the Basic environment topology wizard mode, as it is not demonstrating the full capabilities of our platform.
* One more important topology wizard improvement includes the addition of counters for both fixed and flexible cloudlet scrollers. It facilitates the process of specifying the desired resources amount in the case its maximum limit is rather high. Values can be stated with the help of arrow buttons or simply by typing the desired cloudlet quantity in the input fields.
* **Settings** button is now available independently on the environment's status, i.e. even if it's stopped or sleeping. Therefore you can always access its three main options: *Account Management*, *Change Owner* and *Info*.
* The **Full screen** button, located at the right top part of the Deployment manager tab, became more noticeable and got the extended label. It allows to expand the tabs panel at the dashboard's bottom to the full view.
* We've also added the direct link to our [API documentation](https://www.virtuozzo.com/application-platform-api-docs/) from the dashboard (**Help** menu in the upper right corner) in order to make it easily accessible.<a id="e"></a>   
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Environment Aliases
Within the current platform version you now have the ability to specify the alternative name (label) for your environment or even for a separate node by simply clicking on the pencil icon (or just double-click) next to the required item. It can be especially convenient in the case of working with several nodes of the same type by virtue of a [multi-nodes](#a) feature.

This alias tag can include spaces and special characters - just type whatever you want to. Such a custom name, set for an environment, defines it in all appropriate lists at the dashboard and SSH console. In addition, all the labels are visible for other users in collaboration and remain attached after an environment's cloning, transferring, etc. Deleting the alias name anytime will return the default value.<a id="f"></a>  
[More info](/environment-aliases)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Console Tools
Accessing your environment via [SSH](/ssh-overview) allows you to remotely manage your servers with the help of an encrypted shell connection. In PaaS 2.5 release, we've added the support of a few most commonly used tools, in order to facilitate this process:

* typing ***mc*** in the console will open the well-known Midnight Commander file manager. Its text interface can be used for convenient browsing through the data structure inside the container, viewing files' content, editing them, etc;
* executed ***nano*** command will open the same-named GPL-licensed text editor;
* finally, we've also integrated ***vim*** editor, which represents the upgraded version of the commonly available *vi* one with a set of extensions and additional features.<a id="g"></a>  
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## GIT Garbage Collector
With the platform, you can easily deploy your project directly from the remote repository, as well as configure its [automatic periodical redeployment](/git-svn-auto-deploy). During each of these type of pulls (or manual ones) some amount of disposable info about the project's version differences and metadata is collected and accumulated in the **.git** folder at your server. After a while, all this temporary data can start to occupy quite a big amount of disc space (especially if your project is rapidly developing). 

That's why we've enabled the automatic compression of the outdated data (older than 2 weeks), connected with GIT activity. These regularly created archives are stored in the same .git folder and can be easily accessed in the case of necessity. In such a way, some amount of memory is saved, increasing your server's performance.<a id="h"></a>  
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## PHP Improvements
Our developers have also added a few modules to the default PHP applications servers' (Apache and NGINX) builds. Here is the list:

* php-tidy
* PDO_FIREBIRD
* do_sqlite
* hp-intl

Enabling the required module with the platform is as easy as adding just one row to the configuration file - see [this](/php-extensions) instruction to learn more.  
<a id="i"></a>[More info](/php-extensions)
{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Software Stack Versions
The component templates are updated to the latest versions in the 2.5 PaaS release:

|Stack|PaaS 2.5|
|---|---|
|***Tomcat 6***|6.0.39 |
|***Tomcat 7***|7.0.55|
|***TomEE***|1.7.0|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***Java 6***|1.6.0_45 |
|***Java 7***|1.7.0_67|
|***Java 8***|1.8.0_20|
|***MariaDB***|5.5.39 /10.0.13|
|***MongoDB***|2.6.4|
|***MySQL***|5.7.4|
|***PostgreSQL 8***|8.4.22|
|***PostgreSQL 9***|9.3.5|
|***CouchDB***|1.6.0|
|***nginx***|1.6.1|
|***Maven***|3.2.3|
|***Centos 6***|6.5|
|***Memcached***|1.4.20|
|***Apache***|2.2.15-31 |
|***NGINX PHP***|1.6.1|
|***NGINX Ruby***|1.6.1|
|***PHP 5.3***|5.3.29|
|***PHP 5.4***|5.4.32|
|***PHP 5.5***|5.5.16|
|***PHP 5.6***|5.6.0|
|***Ruby 1.9.3***|1.9.3-p547|
|***Ruby 2.0.0***|2.0.0-p481|
|***Ruby 2.1.1***|2.1.2|
|***Python 2.7***|2.7.6|
|***Python 3.3***|3.3.5|
|***Python 3.4***|3.4.0|
|***Node.js***|0.1|

<a id="fix"></a>{{%right%}}[Back to the list of Improvements](#impr){{%/right%}}



## Bug Fixes
In the table below, you can see the list of bug fixes in PaaS 2.5:

{{%table weight="100 450"%}}
|**#**|**Description**|
---|---
JE-17579|Automatic horizontal scaling trigger is not activated after the specified amount of time
JE-17517|Incorrect dashboard behaviour if there are more than 1000 archives uploaded to the Deployment manager
JE-17364|Error report appears after the Cloud9 application has been successfully deployed to the NodeJS app server
JE-17230|Ability to enable High Availability for Apache-Ruby application server
JE-17212|# and ## special symbols are not allowed in Tomcat 8 context names
JE-17108|Incorrect Billing history results for "week" and "month" intervals
JE-16457|Errors are not handled when trying to deploy the wrong package to GlassFish
JE-16385|Absence of the appropriate error message when trying to invite the already linked user to the collaboration
JE-15547|Wrong Ruby project's deployment type in the getprojects method response after it has been changed
{{%/table%}}

{{%right%}}[Back to top](#back){{%/right%}}