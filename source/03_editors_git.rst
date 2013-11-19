========================
Lesson 3: Fun With Files
========================

What we'll discuss
==================
* What's a text editor?
* Features of an editor
* Version control: Git!

What's a text editor?
=====================

.. note:: Quick intro/history:  ed editor
    Pros: low-bandwidth, installed pretty much everywhere, very fast and powerful
    for complicated and repetitive tasks
    Cons: Steep learning curve, different “modes” can be confusing at first

Not an IDE
==========

.. figure:: /static/eclipse_screenshot.gif

Vim, Emacs, etc.
================

* ed -> Vi -> Vim
* Stallman -> lisp -> emacs
* Sublime text recently becoming popular
    * requires license key; NOT OPEN SOURCE


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

Features of an editor
=====================

.. note:: Moving around in a file
    Search / replace
    Text manipulation, ie: cw, dw, c$, yy / p, x, .
* Needs to be installed on your system
* Create files
* Move around within the file
* Add or delete text
* Easily automate tedious tasks

Modes
=====

Command, Insert, Visual

Commands
========

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


