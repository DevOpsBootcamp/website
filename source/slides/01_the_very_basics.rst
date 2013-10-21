=========================
Lesson 1: The Very Basics
=========================

A note about notation:
======================

* Variables
    * $varname
    * <varname>
* Shell prompt
    * $
    * \`literal stuff in backticks\`
* foo, bar, baz, username, etc.



How to get (to) Linux
=====================

* How many have it already installed?
* Otherwise, PuTTy: 
    * http://www.chiark.greenend.org.uk/~sgtatham/putty/
* Students: 
    * ssh <onidusername>@shell.onid.oregonstate.edu
    * flip{1-3} are Engineering servers; less reliable
* Install VM or dual-boot

The Terminal
============

* Used to mean the keyboard+monitor
    * Now that's a crash cart
* Terminal emulator
* Shell: Use bash; others include csh, zsh, tsch
    * ~/.bashrc

Basic Shell Commands:
=====================

* ls
* cd
* invoke/call an installed program
    * python
* get help for an installed program
    * man <program>

Invoking a script: 
==================

* ls -l
    * permissions later
* chmod +x $filename
* arguments
    * ls -a -l
    * ls -al

File Paths:
===========

* . means current directory
* .. means parent directory
* Tilde (~) means your homedir

Special Characters:
===================

* escape with \ to use them literally
* # means a comment
* ; allows multiple commands per line
* !, ?, \*, &&
* Regular expressions (we'll learn more later)

Type less!
==========

* Reverse-i-search
    * ctrl+r then type command
* aliases
    * ~/.bashrc
* Tab completion

Help, get me out of here!
=========================

* ctrl+c kills/quits
* ctrl+d sends EOF (end-of-file)
* :q gets you out of Vi derivatives and man pages
    * esc - esc - :q if you changed modes
* read what's on your screen; it'll help you
* $ clear

More about Man Pages:
=====================

* the manual (rtfm)
* $ man <program>
* $ man man
* else, $ <program> --help

IRC
===

* Internet Relay Chat
* very old
* Works on everything (no GUI needed)
* standardized, and the people you want to listen to are there

A Client: 
=========

* use irssi
* see lug guide

Networks:
=========

* /connect irc.freenode.net

Channels: 
=========

* /join #osu-lug
* /join #devopsbootcamp

Commands:
=========

* take action with \`/me does thing\`
* everything else starting with / is a command
* /say $thing
* /join, /part, /whois <nick>, /msg, /help <command>


Useful tricks:
==============

* Tab-complete works on nicknames. use it.
* Highlight when people say your name
* Symbols are *not* part of names; they mark status in channel
* Logging (expect it); \`/set autolog on\`

Etiquette:
==========

* Lurk more
* Don't ask to ask
* Show that you're worth helping

Terminology: 
============

* ping/pong
* flapping
* tail
* hat

