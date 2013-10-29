=========================
Lesson 1: The Very Basics
=========================

.. note:: Lance and Emily introduce themselves

Today's Agenda
==============

.. note:: Emily presents

* Getting (to) Linux
* The Terminal & Shell
    * Scripts, file paths, special characters
* Productivity tricks
    * Getting help
* IRC
    * Vocabulary
    * Get connected
    * Etiquette

A note about notation
=====================

.. note:: who presents this slide

* Variables
    * ``$varname``
    * ``<varname>``
* Shell prompt
    * ``$``
    * ```literal stuff in backticks```
* foo, bar, baz, username, etc.

How to get (to) Linux
=====================

.. note:: who presents this slide

* How many have it already installed?
* When stuck on Windows, use PuTTy: 
    * http://www.chiark.greenend.org.uk/~sgtatham/putty/
* Students::

    ssh <onidusername>@shell.onid.oregonstate.edu

* flip{1-3} are Engineering servers; less reliable
* Install VM or dual-boot

Trying Linux on a Virtual Machine
=================================

* Virtual machines act as a full system on a physical machine
* Hypervisors:
    * VirtualBox (free)
    * VMWare (mostly free)
    * KVM (Linux only hosts)
    * Parallels
* Public Cloud Virtual Machines
    * Amazon EC2, Rackspace Cloud, Google Compute Engine, etc
* Easy way to test without breaking your machine!

Installing Linux on Virtualbox
==============================

.. note:: Try other distributions if you like to see what's different. Debian
          is a great next step to try out.

#. Download and install: https://www.virtualbox.org/wiki/Downloads
#. Grab the latest minimal ISO: http://centos.osuosl.org/6/isos/x86_64/
#. Create VM
    #. New -> Name "CentOS" -> Default Ram -> Default Disk settings
    #. Settings -> Storage -> Empty -> CD/DVD Drive -> Select ISO
    #. Start -> press enter -> Skip media check
#. ``\o/``

Vagrant & VirtualBox
====================

.. note:: We're using CentOS as our base image for now but will use Debian
          later. You can see the gui by uncommenting the line in the
          Vagrantfile.

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
==================

.. note:: We'll get into more detail later in how you can access ports on your
          VMs and other use cases.

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
============

.. note:: who presents this slide

* Used to mean the keyboard+monitor
    * Now that's a crash cart
* Terminal emulator
* Shell: Use bash; others include csh, zsh, tsch
    * ``~/.bashrc``

Basic Shell Commands
====================

.. note:: Explain architecture: built in commands vs. external binaries
    Demo commands:
    Directory movement and file manipulation: Cd, pwd, ls, rm, mv, touch
    User info: id, whoami, w
    Pipes, redirection (pipe.txt, redirect.txt)
    Special variables: $?, $$ (pid.sh), !!, !*, !$

* ``ls``
* ``cd``
* invoke/call an installed program
    * python
* get help for an installed program
    * ``man <program>``

Invoking a script
=================

.. note:: who presents this slide. Permissions discussed later.

.. code-block:: bash

    ls -l
    chmod +x $filename

    # arguments
    ls -a -l
    ls -al

File Paths
==========

.. note:: who presents this slide

* ``.`` means current directory
* ``..`` means parent directory
* Tilde (~) means your homedir

Special Characters
==================

.. note:: who presents this slide

* escape with \ to use them literally
* # means a comment
* ; allows multiple commands per line
* !, ?, \*, &&, &
* Regular expressions (we'll learn more later)

Type less
=========

.. note:: who presents this slide

* Reverse-i-search
    * ctrl+r then type command
* aliases
    * ``~/.bashrc``
* Tab completion

Help, get me out of here!
=========================

.. note:: who presents this slide

* ctrl+c kills/quits
* ctrl+d sends EOF (end-of-file)
* :q gets you out of Vi derivatives and man pages
    * esc - esc - :q if you changed modes
* read what's on your screen; it'll help you
* $ clear

More about Man Pages
====================

.. note:: who presents this slide

* the manual (rtfm)::

    $ man <program>
    $ man man

* use `/phrase` to search for `phrase` in the document; `n` for next match
* else::

    $ <program> --help

Documentation
=============

.. note:: Emily

* Man pages, blogs you find by Googling, StackOverflow
* Contribute to community
    * Correct it if it's wrong
    * Remind them what newbies don't know
    * Write your own
* For your future self as well
* Start now

IRC
===

.. note:: who presents this slide

* Internet Relay Chat
* very old
* Works on everything (no GUI needed)
* standardized, and the people you want to listen to are there

A Client 
========

.. note:: Emily switches to terminal and shows example

* use irssi in screen

Networks
========

.. note:: who presents this slide

* /connect irc.freenode.net

Channels
========

.. note:: who presents this slide

* /join #osu-lug
* /join #devopsbootcamp

Commands
========

.. note:: who presents this slide

* take action with \`/me does thing\`
* everything else starting with / is a command
* /say $thing
* /join, /part, /whois <nick>, /msg, /help <command>


Useful tricks
=============

.. note:: who presents this slide

* Tab-complete works on nicknames. use it.
* Highlight when people say your name
* Symbols are *not* part of names; they mark status in channel
* Logging (expect it); \`/set autolog on\`

Screen & Irssi Hints
====================

* Paste with ctrl+shift+v
    * PuTTY defaults to right-click to paste
* to get back, `screen -dr IRC`
* Can you use `man screen` to find out what the d and r flags mean?

Etiquette
=========

.. note:: who presents this slide

* Lurk more
* Don't ask to ask
* Show that you're worth helping
* Read the topic
* Pastebin code

Terminology 
===========

.. note:: who presents this slide

* ping/pong
* flapping
* tail
* hat
* common emotes
    * o/ \o high fives
    * `/me &` means afk
  
Review
======

* What's Linux? 
* How do you open a terminal? 
* How do you run a Python script? 
* How do you list all the files in this directory? 
* Give 2 ways to change directory to your home directory.
* How do you start an irc client?
* How do you reconnect to a screen session?
* Give an example of something not to do in IRC
