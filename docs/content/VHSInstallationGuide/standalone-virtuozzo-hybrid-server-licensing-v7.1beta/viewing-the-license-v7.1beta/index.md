---
draft: false
title: "Viewing the License v7.1Beta"
aliases: "/viewing-the-license-v7.1beta/"
seoindex: "index, follow"
seotitle: "Viewing the License v7.1Beta"
seokeywords: ""
seodesc: ""
menu:
    docs:
        title: "Viewing the License v7.1Beta"
        url: "/viewing-the-license-v7.1beta/"
        weight: 10
        parent: "get-started"
        identifier: "viewing-the-license-v7.1beta.md"
---
# Viewing the License v7.1Beta

You can use the `vzlicview` tool to view the information on the installed license and find out its current status. For example:

``` java
# vzlicview
Searching for installed licenses...
VZSRV       
        owner_name="Autogenerated Trial Licenses"       
        status="ACTIVE"       
        version=7.0       
        owner_id=70295522.10134133       
        hwid="3D6F.FFB2.1CD5.1E47.1325.BBE0.6C66.ACF5"       
        serial="BF3D.E943.18C5.5555.5D10.99D9.0310.DFA0"       
        expiration="07/08/2016 03:00:00"       
        start_date="06/07/2016 03:00:00"       
        issue_date="06/08/2016 16:27:11"       
        graceperiod=259200 (259200)       
        key_number="PSBM.10134133.0001"       
        cpu_total=8 (1)            
        architecture="x86"       
        architecture="x86_64"       
        platform="Linux"       
        product="PSBM"       
        nr_vms="unlimited" (2)       
        subscription="70295522:dd482d1a-5268-4980-ae06-2a288a4fb7ab"
```

You can also view the contents of license files with the `vzlicview -f` command. The output does not differ from that in the example above.

The license parameters are described in the following table.

| Column                | Description                                                                                                                                                                                        |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| owner\_name           | The name of the license owner.                                                                                                                                                                     |
| status                | License status. For a description of license statuses, see [License Statuses](#id-.ViewingtheLicensev7.1Beta-LicenseStatuses).                                                                     |
| version               | The version of Virtuozzo Hybrid Server for which the license was issued.                                                                                                                           |
| owner\_id             | The ID of the license owner.                                                                                                                                                                       |
| hwid                  | Server hardware identifier.                                                                                                                                                                        |
| serial                | License serial number. In particular, it is used to identify license files in `/etc/vz/licenses/`.                                                                                                 |
| expiration            | License expiration date if the license is time-limited.                                                                                                                                            |
| start\_date           | The date on which the license becomes active.                                                                                                                                                      |
| issue\_date           | The date on which the license was issued.                                                                                                                                                          |
| graceperiod           | Period, in seconds, during which Virtuozzo Hybrid Server continues to function after the license has expired or if the number of running virtual servers exceeds the limit defined by the license. |
| license\_update\_date | The date on which the license was last updated.                                                                                                                                                    |
| key\_number           | The number under which the license is registered on the Key Authentication server.                                                                                                                 |
| cpu\_total            | The total number of physical CPUs that the server is allowed to have.                                                                                                                              |
| architecture          | System architecture with which the license is compatible.                                                                                                                                          |
| platform              | Operating system with which the license is compatible.                                                                                                                                             |
| product               | The name of the product for which the license has been issued.                                                                                                                                     |
| keyserver\_host       | The hostname and port of the Key Authentication server.                                                                                                                                            |
| nr\_vms               | The number of virtual servers allowed to be simultaneously running on the server.                                                                                                                  |
| subscription          | The Virtuozzo Hybrid Server feature subscription key.                                                                                                                                              |

## License Statuses

------------------------------------------------------------------------

When viewing information on your licenses, pay special attention to the license status, which can be one of the following:

| Status  | Description                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTIVE  | The installed license is valid and active.                                                                                                                                                                                                                                                                                                                                                                          |
| VALID   | The license is valid and can be installed.                                                                                                                                                                                                                                                                                                                                                                          |
| EXPIRED | The license has expired. If an installed license expires, running virtual environments continue to run. Newly started VEs, however, are suspended after 10 minutes. If they cannot be suspended, they are stopped gracefully. If this cannot be done, they are stopped forcefully. If the node is rebooted or the license daemon is restarted, all VEs are treated as new and suspended (stopped) after 10 minutes. |
| GRACED  | The license is installed on the server but is currently on the grace period because it has expired or the number of running virtual servers exceeds the limit defined by the license.                                                                                                                                                                                                                               |
| INVALID | The license is invalid (for example, because of server architecture mismatch) or corrupt.                                                                                                                                                                                                                                                                                                                           |

