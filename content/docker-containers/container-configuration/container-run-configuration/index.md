---
draft: false
title: "Run Configuration"
aliases: ["/container-run-configuration/", "/docker-run/"]
seoindex: "index, follow"
seotitle: "Container Run Configuration"
seokeywords: "run configuration, container run configuration, run container, run options, container run options, container run command, configure run container, entry point container, run command for containers, how to run container, start container, execute container, container entry point"
seodesc: "In order to set the startup options for your container to be run with, access the embedded container configuration wizard and specify the desired values within the Entry Point and Run Command fields."
menu: 
    docs:
        title: "Run Configuration"
        url: "/container-run-configuration/"
        weight: 60
        parent: "container-configuration"
        identifier: "container-run-configuration.md"
---

# Run Configuration
The last **CMD / Entry Point** tab contains two input fields, where you can set the run options for your container: 

* ***Entry Point*** - configures a command to be executed during container launch
* ***Run Command*** - sets defaults for container launch
    * *if no entry point is specified* - a command to be run
    * *if entry point is provided* - additional parameter(s) for the command

![cmd entrypoint layer settings](01-cmd-entrypoint-layer-settings.png)

Using the reverse arrow button, which appears upon entering some custom string inside any of these fields, the specified run options can be easily **Reset to default** values.
{{%tip%}}**Note:** If neither run command is declared within the template settings by default, you have to set the appropriate option(s) using this frame. Otherwise, no application/service will be started at the container launch.{{%/tip%}}


## What's next?

* [Container Configuration](/container-configuration/)
* [Variables](/container-variables/)
* [Links](/container-links/)
* [Volumes](/container-volumes/)
* [Ports](/container-ports/)