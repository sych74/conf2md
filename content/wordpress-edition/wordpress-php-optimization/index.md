---
draft: false
title: "WordPress PHP Optimization"
aliases: "/wordpress-php-optimization/"
seoindex: "index, follow"
seotitle: "WordPress PHP Optimization"
seokeywords: "wordpress hosting, wordpress optimization, wordpress hosting optimization, wordpress php settings, wordpress php extensions, wordpress php.ini, wordpress php configs"
seodesc: "One of the major ways to improve your WordPress instance performance is to optimize your PHP setting for application servers. Boost your server performance by adjusting the main php.ini configuration file and reviewing the list of active extensions."
menu:
    docs:
        title: "WordPress PHP Optimization"
        url: "/wordpress-php-optimization/"
        weight: 70
        parent: "wordpress-edition"
        identifier: "wordpress-php-optimization.md"
---

# WordPress PHP Optimization

PHP-based application servers have multiple functions that allow you to fine-tune a project and achieve maximum performance and security. We recommend configuring several standard PHP functions to protect your server from harm. Of course, these are just basic tools that can complement the overall protection of your system. So, let's see how to perform some initial configurations to increase the security of your PHP environments.

The main PHP configuration file, named ***php.ini***, contains a number of default settings, which you can customize or even add new ones depending on your needs. The file is located in the **etc** directory of your PHP application server. It can be accessed and edited via the [embedded file manager](/wp-dashboard-project-management/#environment-management) directly in the dashboard. You can find it among the main configuration files in the *Favorites* tab.

![WordPress php.ini configuration](01-wordpress-phpini-configuration.png)

{{%note%}}**Note:** All directives and values in this guide are just recommendations. Before making any changes, refer to the official [PHP documentation](https://www.php.net/manual/en/ini.list.php) for additional information and ensure that the new value will benefit your particular project.{{%/note%}}

Follow the instructions below to analyze your configurations and apply the necessary changes.

1\. Some of the commonly used PHP configs are automatically redefined by the platform in the dedicated ***php.d/90-jelastic.ini*** file. Parameters in this file will override the same ones from the **php.ini** config. The following values are redefined by default:

```
upload_max_filesize = 100M
post_max_size = 100M
max_execution_time = 300
expose_php = Off
error_log = /var/log/litespeed/php_errors.log
memory_limit = 512M
```

![php.ini configs override](02-phpini-configs-override.png)

2\. Add the following string to disable the ***insecure functions***:

```
disable_functions = phpinfo, system, mail, exec
```

Additional security can be obtained by disabling the following functions:

```
disable_functions = exec,passthru,shell_exec,system,proc_open,popen,curl_exec,curl_multi_exec,parse_ini_file,show_source
```

![WordPress php.ini disable functions](03-wordpress-phpini-disable-functions.png)

3\. Amount of the ***allowed resources*** (if acceptable for your application):

- **max\_execution\_time = 30** - maximum script execution time (in seconds)
- **max\_input\_time = 60** - maximum time for request data parsing by each script
- **upload\_max\_filesize = 2M** - maximum size of uploaded file
- **memory\_limit = 8M** - maximum script memory amount (the default value is *128M*, but it is acceptable to set the lower one if it doesn't decrease your application performance)
- **post\_max\_size = 8M** - maximum POST data size acceptable for PHP

4\. You can ***restrict functions*** unnecessary for your application:

- **file\_uploads = Off** - disallow HTTP file uploads
- **display\_errors = Off** - disallow displaying the PHP error messages for the end-users
- **safe\_mode\_allowed\_env\_vars = PHP\_** - limit the external access to your PHP environment
- **expose\_php = Off** - restrict the sending back of PHP information
- **register\_globals = Off** - turn off the globals registration for input data
- **allow_url\_fopen = Off** - restrict remote files opening

5\. If needed, ***enable functions*** that give additional information about the security state:

- **cgi.force\_redirect = 0** - ensure appropriateness of PHP redirecting
- **log\_errors = On** - enable all possible errors logging

6\. Switch on the available ***safe modes***:

- **safe\_mode = On** - enable safe mode
- **sql.safe\_mode = On** - enable SQL safe mode

Once again, while specifying the above-mentioned settings, you should consider the requirements of your application. To apply the changes you've made, **Save** the file and **Restart** your PHP application server.


## PHP Extensions

The ***php.ini*** file contains a list of PHP extensions. Some of these modules are enabled for the server by default, while others can be activated manually when necessary. See the list of [PHP extensions](/php-extensions/) available by default at the linked doc.

If you wish to have an extension loaded automatically, use the following syntax:

```
extension={moduleName}
```

For example, "*extension=mysqli*".

{{%tip%}}**Tip:** You can provide custom extensions by uploading them into the default **modules** directory (**/usr/local/lsws/lsphp/lib64/php/modules**) and activating as usual or by specifying an absolute path to the library file:

```
extension=/path/to/extension/mysqli.so
```
{{%/tip%}}

Also, you can configure extensions by adjusting the predefined directives in the corresponding sections of the ***php.ini*** file (or by adding your own ones). In order to apply the changes, you need to **Save** the file and **Restart** your PHP application server node(s).


## What's next?

- [WordPress PaaS](/virtuozzo-application-platform-for-wordpress/)
- [WordPress Dashboard](/wp-dashboard-overview/)
- [WordPress Topologies](/wordpress-topologies/)
- [WordPress Backups](/wordpress-backups/)
- [WordPress Security](/wordpress-security/)