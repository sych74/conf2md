# Kickstart File Example

Below is an example of a kickstart file that you can use to install and configure Virtuozzo Hybrid Server in unattended mode. You can use this file as the basis for creating your own kickstart files.

-   To ensure the disk where you install Virtuozzo Hybrid Server is partitioned correctly, you may need to erase existing partitions with `clearpart`. This command is commented out by default to avoid accidental loss of data.

-   Keeping plain-text passwords in the kickstart file is a security risk if your network is not isolated. Consider encrypting your password according to `auth` parameters (for example, with SHA512 as in this example) and using `rootpw --iscrypted `.

``` java
# Install Virtuozzo Hybrid Server.
install
# Skip loading X Window System and the installer GUI.
# cmdline
# Specify the location of the Virtuozzo Hybrid Server distribution files.
url --url http://<HTTP_server_IP_address>/vz
# Set the language for the installation and the default system language
# to US English.
lang en_US.UTF-8
# Set the keyboard layout to US English.
keyboard --vckeymap=us --xlayouts='us'
# Erase all partitions from the sda hard drive.
# clearpart --drives=sda --all --initlabel --disklabel=gpt
# Automatically creates required partitions. Requires clearpart.
autopart
# Agree to participate in the Customer Experience Program.
cep --agree
# Obtain network configuration via DHCP.
network --bootproto dhcp
# Download updated packages.
# up2date
# Set the root password for the server.
rootpw <passwd>
# Encrypt user passwords with the SHA-512 algorithm and enable shadow passwords.
auth --enableshadow --passalgo=sha512
# Set the system timezone.
timezone --utc America/New_York --ntpservers=0.pool.ntp.org,1.pool.ntp.org
# Set sda as the first drive in the BIOS boot order and write the boot record to
# MBR.
bootloader --location=mbr
# Reboot the system after installation.
reboot
# Install a Virtuozzo Hybrid Server license.
key <key>
# Install Virtuozzo Hybrid Server packages.
%packages
@^cloudserver
@base
@core
@ps
@qemu
@vstorage
@vz
kexec-tools
%end
```

## Advanced Partitioning Example

------------------------------------------------------------------------

For more control over partitioning, you can replace `autopart` with a set of `part` commands to adjust the size of required partitions. In this case, each partition will have the same size on every system you install Virtuozzo Hybrid Server. For example, if you use the lines below, the swap will be 4 GiB, and `/vz` will be 40 GiB on every system (whereas if you use `autopart`, the swap size will depend on RAM size, and `/vz` will occupy all available space).

For example, for installation on BIOS-based systems:

``` java
part /boot --fstype=ext4 --size=1024
part / --fstype=ext4 --size=20096
part /vz --fstype=ext4 --size=40768 --grow
part swap --size=4096
```

For installation on EFI-based systems, also specify

``` java
part /boot/efi --fstype=efi --size=200
```


