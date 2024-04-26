# Enabling the Expert Mode

The expert mode allows choosing packages to install and manually partition disks. The latter capability is needed to install Virtuozzo Hybrid Server on a USB drive. It is recommended to use only the expert mode in this particular case.

To enable the expert mode:

1.  Choose the required installation option and press **E** to edit it.

2.  Add `expert` at the end of the line, starting with `linux /images/pxeboot/vmlinuz`. For example:

    ``` java
    linux /images/pxeboot/vmlinuz inst.stage2=hd:LABEL=<VZ9_ISO_image> quiet ip=dhcp \
    expert
    ```

3.  Press **Ctrl-X** to load the selected installation option.


