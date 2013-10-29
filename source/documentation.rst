=============
Documentation
=============

SysAdmin Traits
===============
* Lazy: 
    * If you have to do something once, you will very likely have to do it again
    * Script and document as much as possible

* Boring:
    * Avoid setting things up in a special way if at all possible
    * Use defaults whenever you can
    * KISS principle

* Perfectionist
    * Seth: “Think now so you don't have to later (at 4am)”
    * Anticipate potential problems and work them out initially to avoid larger
      issues later

Documentation: Why is it important?
===================================

.. note:: Think of the “getting hit by the bus” situation, how will people
        know how to run your server?

        You can never really have too much documentation

* Training new employees
* Emergencies
* Job changes
* Standardize procedures

What to document: Scripts!
==========================

.. note:: * Don't be that guy everyone hates after you leave the job
          * Odds are someone will have to look at your script

* Comment important functions
* If it's complex, document it
* If you're going to forget it, document it
* The more you document, the better!
* Don't be cryptic!

What to document: Server Standards!
===================================

.. note:: Ideally do this *before* deploying

* Disk layout
* Base applications
* Configuration standards
* Services (httpd, smtp, etc)
* Backup procedures
* Monitoring
* Install check list

What to document: Applications!
===============================

* MySQL, Apache, Postfix
* Configuration
* Log file locations
* Defaults
* Web applications
* Drupal, Trac, Bugzilla
* Upgrade procedures

What to document: Procedures!
=============================

.. note:: * Think if you have to fix something at 4AM, if it was documented it
    would make things better!
        * What happens if all the power goes out? How do you bring everything back
        * online? 
        * Specific hardware/software docs are key!!!

* Server Migrations
* Emergency Procedures
* Upgrades
* Complex services
* Do's & Don'ts
* Hardware Upgrades/Tweaks


Wikis
=====

* Easy to use
* Simple (remember K.I.S.S!)
* Fast
* Which wiki?
    * Dokuwiki
        * No DB requirement, all flat files
* Mediawiki
    * More features, but DB requirement


Commit messages
===============

.. note:: Example: I hit a bug in software and knew I would forget about it.
    So I wrote a whole paragraph with web links to explain to myself why it
    doesn't work. I hit the same bug again and remembered I hit it before and
    found my commit message! 

* Useful and informative but short
* If complex, then describe & document
    * One-off that you may hit in the future?
    * Its like leaving a message to your future self!
* Complete history of a machine

