---
draft: false
title: "Python Versions"
aliases: "/python-versions/"
seoindex: "index, follow"
seotitle: "Python Versions"
seokeywords: "python versions, python engine, apache python, python engine versions, create python environment, change python version, switch between python versions, python container, choose python version, python container redeploy, python container update, python stack versions, python software stack versions"
seodesc: "Check the lists of the latest Python versions supported by the platform. Read the guide on how to select the Python version for the new environments and change it for existing Python instances."
menu:
    docs:
        title: "Python Versions"
        url: "/python-versions/"
        weight: 20
        parent: "python"
        identifier: "python-versions.md"
---

# Python Versions

The platform provides all the latest versions of the Python programming language and ensures a swift implementation of any further releases. The list of supported engine versions:

* *3.8.19*
* *3.9.19*
* *3.10.13*
* *3.11.8*
* *3.12.5*

{{%tip%}}The up-to-date list of the releases available on the platform is provided via the dedicated, regularly (weekly) updated [Software Stack Versions](/software-stacks-versions/#engines) document.{{%/tip%}}

These can be selected during a new [environment creation](#create-python-environment) and adjusted for [existing Python instances](#change-python-version).


## Create Python Environment

1\. Access the topology wizard by clicking the **New Environment** button at the top of the dashboard.

![create new environment button](01-create-new-environment-button.png)

2\. Navigate to the ***Python*** programming language tab, where the **Apache Python** application server is automatically selected, and choose the required engine version.

![topology wizard select Python version](02-topology-wizard-select-python-version.png)

Adjust any other settings (e.g. [cloudlets limits](/automatic-vertical-scaling/), [public IPs](/public-ip/), [region](/environment-regions/), etc.), provide environment name and click **Create**.


## Change Python Version

The version of the existing Python instances can be changed with the [container redeploy](/container-redeploy/) feature.

1\. The appropriate dialog can be accessed in the following ways:

* from the central part of the topology wizard (can be accessed with the **Change Environment Topology** button next to the appropriate environment)
![topology wizard redeploy Python nodes](03-topology-wizard-redeploy-python-nodes.png)

* using the **Redeploy container(s)** button next to the required node or layer
![redeploy containers button](04-redeploy-containers-button.png)

2\. Within the opened frame, you can adjust the following settings:

* **Tag** - select the needed Python engine version
* **Keep volumes data** - protect data in the volumes from erasing during redeploy
* **Simultaneous** or **Sequential deployment with delay** (for [scaled servers](/horizontal-scaling/) only) - choose whether all containers within a layer should be redeployed at once or one-by-one

![Python container redeployment frame](05-container-redeployment-frame.png)

Click **Redeploy** to proceed.

3\. Confirm an action via the appeared pop-up window.

![confirm Python container redeployment](06-confirm-python-container-redeployment.png)

That's it! In a minute the Python engine version of your container(s) will be updated.


## What's next?

* [Dashboard Guide](/dashboard-guide/)
* [Setting Up Environment](/setting-up-environment/)
* [Deployment Guide](/deployment-guide/)
* [Container Redeploy](/container-redeploy/)