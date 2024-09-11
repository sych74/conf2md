---
draft: false
title: "LiteSpeed Web ADC"
aliases: "/litespeed-web-adc/"
seoindex: "index, follow"
seotitle: "LiteSpeed Web ADC"
seokeywords: "litespeed, litespeed adc, litespeed balancer, litespeed load balancer, litespeed traffic balancing, litespeed installation, create litespeed, litespeed adc hosting, paas for litespeed, litespeed admin panel, litespeed adc license"
seodesc: "Learn about the LiteSpeed Web ADC (application delivery controller) load balancer in the platform. Follow the simple steps of the LiteSpeed balancer node installation and find out about its license pricing."
menu:
    docs:
        title: "LiteSpeed Web ADC"
        url: "/litespeed-web-adc/"
        weight: 30
        parent: "load-balancers"
        identifier: "litespeed-web-adc.md"
---

# LiteSpeed Web ADC

{{%tip%}}The **LiteSpeed Web ADC** stack is [HTTP/3](/http3/) ready with the feature support enabled by default. However, a [public IP address](/public-ip/) is required to bypass the Shared Load Balancer and work directly with the server over HTTP/3.{{%/tip%}}

<img src="01-litespeed-web-adc-logo.png" width="200" alt="LiteSpeed Web ADC logo" style="float:left;margin:5px 10px">

The **[LiteSpeed Web ADC](https://www.litespeedtech.com/products/litespeed-web-adc)** (Application Delivery Controller) is a high-performance HTTP load balancing solution. It not just distributes traffic but also improves the speed and reliability of the services on the backend. Such benefits are achieved through the implementation and support of the most innovative and efficient technologies required for load balancing, e.g. next-generation HTTP/3 (QUIC) transport protocol.

LiteSpeed Web ADC is suitable for the projects of any scale, being able to handle everyday traffic and seasonal spikes alike. This balancer will surely get the most of your application due to its [numerous features](https://www.litespeedtech.com/products/litespeed-web-adc/features).

{{%note%}}**Note:** Being a commercial software, LiteSpeed Web Server cannot be distributed freely, i.e. requires the license to be applied to the platform. If working with this application server, you'll be charged an [additional fee](#license-pricing) for usage of the license mentioned above.{{%/note%}}

Get your own LiteSpeed Web ADC load balancer server at the platform by following the steps below.

1\. Log in and click the **New Environment** button at the top of the dashboard.

![create new environment](02-create-new-environment.png)

2\. Configure the preferred topology via the opened wizard and choose **LiteSpeed Web ADC** as your load balancer.

![LiteSpeed ADC in topology wizard](03-litespeed-adc-in-topology-wizard.png)

{{%tip%}}**Tip:** You can apply some customization to your LiteSpeed ADC by adjusting some of the [dedicated environment variables](/environment-variables/):

* **JELASTIC_AUTOCONFIG** - enables (*enabled*, by default) or disables (*disabled*) autoconfiguration of the LiteSpeed worker processes count based on the allocated RAM and number of CPU cores
* **DEFAULT_CLUSTER** - selects the load balancing type for requests' proxying (*HTTP*, *AJP*, *FCGI*, *LSAPI*). If working with some custom backends, this logic can be disabled (*0*, *disabled*, *false*)
* **WP_PROTECT** - configures an action for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*off|on|drop|deny|throttle|captcha*; *off* by default)
* **WP_PROTECT_LIMIT** -  sets a limit for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*0|1|2-1000*; *10* by default)

![LiteSpeed ADC variables](04-litespeed-adc-variables.png){{%/tip%}}

Click **Create** to proceed.

3\. If you click the **Open in Browser** button for the LiteSpeed balancer, one of the backend application servers will be automatically accessed.

![LiteSpeed ADC open in browser](05-litespeed-adc-open-in-browser.png)

4\. To manage your load balancer, you can access its **Admin Panel**. Click the appropriate button in the ***Additionally*** list next to the layer (access credentials are sent via email after the node creation).

![LiteSpeed ADC admin panel](06-litespeed-adc-admin-panel.png)

{{%note%}}**Note:** There are some specifics while working with the platform implementation of the LiteSpeed via the admin panel:

* to ensure container stability, the [platform-native redeploy feature](/container-redeploy/) should be used instead of the **Actions > Version Manager** functionality

![LiteSpeed ADC version management](07-litespeed-adc-version-management.png)

* the notification about the license key expiration in the **Actions > Server Log Viewer** should be ignored as the leasing is automatically managed by the platform

![LiteSpeed ADC license key expiration notice](08-litespeed-adc-license-key-expiration-notice.png)
{{%/note%}}

In case you need to adjust any of the configuration files, you can work over the [dashboard file manager](/configuration-file-manager/) or establish an [SSH connection](/ssh-access/).


## License Pricing

The platform seamlessly integrates the cost of the LiteSpeed license in accordance with the fair **pay-as-you-go** principles. Namely, the license is billed only for active containers on an hourly basis for 730 hours per month. In addition, license lifecycle management is fully automated:

- new licenses are issued for every newly-created container (e.g. during environment provisioning or horizontal scaling)
- updated while changing available resource limits within each container
- decommissioned while stopping the environment or scaling in

Based on your needs, you can select the required plan using a dedicated ***LiteSpeed License Manager*** add-on that is automatically installed on all the LiteSpeed-based nodes ([LS Web Server](/litespeed-web-server/), LS ADC, [LLSMP](/lemp-llsmp/)).

![LiteSpeed ADC license manager](09-litespeed-adc-license-manager.png)

The add-on allows switching between plans by adjusting the number of ***Workers*** (processes to do general server work). Also, the ***LiteMage*** caching solution (with unlimited [publicly cached objects](https://www.litespeedtech.com/products/litespeed-web-server/lsws-pricing/lsws-litemage-pricing#objects)) can be automatically configured for LiteSpeed ADC for an additional price of **149$** per month.

![configure LiteSpeed ADC license](10-configure-litespeed-adc-license.png)

License Type|Workers|Pricing (USD)<br>per 1 GB per Hour|Pricing (USD)<br>Min (Max) per Month
:---|:---:|:---:|:---:
*Web ADC Small (default)*|1|0.01$|7.30$ (**65$**)
*Web ADC Medium*|2|0.02$|14.60$ (**130$**)
*Web ADC Large*|4|0.04$|29.20$ (**260$**)
*Web ADC Ultimate*|8|0.08$|58.40$ (**520$**)

The license price is calculated dynamically based on the network traffic processed by the node at the rate specified via the **per 1 GB per Hour** column. Note that active environments are charged for at least 1GB, even if there was no traffic at all during an hour (a minimum fee for the license usage). Also, the license cost per month cannot go above the maximum value specified in the table. For example, for the default *Web ADC Small* plan, any traffic over 6500GB is free of charge until the end of the month (the first charge defines the starting date).

{{%note%}}**Note:** The exact cost may vary slightly for the platforms with a currency other than USD; it depends on the conversion rate at the moment of the hourly billing event. All the account charges can be viewed via the **[Billing History](/monitoring-consumed-resources/#billing-history)** in the dashboard.

![LiteSpeed ADC license in billing history](11-litespeed-adc-license-in-billing-history.png){{%/note%}}


## LiteSpeed ADC Testing

When performing testing of the LiteSpeed Web ADC load balancer, you should take into consideration the following peculiarities:

1\. By default, the load balancer operates in the **Stateful** mode, which tracks sessions associated with each back-end server (also called "Session Affinity"). It means that requests from a single source will always go to the same back-end server (unless it's not working).

2\. If LiteSpeed ADC does not have its own [public IP](/public-ip/), all the requests go through the platform's [Shared Load Balancer](/shared-load-balancer/). In such a case, ADC considers that the load comes from a single IP address (of the Shared Load Balancer).

As a result, for the proper testing of the <u>*production cluster*</u> with LiteSpeed ADC as a load balancer, you need to attach public IP and send requests from multiple sources. Alternatively, you can temporarily switch to the **Stateless** mode, which does not care about sessions (recommended during the <u>*development/testing stages*</u> only). Check out more about [LiteSpeed ADC testing](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:lslb:basic_config#testing) at the official documentation.


## Disabling Health Checks

LiteSpeed ADC automatically monitors the state of the backends and excludes problematic ones to ensure project availability to the end-users. However, in some cases such behavior may not be needed - for example, WordPress-based sites in the *maintenance mode* return a 503 HTTP status code, which excludes the application server from the load balancer’s routes. As a result, a generic balancer’s 500 status code is shown to users instead of the custom WordPress maintenance screen.

In this section, we’ll show how to temporarily disable automatic health checks on the LiteSpeed ADC.

1\. Log in to the LiteSpeed ADC console and go to the **Configuration > Clusters > clusterHTTP > Worker Group** section:

![LiteSpeed ADC work group configurations](12-litespeed-adc-work-group-configurations.png)

2\. Locate the ***Ping URL*** setting and clear the value.

![LiteSpeed ADC ping URL](13-litespeed-adc-ping-url.png)

Repeat this operation for all the Worker Groups.

3\. Perform a **Graceful Restart** to apply the new settings.

![LiteSpeed ADC graceful restart](14-litespeed-adc-graceful-restart.png)

{{%note%}}**Note:** Once the initial operation (the one that requires health check disabling) is finished, be sure to restore Ping URL parameters to ensure that actual problems with the backends won’t be missed.{{%/note%}}


## What's next?

* [Load Balancing](/load-balancing/)
* [LiteSpeed Web Server](/litespeed-web-server/)
* [NGINX Load Balancer](/nginx-load-balancer/)
* [HAProxy](/haproxy/)
* [Varnish](/varnish/)