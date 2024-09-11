---
draft: false
title: "Windows RD Access"
aliases: ["/win-rdp-access/", "/win-vps-rdp/"]
seoindex: "index, follow"
seotitle: "Windows RD Access"
seokeywords: "windows access, remote desktop, remote desktop protocol, windows rdp, rdp access, rdp connection, windows rd access, rdp web client, rdp local client, rdp connection guide"
seodesc: "All the Windows-based nodes at the platform are provided with theembedded Remote Desktop Protocol support. Follow this guide to connect to your Windows node over RDP."
menu: 
    docs:
        title: "Windows RD Access"
        url: "/win-rdp-access/"
        weight: 30
        parent: "windows-dotnet"
        identifier: "win-rdp-access.md"
---

# Windows Remote Desktop Access

{{%imageLeft%}}![Windows RDP access](01-windows-rdp-access.png){{%/imageLeft%}}

All the Windows-based nodes at the platform provide the embedded **Remote Desktop Protocol** support, which allows you to connect to the virtual desktop of your Windows machine and perform any required server configurations through it. 

In order to ensure the maximum convenience while using the Windows hosting services, our platform is equipped with the integrated RDP tool - **Guacamole**. It represents a clientless remote desktop gateway, which is run from within the web-browser by virtue of HTML5 and does not require any additional plugins or client software installed.

Besides this default connection scenario, you can also use your preferred local remote desktop client. So, below we'll describe both ways of the remote desktop connections' establishment in more details:

* [RDP Connection via Web Client](#rdp-connection-via-web-client)
* [RDP Connection via Local Client](#rdp-connection-via-local-client)


## RDP Connection via Web Client

The required workflow for accessing the server’s desktop is similar for all Windows VM nodes. For instant access just after the node’s creation, you can use the direct one-time Guacamole link in the received email. Otherwise, the required operations should be performed through the dashboard.

Let’s consider it on the example of the Windows VM server.

1\. Expand the dedicated **Remote Desktop** list next to the Windows-based node (or layer) and click the **Open in Browser** button.

![remote desktop menu in dashboard](02-remote-desktop-menu-in-dashboard.png)

The other available options are required for connection via the [local RDP client](#rdp-connection-via-local-client):

* **Reset RDP Password** to reset and resend Administrator credentials
* **Info**, which displays short information on establishing the RDP connection manually
* **RDP link** for establishing the RDP connection via your local client

2\. Remote desktop connection will be established in a new browser tab. 

![remote desktop web client access](03-remote-desktop-web-client-access.png)

Once the connection is established, you’ll see the **Server Manager** window opened. Now, you can start [managing your server](/win-vps-roles-features/).


## RDP Connection via Local Client

In case you prefer to work with a local remote desktop client, you’ll need to use the credentials from the email notification sent to you during the corresponding environment creation. The tools you may want to use are: *Remote Desktop* (for Windows), *KRDC*, *Remina* or *RDesktop* (for Linux), *Microsoft Remote Desktop* (for Mac OS X).

Below, we’ll describe the examples of working with the most common RDP clients for Windows and UNIX-based operating systems:

* [For Windows](#for-windows)
* [For Linux/MacOS/FreeBSD](#for-linuxmacosfreebsd)

### For Windows

1\. Get the **[Microsoft Remote Desktop](https://www.microsoft.com/en-us/p/microsoft-remote-desktop/9wzdncrfj3ps#activetab=pivot:overviewtab)** application and launch it.

2\. Click **Add > PC** at the top of the opened window.

![Windows remote desktop application](04-windows-remote-desktop-application.png)

3\. Provide the RDP connection link ([endpoint](/endpoints/)) into the **PC name** field.

{{%note%}}**Note:** If [public IP](/public-ip/) is attached to the Windows VM node, it <u>*must*</u> be used instead of the endpoint.{{%/note%}}

![provide RDP connection link](05-provide-rdp-connection-link.png)

{{%tip%}}**Tip:** You can get the required link from the after-creation email or via the dashboard:

* **environment settings > endpoints**

![Windows VM RDP endpoint](06-windows-vm-rdp-endpoint.png)

* **Remote Desktop** menu for node

![Windows VM RDP link](07-windows-vm-rdp-link.png)
{{%/tip%}}

4\. Click the **+** button next to **User account** and specify your account credentials (view the appropriate email).

![provide Windows VM access credentials](08-provide-windows-vm-access-credentials.png)

Click **Save** and adjust any additional setting, if needed.

That's all, your connection is saved under the "**Saved Desktops**" section. Click it to start a remote session.

### For Linux/MacOS/FreeBSD

We’ve chosen the ***rdesktop*** utility as an example of the RD client, but you can use other ones (e.g. ***freerdp***). If you haven’t got this tool installed at your local computer, get it using the appropriate command according to your OS package manager (e.g. *yum -y install rdesktop* or *sudo apt-get install rdesktop*).

{{%note%}}**Note:** In order to establish remote connection via the ***rdesktop*** tool, you need to disable the *Network Level Authentication* in the **Remote Desktop** configs of the Windows VM node.

![disable network level authentication](09-disable-network-level-authentication.png)

If you want to keep this setting enabled, you can use other tools, like ***freerdp***.{{%/note%}}

Then open your terminal emulator and follow the next steps:

1\. The easiest way to connect to the remote desktop is to execute the next command:

```
rdesktop {access_url}
```

where ***{access_url}*** is a connection URL for RDP access (can be seen at the dashboard or inside the received email), specified without the protocol-defining part.

![Unix RDP access](10-unix-rdp-access.png)

{{%note%}}**Note:** An environment with the required server should have the *Running* status; otherwise, you’ll receive the *Unable to connect* error.{{%/note%}}

2\. In the opened window, you’ll need to log in with the credentials from the same email.

![Unix RDP credentials](11-unix-rdp-credentials.png)

{{%tip%}}**Note:** Another way is to specify your login and password directly in the connection string: 

```
rdesktop -u {username} -p {password} {access_url}
```

![Unix connection with credentials](12-unix-connection-with-credentials.png)

In such a way, you’ll bypass the login screen and will access the desktop immediately.{{%/tip%}}

Once the authentication is done, you’ll see the remote virtual desktop of the required node opened.

Now, you can start configuring your server using the in-built **Server Manager**.


## What's next?

* [.NET Core (Beta)](/net-core/)
* [Windows VM](/win-vm/)
* [Windows Roles & Features](/win-vps-roles-features/)