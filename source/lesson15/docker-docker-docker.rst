Docker Docker Docker
====================

Docker docker docker. Docker docker. Docker.

.. figure:: /static/why_cant_i_hold_all_these_containers.png
    :align: center
    :width: 40%


Docker docker dock Docker?
--------------------------

|

.. figure:: /static/dockertopus.jpg
    :align: center
    :width: 60%


Docker!
-------

|

.. figure:: /static/docker_set_sail.jpg
    :align: center
    :width: 80%


A Practical Introduction to Containers
======================================

The actual talk.


What is a Container?
--------------------

  TLDR: One way to isolate a process without a virtual machine.

**[...] a server-virtualization method where the kernel of an operating system
allows for multiple isolated user-space instances, [...] may look and feel like
a real server from the point of view of its owners and users.**

* A form of process isolation.
* Implemented in one way or another since the late 80's ``(chroot)``.
* Used everywhere from servers to game consoles to your PC.


Upsides / Downsides to Containers?
----------------------------------

* ⬆ Faster to create and destroy than a virtual machine.
* ⬆ Less resource overhead as compared with Virtual Machines [citation needed].
* ⬇ Fairly new in popular use.
* ⬇ We need to iron out some problems.

.. figure:: /static/vm_vs_container.png
    :align: center
    :width: 70%
    :target: https://www.docker.com


What is Docker?
---------------

A very popular tool for working with container-like things.

An API for interacting with Docker containers.

.. code-block:: text

    $ docker run -it alpine:latest /bin/sh
    Unable to find image 'alpine:latest' locally
    latest: Pulling from alpine

    9d710148acd0: Pull complete
    Digest: sha256:24a36bbc059b1345b7e8be0df20f1b23caa3602e85d42fff7ecd9d0bd255de56
    Status: Downloaded newer image for alpine:latest
    / # cat /etc/alpine-release
    3.3.1
    / # echo "Pretty cool!"
    Pretty cool!
    / # exit


Docker is not Perfect
---------------------

There's a lot of security issues related to signing containers and trust. i.e.:
There is no way to verify a Docker Container is trustworthy.

Many of the problems with docker are addressed by `rkt`_; learning from the
experience of others, etc.

.. _rkt: https://coreos.com/rkt/docs/latest/


Further Reading
---------------

* `The wiki page on containers`_
* `docker documentation`_
* `rkt documentation`_

.. _The wiki page on containers: https://en.wikipedia.org/wiki/Operating-system-level_virtualization
.. _docker documentation: https://docs.docker.com/
.. _rkt documentation: https://coreos.com/rkt/docs/latest/


Activity
--------

This week's demo can be found here:

https://github.com/DevOpsBootcamp/Bootcamp-Exercises/tree/master/2015-2016/docker
