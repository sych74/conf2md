# Transferring the License to Another Server

To transfer a license installed on one server to another server, you can do as described below.

If you have a Virtuozzo Hybrid Server product key:

1.  Remove the installed license from the source server with the `vzlicload-r ` command (the serial is shown in the `vzlicview` output).
2.  Install the product key on the destination server:

    ``` java
    # vzlicload -p <product_key>
    ```

A new license file will be generated and installed in the `/etc/vz/license/` directory on the server.

If you have a Virtuozzo Hybrid Server activation code:

1.  Shut down the source server or remove the installed license from it with the `vzlicload-r <serial>` command (the serial is shown in `vzlicview` output).
2.  Ensure the destination server is up, connected to the Internet, and has at least one public IPv4 address.
3.  On the destination server, run

    ``` java
    # vzlicupdate -t -a <activation_code>
    ```

    When executed, `vzlicupdate` sends the activation code to the KA server. The KA server verifies the code, generates a new license file, sends it back, and the license file is installed on the server automatically.

4.  To check that the license transfer has been successful, run `vzlicview`. The information about the newly installed license should be displayed.


