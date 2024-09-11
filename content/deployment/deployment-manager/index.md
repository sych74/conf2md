---
draft: false
title: "Deployment Manager"
aliases: ["/deployment-manager/", "/file-uploading/"]
seoindex: "index, follow"
seotitle: "Deployment Manager"
seokeywords: "deployment manager, paas deployment manager, archives deployment manager, application archives deployment manager, projects deployment manager, vcs projects deployment manager, store applications, manage projects, add project via url, upload application from local machine, add Git SVN project, deploy manager archive, deploy manager git svn, deploy manager vcs"
seodesc: "Learn about dashboard Deployment Manager to store, organize and easily deploy projects within your PaaS account. Upload your application archive from local machine or provide URL for download, add a project from remote Git / SVN repository."
menu: 
    docs:
        title: "Deployment Manager"
        url: "/deployment-manager/"
        weight: 20
        parent: "deployment"
        identifier: "deployment-manager.md"
---

# Deployment Manager
The **Deployment Manager** is located at the bottom of the dashboard and is used to store applications to simplify their subsequent deployment into your environments. There are two subsections to provide support for the following deployment types:

* ***[Archive](#archive)*** - stores the application packages, which can be uploaded from your local machine or any external link
* ***<a href="#vcs" id="archive">Git / SVN</a>*** - saves the link to your project within the remote Git / SVN repository and the appropriate access credentials (if needed)


## Application Archives

1\. The ***Archive*** tab within the Deployment Manager section allows to view all application archives stored at your account. The list provides the following information:

* **Name** - name of the uploaded archive
* **Comment** - custom note for your application
* **Size** - size of the application archive
* **Upload Date** - date of the archive addition to the Deployment Manager

![archive deployment manager](01-archive-deployment-manager.png)

2\. Click **Upload** and within the appeared dialog box provide the appropriate file either from your local machine (the *Local File* tab) or anywhere over the Internet (*URL*):
![upload archive to deployment manager](02-upload-archive-to-deployment-manager.png)
{{%note%}}**Note:** The maximum archive size for the local file upload is *150 MB*. If your application size exceeds this limit, please use the URL option.{{%/note%}}
Fill in the **Comment** field (if required) and **Upload**.

3\. In order to deploy an application from the archive, hover over the required file and click the appeared **Deploy to** button.
![deploy archive from deployment manager](03-deploy-archive-from-deployment-manager.png)

Within the opened frame you can [configure deployment](/deployment-guide#archive) up to your needs.

4\. The no longer required archives can be removed by selecting them with the appropriate checkboxes before the name and clicking the **Delete** button at the top panel.
![deployment manager delete archives](04-deployment-manager-delete-archives.png)

Now<a id="vcs"></a>, you know how the archive tab of the Deployment Manager works and can use it to organize your deployment packages.

## Git / SVN Projects

1\. The ***Git / SVN*** section of the Deployment Manager stores the link to the remote repository with your projects and, if required, the appropriate authentication credentials.
![git svn deployment manager](05-git-svn-deployment-manager.png)

2\. In order to add a new project, click the **Add Repo** button and fill in the fields of the appeared ***Add Repository*** window:

* **Name** - name of your application (no spaces and special symbols are allowed)
* choose the ***Git*** repo type
    * *URL* - the appropriate URL to the repository
    * *Branch* - the required branch of the project (*master* by default)
    * optionally, tick the *Use Authentication* check box and provide either *Password or Token* or *[SSH Key](/git-ssh)* based credentials
{{%note%}}**Note:** If your repository is protected with two-factor authentication, you need to use the appropriate access token (e.g. for [GitHub](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line) or [GitLab](https://docs.gitlab.com/ee/user/project/deploy_tokens/)) instead of your password.

![deployment authentication with git access token](05.1-deployment-authentication-with-git-access-token.png)

Additionally, you can manage the scope of provided permissions during the access token generation to ensure your repository safety.{{%/note%}}

* choose the ***SVN*** repo type
    * *URL* - link to your repository
    * *Login* and *Password* - authentication credentials (if required)

![add vcs repository to deployment manager](06-add-vcs-repository-to-deployment-manager.png)

You can just **Add** this project into Deployment Manager or **Add + Deploy** to immediately initiate [deployment](/deployment-guide#vcs) of this application.

3\. Hover over the Git / SVN project in Deployment Manager to access the **Deploy to**, **Edit** and **Delete** options.

![manage vcs repositories in deployment manager](07-manage-vcs-repositories-in-deployment-manager.png)

Now, you know how to manage your VCS projects within the platform Deployment Manager.


## What's next?
* [Deployment Guide](/deployment-guide/)
* [Deployment Hooks](/deployment-hooks/)
* [SSH Access to GIT Repository](/git-ssh/)
* [Git / SVN Auto-Deploy](/git-svn-auto-deploy/)