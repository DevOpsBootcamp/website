DevOps DayCamp Introduction
===========================

OSU OSL & OSU LUG

http://devopsbootcamp.osuosl.org/daycamp

What's DevOps?
--------------

.. figure:: /static/devops.jpg

Software Development + Operations Engineering

.. note:: -edunham-

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

.. note:: -edunham-
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

.. note:: jme

What you'll do:
---------------

.. note:: jme

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

.. note:: edunham

* Probably!
* No background knowledge needed
* Time commitment
    * Attend lectures
    * Play with what we teach you
    * You get out what you put in
* If in doubt... try anyway!

Career Paths:
-------------

.. note:: jme

* Hands-on learning & OSL reputation:
    * Internships
    * Industry connections
    * Start career with mid-level/high-level experience
    * Confidence and something unique to talk about in interviews
        * having your own ‘playground’ to experiment with

OSL Hiring:
-----------

.. note:: jme

* Students need basic skills to join
    * Systems engineers
    * Developers
    * Media
* Typically 2-3 years employment
* Alumni
    * Google, Rackspace, Intel, Microsoft, Mozilla, Facebook

Getting involved with Bootcamp
------------------------------

.. note:: edunham

* Find our site (http://devopsbootcamp.osuosl.org)
* Fill out registration with times available
* Join mailing list

This Session's Agenda
---------------------

.. note:: edunham

* Notation
* Vocabulary
* Virtual Machines
* Install your VM!

.. figure:: /static/Tux.png
    :align: right

A note about notation
---------------------

.. note:: edunham

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

.. note:: edunham

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

.. note:: jme

* Operating System (OS)
* Virtual Machine (VM)
* host
* guest
* virtualbox
* vagrant
* disk image
* vagrant box
* GNU/linux
* terminal/command line/cli

Operating System
----------------

.. note:: jme

* Kernel + Userland utilities
* Kernel manages things like:

  * hardware
  * processes
  * filesystems

* Userland utilities provide basic tools to make the system useful

Virtual Machine
---------------

.. note:: edunham

* The host creates some virtual hardware, and 'runs' the virtual hardware
* virtual hardware runs an operating system, which interacts with the virtual hardware
* Different virtual machines can be more or less virtualized than others

Host
----

.. note:: edunham

The physical machine on which the virtual machine runs

Examples:

  * Your laptop
  * Physical servers that cloud providers (AWS, Rackspace, DigitalOcean) run

Guest
-----

.. note:: edunham

The virtual machine.

Examples:

  * The virtual machine you are about to start up
  * A cloud instance

Virtualbox
----------

.. note:: jme

* Free and Open Source Software (FOSS) to manage and run virtual machines
* Originally written by Sun, now owned by Oracle
* Works well on Linux, OSX, and Windows (and even FreeBSD!)

Vagrant
-------

.. note:: jme

* A tool to manage virtual machines
* Works with lots of types of virtualmachines
* Uses a 'Vagrantfile' to manage machines
* Workflow looks like::

    $ vagrant init <box>
    $ vagrant up
    $ vagrant ssh

Disk Image
----------

.. note:: edunham

* a file which lives on the host that represents a disk to a VM
* delete it, and the hard drive on the VM disappears
* different formats exist, not always convertible

Vagrant Box
-----------

.. note:: edunham

* A disk image + vagrant metadata
* Allows you to copy a virtual machine and run it elsewhere
* Tied to backend vagrant uses (virtualbox for us)

GNU
---

.. note:: jme

.. figure:: /static/gnu.jpg
    :align: right

* Set of user-space tools needed to complete a basic operating system
* Started by Richard Stallman (rms)
* Maintained by the FSF (which is run by rms)
* Licensed under the GPL (which rms wrote)

Linux
-----

.. note:: jme

.. figure:: /static/Tux.png
    :align: left

* A kernel (and ONLY a kernel)
* Started by Linus Torvalds
* Licensed under the GPL

Trying Linux on a Virtual Machine
---------------------------------

.. note:: edunham

Virtual machines act as a full system on a physical machine

.. figure:: /static/virtualbox.png
    :align: right :scale: 50%

* Hypervisors:

    * VirtualBox (free) -- we will use this one
    * VMWare (mostly free)
    * KVM (Linux only hosts)
    * Parallels

* Public Cloud Virtual Machines

    * Amazon EC2, Rackspace Cloud, Google Compute Engine, etc

* Easy way to test without breaking your machine!

Installing Linux on Virtualbox
------------------------------

.. note:: jme

* Install virtualbox and vagrant from the USB drives
* Copy centos-6.5.box to your laptop
* Copy putty.exe to your laptop if you're on Windows.
* Get instructions for individual operating systems from the helpers

Vagrant & VirtualBox
--------------------

.. note:: jme

.. note::
  We're using CentOS as our base image for now but will use Debian later. You
  can see the gui by uncommenting the line in the Vagrantfile.

* Open a terminal and cd to the directory you copied the box file to.

  * Don't know what this means? Ask! We'll help!

.. code-block:: bash

    # add the box
    vagrant box add centos centos-6.5.box

    # initialize
    vagrant init centos

    # start vm
    vagrant up

    # log in
    vagrant ssh # windows users will use putty here

Vagrant cheat sheet
-------------------

.. note:: jme

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

.. note:: edunham

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

