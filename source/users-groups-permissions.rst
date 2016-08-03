.. _users_groups_permissions:


Lesson 4: Users, Groups, Permissions
====================================

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

    - What a user is.
    - Who can be a user.
    - What a group is.
    - Acting as another user.
    - The ``root`` user.


The User
--------

You... ish.

.. ifnotslides::

    Users are the *actors* that do *things* in an OS.  A user is responsible
    for invoking a program, has a list of unique attributes, and has certain
    permissions / restrictions.

    Users can be people or non-people, but as far as the OS is concerned both
    are almost identical.

::

    $ whoami    # your username
    $ who       # who is logged in?
    $ w         # who is here and what are they doing?
    $ id        # user ID, group ID, and groups you're in

Sometimes robots are users too: Apache, Mailman, ntp.

What a User has
~~~~~~~~~~~~~~~

.. ifslides::

    - Username
    - UID
    - Group
    - Shell (not always interactive)
    - Password (Usually but not always)
    - Home Directory (Usually but not always)

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


What Users Can Do
~~~~~~~~~~~~~~~~~


- Change Passwords with the ``passwd`` command.

- Act as Another user with `su`.

::

    $ su $USER          # become user, with THEIR password
    $ su                # become root, with root's password
    $ sudo su -         # use user password instead of root's
    $ sudo su $USER     # become $USER with your password

- Act as themselves.

    - ``ls -l`` to see file permissions.
    - Check the file's group and user.
    - Check the file's read, write, and execute bits.

.. nextslide::

.. image:: /static/xkcd_838.png
    :align: center
    :alt: Sudoers Naught List
    :target: https://www.xkcd.com/838/

Managing Groups and Users
-------------------------

.. ifnotslides::

    As someone interacting with servers, even as a developer, it's necessary
    to understand how to manage users and groups on a Linux machine.

    To view all user information on a system check the file ``/etc/passwd``:

::

    $ cat /etc/passwd
    # username:x:UID:GID:GECOS:homedir:shell

.. ifnotslides::

    To add, delete, and change the password of a user respectively run the
    following commands:

::

    $ useradd <user_name>  # vs adduser, the friendly Ubuntu version
    $ userdel <user_name>
    $ passwd

.. ifnotslides::

    To add a group, or the permissions of a user/group run ``groupmod``,
    ``usermod``, and ``groupmod`` respectively.  Similarly to ``/etc/passwd``,
    ``/etc/group`` carries group information.

::

    $ groupadd
    $ usermod
    $ groupmod
    $ cat /etc/group
        root:x:0:

.. nextslide::

.. image:: /static/xkcd215.png
    :alt: xkcd letting go
    :target: https://www.xkcd.com/215/
    :align: center


Root and Sudo
-------------

Root:
    Basically god on Linux.

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

::

    [foo@compe ~]$ yum install httpd    # Runs command as `foo` user
    Loaded plugins: fastestmirror, ovl
    ovl: Error while doing RPMdb copy-up:
    [Errno 13] Permission denied: '/var/lib/rpm/__db.002'
    You need to be root to perform this command.
    [foo@compe ~]$ sudo yum install httpd    # Runs command as `root` user.
    password:
    Loaded plugins: fastestmirror, ovl
    [... installs correctly ...]

.. nextslide::
    
.. image:: /static/xkcd_149.png
    :align: center
    :target: https://xkcd.com/149/
    :alt: Sudo get me a sandwich.

.. warning::

    Acting as root is dangerous!  You can accidentally delete you filesystem,
    forcing you to completley re-install your OS!  **Type carefully.**


TODO
----

- Create a user on your system for yourself, with your preferred username.
- Give your user ``sudo`` powers.
- Use ``su`` to get into your user account.
- Change your password.
- Create a directory called ``bootcamp`` in your home directory.
- Create a group called ``devops``.

.. TOOD: Add answer key


Further Reading
---------------

.. TODO: Add Further Reading
