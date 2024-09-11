---
draft: false
title: "Common Cases"
aliases: "/oom-killer-common-cases/"
seoindex: "index, follow"
seotitle: "Common Cases"
seokeywords: ""
seodesc: "Examine the following table to get resolutions for some of the most common processes being killed by the OOM tool:ProcessResolutionadtRestart container in order to restore the..."
menu: 
    docs:
        title: "Common Cases"
        url: "/oom-killer-common-cases/"
        weight: 2
        parent: "oom-killer-troubleshooting"
        identifier: "oom-killer-common-cases.md"
---

# OOM Killer Resolutions: Common Cases

Examine the following table to get resolutions for some of the most common processes being killed by the OOM tool:

|Process|Resolution|
|---|---|
|*adt*|Restart container in order to restore the process|
|*cron*|Restart container in order to restore the process|
|*crond*|Restart container in order to restore the process|
|*expect*|Could be caused by *git fetch*, *git pull* or *git gc* processes (probably, due to the project big size or slow connection)|
|*git*|Initiate **Update from GIT** with the appropriate button next to your project in dashboard or just wait for the next [auto-deploy](/git-svn-auto-deploy/) being run (if enabled) to restore the *git* process automatically|
|*git-remote-http*|Could be caused by *git fetch*, *git pull* or *git gc* processes (probably, due to the project big size or slow connection)|
|*gitlab-projects*|Could be caused by *git fetch*, *git pull* or *git gc* processes (probably, due to the project big size or slow connection)|
|*jem*|Most likely, one of the latter operations you've performed via the platform dashboard (e.g. application deploy, SSL installation, engine change, etc.) haven't been accomplished - just initiate it one more time|
|*nscd*|Restart container in order to restore the process|
|*ssh*|Restart container in order to restore the process|
|*sshd*|Restart container in order to restore the process|
|*systemd*|Restart container in order to restore the process|
|*systemd-journal*|Restart container in order to restore the process|
|*taskrunner*|Restart container in order to restore the process|


## What's next?

* [OOM Killer Troubleshooting](/oom-killer-troubleshooting/)
* [Memory Leak Processes](/oom-killer-leak-risk-processes/)
* [Non-Leaking Processes](/oom-killer-non-leaking-processes/)
* [Auto-Deploy of Git Updates](/git-svn-auto-deploy/)