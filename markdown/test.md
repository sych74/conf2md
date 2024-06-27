# Creating a virtual machine

{{%tip%}}

For supported guest operating systems and other information, refer to "Managing virtual machines" in the Administrator Guide.

{{%/tip%}}

1.  On the <span class="uicontrol">Virtual machines</span> screen, click <span class="uicontrol">Create virtual machine</span>. A window will open where you will need to specify the VM parameters.

2.  Specify a name for the new VM.

3.  Select the VM boot media:

    - If you have an ISO image or a template In the \<span class="uicontrol"\>Images\</span\> window, select the ISO image or template, and then click \<span class="uicontrol"\>Done\</span\>.
    - If you have a compute boot volume In the \<span class="uicontrol"\>Attach volume\</span\> window, find and select the volume, and then click \<span class="uicontrol"\>Attach\</span\>.

    {{%tip%}}

    If you select an image or volume with an assigned placement, the created VM will also inherit this placement.

    {{%/tip%}}

    After selecting the boot media, volumes required for this media to boot will be automatically added to the <span class="uicontrol">Volumes</span> section.

4.  Configure the VM disks:

    1.  In the <span class="uicontrol">Volumes</span> window, make sure the default boot volume is large enough to accommodate the guest OS. Otherwise, click the ellipsis icon next to it, and then <span class="uicontrol">Edit</span>. Change the volume size and click <span class="uicontrol">Save</span>.

    2.  Add more disks to the VM by creating or attaching volumes. To do this, click the pencil icon in the <span class="uicontrol">Volumes</span> section, and then <span class="uicontrol">Add</span> or <span class="uicontrol">Attach</span> in the <span class="uicontrol">Volumes</span> window.

    3.  Select volumes that will be removed during the VM deletion. To do this, click the pencil icon in the <span class="uicontrol">Volumes</span> section, click the ellipsis icon next to the needed volume, and then <span class="uicontrol">Edit</span>. Enable <span class="uicontrol">Delete on termination</span> and click <span class="uicontrol">Save</span>.

    4.  When you finish configuring the VM disks, click <span class="uicontrol">Done</span>.

5.  Choose the amount of RAM and CPU resources that will be allocated to the VM in the <span class="uicontrol">Flavor</span> section. In the <span class="uicontrol">Flavor</span> window, select a flavor, and then click <span class="uicontrol">Done</span>.

    {{%note%}}

    When choosing a flavor for a VM, ensure it satisfies the hardware requirements of the guest OS.

    {{%/note%}} {{%tip%}}

    To select a flavor with an assigned placement, you can filter flavors by placement. The VM created from such a flavor will also inherit this placement.

    {{%/tip%}}

    <a href="resources/images/compute_vms5_vz.png" class="MCPopupThumbnailLink MCPopupThumbnailPopup"><img src="resources/images/compute_vms5_vz_thumb_0_100.png" class="MCPopupThumbnail img" style="mc-thumbnail: popup;mc-thumbnail-max-height: 100px;mc-thumbnail-max-width: auto;" data-mc-height="596" data-mc-width="1037" tabindex="" /></a>

6.  Add network interfaces to the VM in the <span class="uicontrol">Networks</span> section:

    1.  In the <span class="uicontrol">Network interfaces</span> window, click <span class="uicontrol">Add</span> to attach a network interface.

    2.  In the <span class="uicontrol">Add network interface</span> window, select a compute network to connect to, and then specify MAC address, IPv4 and/or IPv6 addresses, and security groups. By default, MAC and primary IP addresses are assigned automatically. To specify them manually, clear the <span class="uicontrol">Assign automatically</span> check boxes, and enter the desired addresses. Optionally, assign additional IP addresses to the network interface in the <span class="uicontrol">Secondary IP addresses</span> section. Note that a secondary IPv6 address is not available for an IPv6 subnet that works in the SLAAC or DHCPv6 stateless mode.

        {{%tip%}}

        Secondary IP addresses, unlike the primary one, will not be automatically assigned to the network interface inside the virtual machine guest OS. You should assign them manually.

        {{%/tip%}}

        - If you selected a virtual network with enabled IP address management In this case, spoofing protection is enabled and the \<span class="uicontrol"\>default\</span\> security group is selected by default. This security group allows all incoming and outgoing traffic on all the VM ports. If required, you can select another security group or multiple security groups.
        - If you selected a virtual network with disabled IP address management
        - If you selected a shared physical network In this case, spoofing protection cannot be configured by a self-service user. If you want to enable or disable spoofing protection, contact your system administrator.

        <a href="resources/images/compute_vms6_vz.png" class="MCPopupThumbnailLink MCPopupThumbnailPopup"><img src="resources/images/compute_vms6_vz_thumb_0_100.png" class="MCPopupThumbnail img" style="mc-thumbnail: popup;mc-thumbnail-max-height: 100px;mc-thumbnail-max-width: auto;" data-mc-height="862" data-mc-width="751" tabindex="" /></a>

        After specifying the network interface parameters, click <span class="uicontrol">Add</span>. The network interface will appear in the <span class="uicontrol">Network interfaces</span> list.

    3.  If required, edit IP addresses and security groups of newly added network interfaces. To do this, click the ellipsis icon, click <span class="uicontrol">Edit</span>, and then set the parameters.

    4.  When you finish configuring the VM network interfaces, click <span class="uicontrol">Done</span>.

7.  If you have chosen to boot from a template or volume, which has cloud-init and OpenSSH installed:

    {{%note%}}

    As cloud images have no default password, you can access VMs deployed from them only by using the key authentication method with SSH.

    {{%/note%}}

    - Add an SSH key to the VM, to be able to access it via SSH without a password. In the \<span class="uicontrol"\>Select an SSH key\</span\> window, select an SSH key and then click \<span class="uicontrol"\>Done\</span\>.
    - Add user data to customize the VM after launch, for example, change a user password. Write a cloud-config or shell script in the \<span class="uicontrol"\>Customization script\</span\> field or browse a file on your local server to load the script from.

8.  Enable CPU and RAM hot plug for the VM in <span class="uicontrol">Advanced options</span>, to be able to change its flavor when the VM is running. You can also enable hot plug after the VM is created.

    {{%tip%}}

    If you do not see this option, CPU and RAM hot plug is disabled in your project. To enable it, contact your system administrator.

    {{%/tip%}}

9.  If you have chosen to boot from an ISO image, enable UEFI boot in <span class="uicontrol">Advanced options</span>, to be able to boot the VM in the UEFI mode. This option cannot be configured after the VM is created.

    {{%tip%}}

    You cannot configure UEFI boot if you have selected a template as the VM boot media. If your template has UEFI boot enabled, the option is automatically enabled for the VM, and vice versa.

    {{%/tip%}}

10. After configuring all of the VM parameters, click <span class="uicontrol">Deploy</span> to create and boot the VM.

If you are deploying the VM from an ISO image, you need to install the guest OS inside the VM by using the built-in VNC console. For VMs with UEFI boot enabled, open the VNC console, and then press any key to boot from the chosen ISO image. Virtual machines created from a template or a boot volume already have a preinstalled guest OS.
