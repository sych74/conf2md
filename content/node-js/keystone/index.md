---
draft: false
title: "Keystone Deployment"
aliases: "/keystone/"
seoindex: "index, follow"
seotitle: "Keystone Deployment"
seokeywords: "keystone, keystonejs, keystone cms, keystone nodejs, install keystone, keystone deployment, keystone hosting, keystone paas, keystone tutorial, keystone guide"
seodesc: "Keystone is a model-driven CMS for Node.js build with MongoDB. Follow this guide to easily deploy your own Keystone instance at the platform."
menu:
    docs:
        title: "Keystone Deployment"
        url: "/keystone/"
        identifier: "keystone.md"
---

# How to Install Keystone

**Keystone** is the easiest way to build database-driven websites, applications and APIs in Node.js.

This application provides multiple awesome features. It is used for creation of dynamic web sites or applications with well-structured routes, templates and models. Keystone auto-creates a beautiful Admin UI, based on the database models you define, and enhances models with additional field types and functionality. And integration with different services provides even more features:

- Integration with Cloudinary for image uploading, storage and resizing
- Integration with Mandrill for sending emails easily
- Integration with Google Places for clever location fields
- Integration with Embedly for powerful video and rich media embedding tools

In this tutorial, we’ll describe how to easily host your Keystone project within the platform.


## Create Environment

1\. Log in to the platform and click the **New Environment** button in the upper left corner of the dashboard.

![create new environment button](01-create-new-environment-button.png)

2\. In the opened frame switch to the ***Node.js*** tab and choose **NodeJS** as your application server and **MongoDB** as a NoSQL database. Use the cloudlet sliders to allocate the required amount of resources for these nodes. Then type your environment name (e.g. *keystone*) and click the **Create** button.

![envirronment topology wizard](02-envirronment-topology-wizard.png)

Your environment will be created in a few minutes.


## Create Database

Create a new database for your Keystone application.

1\. Click the [WebSSH](/web-ssh-client/) icon next to the MongoDB instance and issue commands in the open terminal.

![MongoDB WebSSH button](03-mongodb-webssh-button.png)

2\. Log in the mongo database with user credentials you got upon installation:

```
mongo -u admin -p CYAacv61166 admin
```

![MongoDB log in](04-mongodb-log-in.png)

3\. The next command creates the database, e.g. ***keystonedb***.

```
use keystonedb
```

4\. Add a user for the newly created database with username, password, and role:

```
db.createUser({ user: "keystoneuser", pwd: "keystonepassword", roles: ["readWrite","dbAdmin"] })
```

![MongoDB create user](05-mongodb-create-user.png)

Now you have an empty DB and credentials to access it from your Keystone application.


## Run Keystone

1\. To start the application you need to access your environment via SSH protocol.

![NodeJS WebSSH button](06-nodejs-webssh-button.png)

2\. The easiest way to get started with Keystone is to use the [Yeoman](https://yeoman.io/learning/index.html) generator. Type the following commands in your terminal in order to install it:

```
sudo npm install -g yo
sudo npm install -g generator-keystone
```

3\. Once the installation is finished, let’s create a new directory for your project, for example, ***keystone-project*** in the **ROOT** folder and navigate inside it.

```
cd $ROOT_DIR
mkdir keystone-project
cd keystone-project
```

![create Keystone project directory](07-create-keystone-project-directory.png)

4\. Now it’s time to create a new project with the help of the embedded wizard. Type the next command:

```
yo keystone
```

Answer the appeared questions in order to include the preferred modules to your site and configure it:

![configure Keystone installation](08-configure-keystone-installation.png)

Wait until all the necessary packages are installed and your project is ready.

5\. Before you run your application, it should be connected to the previously created database. Therefore, open the ***.env*** file in the **keystone-project/my-site** folder using a built-in editor in [Configuration File Manager](/configuration-file-manager/).

![adjust .env configuration file](09-adjust-env-configuration-file.png)

Add the following line to it:

```
MONGO_URI=mongodb://{user}:{password}@{database_URL}:27017/{database_name}
```

Here should be substituted:

- ***{user}*** with *keystonedb* database username **keystoneuser** in our example
- ***{password}*** with respective password **keystonepassword** as for *keystoneuser*
- ***{database_URL}*** with the link to your DB server that can be found in the respective email
- ***{database_name}*** - with the name of the database you’ve created earlier the **keystonedb** as for our example.

So, the final connection string may look like as follows:

```
MONGO_URI=mongodb://kystoneuser:keystonepassword@node268626-keystone.vip.jelastic.cloud:27017/keystonedb
```

{{%note%}}**Note:** If you’ve added some modules to your site (like image gallery, etc.) ***.env*** file can contain some additional connection strings. DO NOT delete these settings, just add the specified line below them.{{%/note%}}

![add Mongo URI](10-add-mongo-uri.png)

6\. Now we are about to start as the main website of our Keystone application instead of the default one that comes with the platform Node.js certified template. To do that you have to replace the content of the **ROOT** directory with the content of our keystone project ***ROOT/keystone-project/my-site***. Issue the following commands in the terminal at the application server:

```
cd $ROOT_DIR  - goes to the /home/jelastic/ROOT directory
ls | grep -v keystone-project | xargs rm -rfv -  removes all of the files from the ROOT
mv keystone-project/my-site/{.[!.],}* .  - reallocates all content from keystone-project/my-site directory to the ROOT
ln -s keystone.js server.js - creates a symbolic link server.js to the keystone.js, since nodejs daemon runs servers.js by default
```

In order to run keystone on the port ***8080*** open ***keystone.js*** file in the dashboard editor and add the following line as follows:

```
'port': 8080,
```

![add port to keystone.js](11-add-port-to-keystonejs.png)

Press **Save** to apply the changes.

7\. Finally, restart the application server.

![NodeJS restart node](12-nodejs-restart-node.png)

8\. Run your project by means of clicking **Open in Browser** next to your *keystone* environment.

![environment open in browser](13-environment-open-in-browser.png)

Congratulations! Now you have a complete and ready-to-work site, with numerous awesome features available.

![Keystone application welcome page](14-keystone-application-welcome-page.png)

To sign in, use the email and password you have entered at the project creation step, as for our example:

![Keystone log in](15-keystone-log-in.png)

Enjoy the power of the Cloud with the platform!


## What's next?

* [Tutorials by Category](/tutorials-by-category/)
* [Node.js Tutorials](/nodejs-tutorials/)
* [Node.js Dev Center](/nodejs-center/)