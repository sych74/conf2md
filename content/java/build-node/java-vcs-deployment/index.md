---
draft: false
title: "Java VCS Deployment with Maven"
aliases: ["/java-vcs-deployment/", "/maven-build-node/", "/bitbucket-project-maven/", "/maven-cloud-hosting-in-jelastic/"]
seoindex: "index, follow"
seotitle: "Java VCS Deployment with Maven"
seokeywords: "java vcs deployment, maven build node, maven deployment, deploy with maven, java application deployment, deploy java project git, deploy java project svn, deploy java project bitbucket, vcs deployment with maven, maven build tool, java application deployment git svn, java maven deployment, vcs project deployment, maven add project, maven build project, maven deploy project, maven manage rojects"
seodesc: "Find out how to add public or private Java project from your VCS repository into the platform. Use a Maven build node to deploy your Java applications from the remote Git, SVN, or Bitbucket repositories."
menu: 
    docs:
        title: "Java VCS Deployment with Maven"
        url: "/java-vcs-deployment/"
        weight: 10
        parent: "build-node"
        identifier: "java-vcs-deployment.md"
---

# Java VCS Deployment with Maven

**Maven** is a build automation and software comprehension tool, which is primarily used for Java programming. With the platform you can add any *public* or *private* project directly from your version control system (VCS) repository using the appropriate link type: *http*, *https* or *svn* for **SVN** and *git*, *http*, *https* or *ftp* for **Git**. After addition, Java projects can be deployed to the appropriate application servers using the Maven build node.

Now, let's see how you can add private or public Java application from a remote VCS repository directly to the Maven node and deploy this project to your environment.

{{%tip%}}**Tip:** Before proceeding to the deployment, you need to add your project to the [Deployment Manager](/deployment-manager/#git--svn-projects). As an example, you can use the demo "Hello World" application from our [GitHub repository](https://github.com/jelastic/HelloWorld-CI-CD) (no authentication needed) - use the **Clone or download** button to get the required URL.{{%/tip%}}


## Add Project to Maven

You can add Java project directly to the Maven build node.

1\. Select the **Add project** button next to the *Maven* layer, node or the *Projects* line underneath:

![Maven add project](01-maven-add-project.png)

2\. In the opened dialog box, you need to fill in the required fields:

* **Name** - sets a name for your project (no spaces and special symbols are allowed)
* **Repository** - allows to select the Git / SVN project from Deployment Manager (or jump to its addition form)
* **Branch** - defines the used repository branch (*master* by default)
* **Working Directory** (optional) - provides relative path to the repository subdirectory with application source code
* **Deploy** - chooses whether project should be just build on the Maven node (if unticked) or build and immediately deployed (if ticked); herewith, the letter option requires to fill into two additional fields:
    * **Environment** - selects a target environment with the application server (is automatically selected, when installing from application server)
    * **Context** - sets the desired custom context for the project (*ROOT* by default)
* **Hooks** - applies the provided [scripts](/deployment-hooks/) either before or after build / deployment processes
* **Check and auto-deploy updates** - enables periodical check ups for code changes in your repository (with configurable frequency); if any, project [automatic deployment](/git-svn-auto-deploy/) is initiated
* **Auto-resolve conflicts** - prevents the occurrence of merge conflicts by updating the contradictory files to the repository version (i.e. locally made changes are discarded)

![Maven configure project](02-maven-configure-project.png)

{{%tip%}}**Tip:** If initiating deployment from a Java application server, you may need to set some additional options:

* **Build** - allows to select the existing Maven build node or add one into the target environment
* **Deploy Strategy** (for deployments into [scaled server](/horizontal-scaling/)) - allows to choose between relatively quicker *Simultaneous deployment* variant, which causes a brief downtime, and the *Sequential deployment with delay* option to perform deployment on servers one-by-one with a set delay between operations, which ensures application uptime

![Maven deploy project](03-maven-deploy-project.png){{%/tip%}}

Finally, select **Add** or **Add + Build** (**Add + Deploy**) at the bottom of the frame. The first option will just save the provided data as a project template (i.e. without performing any actual actions), allowing to easily execute *build* and *deploy* operations in a future.

3\. Now, your project will appear in the Maven node *Projects* list. Here, upon hovering over and clicking the appropriate button, you can call the following actions:  

* **Build** - downloads project from repository to Maven node (only if there were some changes since the last build) and prepares it for deployment
{{%tip%}}**Tip:** The project created with this option can be automatically uploaded to the [Deployment Manager](/deployment-manager/) as archive by ticking the *Upload builds to Deployment Manager* checkbox.

![Maven build project archive](04-maven-build-project-archive.png){{%/tip%}}

* **Build and Deploy** - checks for changes and deploys project into the target environment (allows to choose between the *Simultaneous deployment* and *Sequential deployment with delay* options, if deploying into [scaled server](/horizontal-scaling/))
* **Edit project** - opens a form to edit data specified in the project addition frame described in the previous step
* **Config** - opens the build project folder within the [configuration file manager](/configuration-file-manager/) 
* **Log** - opens the [Log](/view-log-files/) section for issues troubleshooting and analysis
* **Delete** - removes this project from Maven

![Maven manage projects](05-maven-manage-projects.png)

These are GUI options available for Maven build node management, for additional tuning get acquainted with the [Maven Configuration](/maven-configuration/) guide.


## What's next?

* [Deployment Manager](/deployment-manager/)
* [Deployment Hooks](/deployment-hooks/)
* [Git / SVN Auto-Deploy](/git-svn-auto-deploy/)
* [Configuration File Manager](/configuration-file-manager/)