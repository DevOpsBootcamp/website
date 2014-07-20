Lesson 12: Configuration Management
===================================

.. note:: starting off with cs312 content

Large site management
---------------------

* Configuration Management
* Automation
* Centralized
* Standardization
* History

.. note:: 

    * Automating most of what you do
    * Scaling the configuration management is key
    * Centralized so that a team can work together
    * History via SCM (source control management)

What config management does
---------------------------

* Verify permissions for security/mgmt purposes
* Distribute config files and scripts
* Control batch jobs
* Ensure packages are up to date
* Look for file changes

.. note::

  Ensures that critical configs always are set like you want. No mucking around
  by a bad admin

Configuration Management
------------------------

* System-wide settings
    * sshd, ntp, ldap, etc
* Group settings
    * Web, email, database
* Standardize settings globally
* Easy to troubleshoot

CF Management Tools
-------------------

* CFEngine
    * Mature, widely used
* Puppet
    * Getting mature, different concept
* Chef
    * Very new

.. note:: Different concepts
    Feature set different between them
    Each have their own issues

Puppet
------

Let's install puppet

.. code-block:: bash

    $ yum install puppet

Declarative Configuration
-------------------------

* We 'declare' the desired state of the system
* Puppet does the necessary work to make the system match our declaration
* We can save these declarations in a repository, just like code

Puppet Resources
----------------

Puppet knows about "resources" on the system

.. code-block:: bash

    $ puppet describe -l

Look at all those things Puppet can manage out of the box. We're most interested
in these:

::

    file            - Manages files, including their content, owner ...
    group           - Manage groups
    package         - Manage packages
    service         - Manage running services
    user            - Manage users

Resources Have Attributes
-------------------------

.. code-block:: bash

    # let's look at the vagrant user
    $ sudo puppet resource user vagrant 

.. code-block:: puppet

    user { 'vagrant':
      ensure           => 'present',
      gid              => '500',
      groups           => ['wheel'],
      home             => '/home/vagrant',
      password         => '$1$aDsSD/Uu$.tXG5wN.TSit1AP5ZyphB0',
      password_max_age => '99999',
      password_min_age => '0',
      shell            => '/bin/bash',
      uid              => '500',
    }

We can declare a value for any of those attributes, and Puppet will make it
happen.

.. note::

  the password is a password hash, as appears in /etc/shadow - don't put
  passwords in puppet manifests!

Puppet Manifests
----------------

Puppet keeps its declarations in manifest files. We can write a manifest to
create a user:

.. code-block:: bash

    $ sudo su -
    $ vim users.pp

.. code-block:: puppet

    user {'yournamehere':
      ensure    => 'present',
      home      => '/home/yournamehere',
      groups    => ['wheel', 'vagrant'],
      shell     => '/bin/tcsh',
    }

Pull the Strings
----------------

Lets run our manifest.

::

    > puppet apply user.pp
    Notice: Compiled catalog for devops-bootcamp.osuosl.org in
    environment production in 0.12 seconds
    Notice: /Stage[main]/Main/User[yournamehere]/ensure: created
    Notice: Finished catalog run in 0.13 seconds

.. note:: we are using stand-alone mode, manually running an individual manifest

Declarations Are Idempotent
---------------------------

Lets run our manifest again.

::

    > puppet apply user.pp
    Notice: Compiled catalog for devops-bootcamp.osuosl.org in
    environment production in 0.12 seconds
    Notice: Finished catalog run in 0.02 seconds

The state of the system is already what we declared it should be, so applying
the manifest again doesn't change anything.

.. note::

  idempotency is important, the puppet master daemon will run periodically, and
  it is important that running the same commands over and over does not have
  cumulative effects

Packages and Services
---------------------

We can declare that our system should have certain things installed and running.

apache.pp:

.. code-block:: puppet

    package{'httpd':
        ensure => 'present'
    }

    service{'httpd':
        ensure => 'running',
        enable => 'true',
        require => Package['httpd'],
    }

.. note::

  The 'service' block makes sure that the httpd service is started, and that it
  is enabled, the 'require' directive tells the service that it must wait until
  the package 'httpd' is processed. Services are anything you would start with
  "service x start" and packages anything you would install with "yum install x"

Puppet Config
-------------

Where does Puppet keep its configuration files?

.. note:: the audience really ought to know where to start looking by this point

/etc/puppet
-----------

.. code-block:: bash

    $ ls /etc/puppet
    auth.conf  modules  puppet.conf

* ``puppet.conf`` - systemwide configuration
* ``auth.conf`` - puppet agent configuration
* ``modules`` - we'll talk about that later 

.. note::

  there isn't much of anything we need to worry about in any of the config files

The Site Manifest
-----------------

We want to move beyond running individual manifests on the command line.
'``/etc/puppet/manifests/site.pp``' is the place to put your site's
configuration.

.. code-block:: bash

    $ mkdir /etc/puppet/manifests
    $ vim /etc/puppet/manifests/site.pp


But First, Nodes
----------------

* Nodes are defined in the site manifest
* A node is a single machine, identified by its FQDN (Fully-Qualified Domain
  Name).
* You can define many nodes.
* You can add declarations to a node definition.
* A special 'default' node will be used if a node's name can't be found.

We will put our configurations in the default node for now.

.. note:: a node can inherit from another node, but this is discouraged


An Example Site Manifest
------------------------

.. code-block:: puppet

    node default {
        file {'/etc/issue':
            path    => '/etc/issue',
            mode    => 644,
            ensure  => present,
            content => "Welcome to the DevOps Bootcamp VM.\n",
        }

        package{'httpd':
            ensure => 'present'
        }

        service{'httpd':
            ensure => 'running',
            enable => 'true',
            require => Package['httpd'],
        }
    }

.. note::

  have we talked about /etc/issue? The file resource lets you declare the
  filename, ownership, and contents. You can also have it copy files from the
  module onto the node instead of manually inserting content here.

The Master and the Agent
------------------------

Puppet uses a Master/Agent architecture.

* The Master reads the '``site.pp``' and listens for an Agent to contact it.
* Agents run on nodes, they contact the master to get their configuration
* Master and Agent can be on the same machine.
* When they are on different machines, they need an SSL certificate to
  authenticate

Run the master on your vm:

.. code-block:: bash

    $ puppet master

.. note::

  the master will background by default and log to syslog, but you can run it in
  the foreground with --no-daemonize and get extra logging on stdout with
  --verbose

The Agent
---------

The agent will look for its master on the host '``puppet``' by default. Lets add
the hostname '``puppet``' to our local host definition in ``/etc/hosts``, so it
will look on the local machine.

.. code-block:: bash

    $ vim /etc/hosts

    127.0.0.1   devops-bootcamp.osuosl.org devops-bootcamp localhost 
    localhost.localdomain localhost4 localhost4.localdomain4 puppet
                                                             ^^^^^^

Now run the agent in test mode:

.. code-block:: bash
    
    $ puppet agent --test --verbose

.. note::

  the agent will also background by default, the --test flag prevents that and
  shows us what is going on. In a production environment, the master and agent
  would always be running in the background, usually started as services on
  boot.

Modules
-------

We can keep adding configurations to site.pp, but it's going to get long and
messy. Let's use modules instead.

* Modules are classes
* Modules encapsulate a set of related configurations
* Modules make it easy to apply configurations to many nodes
* Community created modules already exist for almost everything

.. note::

  community or puppetlabs modules vary in quality, always read the docs
  thoroughly

Module Structure
----------------

.. code-block:: bash

    /etc/puppet/modules/
                    modulename/
                        files/
                            some_file
                        manifests/
                            init.pp
                            some_other_manifest.pp

.. note::

  that files directory is served to the puppet agent like a fileserver, file
  resources can declare their source attribute like
  "puppet:///modules/module_name/some_file" and the file will be copied into
  place


The Bootcamp Apache Module
--------------------------

.. code-block:: bash

    # Let's create a module for our Apache configuration.
    $ cd /etc/puppet/modules
    $ mkdir bootcamp_apache
    $ mkdir bootcamp_apache/manifests
    $ vim bootcamp_apache/manifests/init.pp

.. code-block:: puppet
  
    class bootcamp_apache {
        package{'httpd':
            ensure => 'present'
        }
        package{'mod_wsgi':
            ensure => 'present'
        }
        service{'httpd':
            ensure => 'running',
            enable => 'true',
            require => Package['httpd'],
        }
    }

.. note::

  it is good practice to namespace the class name of your modules, so instead of
  just 'apache', we use bootcamp_apache, which won't collide with any other
  apache related module.

Site.pp Modularized
-------------------

.. code-block:: puppet

    node default {
        file {'/etc/issue':
            path    => '/etc/issue',
            mode    => 644,
            ensure  => present,
            content => "Welcome to the DevOps Bootcamp VM.\n",
        }

        include bootcamp_apache
    }

.. note::

  the include statement assumes a module located in modules/ under the pupper
  config dir. The name is the class name of the the module, which is not
  necessarily the directory name the module is stored under (but it is much
  easier to name them the same)

Community Modules
-----------------

We need MySql installed for our SystemView app, as well as a database, user, and
permissions. We could do all that with package, service and file resources, but
there is a better way, the puppetlabs-mysql module.

https://github.com/puppetlabs/puppetlabs-mysql

(It's in Git, how convenient!)

.. code-block:: bash

    $ cd /etc/puppet/modules/
    # We'll clone into a directory named mysql, because that's the module name
    $ git clone https://github.com/puppetlabs/puppetlabs-mysql.git mysql

We can include this module's class into our site manifest or our own modules.

The Bootcamp Mysql Module
-------------------------

We want to create a database and users, so lets make a module and not clutter up
the site.pp

.. code-block:: bash

    $ cd /etc/puppet/modules
    $ mkdir bootcamp_mysql
    $ mkdir bootcamp_mysql/manifests
    $ vim bootcamp_mysql/manifests/init.pp

.. code-block:: puppet

    class bootcamp_mysql {
        class { '::mysql::server' }
    }   

``::mysql::server`` causes Puppet to install MySql and makes available many
methods for managing MySql.

.. note::

  Calling the 'mysql' class essentially includes that module, which
  includes a package declaration insuring mysql is installed. It is easy to
  explore the module files and see what is in it.

Databases, Users, and Grants
----------------------------

.. code-block:: puppet

        class bootcamp_mysql {
            class { '::mysql::server' }

            mysql_database { 'systemview':
                ensure  => 'present',
                charset => 'utf8',
                collate => 'utf8_swedish_ci',
            }
            mysql_user { 'vagrant@localhost':
                ensure  => 'present',
            }
            mysql_grant { 'vagrant@localhost/systemview.*':
                ensure     => 'present',
                options    => ['GRANT'],
                privileges => ['ALL'],
                table      => 'systemview.*',
                user       => 'vagrant@localhost',
            }
        }

.. note:: the mysql module has a lot of stuff in it, there isn't time to get into it all.

Test It Out
-----------

.. code-block:: bash

    $ puppet agent --test --verbose

Further Reading
---------------

- http://docs.puppetlabs.com/learning/introduction.html
- https://github.com/puppetlabs/puppetlabs-mysql
