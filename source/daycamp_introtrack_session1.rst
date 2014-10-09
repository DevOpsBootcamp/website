DevOps DayCamp Introduction
===========================

OSU OSL & OSU LUG

http://devopsbootcamp.osuosl.org/daycamp

What's DevOps?
--------------

.. figure:: /static/devops.jpg

Software Development + Operations Engineering

.. note::

    development (write the software) + operations (run the servers)
    old paradigm: dev + ops discrete... this worked because

        * clearly defined interface between the two, relatively standardized
        * slower workflow means more time to troubleshoot/debug

    new paradigm:

        * software released faster ("agile")
        * larger scale = many identical servers
        * devs need to know ops for testing, anticipating deployment issues
        * ops need to know dev to minimize wasted resources, improve security

What's BootCamp?
----------------

* Started last year
* Free education program
    * Mentorship
    * Apprenticeship
    * Hands-on training
* NOT:
    * OSU class for credit
    * student job

.. note::
    meet every 1-2 weeks through the term
    time decided by Doodle poll
    you get out what you put in
    skills etc. to do well in job interviews (especially ops)

Why are we doing this?
----------------------

* OSL's move to EECS
* Bridge the “Skills Gap”
* Demand from companies for students
* Build community

What you'll do:
---------------

* Learn:
    * Linux systems
    * Networking
    * Software development
    * ...and the other skills you’ll need
* Build:
    * Duplicate internet infrastructure
    * Graduate to helping with OSL tasks
        * work with real open source projects
        * solve real problems

Can you do it?
--------------

* Probably!
* No background knowledge needed
* Time commitment
    * Attend lectures
    * Play with what we teach you
    * You get out what you put in
* If in doubt... try anyway!

Career Paths:
-------------

* Hands-on learning & OSL reputation:
    * Internships
    * Industry connections
    * Start career with mid-level/high-level experience
    * Confidence and something unique to talk about in interviews
        * having your own ‘playground’ to experiment with

OSL Hiring:
-----------

* Students need basic skills to join
    * Systems engineers
    * Developers
    * Media
* Typically 2-3 years employment
* Alumni
    * Google, Rackspace, Intel, Microsoft, Mozilla, Facebook

Getting involved with Bootcamp
------------------------------

* Find our site (http://devopsbootcamp.osuosl.org)
* Fill out registration with times available
* Join mailing list

This Session's Agenda
---------------------

* Notation
* Vocabulary
* Virtual Machines
* Install your VM!

.. figure:: /static/Tux.png
    :align: right

A note about notation
---------------------

.. figure:: /static/stickynote.png
    :align: right
    :scale: 20%

* Variables
    * ``$varname``
    * ``<varname>``
* Shell prompt
    * ``$``
    * ```literal stuff in backticks```
* metasyntactic variables: foo, bar, baz, username, etc.

How to get (to) Linux
---------------------

.. figure:: /static/dualboot.png
    :align: right
    :scale: 40%

* How many have it already installed?
* Install VM or dual-boot
* When stuck on Windows, use `PuTTy`_:
* Students::

    ssh <onidusername>@shell.onid.oregonstate.edu


.. figure:: /static/osm_server.jpg
    :align: right
    :scale: 50%

* flip{1-3} are Engineering servers; less reliable

.. _PuTTy: http://www.chiark.greenend.org.uk/~sgtatham/putty/

Essential Vocabulary
--------------------

Operating System
Virtual Machine
host
guest
virtualbox
vagrant
disk image
vagrant box
GNU/linux
terminal/command line/cli

Trying Linux on a Virtual Machine
---------------------------------

Virtual machines act as a full system on a physical machine

.. figure:: /static/virtualbox.png
    :align: right
    :scale: 50%

* Hypervisors:
    * VirtualBox (free)
    * VMWare (mostly free)
    * KVM (Linux only hosts)
    * Parallels
* Public Cloud Virtual Machines
    * Amazon EC2, Rackspace Cloud, Google Compute Engine, etc
* Easy way to test without breaking your machine!

Installing Linux on Virtualbox
------------------------------

.. note:: 
  Try other distributions if you like to see what's different. Debian is a great
  next step to try out.

#. Download and install: https://www.virtualbox.org/wiki/Downloads
#. Grab the latest minimal ISO: http://centos.osuosl.org/6/isos/x86_64/
#. Create VM
    #. New -> Name "CentOS" -> Default Ram -> Default Disk settings
    #. Settings -> Storage -> Empty -> CD/DVD Drive -> Select ISO
    #. Start -> press enter -> Skip media check
#. ``\o/``

Vagrant & VirtualBox
--------------------

.. note::
  We're using CentOS as our base image for now but will use Debian later. You
  can see the gui by uncommenting the line in the Vagrantfile.

* Vagrant is a tool used with Virtualbox (and other) platforms
* Make a reproducible pre-installed Linux environment
* Download and install: http://www.vagrantup.com/
* Clone our repo, start and access the vm:

.. code-block:: bash

    # clone
    git clone https://github.com/DevOpsBootcamp/devopsbootcamp-vagrant.git

    # start up
    cd devopsbootcamp-vagrant
    vagrant up

    # access vm
    vagrant ssh

Vagrant cheat sheet
-------------------

.. note::
  We'll get into more detail later in how you can access ports on your VMs and
  other use cases.

.. code-block:: bash

    # start
    vagrant up

    # stop
    vagrant halt

    # destroy (remove vm)
    vagrant destroy

    # ssh to the vm
    vagrant ssh

Also check out the `Vagrant Documentation
<http://docs.vagrantup.com/v2/cli/index.html>`_ for more information.

The Terminal
------------

.. figure:: /static/crashcart.jpg
    :align: right
    :scale: 75%

* Used to mean the keyboard+monitor
    * Now that's a crash cart
* Terminal emulator
* Shell: Use bash; others include csh, zsh, tsch
    * ``~/.bashrc``

.. figure:: /static/televideo_terminal.jpg
    :align: right
    :scale: 40%

.. figure:: /static/teletype_terminal.jpg
    :align: left

