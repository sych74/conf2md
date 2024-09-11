---
draft: false
title: "Tomcat Clustering"
aliases: ["/tomcat-server-clustering/", "/tomcat-clustering/"]
seoindex: "index, follow"
seotitle: "Tomcat Clustering"
seokeywords: "tomcat install, install tomcat server, tomcat clustered environment, server tomcat, replication tomcat, cluster tomcat, tomcat session replication, tomcat cluster, tomcat hosting, software clustering, tomcat replication, tomcat 6, tomcat 7"
seodesc: "See the step-by-step tutorial describing the technology of clustering used in the platform. Examine how to easily configure your own Tomcat application server cluster."
menu: 
    docs:
        title: "Tomcat Clustering"
        url: "/tomcat-server-clustering/"
        weight: 40
        parent: "tomcat-and-tomee"
        identifier: "tomcat-server-clustering.md"
---

# Tomcat Cluster in the Cloud

The platform multicast and redirecting requests to each server with load balancer provides session replication between the pairs of server nodes. This guarantees session exchange between the nodes through the local net and eliminates the need of additional software or Memcached. With this approach you can use a big clustered app hosting.

This instruction shows the clustering technology used in the platform by the example of the Tomcat app server.

![Tomcat cluster](01--tomcat-cluster.png)

The given scheme presents a **Tomcat cluster** with two servers and one load balancer. All requests are handled and distributed by the balancer between different nodes due to the availability and server load.

If one of the servers fails, the users from that node will be automatically switched to the other instance of this Tomcat cluster. Thanks to the replication, the other instance already has all the sessions of the failed node, so end-users never notice any change.

**To use the Tomcat clustering in the platform, you have to perform the next steps:**

1\. Log into your platform dashboard.

2\. Click **New** **Environment**.

![new environment button](00create.png)

3\. Pick **Tomcat** as the application server you want to use, specify the cloudlet limits and turn on **High-availability** as shown in the picture below. State the name of the environment and click **Create**.

![Tomcat cluster in topology wizard](01wizard.png)

{{%tip%}}**Note:** *Horizontal scaling* and *High Availability* mode are two different functionalities in the platform. With the first one you have multiple servers and the load is distributed evenly between the chosen number of instances with the load balancer. High Availability mode sets replication between pair or few pairs of servers using multicast membership.{{%/tip%}}

When you enable **High Availability** a special Tomcat config file (***jelastic-ha.xml***) is generated for each node by our system. Here is an example:

```xml
<Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"
      channelSendOptions="4">

<Manager className="org.apache.catalina.ha.session.DeltaManager"
      expireSessionsOnShutdown="false"
      notifyListenersOnReplication="true"/>

<Channel className="org.apache.catalina.tribes.group.GroupChannel">

 <Membership className="org.apache.catalina.tribes.membership.McastService"
       address="228.0.0.4"
       port="${MagicPort}"
       frequency="500"
       dropTime="3000"/>

 <Receiver className="org.apache.catalina.tribes.transport.nio.NioReceiver"
       address="${ReceiverIp}"
       port="4000"
       autoBind="100"
       selectorTimeout="5000"
       maxThreads="6"/>

 <Sender className="org.apache.catalina.tribes.transport.ReplicationTransmitter">
 <Transport className="org.apache.catalina.tribes.transport.nio.PooledParallelSender"/>
 </Sender>

 <Interceptor className="org.apache.catalina.tribes.group.interceptors.TcpFailureDetector"/>
 <Interceptor className="org.apache.catalina.tribes.group.interceptors.MessageDispatch15Interceptor"/>
</Channel>

 <Valve className="org.apache.catalina.ha.tcp.ReplicationValve"
     filter=""/>
 <Valve className="org.apache.catalina.ha.session.JvmRouteBinderValve"/>

 <ClusterListener className="org.apache.catalina.ha.session.JvmRouteSessionIDBinderListener"/>
 <ClusterListener className="org.apache.catalina.ha.session.ClusterSessionListener"/>
</Cluster>
```

Let's look through this file in details:

1\. This is the major element, inside which all the other cluster elements are configured.

```xml
<Cluster className="org.apache.catalina.ha.tcp.SimpleTcpCluster"
       channelSendOptions="4">
```

The ***channelSendOptions*** flag is attached to every message sent by ***SimpleTcpCluster*** class or any objects that are calling the ***SimpleTcpCluster.send*** method.

2\. The ***DeltaManager*** uses the ***SimpleTcpCluster.send*** method to send information though the channel.

```xml
<Manager className="org.apache.catalina.ha.session.DeltaManager"
     expireSessionsOnShutdown="false"
     notifyListenersOnReplication="true"/>;
```

3\. The group communication framework inside Tomcat is called **Tribes**. It is used as the channel element here. It encapsulates everything that relates the membership, logic and communication.

```xml
<Channel className="org.apache.catalina.tribes.group.GroupChannel">  
```

4\. Membership is made using **multicast**. Tomcat cluster separation consists of a multicast address and port number. Communication between nodes is realized over TCP.

```xml
<Membership className="org.apache.catalina.tribes.membership.McastService"
    address="228.0.0.4"
    port="${MagicPort}"
    frequency="500"
    dropTime="3000"/>
    <Membership className="org.apache.catalina.tribes.membership.McastService"
        address="228.0.0.4"
        port="${MagicPort}"
        frequency="500"
        dropTime="3000"/>
```

***{MagicPort}*** is a unique port number for the cluster, which is generated on the fly from the Java arguments.

5\. Tribes' logic of sending and receiving data includes two components: sender and receiver. The **Receiver** is responsible for data receiving. There is a thread pool in this element which has a ***maxThreads*** and ***minThreads*** setting. The address attribute is the host address that will be broadcasted by the membership component to the other nodes.

```xml
<Receiver className="org.apache.catalina.tribes.transport.nio.NioReceiver"
    address="${ReceiverIp}"
    port="4000"
    autoBind="100"
    selectorTimeout="5000"
    maxThreads="6"/>
```

6\. The **Sender** component is responsible for sending messages to other nodes. The Sender includes the ***ReplicationTransmitter***, a special shell component, and ***Transport*** sub component. Messages can be sent concurrently with the NIO sender and parallel with pool of senders.

```xml
<Sender className="org.apache.catalina.tribes.transport.ReplicationTransmitter">
<Transport className="org.apache.catalina.tribes.transport.nio.PooledParallelSender"/>
</Sender>
```

7\. The elements of the Tribes stack interceptors are:

* ***TcpFailureDetector*** - verifies crashed members via TCP
* ***MessageDispatch15Interceptor*** - dispatches messages to a thread pool to send message asynchronously

```xml
<Interceptor className="org.apache.catalina.tribes.group.interceptors.TcpFailureDetector"/>
<Interceptor className="org.apache.catalina.tribes.group.interceptors.MessageDispatch15Interceptor"/>
</Channel>
```

8\. The cluster uses valves to track requests to web applications:

* ***ReplicationValve*** finds out when the request has been completed and initiates the replication
* ***JvmRouteBinderValve*** is responsible for backing up your data

```xml
<Valve className="org.apache.catalina.ha.tcp.ReplicationValve" 
     filter="">
<Valve className="org.apache.catalina.ha.session.JvmRouteBinderValve"/>
```

9\. The ***SimpleTcpCluster*** is a sender and receiver of the Channel object, so components are registered as listeners to this cluster.

```xml
<ClusterListener className="org.apache.catalina.ha.session.JvmRouteSessionIDBinderListener"/>
<ClusterListener className="org.apache.catalina.ha.session.ClusterSessionListener"/>
```

High Availability configuration is automated so you can easily set it up for every Java app server supported by the platform.


## What's next?

* [Cluster in Cloud](/cluster-in-cloud/)
* [Tomcat](/tomcat/)
* [TomEE](/tomee/)