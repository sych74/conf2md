---
draft: false
title: "NGINX Modules"
aliases: "/nginx-modules/"
seoindex: "index, follow"
seotitle: "NGINX Modules"
seokeywords: "php modules, nginx modules, available php module, enable module, php server modules, add module, default modules, config php module, nginxphp modules, default nginx modules"
seodesc: "Here is an instruction describing the full list of modules, available for NGINX PHP application server within the platform."
menu: 
    docs:
        title: "NGINX Modules"
        url: "/nginx-modules/"
        weight: 30
        parent: "nginx-php"
        identifier: "nginx-modules.md"
---

# Apache & NGINX Modules

Here you can see the full list of the Apache and NGINX modules available in the platform by default.

**Apache modules**

{{%table-without-head%}}
||||
|---|---|---|
|actions_module<br>(mod_actions)                            |cern_meta_module<br>(mod_cern_meta)            |mod_security            |
|alias_module<br>(mod_alias)|cgi_module<br>(mod_cgi)|negotiation_module<br>(mod_negotiation)|
|asis_module<br>(mod_asis)|dav_fs_module<br>(mod_dav_fs)|proxy_balancer_module<br>(mod_proxy_balancer)|
|auth_basic_module<br>(mod_auth_basic)|dav_module<br>(mod_dav)|proxy_connect_module<br>(mod_proxy_connect)|
|auth_digest_module<br>(mod_auth_digest)|deflate_module<br>(mod_deflate)|proxy_ftp_module<br>(mod_proxy_ftp)|
|authn_alias_module<br>(mod_authn_alias)|dir_module<br>(mod_dir)|proxy_http_module<br>(mod_proxy_http)|
|authn_anon_module<br>(mod_authn_anon)|disk_cache_module<br>(mod_cache_disk)|proxy_module(mod_proxy)|
|authn_dbm_module<br>(mod_authn_dbm)|env_module<br>(mod_env)|proxy_wstunnel_module<br>(mod_proxy_wstunnel)|
|authn_default_module<br>(mod_authn_default)|expires_module<br>(mod_expires)|rewrite_module<br>(mod_rewrite)|
|authn_file_module<br>(mod_authn_file)|ext_filter_module<br>(mod_ext_filter)|rpaf_module|
|authnz_ldap_module<br>(mod_authnz_ldap)|headers_module<br>(mod_headers)|setenvif_module<br>(mod_setenvif)|
|authz_dbm_module<br>(mod_authz_dbm)|include_module<br>(mod_include)|speling_module<br>(mod_speling)|
|authz_default_module<br>(mod_authz_default)|info_module<br>(mod_info)|ssl_module<br>(mod_ssl)|
|authz_groupfile_module<br>(mod_authz_groupfile)|ldap_module<br>(mod_ldap)|status_module<br>(mod_status)|
|authz_host_module<br>(mod_authz_host)|log_config_module<br>(mod_log_config)|suexec_module<br>(mod_suexec)|
|authz_owner_module<br>(mod_authz_owner)|logio_module<br>(mod_logio)|userdir_module<br>(mod_userdir)|
|authz_user_module<br>(mod_authz_user)|mime_magic_module<br>(mod_mime_magic)|usertrack_module<br>(mod_usertrack)|
|autoindex_module<br>(mod_autoindex)|mime_module<br>(mod_mime)|version_module<br>(mod_version)|
|cache_module<br>(mod_cache)|mod_geoip|vhost_alias_module<br>(mod_vhost_alias)
{{%/table-without-head%}}

**NGINX modules**

{{%table-without-head%}}
||||
|---|---|---|
|http_ssl_module|nginx-dav-ext-module|http_random_index_module|
|http_realip_module|headers-more-nginx-module|http_secure_link_module|
|http_flv_module|mod_geoip|http_stub_status_module|
|http_sub_module|mod_security|http_geoip_module|
|http_dav_module|file-aio|http_sub_module|
|http_gzip_static_module|http_addition_module|ipv6|
|nginx-sticky-module-1.1|http_flv_module|mail|
|nginx_tcp_proxy_module-master|http_mp4_module|mail_ssl_module|
{{%/table-without-head%}}

## What's next?
* [Add Apache Modules](/add-apache-modules/)
* [Apache WebDav Module](/apache-webdav-module/)
* [NGINX WebDav Module](/nginx-webdav-module/)
* [Apache as Frontend](/tomcat-behind-apache/)