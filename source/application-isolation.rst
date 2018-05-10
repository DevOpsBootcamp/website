.. _application_isolation:


Lesson 18: Application Isolation
================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/application-isolation.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/application-isolation.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - Application Isolation
    - Virtual Machines
    - Containers
    - Pros
    - Cons
    - Tools


Application Isolation
---------------------

.. ifslides::

    **The separation of one application stack from the rest of the computer**

.. ifnotslides::

    Application isolation is the separation of one program or application stack
    from the rest of the running processes.  The oldest way to do this is to
    simply run your application on a separate computer, but that gets very
    expensive very quickly.

    There are two main ways to tackle Application Isolation on one computer:
    Virtual Machines and Containers.  They both achieve similar end results
    but achieve that end in different ways and offer different advantages /
    disadvantages.


Virtual Machines
----------------

.. image:: /static/vm-diagram.png
    :align: center
    :alt: Anatomical Diagram of a VM
    :target: https://commons.wikimedia.org/wiki/File:Hardware_Virtualization_%28copy%29.svg
    :width: 50%

.. nextslide::

.. ifnotslides::

    Virtual Machines are programs that act like (or emulate) another computer
    (Also called a "guest") that's running on your physical computer (The
    "host").  This is useful because a VM completely isolates programs running
    from the host computer.

    Here is a demonstration showing the processes inside of a VM versus a host
    OS

::

    [vm] # ps aux
    USER PID %CPU %MEM    VSZ   RSS TTY STAT START   TIME COMMAND
    root   1  0.0  0.6 110564  3164 ?   Ss    2015  11:17 /lib/systemd/systemd --system --deserialize 15
    root   2  0.0  0.0      0     0 ?   S     2015   0:00 [kthreadd]
    root   3  0.0  0.0      0     0 ?   S     2015   3:55 [ksoftirqd/0]
    root   5  0.0  0.0      0     0 ?   S<    2015   0:00 [kworker/0:0H]
    [... 120+ more lines ...]

::

    [host] # ps aux
    USER  PID %CPU %MEM    VSZ   RSS TTY STAT START   TIME COMMAND
    root    1  0.0  0.1 200328  5208 ?   Ss   Aug25   0:44 /sbin/init
    root    2  0.0  0.0      0     0 ?   S    Aug25   0:00 [kthreadd]
    root    3  0.0  0.0      0     0 ?   S    Aug25   0:05 [ksoftirqd/0]
    root    5  0.0  0.0      0     0 ?   S<   Aug25   0:00 [kworker/0:0H]
    [... 240+ more lines ...]


OS Emulation
~~~~~~~~~~~~

.. ifnotslides::

    Let's talk about that emulation problem.  Imagine you are running a
    computer that has an X86_64 CPU on it.  You want to emulate a computer
    with an ARM5 CPU.  The emulated operating system makes system calls to the
    *'hardware'* it thinks it is running on.  The host operating system
    translates those system calls into *real* system calls on the *actual*
    hardware.  This translation is cost intensive and usually slow, but it's
    gotten a lot better over the decades.  When emulating a separate CPU
    architecture, optimizations usually have to be made for the emulated OS to
    be usable.

    **Note:** When you are emulating an X86_64 VM on an X86_64 piece of
    hardware, an optimization that can be made in which the host OS passes the
    system calls directly to the hardware without having to *translate*
    anything.  This is done by a *hypervisor* which enforces certain security
    protocols so the two operating systems (host and guest) are still isolated,
    but things go much faster.


Containers
----------

.. ifnotslides::

    Containers approach application isolation from a different angle.  Instead
    of emulating the guest OS, containers use the same kernel as the host but
    *lie* to the guest process and tell it that it's the only application
    running on that OS.  Containers bypass the emulation problem by avoiding
    emulation altogether. They run on the same hardware as the host OS but with
    a thin layer of separation.

    Containers have very become popular recently, but their underlying
    technologies aren't new.  Many application developers and system
    administrators have begun migrating toward using Containers over VMs as
    they tend to be more performant, but the industry as a whole is waiting
    for them to get a bit more battle-tested.

    Here is the previous demonstration in a container:

::

    [container] $ ps aux
    PID   USER     TIME   COMMAND
    1     root     0:00   sh
    6     root     0:00   ps aux

.. ifnotslides::

    As you can see, instead of emulating an entire OS (running 100+
    processes), the container is told that it's processes (``sh`` and ``ps``
    in this case) are the only one in this environment.  In theory this
    prevents a malicious attack from inside the container from invading the
    host OS.


Container Technologies
~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Containers are made possible by many underlying technologies that coexist
    both inside and outside of the Linux kernel.

    ``chroot``
        A program that allows you to only make part of a filesystem visible to
        another process by changing the root directory. Literally
        " ``ch`` ange ``root`` ".

    CGroups
        A linux kernel-level technology that name-spaces processes.  It performs
        many functions, but it's used by container engines to convince a process
        that it's running in its own environment.  This is what isolates a
        process from other processes, if they think they're the only thing
        running they can't tamper with the host OS.

    Systemd
        The service manager for most Linux distributions.  Systemd can be used
        to run and manage services such as web servers, but it can also limit an
        application's resource usage. This allows you to limit a container from
        using all of your computer's resources. In addition, many popular
        container management systems such as Docker run as services managed by
        Systemd.


Containers vs VMs
-----------------

.. image:: /static/hypervisor-vs-containers.png
    :align: center
    :alt: Diagram of Containers vs Virtual Machines


Pros
~~~~

======================================= =======================================
**Virtual Machines**                    **Containers**
--------------------------------------- ---------------------------------------
Complete process isolation              Fast startup
'Battle Tested'                         Little overhead
======================================= =======================================


Cons
~~~~

======================================= =======================================
**Virtual Machines**                    **Containers**
--------------------------------------- ---------------------------------------
Slightly more overhead.                 Security concerns.
Slow startup.                           No cross-kernel emulation.
Cross-kernel emulation.
======================================= =======================================

.. ifnotslides::

    Many of these concerns are temporary or negligible.  For instance, many
    organizations that run virtual machines aren't concerned with startup
    times.  And security concerns are a temporary issue in that the industry
    is already developing solutions for the existing security problems with
    containers.

    One of the major downsides to containers is that by definition they're
    restricted to using the host machine's kernel. This means that a Linux host
    cannot run a Windows container and vice-versa. The industry solution to this
    problem is to run a container in a small VM, since virtual machines can run
    any type of kernel on any host system.


Tools
-----

.. ifnotslides::

    There are a multitude of tools for using and managing VMs and Containers.

======================================= =======================================
**Virtual Machines**                    **Containers**
--------------------------------------- ---------------------------------------
VirtualBox                              Docker
VMWare                                  Rkt
======================================= =======================================


Virtual Machines
~~~~~~~~~~~~~~~~

.. ifnotslides::

    There are a lot of tools for managing Virtual Machines in many
    different ways.

VirtualBox
    An Open Source VM Manager.

    Widely used and supported on Linux, Mac, and Windows.

VMWare
    A closed source VM Manager.

    VMWare is a widely used and tends to have better performance than Virtual
    Box.  While it can emulate Linux it does not work natively on Linux.

KVM
    The Kernel-based Virtual Machine.

    Linux's native infrastructure for handling Virtual Machines and emulation.
    Usually used in a larger emulation program, not alone.


Containers
~~~~~~~~~~

.. ifnotslides::

    Containers have only recently gained popularity, but there are already many
    tools available for container management.

Docker
    The de facto CLI tool for creating and using containers.

    Very popular and well integrated into other tools.

RKT
    A competitor to Docker created by CoreOS.  Approaches container management
    from a different angle which has it's advantages and disadvantages.

``chroot``
    The *oldschool* way to use containers.  Not a container in the modern
    sense, but achieves similar process isolation.

Jails
    The BSD Unix form of containerization.  Offers a level of secure isolation
    not really possible in Linux.


TODO
----

.. TODO: Add activity.


Further Reading
---------------

`Docker`_

`RKT`_

.. _Docker: https://docs.docker.com/
.. _RKT: https://coreos.com/rkt/docs/latest/

.. TODO: Add further reading.
.. Suggested:
   - Docker docs
   - RKT Docs
   - Virtualbox docs
   - etc...
