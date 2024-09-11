---
draft: false
title: "Application Lifecycle Management"
aliases: ["/how-to-manage-application-lifecycle/", "/how-to-manage-the-application-lifecycle-in-jelastic/"]
seoindex: "index, follow"
seotitle: "Application Lifecycle Management"
seokeywords: "application lifecycle, application lifecycle management, manage application, application production, application testing, application developing, lifecycle application, dns node"
seodesc: "Examine what is application lifecycle management and how to realize it. Learn how to create few copies of application - for production, testing and developing - to ensure its stability."
menu: 
    docs:
        title: "Application Lifecycle Management"
        url: "/how-to-manage-application-lifecycle/"
        weight: 150
        parent: "application-settings"
        identifier: "how-to-manage-application-lifecycle.md"
---

# How to Manage Application Lifecycle

Complex applications with highly customized logic and user interfaces take time to develop and require more formal practices to ensure that they work as intended and meet users' needs. Your project might not be so large, but you can still benefit from using development and test environments, where you can develop and test your code without affecting end users. Building your own applications requires a thorough understanding of the issues that can take place during the app lifecycle, from development to the production stage.

![application lifecycle](01-application-lifecycle.png)

Application lifecycle management becomes a lot easier thanks to the automation of routine operations (creating environments, building and deploying projects, binding and swapping domains, etc.). One of the best practices is to make your test environment look like your production environment and to periodically synchronize the test database with the data from production, and both of environments will look at one database. Also we'll show how to use separate building environments to build all your projects with the embedded Maven tool.

![development steps](02-development-steps.png) 

To realize the schema above we'll come through the next steps:

* [Create the production environment](#production-env)
* [Create the build environment](#build-env)
* [Build and deploy the project](#deploy-project)
* [Create database environment](#database-env)
* [Configure database connection](#database-connection)
* [Create the test environment](#test-env)
* [Upgrade application](#update-app)

Also here is a video version of the same procedure:

<iframe src="https://www.youtube.com/embed/JLCBjkWY4s8" allowfullscreen="" frameborder="0" height="349" width="560"></iframe>

Let's get started<a id="production-env"></a>!


## Create the Production Environment

1\. Log into the platform dashboard.

2\. Create a new environment.

![create environment](03-create-environment.png) 
 
3\. Select the application server you want to use (for example *GlassFish*), set the cloudlets limit and type the name of your first environment, for example, *prodenv*. Then click **Create**.

![production environment wizard](04-production-environment-wizard.png)

Wait just a minute for your environment to be created.

![production environment created](05-production-environment-created.png)<a id="build-env"></a>


## Create the Build Environment

You can build applications in the platform instead of building your projects locally and uploading WAR archives. It is faster and takes less time and bandwidth, you get the efficiency of the cloud and can continue to use your computer without extra loads. The platform can take application source code directly from your version control repositories (via Git or SVN protocol).

The next step is to create a building environment.

1\. Create a new environment, pick **Maven** as your building tool, set the cloudlets limit and type the environment name, for example: *buildenv*. You can create environment without a compute node. No need to have separate building tools for each of your environments.

![build environment wizard](06-build-environment-wizard.png) 

2\. In just a couple of minutes your environment will be created.

![build environment created](07-build-environment-created.png)<a id="deploy-project"></a>


## Build and Deploy the Project

Now we can easily build our first project and deploy it to the production environment.

1\. Add your project to Maven. 

![add project](08-add-project.png)

In the dialog, navigate to the **Git** tab (or SVN) if you want to use Git as your revision control system. Specify your project name, **Path** to your project, **Branch, Login** and **Password** of your repository, name of your **Environment**, **Context** in which you will deploy your project, and click **Add**.

![add "before" project](09-add-before-project.png) 
 
2\. Click **Buid and deploy** button for your project.

![build and deploy](10-build-and-deploy.png)<a id="database-env"></a>


## Create Database Environment

Let's create one more environment with the database without a compute node. This allows you to store all your applications' data there.

1\. Click on **Create environment** and pick the database (for example MySQL) that you want to use.

![database environment wizard](11-database-environment-wizard.png) 
 
2\. When your environment is successfully created, click the **Open in Browser** button for **MySQL**. The platform have sent you an email with credentials to the database. Create an account and the database with the application using these credentials.

![database add user](12-database-add-user.png)

![create dedicated database](13-create-dedicated-database.png)<a id="database-connection"></a>


## Configure Database Connection

1\. Click the button **Config** next to the application server of your production environment.

![GlassFish config](14-glassfish-config.png) 

2\. In the opened tab create a ***mydb.cfg*** file in the **/opt/glassfish3/temp** directory and add there all necessary configurations:
```
host=jdbc:mysql://mysql{node_id}-{your_env_name}.{hoster_domain}/{db_name}
username={get in the email}
password={get in the email}
driver=com.mysql.jdbc.Driver
```

![database connection configs](15-database-connection-configs.png)

{{%tip%}}**Note:** You can mention all connection settings in your code (application). In the given example, we put all the settings in the file, which is read by our application.{{%/tip%}}

3\. Upload MySQL connector to the **/opt/glassfish3/glassfish/domains/domain1/lib** directory of GlassFish.

![upload MySQL connector](16-upload-mysql-connector.png)

4\. Restart GlassFish and open your app in a web browser.

!["before" application in production environment](17-before-application-in-production-environment.png)

5\. With the platform, you have the ability to set your own domain name for your URL instead of using your hoster domain name. So, buy a domain name for your production environment. In this case, we recommend you to set your own custom domain by adding a CNAME record. Click the **Settings** button (the wrench icon) for your environment and bind the domain. In our case the URL is *production.com*. 

![bind production domain](18-bind-production-domain.png) 

!["before" application production](19-before-application-production.png) 

{{%tip%}}**Note:** In this example we use DNS names (production.com, test.com) that were previously added to local DNS-server (file hosts)<a id="test-env"></a>.{{%/tip%}}


## Create the Test Environment

It's time to create our test environment now. For this purposes you can easily clone your production environment. That lets you work with multiple versions of the same environment and branch your environments as needed. The cloned environment is identical to the original environment and includes all data in its databases, deployed \*.WAR and \*.JAR packages.

1\. Clone your production environment to get the exact copy of it for adding some new features and testing them.

![clone environment](20-clone-environment.png) 

Let's call it *testenv*.

![environment clone name](21-environment-clone-name.png)

2\. You can open it in a browser just to ensure that everything is ok.

!["before" application in test environment](22-before-application-in-test-environment.png)<a id="update-app"></a>


## Upgrade Application

If, for example, you need to make some changes to your application:

1\. Add your new project to Maven.

![add "after" project](23-add-after-project.png) 

2\. Click **Buid and deploy** button for the new project. Your project must appear in the context that you have specified.

!["after" project deployed to test environment](24-after-project-deployed-to-test-environment.png) 

3\. Click the **Settings** button for your environment and bind the domain (e.g. test.com) that you have bought earlier.

![bind test domain](25-bind-test-domain.png)
 
4\. Let's open our new application in a web browser to see the changes.

!["after" application test](26-after-application-test.png) 

After you have tested your new features you can just swap domains. With this functionality, your application's end users will not experience downtime when you deploy a new application version. You can stage your new application version in a test environment and swap the URLs with the production environment in just a few clicks.

5\. Open the settings for one of your environments and in the "Custom domains" section, choose the other environment for swapping and click **Swap**.

![swap domains](27-swap-domains.png)

Now you can go to *production.com* and you'll see that your application has been already updated.

!["after" application production](28-after-application-production.png)
 

## What's next?

* [Application Сonfiguration](/configuration-file-manager/)
* [Clone Environment](/clone-environment/)
* [Deploy Application](/deployment-guide/)