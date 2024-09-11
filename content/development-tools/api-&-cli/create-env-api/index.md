---
draft: false
title: "CreateEnv Params"
aliases: "/create-env-api/"
seoindex: "index, follow"
seotitle: "Parameters for CreateEnv API"
seokeywords: "cli, platform cli, api, platform api, create environment, create environment parameters, api parameters, cli parameters, create environment example"
seodesc: "Get a full list of parameters for a new environment creation procedure, which is used by such platform development tools as CLI, API and JPS."
menu: 
    docs:
        title: "CreateEnv Params"
        url: "/create-env-api/"
        weight: 40
        parent: "api-&-cli"
        identifier: "create-env-api.md"
---

# Parameters for CreateEnvironment API

Creation of a new environment at the platform can be automated in a variety of different ways, e.g. with the help of [platform CLI](/cli/), through the direct [API](https://www.virtuozzo.com/application-platform-api-docs/) request or by declaring the appropriate parameters via [JPS](/jps/) manifest. Herewith, though representing a rather simple operation, it can include a bunch of different parameters for the precise topology definition.

Thus, below we provide the description for all of such settings with the examples on their usage via CLI. They are divided into 3 major sections as arrays of the *~/jelastic/environment/control/createenvironment* method, being named according to the appropriate arrays' denominations - two common ones and listing of the specialized parameters for the Docker containers' creation:

* [env](#common-environment-configurations)
* [nodes](#nodes-configurations)
* [docker](#docker-based-environment-configurations)


## Common Environment Configurations

The parameters below are to be specified within the ***env*** array (of either CLI command or JSON file) and define the most common environment configurations, like *programming language*, *name*, *region* and others:

Name|Description|Type|Example Value|Mandatory
---|---|---|---|---
*region*|[Environment region](/environment-regions)|string|Name of the required region - depends on hosting service provider settings.|no
*ishaenabled*|[High Availability](/session-replication)|boolean|*true*, *false*<br>**Note:** Applicable only for *Tomcat 6/7*, *Jetty6*, *TomEE*, *GlassFish3*|no
*engine*|Programming language version|string|*java6*, *java7*, *java8*, *php5.3*, *php5.4*, *php5.5*, etc.|yes (except of Docker-based environments)
*displayName*|[Environment alias](/environment-aliases)|string|*my-env-alias*|no
*sslstate*|[Built-In SSL](/built-in-ssl/)|boolean|*true*, *false*|no
*shortdomain*|Name for the environment to be created|string|*my-cli-env*|yes

Example: 

```
env '{"region": "default_hn_group", "ishaenabled": "false", "engine": "java7", "displayName": "my-env-alias", "sslstate": "true", "shortdomain": "my-cli-env"}'
```


## Nodes Configurations

Within the ***nodes*** section, more subtle adjustment can be set to define the comprised servers' parameters, like their *type*, *amount*, number of allocated *reserved/dynamic cloudlets* and more:

Name|Description|Type|Example Value|Mandatory
---|---|---|---|---
*extip*|[Public IP](/public-ipv4)|boolean|*true*, *false*|no
*count*|Number of nodes|integer|*1*, *2*, *3*, ...|no
*fixedCloudlets*|Number of fixed cloudlets|integer|*1*, *2*, *3*, ...|yes
*flexibleCloudlets*|Number of flexible cloudlets|integer|*1*, *2*, *3*, &hellip; but can not be less than **fixedCloudlets**|yes
*displayName*|Node's [alias](/environment-aliases) name|string|*my-node-alias*|no
*nodeType*|Type of the stack|string|*docker*, *tomcat6*, *tomcat7*, *tomee*, *mysql5*, *apache2*, *nginxphp*, etc. (see the full list of available values [here](/application-manifest#nodeTypeList))|yes
*docker*|List of Docker container settings |array|check the corresponding section [below](#docker)|only for *docker* **nodeType**

Example:

```
nodes '[{"extip": "true", "count": "2", "fixedCloudlets": "16", "flexibleCloudlets": "32", "displayName": "my-node-alias", "nodeType": "docker", "docker": {...}}]'
```


## Docker-Based Environment Configurations

The ***docker*** subsection is intended to state the specialized Docker container parameters, required for its deployment.

Name|Description|Type|Example Value|Mandatory
---|---|---|---|---
*cmd*|[Run command](/docker-run) configuration|string|*run.sh*|no
*image*|Docker image name with a tag version (optionally)|string|*ubuntu*, *tutum/apache-php*, *jelastic/tomcat8:latest*, etc.|yes
*nodeGroup*|Environment layer the image should be placed to|string|*cp* - application server<br>*bl* - load balancer<br>*nosqldb* - noSQL database<br>*sqldb* - SQl database<br>*cache* - cache node<br>*storage* - storage node|no (if not specified, an image will be added to the *Extra* layer)
*links*|[Linking](/docker-links) parameters|array|described within the expandable list below|no
*env*|The list of [environment variables](/docker-variables)|object|described within the expandable list below|no
*registry*|Credentials for the private registry|array|described within the expandable list below|no
*volumes*|List of local [volumes](/docker-volumes)|array|described within the expandable list below|no
*volumeMounts*|List of [mounted](/mount-points) data directories|array|described within the expandable list below|no
*volumesFrom*|List of nodes to copy the volume settings from|array|described within the expandable list below|no

Example:

```
"docker": {"cmd": "run.sh", "image": "jelastic/tomcat8:latest", "nodeGroup": "cp", "links": [...], "env": {...}, "registry": {...}, "volumes": [...], "volumeMounts": {...}, "volumesFrom": [{...}]}
```

* {{%accordion title="linking configuration - for establishing connection between Docker containers in confines of a single environment"%}}
|Name|Description|Type|Example Value|Mandatory|
|---|---|---|---|---|
|*-*|defines the layer/node the current instance should be linked with and sets an alias for this bundle|string|*sqldb:DB*, *cp:alias*|no|

Example: 
```
"links": ["cp:alias", "sqldb:DB"]
```
{{%/accordion%}} 

* {{%accordion title="environment variables configuration - for stating environment variables in Docker containers"%}}
|Name|Description|Type|Example Value|Mandatory|
|---|---|---|---|---|
|*custom_variable_name*|Sets the environment variables|string|*var1 value1* (the entire string after first space will be treated as the value, including spaces and quotes) *var2=value1 \value2 \value3* (for setting multiple values at a time, i.e. to create an array; here, quotes and backslashes are used as separators)|no|
 
Example:
```
"env": {"var1": "value1", "var2": "value1 \value2 \value3"}
```
{{%/accordion%}} 

* {{%accordion title="registry configuration - for connection to private registry"%}}
|Name|Description|Type|Example Value|Mandatory|
|---|---|---|---|---|
|*password*|Password to a private registry|string|*passw0rd*|only if you are using private registry|
|*user*|Name of the user of a private registry|string|*admin*|only if you are using private registry|
|*url*|URL to a private registry|string|*<span>http</span>://example.com/private-registry*|only if you are using private registry|

Example:
```
"registry": {"password": "passw0rd", "user": "admin", "url": "http://example.com/private-registry"}
```
{{%/accordion%}}
 
* {{%accordion title="local volumes - list of volumes to be created within local file system of Docker container"%}}
|Name|Description|Type|Example Value|Mandatory|
|---|---|---|---|---| 
|custom_path|Local volume path|string|*/my_custom_volume*|no|

Example:
```
"volumes": ["/volume1", "/volume2", "/volume3"]
```
{{%/accordion%}}

* {{%accordion title="mount points - set of parameters that define folder(s) with required data to be attached from other servers"%}}
|Name|Description|Type|Example Value|Mandatory|
|---|---|---|---|---|
|local_path|Local path the mounted data will refer to|array|*/mounted_data*|yes|
|sourcePath|Path to the required data directory on the remote server|string|*/required_data*<br>if not defined, is stated equal to ***local_path*** (for remote storage server)|no|
|sourceNodeId|Node ID of storage container|integer|*459315*|yes in case neither ***sourceNodeGroup***, nor ***sourceHost*** is specified|
|sourceNodeGroup|Particular environment layer within current environment|string|*cp* - application server<br>*bl* - load balancer<br>*nosqldb* - noSQL database<br>*sqldb* - SQl database<br>*cache* - cache node<br>*storage* - storage node|yes in case neither ***sourceNodeId***, nor ***sourceHost*** is specified|
|sourceHost|Public IP or domain of the external Data Storage server|string|*195.67.231.39*|yes in case neither ***sourceNodeGroup***, nor ***sourceNodeId*** is specified|
|readOnly|Defines *read only* or *read & write* rights for client node|boolean|*true* is *false* by default|no|

Example:
```
"volumeMaunts": {"/data": {"sourcePath": "/exported", "sourceNodeId": "693215", "readOnly": "true"}}
```
{{%/accordion%}}

* {{%accordion title="account volumes - list of nodes at the current account for the volumes to be imported from"%}}
|Name|Description|Type|Example Value|Mandatory|
|---|---|---|---|---|
|sourceNodeId|ID of storage container|integer|*81725*|yes, if ***sourceNodeGroup*** is not specified|
|sourceNodeGroup|Particular environment layer within current environment|string|*cp* - application server<br>*bl* - load balancer<br>*nosqldb* - noSQL database<br>*sqldb* - SQl database<br>*cache* - cache node<br>*storage* - storage node|yes, if ***sourceNodeId*** is not specified|
|volumes|List of volumes to export|string|*/volume*<br>If not specified, all volumes on a node will be exported|no|
|readOnly|Defines *read only* or *read & write* rights for client node|boolean|*true*(states in *false* by default)|no|

Example:
```
"volumesFrom": [{"sourceNodeGroup": "cp", "volumes": ["/master", "/local"], "readOnly": "true"}]
```
{{%/accordion%}}


## What's next?

* [API Overview](/api-overview/)
* [API Methods](https://www.virtuozzo.com/application-platform-api-docs/)
* [Platform CLI](/cli/)