---
draft: false
title: "Managing Server Roles & Features"
aliases: ["/win-vps-roles-features/", "/win-vps-roles-and-features/"]
seoindex: "index, follow"
seotitle: "Windows Roles and Features"
seokeywords: "windows server roles and features, windows vps add roles, windows vm server manager, windows vps remote desktop, windows vm rdp manager, windows virtual private server rdp, windows vm rdp access, windows vps roles, windows vps guacamole, windows vps rdp server manager"
seodesc: "Access Windows-based virtual private server over RDP via local RD client. Learn how to perform basic configurations, such as setting server roles and features by means of tools available within RDP Server Manager."
menu: 
    docs:
        title: "Managing Server Roles & Features"
        url: "/win-vps-roles-features/"
        weight: 40
        parent: "windows-dotnet"
        identifier: "win-vps-roles-features.md"
---

# Set Windows Roles and Features via Server Manager

[Windows VM](/win-vm/) provides a powerful GUI of Windows OS that can be accessed via [remote desktop protocol](/win-rdp-access/) (RDP). It allows connect to and manage your Windows instance remotely, for example:

* via the [Guacamole](/win-rdp-access/#rdp-connection-via-web-client) HTML5 tool directly in your browser
* via the [local RD client](/win-rdp-access/#rdp-connection-via-local-client) (the appropriate credentials for connection establishment can be found in the email, sent after environment creation)

For configuring Windows virtual private server via RDP, the inbuilt Server Manager is used. Below we highlight some of the basic functionalities it provides :

* [setting server roles](#set-windows-vm-roles)
* [adding server features](#add-features-to-windows-server-roles)


## Set Windows VM Roles

Once [connected](/win-rdp-access/) to the required node's desktop, you'll see the **Server Manager** tool opened. As an example, let's add a new server role with the following steps.

1\. Click the **Add roles and features** link located on the manager's main page.

![Windows server manager](01-windows-server-manager.png)

2\. The corresponding wizard will be opened in a new window with some basic pre-start information displayed, thus check it out and click on **Next**.

![Windows add roles](02-windows-add-roles.png)

At the *Installation Type* tab, select the **Role-based or feature-based installation** option and proceed with the **Next** button.

3\. The *Server Selection* tab will help you to choose the server you want to configure (several servers of a single Active Directory domain can be added through the *Add Servers* option on the main **Server Manager** page).

![Windows server select](03-windows-server-select.png)

Select the current one and navigate to the **Next** tab.

4\. Within the *Server Roles* tab, click on a particular role from the list of available ones to get its description (at the right part of the window) and tick the required check-boxes to enable corresponding roles.

![Windows server roles](04-windows-server-roles.png)

We'll add the **Web Server (IIS)** role as an example and proceed with managing its features in the next section. 


## Add Features to Windows Server Roles

Depending on the previously selected server role, you can activate some additional server features inherent for it.

1\. Upon a role selection, you'll be displayed a pop up window with the list of non-obligatory role-dedicated management tools (you can enable or disable their installation with the check-box below).

![Windows add features](05-windows-add-features.png)

Hit the **Add Features** button.

2\. During the next several wizard steps (depending on the chosen roles) you can manage some additional features. For that, read the selected roles' details and specify the required services for them.

![Windows role services](06-windows-role-services.png)

Finish your configurations and click **Next**.

3\. At the last *Confirmation* tab, check the configurations you've previously specified and click **Install** if everything is OK.

![Windows install roles and features](07-windows-install-roles-and-features.png)

4\. The installation will start automatically. You can wait until it is successfully finished or close the current window and continue working, while this process will be finished in the background.

![Windows roles and features installed](08-windows-roles-and-features-installed.png)

5\. Once installation is completed, new role(s) will appear at the **Server Manager**'s dashboard, where they can be easily accessed for tracking and additional adjustment of parameters.

![Windows remove roles and features](09-windows-remove-roles-and-features.png)

Also, you can always remove any custom role or feature with the help of the completely similar wizard, available through the **Remove Roles and Features** option in the **Manage** drop-down dashboard list.

{{%tip%}}**Tip:** If you'd like to learn more about the available Windows VM possibilities, refer to the [Windows Server 2008 R2](https://technet.microsoft.com/en-us/library/dd349801%28v=ws.10%29.aspx) and [Windows Server 2012](https://technet.microsoft.com/en-us/library/hh801901.aspx) official documentation.{{%/tip%}}


## What's next?

* [.NET Core (Beta)](/net-core/)
* [Windows VM](/win-vm/)
* [Windows RD Access](/win-rdp-access/)