Lesson 13: Contributing to Open Source
======================================

Getting started in Open Source
------------------------------

* `Carlos's CS419 in a nutshell`__
* Relevant books 
    * `The cathedral and the bazaar (Eric Raymond)`__
    * `Producing Open Source Software (Karl Fogel)`__
    * `Open Advice (Lydia Pintscher)`__

.. __: http://classes.engr.oregonstate.edu/eecs/spring2014/cs419-003/
.. __: http://www.catb.org/~esr/writings/homesteading/cathedral-bazaar/cathedral-bazaar.ps
.. __: http://producingoss.com/
.. __: http://open-advice.org/Open-Advice.pdf

Joining vs Starting a Project
-----------------------------
|

.. figure:: static/cowbrush.gif
    :align: right

* Scratch an itch.
* Research first
* Revive dead project vs. rewrite
* Get involved with communities even if you plan to start your own
    * Learn from their examples

Know your licenses
------------------

.. note::

    I am not a lawyer. 

    http://opensource.org/licenses is pretty cool

    " Freely used, modified, and shared"

    :MIT/X11:
      Short, permissive, says attribution and no liability. Doesn't discuss
      copyright. Can convert to Apache 2

    :Apache:
      Short, permissive, goes in every file, grants patent rights from
      contributors to users, author keeps copyright. Plays nice with GPL3 (?)

    :BSD: Attribution, keep copyright, no liability

    :AGPL:
      Demands source distribution even when software not distributed (for
      cloud/hosted)

    :GPL:
      Viral, copyleft. Viral = infects entire program if it links to GPL library
      or uses a single line of GPL'd code

    :LGPL: Fixes library linking issue with GPL
    
    :CC: Non-code content

.. figure:: static/licensing.jpg
    :align: right
    :scale: 25%

* MIT/X11
* Apache
* BSD
* AGPL/GPL/LGPL
* Creative Commons
* http://choosealicense.com/

Assessing a new community
-------------------------

* Elitism vs welcomeness
* Communication style
* Documentation and guides
* Faster or slower change?

.. figure:: static/welcome_mat.jpg
    :align: center
    :scale: 30%

Getting involved
----------------

.. figure:: static/keeptrying.png
    :align: right
    :scale: 60%

* Lurk more
* Make accounts
    * Mailing lists
    * IRC channels
    * Wikis
    * Issue trackers
* Your nick is your reputation
* It's okay to make mistakes... But learn from them.

Finding a project
-----------------

.. note::
  First contributions will be metric of how nice they are to newbies

  There's a thing where older project members get grumpy at newbies because
  they've answered the question over and over... read docs/faq then improve them

.. figure:: static/osslogos.jpg
    :align: right 
    :scale: 60%

* Openhatch
* Easy bugs
* GSOC submitters who didn't get enough interns
* Search by language
* Search by project type -- find something that interests you (web dev?
  bioinformatics? video games?)
* Your immediate payment for contributions will be satisfaction, so pick
  something satisfying

First steps
-----------
|

.. figure:: static/babypenguin.gif
    :align: center 

.. note::
  It will feel like you have only a vague idea what you're doing. This means
  you've found a project that's challenging and that you'll learn from.

* Lurk awhile then ask
* Write a test
* Fix a typo
* Deploy and update the installation docs

DevOps Concerns
---------------

.. figure:: static/devops_all_the_things.jpg
    :align: right
    :scale: 70%

* Configurations often managed in public repos
* Root can't be handed out to just anyone
* Build trust, contribute to project consistently
* Practice with the tools they use

Your Homework
-------------

* Find a project that you'd like to get involved with this summer
* Join IRC, mailing lists, etc.
* Pull the code and run its tests using what you've learned
* Find something you can contribute to the project
* Discuss how it's going in ``#devopsbootcamp`` on irc.freenode.net

Questions?
----------

Any questions about anything from this year? 

* Conferences: OSBridge, OSCON may have free expo hall passes
* In Corvallis? Want to come to the OSL and see what we do, pair program, etc.?
* No meeting next week -- `please leave feedback!`_

.. _please leave feedback!: https://docs.google.com/forms/d/14wO3fq80bIWCJDfnE1rYy2w_D7DP_Vu6i6Eul6sXIAk/viewform
