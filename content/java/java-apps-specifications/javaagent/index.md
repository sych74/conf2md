---
draft: false
title: "Java Agent"
aliases: "/javaagent/"
seoindex: "index, follow"
seotitle: "Java Agent"
seokeywords: "java agent, java agent integration, jvm, configure java agent, enable java agent, java agent paas, java agent variable, jvm arguments, java interceptor, javaagent parameter, java agent jar"
seodesc: "See the instruction on how to configure certified Java containers in the platform to enable a custom Java agent - an interceptor applet launched at the JVM startup to support agent-based applications."
menu: 
    docs:
        title: "Java Agent"
        url: "/javaagent/"
        weight: 2
        parent: "java-apps-specifications"
        identifier: "javaagent.md"
---

# Java Agent Integration

**Java agent** is an interceptor in front of the application's main method. Generally, it is a .jar package statically loaded in the *PreMain-Class* method, which implements a mechanism of re-defining the running classes' content. The platform allows you to automatically launch such an applet at startup (just after the JVM is initialized).

{{%tip%}}**Tip:** All of the platform-certified Java stacks runs the ***jelastic-gc-agent.jar*** Java agent as a part of the standard optimization. It performs periodical Full GC calls to reduce the memory usage and release unused RAM back to OS. Due to [the platform contribution to the Java development](https://www.virtuozzo.com/company/blog/elastic-jvm-vertical-scaling/), similar functionality is natively implemented since the *12th* version of JDK.

Refer to the [Memory Agent](https://github.com/jelastic-jps/java-memory-agent) add-on to learn more about the platform automatic optimization of the managed Java stacks or use it to optimize any *custom* Java container.
![java memory agent add-on](00--java-memory-agent-addon.png){{%/tip%}}

Follow the next steps to add a custom Java agent into a container:

1\. Log in to the platform dashboard with your credentials and click the **Config** button for the application server in your Java environment:

![environment config button](01-environment-config-button.png)

2\. In the opened [configuration file manager](/configuration-file-manager), you can **Upload** your Java agent ***.jar*** file to any preferable location. Use the **Actions** list at the top panel (for the current folder) or the context menu when hovering over the particular directory.
![upload file to container](02-upload-file-to-container.png)

Provide a link to the required file or locate it on the local machine to **Upload**.

3\. Next, switch to the ***[variables.conf](/custom-environment-variables#java)*** file (the exact location vary based on the particular software stack) to provide custom variables and [JVM options](/java-options-arguments). Here, you can specify the *javaagent* parameter with a path to the required ***jar*** file. For example:
*javaagent:/opt/tomcat/temp/my-java-agent.jar*
![variables conf file](03-variables-conf-file.png)

Don't forget to **Save** the changes with the appropriate button above the editor.

4\. To apply the newly added settings, you need to **Restart Nodes** of your application server layer using the same-named option.
![restart nodes button](04--restart-nodes-button.png)

That's all! Now, your custom Java agent is up and running.


## What's next?
* [Environment Variables](/environment-variables/)
* [Custom Environment Variables](/custom-environment-variables/)
* [Java App Server Configuration](/java-application-server-config/)
* [Upload JAR Files](/upload-jar-archieves/)
* [Garbage Collector Agent](/garbage-collector-agent/)