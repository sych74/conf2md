Follow the procedure to set up a backup server:

## staticInstalling Static Backup Server

------------------------------------------------------------------------



<span style="color: rgb(51,51,51);">To install a static backup server,
run the following procedure:</span>

1.  Update your server:

    \# yum update

2.  Install the OnApp backup server installer package:

    \# yum install onapp-bk-install

3.  configCheck and set the backup server default settings:

    \# vi /onapp/onapp-bk.confEdit the backup server default settings in
    the /onapp/onapp-bk.conf file.

    **
    Default server to synch time on the HV**

    NTP\_TIME\_SERVER='pool.ntp.org'

    **The number of retries for WGET to download the file**

    WGET\_TRIES=5

    **OnApp templates directory
    **

    Please refer to the corresponding settings at OnApp Control Panel
    web interface.TEMPLATES\_DIR='/onapp/templates'

    **OnApp backups directory
    **

    Please refer to the corresponding settings at OnApp Control Panel
    web interface.BACKUPSS\_DIR='/onapp/backups'

4.  installerRun the installer.

    \# sh /onapp/onapp-bk-install/onapp-bk-install.sh The full list of
    installer options.

    **Usage**:

    \# /onapp/onapp-bk-install/onapp-bk-install.sh \[-c CONFIG\_FILE\]
    \[-a\] \[-y\] \[-b\] \[-v BK\_VERSION\] \[-p API\_VERSION\] \[-h\]

    **Where: **

    <table class="wrapped">
    <tbody>
    <tr class="odd">
    <td><p><code>-c CONFIG_FILE </code></p></td>
    <td><p>Custom installer configuration file. Otherwise, the pre-installed
    one is used.</p></td>
    </tr>
    <tr class="even">
    <td><p><code>-a </code></p></td>
    <td><p>Do NOT be interactive. Process with automatic
    installation.</p></td>
    </tr>
    <tr class="odd">
    <td><p><code>- v BK_VERSION</code></p></td>
    <td>Custom backup tools version.</td>
    </tr>
    <tr class="even">
    <td><p><code>- p API_VERSION</code></p></td>
    <td>Custom StorageAPI version.</td>
    </tr>
    <tr class="odd">
    <td><p><code>-y </code></p></td>
    <td><p>Update OS packages (except for the ones provided by OnApp) with
    <code>yum update</code>.</p></td>
    </tr>
    <tr class="even">
    <td><p><code>- b</code></p></td>
    <td>Initiate the Base templates download.</td>
    </tr>
    <tr class="odd">
    <td><p><code>-h </code></p></td>
    <td><p>Print this info.</p></td>
    </tr>
    </tbody>
    </table>

5.  Сonfigure the backup server for your cloud. This step is also
    required for the SNMP statistics receiver configuration:

    \# /onapp/onapp-bk-install/onapp-bk-config.sh -h
    &lt;CP\_HOST\_IP&gt; -p &lt;BK\_HOST\_IP&gt;The full list of
    configuration options.

    **Usage**:

    \# /onapp/onapp-bk-install/onapp-bk-config.sh \[-h CP\_HOST\_IP\] \[
    -p BK\_HOST\_IP\] \[-a|-i \[USER:PASSWD\]\] \[-s\] -?

    **Where:**

    <table class="wrapped">
    <tbody>
    <tr class="odd">
    <td><p><code>-h CP_HOST_IP</code></p></td>
    <td><p>The FQDN or IP address of the management server which receives
    all status reports and is authoritative for this backup server.</p></td>
    </tr>
    <tr class="even">
    <td><p><code>-p BK_HOST_IP</code></p></td>
    <td><p>The FQDN or IP address of the backup server that will serve all
    stats-related and other requests sent by the
    <code>CP_HOST_IP</code>.</p>
    <p>Used by SNMPD and StorageAPI.</p></td>
    </tr>
    <tr class="odd">
    <td><p><code>-a</code></p></td>
    <td><p> Install AoE.</p></td>
    </tr>
    <tr class="even">
    <td><p><code>-i [USER:PASSWD]</code></p></td>
    <td><p> Install iSCSI utils and configure with <code>USER</code> and
    <code>PASSWD</code> (if specified).</p></td>
    </tr>
    <tr class="odd">
    <td><p><code>-s</code></p></td>
    <td> Install SSHFS.</td>
    </tr>
    <tr class="even">
    <td><p><code>-?</code></p></td>
    <td><p> Print this help info.</p></td>
    </tr>
    </tbody>
    </table>

6.  Install SSH keys for the backup server by running the following
    script on the Control Panel server:

    \# ssh-copy-id -i /home/onapp/.ssh/id\_ed25519.pub root@BS\_HOST\_IP

7.  <span style="color: rgb(14,16,26);">From the Control Panel server,
    enter the compute resource server from the OnApp user via SSH to add
    it to .`ssh/known_hosts`:
    </span>

    su onapp ssh root@HV\_HOST\_IP

8.  Add a backup server via the Control Panel user interface:
    -   Go to your Control Panel &gt; **Admin **&gt;* ***Settings** menu
        and click the **Backup Servers** icon.
    -   Click the **Create Backup Server** button.
    -   Fill in the form that appears:

    1.  -   *Label* - give your backup server a label.
        -   *IP address* - enter the backup server IP address (IPv4).
        -   *Backup IP address* - add a provisioning network IP address.
        -   *Capacity* - set the backup server capacity (in GB).
        -   *Backup server zone* - select the backup server zone to
            which this backup server will be assigned. For more
            information on adding or editing backup server zones, see
            the [Backup Server Zones
            Settings](https://docs.onapp.com/vhs9ag/latest/storage-and-backups/backup-settings/backup-server-zones-settings)
            section.

    -   Move the **Enabled** slider to the right to enable the backup
        server.
    -   Click the **Add Backup Server** button.

9.  Inside your Control Panel, perform the following CLI commands:

    su - onapp scp /onapp/templates/\*
    root@backup\_server\_ip:/onapp/templates/
