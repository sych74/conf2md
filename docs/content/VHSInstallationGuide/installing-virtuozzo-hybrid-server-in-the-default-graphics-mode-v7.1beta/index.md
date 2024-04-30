---
draft: false
title: "Installing Virtuozzo Hybrid Server in the Default Graphics Mode v7.1Beta"
aliases: "/installing-virtuozzo-hybrid-server-in-the-default-graphics-mode-v7.1beta/"
seoindex: "index, follow"
seotitle: "Installing Virtuozzo Hybrid Server in the Default Graphics Mode v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Installing Virtuozzo Hybrid Server in the Default Graphics Mode v7.1Beta"
        url: "/installing-virtuozzo-hybrid-server-in-the-default-graphics-mode-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "installing-virtuozzo-hybrid-server-in-the-default-graphics-mode-v7.1beta.md"
---
# Installing Virtuozzo Hybrid Server in the Default Graphics Mode v7.1Beta

To install Virtuozzo Hybrid Server in graphics mode, choose **Install Virtuozzo Hybrid Server** on the welcome screen. After the installation program loads, you will see the **Installation Summary** screen. On this screen, you need to specify the number of parameters required to install Virtuozzo Hybrid Server.

## Accepting EULA

------------------------------------------------------------------------

You need to accept the Virtuozzo Hybrid Server End-User License Agreement to install Virtuozzo Hybrid Server.

To accept the Virtuozzo Hybrid Server EULA, open the **EULA** screen, select **Accept**, and click **Done**.

![](attachments/194478151/194478387.png){.image-center width="450"}

## Setting Date and Time

------------------------------------------------------------------------

If you need to set the date and time for your Virtuozzo Hybrid Server installation, open the **DATE & TIME** screen and make the necessary changes.

## Selecting the Keyboard Layout

------------------------------------------------------------------------

The selected keyboard layout can be used during installation and, once the installation is complete, in the console (for example, for entering localized descriptions, configuration file comments, and such).

If you need to change the default English (US) keyboard layout, open the **KEYBOARD** screen, click the plus sign to add a layout, and click **Options** to choose a key combination for switching layouts.

![](attachments/194478151/194478391.png){.image-center width="450"}

## Configuring Network

------------------------------------------------------------------------

Usually network is configured automatically by the installation program. If you need to modify network settings, you can do so on the **NETWORK & HOST NAME** screen.

To install Virtuozzo Hybrid Server, you will need to have at least one network card configured and you will also need to provide a hostname: either a fully qualified domain name (`.`) or a short name (``).

![](attachments/194478151/194478393.png){.image-center width="450"}

### Creating Bonded and Teamed Connections

Bonded and teamed connections offer increased throughput beyond the capabilities of a single network card as well as improved redundancy.

During installation, you can configure bonding on the **NETWORK & HOSTNAME** screen as described below. Teaming can be configured in a similar way after choosing **Team** on step 1.

1.  To add a new bonded connection, click the plus button in the bottom, select **Bond** from the drop-down list, and click **Add**.

    ![](https://docs.virtuozzo.com/virtuozzo_hybrid_server_7_installation_guide/_images/stor_install1.png){.align-center .image-center width="450"}

2.  In the **Editing Bond connection…** window, set the following parameters:

    1.  **Mode** to `XOR`.

    2.  **Link Monitoring** to `MII (recommended)`.

    3.  **Monitoring frequency**, **Link up delay**, and **Link down delay** to `300`.

    ![](https://docs.virtuozzo.com/virtuozzo_hybrid_server_7_installation_guide/_images/stor_install2.png){.align-center .image-center width="450"}

    It is also recommended to manually set `xmit_hash_policy` to `layer3+4` after the installation as detailed in [Setting Up Network Bonding](https://docs.virtuozzo.com/virtuozzo_storage_administrators_command_line_guide/maximizing-cluster-performance/setting-up-network-bonding.html#setting-up-network-bonding). For more information on network bonding, see [Red Hat Enterprise Linux Deployment Guide](index) and [Linux Ethernet Bonding Driver HOWTO](https://www.kernel.org/doc/Documentation/networking/bonding.txt).

3.  In the **Bonded connections** section on the **Bond** tab, click **Add**.

4.  In the **Choose a Connection Type** window, select **Ethernet** from the in the drop-down list, and click **Create**.

    ![](https://docs.virtuozzo.com/virtuozzo_hybrid_server_7_installation_guide/_images/stor_install3.png){.align-center .image-center width="450"}

5.  In the **Editing bond slave…** window, select a network interface to bond from the **Device** drop-down list.

## Choosing the Installation Destination

------------------------------------------------------------------------

Open the **INSTALLATION DESTINATION** screen. If you have multiple disks, select which one will be system.

At the bottom of the screen, you can choose:

-   **Automatically configure partitioning** and click **Done** to have the installation program create the default layout on the server.

-   **I will configure partitioning** and click **Done** to partition your disk(s) manually.

When installing the Virtuozzo Hybrid Server with the default graphic mode and automatically configured partitioning, the default file system of the root partition is ext4. The option of manually selecting the XFS file system in the manual partitioning mode is unavailable. This feature will be implemented in future versions.

All disks recognized by the installation program will be cleaned from partitions once you click **Begin Installation**.

Click **Done** and proceed to finish the installation.

## Creating Root Password

------------------------------------------------------------------------

Click **ROOT PASSWORD** to create a password for the root account. Installation will not begin until the password is created.

![](attachments/194478151/194478400.png){.image-center width="450"}

## Finishing the Installation

------------------------------------------------------------------------

Having configured everything necessary on the **INSTALLATION SUMMARY** screen, click **Begin Installation**.

![](https://docs.virtuozzo.com/virtuozzo_hybrid_server_7_installation_guide/_images/vzinstall16.png){.align-center .image-center width="450"}

### Completing Installation

Once the installation has been complete, click **Reboot** to restart the server.

![](https://docs.virtuozzo.com/virtuozzo_hybrid_server_7_installation_guide/_images/vzinstall18.png){.align-center .image-center width="450"}

If you are installing Virtuozzo Hybrid Server from a USB drive, remove the drive before restarting the server.

After restarting the server, activate a license with the `vzlicload` command:

``` java
vzlicload -p <your_license_key>
```

is an activation key that you can get from your sales manager or by filling in the [contact form](https://www.virtuozzo.com/company/contact/).

For more information about licenses, see [Installing the License](installing-the-license-v7.1beta).

## Attachments:

![](images/icons/bullet_blue.gif){width="8" height="8"} [vzinstall1\_0.png](attachments/194478151/194478288.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [vzinstall1\_1.png](attachments/194478151/194478290.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [vzinstall2.png](attachments/194478151/194478293.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [vzinstall3.png](attachments/194478151/194478296.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [vzinstall4.png](attachments/194478151/194478299.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2024-1-31\_15-18-51.png](attachments/194478151/194478385.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2024-1-31\_15-21-18.png](attachments/194478151/194478387.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2024-1-31\_15-23-30.png](attachments/194478151/194478389.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2024-1-31\_15-24-39.png](attachments/194478151/194478391.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2024-1-31\_15-25-53.png](attachments/194478151/194478393.png) (image/png)
![](images/icons/bullet_blue.gif){width="8" height="8"} [image2024-1-31\_15-42-39.png](attachments/194478151/194478400.png) (image/png)

