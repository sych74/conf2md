---
draft: false
title: "New Relic Update"
aliases: "/update-new-relic/"
seoindex: "index, follow"
seotitle: "New Relic Update"
seokeywords: "update new relic, new relic agent update, new relic cloud monitoring, new relic inside cloud, new relic hosting, how to update new relic, new relic version, new relic apm, new relic agent, new relic tutorial, new relic java agent, new relic java tomcat"
seodesc: "Learn how to perform an effortless update of New Relic APM agent for your application, hosted at the platform. Get the latest monitoring abilities with the embedded option of automatic New Relic updates installation."
menu: 
    docs:
        title: "New Relic Update"
        url: "/update-new-relic/"
        weight: 20
        parent: "monitoring-with-new-relic"
        identifier: "update-new-relic.md"
---

# How to Update Installed New Relic Monitoring Add-on
In order to keep in pace with the most recent [New Relic](/new-relic-installation) monitoring features, the platform provides the inbuilt update option for the dedicated add-on. It checks the presence of the newly released agent versions directly at the corresponding repositories and allows to update it in just a few clicks, without the necessity to handle this manually. So, let's see how to perform this!

## New Relic Agent Update
To find out whether any updates are available for your New Relic agent, open the **Add-ons** section for the required node (with the same-named button next to it) and find the ticked New Relic plank.
 
Click on the gear icon in its top corner and select the **Update Agent** option at the expanded list:
![new relic update](01.png)

Confirm the initiation of the available updates' checking within the appeared dialog frame by clicking **Yes** and wait till the platform completes this.
![check new relic updates](02.png)

As a result, the necessary files (if there are any) will be downloaded and installed.
![new relic update](03.png)

After the add-on is successfully updated, you'll see the corresponding pop-up in the top right corner of the dashboard, which recommends you to restart the instance for these changes to be applied. 

So, follow this tip by clicking the appropriate button next to your application server.

![restart nodes](04.png)

{{%tip%}}**Note:** Please, **pay attention** that if your project is run in a single app server node, the restart will cause a <u>temporary downtime</u> of your application, thus we leave for you to decide when to perform this operation.


However, in case your app server is [scaled horizontally](/multi-nodes#app), the downtime will be minimized, since all the server instances will be restarted sequentially. And starting with [4.9 PaaS version](/release-notes-49#sequential-restart-deploy), you are able to get rid of this inconvenience at all, through setting the delay for executing this operation at each next node within a layer. In such a way, whilst one node is undergoing the maintenance, the rest ones will remain active.{{%/tip%}}

That's it! Your New Relic add-on is updated and ready to work.
{{%tip%}}
Subsequently, the current version of your agent could be checked as follows:

* for *Java* servers - within the ***logs/newrelic_agent.log*** file, located in the dedicated directory with add-on files (see the [list of paths](/new-relic#paths) to it depending on a server)
* for *PHP* servers - via the ***phpinfo()*** output
{{%/tip%}}

In such a way, you can be always up-to-date on the most recent cool features and possibilities the New Relic team provides.


## What's next?
* [New Relic Monitoring Integration](/new-relic-installation/)
* [Automatic Horizontal Scaling](/automatic-horizontal-scaling/)
* [Marketplace](/marketplace/)
* [JPS Collection](https://github.com/jelastic-jps)
* [Application Statistics](/view-app-statistics/)