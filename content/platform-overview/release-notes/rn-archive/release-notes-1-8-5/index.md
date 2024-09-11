---
draft: false
title: "Release Notes 1.8.5"
aliases: ["/release-notes-1-8-5/", "/jelastic-release-notes-1-8-5/"]
seoindex: "index, follow"
seotitle: "Release Notes 1.8.5"
seokeywords: "release, java, deploy, server, php, application, cloudlet, database, configuration, version"
seodesc: "In this release essential changes in comparison with the pregoing version are presented: PHP support, Custom SSL, integration with PBAS, TCP load balancing, App packaging ets."
---

# Virtuozzo Application Platform 1.8.5 Release Notes

In this document you can find all the new features, enhancements and visible changes included in the **PaaS 1.8.5** release:

* [New Features](#a)
* [Improvements](#b)
* [Fixes](#c)

For detailed information on using any of the platform's features, please refer to the [users' documentation](https://jelastic.com/docs) (Features).


## New Features

* **<big>PHP support</big>**
    * At the home page of the platform site you can see the announcement on PHP support. Click **Try PaaS for PHP!** to be redirected to a new site page - [http://php.jelastic.com](https://jelastic.com/)  
At this page you can register for the platform PHP beta usage by submitting your email. Also there you can find useful information about the main benefits of PaaS PHP.

    * Main PHP features supported by the platform:
        * <u>PHP has support for most of the web servers today.</u>
This includes Apache and NGINX stacks supported by PaaS.
        * <u>The platform supports different PHP extensions</u> for both Apache and NGINX. Among these extensions we collected the most widely-used modules. Here are just some of them. Also a user can upload his own modules if needed.
        * The platform allows to make all necessary <u>PHP settings</u>.
        * With the platform it is possible to <u>switch between PHP versions</u>.
        * Also there is the automatic function of the <u>whole project deploying</u> in one archive.
    * Note that if PHP feature was switched on during the last visit of the dashboard, the next time you sign in it will be enabled by default.
    * *HelloWorld.war* is a demo application that user can deploy into environment and see that everything works fine. Now it is also available for PHP users. It contains useful links to the data which can assist your further steps.

* **<big>Custom SSL certificates</big>**  
**Custom SSL** certificates are available now on PaaS! This allows a level of security for your domain names that you have never had before. With the platform, hosting applications that need SSL support becomes as easy as one click action. This feature provides ability to upload and use custom certificates to environments. Environment should have custom domain and external IP attached.
[More info](/custom-ssl)
 
* **<big>Integration with PBAS</big>**
This feature allows PaaS to integrate with popular billing system from Parallels - PBAS. **Parallels Business Automation Standard** is the most proven and the industry's preferred, billing and hosting automation solution for managing and scaling small and medium web hosting businesses.
We implemented some new functionality:
    * Reorganized PaaS top level menu so that it would be more attractive and clear for user
    * Implemented ability to convert user from trial to paid right from the platform dashboard
    * Implemented payment method management option (add, view,set default, delete) (e.g. visa, mastercard, paypal, etc.)
    * implemented ability to refill PaaS account right from the platform dashboard
    * implemented ability to refill PaaS account right from the platform dashboard automatically:
        * periodically with a fixed period
        * periodically after reaching some balance level
    * implemented post-pay billing method (customer pays money only the 1st day of each month)
        
* **<big>TCP load balancing</big>**  
From now platform clients can use **TCP** for balancing requests to databases, mail servers and some TCP based applications. Also TCP can be used instead of HTTP if faster balancing is needed. In this case you just need to note that this fastness is achieved through omitting the process of handling requests.  
**TCP load balancing** component receives a connection request from a client application through a network socket. This component decides which node in the environment receives the request.  
When the connection is established, requests from the client application continue to go through the same connection to the chosen node. The application cannot determine which instance is selected.  
The existing connection can be lost only if a problem occurs, such as a temporary network failure or something like that. The next time a request is received, a new connection is created. This connection can go to any instance in the environment.

[More info](/tcp-load-balancing)

* **<big>App packaging</big>**  
With the platform, you can offer your users and clients a fast and powerful hosted solution. Our application packaging gives you rapid and stable multitenancy.  
With **Application Packaging** you have a great possibility to deploy a necessary application (*Cyclos, XWiki, Liferay* or *MagnoliaCMS*) to the platform right from the application home page or [Solutions](https://jelastic.com/partners/isv) page skipping many steps of manual installation. The process is simple. Just a few clicks and you are done.  
[More info](/app-packaging)


## Improvements

* **<big>The notification email is sent only when environment is fully created</big>**  
The notification emails about adding nodes and creating environment are sent only when all the instances are installed and the environment is fully created.

* **<big>One-time link for automatic signing in from welcome emails</big>**  
After registration you get a welcome email. Now this email includes a link using which you can sign in automatically. Follow this link and you'll be redirected to your dashboard and wonât need to enter your credentials. Note that this is one-time link and can be used only once.

* **<big>Permission to edit JAVA_HOME configuration file of application servers</big>**  
There was given a permission to edit files in **JAVA_HOME** folder of Tomcat6, Tomcat7, Jetty and GlassFish containers.

* **<big>Ability to edit NGINX configuration files</big>**  
There was given a permission to edit NGINX configuration files.

* **<big>Pricing section at the main site</big>**  
At the main site there was added a Pricing section. The given menu button redirects to the [Pricing FAQ](https://jelastic.com/pricing) where you can find important useful information about the platform pricing system.

* **<big>Team page update</big>**  
[Team](https://jelastic.com/team) page was updated. Now you can find there information about some other members of PaaS team.

* **<big>Awards page</big>**  
[Awards](https://jelastic.com/about/company) page is added. There you can find the information about Awards and Recognitions of the company.


## Fixes

The following table lists the bug fixes in PaaS 1.8.5.

|      #      |Description|
|---|---|
|***JE-653***|It should be permitted to state the end date in the billing history not further than the current day|
|***JE-695***|The link under environment name needs to be disabled until the environment is created|
|***JE-1717***|Container HDD outreaching|
|***JE-2230***|Sometimes the error can appear while adding the balancer to the environment|
|***JE-2725***|Incorrect error message while stating too long environment name (more than 32 charachters): "We require domain names to be least 5 characters long"|
|***JE-2748***|Building the project is stuck if a user does not specify credentials (login, password) for private git repository|
|***JE-3232***|Incorrect displaying upload archive pop-up |
|***JE-3326***|Error: {"result":8,"source":"hx-core","error":"permission denied"} while trying to delete shared environment (this function must be inactive at all)|
|***JE-3582***|Error "Domain length must be less than 32" appears when the name of the environment  is too long|
|***JE-3589***|Email notification about created environment without compute node shouldnât contain "Environment URL" link|
|***JE-3801***|Error:{"result":17,"source":"JEL","error":"java.io.IOException: Timeout while waiting for data."} The error appears after resetting MongoDB password|
|***JE-4470***|The field in the pop-up with notification about account registration isnât auto-filled with userâs email|
|***JE-4697***|"Contact support" menu command should go first with separator from other Help commands|
|***JE-4753***|Sometimes the error can appear while deploying a file via URL|