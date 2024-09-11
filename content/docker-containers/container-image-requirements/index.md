---
draft: false
title: "Container Image Requirements"
aliases: ["container-image-requirements", "/supported-os-distributions/", "/docker-supported-distributions/", "/dockers-supported-distributions/"]
seoindex: "index, follow"
seotitle: "Container Image Requirements"
seokeywords: "container images, image requirements, containers os, container base distributions, supported os distributions, base images for containers, docker base images, container architecture"
seodesc: "The up-to-date list of container image requirements. See the list of image architectures and Linux distributions that are supported as a base operating system (OS) for containers at the platform."
menu:
    docs:
        title: "Container Image Requirements"
        url: "/container-image-requirements/"
        weight: 50
        parent: "docker-containers"
        identifier: "container-image-requirements.md"
---

# Container Image Requirements

Currently, the platform containers have the following requirements for the base image:

- [Supported OS Distributions](#supported-os-distributions)
- [Supported Architectures](#supported-architectures)


## Supported OS Distributions

The following Linux distributions are supported as a base of containers that could be deployed at the platform and properly handled by the system (this information is subject to change):

Distribution|Version|VZ Template
:---:|:---:|:---:
AlmaLinux|almalinux 9|almalinux-9-x86_64\*
Alpine|alpine 3|alpine-3.x-x86_64
CentOS|centos 7|centos-7-x86_64
CentOS|centos 8|almalinux-8-x86_64\*
Debian|debian 10|debian-10.0-x86_64
Debian|debian 11|debian-11.0-x86_64
Debian|debian 12|debian-12.0-x86_64\*
RHEL|RHEL 7|centos-7-x86_64
Ubuntu|ubuntu 18.04|ubuntu-18.04-x86_64
Ubuntu|ubuntu 20.04|ubuntu-20.04-x86_64
Ubuntu|ubuntu 22.04|ubuntu-22.04-x86_64
Ubuntu|ubuntu 23.04\*|ubuntu-22.04-x86_64

{{%note%}}**Notes:**

- Platform [hardware servers](https://www.virtuozzo.com/application-platform-ops-docs/hardware-requirements/) must support the **x86-64 v2 CPU instruction set** (or higher version).
- Containers based on the ***[Ubuntu 23](/release-notes-84/#ubuntu-23-support)*** OS template are supported since the *8.4.1* platform version.
- The ***[debian-12.0-x86_64](/release-notes-84/#debian-12-support)*** template is supported since the 8.4.1 platform version (kernel version *3.10.0-1160.90.1.vz7.200.7*, Virtuozzo Hybrid Server 7.5 Update 5 Hotfix 1).
- The ***[almalinux-8-x86_64](/release-notes-824/#almalinux-8-os-support)*** template is supported since the 8.2.4 platform version (kernel version *3.10.0-1160.80.1.vz7.191.4*).
- The ***[almalinux-9-x86_64](/release-notes-83/#almalinux-9-base-os-image)*** template is supported since the 8.3.1 platform version (kernel version *3.10.0-1160.80.1.vz7.191.4*).
{{%/note%}}

In order to run containers of another type, please, [contact us](https://www.virtuozzo.com/company/contact/) to negotiate the appropriate OS support.


## Supported Architectures

Currently, only ***amd64*** image architecture is supported for [custom container deployment](/custom-containers-deployment/) (and [redeployment](/container-redeploy/)).


## What's next?

* [Container Types](/container-types/)
* [Custom Containers Deployment](/custom-containers-deployment/)
* [Container Redeploy](/container-redeploy/)
* [Building Custom Container](/building-custom-container/)