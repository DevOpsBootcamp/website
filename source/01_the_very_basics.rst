=========================
Lesson 1: The Very Basics
=========================

.. note:: Lance and Emily introduce themselves

A note about notation:
======================

.. note:: who presents this slide

* Variables
    * $varname
    * <varname>
* Shell prompt
    * $
    * \`literal stuff in backticks\`
* foo, bar, baz, username, etc.

How to get (to) Linux
=====================

.. note:: who presents this slide

* How many have it already installed?
* Otherwise, PuTTy: 
    * http://www.chiark.greenend.org.uk/~sgtatham/putty/
* Students: 
    * ssh <onidusername>@shell.onid.oregonstate.edu
    * flip{1-3} are Engineering servers; less reliable
* Install VM or dual-boot

Vagrant & VirtualBox
====================

.. note:: Lance, please fill in as many slides as you need for this tutorial.
          Their homework for this week is to have tried to install Linux, but
          they may not all have succeeded. 

The Terminal
============

.. note:: who presents this slide

* Used to mean the keyboard+monitor
    * Now that's a crash cart
* Terminal emulator
* Shell: Use bash; others include csh, zsh, tsch
    * ~/.bashrc

Basic Shell Commands:
=====================

.. note:: who presents this slide

* ls
* cd
* invoke/call an installed program
    * python
* get help for an installed program
    * man <program>

Invoking a script: 
==================

.. note:: who presents this slide

* ls -l
    * permissions later
* chmod +x $filename
* arguments
    * ls -a -l
    * ls -al

File Paths:
===========

.. note:: who presents this slide

* . means current directory
* .. means parent directory
* Tilde (~) means your homedir

Special Characters:
===================

.. note:: who presents this slide

* escape with \ to use them literally
* # means a comment
* ; allows multiple commands per line
* !, ?, \*, &&, &
* Regular expressions (we'll learn more later)

Type less!
==========

.. note:: who presents this slide

* Reverse-i-search
    * ctrl+r then type command
* aliases
    * ~/.bashrc
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

More about Man Pages:
=====================

.. note:: who presents this slide

* the manual (rtfm)
* $ man <program>
* $ man man
* else, $ <program> --help

IRC
===

.. note:: who presents this slide

* Internet Relay Chat
* very old
* Works on everything (no GUI needed)
* standardized, and the people you want to listen to are there

A Client: 
=========

.. note:: who presents this slide

* use irssi
* see lug guide

Networks:
=========

.. note:: who presents this slide

* /connect irc.freenode.net

Channels: 
=========

.. note:: who presents this slide

* /join #osu-lug
* /join #devopsbootcamp

Commands:
=========

.. note:: who presents this slide

* take action with \`/me does thing\`
* everything else starting with / is a command
* /say $thing
* /join, /part, /whois <nick>, /msg, /help <command>


Useful tricks:
==============

.. note:: who presents this slide

* Tab-complete works on nicknames. use it.
* Highlight when people say your name
* Symbols are *not* part of names; they mark status in channel
* Logging (expect it); \`/set autolog on\`

Etiquette:
==========

.. note:: who presents this slide

* Lurk more
* Don't ask to ask
* Show that you're worth helping

Terminology: 
============

.. note:: who presents this slide

* ping/pong
* flapping
* tail
* hat
* common emotes
    * o/ \o high fives
    

