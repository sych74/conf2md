---
draft: false
title: "NGINX Ruby"
aliases: "/nginx-ruby/"
seoindex: "index, follow"
seotitle: "NGINX Ruby"
seokeywords: "nginx, ruby, nginx ruby, nginx server, nginx application server, ruby passenger, ruby puma, ruby unicorn create nginx, add nginx ruby, create nginx ruby, ruby application server"
seodesc: "Find out about the Ruby applications hosting at the platform with the help of the NGINX server. Create a new NGINX Ruby application server and configure it up to your needs."
menu:
    docs:
        title: "NGINX Ruby"
        url: "/nginx-ruby/"
        weight: 30
        parent: "ruby"
        identifier: "nginx-ruby.md"
---

# NGINX Ruby

{{%tip%}}The *NGINX Ruby* stack is [HTTP/3](/http3/) ready with the feature support enabled by default since the *1.16.1* release for Ruby *2.4.9*, *2.5.7*, *2.6.5*, *2.7.0* versions and above. However, a [public IP address](/public-ip/) is required to bypass the Shared Load Balancer and work directly with the server over HTTP/3.{{%/tip%}}

**NGINX Ruby** software stack is a combination of the highly popular, open-source *NGINX* web server with the pre-installed *Ruby* programming language. This combination utilizes the *Passenger* application server by default, but the stack can be easily reconfigured to change the [ruby application server](/ruby-application-server-config/) (to either *Puma* or *Unicorn*).

NGINX Ruby is suitable for any Ruby application due to its scalability, security, reliability, and cost-efficiency. Creating this stack at the platform can be done in just a few clicks in a matter of minutes.

{{%tip%}}**Note:** This template utilizes a modern ***systemd*** initialization daemon.{{%/tip%}}

1\. Click the **New Environment** button at the top-left corner of the dashboard.

![new environment button](01-new-environment-button.png)

2\. Switch to the Ruby tab of the automatically opened topology wizard and choose **NGINX Ruby** as your application server. If needed, add any other stacks required for your environment.

![add NGINX Ruby application server](add-nginx-ruby-application-server.png)

Next, you can configure the [Ruby engine version](/ruby-versions/) and other parameters of the added stacks using the central part of the wizard (e.g. set [scaling limit](/automatic-vertical-scaling/), [nodes count](/horizontal-scaling/), attach [public IPs](/public-ip/), etc.). When ready, provide the desired environment name and click **Create**.

3\. In a minute, your environment will appear on the dashboard.

![environment with NGINX Ruby](environment-with-nginx-ruby.png)

Now, you can proceed to the deployment of your application to the NGINX Ruby serber.


## What's next?

* [Deployment Guide](/deployment-guide/)
* [Ruby App Server Configuration](/ruby-application-server-config/)
* [Ruby Dependency Management](/ruby-dependency-management/)
* [Ruby Post Deploy Configuration](/ruby-post-deploy-configuration/)