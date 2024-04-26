# Beta Release Notes

Issue date: March 12, 2024

Applies to: Beta

Build Number: 9.0.2-244

## 1. Overview

------------------------------------------------------------------------

Virtuozzo introduces the merging of Virtuozzo Hybrid Server 9 and OnApp features, which enables the management of virtual servers residing on Virtuozzo Hybrid Server 9 (RHEL9) based compute resources via a single unified UI.

## 2. New Features

------------------------------------------------------------------------

-   Virtuozzo Hybrid Server 9 (RHEL9) based compute resource support.
-   Integrated Virtuozzo backup and restore.
-   ReadyKernel live patching support for compute resource and backup nodes.
-   Support for next-generation VS templates with pre-installed guest tools.
-   AlmaLinux 9 OnApp Control Panel support.
-   Live migration between Virtuozzo Hybrid Server 9 compute resource nodes.
-   Self-service portal and infrastructure management in a single unified UI.
-   Advanced VS orchestration via a single REST API endpoint.

## 3. Known Issues

------------------------------------------------------------------------

-   Virtuozzo Storage must be configured via CLI. 
-   No migration supported from previous Virtuozzo Hybrid Server 7 or CentOS 7 KVM.
-   No unified installation media.
-   No support for the automatic update of guest tools on virtual servers.
-   Only one Windows virtual server can be created at a time.
-   The wrong operating system and virtualization may appear on the compute resource's Overview and Hardware pages in OnApp Control Panel.


