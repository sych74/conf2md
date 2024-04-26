# Installing Data Stores

After successfully installing the Control Panel server and compute resources, follow the procedure to set up a QCOW2 data store:

## Installing QCOW2 Data Store

------------------------------------------------------------------------

To create a QCOW2 data store:

1.  Go to your Control Panel &gt; **Admin** &gt; **Settings** menu.
2.  Click the Data Stores icon.
3.  Click the Create Data Store button in the lower-right corner and fill in the following:
    Step 1 of 2. Properties
    -   Label - enter the data store label.
    -   Data store type - select qcow2.
    -   Enabled - move the slider to the right to turn on the data store. If disabled, new disks are forbidden to be created automatically on the data store. It prevents the data store from becoming too full and the automatic creation of root disks on particular data stores (high speed, etc.).
    -   Click Next.

    Step 2 of 2. Resources
    -   QCOW2 path - specify the path to the QCOW2 file. 
    -   Disk Capacity - set the disk capacity in GB.
    -   Local Compute Resource - if required, bind the data store with a local compute resource to locate the data store and the compute resource on the same physical server. Thus, it decreases the connection time between the compute resource and the data store. If not bound with the local compute resource, such a data store will be available within the compute zone to which this data store is assigned.
    -   Data Store Zone - in the drop-down list, select a data store zone to assign the data store to it. The drop-down list shows all data store zones set up in the cloud (to add or edit data store zones, see Data Store Zones Settings).

    When adding a data store to a data store zone, the data store inherits the zone type. You can move such a data store exclusively to a data store zone of the same type. For more information, refer to Zone Types.

4.  Click the Create Data Store button.


