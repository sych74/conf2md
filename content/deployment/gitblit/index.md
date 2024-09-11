---
draft: false
title: "Deploying Apps via Gitblit"
aliases: "/gitblit/"
seoindex: "index, follow"
seotitle: "Deploying Apps via Gitblit"
seokeywords: "gitblit, version control system, git tool, git repository tool, gitblit create, new repo gitblit, host projet gitblit, gitblit vcs, deploy from gitblit, git project host, git project build"
seodesc: "Find out how to create a repository at Gitblit - tool, used for managing, viewing and serving your Git repositories - and deploy an app from it into the platform."
menu: 
    docs:
        title: "Deploying Apps via Gitblit"
        url: "/gitblit/"
        weight: 60
        parent: "deployment"
        identifier: "gitblit.md"
---

# Storing and Deploying Apps via Gitblit

{{%imageLeft%}}![](00logo-1.png){{%/imageLeft%}}
[Gitblit](http://gitblit.com/) is one of the most popular tools for managing, viewing and serving your repositories within Git - a widely spread VCS (version control system) for software elaboration. Mainly, Gitblit is designed for small workgroups, which work with centralized repositories, and supports the variety of remarkable features, such as access control, repository's content displayment via web, multiple repositories management, ability to be integrated with other Git-management solutions etc.

So, let's find out how to host Gitblit at the platform and, subsequently, simplify your apps management with its help. You can automatically get a preconfigured ready-to-work **Gitblit** instance up and running within minutes using our one-click installation widget:

<div style="text-align: justify; margin: 2px;" data-app="gitblit" data-width="280" data-theme="modern" data-text="Get it hosted now!" data-tx-empty="Type your email and click the button" data-tx-invalid-email="Invalid email, please check the spelling" data-tx-error="An error has occurred, please try again later" data-tx-success="Check your email" class="je-app">
</div>

Just click **Get it hosted now** and type your email address in order to launch Gitblit and get the ability to proceed directly to the [repository creation](#create-repository) guide section, skipping the steps of manual installation.
{{%tip%}}
The full list of applications, available for one-click installation, can be found at our [Marketplace page](https://www.virtuozzo.com/application-platform/marketplace/) or within the [corresponding](/marketplace/) section at the dashboard.
{{%/tip%}}

Or, if your prefer to take the complete control over the process, you can deploy it manually by following the step-by-step instruction below.

## Create an Environment

1\. Log in to the platform dashboard with your credentials and click the **New Environment** button to open the **Environment Wizard** frame.
![gitblit 01create1](01create1.png)

2\. Choose the ***Java*** language tab and select **Tomcat 7** as an application server.
![gitblit 02env create 1](02env_create-1.png)

Set the rest of configurations according to your requirements, name your environment (*e.g. gitblit*) and click **Create** to initiate the process.

After a while, the designated environment will appear at the dashboard.
![gitblit 03created var2](03created-var2.png)


## Deploy Gitblit

1\. Now, navigate to the [Gitblit](http://gitblit.com) official website and download its latest release in a view of a wrapped ***.war*** archive (the appropriate link is circled on the image below).
![gitblit 04site](04site.png)

2\. Go back to the platform dashboard and use the **Deployment Manager** to upload the archive you've just downloaded - i.e. choose the **Local file** tab, click **Browse** and select the Gitblit *.war* file within your local machine.
![gitblit 05upload](05upload.png)
Click on the **Upload** button to proceed.

3\. After the package appears at manager, deploy it to your environment using the corresponding **Deploy to** option.
![gitblit 06deploy](06deploy.png)
Within the opened frame, you may specify the desired custom context within the input field or just leave it blank to deploy your application to the default ***ROOT*** context.

4\. Once the process is completed, you can click the **Open in browser** button to ensure the application is actually working fine.
<a id="create-repository"></a>![gitblit 07OiB var2](07OiB-var2.png)


## Create a Gitblit Repository

1\. To start working with Gitblit, you need to **login** within its main page with the default *admin/admin* credentials
{{%tip%}}**Tip:** We recommend to change the password to your custom one as soon as possible for the security ensurance{{%/tip%}}
![gitblit 08login var2](08login-var2.png)

2\. Once inside, switch to the **repositories** tab at the top pane. Here, you will see the list of your repos (if there are any) and will have the ability to manage them.
![gitblit 09create repo 1](09create_repo-1.png)
Let's create a **new repository** by clicking the same-named button to the right.

3\. Set the name for your new repo (for example, *GitBlitRepo*) are adjust all the rest configurations according to your preferences (or just leave the default values).
![gitblit 10new repo](10new_repo.png)
Click **create** at the bottom of a page when ready.

4\. The specified empty repository will be shown in a moment.
![gitblit 11empty repo](11empty_repo.png)

5\. Now you should push (add) your project to this repo. The simple steps below will help you with this:

* first, initialize your local repository (i.e. create a folder to store your projects' files locally):
    ```bash
    git init
    ```
* define the files your project should consists of (just as an example, we'll add the ***README*** file to it)
    ```bash
    git add README.md
    ```
* save these changes at the local repo with a commit message (e.g. mark it as a *first commit*)
    ```bash
    git commit -m "first commit"
    ```
* specify the previously created **GitBlit** repository as a remote one for your local Git repo
    ```bash
    git remote add  {name}  {repo_url}
    ```
    where:
    * ***{name}*** - appellation for your remote repository
    * ***{repo_url}*** - link to your GItblit repository, which can be found within the drop-down list on the top of the page from the previous step. The appropriate *http://* link can be copied with the button to the right, as it is shown below:
![gitblit 12copy url 1](12copy_url-1.png)

* finally, push your local project to the **Gitblit** repository:
    ```bash
    git push -u  {name}  {branch}
    ```
    where:
    * ***{name}*** - name of the remote Gitblit repository your project should be copied to (state it the same as above)
    * ***{branch}*** - projects' branch, that should be updated with this new data
![gitblit 12pushed file](12pushed_file.png)

After this is done, refresh the Gitblit page to view your repository with a full data on it (here, you can also switch to the **commits** section to see the information on the latter changes applied, such as author, time and date of a commit, list of changed files, etc.).

## Deploy Project via Gitblit

Now, let's discover how to deploy your project from a Gitblit repository into the platform.

1\. At first, create a separate environment for your application hosting. Let's consider a case with a **Java** project, where, in addition to the application server node, you'll need to use a build tool (i.e. *Maven*).
![gitblit 13env maven 3](13env_maven-3.png)
{{%tip%}}**Note:** that the extra Maven node is required for Java projects only, while for the rest of engines build is performed automatically, while adding a project to application server.
Refer to the appropriate document below in case you need details on how to accomplish this:  

* [Maven for Deploy via Git/SVN](/java-vcs-deployment/)
* [Deploy PHP Projects via Git/SVN](/php-git-svn)
* [Deploy Ruby Project via Git/SVN](/ruby-git-svn)
* [Deploy Python Projects via Git/SVN](/python-git-svn)
* [Deploy Node.js Project via Git/SVN](/nodejs-git-svn){{%/tip%}}

2\. Click the **Add project** button next to the *Maven* node after your environment is successfully created
![gitblit 14add project maven 2](14add_project_maven-2.png)

3\. In the appeared ***Add project*** frame, choose the **Git** tab and fill in the required fields:

* enter the ***Name*** of project (for Maven only)
* specify ***URL*** and ***Branch*** of the repository you've previously created
* in the ***Use authentication*** block, fill in the following fields:
    * ***Login*** used to enter your repo
    * ***Password*** for the above specified login
* choose your ***Environment*** Name from the drop-down menu
* type the ***Context*** you would like to deploy your project to
![gitblit 15add project 2](15add_project-2.png)
Confirm the project addition with the **Add** button.

4\. Next, click the **Build and deploy** option next to the just added project.
![gitblit 16BaD var4](16BaD-var4.png)

5\. Once your application is deployed, you can open it (by pressing the **Open in browser** button for the environment) and ensure everything works fine.
![gitblit 17deployed var4](17deployed-var4.png)
{{%tip%}}**Tip:** Subsequently, all the newly performed at the remote repository changes can be easily applied to your hosted app with just a single click - simply select the same **Build and deploy** button (or **Update from GIT** in case of working with another engine) next to your project and wait for the redeployment to be completed.{{%/tip%}}
That's it! Now, your own Gitblit repository and project within it are both hosted hand by hand at the platform. Enjoy!


## What's next?
* [Maven for Deploy via Git/SVN](/java-vcs-deployment/)
* [Deploy PHP Projects via Git/SVN](/php-git-svn/)
* [Deploy Ruby Project via Git/SVN](/ruby-git-svn/)
* [Deploy Python Projects via Git/SVN](/python-git-svn/)
* [Deploy Node.js Project via Git/SVN](/nodejs-git-svn/)
* [Application Configuration](/application-configuration/)

<script>
    (function(d, s, id) {
        var js, fjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.async = true;
        js.src = "//go.jelastic.com/widgets.js";
        fjs.parentNode.insertBefore(js, fjs);
    }(document, 'script', 'jelastic-jssdk'));
</script>
