---
draft: false
title: "Tomcat Security"
aliases: "/tomcat-security/"
seoindex: "index, follow"
seotitle: "Tomcat Security"
seokeywords: "tomcat application access, limit access java app, set the authentication, authentication tomcat, deny access for ip, ban the ip, ip resrtiction, configure authentication tomcat, add authentication"
seodesc: "Find out how to set up the additional security precaution in front of your application hosted with Tomcat application server. Two most common ways - set the authentication or deny access through ip."
menu:
    docs:
        title: "Tomcat Security"
        url: "/tomcat-security/"
        weight: 50
        parent: "tomcat-and-tomee"
        identifier: "tomcat-security.md"
---

# Security Configs for Tomcat Applications


This instructions shows how to protect an application running on a **Tomcat** server in the platform. We recommend two possible solutions on how to restrict access to your app:

* [request the user authentication](#authentication)
* [deny the access for specified IP addresses](#deny-client-ip-addresses)

You can choose one of them or use both methods together.


## Authentication

To set up the authentication in front of your web-application deployed to Tomcat server, perform the next configurations:

1\. Open the platform dashboard and click the **Config** button next to the Tomcat server in your environment.

2\. Go to the **/opt/tomcat/conf** folder and double-click the ***tomcat-users.xml*** file in order to open it.
Use the following string format in order to specify new users roles and credentials:

```xml
<user username="test" password="test" roles="admin">
```

![tomcat users](tomcat-users.png)

Save the changes made.

3\. Then navigate to the ***web.xml*** file (it is contained in the same **/opt/tomcat/conf** folder) and specify the security constraint for the newly created user.

```xml
<security-constraint>
<web-resource-collection>
  <url-pattern>/*</url-pattern>
</web-resource-collection>
<auth-constraint>
  <role-name>admin</role-name>
  <role-name>user</role-name>
</auth-constraint>
</security-constraint>
<login-config>
<auth-method>BASIC</auth-method>
<realm-name>Test Realm</realm-name>
</login-config>
```

![web xml tomcat](web-xml-tomcat.png)

4\. Don't forget to **Save** the changes and **Restart** your Tomcat application server.

If you've done everything correctly, a user will meet the authentication window while trying to access the application.

![tomcat authentication](authentication-tomcat.png)


## Deny Client IP Addresses

In the case you would like to deny the access to your web-application for particular client IP addresses follow the next steps:

1\. Press the **Config** button for the Tomcat app server in the environment with your application deployed.

2\. Navigate to the **/opt/tomcat/webapps/ROOT/META-INF** folder and open the file named ***context.xml***.

3\. Enter the next strings in the **context.xml** file:

```xml
<Context antiJARLocking="true" path="/">
    <Valve className="org.apache.catalina.valves.RemoteIpValve" />
    <Valve className="org.apache.catalina.valves.RemoteAddrValve" deny="{IP_address}" />
</Context>
```

![context xml](context-xml-tomcat.png)

{{%tip%}}**Note**: In the case you've attached the **Public IP** to your environment you can omit this string:

```xml
<Valve className="org.apache.catalina.valves.RemoteIpValve" />
```
{{%/tip%}}

4\. Press **Save** button and **Restart** Tomcat server.

After the configurations setted up, the user with denied IP address will meet the HTTP Status 403 error while trying to access your application.

![access denied](access-denied.png)


## What's next?

* [Tomcat Server](/tomcat/)
* [Java App&Server Configuration](/java-application-server-config/)
* [NGINX-Balancer Security](/nginx-balancer-security/)