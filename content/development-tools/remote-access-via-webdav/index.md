---
draft: false
title: "Remote Access via WebDAV"
aliases: "/remote-access-via-webdav/"
seoindex: "index, follow"
seotitle: "Remote Access via WebDAV"
seokeywords: "webdav server, webdav client, setup webdav, webdav tutorial, java webdav, webdav free, webdav java, java webdav client, set up webdav, webdav configuration, webdav application, webdav java client, tutorial webdav"
seodesc: "See the tutorial on how to set up WebDAV for your Java application server. Make necessary configurations and use any WebDAV client to perform remove web authoring operations for free."
menu:
    docs:
        title: "Remote Access via WebDAV"
        url: "/remote-access-via-webdav/"
        weight: 80
        parent: "development-tools"
        identifier: "remote-access-via-webdav.md"
---

# Remote File Access via WebDAV

While setting up a website you can face the need to build some complicated method of viewing and updating the information on the site. **Web-based Distributed Authoring and Versioning (WebDAV)** is a set of extensions to HTTP that allows clients to perform remote web authoring operations. Some of these extensions overwrite protection by locking, name-space management and properties (metadata) are fully implemented. Other offered extensions include version management, advanced collections and access control with HTTP Digest Authentication. XML is used to encode method parameters and responses.

**WebDAV** is based on HTTP that already has widely deployed infrastructure. It means that any application built on top of WebDAV can use cryptographically strong authentication, proxying, caching and encryption with SSL, if so desired. Another advantage is that WebDAV uses XML, which means that the protocol itself can be extended without fragmenting it.

You can use **WebDAV** in the platform to create, change, copy and move files on your server and create and manage file directories right in the cloud, simply by accessing them via HTTP/HTTPS. By using WebDAV, you can have free, instant, and secure access to your application files anywhere you have a network connection.

So, let's see how to use this great solution for your Java applications in the cloud!


## Create Environment

1\. Log into the PaaS account.

2\. While in the platform dashboard, click the **Create environment** button:

![remote access via webdav create environment](create-environment.png)

3\. In the **Environment Topology** dialog, pick your application server (for example, **Tomcat 7 or 6**). Then type your environment name, for example, *webdavtest*.

![remote access via webdav webdav1](webdav1.png)

It will take just a minute for your environment to be created.

![remote access via webdav webdav2](webdav2.png)


## Upload Java Package

1\. Upload your Java WAR package to the **Deployment manager**.

![remote access via webdav webdav3](webdav3.png)

2\. Once the package is in the platform, deploy it to the environment you have created earlier.

![remote access via webdav webdav4](webdav4.png)

Open in browser your application to ensure that everything is ok.

![remote access via webdav webdav5](webdav5.png)


## Configure Tomcat

Tomcat implements the WebDAV specification using WebDAV Servlet, which is included with all standard Tomcat distributions. Follow the next steps to configure and test WebDAV connection.

1\. Click **config** button for Tomcat.

![remote access via webdav webdav7](webdav7.png)

2\. Tomcat comes prebundled with a WebDAV Level 2 servlet. To enable your Tomcat WebDAV connection, add the following to **web.xml** (server directory):

```xml
<servlet>
<servlet-name>webdav</servlet-name>
<servlet-class>org.apache.catalina.servlets.WebdavServlet</servlet-class>
<init-param>
    <param-name>debug</param-name>
    <param-value>0</param-value>
</init-param>
<init-param>
    <param-name>listings</param-name>
    <param-value>true</param-value>
</init-param>
<!-- The following for read-write access -->
<init-param>
    <param-name>readonly</param-name>
    <param-value>false</param-value>
</init-param>
</servlet>
<servlet-mapping>
<servlet-name>webdav</servlet-name>
<url-pattern>/webdav/*</url-pattern>
</servlet-mapping>
```

![remote access via webdav webdav8](webdav8.png)

3\. Make sure that only authorized users can access WebDAV to your context. Navigate to **tomcat-users.xml**, create a new user and designate a new role, for example:

```xml
<tomcat-users>
<user name="test" password="tomcat" roles="role1" />
</tomcat-users>
```

![remote access via webdav webdav9](webdav9.png)

4\. Define the role you have just created in the **auth-constraint** section of the **web.xml**:

```xml
<auth-constraint>
<role-name>role1</role-name>
</auth-constraint>
```

![remote access via webdav webdav10](webdav10.png)

5\. Save the changes and restart **Tomcat**.

![remote access via webdav webdav11](webdav11.png)


## Connect to Server

1\. Create a new connection using any desktop client for WebDav (we'll use BitKinex as an example).

![remote access via webdav webdav12](webdav12.png)

2\. Enter the URL of your server (*http://{your_env_name}.<a href="/paas-hosting-providers/">{hoster_domain}</a>/{context}/webdav*), specify login and password to your Tomcat user (in our case credentials are *test/tomcat*).

![remote access via webdav webdav13](webdav13.png)

3\. As you can see we have successfully connected to our server.

![remote access via webdav webdav14](webdav14.png)

As a result you'll see your files and will be able to edit them, update, add some new files, etc.

Enjoy with WebDAV and PaaS!


## What's next?

* [Apache WebDav Module](/apache-webdav-module/)
* [NGINX WebDav Module](/nginx-webdav-module/)
* [VPS Configuration](/vps/)