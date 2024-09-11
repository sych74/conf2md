---
draft: false
title: "Overview"
aliases: "/oom-killer-troubleshooting/"
seoindex: "index, follow"
seotitle: "OOM Killer Troubleshooting"
seokeywords: ""
seodesc: "When receiving an OOM killer load alert notification via email, the next step you should obviously take is to investigate the root cause of a happen problem and apply some resolution. To help you..."
menu: 
    docs:
        title: "Overview"
        url: "/oom-killer-troubleshooting/"
        weight: 1
        parent: "oom-killer-troubleshooting"
        identifier: "oom-killer-troubleshooting.md"
---

# OOM Killer Issues Troubleshooting

When receiving an OOM killer [load alert](/load-alerts) notification via email, the next step you should obviously take is to investigate the root cause of a happen problem and apply some resolution. To help you with that, we've already analyzed the most commonly met issues and defined the very efficient ways to fix them and prevent their occurrence in future.
The three main groups of processes are highlighted below:

* **[Common Cases](/oom-killer-common-cases)** - processes that are run by default on any platform container and can be killed by OOM tool
* **[Processes of High Risk](/oom-killer-leak-risk-processes)** - possible memory leaks, which require special actions or application code optimization; are sorted based on used stack type/program language, where each section provides the appropriate engine-related general recommendations, as well as kill resolutions for specific processes
* **[Non-Leaking Processes](/oom-killer-non-leaking-processes)** - operations that could be terminated by OOM killer though not representing the root of the problem; the general fix for all such issues is to restart a container in order to restore the corresponding processes

So, fetch the process name you've received within the appropriate email notification and look for it within the linked above documents to find out the required solution.