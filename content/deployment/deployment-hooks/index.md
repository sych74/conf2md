---
draft: false
title: "Deployment Hooks"
aliases: "/deployment-hooks/"
seoindex: "index, follow"
seotitle: "Deployment Hooks"
seokeywords: "pre deployment hooks, application deployment hooks, deployment webhooks, deployment hooks use case, hooks for deployment, hooks for application deploy, hooks for deployment automation, custom hook pre deployment, deployment hooks management, custom hook post deployment, custom hooks for deployment, custom hook pre deploy, webhooks example, webhooks use cases"
seodesc: "Configure your application automation through executing custom code scripts (hooks) before and after the build / deployment processes."
menu: 
    docs:
        title: "Deployment Hooks"
        url: "/deployment-hooks/"
        weight: 70
        parent: "deployment"
        identifier: "deployment-hooks.md"
---

# Deployment Hooks

{{%imageLeft%}}![deployment hooks logo](01-deployment-hooks-logo.png){{%/imageLeft%}} **Hook** (or [webhook](https://en.wikipedia.org/wiki/Webhook)) is a procedure of code insertion into some standard operation to apply some customization. In confines of the platform, this functionality allows you to execute your custom scripts before and/or after the application deployment operation. Herewith, for [Maven](/java-vcs-deployment/) build node and Golang application server, the *pre-* and *post-* project build hooks can be additionally set up.

So below we'll examine how to operate with hooks at the platform and will overview several common use cases with step-by-step instructions this functionality can come in handy for:

* [Hooks Management](#hooks-management)
* [Hooks Use Cases](#hooks-use-cases)


## Hooks Management

Being a part of the deployment process, **Hooks** are available within an expandable section of the appropriate dashboard form. So, in order to manage hooks, access the application deployment dialog using one of the following options:

* *Deployment Manager*
![deployment manager](02-deployment-manager.png)

* *Deployment* buttons for an application server
![deployment buttons](03-deployment-buttons.png)

1\. Within the opened frame, choose the preferred deployment source type and expand the ***Hooks*** section.

![deployment hooks](04-deployment-hooks.png)

Here, click on either **Pre** or **Post** button to provide your code, which will be executed respectively just before/immediately after the deployment (according to the chosen option).

2\. Enter the required hook code within the opened editor window. Here, you can use any preferable programming language - just ensure that the appropriate code interpretator is already installed at the target container (being either preliminary installed by yourself or included to the default stack build).

![hook example](05-hook-example.png)

{{%tip%}}**Tip:** Within the top pane, you have an access to the following tools to help you during code editing:
* ***Wrap lines*** - brakes text to continue it in the line below if it reaches the frame border
* ***Search*** - allows to easily find the needed information; is supplied with the additional *Match case* and *Regex* search options
* ***Help*** - redirects to the current document to get the details on proper hooks usage

![hooks editor](06-hooks-editor.png){{%/tip%}}

Click **Apply** when ready. Now you can deploy your application.

3\. After the successful deployment, you can click the **Show Logs** button within the appeared dashboard notification to view the detailed response on performed operations:

![deploy success](07-deploy-success.png)

{{%tip%}}**Note:** In case something goes wrong during the hook execution, you'll get the appropriate notification, whilst the deployment process will be aborted:

![deployment failure](08-deployment-failure.png)

Click the **Show Logs** button in order to get the details on the occurred error by viewing the deployment action log (which corresponds to the ***hooks.log*** file, which can be accessed through the [Logs](/view-log-files/) section for the appropriate server).{{%/tip%}}


## Hooks Use Cases

Hooks provide a broad range of opportunities for developers, allowing to automate the majority of routine processes to get a ready-to-work application just after the deployment. 

As an example, below we've gathered a number of the most common tasks that could be programmed to be automatically accomplished by hooks:

* **Pre-deploy hooks** (i.e. performed before the actual application deployment)
    * to check whether all of the requirements are met
    * to pre-install the required software
    * to clear or prepare a dedicated folder for application files
    * to log data
* **Post deploy** (after deployment is finished)
    * to restart your application server after deployment
    * to install project dependencies
    * to apply any other preferred customization
    * to log data

Below, we've provided a simple example of your own log file creation with the help of hooks.

1\. Initiate deployment of your project using any preferable way. We’ll use the default ***HelloWorld.zip*** archive from a deployment manager.

![deploy HelloWorld](09-deploy-helloworld.png)

2\. Expand the ***Hooks*** section, click on the **Pre** hook and provide the following code within the opened editor:
```php
echo "$(date) - deployment start" >> ~/mylog
if ! grep -q "$(pwd)/mylog" /etc/jelastic/redeploy.conf; then
    echo "$(pwd)/mylog" >> /etc/jelastic/redeploy.conf
fi
```

![pre-deploy hook](10-pre-deploy-hook.png)

This will add a string into the ***mylog*** file (will be automatically created in the home directory, if not exists), which will identify deployment start and provide the appropriate time stamp. Also, we check if the ***redeploy.conf*** file includes our custom log file and, if not, add the appropriate line - in such a way it will be kept after [container redeploy](/container-redeploy/) operation.

3\. For the ***Post*** hook add the next code:
```php
echo "$(date) - deployment end" >> ~/mylog
```

{{%tip%}}**Tip:** If needed, you can use the *exit* command, which allows to break your hook and the appropriate deployment/build operation execution at any point. Herewith, the *0* value (i.e. *exit 0*) is used to indicate success, while any other value assumes an error (e.g. *exit 1*).{{%/tip%}}

![post-deploy hook](11-post-deploy-hook.png)

Here, we just log the end of our deployment.

4\. Finally, deploy your application and check both ***mylog*** and ***redeploy.conf*** file to verify hooks successful execution.

![check hooks execution](12-check-hooks-execution.png)

As you can see, our scripts have worked as intended, providing the deployment start / end time and ensuring it is protected during redeploy operation.

{{%tip%}}If you face any issues while working with hooks, feel free to appeal for our technical experts' assistance at [Stackoverflow](https://stackoverflow.com/questions/tagged/jelastic).{{%/tip%}}


## What's next?

* [Deployment Guide](/deployment-guide/)
* [Maven for Deploy via GIT/SVN](/java-vcs-deployment/)
* [Log Files](/view-log-files/)
* [Container Redeploy](/container-redeploy/)