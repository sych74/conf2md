---
draft: false
title: "Installing Backup Server v7.1Beta"
aliases: "/installing-backup-server-v7.1beta/"
seoindex: "index, follow"
seotitle: "Installing Backup Server v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Installing Backup Server v7.1Beta"
        url: "/installing-backup-server-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "installing-backup-server-v7.1beta.md"
---
# Installing Backup Server v7.1Beta

Follow the procedure to set up a backup server:

## Installing Static Backup Server

------------------------------------------------------------------------

To install a static backup server, run the following procedure:

1.  Update your server:

    ``` java
    # yum update
    ```

2.  Install the OnApp backup server installer package:

    ``` java
    # yum install onapp-bk-install
    ```

3.  Check and set the backup server default settings:

    ``` java
    # vi /onapp/onapp-bk.conf
    ```

    Edit the backup server default settings in the /onapp/onapp-bk.conf file.

    **
    Default server to synch time on the HV**

    ``` java
    NTP_TIME_SERVER='pool.ntp.org'
    ```

    **The number of retries for WGET to download the file**

    ``` java
    WGET_TRIES=5
    ```

    **OnApp templates directory
    **

    Please refer to the corresponding settings at OnApp Control Panel web interface.

    ``` java
    TEMPLATES_DIR='/onapp/templates'
    ```

    **OnApp backups directory
    **

    Please refer to the corresponding settings at OnApp Control Panel web interface.

    ``` java
    BACKUPSS_DIR='/onapp/backups'
    ```

4.  Run the installer. 

    ``` java
    # sh /onapp/onapp-bk-install/onapp-bk-install.sh 
    ```

    The full list of installer options.

    **Usage**:

    ``` java
    # /onapp/onapp-bk-install/onapp-bk-install.sh [-c CONFIG_FILE] [-a] [-y] [-b] [-v BK_VERSION] [-p API_VERSION] [-h]
    ```

    **Where: **

    |                   |                                                                                |
    |-------------------|--------------------------------------------------------------------------------|
    | `-c CONFIG_FILE ` | Custom installer configuration file. Otherwise, the pre-installed one is used. |
    | `-a `             | Do NOT be interactive. Process with automatic installation.                    |
    | `- v BK_VERSION`  | Custom backup tools version.                                                   |
    | `- p API_VERSION` | Custom StorageAPI version.                                                     |
    | `-y `             | Update OS packages (except for the ones provided by OnApp) with `yum update`.  |
    | `- b`             | Initiate the Base templates download.                                          |
    | `-h `             | Print this info.                                                               |

5.  Сonfigure the backup server for your cloud. This step is also required for the SNMP statistics receiver configuration:

    ``` java
    # /onapp/onapp-bk-install/onapp-bk-config.sh -h <CP_HOST_IP> -p <BK_HOST_IP>
    ```

    The full list of configuration options.

    **Usage**:

    ``` java
    # /onapp/onapp-bk-install/onapp-bk-config.sh [-h CP_HOST_IP] [ -p BK_HOST_IP] [-a|-i [USER:PASSWD]] [-s] -?
    ```

    **Where:**

    |                    |                                                                                                                                |
    |--------------------|--------------------------------------------------------------------------------------------------------------------------------|
    | `-h CP_HOST_IP`    | The FQDN or IP address of the management server which receives all status reports and is authoritative for this backup server. |
    | `-p BK_HOST_IP`    | The FQDN or IP address of the backup server that will serve all stats-related and other requests sent by the `CP_HOST_IP`.     
                                                                                                                                                          
                          Used by SNMPD and StorageAPI.                                                                                                   |
    | `-a`               |  Install AoE.                                                                                                                  |
    | `-i [USER:PASSWD]` |  Install iSCSI utils and configure with `USER` and `PASSWD` (if specified).                                                    |
    | `-s`               |  Install SSHFS.                                                                                                                |
    | `-?`               |  Print this help info.                                                                                                         |

6.  Install SSH keys for the backup server by running the following script on the Control Panel server:

    ``` java
    # ssh-copy-id -i /home/onapp/.ssh/id_ed25519.pub root@BS_HOST_IP
    ```

7.  From the Control Panel server, enter the compute resource server from the OnApp user via SSH to add it to .ssh/known\_hosts:

    ``` java
    su onapp
    ssh root@HV_HOST_IP
    ```

8.  Add a backup server via the Control Panel user interface:
    -   Go to your Control Panel &gt; **Admin **&gt;* ***Settings** menu and click the **Backup Servers** icon.
    -   Click the **Create Backup Server** button.
    -   Fill in the form that appears:

    <!-- -->

    -   *Label* - give your backup server a label.
    -   *IP address* - enter the backup server IP address (IPv4).
    -   *Backup IP address* - add a provisioning network IP address.
    -   *Capacity* - set the backup server capacity (in GB).
    -   *Backup server zone* - select the backup server zone to which this backup server will be assigned. For more information on adding or editing backup server zones, see the [Backup Server Zones Settings](https://docs.onapp.com/vhs9ag/latest/storage-and-backups/backup-settings/backup-server-zones-settings) section.

-   Move the **Enabled** slider to the right to enable the backup server.
-   Click the **Add Backup Server** button.

Inside your Control Panel, perform the following CLI commands:

``` java
su - onapp
scp  /onapp/templates/*  root@backup_server_ip:/onapp/templates/  
```

``


