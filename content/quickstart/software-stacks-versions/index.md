---
draft: false
title: "Software Stack Versions"
aliases: ["/software-stacks-versions/", "/supported-cartridges/"]
seoindex: "index, follow"
seotitle: "Software Stack Versions"
seokeywords: "software, versions, stacks, software versions, software stack versions, software stack, load balancers, application servers, database versions, software engines"
seodesc: "Here is a list of software stack versions and programming language engines available on the platform. Create platform-managed containers based on any of these software stack versions."
menu:
    docs:
        title: "Software Stack Versions"
        url: "/software-stacks-versions/"
        weight: 4
        parent: "quickstart"
        identifier: "software-stacks-versions.md"
---

# Software Stack Versions

Within this page, you can find a list of the latest software stacks and engines provided by the platform:

* [Load Balancers](#lb)
* [Application Servers](#app-servers)
* [Databases](#databases)
* [Additional Stacks](#additional)
* [Engines](#engines)

Each software stack remains supported by the platform up to the end-of-life (EOL) date notified by the respective upstream maintainer. After the EOL, stacks are no longer available for the new environment creation, but the already existing ones remain fully operable (including redeploy, cloning, horizontal scaling).

{{%tip%}}**Note:** Software stacks are based on the *CentOS 7* base image by default, which will reach EOL on 30th June 2024. The platform starts transitioning to the software stacks based on the new ***[AlmaLinux 9](/release-notes-83/#almalinux-9-base-os-image)*** images to ensure support of all the up-to-date functionality, modern security standards, and compatibility with all the latest software solutions.

Platform cartridges have officially reached EOL and will not receive updates anymore, including security patches and new platform functionality support (e.g. firewall UI).{{%/tip%}}

We highly recommend re-creating or [redeploying](/container-redeploy/) EOL containers with the up-to-date release of the software to ensure the availability of all the latest functionality and security fixes. Similarly, it is advisable to periodically (at least once per year) update all of your environments.

<a id="lb"></a>

{{%bug-fixes title="LOAD BALANCERS"%}}
Name & Link to Tags|Latest Supported Version
---|---
***[Apache Balancer](https://hub.docker.com/r/jelastic/apachebalancer/tags/)***|2.4.58<br>**AlmaLinux:** 2.4.62
***[HAProxy](https://hub.docker.com/r/jelastic/haproxy/tags)***|2.0.34; 2.2.31; 2.3.10; 2.4.24; 2.5.14; 2.6.16; 2.7.11; 2.8.5 2.9.0<br>**AlmaLinux:** 2.2.32; 2.4.26; 2.6.18; 2.8.10; 2.9.10; 3.0.4<br>**EOL: 1.8.14; 1.9.7; 2.0.10; 2.1.7**
***[LiteSpeed Web ADC](https://hub.docker.com/r/jelastic/litespeedadc/tags)*** ([HTTP/3](/http3/) ready)|2.4; 2.5.1; 2.6.1; 2.7; 3.0.3; 3.1.7<br>**AlmaLinux:** 3.2.2
***[NGINX Balancer](https://hub.docker.com/r/jelastic/nginxbalancer/tags)*** ([HTTP/3](/http3/) ready)|1.16.1; 1.18.0; 1.20.2; 1.22.1; 1.24.0<br>**AlmaLinux:** 1.26.2<br>**EOL: 1.10.3; 1.12.2; 1.14.2**
***[Varnish](https://hub.docker.com/r/jelastic/varnish/tags)*** ([HTTP/3](/http3/) ready)|6.0.11; 7.0.3; 7.1.2; 7.2.1; 7.3.0; 7.4.1<br>**AlmaLinux:** 6.0.13; 7.2.1; 7.3.1; 7.4.3; 7.5.0<br>**EOL: 4.1.8; 5.2.1; 6.1.1; 6.2.1; 6.3.2; 6.4.0; 6.5.1; 6.6.1**
{{%/bug-fixes%}}

<a id="app-servers"></a>

{{%bug-fixes title="APPLICATION SERVERS"%}}
Name & Link to Tags|Latest Supported Version
---|---
***[.NET Core](https://hub.docker.com/r/jelastic/dotnet/tags)***|3.1.426; 5.0.408; 6.0.417; 7.0.404<br>**AlmaLinux:** 6.0.425; 7.0.409; 8.0.401
***[Apache PHP](https://hub.docker.com/r/jelastic/apachephp/tags)***|2.4.57<br>**AlmaLinux:** 2.4.62<br>**EOL: 2.4.45**
***[Apache Python](https://hub.docker.com/r/jelastic/apachepython/tags)***|2.4.58<br>**AlmaLinux:** 2.4.62
***[Apache Ruby](https://hub.docker.com/r/jelastic/apacheruby/tags)***|2.4.58<br>**AlmaLinux:** 2.4.62
***[GlassFish](https://hub.docker.com/r/jelastic/glassfish/tags)***|5.0.0; 5.1.0; 6.1; 6.2.5; 7.0.11<br>**EOL: 3.1.2.2; 4.1.2**
***[Golang](https://hub.docker.com/r/jelastic/golang/tags)***|1.17.12; 1.18.10; 1.19.12; 1.20.12; 1.21.5<br>**AlmaLinux:** 1.20.14; 1.21.13; 1.22.7; 1.23.1<br>**EOL: 1.9.4; 1.10.3; 1.11.13; 1.12.17; 1.13.15; 1.14.15; 1.15.15; 1.16.15**
***[Jetty](https://hub.docker.com/r/jelastic/jetty/tags)***|9.4.53; 10.0.18; 11.0.18; 12.0.4<br>**AlmaLinux:** 11.0.22; 12.0.12
***[LEMP](https://hub.docker.com/r/jelastic/lemp/tags)*** *([HTTP/3](/http3/) ready)*|*LEMP* (NGINX / MariaDB / Redis / PHP)<br>*1.18.0* (1.18.0 / 10.6.12 / 6.2.5 / 8.0.10);<br>*1.20.2* (1.20.2 / 10.6.12 / 6.2.7 / 8.1.7);<br>*1.22.1* (1.22.1 / 10.6.12 / 6.2.11 / 8.2.5)<br>**AlmaLinux:**<br>*1.24.0* (1.24.0 / 10.6.16 / 6.2.14 / 8.3.2);<br>1.26.2 (1.26.2 / 10.6.18 / 6.2.14 / 8.3.10)
***[LiteSpeed Web Server](https://hub.docker.com/r/jelastic/litespeed/tags)*** *([HTTP/3](/http3/) ready)*|5.3.8; 5.4.12; 6.0.12; 6.1.2<br>**AlmaLinux:** 5.4.12; 6.1.2; 6.2.2; 6.3
***[LLSMP](https://hub.docker.com/r/jelastic/llsmp/tags)*** *([HTTP/3](/http3/) ready)*|*LLSMP* (LiteSpeed / MariaDB / Redis / PHP)<br>*5.4.12* (5.4.12 / 10.6.13 / 6.2.12 / 8.2.5);<br>*6.0.12* (6.0.12 / 10.6.11 / 6.2.8 / 8.2.0);<br>*6.1.2* (6.1.2 / 10.6.14 / 6.2.12 / 8.2.5)<br>**AlmaLinux:**<br>*6.2.2* (6.2.2 / 10.6.17 / 6.2.14 / 8.3.3)<br>*6.3* (6.3 / 10.6.18 / 6.2.14 / 8.3.6)
***[NGINX PHP](https://hub.docker.com/r/jelastic/nginxphp/tags)*** *([HTTP/3](/http3/) ready)*|1.18.0; 1.20.2; 1.22.1; 1.24.0<br>**AlmaLinux:** 1.24.0; 1.26.2<br>**EOL: 1.12.2; 1.14.2; 1.16.1**
***[NGINX Ruby](https://hub.docker.com/r/jelastic/nginxruby/tags)*** *([HTTP/3](/http3/) ready)*|1.16.1; 1.20.2; 1.22.1; 1.24.0<br>**AlmaLinux:** 1.24.0; 1.26.2<br>**EOL: 1.14.2**
***[NodeJS](https://hub.docker.com/r/jelastic/nodejs/tags)***|14.21.3; 16.20.0; 20.5.0<br>**AlmaLinux:** 18.20.4; 20.17.0; 21.7.3; 22.5.1; 22.8.0<br>**EOL: 6.17.1; 7.10.0; 8.17.0; 9.11.2; 10.24.1; 11.15.0; 12.22.9; 13.14.0; 15.14.0; 17.9.1**
***[Payara](https://hub.docker.com/r/jelastic/payara/tags)***|5.2022.2; 6.2023.12<br>**EOL: 4.1.2.181; 5.2020.5; 5.2021.10**
***[Spring Boot](https://hub.docker.com/r/jelastic/springboot/tags)***|2<br>**AlmaLinux:** 2
***[Tomcat](https://hub.docker.com/r/jelastic/tomcat/tags)***|8.5.97; 9.0.84; 10.0.23; 10.1.17; 11.0.0-M15<br>**AlmaLinux:** 8.5.100; 9.0.93; 10.1.28; 11.0.0-M24<br>**EOL: 7.0.109**
***[TomEE](https://hub.docker.com/r/jelastic/tomee/tags)***|7.0.5; 7.1.0; 8.0.16; 9.0.0; 9.1.1<br>**AlmaLinux:** 9.1.3
***[WildFly](https://hub.docker.com/r/jelastic/wildfly/tags)***|25.0.1; 26.1.3; 27.0.1; 28.0.1; 29.0.1; 30.0.1<br>**AlmaLinux:** 31.0.1; 32.0.1; 33.0.0<br>**EOL: 10.1.0; 11.0.0; 12.0.0; 13.0.0; 14.0.1; 15.0.1; 16.0.0; 17.0.1; 18.0.1; 19.1.0; 20.0.1; 21.0.2; 22.0.1; 23.0.1; 24.0.1**
{{%/bug-fixes%}}

<a id="databases"></a>

{{%bug-fixes title="DATABASES"%}}
Name & Link to Tags|Latest Supported Version
---|---
***[Couchbase CE](https://hub.docker.com/r/jelastic/couchbase/tags)***|5.0.1; 5.1.1; 6.0.0; 6.5.1; 6.6.0; 7.0.2; 7.1.1
***[MariaDB](https://hub.docker.com/r/jelastic/mariadb/tags)***|10.3.39; 10.4.32; 10.5.23; 10.6.16; 10.7.8; 10.8.8; 10.9.6; 10.10.6; 10.11.6; 11.0.4; 11.1.3<br>**AlmaLinux:** 10.5.25; 10.6.18; 10.11.8; 11.0.6; 11.1.5; 11.2.4; 11.3.2; 11.4.2<br>**EOL: 5.5.68; 10.1.24; 10.2.15**
***[MongoDB 3/4](https://hub.docker.com/r/jelastic/mongo/tags)*** *(deprecated)*|3.6.8; 4.0.2<br>**EOL: 2.6.12**
***MongoDB*** *([by request](/mongodb-license/))*|**AlmaLinux:** 6.0.16; 7.0.12
***[MySQL CE](https://hub.docker.com/r/jelastic/mysql/tags)***|5.7.44; 8.0.35<br>**AlmaLinux:** 8.0.36<br>**EOL: 5.6.50**
***[OpenSearch](https://hub.docker.com/r/jelastic/opensearch/tags)***|1.3.1; 2.11.1<br>**AlmaLinux:** 2.16.0
***[Percona](https://hub.docker.com/r/jelastic/percona/tags)***|5.7.43, 8.0.33<br>**AlmaLinux:** 8.0.36<br>**EOL: 5.5.41; 5.6.50**
***[PostgreSQL](https://hub.docker.com/r/jelastic/postgres/tags)***|11.19; 12.14; 13.10; 14.7; 15.2<br>**AlmaLinux:** 12.20; 13.16; 14.13; 15.8; 16.4<br>**EOL: 9.6.24; 10.22**
***[Redis](https://hub.docker.com/r/jelastic/redis/tags)***|6.0.10; 6.2.14; 7.0.11; 7.2.3<br>**AlmaLinux:** 7.2.4<br>**EOL: 4.0.11; 5.0.8**
{{%/bug-fixes%}}

<a id="additional"></a>

{{%bug-fixes title="ADDITIONAL STACKS"%}}
Name & Link to Tags|Latest Supported Version
---|---
***[AlmaLinux (VPS)](https://hub.docker.com/r/jelastic/almalinuxvps/tags)***|**AlmaLinux:** 9.3
***[CentOS (VPS)](https://hub.docker.com/r/jelastic/centosvps/tags)***|7.6; 7.7; 7.8; 7.9
***[Debian (VPS)](https://hub.docker.com/r/jelastic/debianvps/tags)***|10.13; 11.11; 12.7<br>**EOL: 9.13**
***[Docker Engine CE](https://hub.docker.com/r/jelastic/dockerce/tags)***|19.03.14; 20.10.23; 23.0.6; 24.0.7; 25.0.2<br>**AlmaLinux:** 26.1.2; 27.1.2<br>**EOL: 17.12; 18.09.7**
***[Jenkins](https://hub.docker.com/r/jelastic/jenkins/tags)***|2.332.3; 2.346.3; 2.361.4; 2.375.2; 2.387.1; 2.401.3; 2.426.3<br>**AlmaLinux:** 2.440.2<br>**EOL: 2.263.4; 2.289.3; 2.303.3; 2.319.3**
***[Kubernetes](https://hub.docker.com/r/jelastic/kubernetes/tags)***|1.16.6; 1.17.12; 1.18.10
***[Logstash](https://hub.docker.com/r/jelastic/logstash/tags)***|7.17.0; 8.11.3<br>**AlmaLinux:** 8.15.1
***[Maven](https://hub.docker.com/r/jelastic/maven/tags)***|3.5.4; 3.6.3; 3.8.6; 3.9.5<br>**AlmaLinux:** 3.9.9
***[Memcached](https://hub.docker.com/r/jelastic/memcached/tags)***|1.4.24; 1.5.22; 1.6.15<br>**AlmaLinux:** 1.6.31
***[OpenSearch Dashboards](https://hub.docker.com/r/jelastic/opensearchdashboards/tags)***|1.3.2; 2.11.1<br>**AlmaLinux:** 2.16.0
***[Pgpool-II](https://hub.docker.com/r/jelastic/pgpool2/tags)***|4.3.3; 4.4.4<br>**AlmaLinux:** 4.5.2
***[ProxySQL](https://hub.docker.com/r/jelastic/proxysql/tags)***|2.0.17; 2.3.2<br>**AlmaLinux:** 2.5.5<br>**EOL: 1.4.13**
***[Shared Storage](https://hub.docker.com/r/jelastic/storage/tags)***|2.0-9.6<br>**AlmaLinux:** 2.0-10.5
***[Ubuntu (VPS)](https://hub.docker.com/r/jelastic/ubuntuvps/tags)***|16.04; 18.04; 20.04; 22.04
***Windows*** (VPS)|2012
{{%/bug-fixes%}}

<a id="engines"></a>

{{%bug-fixes title="ENGINES" weight="100 300"%}}
Name|Latest Supported Version
---|---
***AdoptOpenJDK***|8.0.312; 11.0.13; 13.0.2; 14.0.2; 15.0.2; 16.0.2<br>**EOL: 9.0.4; 10.0.2; 12.0.2**
***Alibaba Dragonwell***|8.11.12
***Amazon Corretto***|8.392.08.1; 11.0.21.9.1; 15.0.2.7.1; 16.0.2.7.1; 17.0.9.8.1; 18.0.2.9.1; 19.0.2.7.1; 20.0.2.10.1; 21.0.1.12.1<br>**AlmaLinux:** 8.422.05.1; 11.0.24.8.1; 17.0.12.7.1; 21.0.4.7.1
***Eclipse OpenJ9***|*0.11.0* (8u192-b12; 11.0.1); *0.15.1* (8u222-b10; 11.0.4); *0.17.0* (8u232-b09; 11.0.5; 13.0.1); *0.18.1*(8u242-b08; 11.0.6; 13.0.2) *0.20.0* (8u252-b09; 11.0.7); *0.21.0* (8u262-b10; 8u265-b01; 11.0.8; 14.0.2); *0.22.0* (15.0.0); *0.23.0* (8u272-b10; 11.0.9); *0.24.0* (8u282-b08; 11.0.10); *0.25.0*-16; *0.26.0* (8u292-b10; 11.0.11); *0.27.0* (8u302-b08; 11.0.12); *0.29.0* (8u312-b07; 11.0.13); *0.30.0* (8u322-b06; 11.0.14); *0.32.0* (8u332-b09; 11.0.15); *0.33.1* (8u345-b01; 11.0.16); *0.35.0* (8u352-b08; 11.0.17); *0.36.1* (8u362-b09; 11.0.18); *0.38.0* (8u372-b07; 11.0.19); *0.41.0* (8u392-b08; 11.0.21)<br>**AlmaLinux:** *0.43.0* (8u402-b06; 11.0.22)<br>**EOL: *0.9.0* (9.0.4.12; 10.0.2); *0.15.1*-12.0.2**
***Eclipse Temurin***|8.0.392; 11.0.21; 17.0.9; 18.0.2.1; 19.0.2; 20.0.2; 21.0.0<br>**AlmaLinux:** 8.0.422; 11.0.24; 17.0.12; 21.0.2
***GraalVM CE***|19.3.1; 20.2.0; 21.3.0; 22.3.3
***Liberica JDK***|8.0.322; 11.0.14; 13.0.2; 14.0.2; 15.0.0; 16.0.0; 17.0.2<br>**EOL: 12.0.2**
***Oracle JDK Dev***|7.0_79; 8.0_202; 11.0.2<br>**EOL: 9.0.4; 10.0.2**
***Oracle OpenJDK***|7.0.261; 8.0.392; 11.0.21; 13.0.2; 14.0.2; 15.0.2; 16.0.2; 17.0.2; 18.0.2.1; 19.0.2; 20.0.2; 21; 22.ea-b29<br>**AlmaLinux:** 8.0.412; 11.0.24; 21.0.2; 22.0.2; 23.ea-b31<br>**EOL: 10.0.2; 12.0.2**
***Zulu Community***|7.0.352; 8.0.392; 11.0.21; 13.0.9; 14.0.2; 15.0.10; 16.0.2; 17.0.9; 18.0.2.1; 19.0.2; 20.0.2; 21.0.1<br>**AlmaLinux:** 8.0.422; 11.0.24; 17.0.12; 21.0.4; 22.0.2<br>**EOL: 12.0.2**
***PHP***|8.0.30; 8.1.24; 8.2.11<br>**AlmaLinux:** 8.0.30; 8.1.29; 8.2.23; 8.3.11<br>**EOL: 7.1.33; 7.2.34; 7.3.33; 7.4.33**
***Ruby***|3.0.6; 3.1.4; 3.2.2<br>**AlmaLinux:** 3.1.6; 3.2.5; 3.3.4<br>**EOL: 2.2.10; 2.3.8; 2.4.10; 2.5.9; 2.6.10; 2.7.8**
***Python***|3.8.18; 3.9.18; 3.10.13; 3.11.7; 3.12.0<br>**AlmaLinux:** 3.8.19; 3.9.19; 3.10.14; 3.11.9; 3.12.5<br>**EOL: 2.7.18; 3.4.10; 3.5.10; 3.6.15; 3.7.16**
***Node.js***|14.21.3; 16.20.0; 20.5.0<br>**AlmaLinux:** 18.20.4; 20.17.0; 21.7.3; 22.5.1; 22.8.0<br>**EOL: 6.17.1; 7.10.0; 8.17.0; 9.11.2; 10.24.1; 11.15.0; 12.22.9; 13.14.0; 15.14.0; 17.9.1**
***.NET***|3.1.426; 5.0.408; 6.0.417; 7.0.404<br>**AlmaLinux:** 6.0.424; 7.0.409; 8.0.303
***Go***|1.17.12; 1.18.10; 1.19.12; 1.20.12; 1.21.5<br>**AlmaLinux:** 1.20.14; 1.21.13; 1.22.7; 1.23.1<br>**EOL: 1.9.4; 1.10.3; 1.11.13; 1.12.17; 1.13.15; 1.14.15; 1.15.15; 1.16.15**
{{%/bug-fixes%}}


## What's next?

* [Java Versions](/java-versions/)
* [PHP Versions](/php-versions/)
* [Ruby Versions](/ruby-versions/)
* [Python Versions](/python-versions/)
* [Node.js Versions](/nodejs-versions/)