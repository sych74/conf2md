# ISOs

You can enable users to build and boot virtual servers from ISO images. To enable the usage of ISO, mount the location where ISO images are stored on a Control Panel server to compute resource servers. 

##### **Mount ISO Locations**

When a virtual server is booted from an ISO image, the ISO image is taken from a compute resource server. To mount and share the location where ISO images are stored on a Control Panel server with the compute resource servers, edit the onapp.yml file as follows:  

-   `iso_path_on_cp` - specifies the location where ISO images are stored on the Control Panel server. By default, the location is `/data`. You can change it to any other suitable location. Ensure that this location is shared with the specified` iso_path_on_hv` location.
-   `iso_path_on_hv` - specifies the location where ISO images are located on the compute resource servers. By default, the location is `/data`.  You can change it to any other suitable location with the `onappowner` and read/write access. Ensure that this location is mounted to the specified` iso_path_on_cp `location.

You can store ISO images on a dedicated server at any location with an arbitrary name. In this case, it is necessary to mount the ISO images location on this server to the iso\_path\_on\_cp directory on Control Panel and all iso\_path\_on\_hv locations on compute resources. It can be a backup server to avoid the usage of the Control Panel resources.

##### Enable Permissions in Control Panel UI

Make sure to enable the following permissions for your Admin and other roles in the Control Panel user interface:

-   *Any action on ISOs* - the user can take any action on ISOs.
-   *Create a new ISO* - the user can create a new ISO.
-   *Destroy any ISO* - the user can delete any ISO (own, user, and public).
-   *Destroy own ISO* - the user can delete only their ISO.
-   *Destroy user ISO* - the user can delete ISOs created by any user, but not public ISOs.
-   *Make any ISO public* - the user can make any ISO available to all users.
-   *Make own ISO public* - the user can make public only their ISOs.
-   *Make user ISO public* - the user can make public ISOs created by any user.
-   *Create and manage own ISOs* - the user can create, edit, delete, and view their ISOs.
-   *Manage all ISOs* - the user can manage their/user/public ISOs.
-   *Create and manage user ISOs* - the user can view/create/edit/delete ISOs created by any user.
-   *See all ISOs* - the user can view all ISOs in the cloud.
-   *See own ISOs* - the user can only view the ISOs created by themselves.
-   *See all public ISOs* - the user can view all public ISOs.
-   *See user ISOs* - the user can view the ISOs created by any user in the cloud.
-   *Update any ISO* - the user can edit any ISO in the cloud.
-   *Update own ISO* - the user can edit only their ISO.
-   *Update user ISO* - the user can edit ISOs created by any user in the cloud.


