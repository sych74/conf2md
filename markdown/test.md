# Viewing audit log

In the audit log, you can view all of the management operations performed by users and their activity events.

## To view a log entry

<div class="tabs-container">

<div class="tab">

### Admin panel

1.  Go to the **Monitoring** \> **Audit log** screen to view the list of audit log entries.
2.  Click the required log entry on the list to open its details.

[![](logs_and_alerts4_vz_thumb_0_100.png)](logs_and_alerts4_vz.png)

</div>

<div class="tab">

### Command-line interface

Use the following command:

```
vinfra cluster auditlog show <auditlog>
```

`<auditlog>`
Audit log ID

For example, to the details of the audit log entry about the storage cluster creation, run:

```
# vinfra cluster auditlog list
+----+-----------+------------------------+--------------------------+---------------------+
| id | username  | type                   | activity                 | timestamp           |
+----+-----------+------------------------+--------------------------+---------------------+
| 8  | admin     | CreateCluster          | Create cluster           | 2021-09-07T17:39:16 |
| 7  | anonymous | RegisterNewNode        | Register new node        | 2021-09-07T17:39:14 |
| 6  | anonymous | RegisterNewNode        | Register new node        | 2021-09-07T17:39:10 |
| 5  | admin     | GetRegistrationToken   | Get registration token   | 2021-09-07T17:39:08 |
| 4  | admin     | GetRegistrationToken   | Get registration token   | 2021-09-07T17:39:04 |
| 3  | admin     | LoginUser              | User login               | 2021-09-07T17:39:04 |
| 2  | anonymous | UpdateNodeRegistration | Update node registration | 2021-09-07T17:39:02 |
| 1  | anonymous | RegisterNewNode        | Register new node        | 2021-09-07T17:38:54 |
+----+-----------+------------------------+--------------------------+---------------------+
# vinfra cluster auditlog show 8
+--------------+--------------------------------------+
| Field        | Value                                |
+--------------+--------------------------------------+
| activity     | Create cluster                       |
| cluster_id   |                                      |
| cluster_name |                                      |
| component    | Cluster                              |
| details      | - id: node                           |
|              |   name: Node                         |
|              |   value: node001.vstoragedomain      |
| id           | 8                                    |
| message      | Create cluster "cluster1"            |
| node_id      | c3b2321a-7c12-8456-42ce-8005ff937e12 |
| result       | success                              |
| task_id      | r-38c61bb2c7144cef                   |
| timestamp    | 2021-09-07T17:39:16                  |
| type         | CreateCluster                        |
| user_id      | c727a901a6444ee1a8ad31e3d5b53b3a     |
| username     | admin                                |
+--------------+--------------------------------------+
```

</div>

</div>

<div class="MCHelpControl MCHelpControl-Related relatedTopics relatedTopicssee-also">

<span class="MCHelpControl-RelatedHotSpot_ MCHelpControl-RelatedHotSpot_see-also"><img src="resources/images/transparent.gif" class="MCHelpControl_Image_Icon" width="16" height="16" alt="Related Topics Link Icon" />See also</span>

- <a href="viewing-alerts.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Viewing alerts</a>
- <a href="viewing-cluster-logs.html" class="MCHelpControlListItemLink MCRelatedTopicsControlListItemLink">Viewing cluster logs</a>

</div>
