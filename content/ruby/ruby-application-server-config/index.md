---
draft: false
title: "Ruby App Server Configuration"
aliases: "/ruby-application-server-config/"
seoindex: "index, follow"
seotitle: "Ruby Server Configuration"
seokeywords: "apache ruby, nginx ruby, apache passenger, apache passenger module, nginx passenger, nginx puma, nginx unicorn, ruby passenger, ruby puma, ruby unicorn, nginx passenger module, nginx puma module, nginx unicorn module, change ruby sever, configure application server, switch ruby application server, ruby server configuration, ruby application server configuration, nginx application server modules"
seodesc: "The platform Apache and NGINX Ruby software stacks are provided with the Passenger application server by default. Herewith, NGINX Ruby can be additionally configured to use Puma and Unicorn inbuilt application servers."
menu: 
    docs:
        title: "Ruby App Server Configuration"
        url: "/ruby-application-server-config/"
        weight: 40
        parent: "ruby"
        identifier: "ruby-application-server-config.md"
---

# Ruby Application Server Configuration

The platform provides Ruby application servers based on the two software stacks:

* **Apache Ruby**
* **NGINX Ruby**

Herewith, both ones are configured to utilize the **Passenger** application server by default, which is integrated via the appropriate custom module. Moreover, if needed, the *NGINX Ruby* stack can be easily configured to work with the different inbuilt servers:

* ***[Passenger](https://www.phusionpassenger.com/)*** - one of the most feature rich application servers for Ruby, which are invaluable for the modern web apps and microservice APIs
* ***[Puma](http://puma.io/)*** - a Ruby web server oriented on speed and parallelism due to fast and accurate HTTP 1.1 protocol parsing
* ***[Unicorn](https://bogomips.org/unicorn/)*** - an HTTP server, which takes advantage of the Unix/Unix-like kernels features for serving fast clients on low-latency, high-bandwidth connections

Let's see how it can be switched on the NGINX Ruby server.

## NGINX Application Server Modules
The **Passenger** module is used for all newly created Ruby environments by default. Follow the next steps to change to the different one:

1\. Click the **Config** button next to your *NGINX Ruby* application server.
![nginx ruby server config button](01-nginx-ruby-server-config-button.png)

2\. Within the opened [configuration file manager](/configuration-file-manager) panel, navigate to the **/etc/nginx/<i>nginx.conf**</i> file. Find the ***include app_servers*** strings:

* *include app_servers/nginx-unicorn.conf*
* *include app_servers/nginx-puma.conf*
* *include app_servers/nginx-passenger.conf*
![nginxconf include application server modules](02-nginxconf-include-application-server-modules.png)

3\. Uncomment the string with the required module and comment the previously active one.
{{%note%}}**Note:** Only <u>*one*</u> string for the application server module should be active, otherwise you'll get the compatibility errors.{{%/note%}}
![adjust nginx ruby application server settings](03-adjust-nginx-ruby-application-server-settings.png)
For example, we'll switch to ***Puma***.

4\. **Save** the changes and **Restart Nodes** of the NGINX application server to apply them.
![nginx ruby server restart nodes](04-nginx-ruby-server-restart-nodes.png)

5\. Access your node via SSH (e.g. using [Web SHH](/web-ssh-client)) and run the selected module with the appropriate command executed from the project directory:
```bash
cd /var/www/webroot/ROOT/
pumactl -F config/puma.rb --pidfile puma.pid -S puma.state start &
```
{{%tip%}}**Note:** For the ***Unicorn*** application server run the ***unicorn_rails -c config/unicorn.rb -D &*** command instead.{{%/tip%}}
![nginx ruby start puma application server via ssh](05--nginx-ruby-start-puma-application-server-via-ssh.png)

{{%note%}}**Note:** If you would like to switch to the different module, it could be done in the same way, but you need to stop the currently running application server:

* *for Puma:* ***pumactl -F config/puma.rb --pidfile puma.pid -S puma.state stop***
* *for Unicorn:* ***ps aux | grep 'unicorn' | awk '{print $2}' | xargs kill -QUIT***
{{%/note%}}
That's all! Now you can work with the chosen Ruby NGINX module.


## What's next?
* [Deployment Guide](/deployment-guide/)
* [Configuration File Manager](/configuration-file-manager/)
* [Ruby Dependency Management](/ruby-dependency-management/)
* [Ruby Post Deploy Configuration](/ruby-post-deploy-configuration/)