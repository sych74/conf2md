---
draft: false
title: "WordPress PaaS"
aliases: ["/virtuozzo-application-platform-for-wordpress/", "/wordpress-billing/", "/wordpress-ci-cd/", "/wordpress-plugins/"]
seoindex: "index, follow"
seotitle: "WordPress PaaS"
seokeywords: "wordpress paas, wordpress hosting, wordpress package, wordpress topology, wordpress installation, wordpress prepackaged topology"
seodesc: "The platform provides an automated WordPress hosting with multiple topologies of varying complexity (standalone, cluster, multi-region) available out-of-the-box. Choose the required Wordpress instance topology based on your project-specific needs."
menu:
    docs:
        title: "WordPress PaaS"
        url: "/virtuozzo-application-platform-for-wordpress/"
        weight: 10
        parent: "wordpress-edition"
        identifier: "virtuozzo-application-platform-for-wordpress.md"
---

# WordPress PaaS

Virtuozzo Application Platform for WordPress is a DevOps platform dedicated to WordPress hosting specifically. It offers a number of prepackaged topologies of varying complexity (from single-container solutions to clusters and synchronized multi-region instances), which covers all the range of use cases (from small testing installation to the enterprise-level clusters).

Below, you can find a list of all the standard [WordPress topologies](/wordpress-topologies/) available on the platform:

- **Standalone** - a single-container solution with NGINX
- **Standalone Pro** - a single-container solution with LiteSpeed
- **WooCommerce** - a single-container solution with NGINX and WooCommerce plugin
- **WooCommerce Pro** - a single-container solution with LiteSpeed and WooCommerce plugin
- **Cluster** - a clustered solution based on LiteSpeed and MariaDB Galera
- **WooCommerce Cluster** - a clustered solution based on LiteSpeed, MariaDB Galera, and WooCommerce plugin​
- **Multi-Region Standalone** - the Standalone Pro package deployed and synchronized between different regions

![WordPress topologies and plans](01-wordpress-topologies-and-plans.png)

{{%tip%}}**Tip:** The list of topologies, service plans, and specifics may vary for different platforms.{{%/tip%}}


## Platform Benefits

Virtuozzo Application Platform for WordPress provides numerous features that can significantly enhance your WordPress development and hosting experience:

- **automatic WordPress** instance installation with multiple preconfigured topologies
- **[robust dashboard](/wp-dashboard-overview/)** with numerous features you may like (built-in file manager, real-time statistics monitoring, etc.)
- automated **[backup and restore](/wordpress-backups/)** processes
- the **subscription-based** pricing model
- [powerful API](https://www.virtuozzo.com/application-platform-api-docs/) for automation and scripting


## What's next?

- [WordPress Dashboard](/wp-dashboard-overview/)
- [WordPress Topologies](/wordpress-topologies/)
- [WordPress Backups](/wordpress-backups/)
- [WordPress Security](/wordpress-security/)
- [WordPress PHP Optimization](/wordpress-php-optimization/)