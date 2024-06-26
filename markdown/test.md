<table border="1" cellspacing="0" id="id15">
<thead>
<tr>
<th>Disk role</th>
<th>Quantity</th>
<th>Disk size</th>
<th>Type</th>
<th>Endurance</th>
</tr>
</thead>
<tbody>
<tr>
<td>System</td>
<td>One disk per node</td>
<td>
<p>100 GB minimum</p>
<p>250 GB recommended</p>
</td>
<td>
<p>SATA/SAS HDD minimum</p>
<p>SATA/SAS SSD recommended</p>
</td>
<td>-</td>
</tr>
<tr>
<td>Metadata</td>
<td>
<p>One disk per node</p>
<p>Five disks recommended for one cluster</p>
</td>
<td>100 GB</td>
<td>Enterprise-grade SSD with power loss protection</td>
<td>1 DWPD minimum</td>
</tr>
<tr>
<td>Cache</td>
<td>
<p>Optional</p>
<p>One SSD disk per 4-12 HDDs</p>
</td>
<td>100+ GB</td>
<td>Enterprise-grade SSD with power loss
protection and 75 MB/s sequential write performance per serviced HDD</td>
<td>
<p>1 DWPD minimum</p>
<p>10 DWPD recommended</p>
</td>
</tr>
<tr>
<td>Storage</td>
<td>At least one per cluster</td>
<td>
<p>100 GB minimum</p>
<p>Unlimited size on a physical server; 10 TB maximum recommended inside a virtual machine</p>
</td>
<td> SATA/SAS HDD or enterprise-grade SATA/SAS/NVMe SSD with power loss protection</td>
<td>1 DWPD minimum</td>
</tr>
</tbody>
</table>
<h2>CPU and RAM reservations</h2>
<p>The following table lists the amount of RAM and CPU cores that will be reserved on one node, according to the services you will use:</p>
<table border="1" cellspacing="0" id="id16">
<col/>
<col/>
<col/>
<col/>
<col/>
<col/>
<thead valign="bottom">
<tr data-mc-pattern="2">
<th colspan="2" rowspan="2">Service</th>
<th colspan="2">Management node </th>
<th colspan="2">Secondary node</th>
</tr>
<tr data-mc-pattern="2">
<th>RAM<a href="#" title="Use only Error correction code (ECC) memory, to avoid data corruption.">1</a></th>
<th>CPU cores<a href="#" title="A CPU core here is a physical core in a multicore processor (hyperthreading is not taken into account).">2</a></th>
<th>RAM<a href="#" title="Use only Error correction code (ECC) memory, to avoid data corruption.">3</a></th>
<th>CPU cores<a href="#" title="A CPU core here is a physical core in a multicore processor (hyperthreading is not taken into account).">4</a></th>
</tr>
</thead>
<tbody valign="top">
<tr>
<td colspan="2">System</td>
<td>4.5 GB</td>
<td>3.3 cores</td>
<td>1.5 GB</td>
<td>1.1 cores</td>
</tr>
<tr>
<td colspan="2">Storage services: each disk with Metadata, Storage, or Cache role (any size)<a href="#" title="For clusters larger than 1 PB of physical space, add 0.5 GB of RAM per Metadata service.">5</a></td>
<td>0.5 GB</td>
<td>0.2 cores</td>
<td>0.5 GB</td>
<td>0.2 cores</td>
</tr>
<tr>
<td colspan="2">Compute service<a href="#" title="The recommended configuration for a compute cluster node starts with 64+ GB and 16+ cores.">6</a></td>
<td>10 GB</td>
<td>4 cores</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td colspan="2">Load balancer</td>
<td>1.5 GB</td>
<td>0.5 cores</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td colspan="2">Kubernetes</td>
<td>1 GB</td>
<td>0.5 cores</td>
<td> </td>
<td> </td>
</tr>
<tr>
<td colspan="2">Backup Gateway<a href="#" title="When working with public clouds and NFS, Backup Gateway consumes as much RAM and CPU as with a local storage.">7</a></td>
<td>1 GB</td>
<td>0.5 cores</td>
<td>1 GB</td>
<td>0.5 cores</td>
</tr>
<tr>
<td rowspan="3">S3<a href="#" title="By default, each S3 node runs 4 S3 gateways and can run up to 10 NS and 10 OS instances, but the entire S3 cluster cannot host more than 24 OS and 16 NS instances. The number of OS and NS services is defined during the initial S3 cluster setup. Adding more nodes to the S3 cluster does not affect it. The CPU and RAM reservations depend on the number of S3 nodes. Generally, the larger the S3 cluster, the less resources are reserved on each node.">8</a></td>
<td>Each S3 gateway</td>
<td>256 MB</td>
<td>1 core</td>
<td>256 MB</td>
<td>1 core</td>
</tr>
<tr>
<td>Each OS service</td>
<td>256 MB</td>
<td>0.1 cores</td>
<td>256 MB</td>
<td>0.1 cores</td>
</tr>
<tr>
<td>Each NS service</td>
<td>512 MB</td>
<td>0.2 cores</td>
<td>512 MB</td>
<td>0.2 cores</td>
</tr>
<tr>
<td rowspan="2">NFS</td>
<td>Service</td>
<td>4 GB</td>
<td>1 core</td>
<td>4 GB</td>
<td>1 core</td>
</tr>
<tr>
<td>Each share<a href="#" title="The RAM reservation for an NFS share depends on the number of cluster nodes. The larger the NFS cluster, the less RAM is reserved on each node.">9</a></td>
<td>up to 9 GB</td>
<td>up to 8 cores</td>
<td>up to 9 GB</td>
<td>up to 8 cores</td>
</tr>
<tr>
<td colspan="2">iSCSI</td>
<td>1 GB</td>
<td>1 core</td>
<td>1 GB</td>
<td>1 core</td>
</tr>
</tbody>
</table>
