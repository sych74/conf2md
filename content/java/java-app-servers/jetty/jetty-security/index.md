---
draft: true
title: "Jetty Security"
aliases: "/jetty-security/"
seoindex: "index, follow"
seotitle: "Jetty Security"
seokeywords: "jetty application access, limit access java app, set the authentication, authentication jetty, limit access, access restrictions, deny ip, deny access via ip, security configurations jetty, setting the authentication"
seodesc: "See the tutorial on setting up the additional security configurations for your application hosted with Jetty servlet container. Use authentication and denying access via IP to increase the safety of your app."
menu: 
    docs:
        title: "Jetty Security"
        url: "/jetty-security/"
        weight: 30
        parent: "jetty"
        identifier: "jetty-security.md"
---

# Security Configs for Jetty Applications

This document will help you to configure security realms for your **Jetty** application server in order to level up the protection of your app. Correctly configured realms provide the ability: 

* [to set the authentication and access control for your Jetty web application](#authentication)
* [to grant access to your app for dedicated IP-addresses](#deny-client-ip-addresses)

**Realm** is a login service, which is available to all web applications on a server if it is defined in a Jetty config file. Each realm consists of a range of users and has its unique name. Every specified user has the authentication information and a set of roles associated with it. One or many different realms can be configured depending on your needs.


## Authentication

To configure the authentication request in front of Jetty application server with your app deployed, follow the next instruction: 

1\. Open the platform dashboard with your environment listed and press **Config** button next to the Jetty server node:

![Jetty config button](01-jetty-config-button.png)

2\. Open the ***realm.properties*** file, located in the **/opt/jetty/etc** directory.

3\. Specify the new user's name and password as it is shown in the picture below (*test* and *admin* respectively).

If you are going to use just the default test realm, it's preferably to delete the already specified default users from this file (or just comment them).

![Jetty realm.properties config](02-jetty-realm-properties-config.png)

4\. Then open the ***webdefault.xml*** file (in the same **/opt/jetty/etc** directory) and specify the security restrictions for the created in the previous step new user using the following strings:  

```xml
<security-constraint>
<web-resource-collection>
  <url-pattern>/*</url-pattern>
</web-resource-collection>
<auth-constraint>
  <role-name>admin</role-name>
</auth-constraint>
</security-constraint>
<login-config>
<auth-method>BASIC</auth-method>
<realm-name>Test Realm</realm-name>
</login-config>
```

![Jetty webdefault.xml config](03-jetty-webdefault-xml-config.png)

5\. Don't forget to press the **Save** button in order to apply the changes and click **Restart** button for your Jetty server.

6\. To ensure everything works fine, open your application (**Open in Browser** button next to your Jetty environment with application deployed). You will see the authentication request window:

![Jetty authentication](04-jetty-authentication.png)


## Deny Client IP Addresses

If you need to protect your web-application, deployed to the Jetty application server, within denying access for a client with particular IP address, follow the next short instruction:

1\. Open the configuration manager (press **Config** button) for Jetty server in the environment with your application deployed.

2\. Navigate to the **/opt/jetty/work/Jetty\_0\_0\_0\_0\_8080_webapps\_.\_\_.h3czus/webapp** directory of your deployed web application and create the ***.htaccess*** file.

3\. Specify the IP restrictions in the newly created file. As an example you can use the following code, which allows access only for 192.168.152.1 IP address:

```
<Limit>
satisfy all
order deny,allow
deny from all
allow from 192.168.152.1
</Limit>
```

![Jetty .htaccess config](05-jetty-htaccess-config.png)

4\. Navigate to the **/opt/jetty/contexts** directory and find there the xml file, named after the context of your application (*test.xml* in our case).

5\. Using the *HTAccessHandler*, which interacts with the ***.htaccess*** policy file created earlier, protect the access to your application. Eventually your context xml file will look like the following one:

```xml
  <Call name="setSecurityHandler">
      <Arg>
          <New class="org.mortbay.jetty.security.HTAccessHandler">
              <Set name="protegee">
                  <Ref id=""/>
              </Set>
          </New>
      </Arg>
  </Call>
```

![configure access to test application](06-configure-access-to-test-application.png)

6\. After that **Save** the changes made and **Restart** your Jetty node.

As a result user with any IP except of the allowed one will see the next error while trying to open your application:

![Jetty forbidden access](07-jetty-forbidden-access.png)


## What's next?

* [Jetty](/eclipse-jetty/)
* [Java Server Configuration](/java-application-server-config/)
* [NGINX-Balancer Security](/nginx-balancer-security/)