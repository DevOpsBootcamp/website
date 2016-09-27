.. _contributing_to_open_source:


Lesson 20: Contributing to Open Source
======================================

========= =====================================================================
Homepage  http://devopsbootcamp.osuosl.org
Content   FILL THIS IN
Slides    FILL THIS IN
Video     FILL THIS IN
========= =====================================================================

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------


Open Source
-----------

.. ifnotslides::

    Open Source (sometimes referred to as **Free (/ Libre) Open Source
    Software** or FOSS) is the idea of releasing software, and more
    importantly the *source code* for software, to the public *for free* to
    encourage community collaboration.  This means that if you use Open Source
    software you can not only *report a bug* of *request a feature*, but you
    can also *create the bug-fix* or *implement the feature yourself*!  Pretty
    nifty right?

    Open Source allows individuals and organizations to:

- Learn lots of new things, and grow as developers.
- Give back to a community that has given you something.
- You have more to contribute than you may realize!
- Meet amazing people.
- Personal fulfillment.


Community Benefit
~~~~~~~~~~~~~~~~~

    *Share the Love (and the Code)*

.. ifnotslides::

    One major part of Open Source is that the contributions you make to a
    project (*upstream changes*) are also free for the world.  Instead of
    everybody hoarding the changes they've made, we all benefit from the
    changes *you've* made.

    Say IBM contributes 4% of the code in the last Linux Kernel update (yes,
    companies can do Open Soruce too!).  It might be tempting for them to keep
    those fixes to themselves, since they payed developers to make those
    contributions and they "own" the changes they made.  Put another way
    though, they *got* 96% of the last update for *free*.  Open Source
    development works when everybody plays a *small* part in building a large
    project which millions of people depend on; when everybody pays it forward
    everybody benefits.


Personal Benefit
~~~~~~~~~~~~~~~~

.. ifnotslides::

    Of course Open Source isn't just a selfless act, there is always a personal
    benefit.

    For new developers there is the *experience* benefit.  You don't *start* as
    a great programmer, but you can get experience by contributing to *real*
    projects that people use.  Not only do you get coding experience but you
    also get experience:
    
- 'Learning the Ropes' of a substantial code-base
- Working with others
- Getting code reviewed
- Documenting contributions
- Testing your changes

.. ifnotslides::

    When you contribute to Open Source projects you build a portfolio of
    contributions that prove you can not only code, but you can learn how to
    make an incremental contribution to a larger project, which is what most
    of your job will be in the real world!  Rarely do you build an entire
    product from the ground up all on your own.

    .. note::

        It can be stressful putting your code online.  Just like an actor only
        improves when they perform publicly and get feedback, a programmer
        drastically improves if they publish their code and allow more
        experienced developers to give them feedback.  Before you know it
        you'll be giving newbies like yourself feedback on projects too!


Free?
~~~~~

.. ifnotslides::

    One of the major selling-points of FOSS is that the software is usually
    *monetarily* free, but this isn't really what is meant by the 'Free' in
    'FOSS'.  In this case *'Free'* is closer to *free speech* than it is to
    *free pizza*.  *GNU* has a page outlining this more explicitly:

Free Software:
    *[Free Software] means that* **the users have the freedom to run, copy,
    distribute, study, change and improve the software**.

The Four Freedoms:
    0. The freedom to run the program as you wish, for any purpose.

    #. The freedom to study how the program works, and change it so it does
       your computing as you wish. Access to the source code is a
       precondition for this.

    #. The freedom to redistribute copies so you can help your neighbor.

    #. The freedom to distribute copies of your modified versions to others.
       By doing this you can give the whole community a chance to benefit
       from your changes. Access to the source code is a precondition for
       this.

`gnu.org/philosophy/free-sw`_

.. ifnotslides::

    Put another way, Open Source software isn't just free when the source code
    is available, it is free when the code is available for anyone to use,
    anybody can try to contribute improvements, anybody can distribute their
    own versions (under the same license), and anybody can study the program.
    
    Making the source code avaliable is *nice* but a project which is FOSS
    requires community effort as well as a technical one.  Encouraging
    contributions, documenting your code, mentorship, etc.  It isn't easy but
    in the end it can make for better software.

.. _gnu.org/philosophy/free-sw: https://www.gnu.org/philosophy/free-sw.en.html

Acessing a New Community
------------------------

.. ifslides::

    *Things to consider when looking for a project.*

.. ifnotslides::

    There are a few things to look for when considering contribution to Open
    Source.  Each project has it's own culture and community that you will
    become a part of if you contribute.  Make sure you want to be a part of
    that community keeping the following in mind.


Elitism vs Nice-ism
~~~~~~~~~~~~~~~~~~~

.. ifslides::

    *Is the project welcoming?*

.. ifnotslides::

    Look around the community and see what the general vibe is.  When outsiders
    like yourself get involved are they welcomed diplomatically or are they
    shutdown and shut-out?

    You can find this by checking out open and closed issues and pull requests
    for the project.  It's usually pretty easy to pick up who the leaders of a
    project are, and how they handle newcomers.

    You can also check out the documentation for a project.  If it assumes you
    already know a lot about the project, or it doesn't exist, consider making
    an issue / pull request yourself to improve that.  If you're met with a
    cold shoulder, feel free to move on.


Communication style
~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    While you're reading through Issues, Pull Requests, and Mailing Lists, see
    if their communication styles are compatible with how you like to talk with
    people.  You might not get lunch with these people, but you do want to be
    friendly with them and have them do the same.


Documentation and Guides
~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    If a project isn't documented well, or at all, they might not be looking
    for outside contributors yet.  You should of course bring this to their
    attention, but if they don't want your help right now (this happens a lot
    in new projects) don't be offended and try back later.

    That said, if they have *great* user and developer documentation you should
    take that as a good sign.  They are mature enough to accept outside
    contributions and are probably willing to mentor an excited new
    contributor.


Things to Look for
~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Below are some general guidelines to keep in mind when looking for a
    project.  Check out the project's Source Code page (like Github or Gitlab)
    to see if the project is 'dead' or 'active'.

- When are the top pull requests time-stamped? Anything older than 3-4 months
  might not be ideal.

- Open / recent issues (especially with help wanted labels) are good.

- Many contributors means they're used to people helping out.


How to Get Involved
-------------------

.. ifnotslides::
    
    There are a veriety of ways to get involved with an Open Source project,
    and not all of them are contributing code!

    [Setup] Documenation
        Try *using* their software.  They should have a setup guide, follow
        that and if it doesn't work keep trying until it does and make a Pull
        Request to fix their documentation.

        This is a great way to get your foot in the door and is always
        appreciated.  When developing a project people tend to forget the
        basics and as a newbie you can help make the project more accessible to
        *other newbies*.

    Testing
        Most software should be well tested, but it almost never is.  By
        contributing tests (along with a fix maybe) you help the project
        long-term and make it more stable.

    Asking Questions
        Even reporting an issue can be helpful.  You might not have the time or
        skillset to fix something yourself, but you can always ask a question
        like "This is behaving weird, is it supposed to do that?"

    Writing Code
        Of course you can always contribute code to a project.  Check out the
        Issues, Bugs, and Feature Requests for a project and you can try making
        a contribution.

        Be sure to make a comment saying that you want to help out with a Issue
        before jumping too far in.  Some projects might try to lend you some
        advice, pointers, or mentorship to help you get the job done.

.. ifslides::

    - [Setup] Documenation
    - Testing
    - Asking Questions
    - Writing Code


Finding a Project
-----------------

.. ifnotslides::

    Here are a few useful websites and habits you can use to find a project.

In order of perceived usefulness:

- `Openhatch`_

- `24 pull requests`_

- `BugsAhoy`_

- `Showcased github projects`_

- `Trending github projects`_

- Choose a company, search “<Company Name> Open Source”

- Easy bugs

- GSOC submitters who didn’t get enough interns

- Search by language

- Search by project type – find something that interests you (web dev?
  bioinformatics? video games?)

- Your immediate payment for contributions will be satisfaction, so pick
  something satisfying

.. _Openhatch: http://openhatch.org/search
.. _24 pull requests: http://24pullrequests.com/
.. _BugsAhoy: http://www.joshmatthews.net/bugsahoy/
.. _Showcased github projects: https://github.com/showcases
.. _Trending github projects: https://github.com/trending


I Can't Find a Project I Like!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*That's okay.*

.. ifnotslides::

    If you venture aimlessly (or even if you venture with purpose) it can be
    hard to find a project you feel strongly enough about to contribute to.
    It may sound corny but **the right project will find you**.

    Many times we contribute to a project out of *necessity*, not becuase we
    want to contribute but because we *need* something and the best way to get
    the job done is by contributing to an Open Source project.

    **Example:** You're writing a webapp using cool framework *Hip-Framework*.
    You're trying to get something done in your app, but the Hip-Framework
    doesn't allow it.  You dig around their codebase and realize **you can add
    that feature**.  You make an issue, the project owner likes the idea, you
    make a pull-request, and *BAM* you've contribute to Open Source.

Sometimes you find the project, sometimes the project finds you.


First Steps
-----------

.. image:: /static/babypenguin.gif
    :align: center
    :alt: Baby penguin stumbling.

0. Find a project

#. Read Contributing and Getting Started docs

#. Look at list of issues

#. Do a thing!

    - Write a test

    - Fix a typo

    - Deploy and update the installation docs


Know your Licenses
------------------

.. image:: /static/licensing.jpg
    :align: center
    :alt: Software Licensing

.. ifnotslides::

    You should never publish code without a license.  Code without a license
    makes it hard for others to use and contribute to your software.  Instead
    you should choose one of the many existing licenses that fits you needs
    best.

    A license is just a way for you to tell the world "This is what I say you
    can and cannot do with my software."  It's as simple as having a file in
    your project titled LICENSE with the contents of your license of choice.

    **Never write your own license**.  Lawers get paid a lot of money to write
    Open Soruce licenses, if you are not a lawer then don't write your own.

- **MIT:** A very lax license permitting any (free and non-free) use of the
  software.

- **Apache:** A little more precise, gives more rights to the developers.

- **AGPL/GPL/LGPL:** For when you love Open Source and want to spread the love.

- **Creative Commons:** For when you're not writing code.

- http://choosealicense.com/

TODO: Find a FOSS Project
-------------------------

.. TODO: Add activity


Further Reading
---------------

.. TODO: Add further reading
.. Suggestion:
   - Something about licenses
   - re-link the finding projects urls
