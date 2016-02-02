Cloud Infrastructure
====================

*One* cloud, **two** cloud, *my* cloud, **your** cloud.

What The Cloud is
-----------------

    [...] a model for enabling ubiquitous, on-demand access to a shared pool of
    configurable computing resources

.. figure:: /static/cloud_computing.png
    :width: 65%
    :align: center
    :target: https://en.wikipedia.org/wiki/File:Cloud_computing.svg

What it looks like
------------------

.. figure:: /static/cloud_infra_shapes_and_sizes.png
    :width: 100%
    :align: center

Advantages over bare hardware
-----------------------------

Cloud Infrastructure allows you to abstract out *where* the application is
running and instead focus on more important tasks:

* Performance Optimizations
* Simplified Debugging
* Rapid Development / Deployment
* Easy Scaling

Private Cloud
-------------

    Infrastructure you run in-house to provide the advantages of cloud
    computing.

* Openstack
* CoreOS

Public Cloud
------------

    Shared resources provided by a third party for personal or corporate use.

* AWS
* Azure
* Compute Engine

Cloud + Configuration Management
--------------------------------

Many CM tools integrate directly, or have plugins to integrate with, Cloud
tools.

* Ansible modules
* Chef Server
* Puppet modules
* Hashicorp Atlas
* CoreOS Tectonic
* Google Kubernetes

Cattle vs Pets: Advantages
--------------------------

* Cut a release of your application.
* Spin up a VM on the cloud.
* Put your app on that VM and auto-deploy it.
* Everything upgrades with the click of a button.
* Relatively simple A/B Testing.

Cattle vs Pets: Disadvantages
-----------------------------

* Configuration Management is an expensive process.
* Only suitable for large infrastructures, knowing when to *start* can be tough.
* You just don't need the complexity Cattle Herding creates.

Virtual Machines vs Container
-----------------------------

Other Ways to Phrase the Argument:

Hypervisor vs Shared kernel
  The underlying technology behind each backend.

Security vs Performance
  Mostly a short-term problem, but something to consider.

Anouncement: This is a three part series
----------------------------------------

**Next Week** (02/11)
  CoreOS Speakers on Security, CoreOS, and Jobs.

**The Week After** (02/18)
  Spencer on OpenStack.

