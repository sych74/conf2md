---
draft: false
title: "Release Notes 4.5/4.5.1"
aliases: "/release-notes-45/"
seoindex: "index, follow"
seotitle: "Release Notes 4.5/4.5.1"
seokeywords: ""
seodesc: "In this document, you will find all of the new enhancements and visible changes included in the PaaS 4.5 and 4.5.1."
---

<a id="back"></a>

# Virtuozzo Application Platform 4.5 / 4.5.1

*This document is preliminary and subject to change.*

In this document, you will find all of the new enhancements and visible changes included in the **PaaS 4.5** and **4.5.1** releases:

* [Docker Improvements](#impr)
* [Other Enhancements](#enhance)
* [Bug Fixes](#fix)

For detailed information on using any of the platform's features, please refer to the users’ documentation.

## Docker Improvements

[Container Creation Time Reduction](#docker-creation)  
[Horizontal Scaling Amendment](#docker-scaling)  
[Run Command Validation](#docker-validation)  
[Alpine Linux Template Support](#docker-alpine)  
[Daemon v1.10 Support](#docker-daemon-update)    
[Selection of the Initial Tag Version](#docker-tag-selection)  
<a id="docker-creation" href="#docker-parallel-linking">Parallel Linking of Containers</a>{{%back%}}{{%/back%}}


## Container Creation Time Reduction

[Docker standard support](/dockers-overview) at the platform gains the increasing popularity since the time it was presented almost a year ago, which encourage its further development and improvement. So, within the current release, the massive code refactoring has been done to significantly decrease the Docker images' delivery time (5x faster in average) and, in such a way, to boost appeal of their usage even more.

Each part of the container creation process (from the initial setup method to the concluding detection of the port, required for automatic redirect) was thoroughly examined and adjusted by our developers team to get rid of possible inaccuracies and slowness. This resulted in a number of improvements, such as:

* removal of a set of redundant operations' calls from the code
* erforming configuration of some of required services (like *openSSH*, *logrotate*, *cron*) in background after container creation
* static rebuild of *sed*, *file* and *curl* utilities (i.e. without shared libraries) to eliminate the appropriate delays
* merge of several 'apply config/quotas' calls to one call (net, cpu, mem, disk)
* improval of the logs' gathering process for every performed step


Besides that, a number of other small fixes were applied to ensure the proper compatibility of various images, available at Docker Hub.

As a result, you'll get a completely new experience while leveraging Docker containers, as for now the required dockerized solution can be deployed from both [private registry](/dockers-management#custom) or [public repository](/dockers-management#add) in almost no time.

<a id="docker-scaling" target="_blank" href="/dockers-management">More info</a>
{{%right url="#impr" text="Back to the list of Docker Improvements"%}}{{%/right%}}


## Horizontal Scaling Amendment

In one of the preceding releases, we've implemented the innovative [Docker horizontal scaling](/release-notes-40#dockers-scaling) feature, that allows to operate with multiple Docker-based instances of the same kind within the confines of a single environment stack. Here, the process of scaling for images in application server and load balancer layers initially assumed the complete duplication of the very first node. However, in some cases (e.g. if adding several nodes at once) this could take rather long time, due to the necessity to run a set of consecutive cloning and migration operations sequentially for each new node.

So, to overcome this inconvenience and decrease the time of new Docker instances addition, the above described mechanism was improved through parallelization of multiple containers creation. Also, such an implementation implies that instead of identical nodes addition (i.e. similar to the initial one), each new container will contain the default image, without any custom changes applied. Thereby, the system won't need to clone each piece of the comprised application, getting rid of unrequired delay, while you will need to adjust the newly added app server/balancer containers manually (obviously, only where the changes are actually required).

This allowed to make multiple image copies' creation equally fast regardless of their amount, and even minimize it due to the exclusion of the currently unrequired migration step.

<a id="docker-validation" target="_blank" href="/multi-nodes">More info</a>
{{%right url="#impr" text="Back to the list of Docker Improvements"%}}{{%/right%}}


## Run Command Validation

To keep improving the Docker containers integration to the platform, another adjustment was implemented for the images' [Run Config](/docker-run), that is available at the dedicated Container Settings wizard. For now, the previously unsupported special characters (namely - ***"&"***, ***";"*** and ***">"***) are allowed to be used while specifying the required image start up operations within the **Run Command** field. In such a way, some distinctive run options or several of them at once can be set with the command validation passing correctly.

This resulted in the enlarged amount of official templates, that can be launched without any manual adjustments to be performed before proper running, while you've got the advanced abilities for configuring your already existing Docker containers.

<a target="_blank" id="docker-alpine" href="/docker-run">More info</a>
{{%right url="#impr" text="Back to the list of Docker Improvements"%}}{{%/right%}}


## Alpine Linux Template Support

Within the confines of Docker containers adoption, the platform provides support of the most commonly used OS distributions, that are utilized as a basis for the vast majority of Docker images (the precise list of the currently supported ones can be checked [here](/dockers-overview#get-docker), within the expandable table in a note).

Making the decision to expand these borders and striving to keep pace with the recent demands and usage tendencies, we've gathered and analyzed the statistics of the most frequent installation attempts and appeals. As a result, today we are glad to announce a new operating system for Docker images being supported - **Alpine Linux**.

This OS distribution has bribed its users with provided simplicity, lightweight and security standards. Being built with just *musl libc* and *busybox*, it represents a cleaned up environment for your services, allowing to create really dedicated Docker images. Leveraging Alpine as a base for template ensures efficient utilization of container resources, as it can be run without the unnecessary dependencies, processes and files inside (that, otherwise, are to consume the redundant disk space and cause the overall container slow down). For more information on Alpine characteristics and specifics, please refer to the [official documentation](https://www.alpinelinux.org/about/).

The Alpine-based Docker images' deployment does not differ from that for all other template kinds - see the [Adding Docker Container](/dockers-management) page for the detailed guidance.

[More info](/dockers-overview#get-docker)<a id="docker-daemon-update" target="_blank" href="/dockers-overview#get-docker">More info</a>
{{%right url="#impr" text="Back to the list of Docker Improvements"%}}{{%/right%}}


## Daemon v1.10 Support
The current PaaS 4.5 release also includes a blazingly fast implementation of the just released [Docker 1.10](https://blog.docker.com/2016/02/docker-1-10/) engine support, which brings a bunch of major improvements in security, networking and usability. Among the number of features, described in the official [release notes](https://github.com/docker/docker/releases/tag/v1.10.0), we'll highlight just a few main ones:

* *content addressation* - reference to images and layers via permanent data-related ID (based on security hash)
* *Docker Registry 2.3* - new manifest format and support of shared layers among images
* *push/pull acceleration* - decreased execution time (up to 3x faster) due to parallel layers' processing
* *seccomp profiles* - ensures filtering of complex system calls

Also, a lot of bugs were fixed in order to generally increase the operational stability.
{{%tip%}}**Note:** Apart from being automatically delivered within the confines of platform 4.5.1 upgrade, Docker daemon 1.10 update was additionally applied to all PaaS installations with version *4.2 and higher*.<a id="docker-tag-selection"></a>{{%/tip%}}
{{%right url="#impr" text="Back to the list of Docker Improvements"%}}{{%/right%}}


## Selection of the Initial Tag Version

In order to always provide the best possible Docker solution upon a request, the platform proposes the most recent image version of the chosen template by default. As a standard, the latter release is delivered under the ***latest*** tag, thus it's obvious to automatically substitute this version for each new Docker container. Herewith, you have the ability to additionally define the needed one during installation (as well as change it afterwards through [redeploying](/docker-update#dashboard) a container with another version) or just continue with the default settings stated.

However, sometimes (e.g. in a rare case of the &ldquo;*latest*&rdquo; tag absence), the creation process could end up with a failure if you haven't set the proper tag manually. In connection to this, the logic of initial version selection was adjusted to fetch the available tags list just upon a particular template is picked up. So, in case the &ldquo;*latest*&rdquo; version does not exist, the system will automatically detect and substitute the last committed tag instead (which is usually the newest one).

In addition, this verification allows to instantly identify the unreachable images (e.g. in case of authorization failure or their preceding removal from a registry), just while addition to an environment via wizard. Layers with such Docker containers are to be marked with the exclamation mark (***!***), which displays the additional information upon being hovered upon, while the *Create* button will remain disabled till the problem is solved or broken images are removed from <a id="docker-parallel-linking"></a>topology.
{{%right url="#impr" text="Back to the list of Docker Improvements"%}}{{%/right%}}


## Parallel Linking of Containers

Among other abilities, the embedded *Container Settings* wizard at the platform dashboard provides the functionality of multiple [Docker containers' linking](/docker-links). It allows to quickly establish a proper interaction between them, that is required for building complex dockerized solutions. However, performing this for set(s) of the same-type nodes at once could take the considerable amount of time due to the necessity to run the appropriate operations one-by-one (while otherwise, this would cause the linked images' metadata override).

So, to deal with this issue, the PaaS 4.5 platform upgrade implements addition of a special lock mechanism for an image during the time of link appliance. It ensures that in case of several such processes' calling, they could be performed independently and asynchronously, i.e. in parallel. Beside that, the workflow of links addition was optimized for the images' [run command](/docker-run) for being called only after the linking operation is finished, rather than immediately after the image deployment. In such a way, we get rid of the additional node restart (previously required for the new settings' appliance after linking), so all the services are started only once, just upon a container creation.

[More info](/docker-links)
{{%right%}}<a id="enhance" href="#impr">Back to the list of Docker Improvements</a>{{%/right%}}


## Other Enhancements
[Password Expiration Settings for MySQL (4.5.1)](#password-expiration)  
[Bzip2 Tool Integration (4.5.1)](#bzip2)  
[Software Stack Versions](#software){{%back%}}{{%/back%}}


## Password Expiration Settings for MySQL (4.5.1)
For MySQL servers of 5.7.4 - 5.7.10 versions, a special password lifetime policy was applied, which enforces its automatic expiration after the period of 360 days. This resulted in a number of complaints and disturbances, especially for inexperienced users, as such an unexpected configuration change could lead to occasional project downtime due to inability to establish connection to DB.

Also, this caused a number of inconveniences for the platform users with legacy MySQL containers (created before 4.1 upgrade), as previously the *Reset password* functionality for this server did not imply resetting of the corresponding flag, so the database couldn't be accessed neither with the old password nor with a new one.

Though all of these drawbacks have been fixed (as well as such a password termination workflow was officially removed starting with 5.7.10 MySQL version), it was decided to additionally apply the corresponding adjustment to the MySQL stack template at the platform, in order to avoid similar issues in future. So for now, the default value of *<a href="http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_default_password_lifetime" target="_blank" rel="nofollow">default_password_lifetime</a>* parameter is *0*, which automatically disables the above described expiration policy.

Nevertheless, in case you find this option to be useful in confines of ensuring your data security due to regular changing of access credentials, you still can enable it manually with stating the corresponding setting to any non-zero integer (which defines the number of days after which the current password will be considered outdated and thus should be renewed). To perform this, you need to navigate to the appropriate **etc > <i>my.cnf**</i> file at your MySQL server, edit the *default_password_lifetime* parameter value and restart the node.

<a href="/database-configuration-files#mycnf" target="_blank" id="bzip2">More info</a>
{{%right url="#enhance" text="Back to the list of Other Enhancements"%}}{{%/right%}}


## Bzip2 Tool Integration (4.5.1)

Striving to keep containers lightweight and, at the same time, functional enough, the platform includes only the most useful and commonly used tools into the default stacks builds. Within the PaaS 4.5.1 release, the list of embedded RPM packages for the common container template was extended with a highly requested ***bzip2*** utility. Representing a popular, high-quality and efficient data compressor, it is essential for lots of common operations, like dependencies management and NPM modules' packaging.<a id="software"></a>
{{%right url="#enhance" text="Back to the list of Other Enhancements"%}}{{%/right%}}


## Software Stack Versions

The component templates versions have been updated to their latest versions since the previous release:

|Stack|PaaS 4.5|PaaS 4.5.1|
|---|---|---|
|***Tomcat 6***|6.0.43|6.0.43|
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
|***Centos 6***|7.1|7.1|
|***Memcached***|1.4.24|1.4.24|
|***Apache***|2.4.6|2.4.6|
|***NGINX PHP***|1.8.0|1.8.0|
|***NGINX Ruby***|1.8.0|1.8.0|
|***PHP 5.3***|5.3.29|5.3.29|
|***PHP 5.4***|5.4.45|5.4.45|
|***PHP 5.5***|5.5.31|5.5.32|
|***PHP 5.6***|5.6.17|5.6.18|
|***PHP 7***|7.0.2|7.0.3|
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

{{%right%}}<a href="#enhance" id="fix">Back to the list of Other Enhancements</a>{{%/right%}}


## Bug Fixes


In the table below, you can see the list of bug fixes in PaaS 4.5 and 4.5.1:

{{%bug-fixes title="PaaS 4.5"%}}
**#**|**Description**
---|---
JE-23528|Cron daemon is not started in some Docker containers
JE-23803|Error while trying to install Docker image with CentOS 5
JE-23915|&ldquo;Can not detect OS version&rdquo; error while trying to deploy Docker with Fedora 23
JE-24226|Long Docker images' names are displayed incorrectly while connecting via SSH Gateway
JE-24478|Error while trying to install Docker images under Ubuntu 15.10 OS
JE-24563|Initialization delay for Docker images with empty *Run Command*
JE-24565|Lock process for a service remains running after the service itself was forcibly stopped
JE-24566|Initialization process doesn't start after the first Docker container restart
JE-24838|The *vsftpd* FTP service fails while being restarted with new parameters on CentOS 6
JE-24950|Error while trying to open file/log manager for the cloned Docker-based environment
JE-24994|Incorrect description for the &ldquo;Can not detect OS version&rdquo; error in Task Manager
JE-25012|Improper order of nodes within the *Show Logs* drop down list
{{%/bug-fixes%}}

{{%bug-fixes title="PaaS 4.5.1"%}}
**#**|**Description**
---|---
JE-22766|The Dripstat JPS installation via Marketplace hangs with the *Confirm installation *frame shown in the background
JE-23839|Docker volumes are not mounting if being added before the actual container creation
JE-25179|Custom variables are not replicated to the newly added Docker containers, created upon horizontal scaling
JE-25181|The *file* utility is missed for containers with *oraclelinux:7* image deployed
JE-25182|Absence of the *resolv.conf* file in containers with Ubuntu-based Docker images
JE-25246|Notification on successful environment creation with the *Show Logs* button remains displayed after the environment has been deleted
JE-25247|Wrong validation of Docker repository name with underscore &lsquo;_' in it when adding a custom image
{{%/bug-fixes%}}

{{%right%}}[Back to the top](#back){{%/right%}}