---
draft: false
title: "Environment Cloning"
aliases: "/cli-clone-environment/"
seoindex: "index, follow"
seotitle: "CLI Tutorial: Clone Environment"
seokeywords: "cli tutorial, cli guide, clone environment, cli clone environment, duplicate environment, copy environment, development environment, test environment "
seodesc: "See how to create a copy of your environment with a single CLI command. Subsequently, you can use this clone for testing or development purposes without affecting the original one."
menu: 
    docs:
        title: "Environment Cloning"
        url: "/cli-clone-environment/"
        weight: 4
        parent: "platform-cli"
        identifier: "cli-clone-environment.md"
---

# CLI Tutorial: Environment Cloning
The [environment cloning](/clone-environment) feature is also supported by CLI and can be easily called to help you in creation of new branches/multiple versions of your application. So, to duplicate your environment, just execute the next line:
```bash
~/jelastic/environment/control/cloneenv --appid  {src_env} --domain  {new_env}
```
where:

* ***{src_env}*** - name of the environment you'd like to clone
* ***{new_env}*** - name for your the environment copy

![CLI clone environment method](1.png)

In a few minutes, you'll get a new environment within your account, that is similar to the source one.


## What's next?
Learn some other popular CLI operations:

* [environment creation](/cli-create-environment/)
* [environment start/stop](/cli-environment-control/)
* [environment migration](/cli-environment-migration/)
* [server scaling](/cli-scaling/)
* [container redeploy](/cli-container-redeploy/)
* [Docker volumes](/cli-docker-volumes/)
* [mount points](/cli-mount-points/)
* [VCS projects deployment](/cli-vcs-deploy/)
* [swap Public IPs](/cli-ip-swap/)