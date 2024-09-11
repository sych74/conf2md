---
draft: false
title: "Database Auto-Configuration"
aliases: "/database-auto-configuration/"
seoindex: "index, follow"
seotitle: "Database Auto-Configuration"
seokeywords: "auto configuration, database auto configuration, database resource optimization, database container optimization, database optimization, database smart configuration"
seodesc: "The platform automatically optimizes database stacks configurations based on the number of allocated resources (cloudlets) to ensure efficient resource utilization and the best performance."
menu: 
    docs:
        title: "Database Auto-Configuration"
        url: "/database-auto-configuration/"
        weight: 20
        parent: "smart-auto-configuration"
        identifier: "database-configuration-overview.md"
---

# Database Auto-Configuration

The platform **[Smart Auto-Configuration](/auto-configuration/)** automatically adjusts the ***MySQL***, ***MariaDB***, and ***Percona*** databases in accordance with the resource limit allocated to the containers. Namely, the changes affect the ***/etc/my.cnf*** configuration file and the following settings in particular:

- *key_buffer_size*
- *table_open_cache*
- *myisam_sort_buffer_size*
- *innodb_buffer_pool_size*

Starting with the **5.7** and **8.0** versions of the **MySQL/Percona** and **MariaDB 10.x**, two additional parameters are configured by the platform:

- *innodb_buffer_pool_instances* - deprecated in MariaDB since the *10.6.x* (always 1 pool instance) 
- *innodb_buffer_pool_chunk_size*

If you want to manually change any of the settings from the list above, you need to set the ***JELASTIC_AUTOCONFIG*** [environment variable](/container-variables/) to "*false*", "*disable*", or "*0*". Otherwise, your custom changes will be overwritten.

![PaaS autoconfig variable](01-paas-autoconfig-variable.png)

{{%tip%}}**Tip:** Alternatively, you can override any of the settings in the ***/etc/my.cnf*** file (including ones managed by the platform's *Smart Auto-Configuration*) by stating them in the ***/etc/mysql/conf.d/custom.cnf*** file.{{%/tip%}}

### Legacy Implementation

If you want to manually change the auto-configured settings on the old containers, you need to remove the "*#Jelastic autoconfiguration mark.*" line at the start of the ***/etc/my.cnf*** file.

![PaaS autoconfiguration mark](02-paas-autoconfiguration-mark.png)


## What's next?

* [Smart Auto-Configuration](/auto-configuration/)
* [PHP Auto-Configuration](/php-auto-configuration/)
* [Configuration File Manager](/configuration-file-manager/)
* [Environment Variables](/environment-variables/)