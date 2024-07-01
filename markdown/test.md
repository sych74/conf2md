Prerequisites

- A clear understanding of the concept <a href="traffic-types.html" class="MCXref xref">Traffic types</a>.

To create the network configuration for object storage

<div class="tabs-container">

<div class="tab">

Admin panel

1.  Go to **Infrastructure** \> **Networks** and ensure that your infrastructure has the following networks:
    - A private network with the **OSTOR private** traffic type
    - A public network with the **S3 public** traffic type
2.  Ensure the public network for the S3 nodes is balanced by an external DNS load balancer.
3.  If you plan to use RDMA over InfiniBand, move the traffic type **Storage** to a dedicated network and assign that network to the IB interface.
4.  Configure network interfaces on the nodes that you plan to join the S3 cluster.

</div>

<div class="tab">

Command-line interface

Review your network configuration by using the following command:

```
# vinfra cluster network list -c id -c name -c traffic_types
+--------------------------------------+---------+-----------------------------------------------------------------+
| id                                   | name    | traffic_types                                                   |
+--------------------------------------+---------+-----------------------------------------------------------------+
| f50605a3-64f4-4f0c-b50e-9481ec221c72 | Private | Backup (ABGW) private,Internal management,OSTOR private,Storage |
| 955041d4-b059-47a1-ba4c-0be117e8cbd2 | Public  | Backup (ABGW) public,iSCSI,NFS,S3 public,Admin panel,SSH        |
+--------------------------------------+---------+-----------------------------------------------------------------+
```

</div>

</div>

<div class="MCHelpControl MCHelpControl-Related relatedTopics relatedTopicssee-also">

<span class="MCHelpControl-RelatedHotSpot_ MCHelpControl-RelatedHotSpot_see-also"><img src="resources/images/transparent.gif" class="MCHelpControl_Image_Icon" width="16" height="16" alt="Related Topics Link Icon" />See also</span>

- <a href="managing-infrastructure-networks.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Managing infrastructure networks</a>

</div>

<div class="MCHelpControl MCHelpControl-Related relatedTopics relatedTopicswhats-next">

<span class="MCHelpControl-RelatedHotSpot_ MCHelpControl-RelatedHotSpot_whats-next"><img src="resources/images/transparent.gif" class="MCHelpControl_Image_Icon" width="16" height="16" alt="Related Topics Link Icon" />What's next</span>

- <a href="configuring-node-network-interfaces.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Configuring node network interfaces</a>

</div>
