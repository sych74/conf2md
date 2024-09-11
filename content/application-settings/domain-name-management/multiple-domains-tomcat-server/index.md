---
draft: false
title: "Multiple Domains for Tomcat"
aliases: ["/multiple-domains-tomcat-server/", "/multiple-domains2/", "/multiple-domains-tomcat/"]
seoindex: "index, follow"
seotitle: "Multiple Domains for Tomcat"
seokeywords: "multiple domain hosting, multiple domain web hosting, multiple domain name hosting, multiple domains configuring, multiple domain names, host multiple domain names, http headers"
seodesc: "Host multiple different applications under their own different domain names within a single environment. Realize multiple domains setting at the HTTP Headers' layer."
menu: 
    docs:
        title: "Multiple Domains for Tomcat"
        url: "/multiple-domains-tomcat-server/"
        weight: 30
        parent: "domain-name-management"
        identifier: "multiple-domains-tomcat-server.md"
---

# Multiple Domain Names on Tomcat Server

Set up multiple domain names on the Tomcat server in order to increase the usability, efficiency and scalability of your application, as well as save your costs without having to configure separate instances. For this, make some minor adjustments within Tomcat configuration files as described below.

1\. Log into the platform dashboard and click the **New Environment** button:

![PaaS main buttons](01-paas-main-buttons.png)

2\. In the **Environment Topology** dialog, pick your application server (e.g. [Tomcat 9](/tomcat/)), and type your environment name, for example, *multibinding*.

![topology wizard](02-topology-wizard.png)

In a minute your environment will be successfully created.

![new Tomcat environment](03-new-tomcat-environment.png)

3\. You can buy and set up your own domain names instead of default ones by adding CNAME record or by setting A Records. Read more in the [Custom External Domain Name Binding](/custom-domains/) document.

4\. Go back to the platform dashboard, click the **Settings** button for your environment and bind your domains.

![environment settings button](04-environment-settings-button.png)

In our example, we'll use ***tomcatfirst.tk*** for the first domain name, and ***tomcatsecond.tk*** for the second.

![bind custom domain](05-bind-custom-domain.png)

5\. Now you need to deploy the projects.

* Upload the application file to the **Deployment Manager** and press **Deploy to** button.  

As an example, we use *Hello World* which is available in Deployment Manager by default.

![deploy application](06-application-deployment.png)

When the **Deploy** form appears choose your environment and assign the context (**tomcatfirst**, in our case). Then press **Deploy** button.

![deploy dialog](07-deploy-dialog.png)

* Upload the second application archive. We will use modified *Hello World* (the words &ldquo;You did it!&rdquo; are recolored in red) just to see the difference at the final steps.

Then deploy this application to the same environment but with different context, (e.g. **tomcatsecond**).

![deploying second app into environment](08-deploy-second-app.png)

When deployment is finished you have two applications deployed in your environment.

![environment with two apps](09-environment-with-two-apps-deployed.png)

6\. Now click on **Сonfig** button for Tomcat and navigate to ***server.xml*** file (the **/opt/tomcat/conf** directory).

![server.xml config file](10-server-xml-config-file.png)

Add ***Host*** tags for each domain you want to bind:

```xml
<Host name="external.domain.tld" appBase="webapps/context_name" autoDeploy="true">
    <Alias>external.domain.tld</Alias>
    <Context path="" docBase="${catalina.base}/webapps/context_name"/>
</Host>
```

In our sample, we add the following code to ***server.xml*** file:

```xml
<Host name="tomcatfirst.tk" appBase="webapps/tomcatfirst" autoDeploy="true">
<Alias>tomcatfirst.tk</Alias>
<Context path="" docBase="${catalina.base}/webapps/tomcatfirst"/>
</Host>
<Host name="tomcatsecond.tk" appBase="webapps/tomcatsecond" autoDeploy="true">
<Alias>tomcatsecond.tk</Alias>
<Context path="" docBase="${catalina.base}/webapps/tomcatsecond"/>
</Host>
```

![configuring tomcat server](11-adjust-tomcat-settings.png)

7\. **Save** the changes and **restart** Tomcat.

![restart nodes button](12-restart-nodes-button.png)

8\. Now you can check the results. Both your applications will be available through the specified domain names running on a single Tomcat server.

![first application with custom domain](13-first-application-custom-domain.png)

![second application with custom domain](14-second-application-custom-domain.png)

{{%note%}}**Note:** If you want to redeploy an application to the Tomcat instance with already configured *server.xml*, you need to comment *< Host >* block before redeploying and uncomment it afterwards.{{%/note%}}


## What's next?

* [Swap Domains](/swap-domains/)
* [Multiple Domains for GlassFish](/multiple-domains-glassfish/)
* [Multiple Domains with Public IP ](/multiple-domains/)

