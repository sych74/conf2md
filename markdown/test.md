# Configuring scheduling of virtual machines

In the compute cluster, the `nova-scheduler` service manages scheduling of virtual machines, that is, determines on which compute node to launch a VM. Each scheduling request goes through the following steps:

1.  Prefilters. The scheduler uses the Placement service to filter compute nodes and excludes those that do not satisfy the request parameters.

2.  Filters. The scheduler applies filters to the list of candidate nodes, to determine which nodes are suitable for launching a VM. A node is either passed through by the filters or excluded from the list. These filters include:

    - `AvailabilityZoneFilter`: Passes all nodes that match the availability zone specified in the VM properties.
    - `ComputeFilter`: Passes all compute nodes that are operational and enabled.
    - `ComputeCapabilitiesFilter`: Passes all nodes that satisfy the flavor extra specs.
    - `ImagePropertiesFilter`: Passes all nodes that satisfy the requested image properties.
    - `PciPassthroughFilter`: Passes all nodes that have requested PCI devices.
    - `ServerGroupAntiAffinityFilter`: Passes all nodes that are not hosting virtual machines in a specified group.
    - `ServerGroupAffinityFilter`: Passes all nodes that are already hosting virtual machines in a specified group.
    - `SameHostFilter`: Passes the node that is hosting all other VMs in a set of VMs.

3.  Weights. The scheduler weighs the filtered compute nodes by using the enabled weighers and their multipliers, to decide which node has the highest priority for launching a VM. The following weighers are available:

    - `RAMWeigher`: Weighs nodes based on the available RAM. It accounts for the physical RAM on a node with the overcommitment ratio, excluding the RAM reserved for system and storage services, and provisioned for VMs.
    - `CPUWeigher`: Weighs nodes based on the available virtual CPUs. It accounts for the physical CPU cores on a node with the overcommitment ratio, excluding the vCPUs reserved for system and storage services, and provisioned for VMs
    - `ServerGroupSoftAntiAffinityWeigher`: Weighs nodes based on the number of VMs running on them from the same VM group in increasing order.
    - `PCIWeigher`: Weighs nodes based on the number of available PCI devices and the number of PCI devices requested by a VM.
    - `MetricsWeigher`: Weighs nodes based on their real-time metrics.

    First, each weight is normalized to a value between 0.0 and 1.0, depending on the availability of a resource. Then, a multiplier is applied to each weight. The weight multiplier defines the weigher priority compared to other weighers. The final weight for a node is calculated by using this formula:

        node_weight = weight1_multiplier * norm(weight1) + weight2_multiplier * norm(weight2) + ...

    The node with the highest weight is considered by the scheduler the most suitable for launching a VM.

<img src="resources/images/vm_scheduling.png" style="max-width: 75%;max-height: auto;" />

To change the default VM scheduling behavior in the compute cluster, you need to create a configuration file in the YAML format, and then use it to reconfigure the compute cluster.

## To create the scheduler configuration file

Set custom weight multipliers to any of the enabled weighers. Valid values are float. The following weight multipliers can be defined in the configuration file:

`ram_weight_multiplier`

>If set to a positive value, the scheduler will place VMs on nodes with more available RAM, and thus, spread them evenly across all compute nodes. In this case, however, you may end up unable to launch large VMs on particular nodes while having plenty of free RAM in the entire cluster.

>If set to a negative value, the scheduler will place VMs on nodes with less available RAM, which will optimize VMs distribution and fill up nodes as much as possible.

>The default value is 1.0.

`cpu_weight_multiplier`

If set to a positive value, the scheduler will place VMs on nodes with more available vCPUs, and thus, spread them evenly across all compute nodes. In this case, however, you may end up unable to launch large VMs on particular nodes while having plenty of free vCPUs in the entire cluster.

If set to a negative value, the scheduler will place VMs on nodes with less available vCPUs, which will optimize VMs distribution and fill up nodes as much as possible.

The default value is 1.0.

#### `soft_anti_affinity_weight_multiplier`
The multiplier only accepts positive values. The default value is 5.0.

#### `pci_weight_multiplier`
The multiplier only accepts positive values. The default value is 1.0.

#### `metrics_weight_multiplier`
If set to a value greater than 1.0, the weight of the metrics specified by the `metrics_weight_setting` parameter will be increased.

If set to a value between 0.0 and 1.0, the weight of the metrics specified by the `metrics_weight_setting` parameter will be reduced.

If set to a negative value, the node with lower metrics specified by the `metrics_weight_setting` parameter will have a higher weight.

The default value is 1.0.

`metrics_weight_setting`

Specifies the node metrics and their multipliers to use for weighing.

Valid metric names are the following:

- `cpu_percent`
- `cpu_frequency`
- `cpu_kernel_time`
- `cpu_kernel_percent`
- `cpu_user_time`
- `cpu_user_percent`
- `cpu_idle_time`
- `cpu_idle_percent`
- `cpu_iowait_time`
- `cpu_iowait_percent`
- `mem.free.mb`
- `mem.free.percent`
- `mem.cached.mb`
- `mem.cached.percent`
- `mem.buffers.mb`
- `mem.buffers.percent`

The default metric multiplier is 1.0.

The scheduler configuration file may look like this:

- cpu_weight_multiplier: -1.0

  The scheduler will consolidate virtual machines on nodes with less available vCPUs.

- ram_weight_multiplier: 2.0
      metrics_weight_multiplier: 2.5
      metrics_weight_setting:
         cpu_user_time: 3.0
         cpu_kernel_time: 1.5

  The final node weight will be calculated as follows:

      node_weight = 2.0 * norm(free_ram_mb) + 2.5 * (3.0 * norm(cpu_user_time) + 1.5 * norm(cpu_kernel_time))

  When placing virtual machines, the scheduler will prefer nodes with more available RAM and real-time CPU usage.

## To apply new VM scheduling parameters

Pass the scheduler configuration file to the `vinfra service compute set` command. For example:

    # cat scheduler.yaml
    ram_weight_multiplier: 2.0
    metrics_weight_multiplier: 2.5
    metrics_weight_setting:
       cpu_user_time: 3.0
       cpu_kernel_time: 1.5
    # vinfra service compute set --scheduler-config scheduler.yaml

To check that the scheduler parameters are successfully modified, run:

    # vinfra service compute show
    +--------------+---------------------------------------------+
    | Field        | Value                                       |
    +--------------+---------------------------------------------+
    | <...>        | <...>                                       |
    |              | scheduler:                                  |
    |              |   cpu_weight_multiplier: 1.0                |
    |              |   metrics_weight_multiplier: 2.5            |
    |              |   metrics_weight_setting:                   |
    |              |     cpu_kernel_time: 1.5                    |
    |              |     cpu_user_time: 3.0                      |
    |              |   pci_weight_multiplier: 1.0                |
    |              |   ram_weight_multiplier: 2.0                |
    |              |   soft_anti_affinity_weight_multiplier: 5.0 |
    | status       | active                                      |
    | storages     | - vstorage                                  |
    +--------------+---------------------------------------------+

The applied changes are consistent on all compute nodes and not overwritten after product updates and upgrades.

<div class="MCHelpControl MCHelpControl-Related relatedTopics relatedTopicssee-also">

<span class="MCHelpControl-RelatedHotSpot_ MCHelpControl-RelatedHotSpot_see-also"><img src="resources/images/transparent.gif" class="MCHelpControl_Image_Icon" width="16" height="16" alt="Related Topics Link Icon" />See also</span>

- <a href="configuring-compute-parameters.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Configuring compute parameters</a>
- <a href="configuring-memory-for-virtual-machines.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Configuring memory for virtual machines</a>
- <a href="changing-vcpu-overcommitment.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Changing virtual CPU overcommitment</a>
- <a href="configuring-vm-cpu-features.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Configuring CPU features for virtual machines</a>

</div>
