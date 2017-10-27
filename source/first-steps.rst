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

.. nextslide::

Development:
    - **Version Control:** A way to track changes and contributions to a
      project.
    - **Continuous Integration:** Releasing updates *continuously*.

Buzzwords:
    - **FOSS:** Free (and Libre) Open Source Software.  Free as in Speech, not
      Free as in Pizza (but that too usually).
    - **'The Cloud':** Computers somewhere else.
    - **Containers:** Not virtual machines, but basically virtual machines.


TODO: What Vocabulary Do *You* Know?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    *What other vocabulary can you think of related to DevOps?*

    *What about Silicon Valley, Programming, System Administration, etc?*

.. note::

    This is a **TODO**.  It's basically an exercise or activity but with a
    cheeky name.  Try them out if you don't feel confident in a topic.


Notation
--------

.. ifnotslides::

    Some notes about notation...

    Just like a textbook, we have some unique notation you should be aware of.
    The following is a short list of key notation used in DOBC.

- Variable (use whatever word you like here e.g., foo, bar, baz)
    - ``$ONE_VARIABLE_NOTATION``
    - ``<another notation for variables>``

- Literal (copy this exactly)
    - ``copy_me_exactly``

- Comments (parts of the code just for humans)
    - ``this_is(code)  # everything after the octothorp is a comment!``
    - ``other_code(line)  // This can also be a comment.  It depends on the
      langauge!``

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
    # It should be clear Where it 'goes' and how to run it based on context.
    print('Hello world!')

.. ifnotslides::

    *You can copy the above script into a file named* ``<whatever you
    want>.py`` *and run it with* ``python <whatever you want>.py``

    Shell commands are annotated with a ``$``. For instance:

.. code:: bash

    # Copy the text after `$` into your terminal & press enter.
    $ echo Hello World


TODO: Reading Examples
~~~~~~~~~~~~~~~~~~~~~~

    *Trick question: how would you read this*

.. code-block:: python

    #!/bin/python
    dogs = ['$BREED_ONE', '$BREED_TWO', '$BREED_THREE']
    for breed in dogs:
        print(breed)


Answer: Reading Examples
~~~~~~~~~~~~~~~~~~~~~~~~

Replace the ``$BREED_N`` with actual dog breeds.

.. code-block:: python

    #!/bin/python
    dogs = ['corgie', 'pug', 'french bulldog']
    for breed in dogs:
        print(breed)


Getting Setup on Linux
----------------------

.. ifnotslides::

    If you are taking the course exclusively online you will need to run a
    Virtual Machine on your own computer. For more information jump down to the
    :ref:`setup_at_home` section of this lesson.

    If you are taking DOBC in person we are able to offer you credentials to
    the OSU OSL Student Cloud. More information in the :ref:`setup_at_lecture`
    section.

.. image:: /static/Tux.png
    :align: center
    :alt: Tux Linux Logo

.. _setup_at_lecture:


Lecture Setup
~~~~~~~~~~~~~

1. Get login credentials from your lecturer.
    - You will be provided a ``username``, ``password``, ``host``, and
      ``port``.

Linux/Mac:
    2. Open a terminal and verify you have ``ssh`` installed by
       entering the command ``ssh --version``.

    3. Run ``ssh -p <port> <username>@<host>`` and enter the password when
       prompted (it will hide your password in the terminal).

.. nextslide::

Windows:
    2. Install an SSH Client (`install Putty`_)

    3. Log into your remote Linux environment using the credentials given to
       you.

        ii. Under ``Host Name (or IP address)`` enter ``<user>@<host>``, under
            ``Port`` enter ``<port>``.
        iii. You will be prompted for your password in new window, it will hide
             the password as you type it.

.. _install Putty: http://www.putty.org/

.. _setup_at_home:


Home Setup
~~~~~~~~~~

We suggest you `install Vagrant`_, a tool which makes it easy to run and
acquire `Virtual Machines`_.

You may also need to `install VirtualBox`_, a tool necessary for Vagrant to
function.

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

TODO: Change Your Password!
~~~~~~~~~~~~~~~~~~~~~~~~~~~

    **Challenge** *Change your password on your Linux machine.*

.. ifnotslides::

    To get aquainted with your new Virtual Machine we are going to change your
    users password.  This is just like changing your password on your personal
    laptop (you've done that before right?) but *entirely via the terminal*, no
    windows or click-buttons at all.

    Start by logging in (outlined in the previous slides).  Then run the
    following command:

.. code::

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

- More information on `Virtual Machines`_.
- `Install Putty`_ if you want to access a remote Linux box.
- `Install Vagrant`_ if you want to run a local Linux Virtual machine.
- `Install VirtualBox`_ in addition to Vagrant for local virtual machines.

.. TODO: Add more Further Reading
