====================================
Lesson 2: Single System Fundamentals
====================================

Or, how to be a power user.

Housekeeping
============

.. figure:: /static/virtualbox.png
    :align: center
    :scale: 30%

10 minutes to make sure everyone's Virtualbox instances are up and running


**Your opinions:**

* Want to meet during dead week vs. have last meeting of term next week?

* Start wk1 of winter term?


Today's Topics
==============
* What are files?
    * Permissions/users
* What are user accounts?
    * User management
    * Root vs. normal
    * Groups
* What are packages?
    * How to use package managers
    * Differences between Linux Distributions
    * Other package managers

What are users?
===============

* You, right now

.. code-block:: bash

    $ whoami    # your username
    $ who       # who is logged in?
    $ w         # who is here and what are they doing?
    $ id        # user ID, group ID, and groups you're in

* Not just people: Apache, Mailman, ntp

Users have
==========

* Username
* UID
* Group
* Usually (but not always) password
* Usually (but not always) home directory

Managing users
==============

.. code-block:: bash

    $ cat /etc/passwd
    # username:x:UID:GID:GECOS:homedir:shell
    $ useradd $USER # vs adduser, the friendly Ubuntu version
    $ userdel $USER
    $ passwd

.. figure:: /static/xkcd215.png
    :align: center

.. code-block:: bash

    # GECOS: full name, office number and building, office phone extension, 
    # home phone number (General Electric Comprehensive Operating System)
    $ chfn # change GECOS information; only works sometimes
    $ finger # tells you someone's GECOS info
    

Passwords
=========

* ``/etc/shadow``, not ``/etc/passwd``

.. code-block:: bash

    test@x230 ~ $ ls -l /etc/ | grep shadow
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
==============

* UID 0
* ``sudo``

.. figure:: /static/xkcd149.png
    :align: center

Acting as another user
======================

.. code-block:: bash

    $ su $USER          # become user, with THEIR password
    $ su                # become root, with root's password
    $ sudo su -         # use user password instead of root's
    $ sudo su $USER     # become $USER with your password

.. figure:: /static/xkcd_838.png
    :scale: 80%

If someone has permissions errors:
    * Check that they or their group owns the files
    * Check that they have the flag +x to execute


What are groups?
================

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

Hands-On: Users and Groups
==========================

.. note:: To give yourself sudo powers do the following:

  #. Add your user to the ``wheel`` group using ``gpasswd``.
  #. As the root user, use ``visudo`` and uncomment this line::

      %wheel  ALL=(ALL)   ALL

  #. Save the file and now you should have sudo!

  *We'll cover sudo in more depth at a later time.*

* Create a user on your system for yourself, with your preferred username
* Give your user sudo powers
* Use use su to get into your user account
* Change your password
* Create a directory called bootcamp in your home directory
* Create a group called devops 


What are files?
===============

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
===============

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
======

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

    +=====+========+=======+
    | rwx | Binary | Octal |
    +=====+========+=======+
    | --- | 000    | 0     |
    | --x | 001    | 1     |
    | -w- | 010    | 2     |
    | -wx | 011    | 3     |
    | r-- | 100    | 4     |
    | r-x | 101    | 5     |
    | rw- | 110    | 6     |
    | rwx | 111    | 7     |
    +=====+========+=======+

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
==============

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

ACLs
====

* Access control lists

* Not recommended; hard to maintain

* Typically how other OSes manage permissions

* Support depends on OS and filesystem

Hands-On: Files and Permissions
===============================

.. code-block:: bash
   
    $ touch foo # create empty file called foo

* As root, create a file in /home/$yourusername/bootcamp
* Who can do what to the file? 
* Make the devops group own the file
* Make a file called allperms and give user, group, and world +rwx 
* Make more files and practice changing their permissions

Package Management
==================

*Take care of installation and removal of software*

**Core Functionality:**

* Install, Upgrade & uninstall packages easily
* Resolve package dependencies
* Install packages from a central repository
* Search for information on installed packages and files
* Pre-built binaries (usually)

**Popular Linux Package Managers**

* .deb / APT (used by Debian, Ubuntu)
* .rpm / YUM (used by RedHat, CentOS, Fedora)

RPM & yum (RedHat, CentOS, Fedora)
==================================

.. image:: /static/rpm.png
    :align: right
    :width: 30%

**RPM**

  Binary file format which includes metadata about the package and the
  application binaries as well.

.. image:: /static/yum.png
    :align: right
    :width: 30%

**Yum**

  RPM package manager used to query a central repository and resolve RPM
  package dependencies.

Yum Commands (Redhat, CentOS, Fedora)
-------------------------------------

We'll use the ``tree`` package as an example below.

.. code-block:: bash

  # Searching for a package
  $ yum search tree

  # Information about a package
  $ yum info tree

  # Installing a package
  $ yum install tree

  # Upgrade all packages to a newer version
  $ yum upgrade

  # Uninstalling a package
  $ yum remove tree

  # Cleaning the RPM database
  $ yum clean all

RPM Commands
------------

Low level package management. No dependency checking or central repository.

.. code-block:: bash

  # Install an RPM file
  $ rpm -i tree-1.5.3-2.el6.x86_64.rpm

  # Upgrade an RPM file
  $ rpm -Uvh tree-1.5.3-3.el6.x86_64.rpm

  # Uninstall an RPM package
  $ rpm -e tree

  # Querying the RPM database
  $ rpm -qa tree

  # Listing all files in an RPM package
  $ rpm -ql tree

DPKG & Apt (Debian, Ubuntu)
===========================

**Deb**

  Binary file format which includes metadata about the package and the
  application binaries as well.

.. image:: /static/debian.png
    :align: right

**DPKG**

  Low level package installer for the .deb file format. Does no package
  dependency resolution.

**Apt**

  DPKG package manager used to query a central repository and resolve Deb
  package dependencies. Considered mostly a front-end to dpkg.

Apt Commands (Debian, Ubuntu)
-----------------------------

.. note:: You can also use aptitude as a front-end to dpkg instead of apt-get.

.. code-block:: bash

  # Update package cache database
  $ apt-get update

  # Searching for a package
  $ apt-cache search tree

  # Information about a package
  $ apt-cache show tree

  # Installing a package
  $ apt-get install tree

  # Upgrade all packages to a newer version
  $ apt-get upgrade
  $ apt-get dist-upgrade

  # Uninstalling a package
  $ apt-get remove tree
  $ apt-get purge tree

Dpkg Commands
-------------

Low level package management. No dependency checking or central repository.

.. code-block:: bash

  # Install or upgrade a DEB file
  $ dpkg -i tree_1.6.0-1_amd64.deb

  # Removing a DEB package
  $ dpkg -r tree

  # Purging a DEB package
  $ dpkg -P tree

  # Querying the DPKG database
  $ dpkg-query -l tree

  # Listing all files in a DEB package
  $ dpkg-query -L tree

Language-specific Package Managers
==================================

* Languages sometimes have their own package management suite
* Can be useful for using newer versions of packages
* **Examples**
    * pip (Python)
    * rubygems (Ruby)
    * CPAN (Perl)
    * cabal (Haskell)
    * npm (NodeJS)
    * *... and so on forever ...*

Other Package Managers
======================

They each fill a specific niche and have their own pros and cons.

* Portage (Gentoo) -- Source based package installer
* pacman (Arch Linux)
* ZYpp / Zypper (SUSE) -- Yet another RPM package manager

Installing from source
======================

* Download source tarball, run build scripts and install in a local directory.
* RPM/DEB packages do this for you
* Not for the faint of heart ... **Not recommended!**
* Using ``grep`` as an example

.. code-block:: bash

  $ wget http://mirrors.kernel.org/gnu/grep/grep-2.15.tar.xz
  $ tar -Jxvf grep-2.15.tar.xz
  $ cd grep-2.15
  $ ./configure
  $ make
  $ make install


Hands-on: Package Management
============================

* Install the ``git`` package
* Query the RPM/APT database for installed packages
* List the files in an installed package
* Remove the ``git`` package

Questions:
==========

* read example output of ls -al
* read output of yum or aptitude search
* install a package on their VM/partition (Vim, Git)
        * explain what dependencies it also installed
