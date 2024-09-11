---
draft: false
title: "Release Notes 5.3/5.3.2"
aliases: "/release-notes-53/"
seoindex: "index, follow"
seotitle: "Release Notes 5.3/5.3.2"
seokeywords: ""
seodesc: "In this document, you will find all of the new features, enhancements and visible changes included to the PaaS 5.3 and 5.3.2."
---

<a id="back"></a>

# Virtuozzo Application Platform 5.3/5.3.2

*This document is preliminary and subject to change.*
In this document, you will find all of the new features, enhancements and visible changes included to the **PaaS 5.3** and **5.3.2** releases:

* [Features](#features)
* [Improvements](#improvements)
* [Bug Fixes](#bug-fixes)

For detailed information on using any of the platform features, please refer to the [users' documentation](/).


## Features
* [Support of Public IPv6 Addresses](#support-of-public-ipv6-addresses)
* [Multiple Public IP Addresses for a Single Container](#multiple-public-ip-addresses-for-a-single-node-container)
* [Personal Access Tokens for API Request Authentication](#personal-access-tokens-for-api-request-authentication){{%back%}}{{%/back%}}


## Support of Public IPv6 Addresses
The ***v6*** is the most recent version of <a href="https://en.wikipedia.org/wiki/Internet_Protocol" target="_blank" rel="nofollow">Internet Protocol</a> (IP), which is responsible for device identification and defining their location within network, as well as for traffic routing across the Internet. The 6th IP revision is an evolutionary upgrade of IPv4, designed to fulfill the need of more addresses, simplify processing by routers, eliminate NAT (Network Address Translation) issues and private address collisions, etc.

Starting with the present 5.3 release, the platform provides out-of-box support of Public *IPv6*, which can be attached to any container (except for Window-based ones) directly from the [topology wizard](/setting-up-environment). Herewith, the availability of this internet protocol version at a particular Platform depends on hosting provider settings. To check this, refer to the **[Quotas & Pricing](/resource-consumption#3)** frame: 

* **Account Limits** provides information on the *Public IPv6 addresses* availability for your account (note it can be limited during trial period)
* **Pricing &gt; Options** section displays the cost of this feature usage at your Platform

The *6th* internet protocol version can be used on a par with IPv4, providing all the same functionality. In case the address type to use is not specifically indicated (e.g. in JPS packages, add-ons or when creating a VPS node), the *4th* address revision will be used by default.

In order to support IPv6 usage via [API](https://www.virtuozzo.com/application-platform-api-docs/), the following changes were implemented:

* the ***AttachExtIp*** request was deprecated (still remaining valid for backward compatibility)
* a new ***SetExtIpCount*** method was added; operates with two supplementative parameters: ***type*** (*ipv4* or *ipv6*) and ***count*** (number of IPs to add per container - required for the *[multiple IPs](#multiple-public-ip-addresses-for-a-single-node-container)* feature)
* the ***SwapExtIps*** method was limited to be used with IPv4 only

[More info](/public-ipv4)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}

## Multiple Public IP Addresses for a Single Node (Container)
In confines of the PaaS 5.3 upgrade, a possibility to attach multiple Public IPs (both IPv4 and [IPv6](#support-of-public-ipv6-addresses)) to a container was implemented. For example, this allows to run several websites on a single node by using a number of dedicated SSL certificates, associated with the specific IPs.

Multiple IPs can be added in two ways due to the following UI updates:

* the **Public IPv4** and **IPv6** counters were added to topology wizard, so the required IP number can be set right during environment creation / topology adjustment
* each node within the dashboard environment list can be expanded to view and manage all of the attached IP addresses:
    * the total number of *Public IPs* can be adjusted directly from this list using the **Attach/Detach IP(s)** button (separately for IPv4 and IPv6)
    * each particular address can be copied to clipboard or detached from a node with the appropriate buttons

The first Public IP of each type to be added to container will be considered as *primary* one, i.e. will be used for all the outgoing traffic, while the rest of IPs can only receive it. Also, primary IP can only be removed if it is the last public address attached to node.

Other changes due to this feature integration are listed below:

* the ***SwapExtIps*** [API method](https://www.virtuozzo.com/application-platform-api-docs/) was adjusted to allow swap of particular  IPv4 addresses (using the *sourceIp* / *targetIp* parameters pair), as well as all of them at once (*sourceNodeId* / *targetNodeId*)
* upon attaching new IP to the existing node, you receive the appropriate email notification with the list of all its addresses
* the list of assigned IP addresses is displayed in the WAN IP column of the SSH menu while connecting to the Platform via terminal

[More info](/public-ipv4)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Personal Access Tokens for API Request Authentication
Every [platform API](https://www.virtuozzo.com/application-platform-api-docs/) call requires a special *session* parameter to verify whether a user is allowed to execute the appropriate operation. In order to get it, the **Users > Authentication > <i>SignIn**</i> method should be called. However, the obtained *session* value has a short-term validity, being frequently generated anew due to security reasons.

In the current 5.3 PaaS release, an alternative approach of authentication via ***tokens*** was implemented. It is aimed to maintain the security of the sessions-based approach (i.e. ensuring no one else can operate with your account), at the same time extending the API usability greatly. For example, tokens can be used within various scripts (e.g. during application lifecycle automatization) or be shared with co-workers to grant temporary access to some particular account/environments actions. There are a number of specifics to ensure the best user experience:
 
* *permission management* - can be assigned to some specific tasks (each particular token can be allowed to work with a particular API methods only)
* *time to live* - allows to set an expiration date for token
* *multiple tokens* - supports up to 100 different tokens per account
* *renewal possibility* - regenerates lost tokens with the same parameters as original ones
* *prohibited self duplication* - restricts token usage for the *Authentication* API methods (i.e. can not be used to create new or to manage existing tokens)

Below, you can find a list of the appropriate API methods, which were provided for tokens management (check the **Users > Authentication** section of the [documentation](https://www.virtuozzo.com/application-platform-api-docs/) for detailed information): 

* ***CreateToken*** - creates token with the required permissions, expiration day and description
{{%tip%}}**Note:** The exact value (name) of your token will be shown just once and won't be exposed anywhere afterward, so ensure you've saved it before closing method response.{{%/tip%}}
* ***DeleteTokens*** - removes token(s) by ID
* ***EditToken*** - allows to adjust existing token
* ***GetTokenApiList*** - returns a list of all operations, which can be authenticated by token (upon granting the appropriate permissions during creation)
* ***GetTokens*** - displays information on a particular (or multiple) account token
* ***RegenerateToken*** - generates a new name for existing token, while maintaining all other parameters

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right url="#features" text="Back to the list of Features"%}}{{%/right%}}


## Improvements

* [Deployment Manager Improvements](#deployment-manager-improvements)
* [Unlocked Environment Management During Reconfiguration](#unlocked-environment-management-during-reconfiguration)
* [UI/UX Improvements](#uiux-improvements)
* [Environment Variables Management via API](#environment-variables-management-via-api)
* [Removed Deployment Delay Option for Clusterized GlassFish](#removed-deployment-delay-option-for-clusterized-glassfish)
* [Fixes Compatible with Prior Versions](#fixes-compatible-with-prior-versions)
* [Software Stack Versions](#software-stack-versions){{%back%}}{{%/back%}}


## Deployment Manager Improvements

The version control systems (VCS) are extremely popular among developers, as they allow to record and recall changes to your application, as well as manage several different versions of it at once. Thus, to simplify integration of VCS projects into the platform, a special enhancements were applied to the [deployment manager](/dashboard-guide/#deployment).

Starting with the current 5.3 release, it has two tabs - ***Archive*** and ***Git/SVN***. The first one maintains functionality of packages deployment via uploading them from the local machine or providing a direct link to file, while the *Git/SVN* tab is a new implementation. Here, you are able to store VCS projects for a simpler future deploys (i.e. no need to specify your repository detail multiple times).

Use the **Add Project** button on the top of the *Git/SVN* tab of deployment manager to create a new VCS project. Within the opened ***Add Git / SVN Project*** frame, you can specify any custom *Name*, provide *Git* or *SVN* repository details and, if needed, *Use authentication*. When everything is configured, click the **Add** or **Add + Deploy** button. Either way, your project will be stored in manager, but, in the later case, you can immediately deploy it to any environment on your account.
{{%tip%}}**Note:** While deploying project to the Java application server, the [Maven build node](/java-vcs-deployment/) is obligatory required, which, due to this improvement, can be either selected from the list of already existing ones or automatically installed to the deployment target environment.{{%/tip%}}

Apart from that, some changes were applied to the environments list in dashboard. For now, all of the deployed projects are shown under the ***Deployments*** section (former *Context* / *Projects*), which is displayed as the first element within the application server layer. Hover over *Deployments* to get a quick access to the **File**, **URL** and **Git/SVN** deployment dialogs through the same-named buttons.
Also, all of the deployment [API methods](https://www.virtuozzo.com/application-platform-api-docs/) were refactored and gathered under the new **Environment > Deployment** section:

* ***CreateProject*** - creates a project based on sources from a VCS repository (both login/password or ssh key authorization can be used)
* ***EditProject*** - edits the specified project
* ***DeleteProject*** - deletes project from the deployment manager
* ***DeployArchive*** - deploys an application package into the given context (*ROOT* by default)
* ***DeployProject*** - deploys application based on the specified project
* ***GetProjects*** - returns information about the projects
* ***RenameContext*** - renames application by moving it from the old context to a new one
* ***Undeploy*** - removes application from the given context
* ***Update*** - updates project from a VCS repository

[More info](/dashboard-guide/#deployment)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Unlocked Environment Management During Reconfiguration

While applying changes to an environment, it becomes fully locked (i.e. prohibits any other actions) and automatically closes all the associated tabs and dialogs in dashboard. Starting with the current PaaS release, such behaviour was changed, allowing to continue environment management during the ongoing time-consuming operation (e.g. topology adjustment, Docker container redeploy, application deploy, etc.). Herewith, the list of allowed actions varies depending on the exact process in progress, but in the most cases you'll be able to access [file manager](/application-configuration) to adjust configs, as well as to monitor environment via [logs](/view-log-files) and [statistics](/view-app-statistics).

Additionally, tabs and dialogs related to the adjusted environment will no longer be closed (with the exception of the ***Docker container redeploy*** action). Herewith, when frame operates with container, that is being removed, it will automatically switch to another node.

{{%right%}}<a href="#improvements">Back to the list of Improvements</a></p>{{%/right%}}

## UI/UX Improvements

* [Possibility to Download Log Files](#possibility-to-download-log-files)
* [Welcome Tutorial Update](#welcome-tutorial-update)
* [Redesign of the Default HelloWorld Application Example](#redesign-of-the-default-helloworld-application-example)

#### Possibility to Download Log Files
Logs analysis is an important part of web hosting monitoring, which helps to understand system behaviour as well as perform troubleshooting in case of necessity. The platform provides access to server [log files](/view-log-files) directly from dashboard (with the **Log** button next to the required node) for a quick online analysis.

In the 5.3 Platform upgrade, the possibility to download the appropriate files from a Cloud to your local machine was implemented. This could be done using a new **Download** button, which was added to the top pane of the log tab. In such a way, you can explore ***logs*** with any preferable analysis tools or perform any application-specific operations with the obtained file.

[More info](/view-log-files)
{{%right%}}<a href="#improvements">Back to the list of Improvements</a></p>{{%/right%}}

#### Welcome Tutorial Update
Helping new users to get started, the platform welcome tutorial is automatically started upon the very first login to dashboard (although, it can be called manually from the **Help &gt; Tutorial** menu at any time). This short guide provides a summary of the platform main benefits and, consequently, leads through the steps required to create environment and to deploy the first application.

Currently, the first part of the welcome tutorial (i.e. platform overview presentation) was updated to show info on how to build your [application](/paas-components-definition/#application) topology. Additionally, some minor adjustments were applied to the other slides to provide even better clarity on the platform [pricing advantages](/pricing-model).

{{%right%}}<a href="#improvements">Back to the list of Improvements</a></p>{{%/right%}}

#### Redesign of the Default HelloWorld Application Example
All new users on the platform are automatically provided with a simple, lightweight *HelloWorld* application sample. This package can be easily [deployed](/deployment-guide) to any platform-managed app server and is used during a welcome tutorial. In the current 5.3 release, it was upgraded according to the latest platform design. Additionally, the *HelloWorld* package was provided with a number of useful links ([Pricing FAQ](/pricing-model), [SSH Access](/ssh-access), etc.) and some specific URLs based on the used program language (e.g. for PHP - [PHP Settings](/php-application-server-config), [PHP Extensions](/php-extensions)).

{{%right%}}<a href="#improvements">Back to the list of Improvements</a></p>{{%/right%}}

## Environment Variables Management via API
In the present PaaS 5.3 release, two new [API methods](https://www.virtuozzo.com/application-platform-api-docs/) were added to help managing [environment variables](/docker-variables) in Docker containers and dockerized stacks. Both operations were specially designed to work with either single node or a whole layer at once:

* ***AddContainerEnvVars*** - adds variables to the target container(s)
* ***RemoveContainerEnvVars*** - removes variables from the target container(s)

Herewith, variables are provided in the JSON format, which allows to add / remove several of them at a time. If both single container and layer are specified as target for these methods, the *nodeId* parameter will have a higher priority (i.e. only specified container will be updated). Also, in case the *AddContainerEnvVars* method is provided with a variable, which already exists, it will be overwritten using a new value.

[More info](https://www.virtuozzo.com/application-platform-api-docs/)
{{%right url="#improvements" text="Back to the list of Improvements"%}}{{%/right%}}


## Removed Deployment Delay Option for Clusterized GlassFish
Upon deploying a project (either from *archive* or *Git/SVN*) to environment with [multiple application servers](/app-server-scaling), the appropriate ***Sequential deployment delay*** field appears at the confirmation frame. It allows to set a time frame (30 seconds by default) between redeployment of current and subsequent containers in one node group ([layer](/paas-components-definition/#layer)). In such a way, the handled application downtime can be avoided.

Starting with the current 5.3 release, the above-described field won't be shown at the appropriate dialog box, when deploying to the [GlassFish](/glassfish) application server. Here, all the configurations are performed on a master node only, while slaves get these changes through replication.

{{%right%}}<a href="#improvements">Back to the list of Improvements</a></p>{{%/right%}}

## Fixes Compatible with Prior Versions

Below, you can find lists of fixes which except of being implemented within PaaS 5.3 release, have been also integrated to preceding platform versions by means of the appropriate patches:

{{%table3 title="PaaS 5.3"%}}
**#**|**Compatible from**|**Description**
---|---|---
JE-33862|3.3|The *GlassFish 4* application server start page can not be accessed
JE-34125|3.3|Incorrect redirect to admin panel in the *GlassFish 4* application server
JE-33629|4.9|Securing *Redis* nodes with obligatory authentication by default
JE-32086|4.10|Rename the deprecated directives in *Apache Balancer* configuration files to their latest denominations
JE-33022|4.10|Environment topology is not updated in SSH menu after refresh
JE-31847|5.0.5|Incorrect redirect for the *keys* shortcut in a favorites list of the *Tomcat 9* software stack
JE-32103|5.0.5|Insufficient permissions for the logs files in the *HAProxy* load balancer stack
JE-33133|5.0.5|Improper CSS styles for SQL editor in the *phpMyAdmin* panel on MySQL or MariaDB nodes
JE-33615|5.0.5|Tomcat 9 stack can not be accessed via *https* after addition of a custom SSL certificate
JE-34008|5.0.5|Remove old hosts from *Varnish* configs after environment cloning
JE-31900|5.0.6|The dockerized Varnish stack is not properly initiated on startup
JE-33726|5.0.7|The *can't read ssl certificate* error appears, while installing *Let's Encrypt* add-on
JE-33524|5.1|Error, while deploying projects using the platform Maven plugin
JE-33327|5.2|Application can not be connected after being deployed into already existing context on *JBoss* and *WildFly* nodes
{{%/table3%}}

{{%right%}}[Back to the list of Improvements](#improvements){{%/right%}}

## Software Stack Versions
The most notable software stack updates in confines of PaaS 5.3 and 5.3.2 releases is addition of the [OpenJDK](http://openjdk.java.net/) 7/8 engines, which are compatible with the *Tomcat 6/7/8*, *Maven*, *TomEE* dockerized templates. Below, you can check the list of the most accurate software stack versions:

|Stack|PaaS 5.3/5.3.2|
|---|---|
|***Tomcat 6***|6.0.53|
|***Tomcat 7***|7.0.79|
|***Tomcat 8***|8.5.5|
|***TomEE***|7.0.3|
|***Jetty 6***|6.1.26|
|***GlassFish 3***|3.1.2.2|
|***GlassFish 4***|4.1.2|
|***GlassFish 5***|5.0|
|***Payara 4***|4.1.2|
|***Payara 5***|5.0.0.174|
|***Java 6***|1.6.0_45|
|***Java 7***|1.7.0_79|
|***Java 8***|1.8.0_141|
|***OpenJDK 7***|1.7.0.141|
|***OpenJDK 8***|1.8.0.141|
|***MariaDB***|5.5.57 / 10.2.7|
|***MongoDB 2.6***|2.6.11|
|***MongoDB 3.0***|3.4|
|***MySQL***|5.6.37 / 5.7.19|
|***PostgreSQL***|9.5.5|
|***CouchDB***|1.6.1|
|***nginx***|1.10.1|
|***Maven***|3.5.0|
|***Centos 7***|7.2|
|***Memcached***|1.4.24|
|***Apache***|2.4.6-45|
|***NGINX PHP***|1.10.1|
|***NGINX Ruby***|1.12.0|
|***PHP 5.3***|5.3.29|
|***PHP 5.4***|5.4.45|
|***PHP 5.5***|5.5.38|
|***PHP 5.6***|5.6.31|
|***PHP 7***|7.0.21|
|***PHP 7.1***|7.1.7|
|***Ruby 2.2***|2.2.7|
|***Ruby 2.3***|2.3.4|
|***Ruby 2.4***|2.4.1|
|***Python 2.7***|2.7.12|
|***Python 3.3***|3.3.6|
|***Python 3.4***|3.4.5|
|***Python 3.5***|3.5.2|
|***Node.js***|0.10.46 / 0.12.15|
|***Node.js 4***|4.26 / 4.3.0 / 4.5.0|
|***Node.js 5***|5.1.1 / 5.6.0|
|***Node.js 6***|6.5.0|

{{%right%}}[Back to the list of Improvements](#improvements){{%/right%}}

## Bug Fixes

In the table below, you can see the list of bug fixes in PaaS & CaaS 5.3 and 5.3.2:

{{%bug-fixes title="PaaS 5.3"%}}
**#**|**Description**
---|---
JE-3856|Incorrect font size for VPS label in Russian localization
JE-8762|Same ID is assigned to archives, if upload is initiated simultaneously
JE-15525|Add warning message in topology wizard upon removing public IP for node with installed FTP addon
JE-18638|Unhandled error, while trying to edit custom file with insufficient permissions via file manager
JE-22150|Renew icon on the environment remove confirmation frame
JE-22505|Incorrect validation message, while using the '*_*' symbol in environment name 
JE-22934|Some elements of environment settings are displayed incorrectly in a full screen mode
JE-23043|Automatically correct the "*root*" context to "*ROOT*" on Apache PHP
JE-23044|Warning notification is not displayed upon deploying archive with a blank context specified and the *ROOT* context already in use by Git/SVN project
JE-23421|ZDT deployment can be enabled for non *ROOT* context, while called via API
JE-23813|Unhandled error, while building project with incorrect parameters via API 
JE-23878|Sometimes the *Activate* button is not displayed for trial users on the *Quotas & Pricing &gt; Account Limits* frame
JE-25819|Tasks for both add and remove horizontal scaling triggers are displayed, even when just one option was selected
JE-27178|Cloned environment can be hibernated earlier if no actions were performed with it
JE-27867|Sometimes regex expressions are ignored by search in file manager
JE-27965|Configuration files can not be edited on the dockerized stack templates
JE-28058|A mount point record is added even in case the data export operation was failed
JE-28300|Incorrect versions sequence in topology wizard for the *WildFly* stack
JE-28354|The *CouchDB* and *MongoDB* software stacks can not be created
JE-28377|Some buttons are displayed with artifacts upon zooming in browser
JE-28433|The *Import* button should be disabled, when nothing is specified on the *Import &gt; JPS* frame
JE-28635|Environment dependencies should be checked upon scaling in *Storage* nodes
JE-28638|Unhandled error appears, when collaborator tries to bind/swap external domain for environment, where owner does not have the appropriate permissions
JE-28691|Sometimes the engine tabs can be duplicated in topology wizard for trial and beta users
JE-29007|Files are not displayed on the second container upon creating same mount point on two nodes
JE-29079|Some directories from the favorites list are absent on the dockerized containers
JE-29248|Docker volumes are duplicated if specified with a "/" character in the end
JE-29623|The input field for the *balance less than* option in auto-refill section is displayed incorrectly
JE-30761|Public IPs can not be swapped for VPS nodes without internal IP
JE-30766|The wrap lines functionality should work for YAML in the *Import &gt; JPS* frame
JE-30847|The platform welcome tutorial should be interrupted in case of a "*No free hardware*" error
JE-31069|Highlight environment group in a list, when trying to add one that is already attached
JE-31419|Incorrect favourites list in file manager for the dockerized *Varnish* template
JE-31427|Incorrect status label for environment during the *FTP* add-on installation
JE-31430|Incorrect icon in the file manager for files added to / removed from Docker volume
JE-31459|Delay between starting to build a project with Maven node and displaying the building status at dashboard
JE-31466|While connected to it via SSH Gate, container name is displayed incorrectly for dockerized stacks after redeploy
JE-31511|Error, when opening and instantly closing the new project addition frame for the *Apache PHP*, *NGINX PHP* or *Maven* node
JE-31816|MySQL connector is absent on the *Tomcat* and *TomEE* dockerized stacks
JE-31902|Error, while configuring target region in on the environment *Settings &gt; Migration* frame
JE-31922|Unhandled error on dashboard upon creating environment with existing domain name via CLI
JE-32185|Collaborators with a *view* permissions can not download files from the dashboard config manager
JE-32226|Incorrect validation for the URL field, while adding project from Git/SVN
JE-32672|Engines drop-down list should not be displayed in topology wizard, when just one option is available
JE-32746|Directory name should be validated by length, while adding Docker volumes
JE-32911|The *Add to Volumes* button should be disabled for the folders with restricted access
JE-33079|If account limits are insufficient for JPS package installation, it should proceed using the maximum of allowed resources
JE-33080|Mount points can not be configured between two shared environments
JE-33125|The *zip* binaries are absent on the dockerized stack templates
JE-33213|Environment nodes in dashboard should be sorted according to the topology layers order
JE-33214|Not all IP addresses of the SSH Gate are allowed for connection to the *22* port of dockerized stack containers
JE-33215|The core dump files are created, when managing container via file manager
JE-33324|The maximize button should be hidden for the *URL* tab of the *Import* frame
JE-33330|Project update hangs on the Python and Ruby nodes, if the corresponding Git/SVN URL was specified incorrectly
JE-33334|The UDP traffic does not pass through environment endpoints
JE-33338|Docker container settings can not be accessed for the password-protected private Docker images
JE-33341|The post parameters are not working properly, while processing application content or JSON file
JE-33364|The *CouchDB* container can not be created
JE-33380|No response from the platform CLI commands after sign in
JE-33381|The help messages for the Docker *Volumes* and *Links* settings in topology wizard are not displayed
JE-33384|Environments with the platform certified containers can not be exported from the regions based on Virtuozzo 7
JE-33469|Unhandled error, while trying to export files from a shared environment by a collaborator with a *view* permissions
JE-33630|Upon consecutive execution of the restart and redeploy operations, the action log is hidden each time
JE-33641|Balance refills using the WHMCS credit are not accepted
JE-33724|Environments can not be created via platform CLI
JE-33882|The removed environments are displayed in dashboard with the *Creating* status
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.3.2 (build 6)"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-32287|The *Debian 9* OS template is not supported by Docker containers
JE-32973|Docker container can not be created from a dockerfile file with the "*result*" environment variable
JE-33456|After changing an external IP, an NSCD cache provides old address for the prolonged period of time
JE-34040|The *FIREWALL_ENABLED* setting is reset to "*0*" on dockerized containers after redeploy
JE-34315|Deployed projects are not displayed within dashboard after environment cloning
JE-34390|The *Ubuntu 17.10* OS template is not supported by Docker containers
JE-34397|The *Fedora 26* OS template is not supported by Docker containers
JE-34450|Prolonged environment creation time due to the incorrect *MASTER_HOST* variable format on dockerized containers
JE-34490|Admin password is reset while cloning a standalone GlassFish or Payara server
JE-34518|Invalid DNS records are added while creating clustered GlassFish or Payara servers
JE-34721|An unhandled error occurs, when deploying two project into the same context on clustered GlassFish or Payara servers
JE-34756|The */dev/null* folder has inappropriate access permissions and */dev/fd* is missing on the Docker containers based on the *Alpine* OS distribution
JE-34781|Some log files are not displayed for Docker containers in the user dashboard *Logs* section 
JE-34867|The IPv4 address can not be attached via the *attachExtIP* API method when the IPv6 account quota is disabled
JE-34912|Password to admin panel should be set only for the Couchbase cluster master node
JE-35010|Docker containers layer redeployment failure, if it contains just a single node
JE-35159|Docker container can not be redeployed, if one of the image tags has "*result*" in its name
JE-35299|Sometimes, network is not started for Docker containers based on the *Debian 9* OS template
JE-35350|The NSCD cache daemon management operations should be executable with *sudo* permissions on containers
JE-35377|Errors during add-on installation are not displayed at dashboard
JE-35417|API methods for logs management starts containers on the stopped (sleeping) environment
JE-35464|Some placeholders are not displayed within email templates
JE-35490|The "*Cloud account is going to be destroyed*" email notification is sent too often (hourly)
JE-35529|The *Deploy* button is active on the *Git/SVN* deployment form, when the required fields are empty
{{%/table%}}
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.3.2 (build 6)"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-34129|An error message appears for a successful installation of custom SSL on the Apache, Varnish and HAProxy load balancers
JE-34159|Sometimes, incorrect email notification is sent after creating environment without application server
JE-34515|Firewall ruleset is incomplete on the *Storage* node with the *nfsd* filesystem
JE-35160|File upload and archives deploy operations should be forbidden when a Platform Uploader is down 
JE-35317|The *connection time out* error occurs, while mounting from the application server to load balancer
JE-35400|Unhandled error for crossmounts, caused by manual mount operations
JE-35469|Environment with the *PostgreSQL* database of the *9.6* and *10.1* versions can not be created
JE-35494|An error occurred while getting a list of environments for account
JE-35549|During Java projects deployment, the *Maven* build node can not be created automatically on the accounts with cloudlets limit less than 16
JE-35694|The autopay feature should be disabled for account if the last order was not fulfilled
JE-35704|User session for dashboard is not valid for the platform Marketplace
JE-35797|Upon platform Marketplace inaccessibility, the appropriate tab in dashboard is opened for a prolonged period of time
JE-35803|An empty row appears at the bottom of the dashboard upon hovering over region of an environment in the deploying status
JE-35816|Sometimes, the network *bandwidth* limit and a number of *cloudlets* are displayed incorrectly within dashboard
JE-36108|The *centos-jelastic-6-x86_64-ez* package should be maintained to support legacy containers based on CentOS 6
JE-36131|Environments under a heavy load are removed for a prolonged period of time
JE-36175|An error occurs, while trying to remove a big file uploaded to dashboard via URL
JE-36181|Incorrect description for the node(s) restart operation in dashboard Tasks manager
JE-36257|The *Contact Support* form validation restricts appeals in a non-English language
JE-36490|Sometimes, environments with the *Ubuntu VPS* node(s) can not be created
{{%/table%}}
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.3.2 (build 10)"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-30173|Credentials to a private Docker registry can not be adjusted
JE-36464|The *Add-ons* button should be permanently displayed for the load balancer layer
JE-37100|The "*Image not found*" error should provide more details on the occured issue
{{%/table%}}
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 5.3.2 (build 11)"%}}
{{%table weight="100 450"%}}
**#**|**Description**
---|---
JE-35007|An error occurs, while trying to remove the last application server node in environments with the *NGINX* load balancer
{{%/table%}}
{{%/bug-fixes%}}
{{%right%}}[Back to the top](#back){{%/right%}}