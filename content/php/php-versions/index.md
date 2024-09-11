---
draft: false
title: "PHP Versions"
aliases: "/php-versions/"
seoindex: "index, follow"
seotitle: "PHP Versions"
seokeywords: "php, apache, nginx, php environment, apache php, nginx php, php application, php versions"
seodesc: "List of supported PHP versions. With the platform, you have a possibility to switch between PHP versions."
menu:
    docs:
        title: "PHP Versions"
        url: "/php-versions/"
        weight: 20
        parent: "php"
        identifier: "php-versions.md"
---

# PHP Versions

Within the confines of PHP hosting at the platform, the following PHP engine versions are supported:

* *PHP 8.0.30*
* *PHP 8.1.29*
* *PHP 8.2.23*
* *PHP 8.3.11*

{{%tip%}}The up-to-date list of the releases available on the platform is provided via the dedicated, regularly (weekly) updated [Software Stack Versions](/software-stacks-versions/#engines) document.{{%/tip%}}

You can choose the version you need while environment creation and easily [switch between them](#switch) afterwards via topology wizard. The workflow is the following:

1\. Click the **New Environment** button at the top dashboard pane to open the *Environment Wizard* frame.

![new environment](01-new-environment.png)

2\. Navigate to the ***PHP*** language tab and pick the preferred application server. Choose the desired engine version by means of the second drop-down list in the central pane.

![PHP environment wizard](02-php-environment-wizard.png)

Specify the resource limits, select the preferred [region](/environment-regions/), type your environment name (or leave the default one) and click the **Create** button.

{{%tip%}}**Tip:** For more information on PHP hosting specifics at the platform and the possibilities it provides, refer to the [PHP Developer's Center](/php-center/) document.{{%/tip%}}

3\. In order to change the version of PHP for the already existing environment, click the **Redeploy containers** icon next to the appropriate layer.

![PHP redeploy button](03-php-redeploy-button.png)

4\. Select required engine version within the *Tag* list of the opened frame.

![PHP redeploy dialog](04-php-redeploy-dialog.png)

Click **Redeploy** to confirm the changes.

{{%note%}}**Note:** In case of switching the engine version to PHP 7 for legacy PHP containers, you may require to manually [re-define](/php-extensions/#activate-extension) the included PHP modules, as part of them was turned into dynamic (i.e. to be activated only upon the necessity) in confines of the [PaaS 4.3](/release-notes-43/#php-modules-list-refactoringnbsp43--44) release.{{%/note%}}


## What's next?

* [Software Stack Versions](/software-stacks-versions/)
* [Deployment Guide](/deployment-guide/)
* [PHP App Server Configuration](/php-application-server-config/)
* [PHP Tutorials](/php-tutorials/)