---
draft: false
title: "Atlassian Confluence Clustering"
aliases: "/atlassian-confluence-cluster/"
seoindex: "index, follow"
seotitle: "Atlassian Confluence Clustering"
seokeywords: "confluence install, install atlassian confluence, confluence clustered environment, atlassian confluence cluster, confluence cluster, atlassian confluence hosting, software clustering, deploy confluence, confluence download, atlassian confluence app"
seodesc: "See the step-by-step tutorial on how to create the Atlassian Confluence cluster with a few automatically scaled application servers to increase the performance of your Confluence hosting."
menu: 
    docs:
        title: "Atlassian Confluence Clustering"
        url: "/atlassian-confluence-cluster/"
        identifier: "atlassian-confluence-cluster.md"
---

# Atlassian Confluence Clustering                                                                    

Let's create the **Atlassian Confluence** cluster with a few automatically scaled application servers. Using a cluster instead of a single server will increase the performance of your Confluence hosting through ability to serve much more requests simultaneously and provide some resiliency - if one node fails it won't cause the shutdown of other(s).
![atlassian confluence cluster cluster scheme](cluster-scheme.png)

To set your Atlassian Confluence cluster just follow the next detailed instruction.

* **<big><span type="A">Create a new environment</big>**</span>
    * Log in to the platform dashboard.
    * Click **Create environment** and set up a new environment within topology Wizard.
    * Pick up two **Tomcat 7** application servers and select **MySQL** (or PostgreSQL) database. Then specify the amount of resources for each of these nodes, enter the name for your environment and confirm its creation.
![atlassian confluence cluster confluence environment](confluence-environment.png)
Just in a minute your new environment will appear in the environment list.

* **<big><span type="A">Application Deployment</big>**</span>
    * Open the [Confluence web-site](https://www.atlassian.com/software/confluence/download) and download **Confluence x.x.x Cluster – EAR/WAR** .zip package. Preferably use 5.3 version (OnDemand release) or higher.
    * Extract the downloaded **Confluence** package. Build a new **.war** package with Confluence folder contents (just include it to a new **.zip** archive and change archive’s extension to **.war**).
    * As the size of the archive exceeds the **Deployment manager** upload restriction (150MB), you should upload the created archive to any file storage system. Copy the link to your uploaded package.
    * Navigate back to the dashboard, open the *URL* tab in the **Deployment manager** and enter the link you've just copied. Press the **Upload** button.
![atlassian confluence cluster upload confluence](upload-confluence.png)
    * When uploading is successfully finished, deploy the application to the environment you've created before. 
![atlassian confluence cluster confluence deploy](confluence-deploy.png)
    * Then press the **Config** button next to the Tomcat instances. In the opened **Configuration manager** navigate to the **Home** directory and create a new folder in it (named, for example, *data*).
![atlassian confluence cluster confluence configuration](confluence-configuration.png)
    * Now you should open the **confluence-init.properties** file, located in the ***webapps/ROOT/WEB-INF/classes/*** folder, and specify the path to the folder you've created in the previous step.
![atlassian confluence cluster confluence properties](confluence-properties.png)

* **<big><span type="A">Configuring database</big>**</span>
    * Click the **Open in browser** button next to the MySQL node and log in to the **phpMyAdmin** panel with the credentials you've received after environment creation.
    * Create a new user and database with the same names, for example, *confluence*.
![atlassian confluence cluster mysql with confluence](mysql-with-confluence.png)
    * Navigate back to the platform dashboard. Find your environment in the list and click **Config** button next to the Tomcat instances.
    * Open the **lib** folder and upload the MySQL connector there.
![atlassian confluence cluster mysql connector](mysql-connector.png)
    * Press the **Restart node** button next to the Tomcat to apply the performed settings.
    
* **<big><span type="A">Atlassian Confluence Cluster Installation</big>**</span>
    * Press the **Open in the browser** button for your environment. The Confluence setup wizard will be opened.
    * Specify the license key in the appropriate field and confirm the cluster installation.
![atlassian confluence cluster confluence license](confluence-license.png)
<i>**Note:** Don't try to enter the online generated key cause it doesn't fit for the cluster installation. You should buy the appropriate license for cluster or contact the Atlassian support in order to receive the Clustered Confluence Evaluation for testing.</i>
    * Specify the name of your cluster.
    * In the next window choose the direct **JDBC connection** to your database.
To fill in the **Database URL** field use the following format of the link to your database:  
*jdbc:mysql://mysql-{your_env_name}.{hoster_domain}/{db_name}?sessionVariables=  
storage_engine%3DInnoDB&useUnicode=true&characterEncoding=utf8*  
![atlassian confluence cluster install confluence](install-confluence.png)
    * Go through the remained **Load content** and **Configure user management** Confluence installation steps.
![atlassian confluence cluster confluence installation](confluence-installation.png)
    * Finally, you can log in and start working with your own clustered Confluence application.
![atlassian confluence cluster confluence cluster](confluence-cluster.png)

Enjoy! Hope this step-by-step instruction helped you.