Lesson 1: The Very Basics
=========================

Today's Agenda
--------------

* Getting (to) Linux
* The Terminal & Shell
    * Scripts, file paths, special characters
* Productivity tricks
    * Getting help

.. figure:: /static/Tux.png
    :align: right

* IRC
    * Vocabulary
    * Get connected
    * Etiquette

A note about notation
---------------------

.. figure:: /static/stickynote.png
    :align: right
    :scale: 20%

* Variables
    * ``$varname``
    * ``<varname>``
* Shell prompt
    * ``$``
    * ```literal stuff in backticks```
* foo, bar, baz, username, etc.

How to get (to) Linux
---------------------

.. figure:: /static/dualboot.png
    :align: right
    :scale: 40%

* How many have it already installed?
* Install VM or dual-boot
* When stuck on Windows, use `PuTTy`_:
* Students::

    ssh <onidusername>@shell.onid.oregonstate.edu


.. figure:: /static/osm_server.jpg
    :align: right
    :scale: 50%

* flip{1-3} are Engineering servers; less reliable

.. _PuTTy: http://www.chiark.greenend.org.uk/~sgtatham/putty/

Trying Linux on a Virtual Machine
---------------------------------

Virtual machines act as a full system on a physical machine

.. figure:: /static/virtualbox.png
    :align: right
    :scale: 50%

* Hypervisors:
    * VirtualBox (free)
    * VMWare (mostly free)
    * KVM (Linux only hosts)
    * Parallels
* Public Cloud Virtual Machines
    * Amazon EC2, Rackspace Cloud, Google Compute Engine, etc
* Easy way to test without breaking your machine!

Installing Linux on Virtualbox
------------------------------

.. note:: 
  Try other distributions if you like to see what's different. Debian is a great
  next step to try out.

#. Download and install: https://www.virtualbox.org/wiki/Downloads
#. Grab the latest minimal ISO: http://centos.osuosl.org/6/isos/x86_64/
#. Create VM
    #. New -> Name "CentOS" -> Default Ram -> Default Disk settings
    #. Settings -> Storage -> Empty -> CD/DVD Drive -> Select ISO
    #. Start -> press enter -> Skip media check
#. ``\o/``

Vagrant & VirtualBox
--------------------

.. note::
  We're using CentOS as our base image for now but will use Debian later. You
  can see the gui by uncommenting the line in the Vagrantfile.

* Vagrant is a tool used with Virtualbox (and other) platforms
* Make a reproducible pre-installed Linux environment
* Download and install: http://www.vagrantup.com/
* Clone our repo, start and access the vm:

.. code-block:: bash

    # clone
    git clone https://github.com/DevOpsBootcamp/devopsbootcamp-vagrant.git

    # start up
    cd devopsbootcamp-vagrant
    vagrant up

    # access vm
    vagrant ssh

Vagrant cheat sheet
-------------------

.. note::
  We'll get into more detail later in how you can access ports on your VMs and
  other use cases.

.. code-block:: bash

    # start
    vagrant up

    # stop
    vagrant halt

    # destroy (remove vm)
    vagrant destroy

    # ssh to the vm
    vagrant ssh

Also check out the `Vagrant Documentation
<http://docs.vagrantup.com/v2/cli/index.html>`_ for more information.

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

.. figure:: /static/pylogo.png
    :align: right
    :scale: 75%

* ``ls``, ``cd``, ``cat``, ``echo``
* invoke/call an installed program
* get help: ``man <program>``

::

    test@x230 ~ $ tree
    .
    ├── Documents
    │   ├── Code
    │   │   └── scripts
    │   │       └── test.sh
    │   ├── School
    │   └── Work
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

**Arguments** are extra information that you pass to a script or program when
you call it. They tell it in more detail what you want to do.

.. code-block:: bash

    $ ls -a -l
    $ ls -al

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
    test@x230 ~/Documents $


.. note::
  root directory is not to be confused with a home directory for the root
  account

Special Characters
------------------

* escape with ``\`` to use them literally
* # means a comment
* ; allows multiple commands per line
* !, ?, \*, &&, &
* Regular expressions (we'll learn more later)

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
    │   ├── Code
    │   │   └── scripts
    │   │       └── test.sh
    │   ├── School
    │   └── Work
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

IRC
---

.. figure:: /static/multiple_networks.gif
    :scale: 40%
    :align: center

* Internet Relay Chat
* Very old (RFC 1459 May 1993)
* Works on everything (no GUI needed)
* The people you want to listen to are there

A Client
--------

.. note:: Switche to a terminal and show example

Use irssi in screen

.. code-block:: bash

    # This step is optional, but persistent IRC is cool
    $ ssh <username>@<preferred shell host>

    # start Screen
    $ screen -S irc

    # start your client
    $ irssi

    # after ending ssh session, to get back:
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
* Symbols are *not* part of names; they mark status in channel
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

* What's Linux?
* How do you open a terminal emulator?
    * This varies between window managers
* I have the script ``test.py``. How do I run it??
* How do you list all the files in the current directory?
* Give 2 ways to change directory to your home directory.
* How do you start an irc client?
    * How often should you need to start your IRC client?
* How do you reconnect to a screen session?
* Give an example of something which you should not do in IRC
