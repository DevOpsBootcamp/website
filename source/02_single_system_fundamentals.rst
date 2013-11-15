====================================
Lesson 2: Single System Fundamentals
====================================

Or, how to be a power user.

Today's Topics
==============
* What are files?
    * Permissions/users
* What are user accounts?
    * user management
    * root vs. normal
    * groups
* What are packages?
    * repositories
    * other options (tarballs, build from source)
    * how installation works
    * what're scripts

What are users?
===============

* You, right now

.. code-block:: bash

    $ whoami
    $ who
    $ w
    $ id

* Not just people: Apache, Mailman, ntp

Users have
----------

* Username
* UID
* Usually (but not always) password
* Usually (but not always) home directory

Managing users
--------------

.. code-block:: bash

    $ cat /etc/passwd
    $ useradd $USER # vs adduser
    $ userdel $USER
    $ passwd

Passwords
---------

* ``/etc/shadow``, not ``/etc/passwd``

.. code-block:: bash

    test@x230 ~ $ ls -l /etc/ | grep shadow
    -rw-r-----  1 root shadow    857 Nov 12 17:37 gshadow
    -rw-------  1 root root      846 Nov 12 17:37 gshadow-
    -rw-r-----  1 root shadow   1503 Nov 12 17:37 shadow
    -rw-------  1 root root     1378 Nov 12 17:37 shadow-

    $ sudo su -
    $ cat /etc/shadow
    daemon:*:15630:0:99999:7:::
    bin:*:15630:0:99999:7:::
    sys:*:15630:0:99999:7:::
    sync:*:15630:0:99999:7:::
    games:*:15630:0:99999:7:::
    man:*:15630:0:99999:7:::
    lp:*:15630:0:99999:7:::
    mail:*:15630:0:99999:7:::
    news:*:15630:0:99999:7:::


* Expire or disable (``chage``)

Root/Superuser
--------------

* UID 0
* ``sudo``

Acting as another user
----------------------

.. code-block:: bash

    $ su $USER
    $ sudo su -
    $ sudo su $USER

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

Hands-On
========

* Create group ``bootcamp``
* Create user foo
* Create user baz
* Add baz to the bootcamp group
* Give foo sudo powers

What are files?
===============

* Nearly everything
* Files have:
    * Owner
    * Permissions
    * Size
    * Filename

File extensions
---------------

* ``.jpg``, ``.txt``, ``.doc``

* Really more of a recommendation
    * File contains information about its encoding

.. code-block:: bash

    $ file $FILENAME # tells you about the filetype

ls -l
------

* First bit: type
* Next 3: user
* Next 3: group
* Next 3: world

* user & group

.. code-block:: bash

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


chown
-----

user & group

.. code-block:: bash

    # Change the owner of myfile to "root".
    $ chown root myfile

    # Likewise, but also change its group to "staff".
    $ chown root:staff myfile

    # Change the owner of /mydir and subfiles to "root".
    $ chown -hR root /mydir

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
* .rpm / YUM (used by RedHat, CentOS, Fedora, SuSe)

RPM & yum (RedHat, CentOS, Fedora)
----------------------------------

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
  $ rpm -Uvh tree-1.5.3-3.el6.x86_64

  # Uninstall an RPM package
  $ rpm -e tree

  # Querying the RPM database
  $ rpm -qa tree

  # Listing all files in an RPM package
  $ rpm -ql tree

DPKG & Apt (Debian, Ubuntu)
----------------------------------


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

Apt/Aptitude Commands (Debian, Ubuntu)
--------------------------------------

.. code-block:: bash

  # Update package cache database
  $ apt-get update

  # Searching for a package
  $ apt-cache search tree

  # Information about a package
  $ apt-cache showpkg tree
  $ aptitude show tree

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
----------------------------------

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
----------------------

They each fill a specific niche and have their own pros and cons.

* Portage (Gentoo) -- Source based package installer
* pacman (Arch Linux)
* ZYpp / Zypper (SUSE) -- Yet another RPM package manager

Installing from source
----------------------

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
----------------------------

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

.. note:: Questions out of CS312 curriculum

    1) (1 pt.) Why is a salt used when storing encrypted passwords in
    /etc/shadow?
    2) (1 pt.) What portion of the MD5 hash
    '$1$xxUwcovy$JfV9i7j9H/NFA3RBCrVHN.' is the salt?
    3) (1 pt.) What UID is used for the root user?
    4) (2 pts.) Where is a user's primary ("default") group defined?
    Specifically which file and which "field".
    5) (3 pts.) Add a user 'foobar' to your system. Use 'useradd' to add
    the user and to create their home directory
        containing files from /etc/skel. Show the user's entry in /etc/passwd
    as well as the full useradd command
    needed.
    6) (3 pts.) Create a group 'cs312' on your system.
    Show the command used (not editing files by hand).
    7) (3 pts.) Assume the user 'foobar' belongs to multiple groups. Add
    'foobar' to the 'cs312' group by using a
    system command (not editing files by hand) without changing any of
    their other groups. Show the command used.
    8) (4 pts.) What chmod command (using octal mode) would you use to
    allow owner read and write access and group
    read access (and *no* other permissions!) to a file 'foo'? Using chmod
    *without* octal mode, how would you do
    the same?
    9) (2 pts.) What does it mean for a binary to be setuid?
        is setuid a potential security risk?
        Why is this important for tools such as 'passwd'?
    10) (2 pts.) You have the following 'foo' directory:
        drwxr-xr-x 7 jeff cs312 4096 Mar 31 09:15 foo
    What chmod command can you run to ensure files created inside that
    directory will default to having 'cs312' group
    ownership? Assume the user creating the files is in the 'cs312' group.

