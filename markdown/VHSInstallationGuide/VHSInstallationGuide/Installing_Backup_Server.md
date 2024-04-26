# Installing Backup Server

Follow the procedure to set up a backup server:

## Installing Static Backup Server

------------------------------------------------------------------------

To install a static backup server, run the following procedure:

1.  Update your server:

    ``` java
    # yum update
    ```

2.  Download the OnApp repository:**
    **

    ``` java
    # rpm -Uvh http://rpm.repo.onapp.com/repo/onapp-repo-7.1.noarch.rpm
    ```

3.  Install the OnApp backup server installer package:

    ``` java
    # yum install onapp-bk-install
    ```

4.  Check and set the backup server default settings:

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

5.  Run the installer. 

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

6.  Сonfigure the backup server for your cloud. This step is also required for the SNMP statistics receiver configuration:

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

7.  Install SSH keys for the backup server by running the following script on the Control Panel server:

    ``` java
    # ssh-copy-id -i /home/onapp/.ssh/id_rsa.pub root@BS_HOST_IP
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
    -   *Backup server zone* - select the backup server zone to which this backup server will be assigned.

-   Move the **Enabled** slider to the right to enable the backup server.
-   Click the **Add Backup Server** button.

``


