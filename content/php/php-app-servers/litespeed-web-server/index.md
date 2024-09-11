---
draft: false
title: "LiteSpeed Web Server"
aliases: "/litespeed-web-server/"
seoindex: "index, follow"
seotitle: "LiteSpeed Web Server"
seokeywords: "litespeed, litespeed server, litespeed application server, litespeed web server, litespeed php, litespeed installation, create litespeed, php hosting, litespeed php hosting, paas for litespeed, litespeed admin panel, litespeed license"
seodesc: "Learn about PHP hosting with the LiteSpeed Web Server in the platform. Follow the simple steps of the LiteSpeed PHP application server installation and find out about its license pricing."
menu:
    docs:
        title: "LiteSpeed Web Server"
        url: "/litespeed-web-server/"
        weight: 30
        parent: "php-app-servers"
        identifier: "litespeed-web-server.md"
---

# LiteSpeed Web Server

{{%tip%}}The **LiteSpeed Web ADC** stack is [HTTP/3](/http3/) ready with the feature support enabled by default. However, a [public IP address](/public-ip/) is required to bypass the Shared Load Balancer and work directly with the server over HTTP/3.{{%/tip%}}

<img src="01-litespeed-web-server-logo.png" width="100" alt="litespeed web server logo" style="float: left; margin-left: 10px; margin-right: 10px;" />
The **[LiteSpeed Web Server](https://www.litespeedtech.com/products/litespeed-web-server)** is a high performance and low memory consumption PHP web server with high scalability. It is built based on the best practices of the PHP hosting, utilizing the benefits of both *Apache* and *NGINX* implementations, and integrating its own optimizations.

The feature-rich structure of the LiteSpeed application server includes the following specifics:

* an event-driven architecture (like NGINX) consumes fewer resources than Apache process-based model, ensuring better performance with minimum memory and CPU usage
* full compatibility with commonly used Apache features including *mod_rewrite*, *.htaccess*, and *mod_security*
* individual optimization for the most popular hosting platforms (e.g. *WordPress*, *Magento*, *Drupal*, *Joomla*, etc.)
* support of the caching plugins, cutting-edge anti-DDoS features, built-in WAF security, etc.

{{%note%}}**Note:** Being a commercial software, LiteSpeed Web Server cannot be distributed freely, i.e. requires the license to be applied to the platform. If working with this application server, you'll be charged an [additional fee](#license-pricing) for usage of the license mentioned above.{{%/note%}}

The creation of a new LiteSpeed Web Server instance in the platform is straightforward.

1\. Log in to the dashboard and click the **New Environment** button at the top of the page.

![new environment button](02-create-new-environment-button.png)

2\. Within the opened topology wizard, switch to the ***PHP*** engine tab and choose **LiteSpeed Web Server** as your application server.

![LiteSpeed application server wizard](03-litespeed-application-server-wizard.png)

{{%tip%}}You may want to adjust some [dedicated environment variables](/environment-variables/) to customize your LiteSpeed Web Server:

* ***JELASTIC_AUTOCONFIG*** - enables (*enabled*, by default) or disables (*disabled*) autoconfiguration of the LiteSpeed worker processes count based on the allocated RAM and number of CPU cores
* ***LSWS_MAX_CHILDREN*** - redefines the maximum children process limit for the server. The variable is hidden by default as the platform sets this value equal to the number of available CPU cores (usually ensures the best operability). You need to manually add this variable and restart the server to redefine the value
* ***REDIS_ENABLED*** - enables (*true*) or disables (*false*, by default) object caching with Redis
* ***WAF*** - enables (*true*) or disables (*false*, by default) Web Application Firewall with the [Comodo](https://waf.comodo.com/) default ruleset
* **WP_PROTECT** - configures an action for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*off|on|drop|deny|throttle|captcha*; *off* by default)
* **WP_PROTECT_LIMIT** -  sets a limit for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*0|1|2-1000*; *10* by default)

![LiteSpeed variables](04-litespeed-variables.png){{%/tip%}}

Configure any other required parameters ([cloudlets](/automatic-vertical-scaling/), disk space, [regions](/environment-regions/), etc.) and proceed with the **Create** button.

3\. After creation, you can view the default *phpinfo* data on the server by clicking **Open in Browser** next to your LiteSpeed server:

![LiteSpeed open in browser](05-litespeed-open-in-browser.png)

4\. To start managing the server, access the **Admin Panel** with the appropriate button in the ***Additionally*** list next to the layer (access credentials are sent via email after the node creation).

![LitesSeed admin panel](06-litespeed-admin-panel.png)

{{%note%}}**Note:** There are some specifics while working with the platform implementation of the LiteSpeed via the admin panel:

* to ensure container stability, the [platform-native redeploy feature](/container-redeploy/) should be used instead of the **Actions > Version Manager** functionality

![LiteSpeed version management](07-litespeed-version-management.png)

* the notification about the license key expiration in the **Actions > Server Log Viewer** should be ignored as the leasing is automatically managed by the platform

![LiteSpeed license key expiration notice](08-litespeed-license-key-expiration-notice.png){{%/note%}}

The application [deployment](/deployment-guide/) process is the same as for any other application server.


## License Pricing

The platform seamlessly integrates the cost of the LiteSpeed license in accordance with the fair **pay-as-you-go** principles. Namely, the license is billed only for active containers on an hourly basis for 730 hours per month. In addition, license lifecycle management is fully automated:

- new licenses are issued for every newly-created container (e.g. during environment provisioning or horizontal scaling)
- updated while changing available resource limits within each container
- decommissioned while stopping the environment or scaling in

Based on your needs, you can select the required plan using a dedicated ***LiteSpeed License Manager*** add-on that is automatically installed on all the LiteSpeed-based nodes (*LS Web Server*, *[LS ADC](/litespeed-web-adc/)*, *[LLSMP](/lemp-llsmp/)*).

![LiteSpeed license manager](09-litespeed-license-manager.png)

{{%tip%}}**Tip:** By default, a license type is selected based on the RAM (i.e. number of cloudlets) available after the node creation:

- up to 2 GB (16 cloudlets) - free of charge
- up to 8 GB (64 cloudlets) - 0.014$ per hour (**10$** per month)
- over 8 GB (64 cloudlets) - 0.022$ per hour (**16$** per month){{%/tip%}}

Add-on allows choosing the LiteSpeed plan by specifying the required limits for:

- ***Workers*** - indicates how many processes will be spawned to do general server work
- ***Domains*** - sets the [top-level domains'](/custom-domains/) limit (subdomains are unlimited); any domain that exceeds the specified limit will result in a 403 error

![configure LiteSpeed license](10-configure-litespeed-license.png)

License Plan Name|Domain Limit|Workers|RAM Limit, GB<br>(max cloudlets)|Pricing (USD)
:---|:---:|:---:|:---:|:---:
*FREE Starter*|1|1|2 (16)|free of charge
*Site Owner*|5|1|8 (64)|0.014$ per hour<br>(**10$** per month)
*Site Owner Plus*|5|1|Unlimited|0.022$ per hour<br>(**16$** per month)
*Web Host Lite*|Unlimited|1|8 (64)|0.036$ per hour<br>(**26$** per month)
*Web Host Essential*|Unlimited|1|Unlimited|0.049$ per hour<br>(**36$** per month)
*Web Host Professional*|Unlimited|2|Unlimited|0.060$ per hour<br>(**44$** per month)
*Web Host Enterprise*|Unlimited|4|Unlimited|0.082$ per hour<br>(**60$** per month)
*Web Host Elite*|Unlimited|8+|Unlimited|0.126$ per hour<br>(**92$** per month)

Additionally, the add-on can automatically configure a **LiteMage Cache** extension for your server - a popular, fast, full page caching solution that caches dynamic pages as static files. Just turn on the appropriate setting within the add-on frame and choose the required plan (determines the number of [publicly cached objects](https://www.litespeedtech.com/products/litespeed-web-server/lsws-pricing/lsws-litemage-pricing#objects)) in the appeared **Options** field:

- **Starter** - 1500 cached objects (**0** USD/month)
- **Standard** - 25000 cached objects (**40** USD/month)
- **Unlimited** - unlimited cached objects (**100** USD/month)

![LiteMage cache for LiteSpeed](11-litemage-cache-for-litespeed.png)

{{%note%}}**Note:** The exact cost may vary slightly for the platforms with a currency other than USD; it depends on the conversion rate at the moment of the hourly billing event. All the account charges can be viewed via the **[Billing History](/monitoring-consumed-resources/#billing-history)** in the dashboard.

![LiteSpeed license in billing history](12-litespeed-license-in-billing-history.png){{%/note%}}


## What's next?

* [Apache PHP](/apache-php/)
* [NGINX PHP](/nginx-php/)
* [Deployment Guide](/deployment-guide/)
* [LiteSpeed Web ADC](/litespeed-web-adc/)