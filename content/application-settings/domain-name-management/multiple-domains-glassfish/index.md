---
draft: false
title: "Multiple Domains for GlassFish"
aliases: ["/multiple-domains-glassfish/", "/multiple-domains-for-glassfish/"]
seoindex: "index, follow"
seotitle: "Multiple Domains for GlassFish"
seokeywords: "miltiple custom domains, domain names, multiple domain names, setting multiple domain, configure multiple domain, multiple domain benefits, multiple domain hosting, glassfish multiple domains, glassfish domains setting, virtual server gf, gh hosts"
seodesc: "Here is a detailed instruction describing the benefits of using multiple domain names and how to configure multiple domains for your Java environment with GlassFish application server."
menu:
    docs:
        title: "Multiple Domains for GlassFish"
        url: "/multiple-domains-glassfish/"
        weight: 40
        parent: "domain-name-management"
        identifier: "multiple-domains-glassfish.md"
---

# Running Multiple Custom Domains on GlassFish Server

Let's see how to easily set up a few domain names for Java application hosted with GlassFish container servlet, which combines enterprise-class facilities and open-source cost efficiency. It's an enterprise-ready application server with true interoperability and a wide range of features including superior documentation, configuration and administration.

To run multiple domains for your Java site on GlassFish server just follow the next simple steps.

1\. Log into the platform dashboard and click **Create environment** button.

2\. Pick **GlassFish** as an application server and specify the cloudlet limits for it. Then type your environment name and click **Create** button.

![multiple domains GlassFish environment wizard](01-environment-wizard.png)

3\. In a matter of seconds your environment will be successfully created and appears on the dashboard in the list of environments.

![GlassFish environment created](02-glassfish-environment-created.png)

4\. After that you need to add a CNAME record or set an A Record, as it is described in [Custom Domains](/custom-domains/) document.

5\. For binding your custom domain names click the **Settings** button next to your environment and choose the Custom domains setting. Then enter your domains in the appropriate field (we will use *myapplication.com* and *myapplication.org* as examples) and click **Bind** button.

![bind environment domains](03-bind-environment-domains.png)

{{%tip%}}**Note:** We've put entries into our hosts file for local testing so this will work only from our machine, which has those hosts' entries.{{%/tip%}}

6\. When you created the environment, the platform sent you the link and credentials to GlassFish DAS node. Log in to the admin panel using these credentials and navigate to the **Applications** tab in order to deploy your application.

![GlassFish admin panel applications](04-glassfish-admin-panel-applications.png)

7\. After your application is successfully deployed navigate to ***Configurations > default-config > Virtual Servers*** block and click **New** button in order to create a new virtual server.

![GlassFish admin panel virtual servers](05-glassfish-admin-panel-virtual-servers.png)

8\. Enter the ID for new server, in the **Hosts** field specify bounded to your environment custom domains separated by commas, then select the suitable http listener and pick the necessary web module.

![GlassFish new virtual server](06-glassfish-new-virtual-server.png)

9\. Save the changes and voil&agrave;! Now you can ensure that your application is available via the all specified domain names.

![GlassFish multiple domain names](07-glassfish-multiple-domain-names.png)

As you can see, it's very easy to manage application custom domains with the platform's rich set of tools. Enjoy!


## What's next?

* [GlassFish](/glassfish/)
* [GlassFish Auto-Clustering](https://www.virtuozzo.com/company/blog/glassfish-payara-auto-clustering-cloud-hosting/)
* [Multiple Domains on Tomcat Server](/multiple-domains-tomcat-server/)
* [Multiple Domains with Public IP](/multiple-domains/)