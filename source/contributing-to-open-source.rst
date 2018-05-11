.. _contributing_to_open_source:


Lesson 20: Contributing to Open Source
======================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/contributing-to-open-source.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/contributing-to-open-source.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - Open Source
    - Assessing a New Community
    - How to Get Involved
    - Finding a Project
    - First Steps
    - Know Your Licenses


Open Source
-----------

.. ifnotslides::

    Open Source is a philosophy that encourages community effort and
    collaboration on software by making the software's *source code* available
    to the public. This means that if you use Open Source software you can not
    only *report a bug* or *request a feature*, but you can also *fix that bug*
    or *implement that feature!*  Pretty nifty right?

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
    companies can do Open Source too!).  It might be tempting for them to keep
    those fixes to themselves, since they paid developers to make those
    contributions and they "own" the changes they made.  Put another way
    though, they *got* 96% of the last update for *free*.  Open Source
    development works when everybody plays a *small* part in building a large
    project which millions of people depend on. When everybody pays it forward
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

    One of the major selling-points of Open Source is that the software is
    usually *monetarily* free, but in this case *'free'* is closer in meaning to
    *free speech* or *freedom* than it is to *free pizza*.  *GNU* has a page
    outlining this more explicitly:

Free Software:
    *[Free Software] means that* **the users have the freedom to run, copy,
    distribute, study, change and improve the software**.

.. nextslide::

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

.. ifnotslides::

    Put another way, Open Source software isn't just free when the source code
    is available, it is free when the code is available for anyone to use,
    anybody can try to contribute improvements, anybody can distribute their
    own versions (under the same license), and anybody can study the program.

    Making the source code available is *nice* but an Open Source project
    requires community effort.  Encouraging contributions, documenting code,
    mentoring new contributors, etc.  In the end, this open process not only
    leads to higher-quality software but also fosters great communities.

    `GNU's article about the Four Freedoms`_

.. _GNU's article about the Four Freedoms: https://www.gnu.org/philosophy/free-sw.en.html

Assessing a New Community
-------------------------

.. ifslides::

    *Things to consider when looking for a project.*

.. ifnotslides::

    There are a few things to look for when considering contributing to Open
    Source.  Each project has its own culture and community.  Make sure you
    want to be a part of that community keeping the following in mind:


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

    You can also check out the documentation for a project.  If it's not very
    detailed or if it doesn't exist, consider making an issue / pull request
    yourself to improve that.  If you're met with a cold shoulder, feel free to
    move on.


Communication style
~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    While you're browsing the project's communication channels (Github issues,
    mailing lists, etc.), check if their communication styles are compatible
    with how you like to talk with people.  You might not get lunch with these
    people, but you do want to be able to communicate with them effectively.


Documentation and Guides
~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    If a project isn't documented well (or at all), they might not be looking
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

    There are a variety of ways to get involved with an Open Source project,
    and not all of them are contributing code!

    [Setup] Documentation
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
        skill set to fix something yourself, but you can always ask a question
        like "This is behaving weird, is it supposed to do that?"

    Writing Code
        Of course you can always contribute code to a project.  Check out the
        Issues, Bugs, and Feature Requests for a project and you can try making
        a contribution.

        Be sure to make a comment saying that you want to help out with a Issue
        before jumping too far in.  Some projects might try to lend you some
        advice, pointers, or mentorship to help you get the job done.

.. ifslides::

    - [Setup] Documentation
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

.. ifnotslides::

    If all else fails, take to Google and just start searching for open source
    projects by category or by company. You might be surprised at the diversity
    of projects that you find and at the number of companies that contribute to
    or rely on open source!

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

    Many times we contribute to a project out of *necessity*, not because we
    want to contribute but because we *need* something and the best way to get
    the job done is by contributing to an Open Source project.

    **Example:** You're writing a webapp using cool framework *Hip-Framework*.
    You're trying to get something done in your app, but the Hip-Framework
    doesn't allow it.  You dig around their codebase and realize **you can add
    that feature**.  You make an issue, the project owner likes the idea, you
    make a pull-request, and *BAM* you've just contributed to Open Source.


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
    :scale: 40%

.. ifnotslides::

    You should never publish code without a license.  Code without a license
    makes it hard for others to use and contribute to your software because most
    countries will implicitly assign exclusive copyright without a license.
    Instead you should choose one of the many existing licenses that fits you
    needs best.

    A license is just a way for you to tell the world "This is what I say you
    can and cannot do with my software."  It's as simple as having a file in
    your project titled LICENSE with the contents of your license of choice
    (though some licenses such as Apache recommend that you add a license
    header to each file of source code).

    **Never write your own license**.  Lawyers get paid a lot of money to write
    Open Source licenses, if you are not a lawyer then don't write your own.

.. nextslide::

**Licenses to use:**

- **MIT**

.. ifnotslides::

    A very lax license permitting any (free and non-free) use of the software.
    Also sometimes called the **X11 License**.

    Examples of MIT-licensed software:
        - jQuery
        - .NET core

- **Apache 2.0**

.. ifnotslides::

    The Apache 2.0 license is often called a "corporate-friendly" license
    because of its built-in trademark protection and copyright provisions.

    Examples of Apache-licensed software:
        - Apache web server
        - Android

- **AGPL/GPL/LGPL 2/3**

.. ifnotslides::

    A family of licenses from the Free Software Foundation in
    descending order of copyleft strictness. In addition, version 3 of these
    licenses is stricter copyleft than version 2. There are the canonical Free
    Software licenses, but make sure that you've read them and understand their
    provisions before using them in your own projects.

    Examples of GPL-licensed software:
        - Linux (GPL 2.0)
        - GIMP (GPL 3.0)

**Licenses to *not* use:**

- **Public Domain Dedication**

.. ifnotslides::

    The public domain is a tricky concept because it doesn't exist in every
    country (though workarounds such as the CC0 license exist). This is
    usually not a recommended way to release your code because the nuances of
    the public domain might make it difficult for new contributors to get
    involved. However, there are some notable projects (such as SQLite) have
    been dedicated to the public domain.


TODO: Find an Open Source Project
---------------------------------

.. TODO: Add activity


Further Reading
---------------

`Choose A License`_

.. _Choose A License: https://choosealicense.com

.. TODO: Add further reading
.. Suggestion:
   - Something about licenses
   - re-link the finding projects urls
