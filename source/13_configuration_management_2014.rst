Configuration Management History & Basics
=========================================

Configuration Management
------------------------

What is it?

    *"Configuration management is the process of standardizing resource
    configurations and enforcing their state across IT infrastructure in an
    automated yet agile manner."* `PuppetLabs`_

.. _PuppetLabs: http://puppetlabs.com/solutions/configuration-management

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

**CFengine**

* Lightweight agent system. Manages configuration of a large number of computers
  using the client–server paradigm or stand-alone.

**Puppet**

* Puppet consists of a custom declarative language to describe system
  configuration, distributed using the client–server paradigm.

CM Platforms (part 2)
---------------------

**Chef**

- Chef is a configuration management tool written in Ruby, and uses a pure Ruby
  DSL for writing configuration "recipes". Also a client-server model.

**Ansible**

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

Ansible Example
---------------

- Install apache and start the service
- Uses YAML file format for configuration

.. code-block:: yaml

  - hosts: all
    tasks:
      - name: 1. Install Apache
        yum: name=httpd state=present
      - name: 2. Start Apache Service
        service: name=httpd state=running enabled=yes

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

Push vs. Pull
-------------

* Pull

  * Clients poll a centralized master periodically for updates (i.e. Chef,
    Puppet, Cfengine)
  * Pros: Full automation capabilities, increased scalability
  * Cons: configuration management specific DSL, difficult to send immediate
    changes

* Push

  * Server calls client and can execute an immediate remote execution usually
    using ssh (i.e. Salt, Ansible)
  * Pros: Control, simplicity, can send commands immediately
  * Cons: Automation requires more work, Lack of scalability

DevOps workflow in an agency environment
----------------------------------------

Greg Lund-Chaix

Director of Technology

http://squishymedia.com


Tools @ Squishy
---------------

* GitLab & GitLab CI - http://gitlab.com
* Puppet - http://puppetlabs.com
* Vagrant - http://vagrantup.com

Workflow @ Squishy
------------------

Repository layout:

.. rst-class:: codeblock-sm

::

  [repo root]
  ├── .git
  ├── bin
  │   └── deploy.sh
  ├── core
  │   └── drupal-7.x
  ├── data
  ├── docs
  ├── htdocs -> core/drupal-7.x
  ├── private
  ├── README.md
  ├── tests
  │   ├── app
  │   └── e2e
  ├── vagrant
  │   ├── manifests
  │   └── modules
  └── Vagrantfile

Workflow @ Squishy
------------------

* Clone & create new branch
* Develop & test locally using Vagrant (if needed)
* Push to GitLab & create merge (pull) request to master

  - CI runs all tests in the tests directory on every push

* Code review by another team member, approve merge/pull request
* Push to master with all tests passing triggers a deploy to staging via bin/deploy.sh
* Deployment to production is currently manual

What works?  What doesn't?
--------------------------

* Puppet & Vagrant
* Code review
* CI & Drupal
