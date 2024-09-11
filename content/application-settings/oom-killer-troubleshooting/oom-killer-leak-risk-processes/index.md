---
draft: false
title: "Memory Leak Processes"
aliases: "/oom-killer-leak-risk-processes/"
seoindex: "index, follow"
seotitle: "Memory Leak Processes"
seokeywords: ""
seodesc: "Pay special attention to the processes in this group as to the most probable cause of your out-of-memory issues (sorted based on server role):Load BalancersApplication ServersDatabase ServersCommon..."
menu: 
    docs:
        title: "Memory Leak Processes"
        url: "/oom-killer-leak-risk-processes/"
        weight: 3
        parent: "oom-killer-troubleshooting"
        identifier: "oom-killer-leak-risk-processes.md"
---

# OOM Killer Resolutions: Processes with High Risk of Memory Leak

Pay special attention to the processes in this group as to the most probable cause of your out-of-memory issues (sorted based on server role):

* [Load Balancers](#load-balancers)
* [Application Servers](#application-servers)
* [Database Servers](#database-servers)
* <a href="#common-processes" id="load-balancers">Common Processes for Different-Type Stacks</a>


## Load Balancers

#### Common recommendations

Allocate more RAM to a corresponding node - handled services could just require more memory for normal operability.

#### Related processes

|Process|Resolution|
|---|---|
|*varnishd*|Allocate more RAM to a node - handled services could just require more memory for normal operability<a id="application-servers"></a>|


## Application Servers

Click on points within the list below to view some common recommendations on dealing with memory shortage issues considering used programming language, as well as appropriate resolutions for the most demanding related processes:

* {{%accordion title="Java"%}}

#### Common recommendations

Review the main memory management configurations for your Java machine and, if required, adjust them according to your application needs, e.g.:

*java -Xmx2048m -Xms256m*

where

* ***Xmx*** flag specifies the maximum heap memory that could be allocated for a Java Virtual Machine (JVM)
* ***Xms*** flag defines initial memory allocation pool

Refer to the official documentation for more info on [Java memory management](http://docs.oracle.com/cd/E13150_01/jrockit_jvm/jrockit/geninfo/diagnos/memman.html) system.

{{%tip%}}**Tip:** The platform also implements supplementary automated memory management for Java containers using [Garbage Collector](https://www.virtuozzo.com/company/blog/garbage-collection/). You are able to customize its settings considering your application specifics to avoid OOM issues and gain more efficient memory utilization.

Also, take into consideration, that JVM needs more memory than just heap - read through [Java Memory Structure](https://www.yourkit.com/docs/kb/sizes.jsp) reference to get deeper insights.{{%/tip%}}

#### Related processes

|Process|Resolution|
|---|---|
|*java*|Check the ***xmx***, ***xms***, ***xmn*** parameters of your Java machine and configure them according to your application needs|
{{%/accordion%}}

* {{%accordion title="PHP"%}}

#### Common recommendations

1\. If the problem occurs with the ***httpd*** (***httpd.itk***) service, adjust server memory management parameters as follows:

* check the average amount of RAM, used by each *httpd* instance
* remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file
* decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*

{{%note%}}**Note:** In case you note persistent growth of memory usage per instance (leak), you need to decrease the ***MaxRequestsPerChild*** value (to around 1000-5000).{{%/note%}}

2\. For the ***nginx*** process, connect to your container via SSH and check the size of *php-fpm* instances (e.g. with *ps* or *top* tools):

* if all of them consume ~50-100Mb of RAM, disable [auto configuration](/php-auto-configuration/) and decrease the ***max_children*** parameter
* if instances size varies greatly or is over 200-300Mb, the process is probably leaking - inspect and optimize your code or, alternatively, disable [auto configuration](/php-auto-configuration/) and decrease the ***max_requests_per_child*** parameter

#### Related processes

|Process|Resolution|
|---|---|
|*httpd*|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*lsyncd*|Allocate more RAM to a node - handled services could just require more memory for normal operability|
|*httpd.itk*|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*nginx*|Disable *Jelastic auto configuration* and adjust the [appropriate parameters](/php-auto-configuration/) according to your application specifics|
|*php*|Disable *Jelastic auto configuration* and adjust the [appropriate parameters](/php-auto-configuration/) according to your application specifics|
|*php-fpm*|Disable *Jelastic auto configuration* and adjust the [appropriate parameters](/php-auto-configuration/) according to your application specifics|
|*php-fpm7.0*|Disable *Jelastic auto configuration* and adjust the [appropriate parameters](/php-auto-configuration/) according to your application specifics|
|*php7.0*|Disable *Jelastic auto configuration* and adjust the [appropriate parameters](/php-auto-configuration/) according to your application specifics|
{{%/accordion%}}

* {{%accordion title="Ruby"%}}

#### Common recommendations

Memory leak issues are rather common for Ruby, so, as the first thing to do, consider to inspect and optimize your code. Alternatively, try to increase RAM limit for an instance.

#### Related processes

|Process|Resolution|
|---|---|
|**httpd**|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|***httpd.itk***|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*bundle*|Allocate more RAM to a node - handled services could just require more memory for normal operability|
|*gem*|Allocate more RAM to a node - handled services could just require more memory for normal operability|
|*ruby*|Consider to inspect and optimize your code or add more RAM to a node|
{{%/accordion%}}

* {{%accordion title="Python"%}}

#### Common recommendations

1\. If the problem occurs with the ***httpd*** (***httpd.itk***) service, adjust server memory management parameters as follows:

* check the average amount of RAM, used by each *httpd* instance
* remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file
* decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*

{{%note%}}**Note:** In case you note persistent growth of memory usage per instance (leak), decrease the ***MaxRequestsPerChild*** value (to around 1000-5000).{{%/note%}}

2\. Otherwise, allocate more RAM to a node - the main Python process could just require more memory for normal operability.

#### Related processes

|Process|Resolution|
|---|---|
|*httpd*|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*lsyncd*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
|*httpd.itk*|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*pip*|Can be caused by network issues (so that the download process stucks); otherwise, allocate more RAM to a node - handled application could just require more memory for normal operability|
|*python*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
|*python2.7*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
{{%/accordion%}}

* {{%accordion title="NodeJS"%}}

#### Common recommendations

Restart container to restore the killed process(es). If the issue repeats, allocate more RAM to a node - handled application could just require more memory for normal operability.

#### Related processes

|Process|Resolution
|---|---|
|*lsyncd*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
|*grunt*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
|*node*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
|*npm*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
|*phantomjs*|Allocate more RAM to a node - handled application could just require more memory for normal operability|
{{%/accordion%}}


## Database Servers

Click on the required DB stack within the list below to reveal appropriate common recommendations on coping with OOM issues, as well as resolutions for particular killed processes:

* {{%accordion title="MySQL"%}}

#### Common recommendations

1\. If using ***InnoDB*** engine (embedded since 5.5 MySQL version), check buffers size with the next command:

*SHOW ENGINE INNODB STATUS\G;*

In case of high buffers value (over 80% of total container RAM), reduce size of the allowed pool with the *innodb_buffer_pool_size* parameter in ***/etc/my.cnf*** file; otherwise, allocate more RAM to a server.

2\. Also, check MySQL logs for warnings and recommendations.

#### Related processes

|Process|Resolution|
|---|---|
|*httpd*|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*mysqld*|1. If using ***InnoDB*** engine (by default for MySQL 5.5 and higher), check buffers size with the *SHOW ENGINE INNODB STATUS\G;* command. In case of high buffers value (over 80% of total container RAM), reduce the allowed pool size with the *innodb_buffer_pool_size* parameter in **/etc/<i>my.cnf**</i> file<br>2. Check MySQL logs for warnings and recommendations|
{{%/accordion%}}

* {{%accordion title="MongoDB"%}}

#### Common recommendations

If the problem occurs with the ***httpd*** service, adjust server memory management parameters as follows:

* check the average amount of RAM, used by each *httpd* instance
* remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file
* decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*

{{%note%}}**Note:** In case you note persistent growth of memory usage per instance (leak), decrease the ***MaxRequestsPerChild*** value (to around 1000-5000).{{%/note%}}

#### Related processes

|Process|Resolution|
|---|---|
|*httpd*|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*mongod*|Allocate more RAM to a node - handled services could just require more memory for normal operability|
{{%/accordion%}}

* {{%accordion title="PostgreSQL"%}}

#### Common recommendations

Allocate more RAM to a corresponding node - handled services could just require more memory for normal operability.

#### Related processes

|Process|Resolution|
|---|---|
|**httpd**|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*|
|*postgres*|Allocate more RAM to a node - handled services could just require more memory for normal operability|
{{%/accordion%}}

* {{%accordion title="Redis"%}}

#### Common recommendations

Allocate more RAM to a corresponding node - handled services could just require more memory for normal operability.

#### Related processes

|Process|Resolution|
|---|---|
|*redis-server*|Allocate more RAM to a node - handled services could just require more memory for normal operability|
{{%/accordion%}}


## Common Processes for Different-Type Stacks

#### Common recommendations

Processes in this section can be run and, subsequently, killed within different node types. Thus, OOM resolutions for them vary and depend on a process itself - see the table below to find the appropriate recommendations.

#### Related processes

Process|Stack|Resolution
---|---|---
*httpd*|PHP<br>Ruby<br>Python<br>MySQL<br>MongoDB<br>PostgreSQL|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*
*lsyncd*|PHP<br>NodeJS<br>Python|Allocate more RAM to a node - handled services could just require more memory for normal operability
*httpd.itk*|PHP<br>Ruby<br>Python|1. Check the average amount of RAM, used by each *httpd* instance<br>2. Remove the *Jelastic autoconfiguration mark* within the ***/etc/httpd/httpd.conf*** file<br>3. Decrease ***ServerLimit*** and ***MaxClients*** values according to the formula: *(Total_RAM - 5%) / Average_RAM*
*procmail*|Any|Restart container in order to restore the process
*vsftpd*|Any|Restart container in order to restore the process
*yum*|Any|Restart container in order to restore the process
*cc1*|3rd party|Allocate more RAM to a node - handled services could just require more memory for normal operability
*clamd*|3rd party|Allocate more RAM to a node - handled services could just require more memory for normal operability
*ffmpeg*|3rd party|Allocate more RAM to a node - handled services could just require more memory for normal operability
*firefox*|3rd party|Allocate more RAM to a node - handled services could just require more memory for normal operability
*newrelic-daemon*|3rd party|Restart the main stack service (nginx, tomcat, nodejs, etc.)


## What's next?

* [OOM Killer Troubleshooting](/oom-killer-troubleshooting/)
* [Common Cases](/oom-killer-common-cases/)
* [Non-Leaking Processes](/oom-killer-non-leaking-processes/)
* [Java Garbage Collection](https://www.virtuozzo.com/company/blog/garbage-collection/)
* [PHP Auto Configuration](/php-auto-configuration/)