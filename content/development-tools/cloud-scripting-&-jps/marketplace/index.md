---
draft: false
title: "Marketplace"
aliases: ["/marketplace/", "/app-packaging/"]
seoindex: "index, follow"
seotitle: "Application Marketplace"
seokeywords: "application, add-on, marketplace, application deploy, add-on deploy, application marketplace, install application, automatic deployment, packaged solutions, categorized solutions, jps packages, application auto-deploy, automatic application installation"
seodesc: "Find out about the platform Marketplace - a library of the automated deployment solutions for the most popular applications. Install these pre-configured ready-to-work solutions in a few clicks without necessity to perform any manual configurations."
menu:
    docs:
        title: "Marketplace"
        url: "/marketplace/"
        weight: 40
        parent: "cloud-scripting-&-jps"
        identifier: "marketplace.md"
---

# Marketplace

Platform Marketplace is a library of the most popular and requested applications, which are configured and optimized in the most beneficial way via the platform [Packaging Standard](/jps/). These packaged solutions can be installed automatically directly from the dashboard, skipping many steps of manual deployment and optimization.

You can access the **Marketplace** via the appropriate button at the top-left corner of the dashboard.

![packaged solutions marketplace](01-packaged-solutions-marketplace.png)

Within the opened section, you can find a list of categorized solutions to install new **Applications** from scratch and configuration **Add-Ons** to update your existing environments. Currently, the platform manages and maintains the following JPS packages, providing them for one-click installation at all platforms:

<table>
    <colgroup><col width="200"><col width="200"><col width="200"></colgroup>
    <tbody>
        <tr><th colspan="3" style="vertical-align: middle; padding: 10px 9px; text-align: center; background-color: #3baaff; font-size: large;">Applications</th></tr>
        <tr>
            <td style="background-color: #eceffd94;"><ul>
                <li>Alfresco</li>
                <li>Ametys</li>
                <li>Auto-Scalable Couchbase CE Cluster</li>
                <li>Auto-Scalable GlassFish Cluster</li>
                <li>Auto-Scalable Magento Cluster v2</li>
                <li>Auto-Scalable Spring Boot Cluster</li>
                <li>Backup Storage</li>
                <li>Cyclos 4 PRO</li>
                <li>DevOps Lab - GitLab Server</li>
                <li>DjangoCMS</li>
                <li>Docker Engine CE</li>
                <li>Docker Swarm Cluster</li>
                <li>DokuWiki</li>
                <li>DropWizard Fat Jar Builder</li>
                <li>Drupal</li>
                <li>Eclipse Mosquitto</li>
                <li>Eclipse Vert.x Fat Jar Builder</li>
                <li>Eclipse Vert.x Thin Jar Builder</li>
                <li>Ghost</li>
                <li>Gitblit</li>
                <li>IOTA Node</li>
                <li>Jenkins DevOps Pack</li>
                <li>Jitsi Video Conferencing</li>
            </ul></td>
            <td><ul>
                <li>Joomla</li>
                <li>Kubernetes Cluster</li>
                <li>Laravel</li>
                <li>Liferay</li>
                <li>LimeSurvey</li>
                <li>Magento Standalone</li>
                <li>Magnolia CMS</li>
                <li>Maian Cart</li>
                <li>MariaDB Multi-Region Cluster </li>
                <li>MariaDB Multi-Region Galera Cluster </li>
                <li>Mattermost Chat Service</li>
                <li>Minio Cluster</li>
                <li>MODX</li>
                <li>MongoDB Replica Set</li>
                <li>Moodle</li>
                <li>Multi-Region Redis Cluster </li>
                <li>Multi-Region WordPress Cluster v1 (Alpha)</li>
                <li>Multi-Region WordPress Standalone</li>
                <li>MySQL/MariaDB/Percona Cluster</li>
                <li>Nexus Repository Manager</li>
                <li>Node-RED Dev</li>
                <li>Odoo Community Edition</li>
                <li>Open Liberty in Kubernetes</li>
            </ul></td>
            <td><ul>
                <li>OpenCart</li>
                <li>OpenCMS</li>
                <li>OpenVPN Access Server</li>
                <li>osTicket</li>
                <li>ownCloud</li>
                <li>Plesk Hosting Platform</li>
                <li>PostgreSQL Multi-Region Cluster</li>
                <li>PostgreSQL Primary-Secondary Cluster</li>
                <li>PrestaShop</li>
                <li>qdPM</li>
                <li>Redis cluster</li>
                <li>Redmine</li>
                <li>Spring Boot Fat Jar Builder</li>
                <li>Spring Boot Thin Jar Builder</li>
                <li>Tomcat/TomEE cluster with High Availability</li>
                <li>Traffic Distributor</li>
                <li>WebMail Lite</li>
                <li>WildFly Continuous Deployment</li>
                <li>WildFly Managed Domain Cluster</li>
                <li>WordPress Cluster Kit v2</li>
                <li>WordPress Standalone Kit</li>
                <li>XWiki</li>
            </ul></td>
        </tr>
    <tbody>
</table>

<table>
<colgroup><col width="200"><col width="200"><col width="200"></colgroup>
<tbody>
    <tr><th colspan="3" style="vertical-align: middle; padding: 10px 9px; text-align: center; font-size: large; background-color: #3baaff;">Add-Ons</th></tr>
    <tr>
        <td style="background-color: #eceffd94"><ul>
            <li>Database Backup/Restore Add-On</li>
            <li>Database Cluster Recovery</li>
            <li>Database Corruption Diagnostic</li>
            <li>Env Start/Stop Scheduler</li>
            <li>File Synchronization</li>
            <li>Git-Push-Deploy Add-On</li>
        </ul></td>
        <td><ul>
            <li>HTTP/3 Premium CDN<i><b>*</b></i></li>
            <li>ionCube Add-On</li>
            <li>Let's Encrypt Free SSL</li>
            <li>Load Alerts to Slack (BETA)</li>
            <li>MySQL-based SSL/TLS Encrypted Connection (MySQL/MariaDB/Percona)</li>
            <li>New Relic APM</li>
        </ul></td>
        <td><ul>
            <li>NGINX Amplify</li>
            <li>Postgres SSL/TLS Encrypted Connection</li>
            <li>Redis Encrypted Connection</li>
            <li>TimeZone Change</li>
            <li>WordPress Backup/Restore for the filesystem and the databases</li>
        </ul></td>
        </tr>
</tbody></table>

{{%tip%}}**Note:** The provisioned set of JPS packages can vary on each particular platform as it depends on the hosting provider settings.

For example, the ***HTTP/3 Premium CDN*** add-on is supported on the following [platform installations](https://www.virtuozzo.com/application-platform-partners/?featuresSupport=CDN) only.{{%/tip%}}

The PaaS team frequently implements new solutions to extend this list. The majority of such updates are highlighted within the [platform blog](https://www.virtuozzo.com/company/blog/), so if you are interested, you can subscribe to be notified about all of the new utilities.

{{%tip%}}**Tip:** For more solution examples refer to the [JPS Collection](https://github.com/jelastic-jps/) on GitHub, where you can find multiple packages to be used with the platform:

* [Enterprise WordPress Cluster for Auto Scaling, High Performance and High Availability](https://github.com/jelastic-jps/wordpress-cluster)
* [Scalable MySQL Cluster with ProxySQL Load Balancer and Orchestrator](https://github.com/jelastic-jps/mysql-cluster)
* [Free Let's Encrypt SSL Certificates Integration for the Most Popular Software Stacks](https://github.com/jelastic-jps/lets-encrypt)
* [Highly Available and Auto-Scalable Magento Cluster](https://github.com/jelastic-jps/magento-cluster)
* [Cyclos - a Payment Platform for Large Businesses and Organisations](https://github.com/jelastic-jps/cyclos)
* [Cron-Based Scheduler for Automatic Environment Hibernation](https://github.com/jelastic-jps/start-stop-scheduler)
* [Minio Cluster - S3 Compatible Object Storage](https://github.com/jelastic-jps/minio)
* [Auto-Scalable Docker Engine and Docker Swarm Cluster](https://github.com/jelastic-jps/docker-native)
* [Simple Automated CI/CD Pipeline for GitHub and GitLab Projects](https://github.com/jelastic-jps/git-push-deploy)
* [Java Memory Agent for Container RAM Usage Optimization](https://github.com/jelastic-jps/java-memory-agent)

[Import](/environment-import/) the appropriate manifest file via the dashboard to instantly get your solution. Also, you can explore the source code of any package, fork repository for yourself and customize it up to your particular needs before installation.{{%/tip%}}


## Subscription Products

*This feature availability depends on the particular hosting provider’s settings.*

The **Subscription Plans** section of the Marketplace lists all the products that are offered on a subscription-based basis (i.e. for a fixed price). You can learn more in the dedicated [Subscription-Based Products](/subscription-products/) guide.

![install subscription product](02-install-subscription-product.png)


## Installing Solution from Marketplace

Below, we'll provide an example of a packaged solution installation.

1\. To find a particular application, use a special **Search** box at the top-left corner of the ***Marketplace*** section. Type a phrase, and it will be looked for within solutions' names and descriptions (both for applications and add-ons).

![search within marketplace](03-search-within-marketplace.png)

2\. We'll use the **WordPress Standalone Kit** as an example. Select it from the proposed search results to instantly open the installation frame. Alternatively, you can locate the required solution manually within the categorized list (*Content Management* section in our case), hover over to unfold additional details, and click **Install**.

![install solution from marketplace](04-install-solution-from-marketplace.png)

3\. Based on the particular package, you may need to provide some additional data to customize the solution up to your needs. For example, it could be the preferable nodes count or specific option availability.

For a detailed overview of the [WordPress Standalone Hosting](https://www.virtuozzo.com/company/blog/wordpress-hosting-standalone-container/) peculiarities, refer to the linked article on our blog. In general, the basic settings (i.e. required by any application) are environment name, [alias](/environment-aliases/), and, if available, [region](/environment-regions/).

![solution installation frame](05-solution-installation-frame.png)

Click **Install** to continue.

4\. The installation process may require up to several minutes, based on the selected solution.

![solution automatic installation](06-solution-automatic-installation.png)

{{%tip%}}**Tip:** You can track the JPS package installation process in detail via the Cloud Scripting console. While logged into your dashboard account, add the ***/console*** suffix to URL:

*https://app.**[{platformDomain}](/paas-hosting-providers/)**/console*

![cloud scripting console](07-cloud-scripting-console.png){{%/tip%}}

5\. After all the required configurations, you'll see a success frame. In our case, it additionally provides the corresponding administration data (which is also sent via the appropriate email notification).

![marketplace installation success](08-marketplace-installation-success.png)

Click the **Open in Browser** button.

6\. Your ready-to-work application will be opened in a new browser tab.

![WordPress automatically installed](09-wordpress-automatically-installed.png)

That's all! Now, you can enjoy using your application.


## What's next?

* [JPS Overview](/jps/)
* [Application Manifest](/application-manifest/)
* [Cloud Scripting](https://docs.cloudscripting.com/)