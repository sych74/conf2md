---
draft: false
title: "Diaspora*"
aliases: ["/diaspora/", "/diaspora-tutorial/"]
seoindex: "index, follow"
seotitle: "Diaspora* Ruby Tutorial"
seokeywords: "diaspora, diaspora ruby, diaspora tutorial, diaspora social network, host social network, ruby tutorial, redis tutorial, install diaspora"
seodesc: "Learn how to install the Diaspora* social network application on top of the Ruby-based application server and connect it to the Redis database."
menu:
    docs:
        title: "Diaspora*"
        url: "/diaspora/"
        weight: 20
        parent: "ruby-tutorials"
        identifier: "diaspora.md"
---

# How to Install Diaspora*

**Diaspora\*** is an open-source user-owned distributed social network with more than 1 million accounts all over the world. It consists of separate nodes named podes. Each pode operates a copy of the Diaspora software and represents a personal web-server.

So, let's find out how to create your own Diaspora* pode with the help of PaaS.


## Create Environment

1\. Log in to the platform dashboard using your credentials.

2\. Press **Create environment** button. In the opened environment topology wizard navigate to the **Ruby** programming language tab. Pick the following nodes:

* **Apache** application server
* **MySQL** database
* **Redis** data structure server

Then state the resources limits for the chosen nodes. Finally, enter name for your environment (e.g. *diaspora-network*), and click **Create** button.

![environment wizard](01-environment-wizard.png)

3\. After about a minute your new environment will appear at the dashboard.

![environment for Diaspora created](02-environment-for-diaspora-created.png)


## Diaspora* Deployment

1\. Navigate to the [Diaspora GitHub repository](https://github.com/diaspora/diaspora). There change the branch to ***master*** and click **Download ZIP** button.

![download Diaspora zip](03-download-diaspora-zip.png)

You will be offered to save **.zip** archive with the latest Diaspora* stable version.

2\. Then navigate back to the platform dashboard and upload this archive with the help of **Deployment manager**.

![upload Diaspora archive](04-upload-diaspora-archive.png)

3\. Then press **Deploy to..** button next to the *diaspora-master.zip* package. In the opened window choose *test* deployment type and click **Deploy**.

![deploy Diaspora application](05-deploy-diaspora-application.png)

{{%tip%}}**Note:** In order to run Diaspora\* in *production* mode you need to have certificate authorities (CA) certificates installed at your server.{{%/tip%}}

4\. The process of deployment can take some time, so be patient, please. Finally, you'll see a new *test* context listed for Apache.

![Diaspora application deployed](06-diaspora-application-deployed.png)


## Database Configurations

1\. Press **Open in Browser** button next to the **MySQL** node in your environment.

![open MySQL in browser](07-open-mysql-in-browser.png)

2\. In the opened browser tab log in using the MySQL credentials you've received while environment creation and navigate to the **SQL** section.

![database admin SQL tab](08-database-admin-sql-tab.png)

3\. You'll see an empty form for SQL request executing. Enter the following line there and click **Go** in order to create a new database named *diaspora_test*.

```
CREATE DATABASE diaspora_test CHARACTER SET utf8;
```

![create Diaspora database](09-create-diaspora-database.png)

4\. After that open the platform dashboard again and press **Config** button for **Apache** application server.

![Apache config button](10-apache-config-button.png)

5\. In the opened configuration manager navigate to the **webroot > config** folder, find ***database.yml.example*** file and copy its content.

![database yml example](11-database-yml-example.png)

6\. Then create new ***database.yml*** file in the same (**config**) folder and paste the copied strings to it.

![crerate database yml](12-crerate-database-yml.png)

7\. Now it's necessary to set up the connection between your application and MySQL database.

Find the section for MySQL configurations. Specify your MySQL ***host*** (URL to your database without *http://*) and credentials you've received while environment creation in ***username*** and ***password*** strings.

![configure database connection](13-configure-database-connection.png)

Don't forget to **Save** the changes made.


## Application Server and Redis Configurations

1\. Press **Config** button for **Apache** application server again.

![Apache config button](10-apache-config-button.png)

2\. Navigate to the **webroot > config** folder and create a new ***diaspora.yml*** file there. Then find ***diaspora.yml.example*** configuration file in the same folder, copy its content, and paste it into the newly created file.

![create diaspora yml](14-create-diaspora-yml.png)

3\. After that navigate to the ***configuration*** section in this file and change the following values:

* find the ***#url: "https:/\/example.org/"*** string and paste your environment's URL instead of *https:/\/example.org/* value (you can find it by pressing **Open in Browser** button for your environment and copying URL in the address bar).

![configure environment URL](15-configure-environment-url.png)

* scroll a bit lower and find the settings for remote Redis connection in the same file:

```
## URL for a remote redis.
## Don't forget to restrict the IP access!
## Leave it commented out for the default (localhost)
#redis: 'redis://exmaple_host'
#redis: 'redis://username:password@host:6379/0'
#redis: 'unix:///tmp/redis.sock'
```

Delete the **#** symbol from the ***#redis: 'redis://username:password@host:6379/0'*** line. Then substitute the values in this parameter with your own data, received via email after the environment creation.

![Redis DB credentials email](16-redis-db-credentials-email.png)

Change ***username*** and ***password*** values to the credentials for admin access to your Redis node. The same story with the ***host*** word: substitute it with the **DNS address** you can find in this letter.

![configure Redis connection](17-configure-redis-connection.png)

* finally, locate the ***#require_ssl: true*** line and change the *true* value to *false*

![set SSL config false](18-set-ssl-config-false.png)

It's time to **Save** the changes.

4\. Then navigate to the ***application.rb*** file, located in the same **config** folder. Find ***#config.i18n.default_locale = :de*** string and change its value to ***:en***.

![set default locale English](19-set-default-locale-english.png)

Don't forget to press the **Save** button in the panel above.

5\. After that find the ***defaults.yml*** file (still in the **config** folder). At the #142-144 lines (or about it) you can see the following lines:

```
 i_am_a_dummy: # Remove if you add an actual override
test:
 environment:
   url: 'http://localhost:9887/'
```

![dummy URL override](20-dummy-url-override.png)

Please, delete the line started with *i_am_a_dummy* string, and change an **url** parameter's value to the host url of your environment (it can be seen in the e-mail you've got earlier or by pressing the **Open in Browser** button next to your environment and copying URL in the address bar).

You should get something like following:

![URL override to environment](21-url-override-to-environment.png)

**Save** the changes.

6\. Finally, create new ***rake_deploy*** file in the **webroot** folder. Enter the following strings there:

```
db:create
db:schema:load
assets:precompile
```

![configure rake deploy](22-configure-rake-deploy.png)

7\. Press **Save** button one more time and **Restart** the Apache node in order to apply all the configurations you've made.

{{%tip%}}**Note:** The first restart of the server after applying new settings can take some time, please, be patient.{{%/tip%}}

![Apache restart button](23-apache-restart-button.png)

8\. Now you can press **Open in Browser** button for your environment and start working with your own Diaspora\* application hosted.

![Diaspora start page](24-diaspora-start-page.png)

Enjoy!


## What's next?

* [Setting Up Environment](/setting-up-environment/)
* [Database Hosting](/database-hosting/)
* [Redis Overview](/redis/)
* [Redmine](/redmine/)