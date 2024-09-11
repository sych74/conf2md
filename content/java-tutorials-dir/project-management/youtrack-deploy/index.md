---
title: "YouTrack Deployment"
aliases: ["/youtrack-deploy/", "/youtrack-deploy-to-jelastic/"]
seoindex: "index, follow"
seotitle: "YouTrack Deployment"
seokeywords: "youtrack, youtrack jar, youtrack jar deployment, youtrack tutorial, youtrack java engine, youtrack installation, youtrack application, youtrack hosting, youtrack java, youtrack cloud, youtrack paas"
seodesc: "See the tutorial on how to deploy YouTrack (issues tracking and project management tool) JAR package at the platform."
menu:
    docs:
        title: "YouTrack Deployment"
        url: "/youtrack-deploy/"
        identifier: "youtrack-deploy.md"
---

# How to Deploy YouTrack

**[YouTrack](https://www.jetbrains.com/youtrack/)** is an innovative issue tracking and project management tool that helps deliver great products and boost your team's productivity. Flexible customization options ensure the best experience not just for the whole team but for every team member.

This guide below provides detailed steps on the few simple actions required to deploy and launch YouTrack at the platform.


## Create and Configure Environment

1\. Log in to the platform dashboard and click the **New Environment** button to [set up a new environment](/setting-up-environment/).

![new environment](01-new-environment.png)

2\. YouTrack requires root permission in order to be installed and run, so let's create a **[Java Engine](/java-engine/)** server.

Switch to the ***Java*** tab and select **Java Engine** in the application servers block. In the middle part of the wizard, you can configure the necessary number of cloudlets, select the JDK version, and set other parameters.

![create Java Engine environment](02-create-java-engine-environment.png)

Type the preferred name (e.g. *youtrack*) and click **Create**. In a minute, your environment will be created and added to the environments list.

3\. YouTrack uses a [unique Java agent](https://www.jetbrains.com/help/youtrack/standalone/install-youtrack-jar.html#run-youtrack-jar) that only processes options started with **-J** or **-\-J**. So, let's connect to the container via **[Web SSH](/web-ssh-client/)** and remove the default Java agent:

```
bash /java_agent/java --uninstall
```

![SSH uninstall Java agent](03-ssh-uninstall-java-agent.png)

4\. Next, add the required *host* and *port* value to the ***JAVA_ARGS*** [variable](/container-variables/):

```
JAVA_ARGS=0.0.0.0:8080
```

![JAVA_ARGS variable](04-java-args-variable.png)

Now, you are ready to deploy YouTrack.


## Deploy YouTrack

1\. Go to the official website and copy a link to the JAR file of the [YouTrack standalone server](https://www.jetbrains.com/youtrack/download/get_youtrack.html#section=standalone).

![download standalone YouTrack](05-download-standalone-youtrack.png)

![copy direct YouTrack JAR link](06-copy-direct-youtrack-jar-link.png)

2\. Return to the dashboard and upload JAR to the **[Deployment Manager](/deployment-manager/)** via URL. In our case:

*https\://download.jetbrains.com/charisma/youtrack-2021.3.26792.jar*

![uplpad YouTrack package](07-uplpad-youtrack-package.png)

3\. Now, deploy it to the environment you've created earlier.

![deploy YouTrack package](08-deploy-youtrack-package.png)

After deployment, <u>*wait several minutes*</u> for YouTrack to initialize and proceed to the application set up.


## Set Up YouTrack

1\. Click the **Open in Browser** button for your environment with deployed YouTrack.

You need to set up YouTrack before you can use it, so provide a special *Token* and click **Log in**.

{{%tip%}}**Tip:** You can get a token from the:

- dedicated ***/home/jelastic/teamsysdata/conf/internal/services/configurationWizard/wizard_token.txt*** [file](/configuration-file-manager/)
- container [logs](/view-log-files/) (displayed in the ***run.log*** file after the application deployment)
{{%/tip%}}

![YouTrack authentication](09-youtrack-authentication.png)

2\. Next, select the **Set up** option.

![set up YouTrack](10-set-up-youtrack.png)

3\. You can learn all the possible parameters at the [official documentation](https://www.jetbrains.com/help/youtrack/standalone/Installation-and-Upgrade.html). For this example, we'll just use all the default values.

![starting YouTrack](11-starting-youtrack.png)

4\. Once YouTrack starts up, log in with the admin credentials you've provided during the configuration.

![YouTrack log in](12-youtrack-log-in.png)

That's it! You can start working with your own YouTrack server.

![YouTrack project manager](13-youtrack-project-manager.png)

Hopefully, this instruction will be helpful to you!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Java Tutorials](/java-tutorials/)
* [Setting Up Environment](/setting-up-environment/)