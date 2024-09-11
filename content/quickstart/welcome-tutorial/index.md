---
draft: false
title: "Welcome Tutorial"
aliases: "/welcome-tutorial/"
seoindex: "index, follow"
seotitle: "Welcome Tutorial"
seokeywords: "paas tutorial, welcome tutorial, platform introduction guide, paas introduction guide, application deployment guide, platform overview presentation, interactive guide. paas benefits, paas features, start working with paas"
seodesc: "Follow the introduction guide for the platform to familiarize with the platform&#8217;s main benefits. Check the overview presentation on the central features and UI, then go step-by-step to deploy the first application."
menu: 
    docs:
        title: "Welcome Tutorial"
        url: "/welcome-tutorial/"
        weight: 3
        parent: "quickstart"
        identifier: "welcome-tutorial.md"
---

# Platform Welcome Tutorial

On the very first login into the dashboard, the platform automatically starts a quick introduction guide. The tutorial includes information on the main functionality and features available for you and helps to deploy your first application. The whole process requires just a few minutes to complete and is an excellent basis to start working with the platform.

If needed, this tutorial can be manually run via the **Help > Tutorial** menu at any time:

![start PaaS welcome tutorial](01-start-paas-welcome-tutorial.png)

Let's walk through all of the tutorial steps.

1\. Guide starts with an introductory presentation. The first frame is named ***The Benefits of PaaS***, which provides a list of the central features of the platform.

![tutorial PaaS benefits](02-tutorial-paas-benefits.png)

Hover over a particular point within the list to view an explanatory illustration. Click it to open the dedicated documentation page for even more details.

Hovering over any point reveals the corresponding illustration, while clicking on it redirects to the dedicated documentation page.

2\. The second ***Build Your Application Topology*** slide shows how to build your application topology using the platform components. Refer to the **[Concept & Terminology](/paas-components-definition/)** document for additional details.

![tutorial build application topology](03-tutorial-build-application-topology.png)

3\. The next ***Tune Your Resource Consumption*** frame demonstrates how to provide resources for the instances and how the estimated price is automatically calculated.

![tutorial tune resource consumption](04-tutorial-tune-resource-consumption.png)

The platform automatically provides *Estimated cost* for the currently configured topology based on the *hourly*, *daily*, and *monthly* basis (use the drop-down menu circled in the image above).

{{%tip%}}**Note:** The maximal usage pricing is almost unreachable in practice (100% load on all nodes at all times), see the next step for more details.{{%/tip%}}

4\. The last ***Enjoy Pricing Advantages*** slide helps to explain the efficiency of the platform [usage-based pricing](/pricing-model/) comparing to other cloud vendors' models.

![tutorial PaaS pricing advantages](05-tutorial-paas-pricing-advantages.png)

5\. Next, the presentation is closed and the topology wizard is automatically opened.

![tutorial create environment](06-tutorial-create-environment.png)

{{%tip%}}**Tip:** You can hide the current hint or completely abandon the tutorial with the appropriate icons (*cross* and *crossed out circle* respectively).

![close and stop tutorial](07-close-and-stop-tutorial.png){{%/tip%}}

If needed, you can [set up your new environment](/setting-up-environment/) using all of the parameters available via topology wizard. However, you don't need any specific configurations for this tutorial, so we recommend to follow the hint and click **Create** straightaway.

6\. Wait a minute for your environment to be created. Meanwhile, you can track the process state in the **[Tasks](/dashboard-guide#tasks)** panel.

![tutorial tasks panel](08-tutorial-tasks-panel.png)

7\. Once the operation is completed, tutorial automatically navigates you to the [deployment manager](/deployment-manager/) section. Here, a button to deploy the default *Hello World* application will be highlighted. Click it to proceed.

![tutorial deploy default application](09-tutorial-deploy-default-application.png)

8\. Within the opened [deploy frame](/deployment-guide#archive), select your just created *Environment* in the appropriate drop-down menu and click the **Deploy** button.

![tutorial confirm application deployment](10-tutorial-confirm-application-deployment.png)

9\. Wait a moment for the application to be deployed.

![tutorial wait for deployment](11-tutorial-wait-for-deployment.png)

10\. Great! Your first application is ready to work, click the highlighted **Open in Browser** button to view it in a separate browser tab.

![tutorial open application in browser](12-tutorial-open-application-in-browser.png)

The whole tour requires a couple of minutes but provides information on the main principles of hosting with the platform.


## What's next?

* [Getting Started](/getting-started/)
* [Basics & Terminology](/paas-components-definition/)
* [Dashboard Guide](/dashboard-guide/)
* [Setting Up Environment](/setting-up-environment/)
* [Deployment Guide](/deployment-guide/)