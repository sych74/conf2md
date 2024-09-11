---
draft: false
title: ".NET Core Application Server"
aliases: ["/net-core/", "/iis8/", "/deploy-dotnet-archive-url/", "/connection-to-mssql/"]
seoindex: "index, follow"
seotitle: ".NET Core"
seokeywords: ".net, dotnet, .net core, dotnet core, install dotnet, install dotnet core, .net core application server, deploy dotnet application, crete dotnet core environment"
seodesc: "Learn how to install .NET Core application server at the platform. Deploy and run a simple .NET application in the cloud."
menu: 
    docs:
        title: ".NET Core"
        url: "/net-core/"
        weight: 10
        parent: "windows-dotnet"
        identifier: "net-core.md"
---

# .NET Core Application Server

**[.NET Core](https://docs.microsoft.com/en-us/dotnet/core/about)** is an open-source, cross-platform version of .NET for building websites, services, and console applications. Often it is used for cloud applications or refactoring large enterprise applications into microservices.

.NET Core consists of the following components:

* **[.NET Core runtime](https://github.com/dotnet/runtime/tree/master/src/coreclr)** - provides essential services (type system, assembly loading, garbage collector, etc.). [Framework libraries](https://github.com/dotnet/runtime/tree/master/src/libraries) provide primitive data types, app composition types, and fundamental utilities
* **[ASP.NET Core runtime](https://github.com/dotnet/aspnetcore)** - provides a framework for building modern, cloud-based, internet-connected applications (*web apps*, *IoT apps*, and *mobile backends*)
* **[.NET Core SDK](https://github.com/dotnet/sdk)** and language compilers ([Roslyn](https://github.com/dotnet/roslyn) and [F#](https://github.com/microsoft/visualfsharp)) - allow the development of the .NET Core projects
* **[dotnet command](https://docs.microsoft.com/en-us/dotnet/core/tools/dotnet)** - launches .NET Core applications and CLI commands. It selects and hosts the runtime, provides an assembly loading policy, and launches apps and tools

{{%tip%}}**Notes:**

- This stack availability depends on the particular hosting provider settings.
- This template utilizes a modern ***systemd*** initialization daemon.
{{%/tip%}}


## Creating .NET Core Server

1\. Log in to the PaaS dashboard and click the **New Environment** button at the top-left corner.

2\. Within the opened [topology wizard](/setting-up-environment/), navigate to the **.NET** tab and select the ***.NET Core*** application server. Configure the other parameters (*[cloudlets](/cloudlet/)*, *disk limit*, *[public IPs](/public-ip/)*, etc.) up to your needs.

![.NET Core topology wizard](01-dotnet-core-topology-wizard.png)

Click **Create** to proceed.

3\. Your environment with the *.NET Core* server will be created in a few minutes.

![.NET Core application server created](02-dotnet-core-application-server-created.png)

The application server operates in a separate container (node) - an isolated virtualized instance - provisioned for a software stack. The container has its own private IP and unique DNS record.


## Deploying Application to .NET Core Server

The platform provides multiple options to automatically [deploy projects](/deployment-guide/). In this example, we'll add a simple .NET project stored on GitHub.

1\. Open the ***Git/SVN*** tab of the **[Deployment Manager](/deployment-manager/#git--svn-projects)** to add a new repository. 

![deployment manager add repository](03-deployment-manager-add-repository.png)

{{%tip%}}**Tip:** If you are interested in [creating your own .NET application](https://docs.microsoft.com/en-us/aspnet/core/tutorials/razor-pages/razor-pages-start) follow the official documentation.{{%/tip%}}

2\. Provide the necessary *URL* and *Branch* for your project.

{{%tip%}}**Note:** .NET Core supports several specific [variables](/container-variables/) that can help with application deployment:

- ***APP_NAME*** - points to the particular folder (if there are multiple applications in a single repository) or runs a specific ***.dll*** file in your project
- ***ASPNETCORE_URLS*** - configures services to work with the specified URL
- ***RUN_OPTION*** - provides additional ***dotnet run*** options for your project

![.NET Core app name variable](04-dotnet-core-app-name-variable.png){{%/tip%}}

![add .NET Core application](05-add-dotnet-core-application.png)

Click **Add** to save the project in your Deployment Manager.

3\. Open the deployment dialog using one of the two buttons in the image below:

![deploy from Git](06-deploy-from-git.png)

4\. Within the opened frame, you need to select an application to be deployed, branch, and the target environment.

![deploy .NET Core application](07-deploy-dotnet-core-application.png)

{{%tip%}}**Note:** Similar to the *Python*, *Node.js*, and *Go* programming languages, the **.NET Core** has a single context (i.e. only one app can be deployed at a time).{{%/tip%}}

Configure any other parameters according to your needs by following the deployment guide.

5\. In a minute, the application will be deployed and can be accessed using the **Open in Browser** button next to the .NET Core application server.

![open .NET Core in browser](08-open-dotnet-core-in-browser.png)

Your web application should be opened in a new browser tab. In our case, it is just a simple .NET website.

![.NET Core web application](09-dotnet-core-web-application.png)

Use this guide as a reference to deploy your own application to the .NET Core server.


## What's next?

* [Windows VM](/win-vm/)
* [Windows RD Access](/win-rdp-access/)
* [Windows Roles & Features](/win-vps-roles-features/)