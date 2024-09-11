---
draft: false
title: "MySQL/MariaDB/Percona Encryption in Transit"
aliases: "/db-ssl-addon/"
seoindex: "index, follow"
seotitle: "MySQL/MariaDB/Percona Encryption in Transit"
seokeywords: "mysql ssl, mariadb ssl, percona ssl, mysql encryption in transit, mariadb encryption in transit, percona encryption in transit, mysql encryption, mariadb ssl encryption, percona ssl addon"
seodesc: "Learn how to enable SSL/TLS \"encryption in transit\" feature for the MySQL/MariaDB/Percona databases in the Virtuozzo Application Platform."
menu:
    docs:
        title: "Encryption in Transit Add-On"
        url: "/db-ssl-addon/"
        weight: 38
        parent: "mysql"
        identifier: "db-ssl-addon.md"
---

# SSL/TLS Encryption in Transit for MySQL/MariaDB/Percona

MySQL/MariaDB/Percona database solutions are provided with a built-in add-on that implements “**encryption in transit**”. The functionality ensures data protection with SSL/TLS encrypted connection while it moves between servers. After the add-on installation, all the related operations are handled automatically - data encryption before transmission, endpoints authentication, content decryption, and verification upon arrival.


## Add-On Installation

The add-on can be installed on top of the **MySQL/MariaDB/Percona** and **ProxySQL** (for database clusters) nodes only.

1\. In the platform dashboard, go to the **Add-Ons** section of the appropriate database layer, and click **Install** for the *SSL/TLS Encrypted Connection* solution.

{{%tip%}}**Tip:** The add-on is also available from the [Marketplace](/marketplace/) and can be imported from the appropriate GitHub repository.{{%/tip%}}

![MySQL SSL add-on](01-mysql-ssl-addon.png)

2\. Within the opened installation window, select the target **Environment** and **Node Group(s)** where the add-on will be installed.

![install MySQL SSL add-on](02-install-mysql-ssl-addon.png)

{{%note%}}**Note:** Both **MySQL/MariaDB/Percona** and **ProxySQL** (if added) layers should be selected for the clustered solution.{{%/note%}}

Click **Install** to continue.

3\. In a minute, your database will be reconfigured to work over an encrypted connection.

![SSL add-on installed](03-ssl-addon-installed.png)


## Add-On Specifics

Below you can learn about certificates generation processes and specifics:

- Certificates are generated with the ***/usr/local/sbin/selfcertgen*** utility.
- Certificates are self-signed and issued for the hostname of the particular node. It means that each node has a set of own certificates, and you must use the ones corresponding to the accessed node for authentication.
- Certificates are stored within the **/var/lib/jelastic/keys/SSL-TLS** folder (accessible via the ***keys*** shortcut in the file manager). Two subfolders are present:
  - ***server*** – server certificates are used to provide the TLS encryption of connection to the database
  - ***client*** – downloadable client certificates can be used to authenticate client connection to the database server

![SSL add-on certificates](04-ssl-addon-certificates.png)

**MySQL/MariaDB/Percona configurations:**

- All the add-on configurations are provided via a separate ***/etc/mysql/conf.d/ssl-config.cnf*** configuration file:

```
[mysqld]
ssl_cert=/var/lib/jelastic/keys/SSL-TLS/server/server.crt
ssl_key=/var/lib/jelastic/keys/SSL-TLS/server/server.key
ssl-cipher=ECDHE-RSA-AES256-GCM-SHA384:DHE-RSA-AES256-SHA
#require_secure_transport=ON
```

![SSL configuration file](05-ssl-configuration-file.png)

- The config provides paths to server SSL files and lists supported ciphers. Also, it includes an option (commented by default) to make server demand usage of the secure connection. If uncommented, it will be impossible for client to connect this server using the plain non-encrypted connection.

**ProxySQL configurations:**

- SSL on the ProxySQL nodes is enabled by setting the following variables on all the servers:
  - ***[mysql-have_ssl](https://proxysql.com/documentation/global-variables/mysql-variables/#mysql-have_ssl)*** (*true*) - enables SSL for frontend connections
  - ***use_ssl*** (*1*) - sets the corresponding column in **mysql_servers**, which will tell ProxySQL that our backend nodes use SSL
- Changes are done with the following SQL query:

```sql
UPDATE global_variables SET variable_value='true' WHERE variable_name='mysql-have_ssl';
LOAD MYSQL VARIABLES TO RUNTIME; SAVE MYSQL VARIABLES TO DISK;
UPDATE mysql_servers SET use_ssl=1 WHERE port=3306;
LOAD MYSQL VARIABLES TO RUNTIME; LOAD MYSQL SERVERS TO RUNTIME; SAVE MYSQL SERVERS TO DISK;
```


## Add-On Configuration

After the installation, the add-on can be found under the **Add-Ons** tab for the appropriate layer(s). Here, you can generate SSL certificates anew by clicking the **Re-issue certificates** button (e.g. if you think they are compromised or accidentally removed).

![configure MySQL SSL add-on](06-configure-mysql-ssl-addon.png)

To remove the add-on from the layer (including custom configs and generated SSL certificates), expand the menu in the top-right corner of the panel and click **Uninstall**.


## Secure Connection to MySQL/MariaDB/Percona

1\. The “**encryption in transit**” (***server-side encryption***) functionality works immediately after the add-on's installation. You can check it by connecting to the database using the credentials from the email. For remote connection, you can add [endpoint](/endpoints/) or [public IP](/public-ip/):

![database endpoint](07-database-endpoint.png)

Use the following command to connect to the database:

```
mysql --ssl-mode=required -h {host} -P {port} -u {user} -p
```

{{%note%}}**Note:** If you are working with the MariaDB client, replace the “*-\-ssl-mode=required*” option with the “***-\-ssl***” one.{{%/note%}}

Here:

- ***{user}*** - database username for the connection
- ***{host}*** - database entry point (endpoint, in our case)
- ***{port}*** - port for the connection (from the endpoint, in our case)

Once connected, run the ***status*** command and check for the SSL line in the output.

![MySQL remote connection with SSL](08-mysql-remote-connection-with-ssl.png)

2\. While connected to the server, you can configure the use of client certificates for authentication to get ***server- and client-side encryption***. Execute the command below to make SSL auth obligatory for the specified user. For example, we’ll provide “***user-2700607***” (replace the ***{user}*** placeholder) from the email received after the environment creation:

```sql
FLUSH PRIVILEGES;ALTER USER '{user}'@'%' REQUIRE X509;ALTER USER '{user}'@'localhost' REQUIRE X509;FLUSH PRIVILEGES;
```

![alter user command](09-alter-user-command.png)

{{%note%}}**Note:** Common name (CN) is not checked, any certificate signed with this certificate authority (CA) will be considered as appropriate. If you want to check the CN of client certificates (i.e. whether the certificate is issued for the specific user), execute the command below:

```sql
FLUSH PRIVILEGES;ALTER USER '{user}'@'%' REQUIRE SUBJECT 'CN={user}';ALTER USER '{user}'@'localhost' REQUIRE SUBJECT 'CN={user}';FLUSH PRIVILEGES;
```

Also, if you want to use just certificates for login, you can remove password requirement with the *ALTER USER* command as well.{{%/note%}}

Now, provide client server (computer/container/VM) with the appropriate SSL certificate files, which can be downloaded from the **/var/lib/jelastic/keys/SSL-TLS/client** directory of the required target node. Once done, you can connect with the following command:

```
mysql –h {host} -P {port} -u {user} -p --ssl-mode=required --ssl-ca={path/to/root.crt} --ssl-cert={path/to/client.crt} --ssl-key={path/to/client.key}
```

![SSL connection with client certificates](10-ssl-connection-with-client-certificates.png)

{{%tip%}}**Tip:** To avoid specifying certificates as arguments, you can add such options to the ***my.cnf*** file on the client server:

```
[client]
ssl-ca = {path/to/root.crt}
ssl-cert = {path/to/client.crt}
ssl-key = {path/to/client.key}
```
{{%/tip%}}


## What's next?

- [DB Hosting Overview](/database-hosting/)
- [MySQL/MariaDB/Percona Auto-Clustering](/db-auto-clustering/)
- [Remote Access to MySQL/MariaDB/Percona](/remote-access-mysql/)
- [Backup/Restore Add-On](/db-backup-restore-addon/)
- [Corruption Diagnostic Add-On](/db-corruption-diagnostic-addon/)