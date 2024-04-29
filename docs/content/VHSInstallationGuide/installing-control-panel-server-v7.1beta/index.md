---
draft: false
title: "Installing Control Panel Server v7.1Beta"
aliases: "/installing-control-panel-server-v7.1beta/"
seoindex: "index, follow"
seotitle: "Installing Control Panel Server v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Installing Control Panel Server v7.1Beta"
        url: "/installing-control-panel-server-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "installing-control-panel-server-v7.1beta.md"
---
# Installing Control Panel Server v7.1Beta

Before You Begin

-   Install Control Panel on a server running the AlmaLinux 9 OS.
-   Review the [Virtuozzo Hybrid Server 9 Get Started Guide](https://docs.onapp.com/vhs9gsg/latest) to ensure your environment is ready for installation.
-   Use the corresponding [option](#id-.InstallingControlPanelServerv7.1Beta-installer) of the Control Panel installer if MySQL is already installed and configured.
-   The installer output is redirected to `/onapp-cp-install.log`.
-   All the installer critical errors are written to `/var/log/messages`.
-   To test the upgrade, you may first simulate the upgrade process on the test environment. For more details, refer to the [Configuring Control Panel Environment for Simulation Purposes](https://docs.onapp.com/misc/configuring-control-panel-environment-for-simulation-purposes-6-3-and-up) section. 
-   Disable SELinux before the installation.

To install the Control Panel server, run the following procedure:

1.  Update your server:

    ``` java
    # yum update
    ```

2.  Install the packages required for the OnApp YUM repository file:

    ``` java
    # yum install chkconfig initscripts
    ```

3.  Download the OnApp YUM repository file:

    ``` java
    # rpm -Uvh http://rpm.repo.onapp.com/repo/centos/9/x86_64/RPMS-7.1-PB/onapp-repo-7.1-2.noarch.rpm
    ```

4.  Install the OnApp Control Panel installer package:

    ``` java
    # yum install onapp-cp-install
    ```

5.  **(Optional) **You can set custom configuration options for Control Panel. It is important to set custom values before the installer script runs.

    The full list of custom configuration options for Control Panel.

    Edit the `/onapp/onapp-cp.conf` file to set custom values for Control Panel:

    \#Template server URL

    ``` java
    TEMPLATE_SERVER_URL='http://templates-manager.onapp.com'
    ```

    \# IPs (separated with a comma) list for the SNMP to trap. It is a list of Control Panel IP addresses on which the traps sent from the compute resources are processed.

    ``` java
    SNMP_TRAP_IPS=""
    ```

    \# OnApp Control Panel custom version

    ``` java
    ONAPP_VERSION=""
    ```

    \# OnApp MySQL/MariaDB connection data (`database.yml`)

    ``` java
    ONAPP_CONN_WAIT_TIMEOUT=15
    ONAPP_CONN_POOL=30
    ONAPP_CONN_RECONNECT='true'
    ONAPP_CONN_ENCODING='utf8'
    ```

    \# MySQL/MariaDB server configuration data (in case of local server)

    ``` java
    MYSQL_WAIT_TIMEOUT=604800
    MYSQL_MAX_CONNECTIONS=500
    MYSQL_LIMITNOFILE=8192
    ```

    \# [Use MariaDB instead of MySQL as OnApp database server](https://docs.onapp.com/display/MISC/Install+OnApp+Control+Panel+with+MariaDB+as+database+server) (Deprecated parameter. If you set any values for this parameter, they will not take effect)

    ``` java
    WITH_MARIADB=0
    ```

    \# Configure the database server relative amount of available RAM

    ``` java
    TUNE_DB_SERVER=1
    ```

    \# The number of C data structures that can be allocated before triggering the garbage collector. It defaults to 8 million. Only change this value if you understand what it does.

    ``` java
    RUBY_GC_MALLOC_LIMIT=16000000
    ```

    \# `sysctl.conf net.core.somaxconn `value

    ``` java
    NET_CORE_SOMAXCONN=2048
    ```

    \# The root of the OnApp database dump directory (on the Control Panel box)

    ``` java
    ONAPP_DB_DUMP_ROOT=""
    ```

    \# Remote server's (to store database dumps) IP, user, path, `openssh` connection options, and number of dumps to keep

    ``` java
    DB_DUMP_SERVER=""
    DB_DUMP_USER="root"
    DB_DUMP_SERVER_ROOT="/onapp/backups"
    DB_DUMP_SERVER_SSH_OPT="-o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -o PasswordAuthentication=no"
    KEEP_DUMPS=168
    DB_DUMP_CRON='40 * * * *'
    ```

    \# [Enable monit - tool for managing and monitoring Unix systems
    ](https://docs.onapp.com/display/MISC/OnApp+Services+Monitoring+Tool)

    ``` java
    ENABLE_MONIT=1
    ```

    \# DEPRECATED: If enabled (the `1` value is set) - install (if local box) and configure RabbitMQ Server (messaging system) for the vCloud support. (Deprecated parameter. If you set any values for this parameter, they will not take effect)

    ``` java
    ENABLE_RABBITMQ=1
    ```

    \# Rotate transactions' log files created more than TRANS\_LOGS\_ROTATE\_TIME day(s) ago

    ``` java
    TRANS_LOGS_ROTATE_TIME=30
    ```

    \# Maximum allowed for uploading file size in bytes, from 0 (meaning unlimited) to 2147483647 (2 GB). The default is `0`.

    ``` java
    MAX_UPLOAD_SIZE=0
    ```

    \# Timeout before ping the Redis server to check if it is started. The default is 10 sec.

    ``` java
    REDIS_PING_TIMEOUT=10
    ```

    \# OnApp Control Panel SSL certificates (please do not change if you aren't familiar with SSL certificates)
    \# \* The data below to generate a self-signed PEM-encoded X.509 certificate

    ``` java
    SSL_CERT_COUNTRY_NAME="UK"
    SSL_CERT_ORGANIZATION_NAME='OnApp Limited'
    SSL_CERT_ORGANIZATION_ALUNITNAME='OnApp Cloud'
    SSL_CERT_COMMON_NAME="`hostname --fqdn 2>/dev/null`"
    ```

    \#   SSLCertificateFile, SSLCertificateKeyFile Apache directives' values
    \#   ssl\_certificate, ssl\_certificate\_key Nginx directives' values

    ``` java
    SSLCERTIFICATEFILE="/etc/pki/tls/certs/ca.crt"
    SSLCERTIFICATECSRFILE="/etc/pki/tls/private/ca.csr"
    SSLCERTIFICATEKEYFILE="/etc/pki/tls/private/ca.key"
    ```

    \# \* PEM-encoded CA Certificate (if custom one exists)
    \#   SSLCACertificateFile, SSLCertificateChainFile Apache directives' values
    \#   ssl\_client\_certificate Nginx directives' values

    ``` java
    SSLCACERTIFICATEFILE=""
    SSLCERTIFICATECHAINFILE=""
    ```

    \#   SSLCipherSuite, SSLProtocol Apache directives' values
    \#   ssl\_ciphers, ssl\_protocols Nginx directives' values

    ``` java
    SSLCIPHERSUITE=""
    SSLPROTOCOL=""
    ```

    ``` java
    # vi /onapp/onapp-cp.conf
    ```

    For a successful installation, accept the EULA.

6.  Run the Control Panel installer

        For AlmaLinux 9:

``` java
# /onapp/onapp-cp-install/onapp-cp-install.sh -i SNMP_TRAP_IPS
```

The full list of installer options for Control Panel.

    # /onapp/onapp-cp-install/onapp-cp-install.sh -h
    Usage: /onapp/onapp-cp-install/onapp-cp-install.sh [-c CONFIG_FILE] [--mariadb | --mariadb-custom | --community | --percona | --percona-cluster] [-m MYSQL_HOST] [--mysql-port=MYSQL_PORT] [--mysql-sock[=MYSQL_SOCK] [-p MYSQL_PASSWD] [-d MYSQL_DB] [-u MYSQL_USER] [-U ADMIN_LOGIN] [-P ADMIN_PASSWD] [-F ADMIN_FIRSTNAME] [-L ADMIN_LASTNAME] [-E ADMIN_EMAIL] [-i SNMP_TRAP_IPS] [--redis-host=REDIS_HOST] [--redis-bind[=REDIS_BIND] [--redis-passwd[=REDIS_PASSWD] [--redis-port=REDIS_PORT] [--redis-sock[=REDIS_SOCK] [--rbthost RBT_HOST] [--vcdlogin VCD_LOGIN] [--vcdpasswd VCD_PASSWD] [--vcdvhost VCD_VHOST] [--rbtlogin RBT_LOGIN] [--rbtpasswd RBT_PASSWD] [-a] [-y] [-D] [-t] [--noservices] [--ha-install] [--rake=RAKE_TASKS] [--quick|--quick-update[=SERVICE] [--accept-eula] [-w] [-h]

        Database server options:
                               Default database SQL server is MySQL Server.

                               Please use one of the following option to install LOCALLY:
                               --mariadb         : MariaDB Server
                   --mariadb-custom  : MariaDB Server (custom for AlmaLinux 9 only)
                               --community       : MySQL Community Server
                               --percona         : Percona Server
                               --percona-cluster : Percona Cluster

                               -m MYSQL_HOST   : MySQL host. Default is 'localhost'
                               --mysql-port=MYSQL_PORT    : TCP port where MySQL Server serves connections.
                                                           Default values is 3306 for the local installation
                               --mysql-sock[=MYSQL_SOCK] : Unix socket on which MySQL Server serves connections.
                                                           Default values is /var/lib/mysql/mysql.sock. Used if local server only
                                                           The socket is unset if the option's argument isn't specified.
                               -p MYSQL_PASSWD : MySQL password. Random is generated if is not set or specified.
                               -d MYSQL_DB     : OnApp MySQL database name. Default is 'onapp'
                               -u MYSQL_USER   : MySQL user. Default is 'root'


        Redis Server options:

                               --redis-host=REDIS_HOST : IP address/FQDN where Redis Server runs. It is used by Control Panel to connect to Redis Server.
                                                         The Redis Server will be installed and configured on the current box if localhost/127.0.0.1 or box's public IP address (listed in SNMP_TRAP_IPS) is specified.
                                                         Default value is 127.0.0.1.
                                                         If local Redis, it will serve as well on the unix socket 'PORT' (if --redis-sock without argument isn't specified)
                               --redis-bind[=REDIS_BIND] : The IP address for Redis Server to serve connections (to listen)
                                                           The option isn't mandatory.

                               --redis-port=REDIS_PORT : Redis Server listen port.
                                                         Defaults are:
                                                           0 - if local server
                                                           6379 - if remote server
                               --redis-passwd[=REDIS_PASSWD] : Redis Server password to authentificate.
                                                               Random password is generated if the option's argument isn't specified.
                                                               By default no password is used for local Redis.
                               --redis-sock[=REDIS_SOCK] : Path to the Redis Server's socket. Used if local server only.
                                                         Default is /var/run/redis/redis.sock
                                                         The socket is unset if the option's argument isn't specified.


        Options to manage OnApp Control Panel administrator account:
                                                    Please note, that these options are for NEW INSTALL only and not for upgrade

                               -P ADMIN_PASSWD    : CP administrator password
                               -F ADMIN_FIRSTNAME : CP administrator first name
                               -L ADMIN_LASTNAME  : CP administrator last name
                               -E ADMIN_EMAIL     : CP administrator e-mail


         RabbitMQ Server and vCloud options:

                               --rbthost   RBT_HOST   : IP address/FQDN where RabbitMQ Server runs.
                                                        The RabbitMQ will be installed and configured on the current box if localhost/127.0.0.1 or box's public IP address (enlisted in SNMP_TRAP_IPS)
                                                        Default values is 127.0.0.1.

                                  VCD_*      : Options are usefull if vCloud/RabbitMQ are already installed and configured.

                               --vcdlogin  VCD_LOGIN  : RabbitMQ/vCloud user. Default value is 'rbtvcd'.
                               --vcdpasswd VCD_PASSWD : RabbitMQ/vCloud user password. The random password is generated if isn't specified.
                               --vcdvhost  VCD_VHOST  : RabbitMQ/vCloud vhost. Default value is '/'

                                  RBT_*         : Options are used to configure RabbitMQ manager account. If local RabbitMQ server.

                               --rbtlogin  RBT_LOGIN  : RabbitMQ manager login. The default value is 'rbtmgr'.
                               --rbtpasswd RBT_PASSWD : RabbitMQ manager password. The random password is generated if isn't specified.


         General options:

                               --ha-install : Proceed with Control Panel and Hight Availability components installation
                                  RHEL/AlmaLinux 9 is supported only!

                               --rake RAKE_TASKS : List of OnApp Control Panel rake tasks (separated with space) to run at the very end of install or upgrade

                               -i SNMP_TRAP_IPS : IP addresses separated with comma for snmp to trap

                               -y : Update OS packages (except of OnApp provided) on the box with 'yum update'.

                               -a : Do not be interactive. Process with automatic installation.
                                    Please note, this will continue OnApp Control Panel install/upgrade even there is transaction currently running.

                               -t : Add to the database and download Base Templates. For new installs only.

                               --noservices : Do not start OnApp services: monit, onapp and httpd
                                              Please note, crond and all OnApp's cron tasks remain running. They could be disabled by stopping crond service manually for your own risk.

                               -D : Do not make database dump, and make sure it is disabled in the cron and not running at the moment

                               -w : Do not disable iptables service.
                                    Is applicable on fresh installs only.

                               --quick|--quick-update[=SERVICE] : Procceed with quick update procedure. 
                                                     This will skip update and configure for services, like: system packages, MySQL database, Redis Server, RabbitMQ Server, Monit service
                                                     Set the SERVICE parameter (space separated list of statements) to define services, which update is needed.
                                                     Possible reserved statements are:
                                                         rpms - for 'system packages' upgrade;
                                                         mysql - for MySQL databse upgrade ond configuring;
                                                         redis - for ERedis Server upgrade and configuring;
                                                         rabbitmq - for RabbitMQ Server upgrade and configuring;
                                                         monit - for Monit upgrade and configuring.

                   --accept-eula : Automatically accept OnApp's End User License Agreement
                                   (DEPRICATED)

                               -c CONFIG_FILE   : Custom installer configuration file. Otherwise, preinstalled one is used.

                               -h : print this info

**Where:**
** Database server options:**
The default database SQL server is a MySQL server. Please use one of the following options to install LOCALLY.
`--mariadb`
MariaDB server.
`--community`
MySQL community server.
`--percona`
Percona server.
`--percona-cluster`
Percona cluster.
`MYSQL_*`
Options are useful if MySQL is already installed and configured.
`-m MYSQL_HOST`
MySQL host. The default is `localhost`.
`--mysql-port=MYSQL_PORT`
The TCP port where MySQL Server serves connections. The default value is `3306` for the local installation.
` --mysql-sock[=MYSQL_SOCK]`
The Unix socket on which the MySQL server serves connections. The default value is `/var/lib/mysql/mysql.sock`.
Used if the local server only. The socket is unset if the option's argument isn't specified.
`-p MYSQL_PASSWD`
MySQL password. Random is generated if not set or specified.
`-d MYSQL_DB`
OnApp MySQL database name. The default is `onapp`.
`-u MYSQL_USER`
MySQL user. The default is `root`.
**Redis server options:**
`REDIS_*`
Options are useful if the Redis server is already installed and configured.
`--redis-host=REDIS_HOST `
The IP address/FQDN where the Redis server runs. It is used by Control Panel to connect to the Redis server.
The Redis server will be installed and configured on the current box if `localhost/127.0.0.1` or the box's
public IP address (listed in `SNMP_TRAP_IPS`) is specified. The default value is `127.0.0.1`.
If the local Redis, it will serve as well on the Unix socket 'PORT' (if `--redis-sock` without argument isn't specified).
`--redis-bind[=REDIS_BIND]`
The IP address for Redis server to serve connections (to listen). The option isn't mandatory.
`--redis-port=REDIS_PORT`
Redis Server listen port.
The defaults are as follows:
`0` - if a local server
`6379` - if a remote server
`--redis-passwd[=REDIS_PASSWD]`
The Redis server password to authenticate.
A random password is generated if the option's argument isn't specified.
By default, no password is used for the local Redis.
`--redis-sock[=REDIS_SOCK]`
The path to the Redis server's socket. Used if local server only. The default is `/var/run/redis/redis.sock`.
The socket is unset if the option's argument isn't specified.
 **Options to manage the OnApp Control Panel administrator account:**
`ADMIN_*`
Options are used to configure OnApp Control Panel administrator data.
Please note that these options are for NEW INSTALL only and not for upgrade.
`-P ADMIN_PASSWD`

CP administrator password.
`-F ADMIN_FIRSTNAME`
CP administrator first name.
`-L ADMIN_LASTNAME`
CP administrator last name.
`-E ADMIN_EMAIL`
CP administrator email.
**RabbitMQ Server and vCloud options:**
`  --rbthost   RBT_HOST  `
The IP address/FQDN where the RabbitMQ server runs. The RabbitMQ will be installed and configured on the current box
if `localhost/127.0.0.1` or box's public IP address (enlisted in `SNMP_TRAP_IPS`). The default value is `127.0.0.1`.
`VCD_*`
Options are useful if vCloud/RabbitMQ is already installed and configured.
`--vcdlogin  VCD_LOGIN`
RabbitMQ/vCloud user. The default value is `rbtvcd`.
`--vcdpasswd VCD_PASSWD`
RabbitMQ/vCloud user password. The random password is generated if not specified.
`--vcdvhost  VCD_VHOST`
RabbitMQ/vCloud vhost. The default value is `/`.
`RBT_*  `
Options are used to configure RabbitMQ manager account. If local RabbitMQ server.
`--rbtlogin  RBT_LOGIN `
RabbitMQ manager login. The default value is `rbtmgr`.
`--rbtpasswd RBT_PASSWD`
RabbitMQ manager password. The random password is generated if not specified.
**General options:**
`--rake RAKE_TASKS`
A list of OnApp Control Panel rake tasks (separated with space) to run at the very end of installation or upgrade.
`-i SNMP_TRAP_IPS`
IP addresses are separated with a comma for SNMP to trap.
`-y`
Update OS packages (except for OnApp provided) on the box with `yum update`.
`-a`
Is not interactive. Process with automatic installation. Please note it will continue OnApp Control Panel installation/upgrade even if there is a transaction currently running.
`-t`
Add to the database and download Base Templates. For new installations only. If this option is not used, only the following mandatory system templates will be added by default during fresh installation: OnApp CDN Appliance; Load Balancer Virtual Appliance; Application Server Appliance.
`--noservices`
Do not start OnApp services: `monit`, `onapp`, and `httpd`.
Please note, `crond` and all OnApp's `cron` tasks remain running. They could be disabled by stopping the `crond` service manually for your own risk.

`-D`
Do not make a database dump, and make sure it is disabled in the `cron` and not running at the moment.
`-w`
Do not disable the iptables service. It is applicable on fresh installs only.

`--quick|--quick-update[=SERVICE] `
Proceed with the quick update procedure. This will skip an update and configuration for services, such as system packages, MySQL database, Redis Server, RabbitMQ Server, and Monit service. Set the `SERVICE` parameter (space-separated list of statements) to define services, which need to be updated. Possible reserved statements are:                  
`rpms` - for 'system packages' upgrade.
`mysql` - for MySQL database upgrade and configuration.
`redis` - for Redis server upgrade and configuration.
`rabbitmq` - for RabbitMQ server upgrade and configuration.
`monit` - for Monit upgrade and configuration.
`--accept-eula`
Automatically accept the OnApp's End User License Agreement.
`-c CONFIG_FILE`
Custom installer configuration file. Otherwise, a preinstalled one is used.
`-h`
Print this info.

    7. Install an OnApp license to activate your Control Panel. Enter a valid license key via the OnApp UI. Your default OnApp credentials are **admin/changeme**. You can change a password via the Control Panel &gt; **Users** menu.

After you enter a license key, it may take up to 15 minutes to activate the key.

   8. Restart the OnApp service:

``` java
# service onapp restart
```

   9. If you add additional compute resources to an existing cloud, update the `authorized_keys` file by running the following script on the Control Panel server:

``` java
# ssh-copy-id -i /home/onapp/.ssh/id_ed25519.pub root@HV_HOST_IP
```

10. From the Control Panel server, enter the compute resource server from the OnApp user via SSH to add it to .ssh/known\_hosts:

``` java
su onapp
ssh root@HV_HOST_IP
```

**Perform the following step (11) if you do not plan to install a dedicated backup server.**

   11. Mount the locations for templates and backups. If you do not have a dedicated backup server, you must mount your template and backup repositories to compute resources. If your template and backup repositories are located on the Control Panel server, you can mount them as follows:        Add the repositories to `/etc/exports` on the Control Panel server and then restart the NFS service:

``` java
# /onapp/templates 192.168.10.0/24(rw,no_root_squash)
# /onapp/backups 192.168.10.0/24(rw,no_root_squash)
```

After the configuration is completed, Control Panel will be available in both http and https protocols. For security reasons, we recommend either closing port 80 or opening port 443. This port is used for secure web browser communication. Data transferred across such connections are highly resistant to interception. Moreover, the identity of the remotely connected server can be verified with significant confidence. 

If you use a time zone with 30-minute or 45-minute offsets, you need to modify the configuration file `/etc/crontab` and change the startup time (`rake vm:generate_hourly_stats`) from 0th minute to 30th or 45th minute, depending on a time zone.

In the script, replace
`0 * * * * onapp cd /onapp/interface; RAILS_ENV=production rake vm:generate_hourly_stats`
with
`30 * * * * onapp cd /onapp/interface; RAILS_ENV=production rake vm:generate_hourly_stats`

12. After adding the backup server, copy virtual server templates from your Control Panel to the configured backup server. Inside your Control Panel, perform the following CLI commands:

``` java
su - onapp
scp  /onapp/templates/*  root@backup_server_ip:/onapp/templates/  
```


