---
draft: false
aliases: "/ruby-center/"
seoindex: "index, follow"
seotitle: "Ruby Dev Center"
seokeywords: "ruby, ruby paas, ruby cloud, ruby hosting, ruby application, ruby hosting specifics, ruby versions, ruby application server, ruby application deployment, ruby domain management, ruby scaling, ruby automatic scaling, ruby dependency management, ruby post deploy configuration"
seodesc: "Out-of-box Ruby web servers, management and automatization tools for efficient hosting and easy Ruby application deployment within the platform."
menu:
    docs:
        title: "Ruby Dev Center"
        url: "/ruby-center/"
        weight: 10
        parent: "ruby"
        identifier: "ruby-center.md"
---

# Ruby PaaS Hosting

{{%imageLeft%}}<img src="01-ruby-cloud-hosting.png" alt="Ruby cloud hosting" width="200"/>{{%/imageLeft%}}

**Ruby** is a popular, open source programming language with a powerful and practical, yet natural and easy to read/write syntax. Ruby combines the best practices from various solutions to provide a unique object-oriented language, which aims for simplicity and provides such features as basic & special object-oriented features; operator overloading; exception handling; iterators and closures; garbage collection, and more.

The platform provides an out-of-box integration of the Ruby web servers, providing all the management and automatization tools (e.g. *Ruby on Rails* web-development framework) for comfortable hosting and maximally convenient Ruby application development.

In this article, we’ll go through the distinctive features of the [Ruby](https://www.ruby-lang.org/en/) hosting and introduce the Ruby-related possibilities within the platform. Use the table of content below to find required information within the guide quicker:

- [Ruby Environment Hosting](#ruby-environment-hosting)
  - [Ruby Application Servers](#ruby-application-servers)
  - [Ruby Versioning](#ruby-versioning)
- [Ruby Application Deployment](#ruby-application-deployment)
- [Ruby Dependency Management](#ruby-dependency-management)
- [Ruby Post Deploy Configuration](#ruby-post-deploy-configuration)
- [Domains Management](#domains-management)
- [Automatic Vertical Scaling](#automatic-vertical-scaling)
- [Manual Horizontal Scaling](#manual-horizontal-scaling)
- [Automatic Horizontal Scaling](#automatic-horizontal-scaling)


## Ruby Environment Hosting

The platform provides a powerful and intuitive topology wizard to [set up](/setting-up-environment/) the hosting of a new environment.

Switch to the *Ruby* language tab, select the required application server and engine version, add any other [software stack](/software-stacks-versions/) required. If needed, adjust other parameters, such as cloudlets (RAM and CPU), disk space, public IPv4/IPv6, node count, etc.

{{%tip%}}**Note:** Both *Apache Ruby* and *NGINX Ruby* templates utilize a modern ***systemd*** initialization daemon.{{%/tip%}}

![Ruby topology wizard](02-ruby-topology-wizard.png)

{{%tip%}}**Note:** All instances are [completely isolated](/isolated-containers/) and fully independent containers. Additionally, scaled out nodes are automatically distributed across the physical servers (or VMs), ensuring [high availability](/isolated-containers/#high-availability-for-applications).{{%/tip%}}

### Ruby Application Servers

The platform provides [Ruby application servers](/ruby-application-server-config/) based on the *Apache* and *NGINX* software stacks. Both ones are configured to utilize the *Ruby on Rails* framework for implementing web applications and the **Passenger** application server by default. 

If needed, the *NGINX Ruby* stack can be easily configured to work with different inbuilt servers:

- ***[Passenger](https://www.phusionpassenger.com/)*** - one of the most feature-rich application servers for Ruby, which are invaluable for the modern web apps and microservice APIs
- ***[Puma](https://puma.io/)*** - a Ruby web server oriented on speed and parallelism due to fast and accurate HTTP 1.1 protocol parsing
- ***[Unicorn](https://bogomips.org/unicorn/)*** - an HTTP server, which takes advantage of the Unix/Unix-like kernels features for serving fast clients on low-latency, high-bandwidth connections

### Ruby Versioning

The following Ruby versions are supported at the time of this writing:

- 3.0.6
- 3.1.6
- 3.2.5
- 3.3.4

{{%tip%}}The up-to-date list of the releases available on the platform is provided via the dedicated, regularly (weekly) updated [Software Stack Versions](/software-stacks-versions/#engines) document.{{%/tip%}}

You can select the required [version of Ruby](/ruby-versions/) via the topology wizard during the creation of a new environment, as well as adjust it for the existing instances via [container redeployment](/container-redeploy/).


## Ruby Application Deployment

The platform automates the deployment process for the managed *Apache Ruby* and *NGINX Ruby* application servers using:

* application ***archive*** uploaded from the local machine or via external URL
* remote ***VCS*** repository (e.g. GitHub)

![uby application deployment ](03-ruby-application-deployment.png)

When deploying a Ruby application, only a single context (*ROOT*) can be used. However, you can select from three *Deployment Types* (i.e. [RAILS_ENV](https://guides.rubyonrails.org/configuring.html#rails-environment-settings)) for it:

- ***development*** - reloads all application classes and turns off caching (allows a faster development cycle)
- ***production*** - turns on all caching
- ***test*** - wipes out database between test runs

If needed, you can switch between the Ruby deployment types via the appropriate drop-down list next to your application (see the image below).

![Ruby deployment types](04-ruby-deployment-types.png)

Read the related documents to learn more about the deployment of the Ruby applications:

- [Deployment Manager](/deployment-manager/)
- [Deployment Guide](/deployment-guide/)
- [Auto-Deploy Overview](/git-svn-auto-deploy/)
- [Deployment Hooks](/deployment-hooks/)


## Ruby Dependency Management

All Ruby instances within the platform are provided with the ***[Bundler](https://bundler.io/)*** dependency manager for automatic tracking and installing the exact gems and versions, which your project requires. If the project has a *Gemfile* file in the root folder, it will automatically resolve dependencies with Bundler after deployment to the server without you having to perform any manual intervention.

Also, if needed, you can include any Ruby framework into your Gemfile (*Sinatra*, *Rack*, *therubyracer*, *Ramaze*, etc.) or utilize ***[Ruby on Rails](https://rubyonrails.org/)*** - one of the most popular frameworks for developing and implementing web applications, which is available by default.

Refer to the [Ruby Dependency Management](/ruby-dependency-management/) documentation for additional information.


## Ruby Post Deploy Configuration

In order to automate the repetitive actions that Ruby projects need to perform after the application is deployed (e.g. *db:migrate*), a ***rake_deploy*** file (located in the root folder of the project) can be created.

The file should contain a list of commands (each one from a new line) that will be executed consecutively via the ***[rake](https://ruby.github.io/rake/)*** tool after each restart of the Apache/NGINX node. After successful execution, the ***rake_deploy*** file is automatically removed. Refer to the [Ruby Post Deploy Configuration](/ruby-post-deploy-configuration/) documentation for additional information.


## Domains Management

You can provide a [custom domain](/custom-domains/) name for your Ruby application to be used instead of the default one. Based on the environment topology, you should use:

* **CNAME redirect** if using *Shared Load Balancer*; is recommended for ***dev*** and ***test*** environments
* **DNS A Record** if using *public IP*; can handle high traffic load and is suitable for ***production*** environments

To switch traffic from one environment to another (e.g. to redirect customers to the newer application version without downtime), the [swap domains](/swap-domains/) functionality should be used. It is also available as the ***SwapExtIps*** [API](https://docs.jelastic.com/api/#!/api/environment.Binder-method-SwapExtIps)/[CLI](/cli-ip-swap/) method.

![Ruby domain management](05-ruby-domain-management.png)


## Automatic Vertical Scaling

One of the key-features of the platform is dynamic provisioning of the exact amount of resources (RAM and CPU) required by your nodes according to the current load with no manual intervention. Just set the required [cloudlets](/cloudlet/) limit (*128 MiB* of RAM and *400 MHz* of CPU each) for your Ruby application server and everything else will be handled by the platform automatically.

![Ruby automatic vertical scaling](06-ruby-automatic-vertical-scaling.png)

As a result, you automatically benefit on a truly user-oriented ***[Pay-per-Use](/pricing-model/)*** charging approach and don’t need to guess or predict the incoming load. It ensures that you [never overpay for unused resources](https://www.virtuozzo.com/company/blog/deceptive-cloud-efficiency-do-you-really-pay-as-you-use/) and save your time because the platform eliminates the need to handle the load-related adjustments or perform architectural changes manually.

![Ruby pay-per-use pricing](07-ruby-pay-per-use-pricing.png)

Refer to the [automatic vertical scaling](/automatic-vertical-scaling/) documentation for additional information.


## Manual Horizontal Scaling

[Horizontal scaling](/horizontal-scaling/) with the platform is as simple as selecting the required number of nodes via the corresponding section in the topology wizard. Additionally, you can choose between two scaling modes:

* ***Stateless*** - simultaneously creates all new nodes from the base image template
* ***Stateful*** - sequentially copies file system of the master container into the new nodes

![Ruby horizontal scaling](08-ruby-horizontal-scaling.png)

{{%tip%}}**Note:** For the proper distribution of requests, a [load balancer](/load-balancing/) instance is automatically added upon Ruby server scaling.{{%/tip%}}

The maximum number of the same-type servers within a single environment layer depends on a particular hosting provider settings (usually this limit stands for 16 nodes and can be enlarged by sending the appropriate request to support).


## Automatic Horizontal Scaling

You can configure [automatic horizontal scaling](/automatic-horizontal-scaling/) for your Ruby environment through tunable triggers, which monitor the changes in the nodes load and increase/decrease their number appropriately.

The process is simple, access the environment **Settings > Monitoring > Auto Horizontal Scaling** section, choose the required layer and resource to be monitored (*CPU*, *RAM*, *Network*, *Disk I/O*, *Disk IOPS*). Set the exact condition and specifics of scaling via the intuitive UI form.

![Ruby automatic horizontal scaling](09-ruby-automatic-horizontal-scaling.png)

In addition, hosting at the PaaS allows using other built-in tools and features, for example:

- [Built-in](/built-in-ssl/) or [Custom SSL](/custom-ssl/)
- [Public IPv4 and IPv6](/public-ip/)
- A wide range of complementary [software stacks](/software-stacks-versions/), including SQL and NoSQL databases
- [Container firewalls](/custom-firewall/), [endpoints](/endpoints/) and [environment network isolation](/environment-isolation/)
- [User-friendly UI](/dashboard-guide/) and [SSH access](/ssh-access/)
- [Open API](/api-overview/) and [Cloud Scripting](https://docs.cloudscripting.com/) for automation
- [Pay-per-use pricing model](/pricing-model/)
- [Collaboration for teamwork](/account-collaboration/)
- [Multi-cloud distribution](/environment-regions/)

Explore Ruby hosting benefits within the platform!


## What's next?

* [Setting Up Environment](/setting-up-environment/)
* [Dashboard Guide](/dashboard-guide/)
* [Deployment Guide](/deployment-guide/)
* [SSH Access](/ssh-access/)