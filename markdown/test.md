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
<th <a href="#" title="adasdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd asdasdasd">RAM</a> </th>
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
