</table>
<h2>CPU and RAM reservations</h2>
<p>The following table lists the amount of RAM and CPU cores that will be reserved on one node, according to the services you will use:</p>
<table border="1" cellspacing="0" id="id16" style="mc-table-style: url('../../resources/tablestyles/borderedtable.css');">
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
<th style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">RAM<a href="#" style="font-size: 0.9em; vertical-align: super" title="Use only Error correction code (ECC) memory, to avoid data corruption.">1</a></th>
<th style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">CPU cores<a href="#" style="font-size: 0.9em; vertical-align: super" title="A CPU core here is a physical core in a multicore processor (hyperthreading is not taken into account).">2</a></th>
<th style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">RAM<a href="#" style="font-size: 0.9em; vertical-align: super" title="Use only Error correction code (ECC) memory, to avoid data corruption.">3</a></th>
<th style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">CPU cores<a href="#" style="font-size: 0.9em; vertical-align: super" title="A CPU core here is a physical core in a multicore processor (hyperthreading is not taken into account).">4</a></th>
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
<td colspan="2">Storage services: each disk with Metadata, Storage, or Cache role (any size)<a href="#" style="font-size: 0.9em; vertical-align: super" title="For clusters larger than 1 PB of physical space, add 0.5 GB of RAM per Metadata service.">5</a></td>
<td>0.5 GB</td>
<td>0.2 cores</td>
<td>0.5 GB</td>
<td>0.2 cores</td>
</tr>
<tr>
<td colspan="2">Compute service<a href="#" style="font-size: 0.9em; vertical-align: super" title="The recommended configuration for a compute cluster node starts with 64+ GB and 16+ cores.">6</a></td>
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
<td colspan="2">Backup Gateway<a href="#" style="font-size: 0.9em; vertical-align: super" title="When working with public clouds and NFS, Backup Gateway consumes as much RAM and CPU as with a local storage.">7</a></td>
<td>1 GB</td>
<td>0.5 cores</td>
<td>1 GB</td>
<td>0.5 cores</td>
</tr>
<tr>
<td rowspan="3">S3<a href="#" style="font-size: 0.9em; vertical-align: super" title="By default, each S3 node runs 4 S3 gateways and can run up to 10 NS and 10 OS instances, but the entire S3 cluster cannot host more than 24 OS and 16 NS instances. The number of OS and NS services is defined during the initial S3 cluster setup. Adding more nodes to the S3 cluster does not affect it. The CPU and RAM reservations depend on the number of S3 nodes. Generally, the larger the S3 cluster, the less resources are reserved on each node.">8</a></td>
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
<td>Each share<a href="#" style="font-size: 0.9em; vertical-align: super" title="The RAM reservation for an NFS share depends on the number of cluster nodes. The larger the NFS cluster, the less RAM is reserved on each node.">9</a></td>
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
