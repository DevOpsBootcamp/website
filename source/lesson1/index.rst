.. _daycamp_01:


Lesson 1: DevOps Daycamp!
=========================

========= =========================================================
homepage: http://devopsbootcamp.osuosl.org/daycamp
content:  http://slides.osuosl.org/dobc/lesson1/first-steps.html
slides:   FILL IN THIS LINK
video:    FILL IN THIS LINK
========= =========================================================

Roadmap
-------

#. What is **DevOps**? DevOps **BootCamp**?
#. Why are we here?
#. Essential vocabulary.
#. Getting ready for activities.
#. First Activity.


What's DevOps?
--------------

.. figure:: /static/devops.jpg

Software Development + Operations Engineering

.. note::

    Development (writing software) + Operations (running servers)

    Pre-DevOps World: The jobs of Devs and Ops were seperate.

    * There was a clearly defined and relatively standardized interface between
      the two.
    * Workflows were slower, meaning ther was more time to troubleshoot/debug.

    Post-DevOps World: A new hybrid job emerges.

    * Software is released faster ("**Agile Development**")
    * Larger scale services = many identical servers ("**Configuration
      Management**").
    * Devs need to know ops for testing purposes to anticipate deployment
      issues.
    * Ops need to know dev to minimize wasted resources and to improve
      security.


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

    We will meet about Twice per month.


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

Getting involved with BootCamp
------------------------------

* Find our site (http://devopsbootcamp.osuosl.org)
* Fill out registration with times available
* Join mailing list

This Session's Agenda
---------------------

* Notation
* Vocabulary
* Virtual Machines
* Setup with OpenStack VM
* HAVE FUN

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

.. note:: this might need to change

* Openstack login::

    ssh <usernumber>@daycamp.osuosl.org

.. _PuTTy: http://www.chiark.greenend.org.uk/~sgtatham/putty/

Essential Vocabulary
--------------------

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

.. figure:: /static/gnu.jpg
    :align: right

* Set of user-space tools needed to complete a basic operating system
* Started by Richard Stallman (rms)
* Maintained by the FSF (which is run by rms)
* Licensed under the GPL (which rms wrote)

Linux
-----

.. figure:: /static/Tux.png
    :align: left

* A kernel (and ONLY a kernel)
* Started by Linus Torvalds
* Licensed under the GPL

Server
------

A local or remote instance of an operating system typically used for shared
resources and/or shared applications.

Examples:

* Web Server (devopsbootcamp.osuosl.org)
* Shell Server (shell.onid.oregonstate.edu)
* File Server (dropbox)
* Game Server (WoW)

"The Cloud"

Host
----

The physical machine on which the virtual machine runs

Examples:

  * Your laptop
  * Physical servers that cloud providers (AWS, Rackspace, DigitalOcean) run

Guest
-----

The virtual machine.

Examples:

  * The virtual machine you are about to start up
  * A cloud instance

Virtual Machine
---------------

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
