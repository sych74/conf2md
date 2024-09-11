---
draft: false
title: "Log Files"
aliases: ["/view-log-files/", "/statistic-log-cloud-hosting-in-jelastic/"]
seoindex: "index, follow"
seotitle: "View and Manage Nodes Log Files"
seokeywords: "view logs, application server log, application server logs, node log, manage logs, view log files, logs of application, download logs, database logs, webapps logs, git pull"
seodesc: "Find out how to view your application server logs, as well as log files of databases and other nodes. Manage and download necessary log files via FTP."
menu:
    docs:
        title: "Log Files"
        url: "/view-log-files/"
        weight: 1
        parent: "built-in-monitoring"
        identifier: "view-log-files.md"
---

# View Log Files

Log files are the main source of the most important information regarding what has happened to your environment. For example, any development or testing task requires access to this crucial information.

So, to view your node's logs, follow these steps:

1\. Log into the platform dashboard with your credentials.

2\. Click the **Log** icon for the required node.

![log button](1-log.png)

3\. The logs tab will appear at the bottom of your dashboard. If your environment contains several [nodes of the same type](/horizontal-scaling/), you can choose the one you want to see the logs for in the drop-down list.

![select node to view logs](2-select-node.png)

Using the buttons above the log text you can **Clear** the log or **Refresh** it.
Use **Prev** and **Next** buttons for navigating through the log body if it is large.

{{%tip%}}**Tip:** In order to make the logs monitoring even more convenient, the *Auto refresh* feature is used, which is enabled by default. It makes the currently opened log file to be refreshed every 3 seconds and thus removes any delay or necessity to refresh them manually in order to get the up-to-date information, allowing to track real time processes like installation or updating with ease.

If some issue happens you can disable *Auto refresh* to concentrate on that information rather than on a new one. For that, uncheck the appropriate option in the ***Refresh*** drop-down list above the log output window.

![logs auto refresh](3-auto-refresh.png)

In just the same way, you can enable the *Auto refresh* option again.{{%/tip%}}

4\. Every log file in the folder can be easily deleted directly from the log list. To perform this, hover over the required server log and click the appeared cross button or select it and press **Delete** at the top tools panel.

![delete log files](4-delete.png)

5\. Logs can also be downloaded via FTP. To learn more about the FTP module's installation and usage, see the [FTP/FTPS Support](/ftp-ftps-support/) document.

6\. Here is a list of available log files you can view depending on the node:

Node|Available log files
---|---
Tomcat 6, 7<br>TomEE|manager<br>localhost_access_log<br>catalina<br>host-manager<br>localhost
Jetty|{date}<br>request
GlassFish|{date}<br>request
MySQL<br>MariaDB|mysqld
PosgreSQL|postgresql-{day of week}
CouchDB|couch
MongoDB|mongod
Apache|access-log<br>dummy-host<br>error_log
NGINX PHP|error<br>access php-fpm
NGINX load balancer|tcp_access<br>error<br>error_log<br>access<br>localhost
Memcached|memcached
Node.js|node

{{%tip%}}**Tip:** If you use the remote [GIT/SVN](/deployment-guide/) repository for deploying your application, a new **vcs_update** pull log file is added to your [Maven](/java-vcs-deployment/) node (for Java) or [Apache](/apache-php/)/[NGINX](/nginx-php/) application server (for PHP), which contains the information on your project's building and deploying.

![VCS update log](5-vcsupdate.png){{%/tip%}}


## What's next?

* [View Statistics](/view-app-statistics/)
* [Load Alerts](/load-alerts/)
* [Configuration File Manager](/configuration-file-manager/)