---
draft: false
title: "Ruby Dependency Management"
aliases: "/ruby-dependency-management/"
seoindex: "index, follow"
seotitle: "Ruby Dependency Management"
seokeywords: "dependency management, ruby dependency management, dependency manager, ruby bundler, ruby gem management, gemfile dependencies, ruby gemfile, ruby gems dependencies"
seodesc: "Learn about dependency management in Ruby application servers at the platform. Check out the specifics of the Bundler integration and gems management via Gemfile."
menu: 
    docs:
        title: "Dependency Management"
        url: "/ruby-dependency-management/"
        weight: 1
        parent: "ruby-apps-specifications"
        identifier: "ruby-dependency-management.md"
---

# Ruby Dependency Management

All Ruby-based application servers (*Apache* and *NGINX*) are provided with the **[Bundler](https://bundler.io/)** dependency manager by default. It automatically tracks and installs dependencies required by your application. You only need to specify the list of required gems in ***[Gemfile](https://bundler.io/gemfile.html)***, which will resolve all dependencies.

Bundler performs dependency resolving in the following cases:

- [deploying applications](/deployment-guide/)
- [switching between Ruby versions](/container-redeploy/)
- [changing deployment type](/ruby-center/#ruby-application-deployment)

After any of the actions mentioned above, Bundler searches [RubyGems.org](https://rubygems.org/) (Ruby community's gem hosting service) for dependencies listed in the config file and, if needed, installs them. By default, Ruby application servers are provided only with gems required for the example application's work.

![Ruby Gemfile dependencies](01-ruby-gemfile-dependencies.png)

***Gemfile*** supports a non-strict version declaration (e.g. greater than specified version, *"jquery-rails", "~> 2.0.2"*). In such a case, the Bundler will download and install the latest version of the corresponding gem on each dependency resolving action.

Also, if your application uses any special (non-public) dependencies, you need to specify their repository URL in Gemfile. In such a way, Bundler will be able to download and install these gems.

{{%note%}}**Note:** When [redeploying](/container-redeploy/) a Ruby environment, ensure that a new engine version is correctly covered in the Gemfile. Otherwise, you'll get a discrepancy error after the process.

We recommend using a non-strict Ruby version declaration in your ***Gemfile***, for example ***ruby "~> 2.6.0"***. Such a flexible form prevents you from  interrupting your deployment or CI process while being able to upgrade your Ruby version.{{%/note%}}


## What's next?

* [Configuration File Manager](/configuration-file-manager/)
* [Ruby App Server Configuration](/ruby-application-server-config/)
* [Post Deploy Configuration](/ruby-post-deploy-configuration/)