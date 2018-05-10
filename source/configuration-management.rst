.. _configuration_management:


Lesson 17: Configuration Management
===================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/configuration-management.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/configuration-management.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What is CM?
    - Infrastructure as Code
    - Push vs Pull
    - Tools
    - Declaration Configuration


Configuration Management
------------------------

    “Configuration management is the process of standardizing resource
    configurations and enforcing their state across IT infrastructure in an
    automated yet agile manner.”

    - Puppet Labs

.. ifnotslides::

    In short, Configuration Management is the concept of turning your server
    infrastructure into code.

    Setting up a server manually is cumbersome.  Installing your operating
    system, setting up users, copying files, installing packages, and all the
    other things you need to do to get a server up and running takes time and
    resources.  An alternative that has become popular in the past decade is
    writing code that allows you to state what you want to happen.  The
    infrastructure-as-code is written once and can be run on hundreds of
    thousands of servers and each machine will be setup exactly as the same as
    all the others.

::

    user { 'audience':
        ensure  => present,
    }


Short History of CM
~~~~~~~~~~~~~~~~~~~

In the beginning there were no computers.

Then many years passed and eventually we built the first computer.

Then a few years after that we had more computers than we really had time
to manage.  Things got out of hand pretty quick.

.. ifnotslides::

    Eventually system administrators were manually managing dozens, or even
    hundreds, of computers.  When a computer is manually managed it's called a
    *Special Snowflake*.  Special Snowflakes are setup manually and are very
    fragile.  Unfortunately companies like Facebook and Google can't scale
    *Special Snowflakes* quickly and easily, so they had to figure out a
    better solution.

    The answer was Configuration Management.  The earliest incarnations were
    **shell scripts** that you would run on a server, but those weren't
    perfect and required re-inventing the wheel quite a bit.  Eventually more
    standardized tools were created to solve this *Special Snowflake* problem
    in a way that scaled faster, iterated quicker, and worked more dependably.


Concept: Infrastructure as Code
-------------------------------

.. ifnotslides::

    Infrastructure as code is the act of describing what you want your servers
    to look like *once*, and using that to *provision* many machines to look
    the same. It turns *pets* into *cattle*.

    Pets (or *Special Snowflakes*) are servers you manage by hand and care very
    much about.  If a Pet dies it takes a while to get over, while you can get
    a new Pet it won't be the same and will take a while to potty-train.

    A Cattle is not important on it's own, all you care about is the herd.  If
    one cattle dies you've got dozens more -- you've still got a herd.
    Infrastructure as code allows you to treat servers like cattle instead of
    pets.

    Provisioning is running your CM code that tells the server what to install
    and which files to write, automatically doing what you would usually do
    manually.  This is much faster than a person doing it and is less error
    prone.


- Install packages, configure software, start/stop services.
- Ensure/guarantee a specific state of a machine.
- Provide history of changes for a system.
- Repeatable way of rebuilding a system.
- Orchestrate a cluster of services together.


Pull vs Push Models
-------------------

.. ifnotslides::

    Configuration Management tools tend to implement one (or both) of these
    models of management.  These are the *ways* a given configuration
    management tool actually *does the things* it has to do, like installing
    packages and writing files.

Pull Model
    Scales well but difficult to manage.

.. ifnotslides::

    - The server being provisioned (node) runs an agent (daemon) that asks a
      central authority (master) if/when it has any updates that it should run.

    - Requires a daemon to be installed on all machines *and* a central
      authority to be setup.

Push Model
    Simple to manage and setup but not scalable.

.. ifnotslides::

    - A central server contacts the nodes and sends updates as they are needed.

    - When a change is made to the infrastructure (code) each node is alerted
      of this and they run the changes.



Tools
-----

.. ifslides::

- Puppet
- Chef
- CFEngine
- Ansible
- Saltstack


Puppet
~~~~~~

.. image:: /static/logo_puppet_labs.png
    :align: right
    :alt: Puppet Logo

.. ifnotslides::

    Puppet (the software and company) has been around since 2005!  It's used
    by huge customers like WalMart and is known for it's stability.

- Uses custom CM Language.
- Primary Push Model.
- Widely Adopted.
- Very stable.
- Difficult to get setup.

.. ifnotslides::
    [ `Puppet Site`_ ]

.. _Puppet Site: https://puppet.com/


Chef
~~~~

.. image:: /static/logo_chef.png
    :align: right
    :alt: Chef Logo

.. ifnotslides::

    Chef has been around since 2009 and is most known for being configured via
    the Ruby programming language.  It has a very similar feature-set to
    Puppet.

- Primarily Push Model.
- Code files are Ruby.
- Widely Adopted.
- Difficult to setup.

.. ifnotslides::
    [ `Chef Site`_ ]

.. _Chef Site: https://www.chef.io/

.. ifnotslides::

    .. image:: /static/logo_cfengine.jpg
        :alt: CFEngine logo
        :align: center


CFEngine
~~~~~~~~

.. ifnotslides::

    CFEngine is a very old configuration management software (started in
    1993!) and is best known for being exceptionally fast and stable, but
    difficult to change / adapt quickly.

- Fast at execution, slow at adaptation.
- Very old.
- Stable.

.. ifslides::

    .. image:: /static/logo_cfengine.jpg
        :alt: CFEngine logo
        :align: center

.. ifnotslides::
    [ `CFEngine Site`_ ]

.. _CFEngine Site: https://cfengine.com/


Ansible
~~~~~~~

.. image:: /static/logo_ansible.png
    :alt: Ansible logo
    :align: right

.. ifnotslides::

    Ansible is notorously easy to setup and use.  It does not use a
    programming language to describe the state of software but declares the
    state of a machine with the ``yaml`` markup language.

- Easy to use.
- Easy to setup.
- Does not scale well.

.. ifnotslides::
    [ `Ansible Site`_ ]

.. _Ansible Site: https://www.ansible.com/


.. nextslide::


SaltStack
~~~~~~~~~

.. image:: /static/logo_saltstack.jpg
    :alt: Saltstack logo
    :align: right
    :scale: 70%

- Easy to use.
- Hard to get started.

.. ifnotslides::
    [ `SaltStack Site`_ ]

.. _SaltStack Site: https://saltstack.com/


Delcaration Configuration
-------------------------

.. ifnotslides::

    Declaration Configuration is the concept of declaring the state a machine
    *ought* to be in and letting the configuration management reach that state
    however it feels is appropriate.  This is advantageous because it can
    short-circuit a process by checking if it is already in that state before
    attempting to install/copy/configure a part of the system.

    Here is some Declaration Configuration pseudo-code:

::

    packages [nginx, python, vim]
        state installed
        update true

    service nginx
        state enabled
        alert service myapp_daemon

.. ifnotslides::

    In this case we used declaration configuration to install a list of
    packages and keep them updated.  We also enabled a service so ``nginx``
    will be run when the machine is turned on.  Lastly we told our
    pseudo-configuration-management to alert another service.  This means that
    there is a block somewhere else in the code for ``service myapp_daemon``
    which will always get run when the ``service nginx`` block gets run.


Chef Example
~~~~~~~~~~~~

- Install apache and start the service
- Configuration is called a ‘recipe’
- Written as pure Ruby code

.. code-block:: ruby

    package "apache" do
      package_name "httpd"
      action :install
    end

    service "apache" do
      action [:enable, :start]
    end

.. note::

    Since chef uses Ruby you can do loops and other cool Ruby-isms in your
    configuration management.  This can be a gift and a curse.


Puppet Example
~~~~~~~~~~~~~~

- Install apache and start the service
- Configuration is called a ‘manifest’
- Puppet DSL based on Ruby

::

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

.. note::

    Since Puppet designed its own language you are more limited in what you can
    express, but this isn't always a bad thing.  It's feature rich and can do
    pretty much anything that Chef can.


Ansible Example
~~~~~~~~~~~~~~~

- Install apache and start the service
- Configuration is called a ‘playbook’
- Uses YAML file format for configuration

.. code-block:: yaml

    - hosts: all
      tasks:

        - name: Install Apache
          yum:
            name: httpd
            state: present

        - name: Start Apache Service
          service:
            name: httpd
            state: running
            enabled: yes

.. note::

    Ansible's *language* is Yaml, which is basically JSON but easier to read
    and write.  This is similar to Puppet in it limits the possible
    functionality, but again: these tools all achieve the same result, they
    just get there in different ways.


Further Reading
---------------

- `Ansible's Documentation`_ is comprehensive and contains an easy-to-follow
  "Getting Started" guide.
- `Kitchen-CI`_ is a Chef oriented testing system
- `Puppet Learning VM`_ is a prebuilt VM for learning Puppet's fundamental
   concepts

.. _Ansible's Documentation: http://docs.ansible.com/ansible/
.. _Kitchen-CI: http://kitchen.ci/
.. _Puppet Learning VM: https://puppet.com/download-learning-vm
