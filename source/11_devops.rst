Devops & Configuration Management Intro
========================================

Session Summary
---------------

- Devops introduction
- Configuration management introduction

Devops Introduction
===================

What is it?

  *"A software development method that stresses communication, collaboration and
  integration between software developers and information technology (IT)
  operations professionals."* [Wikipedia]

.. [Wikipedia] http://en.wikipedia.org/wiki/DevOps

Definition of Devops
--------------------

- Software Engineering (Dev)
- Technology Operations (Ops)
- Quality Assurance (QA)

.. figure:: static/Devops.svg
    :scale: 80%
    :align: center

    Wikipedia (cc)

The old view
------------

- **"Dev"** side being the *"makers"*
- **"Ops"** side being the *"people that deal with the creation after its
  birth”*

.. figure:: static/silo-fire.jpg
    :scale: 50%
    :align: right

    photo by http://thoriseador.deviantart.com/ (CC)

This siloed environment has created much harm in the industry and the core
reason behind creating Devops.

**Burn down those silos!**

History of Devops
-----------------

- mid-2000s

    "*Hey, our methodology of running systems seems to still be in a pretty
    primitive state despite years of effort.  Let’s start talking about doing it
    better"*

- Velocity Conf 2008/2009 - increased presentations on *"Agile System
  Administration*"
- Agile 2008 Conf - "Agile Infrastructure" BOF -- nobody showed up!
- 2009 DevOpsDays in Ghent, Belgium - Patrick Debois

The Agile Approach
------------------

- Iterative, incremental
- Requirements change often thus need to be adaptive
- Very short feedback loop and adaptation cycle
- Quality focus

Manifesto:

- *Individuals and interactions over processes and tools*
- *Working software over comprehensive documentation*
- *Customer collaboration over contract negotiation*
- *Responding to change over following a plan*

*That is, while there is value in the items on the right, we value the items on
the left more.*

Adapting Agile to Ops
---------------------

- Widening the principles towards infrastructure

  *"Infrastructure as code"* - i.e. configuration management

- Integrating ops with dev, QA and product in the product teams
- Continuous Integration

  *"Give your developers a pager and put them on call"*

- Utilizing more specific metric and monitoring schemes

Better Tools enable Devops
--------------------------

Explosion of new tools over the past few years:

  - Release tools (jenkins, travisci, etc)
  - Config Management (puppet, chef, ansible, cfengine)
  - Orchestration (zookeeper, noah, mesos)
  - Monitoring & Metrics (statsd, graphite, etc)
  - Virtualization & containerization (AWS, Openstack, vagrant, docker)

It's not NoOps
--------------

- Existing ops principles, processes and practices have not kept pace
- Business & dev teams need more agility to keep up with competitors
- Deep dev skill set + Deep ops skill set == awesomesauce
- Ops people need to do a little dev
- Dev people need to do a little ops

What is Devops Video
--------------------

.. raw:: html

    <iframe width="560" height="315" src="http://www.youtube.com/embed/_I94-tJlovg"
    frameborder="0" allowfullscreen></iframe>

Devops Explained: No Horse Manure
---------------------------------

.. raw:: html

  <iframe width="560" height="315" src="http://www.youtube.com/embed/g-BF0z7eFoU"
  frameborder="0" allowfullscreen></iframe>

Configuration Management
========================

What is it?

    *"Configuration management is the process of standardizing resource
    configurations and enforcing their state across IT infrastructure in an
    automated yet agile manner."* [PuppetLabs]

.. [PuppetLabs] http://puppetlabs.com/solutions/configuration-management

History of CM
-------------

- mid-1990s -- "snowflake system"; few systems
- Rise of Unix-like systems and commodity x86 hardware increased the need
- CFEngine -- First release 1993; v2 released in 2002
- mid-2000s through present

  - More agile CM systems emerged developed with the cloud in mind
- 2008

  - provisioning and management of individual systems were well-understood

Infrastructure as code
----------------------

- CM enables ops to define their infrastructure in *code*
- Install packages, configure software, start/stop services
- Ensure a state of a machine
- Ensure policies and standards are in place
- Provide history of changes for a system
- Repeatable way of rebuild a system
- Orchestrate a cluster of services together

CM Platforms
------------

- CFengine

  - Lightweight agent system. Manages configuration of a large number of
    computers using the client–server paradigm or stand-alone.
- Puppet

  - Puppet consists of a custom declarative language to describe system
    configuration, distributed using the client–server paradigm.

CM Platforms (part 2)
---------------------

- Chef

  - Chef is a configuration management tool written in Ruby, and uses a pure
    Ruby DSL for writing configuration "recipes". Also a client-server model.

- Ansible

  - Combines multi-node deployment, ad-hoc task execution, and configuration
    management in one package. Utilizes SSH with little to no remote agents.

Puppet Example
--------------

- Install apache and start the service
- Puppet Domain Specific Language (DSL)

.. code-block:: puppet

  package { "apache":
    name    => "httpd",
    ensure  => present,
  }

  service { "apache":
    name    => "apache",
    ensure  => running,
    enable  => true,
    require => Package["apache"],
  }

Chef Example
------------

- Install apache and start the service
- Ruby code

.. code-block:: ruby

  package "apache" do
    package_name "httpd"
    action :install
  end

  service "apache" do
    action [:enable, :start]
  end

CM Platform Comparison
----------------------

- CFEngine scales like mad, not very agile
- Puppet

  - Uses a list of dependencies and figures out what order to run it in
  - The Puppet DSL can become a blocker and a problem, puppet also has scaling
    issues
- Chef

  - Executes commands and scripts as they are listed with minimal amount of
    dependencies
  - Using ruby offers both its advantages and disadvantages
- Each platform offers its own level of complexity

References
----------

- http://theagileadmin.com/what-is-devops/
- http://itrevolution.com/the-convergence-of-devops/
- http://en.wikipedia.org/wiki/DevOps
- http://en.wikipedia.org/wiki/Agile_software_development
- `What is DevOps? - In Simple English (video)`__
- `DevOps Explained: No Horse Manure (video)`__

.. __: https://www.youtube.com/watch?v=_I94-tJlovg
.. __: https://www.youtube.com/watch?v=g-BF0z7eFoU


Traditional Development Workflow
--------------------------------

.. slide::

    .. figure:: static/devops/email1.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/email2.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/email3.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/email4.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/email5.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/email6.png
        :align: center
        :scale: 125%

DevOps Workflow
---------------

.. slide::

    .. figure:: static/devops/irc1.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/irc2.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/irc3.png
        :align: center
        :scale: 125%

.. slide::

    .. figure:: static/devops/irc4.png
        :align: center
        :scale: 125%
