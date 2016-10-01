.. _questions_answers_documentation:


Lesson 7: Questions, Answers, Docs
==================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/questions-answers-documentation.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/questions-answers-documentation.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

  Overview
  --------

  - Where to get help

    - ``man`` (manual) Pages.
    - Project documentation.
    - Forums
    - IRC

When in doubt
-------------

.. ifnotslides::

    When you're on the commandline you're not expected to remember every
    command, and especially not every flag.  Since we don't all have minds
    like a steel-trap, programs are well documented, and getting help is
    as easy as typing ``--help``.

::

    $ <program> --help
    $ <program> -h

Most programs allow you to pass a ``help`` flag which will print out basic
usage. This is useful as a quick reference for how to use the program.


Man Pages
---------

.. ifnotslides::

    Man pages are much longer documents which explain what the program is,
    how to use it, who the authors are, and what each flag/sub-command does in
    greater detail.

::

    $ man <program>

- Type ``/`` and then enter a keyword to see where that word appears.
- Press ``n`` to go to the next (and ``p`` to go to the previous) occurrence
  of that word.

.. nextslide::

::

    $ man man

    MAN(1)                        Manual pager utils                       MAN(1)

    NAME
           man - an interface to the on-line reference manuals

    SYNOPSIS
           man  [-C  file]  [-d]  [-D]  [--warnings[=warnings]] [-R encoding] [-L
           locale] [-m system[,...]] [-M path] [-S list] [-e  extension]  [-i|-I]
           [...]

    DESCRIPTION
           man is the system's manual pager.  Each page argument given to man  is
           normally  the name of a program, utility or function.  The manual page
           [...]

.. ifnotslides::

    Manual pages are local documents installed on your Linux system as part of
    the package installation process.  They are used as a complete reference
    for a program so if you want to know:

    - What a program does.
    - All of the flags for a program.
    - Who made the program.
    - Some examples of the program in action.
    - A conceptual overview of the program.

    Then a man page will probably help.  They're not perfect and are not
    standardized so don't expect a perfect document every time.


Anatomy of a Man Page
~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Since Man Pages are open source, just like the code they document, there
    is not a strict set of standards that need to be met for a manpage to
    exist beyond having some number of the following sections:

Most Man Pages include:
    - Name
    - Flags
    - Description
    - Basic Usage
    - Authors

If you're lucky they will also include:
    - A Good description
    - Advanced Usage.
    - Examples
    - History
    - See Also


Sections of Man
~~~~~~~~~~~~~~~

.. ifnotslides::

    ``man`` pages are also organized by *section*. To read man page for a
    program/library in a specific section type ``man  #  <program or
    library>`` where ``#`` is the section number.

    For instance

    ::

        $ man 2 open # Displays the kernel documentation for open (section 2)
        $ man open   # Displays the documentation for openvt (section 1)

    If there is a collision in man-page naming (like ``open`` and ``open()``)
    ``man`` will pick the page which appears in the lowest-value section.

1. Executable programs or shell commands
2. System calls (function provided by the kernel)
3. Library calls (functions provided from within libraries)
4. Special files (usually found in /dev)
5. Files formats and conventions eg /etc/passwd
6. Games
7. Miscellaneous (including macro packages and conventions), e.g., ``man(7)``,
   ``groff(7)``
8. System administration commands (usually only for root)
9. Kernel routines [Non standard]

.. note:: Some distros use ``info`` instead of ``man``. To learn more about the
          ``info`` command, see Further Reading.


Project Docs
------------

.. ifnotslides::

    Projects also document themselves *beyond* the manpage. These can include
    tutorials, a README, and Q&A.  If you need more information about a tool
    or a specific answer these docs will probably be your best bet.

    These docs may also answer any technical or contributing questions.  These
    docs can be updated more frequently than local ``man`` pages so should
    also be referred to for bleeding-edge information.

Where to look:
    - **http://docs.some-random-project.io/**
    - **http://some-random-project.io/docs/**
    - **http://organization.com/some-random-project/**


Questions and Answers
---------------------

.. ifnotslides::

    It's important to be able to ask questions and get answers.  Thankfully
    this is is something everybdy needs to do so it's almost an entirely
    solved problem.

    Below are some forms of Q&A which are easy to partipate in and usually
    archived, so you can look at what other people asked and get their answers
    (odds are, your question has already asked *somewhere* on the internet
    before you).

- Stack Overflow
- Forums
- Mailing Lists
- Blogs

.. image:: /static/xkcd-979.png
    :align: center
    :alt: XKCD 979, Wisdom of the Ancients
    :target: https://xkcd.com/979/


How to Talk to People
---------------------

.. ifnotslides::

    It's also important to talk to people directly sometimes.  Either you're
    under a time crunch, not sure what direction to go in, or just need a
    second opinion.  If you're online or able to talk in person here are a few
    of the ways to get in touch with like-minded people.

- Chatrooms
- Meetups
- Face to Face (!?)


IRC
---

.. ifnotslides::

    IRC is a very old protocol for communicating online with other people.  On
    IRC it is easy to create a new channel (chat-room) and talk with people in
    public or privately.

    It has become the long-standing defacto mode of online communication right
    next to mailing lists in the technology community.

Quick Facts:
    - Internet Relay Chat (IRC)
    - Very old (RFC 1459, May 1993)
    - Works on everything (Terminal, GUI, Web-browser, etc)
    - The people you want to listen to are there
    - Oregon State ran one of the first servers ever!

TODO Getting on IRC
~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    It's useful to get on IRC so you can communicate with DevOpsBootcamp as
    well as other online communities.  Most large (and many small) Open Source
    projects have a presence on ``irc.freenode.net`` which you can leverage to
    ask questions directly to the developers and active community members.

*To get on IRC, Use irssi or weechat in screen:*

::

    # This step is optional, but persistent IRC is cool
    $ ssh <username>@<a remote linux server>

    # start screen with the name 'irc'
    $ screen -S irc

    # start your client in the 0th window of the screen session
    $ irssi
    # or
    $ weechat-curses

    # exit irc screen with CTRL+a, CTRL+d
    # exit ssh session with CTRL+d or 'exit'
    # to get back to irc:
    $ ssh <username>@<preferred shell host>
    $ screen -dr IRC


Connecting and Setup
~~~~~~~~~~~~~~~~~~~~

In the IRC client run these commands

::

    /connect irc.freenode.net

    /nick <myawesomenickname>
    /msg nickserv register <password> <email>

    /nick <myawesomenickname>
    /msg nickserv identify <password>

    /join #devopsbootcamp

Commands and Tips
~~~~~~~~~~~~~~~~~

- ``/list``: Reports all the channels on a server.
- ``/topic``: Reports current channel topic.
- ``/names``: Reports nicks of users in channel.
- ``/join <channel>``: Join a new channel.
- ``/whois <nick>``: Learn about a person.
- ``/msg``: Directly message an individual.
- ``/help <command>``

.. nextslide::

- Tab-completion works with nicks
- You get a **hi-light** when your name is said.
- Symbols (``@``, ``+``) are not part of names, show status in channel.
- ``chanserv`` and ``nickserv`` are robots.

    - ``/msg nickserv help`` to get nick help.
    - ``/msg chanserv help`` to get channel help.


IRC Jargon
~~~~~~~~~~

.. image:: /static/jargon.jpg
    :alt: Jargon definition
    :align: center

.. nextslide::

- **ping/pong**: "I would like to tell you something"/"I'm here, tell it to me."
- **tail**: "~"
- **hat**: "@" Denotes admin status in a channel.
- **nick**: Your name.
- **netsplit**: When the IRC servers lose connection with eachother.
- **kick/ban/k-line**: GTFO


Asking for Help
~~~~~~~~~~~~~~~

.. ifnotslides::

    Asking for help can be a stressful task.  Sometimes you are talking to
    complete strangers, sometime you are talking to an idol, other times you
    are just so confused you're not even sure what you're asking for.

It's okay to ask for help.  Here are some things to keep in mind:

#. As yourself what should be happening?
#. As yourself what is actually happening?
#. Google the problem(s).
#. Skim the manuals of each component.
#. Identify a friend, mentor, or IRC channel who could help.
#. When they're not busy, give them a quick synopsis of points 1 and 2,
   mentioning what possibilities you've ruled out by doing steps 3 and 4.

Contributions = expertise + time


Further Reading
---------------

.. TOOD: Add furthe reading
.. suggestions:
.. - getting on irc docs
.. - stack overflow sites
.. - bolgpost on this kind of topic

* `About ``Info```_

.. _About ``Info``: http://www.computerhope.com/unix/info.htm
