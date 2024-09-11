---
draft: false
title: "Redis Encryption in Transit"
aliases: "/redis-ssl-addon/"
seoindex: "index, follow"
seotitle: "Redis Encryption in Transit"
seokeywords: "redis, redis ssl, redis certificates, redis ssl certificates, redis encryption in transit, ssl tls redis"
seodesc: "Learn about a built-in add-on for Redis that implements SSL/TLS encryption in transit for the standalone node and database cluster."
menu:
    docs:
        title: "Encryption in Transit Add-On"
        url: "/redis-ssl-addon/"
        weight: 40
        parent: "redis"
        identifier: "redis-ssl-addon.md"
---

# SSL/TLS Encryption in Transit for Redis

The Virtuozzo-certified Redis database is provided with a built-in add-on that implements “***encryption in transit***”. The functionality ensures data protection with SSL/TLS encrypted connection while it moves between servers. After the add-on installation, support for a secure connection is configured on a separate port *6380*, while maintaining the default port *6379* to accept unencrypted connections for backward compatibility (if needed, it can be disabled via settings).


## Add-On Installation

The add-on can be installed on top of the Redis nodes only.

1\. In the platform dashboard, go to the **Add-Ons** section of the appropriate Redis database layer, and click **Install** for the *Redis Encrypted Connection* solution.

{{%tip%}}**Tip:** The add-on is also available from the [Marketplace](/marketplace/) and can be imported from the appropriate GitHub repository.{{%/tip%}}

![Redis SSL add-on](01-redis-ssl-addon.png)

2\. Within the opened installation window, select the target **Environment** and **Node Group(s)** where the add-on will be installed.

![install Redis SSL](02-install-redis-ssl.png)

Click **Install** to continue.

3\. In a minute, your environment will be configured.

![SSL add-on installed](03-ssl-addon-installed.png)

{{%note%}}**Note:** Port ***6380*** is used for secure connection by default and is automatically added to the [firewall rules](/custom-firewall/) during the add-on installation.

![Redis SSL firewall](04-redis-ssl-firewall.png)
{{%/note%}}

You can find generated SSL certificates under the **/var/lib/jelastic/keys/SSL-TLS** folder.


## Add-On Specifics

Below you can learn about certificates generation processes and specifics:

- Add-on pre-installs **[Redli](https://github.com/IBM-Cloud/redli)** – a humane Go-based alternative to the official *redis-cli* utility.
- Certificates are generated with the ***/usr/local/sbin/selfcertgen*** utility.
- Certificates are self-signed and issued for the hostname of the particular node. It means that each node has a set of own certificates, and you must use the ones corresponding to the accessed node for authentication.
- Due to Redis specifics, the alternative hostname is added when creating the server certificate:

```
echo "subjectAltName = @alt_names

[alt_names]
IP.1 = ${ALTNAME}" > /tmp/altname.ext
RANDFILE=/tmp/.random openssl x509 -req -in ${CERT_DIR}/server-req.pem -days 3650 -CA ${ROOT_CERT} -CAkey ${ROOT_KEY} -set_serial 01 -extfile /tmp/altname.ext > ${CERT_DIR}/server.crt
```

- Certificates are stored within the **/var/lib/jelastic/keys/SSL-TLS** folder (accessible via the ***keys*** shortcut in the file manager). Two subfolders are present:
  - ***server*** – server certificates are used to provide the TLS encryption of connection to the Redis database
  - ***client*** – downloadable client certificates can be used to authenticate client connection to the database server

![Redis SSL certificates](05-redis-ssl-certificates.png)

**Redis configurations:**

All the add-on configurations are provided via a separate ***/etc/redis.conf*** configuration file (also added to the *Favorites* list in the file manager).

![Redis configuration file](06-redis-configuration-file.png)

Below, you can check a list of the most common SSL-related settings:

- ***tls-port*** - specifies the port which is used for SSL connection (*6380*).
- ***port*** – sets a port that can accept unencrypted connections (*6379*).

{{%tip%}}**Tip:** Both values are intentionally kept separate by default to ensure backward compatibility. If you want to disable the unencrypted connection completely, set the ***port*** directive to *0*.{{%/tip%}}

- ***tls-cert-file***, ***tls-key-file***, ***tls-ca-cert-file*** – directives specify paths to server-side SSL certificates
- ***tls-auth-clients*** – configures if clients (including replica servers) on a TLS port are required to authenticate using valid client-side certificates. Set to “*optional*” by default - if provided, client certificates are accepted and must be valid (but they are not required).
- ***tls-replication*** and ***tls-cluster*** - can be enabled if needed to support TLS interconnection in the Redis cluster


## Add-On Configuration

After the installation, the add-on can be found under the **Add-Ons** tab for the appropriate layer.

![manage Redis SSL add-on](07-manage-redis-ssl-addon.png)

Here you can click the **Re-issue certificates** button to generate SSL certificates for secure connection anew.

If no longer needed, remove the add-on from the layer by choosing the **Uninstall** option in the add-on menu in the top-right corner.


## Secure Connection to Redis

For secure connection (we’ll use the **[redis-cli](https://redis.io/docs/ui/cli/)** utility as an example), specify the command with the following options:

{{%tip%}}**Tip:** You can store the database password in the dedicated *REDISCLI_AUTH* variable to avoid exposing it in the command line:

```
export REDISCLI_AUTH={password}
```
{{%/tip%}}

```
redis-cli -p 6380 --tls --cacert /var/lib/jelastic/keys/SSL-TLS/client/root.crt {command}
```

![Redis secure connect](08-redis-secure-connect.png)

You can execute any preferred ***{command}*** or omit it to connect to the database in the interactive mode.

If the server requires authentication using a client-side certificate, you can specify a certificate and a corresponding private key using ***-\-cert*** and ***-\-key*** parameters.

```
redis-cli -p 6380 --tls --cert /var/lib/jelastic/keys/SSL-TLS/client/client.crt --key /var/lib/jelastic/keys/SSL-TLS/client/client.key --cacert /var/lib/jelastic/keys/SSL-TLS/client/root.crt {command}
```

![Redis secure connect certificates](09-redis-secure-connect-certificates.png)

For external connection, the client needs to upload the certificate files (*client.crt*, *client.key*, *root.crt*) to their computer/container/VM and use the ***-h*** option to specify a remote hostname or an IP address.


## SSL Configuration Examples

- **forcing SSL connection (for standalone nodes)**

Enforce TLS encrypted connection and completely disable the non-secure connection for clients.

1\. Go to the ***/etc/redis.conf*** configuration file and change the “***port***” directive to *0*. It will disable unencrypted connections.

2\. Next, change the "***tls-port***" option to the default Redis port *6379* in the same file.

3\. If you want to make the usage of client certificates (for auth and mutual TLS) obligatory, set the "***tls-auth-clients***" directive to “*yes*”.

4\. Go to the firewall settings and remove the rule for port *6380*, as it is no longer needed.

5\. Lastly, restart the Redis container to apply the changes.

Now, Redis service is available only through the SSL connection on port *6379*.

- **cluster/sentinel interconnection through SSL**

Redis cluster interconnections are kept plain (non-secure) by default. It ensures backward compatibility with the already existing clusters. However, if you want to enable interconnection encryption, follow the steps below:

{{%note%}}**Note:** The automatic and manual scaling can work incorrectly after the changes due to being designed for plain non-SSL connections.{{%/note%}}

1\. If you are using the clustered solution, ensure that the "***tls-cluster***" directive in the ***/etc/redis.conf*** file is set to “*yes*” (uncomment the option).

2\. If you are using the sentinel replication, uncomment the "***tls-replication***" option as well (should be the “*yes*” value).

3\. The "***tls-auth-clients***" directive should be kept as “*optional*” (default value).

4\. The default cluster configuration uses port *6379* for the cluster interconnection, so you should either change the "***tls-port***" directive to *6379* or change the cluster/replication port to *6380*.

5\. Restart the Redis cluster to apply the changes.

- **multi-regional cluster SSL interconnection**

When working with the [multi-regional Redis cluster](/redis-multi-region-cluster/), the same root certificate must be used on all the nodes of all the environments for successful interconnection between nodes through the TLS.

1\. Install the SSL add-on on the first environment of the multi-regional cluster.

2\. Copy ***/var/lib/jelastic/keys/SSL-TLS/server/root.crt*** and ***/var/lib/jelastic/keys/SSL-TLS/server/root.crt*** to the **/var/lib/jelastic/keys/SSL-TLS/** directories on all the nodes of the second and third environments.

3\. Now install the SSL add-on on these environments as usual – new root certificates will not be generated this way.


## What's next?

- [Redis Overview](/redis/)
- [Redis Auto-Clustering](/redis-cluster/)
- [Redis Multi-Region Cluster](/redis-multi-region-cluster/)
- [Redis Backup/Restore Add-On](/db-backup-restore-addon/)