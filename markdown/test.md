## CPU and RAM reservations
The following table lists the amount of RAM and CPU cores that will be reserved on one node, according to the services you will use:

<table border="1" cellspacing="0" class="TableStyle-bordered-table" id="id16" style="mc-table-style: url('../../resources/tablestyles/borderedtable.css');">
<col class="TableStyle-bordered-table-Column-Column1"/>
<col class="TableStyle-bordered-table-Column-Column1"/>
<col class="TableStyle-bordered-table-Column-Column1"/>
<col class="TableStyle-bordered-table-Column-Column1"/>
<col class="TableStyle-bordered-table-Column-Column1"/>
<col class="TableStyle-bordered-table-Column-Column1"/>
<thead valign="bottom">
<tr class="TableStyle-bordered-table-Head-Header1" data-mc-pattern="2">
<th class="TableStyle-bordered-table-HeadE-Column1-Header1" colspan="2" rowspan="2">Service</th>
<th class="TableStyle-bordered-table-HeadE-Column1-Header1" colspan="2">Management node </th>
<th class="TableStyle-bordered-table-HeadD-Column1-Header1" colspan="2">Secondary node</th>
</tr>
<tr class="TableStyle-bordered-table-Head-Header1" data-mc-pattern="2">
<th class="TableStyle-bordered-table-HeadE-Column1-Header1" style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">RAM<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">1<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>Use only Error correction code (ECC) memory, to avoid data corruption.</span></a></th>
<th class="TableStyle-bordered-table-HeadE-Column1-Header1" style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">CPU cores<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">2<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>A CPU core here is a physical core in a multicore processor (hyperthreading is not taken into account).</span></a></th>
<th class="TableStyle-bordered-table-HeadE-Column1-Header1" style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">RAM<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">3<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>Use only Error correction code (ECC) memory, to avoid data corruption.</span></a></th>
<th class="TableStyle-bordered-table-HeadD-Column1-Header1" style="text-align: left;font-weight: normal;border-left-width: 0;border-right-width: 1px;border-top-width: 0;border-bottom-style: solid;border-bottom-width: 1px;border-bottom-color: #010101;padding-left: 10px;padding-right: 10px;padding-top: 7px;padding-bottom: 7px;">CPU cores<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">4<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>A CPU core here is a physical core in a multicore processor (hyperthreading is not taken into account).</span></a></th>
</tr>
</thead>
<tbody valign="top">
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" colspan="2">System</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">4.5 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">3.3 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">1.5 GB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">1.1 cores</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" colspan="2">Storage services: each disk with Metadata, Storage, or Cache role (any size)<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">5<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>For clusters larger than 1 PB of physical space, add 0.5 GB of RAM per Metadata service.</span></a></td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.5 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.2 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.5 GB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">0.2 cores</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" colspan="2">Compute service<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">6<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>The recommended configuration for a compute cluster node starts with 64+ GB and 16+ cores.</span></a></td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">10 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">4 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1"> </td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1"> </td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" colspan="2">Load balancer</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">1.5 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.5 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1"> </td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1"> </td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" colspan="2">Kubernetes</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">1 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.5 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1"> </td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1"> </td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" colspan="2">Backup Gateway<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">7<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>When working with public clouds and NFS, Backup Gateway consumes as much RAM and CPU as with a local storage.</span></a></td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">1 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.5 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">1 GB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">0.5 cores</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" rowspan="3">S3<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">8<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>By default, each S3 node runs 4 S3 gateways and can run up to 10 NS and 10 OS instances, but the entire S3 cluster cannot host more than 24 OS and 16 NS instances. The number of OS and NS services is defined during the initial S3 cluster setup. Adding more nodes to the S3 cluster does not affect it. The CPU and RAM reservations depend on the number of S3 nodes. Generally, the larger the S3 cluster, the less resources are reserved on each node.</span></a></td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">Each S3 gateway</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">256 MB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">1 core</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">256 MB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">1 core</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">Each OS service</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">256 MB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.1 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">256 MB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">0.1 cores</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">Each NS service</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">512 MB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">0.2 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">512 MB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">0.2 cores</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1" rowspan="2">NFS</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">Service</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">4 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">1 core</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">4 GB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">1 core</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">Each share<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">9<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>The RAM reservation for an NFS share depends on the number of cluster nodes. The larger the NFS cluster, the less RAM is reserved on each node.</span></a></td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">up to 9 GB</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">up to 8 cores</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">up to 9 GB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">up to 8 cores</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyB-Column1-Body1" colspan="2">iSCSI</td>
<td class="TableStyle-bordered-table-BodyB-Column1-Body1">1 GB</td>
<td class="TableStyle-bordered-table-BodyB-Column1-Body1">1 core</td>
<td class="TableStyle-bordered-table-BodyB-Column1-Body1">1 GB</td>
<td class="TableStyle-bordered-table-BodyA-Column1-Body1">1 core</td>
</tr>
</tbody>
</table>
<p>These reserved values correspond to absolute minimum requirements. In general, the more resources you provide for your cluster, the better it works. All extra RAM is used to cache disk reads, while extra CPU cores increase the performance and reduce latency. </p>
<h2>CPU and RAM limits</h2>
<p>The following table lists the current RAM and CPU limits for <span class="mc-variable Cover.ProductName variable">Virtuozzo Hybrid Infrastructure</span> servers:</p>
<table border="1" cellspacing="0" class="TableStyle-bordered-table" id="id14" style="mc-table-style: url('../../resources/tablestyles/borderedtable.css');">
<colgroup>
<col/>
<col/>
<col/>
</colgroup>
<thead valign="bottom">
<tr class="TableStyle-bordered-table-Head-Header1">
<th class="TableStyle-bordered-table-HeadE-Column1-Header1">Hardware</th>
<th class="TableStyle-bordered-table-HeadE-Column1-Header1">Theoretical</th>
<th class="TableStyle-bordered-table-HeadD-Column1-Header1">Certified</th>
</tr>
</thead>
<tbody valign="top">
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">RAM</td>
<td class="TableStyle-bordered-table-BodyE-Column1-Body1">64 TB</td>
<td class="TableStyle-bordered-table-BodyD-Column1-Body1">1 TB</td>
</tr>
<tr class="TableStyle-bordered-table-Body-Body1">
<td class="TableStyle-bordered-table-BodyB-Column1-Body1">CPU</td>
<td class="TableStyle-bordered-table-BodyB-Column1-Body1">5120 logical CPUs<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">10<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>A logical CPU is a core (thread) in a multicore (multithreading) processor.</span></a></td>
<td class="TableStyle-bordered-table-BodyA-Column1-Body1">384 logical CPUs<a class="MCTextPopup popup popupHead" href="javascript:void(0)" style="font-size: 0.9em; vertical-align: super">11<span aria-hidden="true" class="MCTextPopupBody MCTextPopupBody_Closed needs-pie popupBody"><span class="MCTextPopupArrow"> </span>A logical CPU is a core (thread) in a multicore (multithreading) processor.</span></a></td>
</tr>
</tbody>
</table>
<h2>CPU recommendations</h2>
<ul>
<li>The minimum CPU frequency for <span class="mc-variable Cover.ProductName variable">Virtuozzo Hybrid Infrastructure</span> servers is 2.0 GHz. The recommended CPU frequency is at least 2.4 GHz.</li>
<li>CPU frequency affects the cluster performance. Higher CPU frequency reduces latency almost linearly, thus increasing the performance. If other CPU parameters are the same, higher CPU frequency is preferable to a larger number of CPU cores.</li>
<li>Nodes running the metadata service should have high CPU frequency, because this service is CPU intensive.</li>
<li>To improve erasure coding performance, it is recommended to use CPUs that support the AVX-512 instruction set, such as Intel Xeon Silver 4110, Intel Xeon Gold 5115, Intel Xeon Platinum 8171, or newer.</li>
</ul>
<h2>Network interface requirements</h2>
<p>At least 2 x 10 GbE interfaces are recommended, for internal and external traffic; 25 GbE, 40 GbE, and 100 GbE are even better. Bonding is recommended. However, for external traffic, you can start with 1 GbE links, but they can limit cluster throughput on modern loads.</p>

See also

<ul class="MCHelpControlList MCRelatedTopicsControlList">
<li class="MCHelpControlListItem MCRelatedTopicsControlListItem"><a class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink" href="quantity-of-servers.html">Quantity of servers</a>
</li>
<li class="MCHelpControlListItem MCRelatedTopicsControlListItem"><a class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink" href="considerations-for-using-blade-servers.html">Considerations for using blade servers</a>
</li>
<li class="MCHelpControlListItem MCRelatedTopicsControlListItem"><a class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink" href="backup-storage-requirements.html">Backup storage requirements</a>
</li>
<li class="MCHelpControlListItem MCRelatedTopicsControlListItem"><a class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink" href="compute-requirements.html">Compute cluster requirements</a>
</li>
<li class="MCHelpControlListItem MCRelatedTopicsControlListItem"><a class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink" href="object-storage-requirements.html">Object storage requirements</a>
</li>
</ul>
