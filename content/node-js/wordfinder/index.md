---
draft: false
title: "Word Finder Deployment"
aliases: "/wordfinder/"
seoindex: "index, follow"
seotitle: "Word Finder Deployment"
seokeywords: "word finder, word finder application, word finder nodejs, install word finder, word finder deployment, word finder hosting, word finder tutorial, word finder guide, word finder paas"
seodesc: "Word Finder is a simple Node.js application that can find all the worlds matching specified pattern. Follow this guide to deploy Word Finder at the platform."
menu: 
    docs:
        title: "Word Finder Deployment"
        url: "/wordfinder/"
        identifier: "wordfinder.md"
---

# How to Install Word Finder

**Word Finder** will give you the help you need to beat the competition in such game as Words with Friends. Just enter the tile to find all the matched words, and Word Finder will scan through every english word (within a base with over 200k words) to deliver complete word lists suited for your situation.

So, let's find out how to get the Word Finder application hosted just in a few steps with the help of the platform.

## Create Environment

1\. Log in to the platform and click **Create environment** button in the upper left corner of the dashboard.

![create environment button](01-create-environment-button.png)

2\. In the opened window select the **Node.js** tab and choose **NodeJS** as your application server. Use the cloudlets sliders to determine the amount of required resources, type your environment name (e.g. *wordfinder*), and click **Create** button.

![Word Finder environment topology](02-word-finder-environment-topology.png)

3\. Your environment will be created in a minute.

![environment for Word Finder created](03-environment-for-word-finder-created.png)


## Add Project

1\. Navigate to the Word Finder project at GitHub with the following [link](https://github.com/amirrajan/word-finder). Click **Copy to clipboard** button at the right pane.

![GitHub Word Finder project](04-github-word-finder-project.png)

2\. Now return to the platform dashboard and click **Add project** icon next to your NodeJS app server.

![Node.js add project](05-nodejs-add-project.png)

3\. In the opened frame choose the **Git** tab and fill in the **URL** text field with a HTTPS link you've copied at GitHub.

Click **Add** button to proceed.

![deploy Word Finder application](06-deploy-word-finder-application.png)

4\. Wait until the project is successfully added and run the application by means of pressing **Open in Browser** icon next to your environment.

![open Word Finder in browser](07-open-word-finder-in-browser.png)

Now you can start use your Word Finder, hosted with the platform.

![Word Finder successfully deployed](08-word-finder-successfully-deployed.png)

Good luck and beat them all!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Node.js Tutorials](/nodejs-tutorials/)
* [Node.js Dev Center](/nodejs-center/)