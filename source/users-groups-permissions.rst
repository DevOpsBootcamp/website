.. _users_groups_permissions:


Lesson 5: Users, Groups, Permissions
====================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/users-groups-permissions.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/users-groups-permissions.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What a user is.
    - Who can be a user.
    - What a group is.
    - Acting as another user.
    - The ``root`` user.


What are users?
---------------

You, right now.

.. ifnotslides::

    Users are the *actors* that do *things* in an OS.  A user is responsible
    for invoking a program, has a list of unique attributes, and has certain
    permissions / restrictions.

    Users can be people or non-people, but as far as the OS is concerned both
    are almost identical.

.. code-block:: console

    $ whoami    # your username
    $ who       # who is logged in?
    $ w         # who is here and what are they doing?
    $ id        # user ID, group ID, and groups you're in

Not just people: Apache, Mailman, ntp. "system users"

Users have
----------

* Username
* UID
* Group
* Shell
* Usually (but not always) password
* Usually (but not always) home directory

.. ifnotslides::

    Username
        Usernames are what you call yourself as a user.

    UID
        What your User is represented by in the OS.  A unique identifier.

        System users (robots) are UID ``0-999``, People users are UID
        ``1000+``.

    Group
        Groups allow multiple user to share permissions.  Every user is
        usually in their own group and may be added to other groups for
        additional system access.

    Shell (not always interactive)
        This is the shell you are given when you login. Usually defaults to
        ``/bin/bash`` on GNU/Linux.

        Robot users are not given a shell since they don't login.

    Password (Usually but not always)
        Most users have a password, but if one is not supposed to they can be
        given a wildcard password (``*``), which can never be matched, or an
        empty password, which is matched on empty input.

    Home Directory (Usually but not always)
        Below is a line from the file ``/etc/passwd`` which stores user
        information (dispite the name, it shouldn't contain passwords).

    All of this informaion is stored in a file called ``/etc/passwd``.

``/etc/passwd:``

::

    root:x:0:0:root:/root:/bin/bash
    username:password:uid:gid:uid info:home directory:shell

Managing Groups and Users
~~~~~~~~~~~~~~~~~~~~~~~~~

As someone interacting with servers, even as a developer, it's necessary to understand how to manage users and groups
on a Linux machine.

To view all user information on a system check the file ``/etc/passwd``:

.. code-block:: console

    $ cat /etc/passwd
    # username:x:UID:GID:GECOS:homedir:shell

.. nextslide::

To add, delete, and change the password of a user respectively run the following commands:

.. code-block:: console

    $ useradd <user_name>  # vs adduser, the friendly Ubuntu version
    $ userdel <user_name>
    $ passwd

.. image:: /static/xkcd215.png
    :alt: xkcd letting go
    :target: https://www.xkcd.com/215/
    :align: center
    :width: 85%

What are groups?
----------------

To add a group, or the permissions of a user/group run ``groupmod``, ``usermod``, and ``groupmod`` respectively.
Similarly to ``/etc/passwd``, ``/etc/group`` carries group information.

.. code-block:: console

    $ groupadd
    $ usermod
    $ groupmod
    $ cat /etc/group
        root:x:0:
        daemon:x:1:
        bin:x:2:
        sys:x:3:
        adm:x:4:
        tty:x:5:
    # group name:password or placeholder:GID:member,member,member

Users won't be active in new group until they "log back in"

Passwords
~~~~~~~~~

``/etc/shadow``, not ``/etc/passwd``

.. code-block:: console

    user@localhost ~ $ ls -l /etc/ | grep shadow
    -rw-r-----  1 root shadow   1503 Nov 12 17:37 shadow

    $ sudo su -
    $ cat /etc/shadow
    daemon:*:15630:0:99999:7:::
    bin:*:15630:0:99999:7:::
    sys:*:15630:0:99999:7:::
    mail:*:15630:0:99999:7:::

    # name:hash:time last changed: min days between changes: max days
    #    between changes:days to wait before expiry or disabling:day of
    #    account expiry

    $ chage # change when a user's password expires

Root/Superuser
~~~~~~~~~~~~~~

* UID 0
* ``sudo``

.. image:: /static/xkcd_149.png
    :align: right
    :target: https://xkcd.com/149/
    :alt: Sudo get me a sandwich.

.. warning::

  Acting as root is dangerous!  You can accidentally delete your filesystem, forcing you to completely re-install your
  OS!  **Type carefully.**

Sudo
~~~~

Consult ``man 5 sudoers`` for more information:

::

  # User alias specification
  User_Alias  DOBC_ADMIN = lance, teacher
  User_Alias  DOBC_STUDENT = john, jane

  # Runas alias specification
  Runas_Alias ADMIN = root, sysadmin
  Runas_Alias STUDENT = httpd

  # Host alias specification
  Host_Alias OSU_NET = 128.193.0.0/16
  Host_Alias SERVERS = www, db

  # Cmnd alias specification
  Cmnd_Alias KILL = /bin/kill
  Cmnd_Alias SU = /bin/su

  #  User privilege specification
  root          ALL = (ALL) ALL
  DOBC_ADMIN    ALL = NOPASSWD: ALL
  DOBC_STUDENT OSU_NET = (STUDENT) KILL, SU

Acting as another user
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: console

    $ su joe            # become user joe, with THEIR password
    $ su                # become root, with root's password
    $ sudo su -         # become root, with your password
    $ sudo su joe       # become user joe with your password

.. image:: /static/xkcd_838.png
    :align: center
    :width: 75%
    :alt: Sudoers Naught List
    :target: https://www.xkcd.com/838/

A dash after ``su`` provides an environment similar to what the user would expect. Typically a good practice to always
use ``su -``

Super users
-----------

.. ifnotslides::

    All users have a specific set of permissions, i.e., things they *can* and
    *cannot* do.  The Linux super-user ``root`` is not burdened by this and so
    it can do pretty much whever it wants.  As a *person* this is important
    because you can *become* root and get things done that *your* user is
    unable to do.

    The way you act as ``root`` is one of two ways:
        - ``su root`` Is like logging in as ``root``.  Prompts you for the
          root user's password.
        - ``sudo <command>`` runs a single command as root. Prompts you for
          *your* password, but requries you to be on the ``sudoers`` list.

Trying to run commands which require root permissions as a regular user can be a problem. However, ``sudo`` authorizes
you to do commands based on your permissions. For example:

.. code-block:: console

  [dobc@dobc ~]$ yum install httpd      # Runs command as `dobc` user
  Loaded plugins: fastestmirror, ovl
  ovl: Error while doing RPMdb copy-up:
  [Errno 13] Permission denied: '/var/lib/rpm/__db.002'
  You need to be root to perform this command.

  [dobc@dobc ~]$ sudo yum install httpd # Runs command as `root` user.
  password:
  Loaded plugins: fastestmirror, ovl
  [... installs correctly ...]

Exercises
---------

#. Create a user on your system for yourself, with your preferred username.
#. Give your user ``sudo`` powers.
#. Change your password.
#. Use ``su`` to get into your user account.
#. Create a directory called ``bootcamp`` in your home directory.
#. Create a group called ``devops``.

Exercise Answer Key
-------------------

.. rst-class:: build

.. code-block:: console

  $ sudo su -
  $ useradd lance
  # better to use visudo instead
  $ echo "lance ALL = (ALL) ALL" >> /etc/sudoers
  $ passwd lance
  Changing password for user lance.
  New password:
  Retype new password:
  passwd: all authentication tokens updated successfully.
  $ su - lance
  $ mkdir bootcamp
  $ sudo groupadd devops

  We trust you have received the usual lecture from the local System
  Administrator. It usually boils down to these three things:

      #1) Respect the privacy of others.
      #2) Think before you type.
      #3) With great power comes great responsibility.

  [sudo] password for lance:

Further Reading
---------------

.. TODO: Add Further Reading

- `Understanding Linux File Permissions`_

Next: :ref:`files`

.. _Understanding Linux File Permissions: https://www.linux.com/learn/understanding-linux-file-permissions
