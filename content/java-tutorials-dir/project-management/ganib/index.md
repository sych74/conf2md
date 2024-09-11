---
draft: false
title: "How to Deploy Ganib to PaaS"
aliases: "/ganib/"
seoindex: "index, follow"
seotitle: "How to Deploy Ganib to PaaS"
seokeywords: ""
seodesc: "Ganib Enterprises is one of the world&rsquo;s most popular and widely used open source project management software. The open source Ganib product suite includes an array of modules that provide..."
menu: 
    docs:
        title: "How to Deploy Ganib to PaaS"
        url: "/ganib/"
        identifier: "ganib.md"
---

# How to Deploy Ganib to PaaS
**Ganib** Enterprises is one of the world's most popular and widely used open source project management software. The open source Ganib product suite includes an array of modules that provide project management system (PMS), project portfolio management (PPM), project plans, project dashboard, documents management, time and attendance tracking (PTO), timesheet, desktop time tracking and screen capture tool, etc.

Let's see how to deploy Ganib to the platform.

## A. Create an Environment

1\. Open environment topology wizard by clicking **Create environment** button and choose **Tomcat** application server and **MySQL** database nodes. Set resource limits for them, enter environment name, and press **Create**.
![ganib 7883b5f904f95966acba7e076383da9aenv topology](7883b5f904f95966acba7e076383da9aenv-topology.png)

2\. In a few moments your new environment will appear at the panel.
![ganib 7883b5f904f95966acba7e076383da9anew env](7883b5f904f95966acba7e076383da9anew-env.png)

## B. Ganib Deployment

1\. To download Ganib project management system's community edition navigate to the [Sourceforge](http://sourceforge.net/projects/ganib/files/?source=navbar) page.
![ganib 7883b5f904f95966acba7e076383da9asourceforge](7883b5f904f95966acba7e076383da9asourceforge.png)

2\. Open the latest release folder (*Ganib 3.3* in our case) and download ***ganib.war*** file it contains.
![ganib 7883b5f904f95966acba7e076383da9aganib war](7883b5f904f95966acba7e076383da9aganib-war.png)

3\. Navigate back to the platform dashboard and upload **.war** file you've just downloaded.
![ganib 7883b5f904f95966acba7e076383da9auplod war](7883b5f904f95966acba7e076383da9auplod-war.png)

4\. Finally, click **Deploy to** button and choose previously created environment in the list.
![ganib 7883b5f904f95966acba7e076383da9adeploy to](7883b5f904f95966acba7e076383da9adeploy-to.png)

5\. In a minute Ganib application will be deployed to the chosen environment.
![ganib 7883b5f904f95966acba7e076383da9aganib deployed](7883b5f904f95966acba7e076383da9aganib-deployed.png)


## C. MySQL Configuration

1\. Click **Open in browser** button next to the MySQL node in your environment.
![ganib 7883b5f904f95966acba7e076383da9amysql open](7883b5f904f95966acba7e076383da9amysql-open.png)

2\. While you were creating the environment, the platform sent you the email with credentials to the database. Create a user and a database (e.g. *ganib*) using these credentials.
![ganib 7883b5f904f95966acba7e076383da9aadd db user](7883b5f904f95966acba7e076383da9aadd-db-user.png)

3\. After that unpack the downloaded Ganib **.war** file and find ***ganib.sql*** file in the **database** folder. Import it to the database you've created at the previous step.
![ganib 7883b5f904f95966acba7e076383da9aimport sql](7883b5f904f95966acba7e076383da9aimport-sql.png)

Wait for a few minutes till this operation will be completed.


## D. Ganib Configuration

1\. Navigate back to the dashboard and click **Config** button for **Tomcat** server:
![ganib 7883b5f904f95966acba7e076383da9atomcat config](7883b5f904f95966acba7e076383da9atomcat-config.png)

2\. Open the lib folder and upload [MySQL connector](http://dev.mysql.com/downloads/connector/j/) and [Java mail library](http://www.java2s.com/Code/Jar/j/java-mail.htm).
![ganib 7883b5f904f95966acba7e076383da9alibs](7883b5f904f95966acba7e076383da9alibs.png)

3\. Then navigate to the **server &gt; context.xml** file and add the following lines at the very bottom before closing Context tag.  
*&lt;Resource name="jdbc/GanibDB" auth="Container" type="javax.sql.DataSource" username="root" password="" driverClassName="com.mysql.jdbc.Driver" url="" maxActive="125" maxIdle="25" /&gt;*

{{%tip%}}
Note you should specify settings of your database in these strings:

* credentials you've received while environment creation
* URL for your database in the following format:   
```
jdbc:mysql://mysql-{env_name}.{[hoster's_domain](/paas-hosting-providers/)}:3306/{database_name}?useUnicode=true&characterEncoding=utf-8&autoReconnect=true
```
{{%/tip%}}

![ganib 7883b5f904f95966acba7e076383da9acontext xml](7883b5f904f95966acba7e076383da9acontext-xml.png)

4\. **Save** the changes you've made.

5\. Press **Restart** next to the Tomcat node in order to apply the configuration changes.
![ganib 7883b5f904f95966acba7e076383da9arestart tomcat](7883b5f904f95966acba7e076383da9arestart-tomcat.png)


## E. Start the Application

1\. Finally, click **Open in browser** button near your environment.
![ganib 7883b5f904f95966acba7e076383da9aopen in browser](7883b5f904f95966acba7e076383da9aopen-in-browser.png)

2\. You will see the Ganib start page and can proceed to using it.
![ganib 7883b5f904f95966acba7e076383da9aganib welcome page](7883b5f904f95966acba7e076383da9aganib-welcome-page.png)

Now, you have your own Ganib application deployed to the platform. Enjoy!