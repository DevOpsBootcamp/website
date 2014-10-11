Session 2: Linux Basics
=========================

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
* IRC
    * Setup and etiquette
    
    
Operating Systems
-----------------

.. figure:: /static/os.gif
    :align: right

* What is an OS
* GNU/Linux, BSD, Windows, OS X, Plan 9
* Different use cases - desktop, server, phone

The Terminal
------------

.. figure:: /static/crashcart.jpg
    :align: right
    :scale: 75%

* Used to mean the keyboard+monitor
    * Now that's a crash cart
* Terminal emulator
* Shell: Use bash; others include csh, zsh, tsch
    * ``~/.bashrc``

.. figure:: /static/televideo_terminal.jpg
    :align: right
    :scale: 40%

.. figure:: /static/teletype_terminal.jpg
    :align: left

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

* ``ls``, ``cd``, ``cat``, ``echo``
* invoke/call an installed program
* get help: ``man <program>``

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

Type less
---------

* Reverse-i-search
    * ctrl+r then type command
* aliases
    * ``~/.bashrc``
* Tab completion

.. figure:: /static/space_cadet_keyboard.gif
    :align: center
    :scale: 75%

Automation > Typing > Mouse

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

More about Man Pages
--------------------

* the manual (rtfm)::

    $ man <program>
    $ man man

* use ``/phrase`` to search for ``phrase`` in the document; ``n`` for next match
and ``N`` for previous match
* else::

    $ <program> --help

Documentation
-------------

Man pages, blogs you find by Googling, StackOverflow

.. figure:: /static/google.gif
    :align: center
    :scale: 50%

*  Contribute to community
    * Correct it if it's wrong
    * Remind them what newbies don't know
    * Write your own
* For your future self as well
* Start now

Asking for help
---------------

It's okay to ask.

#. What should be happening?
#. What's actually happening?
#. Google it
#. Skim the manuals of each component
#. Identify a friend, mentor, or IRC channel who could help
#. When they're not busy, give them a quick synopsis of points 1 and 2,
   mentioning what possibilities you've ruled out by searching.

**Contributions = expertise + time**

Don't waste experts' time, but do build your expertise.

Review
------

* What's Linux?
* How do you open a terminal emulator?
    * this varies between window managers
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
* Shell
* Usually (but not always) password
* Usually (but not always) home directory



Managing users
--------------

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
---------

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
--------------

* UID 0
* ``sudo``

.. figure:: /static/xkcd149.png
    :align: center

Acting as another user
----------------------

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

Hands-On: Users and Groups
--------------------------

.. note:: To give yourself sudo powers do the following:

  #. Add your user to the ``wheel`` group using ``gpasswd``.
  #. As the root user, use ``visudo`` and uncomment this line::

      %wheel  ALL=(ALL)   ALL

  #. Save the file and now you should have sudo!

  *We'll cover sudo in more depth at a later time.*

* Create a user on your system for yourself, with your preferred username
* Give your user sudo powers
* Use su to get into your user account
* Change your password
* Create a directory called bootcamp in your home directory
* Create a group called devops


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

Hands-On: Files and Permissions
-------------------------------

.. code-block:: bash
   
    $ touch foo # create empty file called foo

* As root, create a file in /home/$yourusername/bootcamp
* Who can do what to the file?
* Make the devops group own the file
* Make a file called allperms and give user, group, and world +rwx
* Make more files and practice changing their permissions

Package Management
------------------

*Take care of installation and removal of software*

**Core Functionality:**
* Install, Upgrade & uninstall packages easily
* Resolve package dependencies
* Install packages from a central repository
* Search for information on installed packages and files
* Pre-built binaries (usually)
* Find out which package provides a required library or file

**Popular Linux Package Managers**
* .deb / APT + dpkg (used by Debian, Ubuntu, Linux Mint)
* .rpm / YUM + rpm (used by RedHat, CentOS, Fedora)

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
.. 
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
* Nix -- Fancy functional/ transactional
* brew (OS X)
* chocolatey (Windows)

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
  $ ./configure --prefix=$HOME/programs/
  $ make
  $ make install

Hands-on: Package Management
----------------------------

* Install the ``git`` package
* Query the RPM/APT database for installed packages
* List the files in an installed package
* Remove the ``git`` package

Review
------

* read example output of ls -al
* read output of yum or aptitude search
* install a package on their VM/partition (Vim, Git)
    * explain what dependencies it also installed

IRC
---

.. figure:: /static/multiple_networks.gif
    :scale: 40%
    :align: center

* Internet Relay Chat
* Very old (RFC 1459 May 1993)
* Works on everything (no GUI needed)
* The people you want to listen to are there
* Oregon State ran one of the first servers ever!

A Client
--------

.. note:: Switch to a terminal and show example

Use irssi or weechat in screen

.. code-block:: bash

    # This step is optional, but persistent IRC is cool
    $ ssh <username>@<preferred shell host>

    # start screen with the name 'irc'
    $ screen -S irc

    # start your client in the 0th window of the screen session
    $ irssi
    # or
    $ weechat-curses

    # exit irc screen with CTRL+a, CTRL+d
    # exit ssh session with CTRL+d or 'exit'
    # to get back to irc:
    $ ssh <username>@<preferred shell host>
    $ screen -dr IRC

Networks
--------

.. figure:: /static/multiple_networks.gif
    :scale: 30%
    :align: center

::

    /connect irc.freenode.net

    /nick <myawesomenickname>
    /msg nickserv register <password> <email>

    /nick <myawesomenickname>
    /msg nickserv identify <password>

Channels
--------

::

    /join #osu-lug
    /join #devopsbootcamp

:``/list``:
  - tells all channels on network
  - Don't do this on Freenode!
:``/topic``: tells you the current channel's topic
:``/names``: tells you who's here

Commands
--------

* take action with ``/me does thing```
* everything else starting with / is a command

::

    /say $thing
    /join, /part, /whois <nick>, /msg, /help <command>

Note that nothing shows up in the channel when you run a ``/whois`` command; it
shows up either in your status buffer or your conversation with the person.

.. rst-class:: codeblock-sm

::

    12:04 -!- _test_ [~test@c-50-137-46-63.hsd1.or.comcast.net]
    12:04 -!-  ircname  : Example User
    12:04 -!-  channels : #ExampleChannel
    12:04 -!-  server   : moorcock.freenode.net [TX, USA]
    12:04 -!-  hostname : c-50-137-46-63.hsd1.or.comcast.net 50.137.46.63
    12:04 -!-  idle     : 0 days 0 hours 2 mins 38 secs [signon: Wed Nov  6
    12:00:30
                          2013]
    12:04 -!- End of WHOIS

Useful tricks
-------------

* Tab-complete works on nicknames. use it.
* Highlight when people say your name
* Symbols are *not* part of names; they mark status in channel (such as @)
* Logging (expect it); \`/set autolog on\`
* chanserv and nickserv are good bots to know
    * hamper is also a bot

Screen & Irssi Hints
--------------------

* Paste with ctrl+shift+v
    * PuTTY defaults to right-click to paste
* to get back, ``screen -dr IRC``
* Can you use ``man screen`` to find out what the d and r flags mean?

::

 SCREEN(1)                                                               SCREEN(1)

 NAME
        screen - screen manager with VT100/ANSI terminal emulation

 SYNOPSIS
        screen [ -options ] [ cmd [ args ] ]
        screen -r [[pid.]tty[.host]]
        screen -r sessionowner/[[pid.]tty[.host]]
 Manual page screen(1) line 1 (press h for help or q to quit)

Etiquette
---------

* Lurk more
* Don't ask to ask
    * Lure help out of hiding with tasty details of problem
* Show that you're worth helping
* Read the topic
    * ``/topic``
    * Output only shows up in your channel, not to everyone else
* Pastebin code
* Choose your nick carefully

Terminology
-----------

* ping/pong
* flapping

.. figure:: /static/jargon.jpg
    :align: right
    :scale: 50%

* tail
* hat
* nick
* netsplit
* kick/ban/k-line
* common emotes
    * ``o/`` AND  ``\o`` high fives
    * ``/me &`` means afk

Review
------

* How do you start an irc client?
    * How often should you need to start your IRC client?
* How do you reconnect to a screen session?
* Give an example of something which you should not do in IRC
