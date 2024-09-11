---
draft: false
title: "Add SSH Key"
aliases: "/ssh-add-key/"
seoindex: "index, follow"
seotitle: "Add SSH Key"
seokeywords: ""
seodesc: "When you have your SSH key generated, you can add it to your PaaS account.In order to manage private SSH keys intended for authentication at your GIT account, follow the corresponding instruction..."
menu: 
    docs:
        title: "Add SSH Key"
        url: "/ssh-add-key/"
        weight: 30
        parent: "ssh"
        identifier: "ssh-add-key.md"
---

# Add SSH Key
When you have your [SSH key generated](/ssh-generate-key), you can add it to your PaaS account.
{{%tip%}}
In order to manage private SSH keys intended for authentication at your GIT account, follow the corresponding instruction within the [SSH Access to GIT Repository](/git-ssh#add-private) guide.
{{%/tip%}}For adding a public SSH key, which subsequently can be used for gaining [SSH access](/ssh-access) to your PaaS account, proceed to the steps below:

1\. Open the platform dashboard and navigate to the upper toolbar.
![ssh add key 5fe565698fc97a20f4c60d3918356107settings button](5fe565698fc97a20f4c60d3918356107settings-button.png)
Click the **Settings** button.

2\. The **Account setting** tab with the already selected **SSH Keychain** option will be opened.
![ssh add key ssh keychain](ssh-keychain.png)

Within this section you can find some information about the SSH protocol usage at the platform and the possibilities it provides with a few useful links to documentation.

3\. Once you are acquainted with the details above, switch to the **Public** suboption and click the **Add Public Key** button.
![ssh add key public](public.png)

4\. Paste the previously generated public key to the **Key** input field. The **Add Public Key** field will be automatically populated if your key already contains this value (or you can specify your own one here). 
Click **Add Key**.
![ssh add key add key](add-key.png)

5\. As a result, the added SSH key will appear in the list, while you'll simultaneously receive an email with details on it (like title, fingerprint and connection string for your SSH client).
![ssh add key public key list](public-key-list.png)

In this way, you can add several keys or delete the unnecessary ones using the red-cross button.
{{%tip%}}**Note:** The added SSH key is attached to your account, but not just to a separate environment.{{%/tip%}}

## What's next?
* [SSH Overview](/ssh-gate/)
* [Generate SSH Key](/ssh-generate-key/)
* [Web SSH](/web-ssh-client/)
* [SSH Gate](/ssh-gate-access/)
* [SSH Management](https://www.virtuozzo.com/company/blog/ssh-to-container/)