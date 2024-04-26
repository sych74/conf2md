# Booting into the Rescue Mode

If you experience problems with your system, you can boot into the rescue mode to troubleshoot these problems. Once you are in the rescue mode, your Virtuozzo Hybrid Server installation is mounted under `/mnt/sysimage`. You can go to this directory and make the necessary changes to your system.

To enter the rescue mode:

1.  Boot your system from the chosen media.

2.  On the welcome screen, click **Troubleshooting–&gt;**, then **Rescue system**.

3.  Once Virtuozzo Hybrid Server boots into the emergency mode, press **Ctrl+D** to load the rescue environment.

4.  In the rescue environment, you can choose one of the following options:

    -   Continue (press **1**): mount the Virtuozzo Hybrid Server installation in read and write mode under `/mnt/sysimage`.

    -   Read-only mount (press **2**): mount the Virtuozzo Hybrid Server installation in read-only mode under `/mnt/sysimage`.

    -   Skip to shell (press **3**): load shell if your file system cannot be mounted. For example, when it is corrupted.

    -   Quit (Reboot) (press **4**): reboot the server.

5.  Unless you press **4**, a shell prompt will appear. In it, run `chroot /mnt/sysimage` to make the Virtuozzo Hybrid Server installation the root environment. Now you can run commands and try to fix the problems you are experiencing.

6.  After you fix the problem, run `exit` to exit the chroot environment, then `reboot` to restart the system.


