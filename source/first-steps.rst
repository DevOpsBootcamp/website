.. _first_steps:


Lesson 1: First Steps
=====================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/first-steps.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/first-steps.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - Vocabulary
    - Notation
    - Setup Development Environments
    - Have Fun!

    .. image:: /static/Tux.png
        :align: center


Vocabulary
----------

    **A 10,000ft view of the world**


.. ifnotslides::

    Below are a few terms we will be using and a brief definition:

General Topics:
    - **Software:** A program that runs on a computer.
    - **Operating System:** Computer software that manages other software.
    - **GNU/Linux**: A *free* Operating System.
    - **Computer Security:** Like physical security but harder to solve with a
      baseball bat.
    - **Virtual Machine:** A computer emulated in software.
    - **Containers:** Not virtual machines, but basically virtual machines.

.. nextslide::

Development:
    - **Version Control:** A way to track changes and contributions to a
      project.
    - **Continuous Integration:** Releasing updates *continuously*.

Buzzwords:
    - **FOSS:** Free (and Libre) Open Source Software.  Free as in Speech, not
      Free as in Pizza (but that too usually).
    - **'The Cloud':** Computers somewhere else.
    - **Docker:** Software that manages Linux containers

Notation
--------

.. ifnotslides::

    Some notes about notation...

    Just like a textbook, we have some unique notation you should be aware of.
    The following is a short list of key notation used in DOBC.

- Variable (use whatever word you like here e.g., foo, bar, baz)

.. code-block:: bash

    $ONE_VARIABLE_NOTATION
    <another notation for variables>

- Literal (copy this exactly): ``copy_me_exactly``

- Comments (parts of the code just for humans)

.. code-block:: bash

  this_is(code)  # everything after the octothorp is a comment!

.. code-block:: java

  other_code(line)  // This can also be a comment. It depends on the
                    // language!

.. ifnotslides::

    We try to write code-blocks so you can copy them verbatim into a file or
    into your terminal and hit *Enter* to see it run (unless it's psuedo code!)

    Every language has it's own comment symbol.  The common ones are ``#``,
    ``//``, and ``/* ... */`` .  If you see that in a code-block it denotes a
    comment block.

.. nextslide::

Code-block:

.. code:: python

    #! /usr/bin/env python
    # This is a code block.
    # Most of the time you can copy this code and run it exactly as is.
    # It should be clear Where it 'goes' and how to run it based on
    # context.
    print('Hello world!')

.. ifnotslides::

    *You can copy the above script into a file named* ``<whatever you
    want>.py`` *and run it with* ``python <whatever you want>.py``

    Shell commands are annotated with a ``$``. For instance:

.. code-block:: bash

    # Copy the text after `$` into your terminal & press enter.
    $ echo Hello World


Exercise: Reading Examples
~~~~~~~~~~~~~~~~~~~~~~~~~~

    *Trick question: how would you read this*

.. code-block:: python

    #!/bin/python
    dogs = ['$BREED_ONE', '$BREED_TWO', '$BREED_THREE']
    for breed in dogs:
        print(breed)

.. rst-class:: build

  Actually prints...

  .. code-block:: console

      $BREED_ONE
      $BREED_TWO
      $BREED_THREE

Answer: Reading Examples
~~~~~~~~~~~~~~~~~~~~~~~~

Replace the ``$BREED_N`` with actual dog breeds.

.. code-block:: python

    #!/bin/python
    dogs = ['corgie', 'pug', 'french bulldog']
    for breed in dogs:
        print(breed)

.. rst-class:: build

  Actually prints...

  .. code-block:: console

      corgie
      pug
      french bulldog

SSH: Secure Shell
-----------------

.. rst-class:: build

- Secure Shell (SSH) provides a secure channel to access a Linux machine remotely via command line.
- It's a primary tool for almost every DevOps engineer
- Designed as a replacement to Telnet which provides unsecured remote shell access
- Allows for password logins and private/public key-based logins which are more secure
- Some tricks you can do with SSH

  - Run a single command remotely
  - Secure file transfer (via ``scp`` or `WinSCP`_)
  - Port forwarding, SOCKS proxy or tunnel
  - `SSHFS`_ -- userspace filesystem which uses SSH

.. _WinSCP: https://winscp.net/eng/download.php
.. _SSHFS: https://github.com/libfuse/sshfs

Getting Setup on Linux
----------------------

.. ifnotslides::

    If you are taking the course exclusively online you will need setup Docker on your own computer. For more
    information jump down to the :ref:`setup_at_home` section of this lesson.

    If you are taking DOBC in person we are able to offer you credentials to the OSU OSL Student Cloud. More
    information in the :ref:`setup_at_lecture` section.

.. image:: /static/Tux.png
    :align: center
    :alt: Tux Linux Logo

There are a variety of ways to run Linux!

- Dual-boot Windows+Linux
- Virtual Machine (VMWare, Virtualbox, cloud server, etc)
- Container (Docker)
- Windows Linux Subsystem

.. ifslides::

  Linux setup we're using today
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  - "Server" running on a VM hosted at the OSL
  - Actually a container running CentOS
  - We'll be using SSH to access the containers remotely
  - All "Servers" will be removed within a week
  - If you want to continue using them at home after today, see :ref:`setup_at_home` or :ref:`setup_vm_at_home`

  .. _setup_at_lecture:

  Lecture Setup
  ~~~~~~~~~~~~~

  1. Get login credentials from your lecturer. You will be provided a ``port`` and ``password``.

  Linux/Mac:

  2. Open a terminal and verify you have ``ssh`` installed by entering the command ``ssh --version``.

  3. Run the following command and enter the password when prompted (it will hide your password in the terminal):

    .. code-block:: console

      $ ssh -p <port> dobc@dobc-shell.osuosl.org

  .. nextslide::

  Windows:
      2. Install an SSH Client (`install Putty`_)

      3. Log into your remote Linux environment using the credentials given to
         you.

          ii. Under '``Host Name (or IP address)``' enter '``dobc@dobc-shell.osuosl.org``', under '``Port``' enter
              '``<port>``'.
          iii. You will be prompted for your password in new window, it will hide the password as you type it.

  .. _install Putty: https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

.. _setup_at_home:

Docker Setup
~~~~~~~~~~~~

We suggest you `install Docker`_ and `Docker Compose`_, a tool which makes it easy to run small `Linux Containers`_ on
your system in a safe sandbox without requiring to install Linux on your own machine. This is the same setup we used in
the lecture.

Make sure you read the install documentation for Docker to ensure your system supports running it and have the required
BIOS settings enabled.

.. nextslide::

After you have it installed, run this to start a container:

.. code-block:: console

  $ git clone https://github.com/DevOpsBootcamp/Bootcamp-Exercises.git
  $ cd Bootcamp-Exercises
  $ docker-compose up -d
  $ docker-compose run -p 8080:8080 dobc bash

.. _install Docker: https://www.docker.com/community-edition
.. _Docker Compose: https://docs.docker.com/compose/install/#install-compose
.. _Linux Containers: https://en.wikipedia.org/wiki/LXC

You can log out by typing ``exit`` and then enter which will stop the container.

To stop the container, run the following:

.. code-block:: console

  $ docker-compose kill
  $ docker-compose rm --all

.. nextslide::

Feel free to try other Docker images, some that we recommend include:

- ``ubuntu``
- ``debian``
- ``centos``
- ``fedora``

To run those, do the following:

.. code-block:: console

  $ docker run -it --rm <docker image name> bash

You can find have more images at the `Docker Hub`_. We also recommend you read `Getting started with Docker`_ to have a
better understanding of how it works.

.. _Docker Hub: https://hub.docker.com/explore/
.. _Getting started with Docker: https://docs.docker.com/get-started/

.. _setup_vm_at_home:

Virtual Machine Setup
~~~~~~~~~~~~~~~~~~~~~

Instead of using Docker, you can also run a Linux `Virtual Machines`_ on your computer. This will give you a full Linux
environment as if it were on a real machine.

We suggest you `install Vagrant`_, a tool which makes it easy to run and acquire `Virtual Machines`_.

You may also need to `install VirtualBox`_ or `install VMWare`_ (Requires TEACH access) a tool necessary for Vagrant to
function.

.. nextslide::

After you get Vagrant and either VirtualBox or VMWare installed, clone our vagrant repo (make sure you `install Git`_
first!) and then start the VM:

.. _install Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git

.. code-block:: console

  $ git clone https://github.com/DevOpsBootcamp/vagrant.git
  $ cd vagrant
  $ vagrant up
  $ vagrant ssh

.. ifnotslides::

  If you have any questions or problems, Google is your friend!  If that does
  not work, :ref:`contact us <contact>` DevOps Bootcamp and we'll help you as
  best we can.

.. image:: /static/vagrant_logo.png
    :target: https://www.vagrantup.com/
    :align: center
    :alt: Vagrant logo

.. _install Vagrant: https://www.vagrantup.com/docs/installation/
.. _Virtual Machines: https://en.wikipedia.org/wiki/Virtual_machine
.. _install VirtualBox: https://www.virtualbox.org/
.. _install VMWare: https://teach.engr.oregonstate.edu/teach.php?type=vmap


Windows Subsystem for Linux Setup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Windows Subsystem for Linux`_ (Bash on Windows) allows you to run
userspace Linux software on Windows, while using less resources than a virtual
machine.

.. image:: /static/ubuntustore.png
    :target: https://msdn.microsoft.com/en-us/commandline/wsl/install-win10
    :align: right
    :width: 50%
    :alt: Windows Store

If you installed the Fall Creators Update for Windows 10, you can install one
or more Linux distributions through the Windows Store.

.. _Windows Subsystem for Linux: https://msdn.microsoft.com/en-us/commandline/wsl/about

Exercise: Change Your Password!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    **Challenge** *Change your password on your Linux machine.*

.. ifnotslides::

    To get acquainted with your new Virtual Machine we are going to change your
    users password.  This is just like changing your password on your personal
    laptop (you've done that before right?) but *entirely via the terminal*, no
    windows or click-buttons at all.

    Start by logging in (outlined in the previous slides).  Then run the
    following command:

.. code-block:: console

    $ passwd
    Changing password for user <user>.
    Changing password for <user>.
    (current) UNIX password: # Enter old password, hidden
    New password:   # Enter new password, also hidden
    Retype new password:
    passwd: all authentication tokens updated successfully.

.. ifnotslides::

    In the next lesson we're going to go over how to do almost *everything* via
    your terminal from editing files to browsing the web!

**Don't forget:** when you login next time, use the *new* password you just
set.


Further Reading
---------------

- More information on `Linux Containers`_ and `Virtual Machines`_.
- `Install Putty`_ if you want to access a remote Linux box.
- `Install Docker`_ if you want to run a local Linux container
- `Install Vagrant`_ if you want to run a local Linux Virtual machine.
- `Install VirtualBox`_ in addition to Vagrant for local virtual machines.
- `Install VMWare`_ in addition to Vagrant for local virtual machines.
- `Windows Subsystem for Linux`_ if you want to use Linux without VM overhead.

Next: :ref:`operating_systems`
