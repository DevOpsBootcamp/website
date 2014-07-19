Lesson 4: Scripting, Troubleshooting, & Workflow
================================================

.. note:: week 1, 1/9/2014
    - log files
    - git bisect, git log, git blame
    - scientific method (small changes)

Agenda
------

* Scripting
    * What's a script?
    * What's a scripting language?
    * Common scripting languages
    * Bash & Python examples
* Troubleshooting
    * Techniques
    * Examples
* Workflow
    * Life cycle of a bug

Scripting
---------

What's a script?
----------------

.. figure:: static/xkcd_1205.png
    :align: right
    :scale: 75%

* Piece of code to automate a boring task
* Explanation of how to do what you do

What's a scripting language?
----------------------------

.. note:: This is more programming language than scripting specific.

* Compiled vs interpreted
* Expresses logic and actions
    * Logic: loops, conditionals, statements
    * Actions: File I/O, print to console, interact with system utilities

Common Scripting Languages
--------------------------

* Bash
* Python
* Language affects the speed of development and performance of a task
* Most tasks can be done using any language

Bash
----

* Adds a bit of logic to automate your shell commands
* Saves re-typing things
* Powered by the tools you invoke from the shell
* Scripts can be hard to read at first because they call to external utilities

Python
------

.. figure:: static/xkcd_353.png
    :align: center
    :scale: 80%

Why Python?
-----------

* Easy to read
* Easy to maintain
* Quick to write
* Lots of libraries

Troubleshooting
---------------

.. figure:: static/xkcd_627.png
    :align: center
    :scale: 65%

Informal method
---------------

.. figure:: static/xkcd_349.png
    :align: right
    :scale: 60%

* Notice that something isn't working right
* Identify what should be happening
    * Define a success criterion ("*it works if...*")

If it used to work
------------------

.. figure:: static/xkcd_1172.png
    :align: right

* Determine what changed
    * Version control history (Git bisect)
    * Emails from the system? Logs? (Check for cron jobs or config mgmt)
    * Ask others who've been working on system
* Use your own notes/documentation


If it's never worked for you
----------------------------

* Determine whether it's possible at all
* Find evidence of similar things working (code, blog posts, stackoverflow)
* If there's no evidence of anything like this working, you might be Doing It
  Wrong (tm)
* If there's documentation of something similar working:
    * Confirm that the docs are correct for the versions of things that you're
      using
    * If they docs are wrong, fix them
    * If the docs appear right, figure out what differs between your code and
      the example
* If there's sample code, make sure you can run it
    * Your goal is minimum viable test case

After finding the problem
-------------------------

.. figure:: static/xkcd_806.png
    :align: right
    :scale: 50%

* Did the docs tell you how to fix it?
* If you can't fix the problem, identify why not, and then fix that
* Ask for help
    * Expert takes 5 minutes to answer a well-asked question
    * Newbie can waste hours

Formal method
-------------
(from `this`__)

* Identify the problem
* Establish a theory of probable cause (question the obvious)
* Test the theory to determine the cause
* Establish a plan of action to resolve the problem and implement the solution
* Verify full system functionality and, if applicable, implement preventative measures
* Document findings, actions, and outcomes

.. __: http://my.safaribooksonline.com/book/certification/aplus/9780768694420/pc-technician-essentials/ch01lev1sec3

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
    * Assessing sites' applicability and reliability
        * Who wrote it?
        * When?
        * Is the other content reliable?
        * Is feedback from others visible? If so, what does it say?

Sources of trouble
------------------

:When using something new:
  * You probably misunderstood it.
  * Maybe their documentation was wrong.
  * If neither, then perhaps their code is wrong.
  * Submit a ticket or pull request to fix the docs or code

:When something previously working breaks:
  * Something changed
  * Someone updated something
  * Figure out who and why; document

Tickets
-------

* Ticket (often sysadmin) or Issue (often developer)
* Ticket comes into tracking system, submitted by a user
* Triage
    * Add details to tickets; consolidate duplicates
    * Contact submitter if more info needed
    * Add tags, milestones, priority, etc.
* Ticket is assigned to someone, who fixes it
* Someone else confirms that the fix works, then ticket is closed

Tickets vs. Issues
------------------

* Workflow defined by tracker system
    * RT, Redmine, Chiliproject, GitHub issues, mailing lists
* Issues/Bugs are developer work items which need to be included in a release of
  code
* Tickets are sysadmin work items, often related to systems improvement or
  maintenance
* Can't log in because your account got reset: Ticket.
* Can't log in because the newest release of the software is incompatible with
  the old database format: Bug.

Some Examples
-------------

- Trac
- Chiliproject
- RT
- Bugzilla
