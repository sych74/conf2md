---
draft: false
title: "A/B Testing"
aliases: "/ab-testing/"
seoindex: "index, follow"
seotitle: "A/B Testing"
seokeywords: "traffic distributor, ab test, compare app versions, compare conversion, smart load balancing, traffic manager, traffic distributor usage, ab testing, ab comparison, test applications, test conversion rate, compare application versions"
seodesc: "Compare two versions of your application with A/B testing using the Traffic Distributor solution. Analyze the obtained results to discover which version has a better conversion rate so it should be used in production to bring bigger revenue."
menu: 
    docs:
        title: "A/B Testing"
        url: "/ab-testing/"
        weight: 30
        parent: "traffic-use-cases"
        identifier: "ab-testing.md"
---

# A/B Testing with TD

Each commercial web-site or application has the embedded options of product purchase, sign up, conversion to paid version, subscription, etc. The amount of such actions, initiated by end-users (which, if being measured in percents, is called *[conversion rate](https://en.wikipedia.org/wiki/Conversion_marketing#Conversion_rate)*), is highly dependent on app's visual appeal, advertising texts and other marketing ploys used. Comparison of different application versions, aimed to designate which app version is better in confines of user's conversion rate, is named [A/B testing](https://en.wikipedia.org/wiki/A/B_testing). Such procedure can help you to find out the best combination of attractions and other product characteristics, that will allow to receive the highest revenue. 

With the help of [Traffic Distributor](/traffic-distributor/), you can easily apply such kind of testing to your projects - find the details below.

1\. To perform A/B testing, you'll need two different application examples to analyze, and any preferable type of monitoring to track the desired actions' calling (e.g. when a user clicks on the required button).

{{%tip%}}**Tip:** You can use any tool that allows to compare conversion rates, from a simple piece of code to count server's "score" (e.g. through just a variable incrementation) to some dedicated third-party testing utilities with a comfortable interface, analysis in graphs, automatic rates calculation, etc.{{%/tip%}}

2\. Next, [install](/traffic-distributor-installation/) your Traffic Distributor or just [configure](/traffic-distributor-installation/#traffic-distributor-reconfiguration) it correspondingly (if having one already created):

![Traffic Distributor configurations for A/B testing](01.png)

The obligatory points here are:

* **Routing method** - select *Sticky Sessions*
* **Traffic ratio** - set *50 to 50* to get the fair analysis

{{%note%}}**Notes:** 
* DO NOT use [Round Robin](/round-robin-traffic-routing/) routing for A/B testing, as this procedure assumes provision of different content on your backends, so some project elements may not be available on a particular server upon the request.
* In case you have the already-run production project, learn how to smartly [inject Traffic Distributor](/traffic-distributor-integration/) in front of it without interrupting application normal work.{{%/note%}}

3\. Everything is set up now, i.e. new incoming requests are evenly routed to both application versions with monitored conversion score. So just share your Traffic Distributor entry point link (i.e. environment domain or your [custom](/custom-domains/) one) among users and wait for some period of time for your customers to try out the given app versions and collect some data on conversions.

4\. Finally, analyse the results you've gathered to choose which project branch is more preferable for usage. Obviously, environment with higher *Conversion Rate* will win the race and can be boldly used in production, while the other one can be removed or just modified for another testing.

{{%tip%}}**Tip:** After you've revealed which app version is better, consider to follow the [Inject Traffic Distributor](/traffic-distributor-integration/) guide to start using it in a bundle with Traffic Distributor for achieving high availability and [failover protection](/failover-protection/).{{%/tip%}}


## What's next?

* [Traffic Distributor Overview](/traffic-distributor/)
* [Traffic Distributor Installation](/traffic-distributor-installation/)
* [Traffic Distributor Injection](/traffic-distributor-injection/)
* [Blue-Green Deploy](/blue-green-deploy/)
* [Failover Protection](/failover-protection/)