.. _operating_systems:


Lesson 2: Operating Systems
===========================

========= =====================================================================
Homepage  http://devopsbootcamp.osuosl.org
Content   FILL THIS IN
Slides    FILL THIS IN
Video     FILL THIS IN
========= =====================================================================

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What an Operating System is
        - Anatomy
        - Types of Operating Systems
    - Families of OS
        - UNIX
        - Windows
        - Linux
    - Flavors of Linux


What an Operating System is
---------------------------

.. image:: /static/operating-system-infographic.png
    :align: center
    :alt: The OS in relation to Hardware, Applications, and Users.
    :target: https://en.wikipedia.org/wiki/File:Operating_system_placement.svg

.. ifnotslides::

    An Operating System is the software which manages physical computing
    resources, interfaces between the hardware and the applications on a
    computer, and what exposes a creates a number of APIs for giving developers
    access to low-level applications / hardware.  The OS allows application
    developers and hardware manufactures to do their jobs and not worry about
    *"How does this spinning disk affect my browser"* and *"How will this
    networking card interact with my game engine"*.


Anatomy of an OS
----------------

.. image:: /static/anatomy-of-an-os.png
    :align: center
    :target: https://commons.wikimedia.org/wiki/File:Kernel_Layout.svg
    :alt: How the kernel fits into the OS stack.

.. ifnotslides::

    The OS is not *always* one thing or another.  Some Operating systems are
    behemoths while others are minimal.  Some are designed for teaching
    purposes while others are optimized for managing data centers.

    The general diagram, from **you -> hardware**, looks like this:

- **User Interface:** What you interact with.
- **Application Layer:** What developers use to make software run.
- **Kernel:** *The Core of the OS*.  Makes communication between hardware and
  applications sane.
- **Hardware:** What does the actual computations.

.. ifnotslides::

    The OS is what we call the middle two parts (Kernel and Application Layer)
    of that list.  The **Kernel** is the core of the OS that can vary in size.
    Some kernels are small (microkernels) while others are far-reaching
    (monolithic), each implements some amount of API between hardware and
    application, but it depends how much a given kernel takes responsiblity for
    based on what the developers want to be responsible for.


Types of Operating Systems
---------------------------

.. ifnotslides::

    Most of us only interact with one or two OS's in a day: our phone OS and
    workstation OS.  There are many other types of OS's depending on a variety
    of needs.  Scientific computing for instance has different requirements
    than a pace-maker or a GameBoy.  Each of these areas has their own *types*
    of applications they run and as a result they have specialized OS's to make
    those applications operate optimally.

    **Single/Multi-tasking**
        An OS may only need to run one task at a time while another OS needs to
        work on many tasks in parallel.

    **Single/Multi-user**
        Some OS host many users interacting with one-another.  More specialized
        OS don't need to handle that.

    **Embedded**
        A *very* simple OS capable of doing one job well. (Arduino, pace-maker,
        etc).

    **Real-time**
        For precise timing applications (e.g., life or death situations).

.. ifslides::

    *Each OS is not created equal (but they're usually made to do their job
    well!)*

    - **Single/Multi-tasking**
    - **Single/Multi-user**
    - **Embedded**
    - **Real-time**


Popular Operating Systems
-------------------------

.. ifnotslides::

    There are many popular (used daily by many people) Operating Systems out
    there.  The ones listed below all get the same jobs done (browsing the web,
    editing documents, playing games, etc), but they approach the problem in a
    **technically** or **philosophically** different way.

- UNIX

  - Linux

    - Andriod
    - Debian
    - RHEL

  - MacOS / Darwin
  - FreeBSD

- Windows

.. ifnotslides::

    The **UNIX family** of operating systems all implement the **POSIX
    standard** OS interafces, which has been around since ~1980.  POSIX is a
    very common standard of OS design which makes it easier to write one
    program that works on different (POSIX) operating systems.  This might not
    seem like such a big deal today but it was revolutionary in the 70's and
    80's.

    This isn't to say Windows is *bad* for being different, it implements a lot
    of interesting and smart designs of it's own, and it's mostly POSIX
    compliant!


GNU/Linux
---------

    *Welcome to the Family*

.. image:: /static/Tux.png
    :align: right
    :alt: Linux Tux Logo

.. image:: /static/gnu.jpg
    :align: left
    :alt: GNU Logo

.. ifnotslides::

    **Linux** is the *kernel* the powers many *flavors* of **GNU/Linux**.  Each
    flavor was created because of some *philosophical*, *technical*, or
    *social* difference in opinions with the existing flavors of Linux *on
    the market*.

    The reason some people call it **GNU**/Linux is because the OS you use is a
    Linux *kernel* with GNU *utilities* on top of it; things like basic
    command-line tools and other software that turns a *kernel* into a
    full-fledged *OS*.  We will flip-flop between calling this OS *GNU/Linux*
    and just *Linux* throughout this course, but we mean the former unless we
    are talking about *Linux Kernel*.

    GNU/Linux runs everything from smart-phones (Android) to the International
    Space Station (Debian) and Data Centers in between.


Flavors of Linux
----------------

.. ifnotslides::

    Variants (forks) of Linux Operating Systems are called *flavors*.  These
    are grouped into *families* based on their operating system ancestry.
    `More Information`_.

- Deian
    - Ubuntu
        - LinuxMint
- RedHat
    - RHEL
    - Fedora
    - Centos
- Gentoo
    - ChromeOS
        - CoreOS
- **Slackware**
- **ArchLinux**

.. _More Information: https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg


TODO
----

.. TODO: Add activity
.. TODO: Add answer key


Further Reading
---------------

OSU Courses:
    CS 344: Operating Systems I
        - Required course for all CS Students at OSU.
        - Covers fundamentals of low-level programming concepts.
            - Multi-threaded programming
            - Read / Write operations
            - Socket programming

    CS 444: Operating Systems II
        - Required course for all CS Students at OSU.
        - Covers kernel hacking and low-level OS design.
            - IO / Process scheduling
            - Building kernel modules
            - Memory management

.. TODO: Add more Further Reading for independent students.
