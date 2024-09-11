---
draft: false
title: "Cloud9 IDE Deployment"
aliases: "/cloud9/"
seoindex: "index, follow"
seotitle: "Cloud9 IDE Deployment"
seokeywords: "cloud9, cloud9 ide, clod9 nodejs, cloud9 nodejs ide, cloud9 deployment, nodejs tutorial, cloud9 guide, deploy cloud9, cloud9 paas, cloud9 ide installation"
seodesc: "Cloud9 is an outstanding IDE, devoted to the applications' development in the cloud. It can be easily deployed into Node.js environment at the platform."
menu: 
    docs:
        title: "Cloud9 IDE Deployment"
        url: "/cloud9/"
        identifier: "cloud9.md"
---

# How to Deploy Cloud9 IDE

**Cloud9** is an outstanding IDE with a support of more than 40 programming languages, devoted to the applications' development in the cloud. It provides programmer with an online code-editor and a complete Ubuntu workspace, facilitating the development process with a number of available features, such as sharing your workspace with a colleague, joint development, ability to track and review all the changes in your code, pushing to the GIT repository, in-built image editor, etc.

Cloud9 use Node.js on a back-end, so, let's examine how to run it with PaaS Node.js hosting!

## Create a New Environment
To start with, let's create a new environment Cloud9 will be deployed to. 

1\. Log in to your PaaS account and click the **Create Environment** button at the dashboard's top panel in order to access the environment topology wizard.

2\. In the opened frame select the tab with **Node.js** engine. Application server will be already chosen. Therefore, just enable **Public IP** address for it and define the resource limits via cloudlet sliders in the central pane.  
Then enter a name for your environment (e.g. *cloud9*) and press **Create** button.
![cloud9 b14bbc4e0c187e37c7de0d9889676151create environment](b14bbc4e0c187e37c7de0d9889676151create-environment.png)

3\. In a minute or so a newly created environment will be added to the list of your environments at the dashboard.
![cloud9 b14bbc4e0c187e37c7de0d9889676151cloud9 environment](b14bbc4e0c187e37c7de0d9889676151cloud9-environment.png)


## Cloud9 Deployment
Let's proceed to the deployment itself.

1\. Cloud9 is an open-source project, therefore its source code is available at [GitHub](https://github.com/ajaxorg/cloud9). Navigate to the repository and copy the **HTTPS URL** at the right.
![cloud9 b14bbc4e0c187e37c7de0d9889676151git repository](b14bbc4e0c187e37c7de0d9889676151git-repository.png)

2\. Switch back to the platform dashboard and press **Add project** button next to the Node.js application server.
![cloud9 b14bbc4e0c187e37c7de0d9889676151add project](b14bbc4e0c187e37c7de0d9889676151add-project.png)

3\. In the opened frame paste the link you've copied earlier to the **URL** field. 
<div><table><colgroup><col width="*"></colgroup><tbody><tr><td>Don't change the *master* value in the **Branch** field.
</td></tr></tbody></table></div>

Press **Add** button.

![cloud9 b14bbc4e0c187e37c7de0d9889676151git project url](b14bbc4e0c187e37c7de0d9889676151git-project-url.png)

4\. Wait until the project is built and deployed. After that ***ROOT*** context for your Node.js server will appear.
![cloud9 b14bbc4e0c187e37c7de0d9889676151app deployed](b14bbc4e0c187e37c7de0d9889676151app-deployed.png)


## Configure and Run Cloud9
Finally, let's configure our IDE and run it.

1\. Press **Config** button next to the Node.js server in order to access its Configuration Manager.
![cloud9 b14bbc4e0c187e37c7de0d9889676151nodejs config](b14bbc4e0c187e37c7de0d9889676151nodejs-config.png)

2\. In the opened tab navigate to the **webroot > ROOT > configs** folder and click on the ***default.js*** file.
![cloud9 b14bbc4e0c187e37c7de0d9889676151default js file](b14bbc4e0c187e37c7de0d9889676151default-js-file.png)

3\. Find the ***var host = argv.l || process.env.IP || "localhost";*** line and substitute the *localhost* value with the external IP you've attached to your Node.js server.
<div><table><colgroup><col width="*"></colgroup><tbody><tr><td>

The External IP address of a node (if attached) can be seen at the dashboard:
![cloud9 b14bbc4e0c187e37c7de0d9889676151external ip](b14bbc4e0c187e37c7de0d9889676151external-ip.png)
</td></tr></tbody></table></div>

![cloud9 b14bbc4e0c187e37c7de0d9889676151localhost line](b14bbc4e0c187e37c7de0d9889676151localhost-line.png)

4\. **Save** the changes and **Restart** your application server.
![cloud9 b14bbc4e0c187e37c7de0d9889676151restart nodejs](b14bbc4e0c187e37c7de0d9889676151restart-nodejs.png)

5\. Finally, click **Open in browser** next to the environment.
![cloud9 b14bbc4e0c187e37c7de0d9889676151open in browser](b14bbc4e0c187e37c7de0d9889676151open-in-browser.png)

Great! Now you have your own web-integrated IDE running with the platform.
![cloud9 b14bbc4e0c187e37c7de0d9889676151cloud9 opened](b14bbc4e0c187e37c7de0d9889676151cloud9-opened.png)

Enjoy the power of cloud computing!