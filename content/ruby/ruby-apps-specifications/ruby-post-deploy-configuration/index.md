---
draft: false
title: "Ruby Post Deploy Configuration"
aliases: ["/ruby-post-deploy-configuration/", "/ruby-post-deploy-conf/"]
seoindex: "index, follow"
seotitle: "Ruby Post Deploy"
seokeywords: "ruby rake, ruby post deploy, ruby post deploy configuration, rake deploy, ruby application configuration, rake commands"
seodesc: "The platform performs post-deployment configuration of the Ruby applications via rake. The list of needed commands is provided via the rake_deploy file at the application root."
menu: 
    docs:
        title: "Post Deploy Configuration"
        url: "/ruby-post-deploy-configuration/"
        weight: 2
        parent: "ruby-apps-specifications"
        identifier: "ruby-post-deploy-configuration.md"
---

# Ruby Post Deploy Configuration

The platform can perform post deployment application configuration via **rake**. This is usually needed to finalize configuration of complex applications, to run additional applications or specific steps for application configuration like db:migrate.

To do this we've introduced a new file called ***rake_deploy***. It is located in the application root and contains a list of the commands that have to be passed to **rake**. Each command has to be located in a separate line. Commands are executed successively.

The platform executes commands from ***rake_deploy*** with each restart of the apache/nginx service and deletes them right after successful execution. As a result, if you need to bypass different commands to rake on each deploy you need to create a ***rake_deploy*** file each time and put the correct commands there.

The platform puts the output of each ***rake_deploy*** into a corresponding log file which is available via the **[Log](/view-log-files/)** view in the platform dashboard.

***Syntaxis of the rake_deploy file:***

```
$COMMAND_NAME_1  
$COMMAND_NAME_2  
...  
$COMMAND_NAME_N
```

And the platform will execute the following scripts:

```
rake $COMMAND_NAME_1  
rake $COMMAND_NAME_2  
...  
rake $COMMAND_NAME_N
```

For example, **rake_deploy** looks like the following in the *[Redmine](/redmine/)* tutorial:

```
generate_secret_token  
db:migrate  
redmine:load_default_data
```

{{%note%}}**Note**: To freeze gems you need to add the ***gems:unpack*** command to *rake_deploy*.{{%/note%}}


## What's next?

* [Ruby Dev Center](/ruby-center/)
* [Dependency Management](/ruby-dependency-management/)
* [Ruby Application Server Configuration](/ruby-application-server-config/)