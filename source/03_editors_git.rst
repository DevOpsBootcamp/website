===================================
Lesson 3: Editors & Version Control
===================================

Check in from last week
=======================

Is anyone having problems with package management?

Install the packages named git, vim, and emacs


What we'll discuss
==================
* What's a text editor?
* Features of an editor
* Version control: Git!


How do you edit files?
======================

.. figure:: /static/word_screenshot.gif

==============================================
No. Never, Ever edit code in Word/LibreOffice.
==============================================

* Autocorrect is your worst enemy
* Syntax highlighting is nice

Then what should you use?
=========================

* Text editors
    * Command-line
    * available in your package manager
* For coding, an IDE can be helpful   

Integrated Development Environments
===================================

.. figure:: /static/eclipse_screenshot.gif

* Entire toolchain in one place
* Almost always graphical

Sysadmin tools
==============

* Frequently work with remote machines over a ssh connection
    * xforwarding can sort of give you a GUI
    * Not all remote machines have a desktop environment
* Faster to edit file in place than transfer it down then back up
    * Frequent small changes when testing or debugging
* Broken machines often have only terminal via crash cart

Editor Requirements:

* Small program
* Runs in terminal
* Preferably installed by default on most systems


Features of an editor
=====================

* Needs to be installed on your system
* Create files
* Move around within the file
* Add or delete text
* Easily automate tedious tasks

Text Editors
============

.. note:: Quick intro/history:  ed editor
    Pros: low-bandwidth, installed pretty much everywhere, very fast and powerful
    for complicated and repetitive tasks
    Cons: Steep learning curve, different “modes” can be confusing at first

* ed -> Vi -> Vim
* Stallman -> lisp -> emacs

* Avoid: 
    * pico/nano
    * SublimeText

Emacs
=====

.. note:: Originally released 1976
    name from Editor MACros for TECO editor, originally Tape Editor and
    COrrector at MIT in the '60s

But, along the way, I wrote a text editor, Emacs. The interesting idea about
Emacs was that it had a programming language, and the user's editing commands
would be written in that interpreted programming language, so that you could
load new commands into your editor while you were editing. You could edit the
programs you were using and then go on editing with them. So, we had a system
that was useful for things other than programming, and yet you could program
it while you were using it. I don't know if it was the first one of those, but
it certainly was the first editor like that.

 -- Richard Stallman, http://www.gnu.org/gnu/rms-lisp.html

Vim
===

.. note:: originally written for Amiga systems (Commodore PCs), 1988
    vim released 1991
    vimscript, Lua (as of Vim 7.3), Perl, Python, Racket, Ruby, Tcl (tool
    command language).
    vi written by Bill Joy in 1976, visual mode for line editor called ex 
    line editors are from age of teleprinters, no cursors

* Available almost everywhere
* Lightweight
* Design decisions explained in http://docs.freebsd.org/44doc/usd/12.vi/paper.html
* Modal editor (command, insert, visual)

How to choose
=============

* What can the people around you help with?
* Try both
* Choose one and get good at it
* Have a good answer when people ask why you made that choice
    * "Because it's familiar" is tolerated
    * "Because I was initially taught it" is common but accepted (honesty)
    * "Because $usecase" provokes argument but more respected
    * "Because I tried both and picked this one" is rare but good
* Your use case as a sysadmin
ks

Modes
=====

Command, Insert, Visual

Commands
========

.. note:: Moving around in a file
    Search / replace
    Text manipulation, ie: cw, dw, c$, yy / p, x, .

.. figure:: /static/vim_cheatsheet.gif

Configuration/customization
===========================

* .vimrc
* :set

Regular expressions (questions to ask)
======================================

You should know basic substitution: 

.. code-block:: bash

    :%s/foo/bar/g

This is not `shell globbing <http://tldp.org/LDP/abs/html/globbingref.html>`_

Editor questions?
=================

* Open an editor, find a cheat sheet, try to add some text
* Modify the text: "disemvowel" it

.. code-block:: bash
    $ vim testvim.txt            $ emacs testemacs.txt
    <i>                          Hello world!
    Hello world!                 <alt + x> replace-regexp
    <esc>                        [aeiou]
    :s/[aeiou]//g                <enter>
    :wq                          <ctrl + x> <ctrl + c>

Version control: Git!
=====================

Why you need it
===============

Basic concepts
==============

How to start a repo
===================

How to add and commit changes
=============================

How to apply others' changes to your work
=========================================

Branching/merging
=================

"Help, I broke everything!"
===========================


