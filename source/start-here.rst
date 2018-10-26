.. _start_here:


Lesson 0: Start Here
====================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/start-here.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/start-here.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - Definitions:
        - System Administration / Engineers
        - DevOps
        - DevOps BootCamp
    - Who teaches DOBC
    - Why you should go to DOBC
    - The 'Agreement'
    - Getting involved

About the Program
-----------------

.. image:: /static/devops.jpg
    :alt: OSU OSL Promotional Photo
    :align: center

Definition: *System Administration*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: build

* Responsible for systems (typically servers) running code, applications,
  and services

  - Keeping applications running (they crash, sometimes a lot)
  - Updates, Security
  - Monitoring, Logging
* Automates significant amounts of work with infrastructure

  - This enables a small team to administer hundreds or thousands of
    servers

* Involved in infrastructure architecture and decisions
* Can be involved in QA/Development work as well

Definition: *System Engineers*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: build

* Responsible for creating the platforms code is run on

  - Work at a lower-level
  - Generally make infrastructure decisions for others
  - Often have expertise with some particular sub-system (networking, filesystems, etc)
  - Not necessarily on-call, but can be

* Sometimes intermixed with Systems Administrators who want Engineer in their title

Definition: *DevOps Engineers*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: build

* Newer position
* Mix of Systems (Operations) and Development work
* Involved where the application and its platform meet
* Responsibilities include a mix of both Ops and Dev, usually:

  - General infrastructure/automation
  - Continuous Integration and Testing
  - Developer Environments/Workflow
  - Logging
  - Often on-call

Definition: *Site Reliability Engineers (SRE)*
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: build

* SRE and DevOps Engineers share the same foundational principles
* SRE is viewed as a "specific implementation of DevOps with some idiosyncratic extensions"
* SRE was originally created at Google as a process to improve managing their services
* Most large tech companies now follow SRE processes

*DevOps*
~~~~~~~~

.. ifnotslides::

    DevOps can mean a lot of thing to a lot of people, and in the grand scheme
    of *Computer Science* it's a relatively new term.  One definition you can
    always get a way with is this:

.. highlights::

    **DevOps** is a field which takes skills from **Software Development** and
    **Operations Engineering** to create and run applications more
    effectively.

    TLDR: Development + Operations == Better Services

.. rst-class:: build

  DevOps defines 5 key pillars of success:

  1. Reduce organizational silos
  2. Accept failure as normal
  3. Implement gradual changes
  4. Leverage tooling and automation
  5. Measure everything

.. ifnotslides::

    In a pre-DevOps world the jobs of Devs and Ops were separate:
        - There was a clearly defined and relatively standardized interface
          between the two.
        - Workflows were slower, meaning there was more time to troubleshoot and
          debug.

    In a Post-DevOps world we have a new hybrid job:
        - Software is released faster via **Agile Development**.
        - Larger scale services means companies need many identical servers,
          spawning **Configuration Management** tools.
        - Devs need to know ops skills to better tests their projects and to
          anticipate issues when it comes to deploying the application.
        - Ops need to know development skills to minimize wasted resources and
          to improve security of the applications and the servers those apps
          run on.


What *DevOps BootCamp* (DOBC) is
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    **TLDR: Couch to DevOps in 1 school year**

DOBC is a free education program offering:
    - **Mentors** teaching DevOps related tools and concepts.
    - **A challenge** for anybody willing to put in the effort.
    - One-on-one **Apprenticeship**.
    - **Hands-on** training and lectures
    - **Free and Open Source course** materials!

.. ifnotslides::

    **DOBC will meet about twice monthly** for in-person lectures and hands-on
    activities.  **All course materials are available from the start** for
    those who are self-guided and want to work ahead.

    Check the schedule for more information.


What DOBC is *not*
~~~~~~~~~~~~~~~~~~

DevOps BootCamp is not:
    - A for-credit OSU class
    - A Student job
    - Easy

.. ifnotslides::

    DOBC is a free course for all types of students. If you want to attend
    online, in person, or just want help on IRC you are welcomed and encouraged
    to participate.

    While the course does not go on your academic transcript, the skills you
    learn and the course itself can (and should) go on you Resume.  The many
    benefits of DOBC will be discussed and brought up throughout the course.


Why DOBC Exists
~~~~~~~~~~~~~~~

DOBC was created because the OSU OSL:
    #. **Merged** with the school of **EECS**.
    #. Wanted to help students **meet Company demands and expectations** of
       recent graduates.
    #. Needed to **bridge the “Skills Gap”** of the OSU EECS curriculum.
    #. Wanted to build a **DevOps Learning community**.

.. ifnotslides::

    The OSU Open Source Lab has become part of the OSU School of EECS so this
    program was created in an effort to contribute *directly* to the learning
    community by sharing our knowledge in a useful and constructive way.

    In teaching OSU Students (and anybody else who wants to learn) we hope to
    give more people a chance reach employment in the growing and exciting
    industries around DevOps.


What You Will do
~~~~~~~~~~~~~~~~

You will Learn:
    - Linux systems
    - Networking
    - Software development
    - Tools and why they matter

.. ifnotslides::

    DOBC focuses on teaching conceptual understanding over wrought memorization
    of commands to get a particular job done. This means that we will be
    addressing the why and what am I doing much more often than the how and
    what do I type.

You will build:
    - Functioning applications on the cloud
    - Cloud infrastructures

.. ifnotslides::

    The tools of industry change every year, but the way we tackle problems
    changes much more slowly. DOBC focuses on learning **how** and **why** in
    problem solving over the **what**.  That doesn't mean we won't mess with
    code and servers, it just means we'll talk about what and why we're doing
    something too!


Who Teaches DOBC
~~~~~~~~~~~~~~~~

The teachers of DOBC include:
    - OSL Students
    - OSL Faculty
    - Guests from *The Industry*
    - You!

.. ifnotslides::

    The OSL employs ~20 part-time students who are all equipped to answer
    questions and teach this course. Many of your lecturers and activity
    assistants were once DOBC students and are now gainfully employed by the
    OSL.

    We also bring in guest speakers in from time-to-time to talk about a
    specific topic. These guest lectures may not be as interactive as other
    lessons, but meeting and talking with industry experts is a valuable
    experience you should take.

    We also encourage asking questions and students contributing to the course.
    If you learned something interesting share it with your peers and during
    class. At the very least ask questions; you’re not the only one who's
    confused.

Bi-Weekly Labs
~~~~~~~~~~~~~~

.. ifnotslides::

  Following the Fall Kickoff, we will be hosting bi-weekly labs in Milne 224 in two hour blocks. These labs initially
  will be structured around the content on the website but will aim to be mostly hands on. OSL students and staff will
  be on-site to help you work through the content. Content discussed at each lab will depend on the attendees interest.
  We will also be opening up our Milne server room for students to learn and interact with actual hardware.

  Some interesting topics we may end up discussing include (expanded on the lessons we already have on the website):

Discuss more advanced topics and also have hands-on with server and network equipment in our lab.

.. ifslides::

  Some interesting topics we may end up discussing include:

- Automated Linux installs
- Network switch configuration
- Out of Band (IPMI) configuration and usage
- Installing servers in racks and configuring them
- Setting up servers to run various services (email, web, DNS, etc)
- Open Source software contributions
- Software Development

.. ifnotslides::

  Our Milne server room includes three `OpenCompute`_ Racks donated from Facebook (includes a total of 90 compute
  nodes), managed network switches, and other various rack mounted server hardware.

.. _OpenCompute: https://www.opencompute.org/

The ‘Agreement’
~~~~~~~~~~~~~~~

**You get out what you put in.**
    DOBC is not meant to be easy. Stick with it, persistence is rewarded.

**Student Benefits:**
    A free education on industry topics, tools, and concepts

**Student Responsibilities:**
    Show up if you can, keep up if you cannot, put forth effort, and don’t
    forget to have fun.

**Give us feedback.**
    - There will be a survey you, should take it.
    - Honesty is the best policy.


Getting Involved
----------------

Where To Ask Questions
    - Slack
    - During Lecture and Hand-on Lessons
    - *More on the* :ref:`about` *page*...

How To Ask Questions
    - Always be respectful to those helping you.
    - Stay calm and articulate.
    - Explain you are trying to achieve and be thorough.

Next: :ref:`first_steps`
