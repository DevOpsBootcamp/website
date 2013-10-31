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
* Backups
    * What should you back up?
    * The easier solutions for an individual user

What are users?
===============

* You, right now

* ``whoami``, ``who``, ``w``, ``id``

* Not just people: Apache, Mailman, ntp

Users have
----------

* Username
* UID
* Usually (but not always) password
* Usually (but not always) home directory

Managing users
--------------

* ``/etc/passwd``

* ``useradd`, ``userdel``, ``usermod``
* ``passwd``

Passwords
---------

* ``/etc/shadow``, not ``/etc/passwd``
* What the fields mean
* Expire or disable (``chage``)

Root/Superuser
--------------

* UID 0
* ``sudo``


What are groups?
================

* Manage permissions for groups of users
* ``groupadd``
* ``usermod``, ``groupmod``


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


ls -al
------

* First bit: type
* Next 3: user
* Next 3: group
* Next 3: world

* user & group

chmod and octal permissions
---------------------------

[table of translations goes here]

chown
-----

user & group

umask
-----

defaults when creating files

Acting as another user
----------------------

If someone has permissions errors: 
    * Check that they or their group owns the files
    * Check that they have the flag 

Packages
========

Why you need them: Installing software

Dependencies
------------

what your software needs to run

examples

Package Manager
---------------

* Comes with your distro
* Usually pre-built packages
* Exceptions: 
    * portage (builds it for you)
    * pypi (distro-agnostic)

CentOS: yum
------------

* search
* install
* remove

Ubuntu/Mint: Apt
----------------

* search
* install
* remove

Other ways to install stuff
---------------------------

* source then compile
* prebuilt, download


Backups
=======

* Anything you customized
* system-specific config files
* Home directories

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

