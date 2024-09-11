---
draft: false
title: "Managing Timezone Settings"
aliases: "/timezone-management/"
seoindex: "index, follow"
seotitle: "Timezone Management"
seokeywords: "timezone rules java, java change timezone rules, java app server timezone management, update timezone rules php, php app servers timezone management, change timezone java, timezone rules php, timezone management java, update timezone rules java, php apache servers timezone management, java environment timezone management in cloud, php environment timezone management in cloud, java app server timezone management in cloud, php app server timezone management in cloud, timezone management spring boot, timezone management tomcat, php nginx servers timezone management, timezone management php nginx, timezone management glassfish"
seodesc: "All of the Java and PHP application servers are supplied with special timezone packages, which required for software, running inside the appropriate containers, and is regularly updated."
menu: 
    docs:
        title: "Managing Timezone Settings"
        url: "/timezone-management/"
        weight: 120
        parent: "application-settings"
        identifier: "timezone-management.md"
---

# Managing Timezone Data

All containers created within the platform utilize the UTC timezone by default. However, in case of necessity, you can easily change it to any preferable one with the help of the ***[TimeZone Change](#timezone-add-on)*** add-on. Follow the steps provided within the linked section to switch timezones on any of your instances.

Alternatively, you can apply the changes manually. For example, all of the Java and PHP application servers at the platform are supplied with special timezone packages, which includes data about the history of local time in different locations around the globe and current timezone rules. This information is required for software, running inside the appropriate containers, and is regularly updated within the corresponding server builds in the confines of the newly released platform versions.

Besides that, you can instantly update the timezone rules manually if necessary, or change the currently used TZ, based on the preferred location. So, below we'll reveal some specifics of the timezone data management at the platform for the application servers of the programming languagesmentioned above:

* [for Java](#timezone-rules-for-java)
* [for PHP](#timezone-rules-for-php)


## TimeZone Add-On

***TimeZone Change*** add-on can be installed on top of any of your environments, changing the timezone for all of the comprised containers in a matter of minutes.

1\. Before proceeding to installation, let's check the timezone on our target container using the ***date*** command.

![date before timezone change](01-date-before-timezone-change.png)

As you can see, the *UTC* zone is used (default for all platform-managed containers).

2\. Go to the [TimeZone Change](https://github.com/jelastic-jps/time-zone-change) add-on repository within the JPS Collection at GitHub. Copy a link to the ***manifest.jps*** file and [import](/environment-import/) it via the dashboard: *https://github.com/jelastic-jps/time-zone-change/blob/master/manifest.jps*.

![import timezone change add-on](02-import-timezone-change-add-on.png)

{{%tip%}}**Tip:** Based on your particular hosting provider settings add-on can be available via [platform Marketplace](/marketplace/).

![marketplace timezone add-on](03-marketplace-timezone-addon.png){{%/tip%}}

3\. Within the opened frame, select the target ***Environment*** and type the preferable ***TimeZone Name*** ([list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)) for it.

![install timezone change add-on](04-install-timezone-change-add-on.png)

Click **Install** to apply changes.

4\. After add-on installation, you can verify the timezone change by running the ***date*** command one more time.

![date after timezone change](05-date-after-timezone-change.png)

As you can see, the system time was successfully switched to the *EDT* (Eastern Daylight Time).


## Timezone Rules for Java

The timezone rules within Java compute nodes are delivered by means of the dedicated **TZdata** package, comprised in each appropriate container. Follow the instructions below to:

* [update timezone data](#updating-timezone-data)
* [change current timezone](#changing-timezone-java)

### Updating Timezone Data

Despite the fact the newest TZdata package edition is integrated into a node during its creation, after some time it becomes outdated due to periodical changing of the intrinsic data. Thus, old containers may require the corresponding updating from time to time (particularly, in order not to be recreated each time this is needed). For that, a special embedded **TZUpdater** tool is used, intended for keeping your timezone data accurate and up-to-date. It is fairly simple to use and can be run with a single-line command; you just need to:

1\. Connect to your Java environment via SSH, e.g. using the embedded [Web SSH](/web-ssh-client/) client:

![Web SSH button](06-web-ssh-button.png)

2\. Once inside, you can check the currently used **TZdata** version by executing the following string:

```bash
java -jar /usr/java/utils/tzupdater.jar -V
```

![check timezone rules version](07-check-tzdata-version.png)

3\. If you've observed the corresponding package in the chosen container is outdated, you can update the timezone information using the embedded **TZUpdater** tool:

```bash
java -jar /usr/java/utils/tzupdater.jar -u
```

![update server timezone](08-update-tzdata.png)

As you can see, getting the latest timezone package version for Java-powered server is a really simple operation with the platform.

### Changing Timezone Java

Now, let's discover how to check and change the application server's local time - we'll consider this on the example of a *Tomcat 9* server.

1\. Let's set the current timestamp to be shown at the server start page - this will help to quickly ensure that new timezone settings have been successfully applied and are relevant for now.

For that, paste the code below instead of the **/opt/tomcat/webapps/ROOT/index.jsp** file default content (the easiest way is to use the inbuilt [File Manager](/configuration-file-manager/) for that).

```html
<%@page import="java.util.*"%>
<html>
   <head>
       <title>TZ Page</title>
   </head>
   <body>
       <%=new Date(System.currentTimeMillis()).toString()%>
   </body>
</html>
```

![Java check time app](09-java-check-time.png)

2\. **Save** the changes and **Open** your environment **in browser** with the corresponding button to see the current server time, like:

![Java time UTC](10-java-time-utc.png)

3\. In order to change the actual timezone for a particular server, perform the following:

* for **Tomcat**, **TomEE**, **Payara**, **Spring Boot** and **Jetty**  
Switch to the ***variables.conf*** configuration file and add the ***-Duser.timezone*** variable with the [required zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) as a value, for example:  
*-Duser.timezone=US/Pacific*
{{%tip%}}**Note:** Depending on a particular application server used, the location of this file may vary:

* Tomcat 7, 8, 9, TomEE - */opt/tomcat/conf/variables.conf*
* Jetty 9 - */opt/jetty/etc/variables.conf*
* Payara 4, 5 - */opt/payara/glassfish/domains/domain1/config/variables.conf*
* Spring Boot 1, 2 - */opt/shared/conf/variables.conf*{{%/tip%}}
![variables.conf timezone variable](11-variables-conf-timezone.png)

* for **GlassFish**
Access the GF admin panel, go to the *Configurations > gfcluster-config* (or *server-config* for GF 4) *> JVM Settings > JVM Options* section and click the **Add JVM Option** button. Paste the corresponding string (e.g. *-Duser.timezone=US/Pacific*) within the appeared input field:
![GlassFish timezone variable](12-gf-timezone.png)

* for **WildFly**
Switch to the **/opt/wildfly/bin/standalone.conf** file (or, if a server was [scaled horizontally](/horizontal-scaling/), refer to the **/opt/wildfly/bin/domain.conf** config) and declare the corresponding variable using the following format:
*export JAVA_OPTS="-Duser.timezone=US/Pacific"*
![WildFly timezone variable](13-wildfly-timezone.png)

**Save** the made adjustment and **Restart** your application server in order to apply new settings.

4\. Now, just refresh the server start page or click **Open in Browser** again to see the updated local time:

![Java time PDT](14-java-time-pdt.png)

Great, new rules were applied successfully. In such a way, you can set any desired time location for your server without any problems, in a matter of minutes.


## Timezone Rules for PHP

Managing of the timezone settings at the platform PHP application servers (*Apache* and *NGINX*) is performed within the **[date]** section of the main PHP configuration file - ***php.ini***.

To access it, you need to click the **Config** button next to the required node. In the opened tab, locate the appropriate file within the file tree (or use the shortcut in the *Favorites* list to the left) and find the above-mentioned section:

![php.ini date settings](15-phpini-date.png)

As you can see, this section comprises two options, which can be used to:

* [get the latest timezone data](#checking-timezone-data)
* [set custom timezone](#changing-timezone-php)

### Checking Timezone Data

The first setting allows you to use the alternative external timezone database (namely - the [Olson](http://www.iana.org/time-zones) one) in case the internal one is outdated.

![PHP update timezone rules](16-php-update-timezone-rules.png)

For that, simply uncomment the appropriate extension through removing the first semicolon symbol, **Save** the made alteration and **Restart** your app server.  

Now, if you click **Open in browser** and scroll until the ***date*** section of the opened *phpinfo()* page, you'll see the latest timezone package version listed, with the denotation the external DB is used:

![PHP info date section](17-php-info-date.png)

### Changing Timezone PHP

The second option in the ***[date]*** section is intended for defining the current timezone location (by default it points to the *UTC* zone) of a node. For showing this on a real example, we'll modify the default server's start page (the **/var/www/webroot/ROOT/index.php** file) with the following code:

```php
<?php
echo date("h:i:sa");
?>
```

![PHP check time app](18-php-check-time.png)

Now, if **Saving** the updated file and clicking **Open in browser**, you'll see the timestamp output:

![PHP time UTC](19-php-time-utc.png)

Return to the platform dashboard and specify the desired [timezone](http://php.net/manual/en/timezones.php) as a value for the *date.timezone* parameter within the ***php.ini*** file (e.g. *Australia/Sydney* in our case).

![PHP change server timezone](20-php-change-timezone.png)

Again, **Save** your new configurations, **Restart** the corresponding PHP compute node and refresh the page with current time shown:

![PHP time Australia](21-php-time-australia.png)

That's it! As you can see, the timezone was successfully changed and now corresponds to a required location.


## What's next?

* [Managing Locale Settings](/locale-settings/)
* [Custom Error Page Settings](/custom-error-page/)
* [Java Application Server Configuration](/java-application-server-config/)
* [PHP Application Server Configuration](/php-application-server-config/)
* [How to Manage the Application Lifecycle in PaaS](/how-to-manage-application-lifecycle/)