.. _daycamp_02:

Linux Basics
============

Today's Agenda
--------------

* The Terminal & Shell
    * Scripts, file paths, special characters

.. figure:: /static/Tux.png
    :align: right

* Productivity tricks
    * Getting help
* What are files?
    * File permissions
* What are user accounts?
    * User and group management
* What are packages?
    * How to use package managers

Basic Shell Commands
--------------------

.. note::

  :Explain architecture: built in commands vs. external binaries
  :Demo commands:
    Directory movement and file manipulation: Cd, pwd, ls, rm, mv, touch
  :User info: id, whoami, w
  :Pipes: redirection (pipe.txt, redirect.txt)
  :Special variables: $?, $$ (pid.sh), !!, !*, !$

.. figure:: /static/bash.png
    :align: right
    :scale: 75%

* ``ls``, ``cd``, ``cat``, ``echo``, ``pwd``
* invoke/call an installed program
* get help: ``man <program>``
* ``history``, up arrow, ctrl+r
* Tab completion

Invoking a script
-----------------

.. note:: Permissions discussed later.

.. code-block:: bash

    $ ls -l
    $ chmod +x $filename
    $ ./$filename

**Arguments** (or flags) are extra information that you pass to a script or
program when you call it. They tell it in more detail what you want to do.

.. code-block:: bash

    $ ls -a -l
    $ ls -al
    $ ls -si
    $ ls --si

Why pass arguments on the command line rather than having an interactive mode?

File Paths
----------

* ``.`` means current directory
* ``..`` means parent directory
* Tilde (``~``) means your homedir (``/home/$username``)
* ``/`` separates directories (not ``\``)
* ``/`` is root directory, so ``~`` expands to ``/home/$username/``
* current path appears in your prompt: I'm logged in as the user test on the
  machine named x230

.. code-block:: bash

    test@x230 ~ $ ls
    Documents  Pictures
    test@x230 ~ $ cd Documents/
    test@x230 ~/Documents $ ls
    Code  School  Work
    test@x230 ~/Documents $ pwd
    /home/test/Documents


.. note::
  root directory is not to be confused with a home directory for the root
  account

Special Characters
------------------

* escape with ``\`` to use them literally
* # means a comment
* ; allows multiple commands per line
* !, ?, \*, &&, &
* Regular expressions - for matching patterns of text

.. figure:: /static/xkcd_regex.png
    :align: center
    :scale: 50%

Help, get me out of here!
-------------------------

.. figure:: /static/exit.jpg
    :align: center

* ctrl+c kills/quits
* ctrl+d sends EOF (end-of-file)
    * also means logout
* :q gets you out of Vi derivatives and man pages
    * esc - esc - :q if you changed modes
* read what's on your screen; it'll help you

Knowledge Check
---------------

::

    test@x230 ~ $ tree
    .
    ├── Documents
    │   ├── Code
    │   │   └── scripts
    │   │       └── test.sh
    │   ├── School
    │   └── Work
    └── Pictures
        ├── manatee.gif
        └── turtle.png
    6 directories, 5 files

* What user am I logged in as?
* What command did I just run?
* What is my current directory when I run that command?

Review
------

.. Tell me what to type

* I have the script ``test.py``. How do I run it?
* How do you list all the files in the current directory?
* Give 2 ways to change directory to your home directory.

What are users?
---------------

* You, right now

.. code-block:: bash

    $ whoami    # your username
    $ who       # who is logged in?
    $ w         # who is here and what are they doing?
    $ id        # user ID, group ID, and groups you're in

* Not just people: Apache, Mailman, ntp

Users have
----------

* Username
* UID
* Group
* Shell (not always interactive)
* Usually (but not always) password
* Usually (but not always) home directory

What are groups?
----------------

* Manage permissions for groups of users

.. code-block:: bash

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

What are files?
---------------

* Nearly everything
* Files have:
    * Owner
    * Permissions
    * inode
    * Size
    * Filename

.. code-block:: bash

    test@x230 ~ $ ls -il
    total 8
    2884381 drwxrwxr-x 5 test test 4096 Nov  6 11:46 Documents
    2629156 -rw-rw-r-- 1 test test    0 Nov 13 14:09 file.txt
    2884382 drwxrwxr-x 2 test test 4096 Nov  6 13:22 Pictures

File extensions
---------------

* ``.jpg``, ``.txt``, ``.doc``

* Really more of a recommendation
    * File contains information about its encoding

.. code-block:: bash

    $ file $FILENAME # tells you about the filetype

    test@x230 ~ $ file file.txt
    file.txt: ASCII text

    test@x230 ~ $ file squirrel.jpg
    squirrel.jpg: JPEG image data, JFIF standard 1.01

ls -l
------

* First bit: type
* Next 3: user
* Next 3: group
* Next 3: world

* user & group

.. code-block:: bash

    $ ls -l
    drwxrwxr-x 5 test test 4096 Nov  6 11:46 Documents
    -rw-rw-r-- 1 test test    0 Nov 13 14:09 file.txt
    drwxrwxr-x 2 test test 4096 Nov  6 13:22 Pictures


chmod and octal permissions
---------------------------

.. code-block:: bash

    +-----+--------+-------+
    | rwx | Binary | Octal |
    +-----+--------+-------+
    | --- | 000    | 0     |
    | --x | 001    | 1     |
    | -w- | 010    | 2     |
    | -wx | 011    | 3     |
    | r-- | 100    | 4     |
    | r-x | 101    | 5     |
    | rw- | 110    | 6     |
    | rwx | 111    | 7     |
    +-----+--------+-------+

* u, g, o for user, group, other
* -, +, = for remove, add, set
* r, w, x for read, write, execute

chown, chgrp
------------

user & group

.. code-block:: bash

    # Change the owner of myfile to "root".
    $ chown root myfile

    # Likewise, but also change its group to "staff".
    $ chown root:staff myfile

    # Change the owner of /mydir and subfiles to "root".
    $ chown -hR root /mydir

    # Make the group devops own the bootcamp dir
    $ chgrp -R devops /home/$yourusername/bootcamp

Types of files
--------------

.. code-block:: bash

    drwxrwxr-x      5 test    test      4096    Nov  6 11:46 Documents
    -rw-rw-r--      1 test    test         0    Nov 13 14:09 file.txt
    drwxrwxr-x      2 test    test      4096    Nov  6 13:22 Pictures
    ----------     -------  -------  -------- ------------ -------------
        |             |        |         |         |             |
        |             |        |         |         |         File Name
        |             |        |         |         +---  Modification Time
        |             |        |         +-------------   Size (in bytes)
        |             |        +-----------------------        Group
        |             +--------------------------------        Owner
        +----------------------------------------------   File Permissions

``-`` is a normal file

``d`` is a directory

``b`` is a block device

.. ACLs
.. ----
..
.. * Access control lists
..
.. * Not recommended; hard to maintain
..
.. * Typically how other OSes manage permissions
..
.. * Support depends on OS and filesystem

Root/Superuser
--------------

* UID 0

.. code-block:: bash

    $ su $USER          # become user, with THEIR password
    $ su                # become root, with root's password
    $ sudo su -         # use user password instead of root's
    $ sudo su $USER     # become $USER with your password

If someone has permissions errors:

    * Check that they or their group owns the files
    * Check that they have the flag +x to execute

.. figure:: /static/xkcd149.png
    :align: center
    :scale: 50%

Hands-On: Users and Groups
--------------------------

.. note:: To give yourself sudo powers do the following:

  #. Add your user to the ``wheel`` group using ``gpasswd``.
  #. As the root user, use ``visudo`` and uncomment this line::

      %wheel  ALL=(ALL)   ALL

  #. Save the file and now you should have sudo!

  *We'll cover sudo in more depth at a later time.*

* Change your password
* Use ``sudo`` to create a new user with your personal nickname
* Switch to that user with ``su``
* Make a new directory in the new user's home directory


Hands-On: Files and Permissions
-------------------------------

.. code-block:: bash

    $ touch foo # create empty file called foo

* Create a file in /home/$yourusername/bootcamp
* Who can do what to the file?
* Make your other user own the file
* Make a file called allperms and give user, group, and world ``+rwx``
* Make more files and practice changing their permissions


.. RPM & yum (RedHat, CentOS, Fedora)
.. ----------------------------------
..
.. .. image:: /static/rpm.png
..     :align: right
..     :width: 30%
..
.. **RPM**
..
..   Binary file format which includes metadata about the package and the
..   application binaries as well.
..
.. .. image:: /static/yum.png
..     :align: right
..     :width: 30%
..
.. **Yum**
..
..   RPM package manager used to query a central repository and resolve RPM
..   package dependencies.
..
.. Yum Commands (Redhat, CentOS, Fedora)
.. -------------------------------------
..
.. .. code-block:: bash
..
..   # Searching for a package
..   $ yum search tree
..
..   # Information about a package
..   $ yum info tree
..
..   # Installing a package
..   $ yum install tree
..
..   # Upgrade all packages to a newer version
..   $ yum upgrade
..
..   # Uninstalling a package
..   $ yum remove tree
..
..   # Cleaning the RPM database
..   $ yum clean all
..
.. RPM Commands
.. ------------
..
.. Low level package management. No dependency checking or central repository.
..
.. .. code-block:: bash
..
..   # Install an RPM file
..   $ rpm -i tree-1.5.3-2.el6.x86_64.rpm
..
..   # Upgrade an RPM file
..   $ rpm -Uvh tree-1.5.3-3.el6.x86_64.rpm
..
..   # Uninstall an RPM package
..   $ rpm -e tree
..
..   # Querying the RPM database
..   $ rpm -qa tree
..
..   # Listing all files in an RPM package
..   $ rpm -ql tree
..
.. DPKG & Apt (Debian, Ubuntu)
.. ---------------------------
..
.. **Deb**
..
..   Binary file format which includes metadata about the package and the
..   application binaries as well.
..
.. .. image:: /static/debian.png
..     :align: right
..
.. **DPKG**
..
..   Low level package installer for the .deb file format. Does no package
..   dependency resolution.
..
.. **Apt**
..
..   DPKG package manager used to query a central repository and resolve Deb
..   package dependencies. Considered mostly a front-end to dpkg.
..
.. Apt (Debian, Ubuntu)
.. -----------------------------
..
.. .. note:: You can also use aptitude as a front-end to dpkg instead of apt-get.
..
.. .. code-block:: bash
..
..   # Update package cache database
..   $ apt-get update
..
..   # Searching for a package
..   $ apt-cache search tree
..
..   # Information about a package
..   $ apt-cache show tree
..
..   # Installing a package
..   $ apt-get install tree
..
..   # Upgrade all packages to a newer version
..   $ apt-get upgrade
..   $ apt-get dist-upgrade
..
..   # Uninstalling a package
..   $ apt-get remove tree
..   $ apt-get purge tree
..
.. Dpkg Commands
.. -------------
..
.. Low level package management. No dependency checking or central repository.
..
.. .. code-block:: bash
..
..   # Install or upgrade a DEB file
..   $ dpkg -i tree_1.6.0-1_amd64.deb
..
..   # Removing a DEB package
..   $ dpkg -r tree
..
..   # Purging a DEB package
..   $ dpkg -P tree
..
..   # Querying the DPKG database
..   $ dpkg-query -l tree
..
..   # Listing all files in a DEB package
..   $ dpkg-query -L tree
