================================================
Lesson 4: Scripting, Troubleshooting, & Workflow 
================================================

.. note:: week 1, 1/9/2014
    - log files
    - git bisect, git log, git blame
    - scientific method (small changes)

We want you to learn these concepts early in the course, because you will
constantly need them as we continue.

- Debugging problems
    - Isolate moving parts
    - Test hypotheses
- Don't make it worse
    - Plan ahead
    - Know what will be overwritten/changed by your actions
- Good bug reports
    - How to reproduce
    - Anticipate what they'll do when they get the report
    - Which logs and details will they need?
    - Why is this a problem?
- Zendo


Scripting
=========

What's a script?
----------------

* Piece of code to automate a boring task

What's a scripting language?
----------------------------

.. note:: This is more programming language than scripting specific.
* Compiled vs interpreted

Common Scripting Languages
--------------------------

* Bash
* Python
* Language affects the speed of development and performance of a task
* Most tasks can be done using any language

.. note:: Bash should have some slides here

Python
------

Troubleshooting
===============

Informal method
---------------

* Notice that something isn't working right
* Identify what should be happening
    * Define a success criterion ("it works if...")
* If it used to work: 
    * Determine what changed
        * Git bisect
        * Check for cron jobs or config mgmt.
        * Ask others who've been working on system
* If it has never worked for you:
    * Determine whether it's possible at all
    * Find evidence of similar things working (code, blog posts, stackoverflow)
    * If there's no evidence of anything like this working, you might be Doing It Wrong (tm)
    * If there's documentation of something similar working: 
        * Confirm that the docs are correct for the versions of things that you're using
        * If they docs are wrong, fix them
        * If the docs appear right, figure out what differs between your code and the example
    * If there's sample code, make sure you can run it
        * Your goal is minimum viable test case
* Once you find the problem, fix it if you can
    * If you can't fix the problem, identify why not, and then fix that
    * Ask for help

Formal method
-------------
(from `this <http://my.safaribooksonline.com/book/certification/aplus/9780768694420/pc-technician-essentials/ch01lev1sec3>`_)

* Identify the problem
* Establish a theory of probable cause (question the obvious)
* Test the theory to determine the cause
* Establish a plan of action to resolve the problem and implement the solution
* Verify full system functionality and, if applicable, implement preventative measures
* Document findings, actions, and outcomes

How to get help
---------------

* Don't ask to ask
* Summarize what's wrong
* Summarize what you've tried and why it hasn't worked
* Make a specific request, politely

* Pick the right place & time to ask

Documentation
-------------

* Man pages
* Wikis
* Google (used wisely)
    * Assessing sites' applicablity and reliability

Sources of trouble
------------------

When using something new:

* You probably misunderstood it.
* Maybe their documentation was wrong.
* If neither, then perhaps their code is wrong. 
* Submit a ticket or pull request to fix the docs or code

When something previously working breaks:

* Something changed
* Someone updated something
* Figure out who and why; document


Tickets
=======

* Tickets vs. Issues 
    * Workflow defined by tracker system
    * RT, Redmine, Chiliproject, GitHub issues, mailing lists

* Issues/Bugs are developer work items which need to be included in a release of code
* Tickets are sysadmin work items, often related to systems improvement or maintenance

* Can't log in because your account got reset: Ticket. 
* Can't log in because the newest release of the software is incompatible with
  the old database format: Bug.




