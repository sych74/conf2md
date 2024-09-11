---
draft: false
title: "Load Alerts"
aliases: ["/load-alerts/", "/environment-triggers/"]
seoindex: "index, follow"
seotitle: "Load Alerts"
seokeywords: "load alerts, application load, load monitoring, load notifications, load triggers, notification triggers"
seodesc: "Configure load alerts notification triggers to automatically sent an email upon the environment resources exceeding the specified consumption limit."
menu:
    docs:
        title: "Load Alerts"
        url: "/load-alerts/"
        weight: 30
        parent: "built-in-monitoring"
        identifier: "load-alerts.md"
---

# Load Alerts

While creating an environment, you state the cloudlet limits for each node. In such a way, the resources are limited and the spends are regulated. When the traffic grows an application requests more resources for normal work. And, if the limits created by you are too low, this can lead to failure in app performance.

To monitor your application's load and the amount of resources it requires, you can configure a set of automatic notification triggers. They are executed if the usage of a particular resource type is above/below the stated value (%) during the appropriate time period. As a result, you'll get an email notification about your application's load change.

{{%note%}}**Note:** Starting with PaaS 4.6 version, each of the newly created containers is delivered with a set of preconfigured load triggers, so you'll receive the appropriate notifications by default. However, any of them can be easily tuned or disabled, as well as the new ones can be added like it's described below.{{%/note%}}

* [Create Alert](#create-alert)
* [Triggers Execution History](#triggers-execution-history)


## Create Alert

In order to configure an alert, follow the next instruction:

1\. Click the **Settings** button for the desired environment:

![load alerts 1](1.png)

2\. In the opened tab, navigate to the **Monitoring > Load Alerts** section:

![load alerts 2](2.png)

Here, if such is stated within your hosting service provider's settings, you can find a bunch of default triggers, which are automatically added during environment creation. These ones, if exist, are to notify you when the *RAM*, *CPU*, *disk*, *inodes* or *network traffic* usage at any node is coming close to current resource limits (according to the predefined by hoster levels of consumption for notification).

3\. Using the buttons in the tool panel, you can either **Add** a new alert or **Edit**, **Remove**, **Enable/Disable** the already existing ones (including the default triggers set). Also, alerts list can be **Refreshed** using the corresponding button.

![load alerts 3](3.png)

Let's consider a case of setting up your own trigger - for that, click on the **Add** button, circled in the image above.

4\. In the opened **Add alert** frame, define the following values:

* ***Name*** - name of the notification trigger
* ***Nodes*** - type of the environment's node (you can apply trigger to any node within the chosen environment)
* ***Whenever*** - type of resources that will be monitored by trigger: *Cloudlets (Memory, CPU)*, *Memory*, *CPU, Network (out ext. + in ext.)*, *Network (out ext.)*, *Storage* (disk space amount), *Disk I/O*, *Disk IOPS* and *Inodes*
* ***Is*** - condition for trigger invocation/execution, due to which the resource consumption should be *above* or *below* (the &ldquo;*&gt;*&rdquo; or &ldquo;*&lt;*&rdquo; values correspondingly - use the first combo-box) of the stated percentage or *Mbps* for the *Network* monitoring
* ***For at least*** - time period before trigger execution, during which it should remains invoked
* ***Notification frequency*** - delay for the repetitive message to be sent

![load alerts 4](4.png)

After you've stated all the preferable configurations, click **Add** button.

5\. As soon as alert is configured and activated, it will appear within list with the name you've specified in the previous step.

![load alerts 5](5.png)

6\. As a result, every time the resource usage comes above/below the stated percentage (depending on the condition stated) during the specified time period, the system will send you an email notification with the current level of consumption, some recommendations on this issue and direct link for the node's scaling limit adjustment:

![load alert email notification](6-load-alert-email-notification.png)

{{%tip%}}**Note:** that if an environment is [shared](/share-environment/) with other users, they will also receive the same preconfigured load notifications via their emails.{{%/tip%}}

In this way, you can set up a number of different triggers for any existing node in your environment.


## Triggers Execution History

You can view the history of triggers' executions for the nodes of a particular environment within its settings.

1\. Navigate to the **Monitoring &gt; Events History** section. The ***Load Alerts*** notification **Type** will be chosen automatically (whilst the second option in the appropriate list is devoted to [auto horizontal scaling](/automatic-horizontal-scaling/) history).

![load alerts 7](7.png)

2\. Using the **Period** drop-down list, define the time interval you'd like to view the alerts for. The available values are: *day*, *week*, *month* and *custom* (where the last one allows to specify the required dates manually).

![load alerts 8](8.png)

3\. As a result, you'll see the list of alerts, that were activated during the stated period. It includes information on:

* **Date** and time when a trigger has been invoked
* **Name** of the activated alert
* **Nodes** type the alert has been configured for
* **Condition** of alert activation
* **Result** of the alert (*success* or *failure*, i.e. whether notification has been sent or not)

4\. Click on a particular load alert to see its **Details** to the right. This pane contains some additional information:

* ***Loading Value*** - resource usage level for the time of alert activation, with the amount of consumed cloudlets in brackets
* ***Action*** - operation, that has been performed after alert activation (*Send Notification* in this case)

![load alerts 9](9.png)

In such a way, you can configure a set of alerts and to be sure that the platform will inform you about your application load changes.

{{%tip%}}In case you have any questions left on configuring alert notifications or just need more detailed information on this functionality, feel free to appeal for our technical experts' assistance at [Stackoverflow](https://stackoverflow.com/questions/tagged/jelastic).{{%/tip%}}


## What's next?

* [Log Files](/view-log-files/)
* [Statistics](/view-app-statistics/)
* [Security of App with NGINX Balancer](/nginx-balancer-security/)