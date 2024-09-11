---
draft: false
title: "Environment Variables"
aliases: "/environment-variables/"
seoindex: "index, follow"
seotitle: "Environment Variables"
seokeywords: "environment variables, default environment variables, software variables, software stack variables, container environment variables, java variables, php variables, ruby variables, nodejs variables, go variables, database variables, load balancer variables"
seodesc: "Find out about the default environment variables used in the platform-managed software stack. With the detailed description of the default environment variables, you&#8217;ll be able to easily utilize them to optimize your project."
menu: 
    docs:
        title: "Environment Variables"
        url: "/environment-variables/"
        weight: 10
        parent: "environment-variables"
        identifier: "environment-variables.md"
---

# Environment Variables

**Environment variables** are used to store the values of the frequently used parameters that are provided to a software program at runtime. The utilization of such placeholders makes your application more portable and flexible.

The most common use of variables is to make quick adjustments to specific values that are utilized multiple times in your application code. Follow the linked guide if you need to create such [custom environment variables](/custom-environment-variables/) for your project.

Another use case for variables is to configure the application through the set of predefined values (enable/disable features, change behavior, etc.). The platform supplements most of the certified software stacks with a number of default variables, which can be used by developers to help with application hosting.


## Default Environment Variables

{{%accordion title="Click this abstract to view a full list of default variables used within the platform containers."%}}
Variable Name|Editable*|Stacks|Description
---|:---:|---|---
**{SOFTWARE}_VERSION**|-|All|A version of the specified software (stack, engine, template, module, etc.).
**ADMIN_USER**|-|GlassFish (Payara), WildFly, Couchbase, LiteSpeed Web Server, LiteSpeed ADC, LLSMP|A login of the admin user for the administration console.
**ADMINPANEL_ENABLED (PHPMYADMIN_ENABLED)**|+|Databases, LLSMP, LEMP|The "*true*" and "*1*" values allow usage of the admin panel, while any other disables it. Restart is required to apply changes. The value in brackets is deprecated but can still be used on the MySQL and MariaDB databases.
**APP_FILE**|+|Node.js|The main Node.js application file to be launched.
**APP_NAME**|+|.NET Core|Points to the particular folder (if there are multiple applications in a single repository) or runs a specific *.dll* file in your project.
**ASPNETCORE_URLS**|+|.NET Core|Configures .NET Core services to work with the specified URL.
**AUTO_OLD_HEAP**|+|Node.js|Turns on/off (*true/false*) the platform memory autoconfiguration - sets the maximum size of an old heap based on the amount of memory on the container.
**CACHE_MEM_LIMIT**|+|PHP|Defines the portion of RAM, which should be reserved for the built-in *Redis* cache server, *10%* of container total RAM by default.
**CLONE_ON_SCALE**|+|All|Defines if new nodes upon horizontal scaling should be clones of a layer's master (*true*) or created from scratch (*false*).
**CP_MEM_LIMIT**|+|LLSMP, LEMP|Defines the portion of RAM, which should be reserved for the application server, *50%* of container total RAM by default.
**DAS**|-|GlassFish (Payara)|Shows if there is a DAS node (required to configure cluster) for the current layer.
**DB_MEM_LIMIT**|+|LLSMP, LEMP|Defines the portion of RAM, which should be reserved for the built-in *MariaDB* database server, *40%* of container total RAM by default.
**DEFAULT_CLUSTER**|+|LiteSpeed ADC|Selects the load balancing type for requests' proxying (*HTTP*, *AJP*, *FCGI*, *LSAPI*). This logic can be disabled (*0*, *disabled*, *false*).
**DOCKER_EXPOSED_PORT**|-|All|Lists ports from the *EXPOSE* directive of the image's dockerfile, which were opened via container firewall during the environment creation.
**FULL_GC_AGENT_DEBUG**|+|Java|Enables (*true*) or disables (*false*) the debug mode to track the Java GC processes in the logs.
**FULL_GC_PERIOD**|+|Java|Sets the interval (in seconds) between the full GC calls; *900* by default, i.e. 15 minutes.
**G1PERIODIC_GC_INTERVAL**|+ (for openJDK 12/13 only)|Java|A frequency of the G1 Periodic Collection in milliseconds (*G1PeriodicGCInterval - 15 minutes* by default); set as *0* to disable.
**G1PERIODIC_GC_SYS_LOAD_THRESHOLD**|+ (for openJDK 12/13 only)|Java|Allows G1 Periodic Collection execution, if the average one-minute system load is below the set value. This condition is ignored if set as zero. Is equal to the *{CPU_cores_number} * {GC_SYS_LOAD_THRESHOLD_RATE}* by default.
**GC_SYS_LOAD_THRESHOLD_RATE**|+ (for openJDK 12/13 only)|Java|Custom multiplier to flexibly adjust the *G1PeriodicGCSystemLoadThreshold* value (*0.3* by default).
**GEM_HOME**|+|Ruby|Locations (can be several) where gems can be found (should include *GEM_PATH*).
**GEM_PATH**|-|Ruby|A location where gems will be installed by default.
**GMS_LISTENER_PORT**|-|GlassFish (Payara)|A port used by the group management service (GMS).
**GO_BUILD_OPTIONS**|+|Go|Options and flags that should be used for the *Go* application building.
**GO_RUN**|+|Go|Sets the name of the executable binary file. If not specified, the deployment script will try to locate one based on the project name.
**GO_RUN_OPTIONS**|+|Go|Options and flags that should be used to run the *Go* application.
**GOPATH**|-|Go|Defines the *Go* application deployment folder.
**HAZELCAST_CONFIG**|+|GlassFish (Payara)|Sets a path to the *hazelcast* configuration file.
**HOME_DIR**|-|GlassFish (Payara), WildFly, Spring Boot, Java Engine, Node.js, Shared Storage|Container home directory.
**HOT_DEPLOY**|+|Tomcat, TomEE|Enables (*true/enabled/1*) or disables (*false/disabled/0*, by default) hot deploy (i.e. deploy without restart) for application server.
**IRBRC**|-|Ruby|A path to the *IRB* configuration file.
**JAVA_ARGS**|+|Java|Allows passing some custom arguments to the main function of your application.
**JAVA_HOME**|-|Java, Maven|Points to the directory where the Java runtime environment (*JRE*) is installed.
**JAVA_OPTS_CONFFILE**|-|Java, Maven|Path to the *[variables.conf](/java-options-arguments/)* file.
**JBOSS_HOME**|-|WildFly|WildFly home directory.
**JELASTIC_AUTOCONFIG**|+|PHP, LiteSpeed ADC, MySQL, MariaDB, Percona|Enables (*true/enabled/1*, by default) or disables (*false/disabled/0*) [smart auto-configuration](/auto-configuration/) based on the allocated RAM and number of CPU cores.
**JELASTIC_EXPOSE**|+|All|Manages the [auto-redirect functionality](/container-ports/#ports-auto-redirect) state with an ability to define the required port manually.
**JELASTIC_MEMORY_AUTOCONFIG**|+|WildFly|Enables (*true*) or disables (*false*) memory auto-configuration for WildFly.
**JELASTIC_PRIORITY_PORTS**|+|GlassFish (Payara)|Sets a *GlassFish* HTTP listener port.
**LAUNCH_JBOSS_IN_BACKGROUND**|+|WildFly|Enables (*true*) or disables (*false*) start of an application server in the background mode.
**LSWS_MAX_CHILDREN**|+|LLSMP, LiteSpeed Web Server|Redefines the maximum children process limit for the server. The variable is hidden by default as the platform sets this value equal to the number of available CPU cores (usually ensures the best operability). You need to manually add this variable and restart the server to redefine the value.
**MASTER_HOST**|-|All|A short hostname for a master node within a layer.
**MASTER_ID**|-|All|A unique node identifier of a master node within a layer.
**MASTER_IP**|-|All|An internal IP address of a master node within a layer.
**MAVEN_DEPLOY_ARTIFACT**|+|Maven|Defines an artifact to be deployed (can be redefined for a [particular project](/maven-configuration/#maven-specific-variables)).
**MAVEN_OPTS**|+|Maven|Sets parameters to be used to start up the JVM running Maven and can be used to supply additional global [options](/java-options-arguments/).
**MAVEN_RUN_ARGS**|+|Maven|Allows passing some custom arguments for the application build (can be redefined for a [particular project](/maven-configuration/#maven-specific-variables)).
**MAX_OOM_REDUCE_CYCLES**|+|MySQL, MariaDB, Percona|Configures a maximum number of cycles for *innodb_buffer_pool_size* reduction after OOM-caused restart (*5* times by default).
**MY_RUBY_HOME**|-|Ruby|A path to the directory where the *Ruby* engine is located.
**NODE_ENV**|-|Node.js|Specifies the environment in which an application is running (e.g. *development*, *staging*, *production*, *testing*, etc.).
**NODE_OPTIONS**|+|Node.js|Variable for specifying the Node.js runtime *v8* options.
**NVM_DIR**|-|Node.js|A path to the *NVM* installation location.
**ON_ENV_INSTALL**|+ (before env creation)|All|A script (or link to it) to be executed after environment creation.
**OOM_ADJUSTMENT**|+|MySQL, MariaDB, Percona|Defines a value in %, MB, GB (*10%* by default) that the current *innodb_buffer_pool_size* parameter should be reduced after each OOM-caused restart.
**OOM_DETECTION_DELTA**|+|MySQL, MariaDB, Percona|Sets a period (*2* seconds by default) for the platform to analyze logs after each service restart to decide if it was caused by OOM killer.
**OPEN_INBOUND_PORTS (JELASTIC_PORTS)**|+ (before env creation)|All|Specifies custom ports, which should be opened in the firewall during container creation.
**PACKAGE_MANAGER**|+|Node.js|A variable that contains the name of a [package manager](/nodejs-package-managers/) for installing the javascript packages (*npm* or *yarn*).
**PACKAGE_MANAGER_OPTS**|+|Node.js|Additional options for the package manager (refer to the official [npm](https://docs.npmjs.com/cli/install) or [yarn](https://yarnpkg.com/lang/en/docs/cli/install/) documentation).
**PATH**|-|All|A default shell variable, with a list of paths to directories with executable programs.
**PHP_MAX_EXECUTION_TIME**|+|PHP|Sets the *[max_execution_time](https://www.php.net/manual/en/info.configuration.php#ini.max-execution-time)* PHP setting - a maximum time (in seconds) before terminating a script. *300* seconds by default.
**PHP_MEMORY_LIMIT**|+|PHP|Sets the *[memory_limit](https://www.php.net/manual/en/ini.core.php#ini.memory-limit)* PHP setting - a  maximum memory limit per script. It can be set in percentage or MB (*25%* by default; *-1* for unlimited).
**PHPFPM_MAX_CHILDREN**|+|NGINX PHP|Sets a number of child worker processes for PHP-FPM. It is equal to the number of CPU cores available for the container by default (but no less than 2).
**PORT_4848_TCP_PORT**|-|GlassFish (Payara)|A port for the admin console.
**PROCESS_MANAGER**|+|Node.js|Variable for choosing the Node.js [process manager](/nodejs-process-managers/) (i.e. *npm*, *pm2*, *forever*).
**PROCESS_MANAGER_FILE**|-|Node.js|A path to the file that contains the start options for the process manager.
**PROXY_READ_TIMEOUT**|+|NGINX balancer, NGINX PHP|Sets a read timeout (in seconds) from the backend.
**PSWD_FILE**|-|GlassFish (Payara)|A path to the file with an admin user password.
**REDIRECT_EXCLUDE_PORTS**|+|Node.js|Excludes listed ports from the [auto-redirect algorithm](/container-ports/#ports-auto-redirect) (e.g. *22,23,25,21,111,2049,8743,7979*).
**REDIS_COMMANDER**|+|Redis|Defines if the *Redis Commander* management tool should be *enabled* or *disabled*.
**REDIS_ENABLED**|+|PHP|Enables (*true*) or disables (*false*) object caching with Redis. Service restart is required to apply changes.
**REDIS_SENTINEL**|+|Redis|Defines if the *Redis Sentinel* high-availability and monitoring tool should be *enabled* or *disabled*.
**ROOT_DIR**|-|Node.js|Displays a path to the application deployment directory.
**RUN_OPTION**|+|.NET Core|Provides additional *dotnet run* options for your project.
**SERVER_WEBROOT**|-|LLSMP, LiteSpeed Web Server|Displays a path to the application deployment directory.
**STACK_NAME**|-|All|The name of the current stack.
**STACK_PATH**|-|All|The home directory of the stack.
**STACK_USER**|-|All|The name of the stack's default user.
**STANDALONE_MODE_CONFIG**|+|WildFly|A configuration file to launch a [standalone WildFly](/wildfly/#standalone-mode) server.
**TCP_BALANCING**|+|HAProxy|Enables (*true*) or disables (*false*) traffic proxying and balancing to TPC backends.
**UPDATE_PACKAGES_ON_RESTART**|+|Node.js|Enables (*true*) or disables (*false*) automatic packages installation after the *nodejs* service restart. If there is no *node_modules* directory inside the *webroot* one, such an update is called regardless of this variable.
**UPSTREAM_KEEPALIVE**|+|NGINX balancer|Sets the *[keepalive](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive)* directive value for the upstream.
**VERT_SCALING**|+|Java|Defines if the default Java [GC agent](https://www.virtuozzo.com/company/blog/garbage-collection/) should be enabled (*true*) or disabled (*false*).
**WAF**|+|LLSMP, LiteSpeed Web Server|Enables (*true*) or disables (*false*) Web Application Firewall with the [Comodo](https://waf.comodo.com/) default ruleset for the *LiteSpeed Web Server*.
**WEB_ROOT**|-|Go|A path to the deployed application.
**WEBROOT**|-|PHP, Tomcat (TomEE), GlassFish (Payara)|Displays a path to the application deployment directory.
**WORKER_PROCESSES**|+|NGINX balancer|Sets a number of worker processes - can be autodetected by NGINX (*auto*) or set equal to the CPU cores count (*define*).
**WP_PROTECT**|+|LLSMP, LiteSpeed Web Server, LiteSpeed ADC|Configures an action for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*off\|on\|drop\|deny\|throttle\|captcha*; *off* by default).
**WP_PROTECT_LIMIT**|+|LLSMP, LiteSpeed Web Server, LiteSpeed ADC|Sets a limit for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*0\|1\|2-1000*; *10* by default).
{{%/accordion%}}

Or use the categorized groups below to narrow the search.

{{%note%}}**Note:** Variables marked with "***+***" in the **Editable** column can be freely adjusted to customize your container. Herewith, a restart is required to apply changes.

It is <u>*not recommended*</u> to adjust variables marked with "***-***" as such an action won't apply any actual changes to the container; however, it may break some internal logic.{{%/note%}}

There are a number of options that can be used with all of the [platform-managed stacks](/software-stacks-versions/):

Variable Name|Editable*|Description|
---|:---:|---
**{SOFTWARE}_VERSION**|-|A version of the specified software (stack, engine, template, module, etc.).
**CLONE_ON_SCALE**|+|Defines if new nodes upon horizontal scaling should be clones of a layer's master (*true*) or created from scratch (*false*).
**DOCKER_EXPOSED_PORT**|-|Lists ports from the *EXPOSE* directive of the image's dockerfile, which were opened via container firewall during the environment creation.
**JELASTIC_EXPOSE**|+|Manages the [auto-redirect functionality](/container-ports/#ports-auto-redirect) state with an ability to define the required port manually.
**MASTER_HOST**|-|A short hostname for a master node within a layer.
**MASTER_ID**|-|A unique node identifier of a master node within a layer.
**MASTER_IP**|-|An internal IP address of a master node within a layer.
**ON_ENV_INSTALL**|+ (before env creation)|A script (or link to it) to be executed after environment creation.
**OPEN_INBOUND_PORTS (JELASTIC_PORTS)**|+ (before env creation)|Specifies custom ports, which should be opened in the firewall during container creation.
**PATH**|-|A default shell variable, with a list of paths to directories with executable programs.
**STACK_NAME**|-|The name of the current stack.
**STACK_PATH**|-|The home directory of the stack.
**STACK_USER**|-|The name of the stack's default user.


### Java

{{%accordion title="Click here to list Java variables."%}}
Stack|Variable Name|Editable*|Description
---|---|:---:|---
All Java|**FULL_GC_AGENT_DEBUG**|+|Enables (*true*) or disables (*false*) the debug mode to track the Java GC processes in the logs.
All Java|**FULL_GC_PERIOD**|+|Sets the interval (in seconds) between the full GC calls; *900* by default, i.e. 15 minutes.
All Java|**G1PERIODIC_GC_INTERVAL**|+ (for openJDK 12/13 only)|A frequency of the G1 Periodic Collection in milliseconds (*G1PeriodicGCInterval - 15 minutes* by default); set as 0 to disable.
All Java|**G1PERIODIC_GC_SYS_LOAD_THRESHOLD**|+ (for openJDK 12/13 only)|Allows G1 Periodic Collection execution, if the average one-minute system load is below the set value. This condition is ignored if set as zero. Is equal to the *{CPU_cores_number} * {GC_SYS_LOAD_THRESHOLD_RATE}* by default.
All Java|**GC_SYS_LOAD_THRESHOLD_RATE**|+ (for openJDK 12/13 only)|Custom multiplier to flexibly adjust the *G1PeriodicGCSystemLoadThreshold* value (*0.3* by default).
All Java|**JAVA_ARGS**|+|Allows passing some custom arguments to the main function of your application.
All Java|**JAVA_HOME**|-|Points to the directory where the Java runtime environment (*JRE*) is installed.
All Java|**JAVA_OPTS_CONFFILE**|-|Path to the *[variables.conf](/java-options-arguments/)* file.
All Java|**VERT_SCALING**|+|Defines if the default Java [GC agent](https://www.virtuozzo.com/company/blog/garbage-collection/) should be enabled (*true*) or disabled (*false*).
Tomcat & TomEE|**HOT_DEPLOY**|+|Enables (*true/enabled/1*) or disables (*false/disabled/0*, by default) hot deploy (i.e. deploy without restart) for application server.
Tomcat & TomEE|**WEBROOT**|-|Displays a path to the application deployment directory.
GlassFish & Payara|**ADMIN_USER**|-|A login of the admin user for the administration console.
GlassFish & Payara|**DAS**|-|Shows if there is a *DAS* node (required to configure cluster) for the current layer.
GlassFish & Payara|**GMS_LISTENER_PORT**|-|A port used by the group management service (*GMS*).
GlassFish & Payara|**HAZELCAST_CONFIG**|+|Sets a path to the *hazelcast* configuration file.
GlassFish & Payara|**HOME_DIR**|-|Container home directory.
GlassFish & Payara|**JELASTIC_PRIORITY_PORTS**|+|Sets a *GlassFish* HTTP listener port.
GlassFish & Payara|**PORT_4848_TCP_PORT**|-|A port for the admin console.
GlassFish & Payara|**PSWD_FILE**|-|A path to the file with an admin user password.
GlassFish & Payara|**WEBROOT**|-|Displays a path to the application deployment directory.
WildFly|**ADMIN_USER**|-|A login of the admin user for the administration console.
WildFly|**HOME_DIR**|-|Container home directory.
WildFly|**JBOSS_HOME**|-|WildFly home directory.
WildFly|**JELASTIC_MEMORY_AUTOCONFIG**|+|Enables (*true*) or disables (*false*) memory auto-configuration for WildFly.
WildFly|**LAUNCH_JBOSS_IN_BACKGROUND**|+|Enables (*true*) or disables (*false*) start of an application server in the background mode.
WildFly|**STANDALONE_MODE_CONFIG**|+|A configuration file to launch a [standalone WildFly](/wildfly/#standalone-mode) server.
Spring Boot|**HOME_DIR**|-|Container home directory.
Java Engine|**HOME_DIR**|-|Container home directory.
{{%/accordion%}}


### PHP

{{%accordion title="Click here to list PHP variables."%}}
Stack|Variable Name|Editable*|Description
---|---|:---:|---
All PHP|**CACHE_MEM_LIMIT**|+|Defines the portion of RAM, which should be reserved for the built-in *Redis* cache server, *10%* of container total RAM by default.
All PHP|**JELASTIC_AUTOCONFIG**|+|Enables (*true/enabled/1*, by default) or disables (*false/disabled/0*) [smart auto-configuration](/auto-configuration/) based on the allocated RAM and number of CPU cores.
All PHP|**PHP_MAX_EXECUTION_TIME**|+|Sets the *[max_execution_time](https://www.php.net/manual/en/info.configuration.php#ini.max-execution-time)* PHP setting - a maximum time (in seconds) before terminating a script. *300* seconds by default.
All PHP|**PHP_MEMORY_LIMIT**|+|Sets the *[memory_limit](https://www.php.net/manual/en/ini.core.php#ini.memory-limit)* PHP setting - a  maximum memory limit per script. It can be set in percentage or MB (*25%* by default; *-1* for unlimited).
All PHP|**REDIS_ENABLED**|+|Enables (*true*) or disables (*false*) object caching with Redis. Service restart is required to apply changes.
All PHP|**WEBROOT**|-|Displays a path to the application deployment directory.
NGINX|**PHPFPM_MAX_CHILDREN**|+|Sets a number of child worker processes for PHP-FPM. It is equal to the number of CPU cores available for the container by default (but no less than 2).
NGINX|**PROXY_READ_TIMEOUT**|+|Sets a read timeout (in seconds) from the backend.
LiteSpeed Web Server|**ADMIN_USER**|-|A login of the admin user for the administration console.
LiteSpeed Web Server|**LSWS_MAX_CHILDREN**|+|Redefines the maximum children process limit for the server. The variable is hidden by default as the platform sets this value equal to the number of available CPU cores (usually ensures the best operability). You need to manually add this variable and restart the server to redefine the value.
LiteSpeed Web Server|**SERVER_WEBROOT**|-|Displays a path to the application deployment directory.
LiteSpeed Web Server|**WAF**|+|Enables (*true*) or disables (*false*) Web Application Firewall with the [Comodo](https://waf.comodo.com/) default ruleset for the *LiteSpeed Web Server*.
LiteSpeed Web Server|**WP_PROTECT**|+|Configures an action for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*off\|on\|drop|deny\|throttle\|captcha*; *off* by default).
LiteSpeed Web Server|**WP_PROTECT_LIMIT**|+|Sets a limit for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*0\|1\|2-1000*; *10* by default).
LLSMP|**ADMIN_USER**|-|A login of the admin user for the administration console.
LLSMP|**ADMINPANEL_ENABLED**|+|The "*true*" and "*1*" values allow usage of the admin panel, while any other disables it. Restart is required to apply changes.
LLSMP|**CP_MEM_LIMIT**|+|Defines the portion of RAM, which should be reserved for the application server, *50%* of container total RAM by default.
LLSMP|**DB_MEM_LIMIT**|+|Defines the portion of RAM, which should be reserved for the built-in *MariaDB* database server, *40%* of container total RAM by default.
LLSMP|**LSWS_MAX_CHILDREN**|+|Redefines the maximum children process limit for the server. The variable is hidden by default as the platform sets this value equal to the number of available CPU cores (usually ensures the best operability). You need to manually add this variable and restart the server to redefine the value.
LLSMP|**SERVER_WEBROOT**|-|Displays a path to the application deployment directory.
LLSMP|**WAF**|+|Enables (*true*) or disables (*false*) Web Application Firewall with the [Comodo](https://waf.comodo.com/) default ruleset for the *LiteSpeed Web Server*.
LLSMP|**WP_PROTECT**|+|Configures an action for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*off\|on\|drop\|deny\|throttle\|captcha*; *off* by default).
LLSMP|**WP_PROTECT_LIMIT**|+|Sets a limit for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*0\|1\|2-1000*; *10* by default).
LEMP|**ADMINPANEL_ENABLED**|+|The "*true*" and "*1*" values allow usage of the admin panel, while any other disables it. Restart is required to apply changes.
LEMP|**CP_MEM_LIMIT**|+|Defines the portion of RAM, which should be reserved for the application server, *50%* of container total RAM by default.
LEMP|**DB_MEM_LIMIT**|+|Defines the portion of RAM, which should be reserved for the built-in *MariaDB* database server, *40%* of container total RAM by default.
{{%/accordion%}}


### Ruby

{{%accordion title="Click here to list Ruby variables."%}}
Variable Name|Editable*|Description
---|:---:|---
**GEM_HOME**|+|Locations (can be several) where gems can be found (should include *GEM_PATH*).
**GEM_PATH**|-|A location where gems will be installed by default.
**IRBRC**|-|A path to the *IRB* configuration file.
**MY_RUBY_HOME**|-|A path to the directory where the Ruby engine is located.
{{%/accordion%}}


### Node.js

{{%accordion title="Click here to list Node.js variables."%}}
Variable Name|Editable*|Description
---|:---:|---
**APP_FILE**|+|The main Node.js application file to be launched.
**AUTO_OLD_HEAP**|+|Turns on/off (*true/false*) the platform memory autoconfiguration - sets the maximum size of an old heap based on the amount of memory on the container.
**HOME_DIR**|-|Container home directory.
**NODE_ENV**|-|Specifies the environment in which an application is running (e.g. *development*, *staging*, *production*, *testing*, etc.).
**NODE_OPTIONS**|+|Variable for specifying the Node.js runtime *v8* options.
**NVM_DIR**|-|A path to the *NVM* installation location.
**PACKAGE_MANAGER**|+|A variable that contains the name of a [package manager](/nodejs-package-managers/) for installing the javascript packages (*npm* or *yarn*).
**PACKAGE_MANAGER_OPTS**|+|Additional options for the package manager (refer to the official [npm](https://docs.npmjs.com/cli/install) or [yarn](https://yarnpkg.com/lang/en/docs/cli/install/) documentation).
**PROCESS_MANAGER**|+|Variable for choosing the Node.js [process manager](/nodejs-process-managers/) (i.e. *npm*, *pm2*, *forever*).
**PROCESS_MANAGER_FILE**|-|A path to the file that contains the start options for the process manager.
**REDIRECT_EXCLUDE_PORTS**|+|Excludes listed ports from the [auto-redirect](/container-ports/#ports-auto-redirect) algorithm (e.g. *22,23,25,21,111,2049,8743,7979*).
**ROOT_DIR**|-|Displays a path to the application deployment directory.
**UPDATE_PACKAGES_ON_RESTART**|+|Enables (*true*) or disables (*false*) automatic packages installation after the *nodejs* service restart. If there is no *node_modules* directory inside the *webroot* one, such an update is called regardless of this variable.
{{%/accordion%}}


### Go (Golang)

{{%accordion title="Click here to list Go (Golang) variables."%}}
Variable Name|Editable*|Description
---|:---:|---
**GO_BUILD_OPTIONS**|+|Options and flags that should be used for the *Go* application building.
**GO_RUN**|+|Sets the name of the executable binary file. If not specified, the deployment script will try to locate one based on the project name.
**GO_RUN_OPTIONS**|+|Options and flags that should be used to run the *Go* application.
**GOPATH**|-|Defines the *Go* application deployment folder.
**WEB_ROOT**|-|A path to the deployed application.
{{%/accordion%}}


### .NET Core

{{%accordion title="Click here to list .NET Core variables."%}}
Variable Name|Editable*|Description
---|:---:|---
**APP_NAME**|+|Points to the particular folder (if there are multiple applications in a single repository) or runs a specific *.dll* file in your project.
**ASPNETCORE_URLS**|+|Configures .NET Core services to work with the specified URL.
**RUN_OPTION**|+|Provides additional *dotnet run* options for your project.
{{%/accordion%}}


### Load Balancers

{{%accordion title="Click here to list Load Balancers variables."%}}
Stack|Variable Name|Editable*|Description
---|---|:---:|---
HAProxy|**TCP_BALANCING**|+|Enables (*true*) or disables (*false*) traffic proxying and balancing to TPC backends.
NGINX|**PROXY_READ_TIMEOUT**|+|Sets a read timeout (in seconds) from the backend.
NGINX|**UPSTREAM_KEEPALIVE**|+|Sets the *[keepalive](http://nginx.org/en/docs/http/ngx_http_upstream_module.html#keepalive)* directive value for the upstream.
NGINX|**WORKER_PROCESSES**|+|Sets a number of worker processes - can be autodetected by NGINX (*auto*) or set equal to the CPU cores count (*define*).
LiteSpeed ADC|**ADMIN_USER**|-|A login of the admin user for the administration console.
LiteSpeed ADC|**DEFAULT_CLUSTER**|+|Selects the load balancing type for requests' proxying (*HTTP*, *AJP*, *FCGI*, *LSAPI*). This logic can be disabled (*0*, *disabled*, *false*).
LiteSpeed ADC|**JELASTIC_AUTOCONFIG**|+|Enables (*true/enabled/1*, by default) or disables (*false/disabled/0*) [smart auto-configuration](/auto-configuration/) based on the allocated RAM and number of CPU cores.
LiteSpeed ADC|**WP_PROTECT**|+|Configures an action for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*off\|on\|drop\|deny\|throttle\|captcha*; *off* by default).
LiteSpeed ADC|**WP_PROTECT_LIMIT**|+|Sets a limit for the [WordPress Brute Force Attack Protection](https://www.litespeedtech.com/support/wiki/doku.php/litespeed_wiki:config:wordpress-protection) feature (*0\|1\|2-1000*; *10* by default).
{{%/accordion%}}


### Databases

{{%accordion title="Click here to list Databases variables."%}}
Stack|Variable Name|Editable*|Description
---|---|:---:|---
All Databases|**ADMINPANEL_ENABLED**  (**PHPMYADMIN_ENABLED**)|+|The "*true*" and "*1*" values allow usage of the admin panel, while any other disables it. Restart is required to apply changes. The value in brackets is deprecated but can still be used on the MySQL and MariaDB databases.
MySQL, MariaDB, Percona|**JELASTIC_AUTOCONFIG**|+|Enables (*true/enabled/1*, by default) or disables (*false/disabled/0*) [smart auto-configuration](/auto-configuration/) based on the allocated RAM and number of CPU cores.
MySQL, MariaDB, Percona|**MAX_OOM_REDUCE_CYCLES**|+|Configures a maximum number of cycles for *innodb_buffer_pool_size reduction* after OOM-caused restart (*5* times by default).
MySQL, MariaDB, Percona|**OOM_ADJUSTMENT**|+|Defines a value in %, MB, GB (*10%* by default) that the current *innodb_buffer_pool_size* parameter should be reduced after each OOM-caused restart.
MySQL, MariaDB, Percona|**OOM_DETECTION_DELTA**|+|Sets a period (*2* seconds by default) for the platform to analyze logs after each service restart to decide if it was caused by OOM killer.
Redis|**REDIS_COMMANDER**|+|Defines if the *Redis Commander* management tool should be *enabled* or *disabled*.
Redis|**REDIS_SENTINEL**|+|Defines if the *Redis Sentinel* high-availability and monitoring tool should be *enabled* or *disabled*.
Coachbase|**ADMIN_USER**|-|A login of the admin user for the administration console.
{{%/accordion%}}


### Other Stacks

{{%accordion title="Click here to list Other Stacks variables."%}}
Stack|Variable Name|Editable*|Description
---|---|:---:|---
Maven|**JAVA_HOME**|-|Points to the directory where the Java runtime environment (*JRE*) is installed.
Maven|**JAVA_OPTS_CONFFILE**|-|Path to the *[variables.conf](/java-options-arguments/)* file.
Maven|**MAVEN_DEPLOY_ARTIFACT**|+|Defines an artifact to be deployed (can be redefined for a [particular project](/maven-configuration/#maven-specific-variables)).
Maven|**MAVEN_OPTS**|+|Sets parameters to be used to start up the JVM running Maven and can be used to supply additional global [options](/java-options-arguments/).
Maven|**MAVEN_RUN_ARGS**|+|Allows passing some custom arguments for the application build (can be redefined for a [particular project](/maven-configuration/#maven-specific-variables)).
Maven|**VERT_SCALING**|+|Defines if the default Java [GC agent](https://www.virtuozzo.com/company/blog/garbage-collection/) should be enabled (*true*) or disabled (*false*).
Shared Storage|**HOME_DIR**|-|Container home directory.
{{%/accordion%}}


## What's next?

* [Custom Environment Variables](/custom-environment-variables/)
* [Java Options and Arguments](/java-options-arguments/)
* [Configuration File Manager](/configuration-file-manager/)