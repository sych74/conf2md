---
draft: false
title: "NodeKick Deployment"
aliases: "/nodekick/"
seoindex: "index, follow"
seotitle: "NodeKick Deployment"
seokeywords: "nodekick, nodekick game, nodekick nodejs, install nodekick, nodekick deployment, nodekick hosting, nodekick paas, nodekick tutorial, nodekick guide"
seodesc: "NodeKick is an open source real time multiplayer fighting game, that can be easily deployed into Node.js environment at the platform."
menu: 
    docs:
        title: "NodeKick Deployment"
        url: "/nodekick/"
        identifier: "nodekick.md"
---

# How to Install NodeKick

**NodeKick** is an open source real time multiplayer fighting game, built at 2d. This application shows a non-trivial usage of *socket.io* and a HTML5 canvas framework called *pixijs*, sharing the common code on the server and client (physics engine in this case). 

Follow the next simple steps in order to get your NodeKick application hosted with the help of the platform.


## Create Environment

1\. Log in to your dashboard and create a new environment.

![create environment](01-create-environment.png)

2\. In the appeared **Environment topology wizard** navigate to the **Node.js** tab and choose **NodeJS** as your application server. Enable **Public IPv4** address for it using the appropriate switcher. Then state the required amount of resources using the cloudlet sliders, type your environment name (e.g. *nodekick*), and click **Create** button.

![environment wizard](02-environment-wizard.png)

3\. In a minute your environment will appear at the dashboard.

![environment for NodeKick created](03-environment-for-nodekick-created.png)


## Add Project

1\. Navigate to the [NodeKick project page](https://github.com/amirrajan/nodekick) at GitHub and copy its HTTPS URL with the corresponding button (circled below).

![NodeKick at GitHub](04-nodekick-at-github.png)

2\. Then switch back to your platform dashboard and click **Add project** icon next to your NodeJS application server.

![add project](05-add-project.png)

3\. In the opened frame select **Git** tab and fill in the **URL** field with a HTTPS link you've copied in the previous step.

![add NodeKick project](06-add-nodekick-project.png)

Click **Add** button to proceed.

4\. Once your project is successfully deployed, open it by means of pressing **Open in Browser** icon next to your environment.

![open NodeKick in browser](07-open-nodekick-in-browser.png)

Now you can start using your own NodeKick server, ran with the help of the platform.

![NodeKick](08-nodekick.png)

Play with your friends and have fun!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Node.js Tutorials](/nodejs-tutorials/)
* [Node.js Dev Center](/nodejs-center/)