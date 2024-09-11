---
draft: false
title: "Dashboard Guide"
aliases: ["/dashboard-guide/", "/jelastic-dashboard-guide/", "/nodejs-dashboard-guide/", "/python-dashboard-guide/", "/ruby-dashboard-guide/", "/mobile-app/", "/php-dashboard-guide/", "/task-panel-cloud-hosting-in-jelastic/"]
seoindex: "index, follow"
seotitle: "Dashboard Guide"
seokeywords: "paas, paas ui, paas user interface, paas dashboard, monitoring resources in cloud environment, custom ssl in cloud environment, tasks panel in cloud platform, export cloud environment, migration in cloud environment, cloning environment in cloud platform, ssh access in cloud environment, clone environment in cloud, cloud platform dashboard guide, ssh connection to cloud environment, deleting environment in cloud platform, firewall rules in cloud environment, topology wizard in platform"
seodesc: "PaaS provides an intuitive and robust dashboard (graphical user interface), which supports all of the platform functionality, ensuring quick and convenient development directly in the web browser."
menu: 
    docs:
        title: "Dashboard Guide"
        url: "/dashboard-guide/"
        weight: 2
        parent: "quickstart"
        identifier: "dashboard-guide.md"
---

# Dashboard Guide

The following guide will provide you with the necessary information on the platform dashboard usage and will help you to get acquainted with the offered possibilities.

To start with, you can check out the quick overview video below to get insights on the main functionality available through the platform intuitive UI:

<iframe width="1280" height="720" src="https://www.youtube.com/embed/d8TYOx2NjvQ" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen=""></iframe>

For better acquaintance, we recommend creating a free account (if you don't have one yet) on any of the installations available at [Cloud Union](https://www.virtuozzo.com/application-platform-partners/) and following the guide steps.

{{%tip%}}**Tip:** A short, interactive tutorial is available directly within the dashboard through the **Help > [Tutorial](/welcome-tutorial/)** option in the top-right corner.{{%/tip%}}

Let's start our detailed exploration of the platform dashboard:

- [Creating and Managing Environments](#creating-and-managing-environments)
- [Function Icons for Environments](#function-icons-for-environments)
- [Environment Settings](#environment-settings)
- [Function Icons for Each Instance](#function-icons-for-each-instance)
- [Import](#import)
- [Marketplace](#marketplace)
- [Environment Groups](#environment-groups)
- [Dashboard Search](#dashboard-search)
- [Deployment Manager](#deployment-manager)
- [Tasks Panel](#tasks-panel)
- [User Settings](#user-settings)
- [Upgrade Trial Account & Balance](#upgrade-trial-account--balance)
- [Help and Account Options](#help-and-account-options)


## Creating and Managing Environments

1\. Click **New Environment** in the upper left corner of the dashboard.

![PaaS main buttons](01-paas-main-buttons.png)

2\. The **Topology Wizard** will be opened, where you can fully customize your environment settings.

The full possibilities of this window are described in the [Setting Up Environment](/setting-up-environment/) article.

![environment topology wizard](02-environment-topology-wizard.png)

After finishing configurations, type your *Environment Name*, and click the **Create** button.

3\. All of your environments will be listed in the central panel of the dashboard.

![environment in the dashboard](03-environment-in-the-dashboard.png)

You can find the following information in the columns:

* **Name** - includes the name (or [alias](/environment-aliases/) if specified) of the environment and its domain. Using the *arrow* icon before the environment's name, you can expand the list of nodes it includes.
* **Status** - shows the current state of your environments (*Running*, *Sleeping*, *Stopped*, *Creating*, *Launching*, *Stopping*, *Cloning*, *Redeploying*, *Exporting*, *Installing*, *Migrating*, *Deleting*).
* **Tags** - displays *[Environment Groups](#environment-groups)* and [region](/environment-regions/) of this environment, versions (*tags*) of the containers, and the name of the deployed *project*.
* **Usage** - shows the current load (i.e. cloudlets and disk space usage). You can also find the ***Billing History*** {{%icon%}}![billing history icon](04-billing-history-icon.png){{%/icon%}} button here, which leads to a separate tab with [your spending statistics](/monitoring-consumed-resources/#billing-history) on the current environment.


## Function Icons for Environments

Hover over a running environment to see multiple icons for its management: *Set Alias*, *Region*, *Open in Browser*, *Settings*, *Change Environment Topology*, *Clone Environment*, *Start/Stop*, *Delete Environment*, *Add/Edit Env Groups*.

![environment icons](05-environment-icons.png)

1\. Use the **Set Alias** {{%icon%}}![set alias icon](06-set-alias-icon.png){{%/icon%}} icon to provide an [alternative environment name](/environment-aliases/) (domain will remain unchanged).

2\. Click the **Open in Browser** {{%icon%}}![open in browser icon](07-open-in-browser-icon.png){{%/icon%}} icon to open the environment in a new browser tab.

{{%tip%}}**Note:** This option could be absent if your environment does not include *application server* and *load balancer* layers.{{%/tip%}}

3\. Click on **Settings** {{%icon%}}![environment settings icon](08-environment-settings-icon.png){{%/icon%}} to open a separate tab with numerous [configuration panels](#environment-settings), check the detailed description in the linked section.

4\. To **Change Environment Topology**, select the needed {{%icon%}}![change environment topology icon](09-change-environment-topology-icon.png){{%/icon%}} option. Perform the required changes in the appeared *Topology Wizard* dialog and click **Apply** to submit them.

5\. To **Clone Environment**, click on the appropriate {{%icon%}}![clone environment icon](10-clone-environment-icon.png){{%/icon%}} button. In the opened frame, specify a name for the new environment and click **Clone**.

More info:

* [Clone Environment](/clone-environment/)
* [Application Lifecycle Management](/how-to-manage-application-lifecycle/)

6\. To change the status of the environment, use the **Start** {{%icon%}}![start environment icon](11-start-environment-icon.png){{%/icon%}} and **Stop** {{%icon%}}![stop environment icon](12-stop-environment-icon.png){{%/icon%}} buttons.

{{%tip%}}**Note:** When the environment is stopped, only the **Settings**, **Clone Environment**, **Start**, and **Delete Environment** buttons are available for it.

Also, the *[Settings](#environment-settings)* tab for such an environment will contain only four active options: *Collaboration*, *Change Owner*, *Migration*, and *Info*.

![stopped environment settings](13-stopped-environment-settings.png){{%/tip%}}

7\. To **Delete Environment**, click on the following {{%icon%}}![delete environment icon](14-delete-environment-icon.png){{%/icon%}} icon and confirm the action by entering your password.

8\. Hover over the ***Tags*** column to manage the [groups of this environment](#environment-groups) with the **Add/Edit Env Group** buttons ({{%icon%}}![add env group icon](15-add-env-group-icon.png){{%/icon%}} or {{%icon%}}![edit env groups icon](16-edit-env-groups-icon.png){{%/icon%}} respectively).

For the platforms with multiple [regions](/environment-regions/), each environment has a region-dedicated icon in the **Tags** column. It allows you to visually separate instances hosted on the different hardware servers and, upon clicking, shows only environments in the appropriate region.


## Environment Settings

There are twelve options within the environment ***Settings*** tab: *Custom Domains*, *Custom SSL*, *SSH Access*, *Endpoints*, *Firewall*, *Load Alerts*, *Auto Horizontal Scaling*, *Collaboration*, *Change Owner*, *Migration*, *Export*, and *Info*.

1\. Select **Custom Domains** to access the following suboptions: *Domain Binding* and *Swap Domains*.

![custom domains settings](17-custom-domains-settings.png)

More info:

* [Custom Domain Name](/custom-domains/)
* [Swap Domains](/swap-domains/)
* [Application Lifecycle Management](/how-to-manage-application-lifecycle/)

2\. Choose the **Custom SSL** option and upload the necessary files to apply your custom SSL certificate.

{{%note%}}**Note:** This feature can be configured only for the certified application servers and load balancers with [public IP](/public-ip/) attached.{{%/note%}}

![custom ssl settings](18-custom-ssl-settings.png)

More info:

* [Self-Signed Custom SSL](/self-signed-ssl/)
* [Custom SSL](/custom-ssl/)

3\. In the **SSH Access** section, you can see the **Public Keys**, **SSH Connection**, and **SFTP / Direct SSH Access** tabs. The first one allows managing your [public SSH keys](/ssh-add-key/). The second one shows how to access your environment (either via *SSH Gate* or *Web SSH*). The third provides details on the connection over the SFTP/FISH protocols.

![ssh access settings](19-ssh-access-settings.png)

More info:

* [SSH Gate](/ssh-gate/)
* [Add SSH Key](/ssh-add-key/)
* [SSH Access via Web Browser](/web-ssh-client/)
* [SSH Access via Local Client](/ssh-gate-access/)
* [SSH Protocols](/ssh-protocols/)

4\. Within the **Endpoints** section, you can manage the mapping of your containers' TCP/UDP ports for ensuring their collaboration with external resources via a direct connection.

![endpoints settings](20-endpoints-settings.png)

More info: [Endpoints](/endpoints/)

5\. The **Firewall** section allows setting **Inbound** and **Outbound Rules** to manage access to your containers. These rules allow you to explicitly define which connections should be accepted and which ones - blocked.

![firewall settings](21-firewall-settings.png)

More info: [Container Firewall](/custom-firewall/)

6\. Use **Load Alerts** to set new triggers (or adjust the default ones) to receive the appropriate email notifications in case the specified resource's usage exceeds the stated limits.

![load alerts settings](22-load-alerts-settings.png)

The **History** tab lists all the triggered alerts in the environment with the details.

More info: [Load Alerts](/load-alerts/)

7\. With the **Auto Horizontal Scaling** option, you can configure triggers to control the number of containers within a layer (except the *Maven* build node). Scaling conditioning can be defined based on the *CPU*, *Memory*, *Network*, *Disk I/O*, and *Disk IOPS* consumption.

![auto horizontal scaling settings](23-auto-horizontal-scaling-settings.png)

Switch to the History tab to view a list of all scaling operations performed by the platform due to the configured triggers.

More info: [Automatic Horizontal Scaling](/automatic-horizontal-scaling/)

8\. In the **Collaboration** section, you can view and manage the list of accounts that have access to the current environment.

![collaboration settings](24-collaboration-settings.png)

If you need to grant access to another user, click **Add** and fill in the *Email* field. To give the *Change Topology / SSH Access* permissions, tick the appropriate option. Click **Save** to apply changes.

More info: [Account Collaboration](/account-collaboration/)

9\. Click **Change Owner** to transfer environment to another user account within the confines of a single platform.

![change owner settings](25-change-owner-settings.png)

More info: [Environment Transferring](/environment-transferred/)

10\. Choose **Migration** to move your environment to another set of hardware ([region](/environment-regions/)).

![migration settings](26-migration-settings.png)

{{%note%}}**Note:** Availability of this option, as well as access to each particular environment region, depends on your hosting provider's settings.{{%/note%}}

More info: [Environment Migration between Regions](/environment-regions-migration/)

11\. Select **Export** to pack all your environment's settings and data into a single downloadable file. Subsequently, it can be restored at another hosting provider's platform, creating an identical environment copy.

![export settings](27-export-settings.png)

{{%note%}}**Note:** Currently, *Windows*, *Storage*, *Elastic VPS*, *Maven*, and *Docker-based* containers are exported without any data inside. In such a case, you'll need to transfer the required files and configurations manually.{{%/note%}}

More info:

* [Environment Export](/environment-export/)
* [Environment Import](/environment-import/)

12\. Switch to the **Info** section to see additional information on the environment *Domain*, its *Owner* and *Creator* (can differ due to the [account collaboration](/account-collaboration/) feature), *[Region](/environment-regions/)*, and *Creation Date*.

![info settings](28-info-settings.png)

That's all of the environment settings.


## Function Icons for Each Instance

Click on the environment in the dashboard to see the list of its [layers](/paas-components-definition/#layer) (load balancers, application servers, databases, etc.). You can further expand these node groups to view and manage separate containers, deployed contexts, attached IP addresses.

Hover over a particular layer or container to see the pop-up icons with different functions.

![node icons](29-node-icons.png)

Use these options to perform the following actions:

* Click the **Set Alias** button to configure an [alternative name](/environment-aliases/) for your layer/node (for example, to define primary and secondary servers in a DB cluster).
* Use **Open in Browser** to access a node of the layer in a new browser tab (can be hidden for some stacks, e.g. *Shared Storage* or *Maven* build node).
* Select the **Restart Node(s)** option to restart the appropriate service inside a particular container or all containers of the layer.
* Select the **Config** option to open [configuration file manager](/configuration-file-manager/) that can adjust nodes by [mounting data](/mount-points/), creating/uploading new files, and modifying/removing existing ones.
* Choose the **Log** option to view the log files for the nodes of the layer. A list of [log files](/view-log-files/) varies based on the selected instance.
* Click the **Statistics** button to [track the data](/view-app-statistics/) on CPU, RAM, Network, Disk space, and IOPS consumption for a separate node or a set of nodes in real-time.
* Select the **Web SSH** option to connect to your [container over SSH](/web-ssh-client/) protocol directly in the browser.
* Use the **Redeploy Container(s)** option to [update nodes](/container-redeploy/) to the preferred tag (version).
* Some nodes can have additional options, such as **Add-Ons** (for installing pluggable modules) or **Remote Desktop** (for [managing Windows-based nodes](/win-rdp-access/)).
* The **Additionally** list allows you to configure [container settings](/container-configuration/) (*Variables*, *Links*, *Volumes*, *CMD / Entry Point*), view *SFTP / Direct SSH Access* details, and access *Scaling Nodes* functionality. Also, depending on the node, it can contain other options (e.g. *Reset Password* or *Admin Panel Login*).


## Import

Next to the **New Environment** option, you can find the **Import** button. It processes the uploaded ***.json***, ***.jps***, ***.cs***, ***.yml***, or ***.yaml*** file to create a new or modify existing environment according to the provided settings.

![PaaS main buttons](30-paas-main-buttons.png)

{{%tip%}}**Tip:** In particular, this feature can be used to create a copy of the environment from another PaaS installation (by [exporting](/environment-export/) it on one platform and [importing](/environment-import/) on the other).{{%/tip%}}

Within the opened **Import** frame, you'll see  the following three tabs (and *[Examples](https://github.com/jelastic-jps)* link to the JPS Collection with numerous ready-to-go solutions):

* ***Local File*** - select the locally stored file (via the **Browse** button), which should be uploaded and executed on the platform
* ***URL*** - provide a direct link to the required manifest file
* ***JPS*** - the built-in JSON/YAML editor can be used to insert and edit your code before the deployment (or even write your package from scratch)

![import dialog window](31-import-dialog-window.png)

For the detailed overview, check the appropriate [Environment Import](/environment-import/) document.


## Marketplace

Upon clicking on the last **Marketplace** option at the top of the dashboard, you'll access a separate window with a list of the pre-packaged solutions for automatic installation.

![PaaS main buttons](32-paas-main-buttons.png)

These packages are divided into two groups: ***Applications*** to create new environments and ***Add-Ons*** to adjust existing ones. You can search for the required solution using the appropriate field at the top-left corner or a categorized list at the left-hand menu.

![marketplace dialog window](33-marketplace-dialog-window.png)

Once you've located the desired package, click **Install** for it, and follow the steps in the appeared installation frame.

Check the appropriate [Marketplace](/marketplace/) article for a detailed overview.


## Environment Groups

The platform provides a possibility to create **[Environment Groups](/environment-groups/)**, which help to categorize your environments. For example, the administration of multiple projects becomes much simpler when each one is organized into a dedicated environment group. If needed, you can apply further division by creating subgroups, e.g. *development/testing/production*, *servers/databases/storages*, etc.

![environment groups](34-environment-groups.png)

{{%tip%}}**Tip:** Usually, environments on the same account are accessible from each other via the platform's internal network. However, if necessary, you can enable network isolation for a group to ensure that environments inside are inaccessible for the environments outside (internal network only).{{%/tip%}}

More info:

* [Group Creation](/environment-groups-creation/)
* [Navigation Across Groups](/environment-groups-navigation/)
* [Group Management](/environment-groups-management/)


## Dashboard Search

The platform provides a built-in search within the dashboard. The core functionality is straightforward - access the *Search* form at the top-right corner (or use the **Ctrl+F**/**Cmd+F** shortcut), type a search term(s), and hit **Enter**. For example, you can locate a container by its IP/ID; search for the particular deployed project/environment; find and deploy applications from [platform Marketplace](/marketplace/).

![dashboard search](35-dashboard-search.png)

The implemented search engine can be personalized to match your specific needs and provide the most accurate results for your requests. Among the main options:

* *special characters* for search expression (e.g. "***-***" prefix to exclude a term or "***\****" wildcard)
* *search source* (either whole account or the current [environment group](/environment-groups/))
* *categories filter* to search among the selected entities (e.g. exclude the Marketplace packages or look for IPs only)

Additional details can be found in the *help* hint for the search form (circled in the image above).


## Deployment Manager

**Deployment Manager** is located at the bottom of the dashboard. It stores applications to automate their subsequent deployment into your environments. There are two subsections within the tab:

* ***[Archive](/deployment-manager/#application-archives)*** - stores the application package itself, **Upload** it from your local machine (*Local File*) or via any external link (*URL*)
* ***[Git / SVN](/deployment-manager/#git--svn-projects)*** - saves the access credentials to your projects at the remote Git / SVN repositories; click the **Add Repo** button and specify the required details

Once your package is added to the Deployment Manager, it can be [automatically deployed](/deployment-guide/) to the required environment by following the linked guide.

{{%tip%}}**Notes:**

* the VCS deployment type for Java application servers is performed with the help of the [Maven build node](/java-vcs-deployment/)
* the [.NET deployment process](/deploy-dotnet-archive-url/) for the Windows-based IIS application server is different from the standardized flow{{%/tip%}}


## Tasks Panel

The **Tasks** panel is placed at the bottom of the dashboard and contains live and historical data on the tasks that the platform is doing or has already done.

![dashboard tasks panel](36-dashboard-tasks-panel.png)

The following data is provided for each record:

* **Status** - shows a state of the operation: *spinner* (in progress), *green* (success) or *red* (error) dot
{{%tip%}}**Tip:** If a [collaborator](/account-collaboration/) works on the account, the icon for the appropriate actions is automatically customized to simplify tasks analysis. Hover over such a custom icon to view the email address of the corresponding account.

![collaborator actions in tasks panel](37-collaborator-actions-in-tasks-panel.png){{%/tip%}}
* **Time** - shows a starting time of the respective operation with the latest records displayed at the top of a tab (additionally, all tasks are grouped by days)
* **Environment** - displays the name of the environment where the action was performed (or dash "**-**" if there is no target environment)
* **Task** - provides an operation or error description
{{%tip%}}**Tip:** You can expand a task to view action **parameters** and server **response** (after completion). The content of these sections can be easily copied with the appropriate button that appears upon hovering over.

![send error report via tasks panel](38-send-error-report-via-tasks-panel.png)

Recent errors can be reported directly to the Support Team using the dedicated icon next to the failed operation.{{%/tip%}}
* **Duration** - shows an execution time for a task (displayed after completion)

If you need to view a complete list of actions performed on the account (i.e. not just the recent ones), switch to the ***Active Log*** tab (the magnifying glass icon). Here, you are provided with advanced search and filter options to quickly locate the required tasks:

* **search** is performed by the parameters and server response (i.e. the data upon expanding an operation) <u>*not the action description*</u>
* you can set the **date range** as last *1/6/24 hour(s)*, *current/previous week*, *current month*, or provide your *custom* period
* tick **Errors only** to hide all the successfully executed operations

![search active log in tasks panel](39-search-active-log-in-tasks-panel.png)

Using the **Tasks** panel, you can always track the activity on your account, as well as troubleshoot issues.


## User Settings

Click the **Settings** button at the top-right corner of the dashboard to access ***User Settings*** configurations.

![user settings button](40-user-settings-button.png)

Here, you can find the following sections: *Account*, *Access Tokens*, *SSH Keys  / SSH Access*, and *Collaboration*.

1\. The ***Account*** section allows managing [two-factor authentication](/two-factor-authentication/) for your account, as well as changing the password.

![account user settings](41-account-user-settings.png)

2\. Within the ***Access Tokens*** tab, you can configure [personal access tokens](/personal-access-tokens/) for your account.

![access tokens user settings](42-access-tokens-user-settings.png)

3\. The ***SSH Keys*** and ***SSH Access*** points open a section with four sub-tabs:

* **Public Keys** - stores [public keys](/ssh-add-key/) added to the platform (required for remote access via local SSH client)
* **Private Keys** - lists [private keys](/git-ssh/#add-private-ssh-key-to-platform-account) added to the platform (required for access to your private Git repository over SSH)
* **SSH Connection** - shows the required steps to connect to your account via *[SSH Gate](/ssh-gate-access/)* and allows accessing particular nodes directly in the browser using *[Web SSH](/web-ssh-client/)*
* **SFTP / Direct SSH Access** - displays connection data for [SFTP/FISH protocols](/ssh-protocols/)

![ssh keys user settings](43-ssh-keys-user-settings.png)

4\. The ***Collaboration*** section consists of two options - **Shared by Me** and **Shared with Me**. The first one allows sharing your environments with other users on the platform, while the second one lists collaborations you are a part of.

![collaboration user settings](44-collaboration-user-settings.png)

For a detailed overview of the [Account Collaboration](/account-collaboration/) feature, refer to the linked guide.


## Upgrade Trial Account & Balance

Depending on the [account type](/types-of-accounts/) (trial or billing), either the **Upgrade Account** or **Balance** section is displayed at the top of the dashboard panel.

1\. The default type for the accounts is *trial*, which provides a free-of-charge hosting period (limited by time or bonus money). However, it is usually limited by the number of provided resources, allowed environments/nodes, etc.

![upgrade trial account](45-upgrade-trial-account.png)

Expand the **Upgrade Account** drop-down menu to see the following options:

* Use the **Upgrade Account** button to get a fully functional [account with no limitations](/types-of-accounts/#billing).
* The **Learn about Trial Limitations** option opens the appropriate *[Account Limits](/quotas-system/)* tab within the *Quotas & Pricing* frame.
* Click on **Learn about Pricing** to be redirected to the documentation page with information about the [pricing model](/pricing-model/).
* Select the **See statistics on recent resource usage** option to open the account's [billing history](/monitoring-consumed-resources/#billing-history).

2\. *Billing* accounts are spared from any limitations but are charged according to the hosting provider's pricing.

![account balance](46-account-balance.png)

Click the **Balance** button to expand a list of the following options:

* **Balance** shows the current balance of the account (both *Cash* and *Bonus*). By clicking on the section, you can open the *Refill Balance* tab.
* **Refresh Balance** option updates balance data to the most actual value.
* Click on **Refill Balance** to [submit the payment](/upgrade-refill-account/).
* **Configure auto-refill** to enable *[automatic refill](/upgrade-refill-account/#auto-refill)* of the account balance (based on the following conditions: *Weekly*, *Monthly* or when *Balance less than* specified sum).
* **Payment Methods** option gives an opportunity to choose the default payment method for the account or add a new one.
* Click on the **Quotas & Pricing** item to see the [information frame](/resource-consumption/#how-much-do-resources-cost) with a set of tabs about platform *Regions* (if multiple ones are available), *Pricing*, and *Account Limits*.
* **Billing History** shows [account spends](/monitoring-consumed-resources/#billing-history) for the specified period.
* Click on the **View Invoices** option to go to the external billing system panel with the account invoices, orders, payments, etc.


## Help and Account Options

The last two sections of the dashboard are **Help** and **Account** (email address).

1\. The ***Help*** drop-down menu provides access to multiple useful links:

* **Contact Support** redirects to the platform customers support page (based on the hosting provider settings, it can be available for billing users only)
* **Go to Community** is a link to the PaaS online community at [Stackoverflow](https://stackoverflow.com/search?tab=newest&q=jelastic)
* **Documentation** navigates to the [Platform Devs Documentation](/)
* **API** opens the [Platform API Documentation](https://www.virtuozzo.com/application-platform-api-docs/)
* **CLI** redirects to the [Platform Command-Line Interface Overview](/cli/)
* **Video** points to the [Platform YouTube Channel](https://www.youtube.com/user/JelasticCloud)
* **Tutorial** starts a short, [interactive guide](/welcome-tutorial/), which explains the basics of working with the platform
* **How do I..?** shows a list of documents relevant to your request

![account help menu](47-account-help-menu.png)

2\. Within the ***Account*** (email address) drop-down list, the following options are available:

* **Settings** redirects you to the *[User Settings](#user-settings)* section
* **Change Password** opens the same-named dialog box, where you need to fill in the required fields (*Current Password*, *New Password*, and *Confirm Password*)
* **Language** allows changing the localization of the dashboard interface (if available)
* **Sign out** to log out of the current account

![general account actions](48-general-account-actions.png)

Now, you know all the basic dashboard possibilities and hopefully won't have any problems working with it. If you still have additional questions, please get in touch with the Support Team of your hosting provider or refer to our technical experts at [Stackoverflow](https://stackoverflow.com/questions/tagged/jelastic).


## What's next?

* [Getting Started](/getting-started/)
* [Basics & Terminology](/paas-components-definition/)
* [Setting Up Environment](/setting-up-environment/)
* [Software Stack Versions](/software-stacks-versions/)
* [Hosters Info](/paas-hosting-providers/)
* [What is PaaS & CaaS](https://www.virtuozzo.com/company/blog/what-is-paas-platform-as-a-service-types-explained/)