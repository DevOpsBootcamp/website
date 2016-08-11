.. _configuration_management:


Lesson 13: Configuration Management
===================================

.. code-block:: puppet

    user { 'audience':
      ensure  => present,
    }

What is it?
-----------

    *"Configuration management is the process of standardizing resource
    configurations and enforcing their state across IT infrastructure in an
    automated yet agile manner."*

    \- Puppet Labs

History of Configuration Management
-----------------------------------

The melting of special snowflakes

Infrastructure as code
----------------------

.. figure:: /static/config_mgmt/infra_as_code.png
    :align: right
    :height: 400px

- CM enables ops to define their infrastructure in *code*
- Install packages, configure software, start/stop services
- Ensure the state of a machine
- Provide history of changes for a system
- Repeatable way of rebuilding a system
- Orchestrate a cluster of services together

Push vs. Pull
-------------

- **Pull**

  - Clients poll a centralized master periodically for updates (Chef,
    Puppet, Cfengine)
  - Pros: Full automation capabilities, increased scalability
  - Cons: configuration management specific DSL, difficult to send immediate
    changes

- **Push**

  - Server calls client and can execute an immediate remote execution usually
    using ssh (Salt, Ansible)
  - Pros: Control, simplicity, can send commands immediately
  - Cons: Automation requires more work, Lack of scalability

Tools of the trade
------------------

So many options!

Puppet
------

- Puppet consists of a custom declarative language to describe system
  configuration, distributed using the client–server paradigm.

.. figure:: /static/config_mgmt/logo_puppet_labs.png
    :align: center
    :height: 300px

Chef
----

- Chef is a configuration management tool written in Ruby, and uses a pure Ruby
  DSL for writing configuration "recipes". Also a client-server model.

.. figure:: /static/config_mgmt/logo_chef.png
    :align: center
    :height: 300px

CFengine
--------

- Lightweight agent system. Manages configuration of a large number of computers
  using the client–server paradigm or stand-alone.

.. figure:: /static/config_mgmt/logo_cfengine.jpg
    :align: center
    :height: 300px

Ansible
-------

- Combines multi-node deployment, ad hoc task execution, and configuration
  management in one package. Utilizes SSH with little to no remote agents.

.. figure:: /static/config_mgmt/logo_ansible.png
    :align: center
    :height: 300px

Show me the magic!
------------------

*Real life code examples!*

Declarative Configuration
-------------------------

- We 'declare' the desired state of the system
- CM solution does the necessary work to make the system match our declaration
- We can save these declarations in a repository, just like code!

Puppet Example
--------------

.. figure:: /static/config_mgmt/logo_puppet_labs.png
    :align: right
    :height: 150px

- Install apache and start the service
- Configuration is called a 'manifest'
- Puppet DSL based on Ruby

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

.. figure:: /static/config_mgmt/logo_chef.png
    :align: right
    :height: 150px

- Install apache and start the service
- Configuration is called a 'recipe'
- Written as pure Ruby code

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

.. figure:: /static/config_mgmt/logo_ansible.png
    :align: right
    :height: 150px

- Install apache and start the service
- Configuration is called a 'playbook'
- Uses YAML file format for configuration

.. code-block:: guess

  - hosts: all
    tasks:
      - name: 1. Install Apache
        yum: name=httpd state=present
      - name: 2. Start Apache Service
        service: name=httpd state=running enabled=yes

You too can be a Sparkly DevOps Princess!
-----------------------------------------

.. figure:: /static/config_mgmt/devops_sparkly.png
    :align: center
    :height: 500px
