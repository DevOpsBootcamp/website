.. _daycamp_01:

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

Getting involved with BootCamp
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
* Setup with OpenStack VM
* HAVE FUN

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

.. note:: this might need to change

* Openstack login::

    ssh <usernumber>@daycamp.osuosl.org

.. _PuTTy: http://www.chiark.greenend.org.uk/~sgtatham/putty/

Essential Vocabulary
--------------------

.. note:: jme

* Operating System (OS)
* GNU/linux
* Server
* Host
* Guest
* Virtual Machine (VM)
* terminal/command line/cli

Operating System
----------------

.. note:: Mentioning the things on this page are enough, no need to overload

* Kernel + Userland utilities
* Kernel manages things like:

  * hardware
  * processes
  * filesystems

* Userland utilities provide basic tools to make the system useful

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

Server
------

A local or remote instance of an operating system typically used for shared
resoruces and/or shared applications.

Examples:
* Web Server (devopsbootcamp.osuosl.org)
* Shell Server (shell.onid.oregonstate.edu)
* File Server (dropbox)
* Game Server (WoW)

"The Cloud"

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

Virtual Machine
---------------

.. note:: edunham

* The host creates some virtual hardware, and 'runs' the virtual hardware
* virtual hardware runs an operating system, which interacts with the virtual
  hardware
* Different virtual machines can be more or less virtualized than others

Trying Linux in the Cloud
-------------------------

Need:
* SSH Client (PUTTY or OSX Terminal)
* Server (daycamp.osuosl.org)
* Login Credentials (usernumber + password)

For future reference you can use Local Virtual Machines to do the same thing.

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

Activities
----------

* Get setup with an OpenStack VM
* ``man man``
