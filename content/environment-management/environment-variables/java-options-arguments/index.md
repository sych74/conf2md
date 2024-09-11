---
draft: false
title: "Java Options and Arguments"
aliases: "/java-options-arguments/"
seoindex: "index, follow"
seotitle: "Java Options and Arguments"
seokeywords: "custom java options arguments cloud hosting, java jvm arguments, pass java arguments spring boot, passing arguments to spring boot, passing java options tomcat, set custom jvm options, set custom jvm arguments, spring boot set java opts args, add jar arguments spring boot, java options paas, jvm options jar arguments, passing java options jetty, java options for paas containers, java memory options paas, java options xmx, java arguments paas, passing jvm options to spring boot, java options arguments paas, adjust java options paas, java_opts variable, java_args variable"
seodesc: "Learn how to adjust Java options and arguments for containers within the platform. Use dedicated environment variables to provide your custom options for Java stacks."
menu: 
    docs:
        title: "Java Options and Arguments"
        url: "/java-options-arguments/"
        weight: 20
        parent: "environment-variables"
        identifier: "java-options-arguments.md"
---

# Java Options and Arguments

In order to ensure cost efficiency, all platform-managed Java servers are automatically configured to utilize memory in the most beneficial way. It is achieved by adjusting the main Java memory parameters based on resources allocated to a container.

{{%tip%}}**Tip:** Custom Java servers (e.g. inside Docker containers or VPS) can be optimized similarly using the [Java Memory Agent](https://github.com/jelastic-jps/java-memory-agent/) add-on.{{%/tip%}}

The default options can be manually changed to ensure high performance or to support any custom implementation.

1\. In order to provide all the preferred [Java options](https://docs.oracle.com/javase/7/docs/technotes/tools/windows/java.html#CBBIJCHG) at once, the ***variables.conf*** file can be utilized.

Depending on a particular application server you are working with, the exact location may vary:

* **Tomcat**, **TomEE** - */opt/tomcat/conf/variables.conf*
* **Jetty** - */opt/jetty/etc/variables.conf*
* **Spring Boot** - */opt/shared/conf/variables.conf*
* **GlassFish** - */opt/glassfish/glassfish/domains/domain1/config/variables.conf*
* **Payara** - */opt/payara/glassfish/domains/domain1/config/variables.conf*
* **WildFly** - */opt/wildfly/conf/variables.conf*

![variables.conf file for Java options](01-variables-conf-file.png)

If needed, you can [redefine the main memory options](#redefining-main-java-parameters) via container variables.

2\. Don't forget to **Restart nodes** to apply changes.

![restart nodes button](02-restart-nodes-button.png)

That's it! Now, your application is running with your custom Java options.


## Redefining Main Java Parameters

Most of the essential memory parameters (*-Xms*, *-Xmn*, *-Xmx*, *-Xminf*, *-Xmaxf*, *-XX:MaxPermSize*, *-XX:+Use.*GC*) can be redefined using the dedicated environment [variables](/container-variables/).

As an example, you can **Add** the ***-Xmx*** option (i.e. maximum size for the Java heap memory):

![add Java memory optimization variable](03-memory-optimization-variables.png)

{{%tip%}}**Tip:** The platform supports two additional variables that allow setting up main RAM parameters as a percentage of the total memory available:

- ***XMS_DEF_PERCENT*** - the initial size (%) of the memory allocation pool
- ***XMX_DEF_PERCENT*** -  the maximum size (%) of the memory allocation pool

These values are automatically validated - if *XMS* is bigger than *XMX*, its actual value is set equal to *XMX*.{{%/tip%}}


## Spring Boot and Java Engine Specific Variables

When operating with the **Spring Boot** and **Java Engine** templates, you can provide two additional [variables](/container-variables/):

* ***JAVA_OPTS*** - to customize Java options for your app (similar to the ***variables.conf*** file)
* ***JAVA_ARGS*** - to pass some custom arguments to your application main function

![Spring Boot variables for Java options arguments](04-spring-boot-java-options-arguments.png)

Don't forget to restart your application server(s) in order to apply changes.


## What's next?

* [Variables List](/environment-variables/)
* [Environment Variables](/container-variables/)
* [Custom Environment Variables](/custom-environment-variables/)