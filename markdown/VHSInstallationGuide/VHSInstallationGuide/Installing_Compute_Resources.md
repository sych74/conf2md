# Installing Compute Resources

After successfully installing the Control Panel server, follow the procedures to set up static compute resources.

## Installing Static Compute Resources

------------------------------------------------------------------------

Before You Proceed

-   Install base Virtuozzo Hybrid Server packages on the local drive before compute resource installation, depending on which virtualization method you choose:
    -   KVM compute resources: Virtuozzo Hybrid Server 9
-   Disable CPU power-saving features in BIOS before you proceed to the compute resource installation.
-   If you are not using a dedicated backup server in your cloud setup, configure the NFS server with the following options to preserve the file owner and group settings during template unpacking on NFS storage:  
    -   `no_root_squash`
    -   `no_all_squash`

**To install a compute resource:**

1.  Update your server:

    ``` java
    # yum update
    ```

2.  Download the OnApp repository:

    ``` java
    # rpm -Uvh http://rpm.repo.onapp.com/repo/onapp-repo-7.1.noarch.rpm
    ```

3.  Install the OnApp compute resource installer package:

    ``` java
    # yum install onapp-hv-install 
    ```

4.  Edit custom configuration for a compute resource. Custom values must be set before the installer script runs.

    ``` java
    # vi /onapp/onapp-hv.conf
    ```

    The full list of custom values for a compute resource.

    -   Enable Monit, the tool for managing and monitoring Unix systems:

        ``` java
        ENABLE_MONIT=1
        ```

    <!-- -->

    -   Default server to sync time on the compute resource:

        ``` java
        NTP_TIME_SERVER='pool.ntp.org'
        ```

    -   Xen HV (Domain-0) related configuration:

        ``` java
        XEN_DOM0_MEM_MIN=409600
        XEN_DOM0_MEM_DEVISOR=48
        XEN_DOM0_MAX_VCPUS=""
        XEN_DOM0_VCPUS_PIN_ENABLE=0
        XEN_DOM0_SCHEDULER_WEIGHT=65535
        XEN_DOM0_SCHEDULER_CAP=200
        # 4.2.x and higher versions only
        XEN_DOM0_SCHEDULER_RATELIMIT_US=100
        XEN_DOM0_SCHEDULER_TIMESLICE_MS=5
        ```

    -   The number of loopback devices created:

        ``` java
        LOOPBACKS=128
        ```

    -   The maximum size of the connection tracking table.

        The value can't be greater than 65536 if the total memory of Xen Domain-0 or KVM is less than 1 Gb.
        The value can be doubled (or even more, depending on the memory amount).

        ``` java
        NET_IPV4_NETFILTER_IP_CONTRACK_MAX=""
        ```

    -   The divisor to calculate the hash table. The recommended value is 8.

        ``` java
        hashsize = nf_conntrack_max / 8
        CONTRACK_TO_HASHSIZE=8
        ```

    -   Outdated Xen compute resource's (Domain-0) configuration parameters:

        ``` java
        XEN_DOM0_MEM_OVERHEAD_MIN=262144
        P_TO_VCPUS=4
        ```

5.  Run the OnApp compute resource installer script: 

    ``` java
    # /onapp/onapp-hv-install/onapp-hv-kvm-install.sh 
    ```

    The full list of KVM installer options

    **Usage: **

    ``` java
    # /onapp/onapp-hv-install/onapp-hv-kvm-install.sh [-c CONFIG_FILE] [-a] [-y] [-t] [-s] [-x] [-v HV_VERSION] [-p API_VERSION] [-h]
    ```

    **Where:**

    |                  |                                                                                                                                                     |
    |------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
    | `-c CONFIG_FILE` | Custom installer configuration file. Otherwise, the pre-installed one is used.                                                                      |
    | `-a`             | Do NOT be interactive. Process with automatic installation.                                                                                         |
    | `-v HV_VERSION`  | Custom compute resource tool version.                                                                                                               |
    | `-p API_VERSION` | Custom StorageAPI version.                                                                                                                          |
    | `-t`             | Initiate Recovery templates and ISO(s), which are used to provision FreeBSD guests, download. The download is initiated if the `-a` option is used. |
    | `-y`             | Update OS packages (except those provided by OnApp for a compute resource) with `yum update`. Useful for an update (not for fresh installation).    |
    | `-s`             | Skip packages management: install, remove, upgrade. Useful for an update (not for fresh installation).                                              |
    | `- x`            | Skip `kvm`, `kernel`, and `libvirt` (compute resource-related RPM) package management. Useful for an update (not for fresh installation).           |
    | `- d`            | Install OnApp Storage-related packages. Applicable to Virtuozzo Hybrid Server 9 only.                                                               |
    | `-h`             | Print this info.                                                                                                                                    |

6.  Configure the compute resource for your cloud. This step is also required for the SNMP statistics receiver configuration:

    ``` java
    # /onapp/onapp-hv-install/onapp-hv-config.sh -h <CP_HOST_IP> -p <HV_HOST_IP> -b <HV_BSNET_IP>
    ```

    The full list of compute resource (both Xen and KVM) configuration options.

    **Usage: **

    ``` java
    # /onapp/onapp-hv-install/onapp-hv-config.sh [-h CP_HOST_IP] [-p HV_HOST_IP] [-b HV_BSNET_IP] [-f FTS_IP] [-l LVM_HOST_ID] [-a|-i [USER:PASSWD]] [-s] -?
    ```

    **Where:
    **

    |                   |                                                                                                                                                                                                     |
    |-------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
    | `-h CP_HOST_IP`   | The FQDN or IP addresses (separated by a comma) of the management server, which should receive all status reports and are authoritative for this compute resource. Used by `snmpd` and `snmptrapd`. |
    | `-p HV_HOST_IP`   | The FQDN or IP address of the server (compute resource) which will serve all stats-related and other requests sent by the `CP_HOST_IP`. Used by `snmpd`, `snmptrapd`, and StorageAPI.               |
    | `-b HV_BSNET_IP`  | The compute resource's IP address from backup servers' network. Used to bind the SCSI target daemon.                                                                                                |
    | `-f FTS_IP`       |  The File Transfer Server FQDN or IP address used for daily `cron` update recovery ISO by `recovery.sh`                                                                                             
                                                                                                                                                                                                                              
                         If unsure, set the Control Panel server's management IP as `CP_HOST_IP` and `FILE_TRANSFER_SERVER_IP`.                                                                                               |
    | ` -l LVM_HOST_ID` | The `lvmlockd sanlock host_id`. The ID should be unique for each compute resource in the cloud. Its value for static compute resources are between 257 and 2000.                                    |
    | `-a`              |  Install AoE.                                                                                                                                                                                       |
    | `-s`              |  Install SSHFS.                                                                                                                                                                                     |
    | `-?`              |  Print this help info.                                                                                                                                                                              |

7.  If requested by the installer, reboot the compute resource to complete the installation:

    ``` java
    # shutdown -r now
    ```

    Perform the steps from 9 to 11 if you haven't installed SSH keys for the compute resource yet. You may proceed to step 10 if you want to install all compute resources or install a particular compute resource at step 11.

8.  Generate SSH keys that OnApp requires for you to access various elements. The script provided will generate and transfer keys as necessary. The script needs to be run on your Control Panel server. It will overwrite any keys that already exist, so if you have custom keys already installed, add them again after running the script. The script will ask you for your login details to various servers during the execution. Please follow the onscreen instructions.
9.  If you install a new cloud instance, connect to your Control Panel server via SSH, download, and run the script:

    ``` java
    # wget http://downloads.repo.onapp.com/install-all-keys.sh
    # /bin/sh install-all-keys.sh
    ```

10. If you add additional compute resources to an existing cloud, update the `authorized_keys` file by running the following script on the Control Panel server:

    ``` java
    # ssh-copy-id -i /home/onapp/.ssh/id_rsa.pub root@HV_HOST_IP
    ```

    Perform the following step 12 if you do not plan to install a dedicated backup server.

11. If you do not have a dedicated backup server, you must mount your template and backup repositories to compute resources. If your template and backup repositories are located on the Control Panel server, you can mount them as follows:

    Ensure that locations are added to `/etc/exports` on the Control Panel server and then reboot.

    ``` java
    # /onapp/templates 192.168.10.0/24(rw,no_root_squash)
    # /onapp/backups 192.168.10.0/24(rw,no_root_squash)
    ```

    Add locations to `/etc/rc.local` on the compute resource and run them manually on the command line (in this example, we are mounting from `192.168.10.101`).

    ``` java
    # mkdir -p /onapp/backups && mount -t nfs 192.168.10.101:/onapp/backups /onapp/backups
    # mkdir -p /onapp/templates && mount -t nfs 192.168.10.101:/onapp/templates /onapp/templates
    ```

12. Mount ISO locations:

    To build virtual servers from ISO images, it is required to mount and share the location where the ISOs are stored at the Control Panel server with all the compute resources. When virtual servers are booted from ISOs, the ISO image is taken from the compute resource server. The location is preconfigured in the `onapp.yml` config file:

    -   `iso_path_on_cp` - specifies the location where ISOs are stored on the Control Panel server. By default, the location is `/data`. You can change it to any other suitable location. Make sure that this location is shared with the specified iso\_path\_on\_hv location.
    -   `iso_path_on_hv` - specifies the location where ISOs are located on the compute resource servers. By default, the location is `/data`.  You can change it to any other suitable location with the `onappowner` user and read/write access. Make sure that this location is mounted to the specified `iso_path_on_cp `location`.`

    ISOs can be hosted on a dedicated server at any desired location with an arbitrary name if you want. In this case, it is necessary to mount the ISOs location on this server to the Control Panel `iso_path_on_cp` directory and all the compute resources `iso_path_on_hv` locations. This can be a backup server to avoid the excess usage of the Control Panel resources.

13. Add the compute resource to your cloud using your Control Panel: **Admin **&gt; **Settings **&gt;** Compute resources **&gt;** Add New Compute Resource**.
    Ensure that the compute resource is visible in your Control Panel.


