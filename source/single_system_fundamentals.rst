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
* install a package on their VM/partition (Vim)
    * explain what dependencies it also instlled
