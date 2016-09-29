.. _shell_navigation:


Lesson 3: Shell Navigation
==========================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/shell-navigation-os.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/shell-navigation-os.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What a shell is.
    - Types of shells.
    - How to navigate an OS via a shell.
    - Shell Scripts
    - Tips, Tricks, and Tabs.


The Shell
---------

    *A shell is a text-based user-interface for a computer.*

.. image:: /static/seashells.jpg
    :align: center
    :alt: sea shell
    :target: https://en.wikipedia.org/wiki/File:Cypraea-moneta-001.jpg

.. ifnotslides::

    Shells are the programs which allows you use a computer via text-based
    commands.  Not to be confused with a *terminal*, which is the environment
    a shell runs in (GNOME terminal, tty1, etc).  A shell is run in a
    terminal, a terminal is the widow you use the shell in.


Shell Examples
~~~~~~~~~~~~~~

.. ifnotslides::

    As with all things in Open Source, there are many options to choose from
    when deciding on a shell.  Below is a short list of popular choices.  Each
    shell has it's positives and negatives. If you don't have an optionion you
    should probably use what comes by default when you open your terminal.

``sh``
    Required by all POSIX Operating Systems.

``bash``
    Default on most GNU/Linux-based Operating Systems.

``csh``
    Default shell on most BSD (Unix) based Operating Systems

``fish``
    Useful but not ``sh`` compliant shell.

``zsh``
    The *hip new shell on the block*.


Navigation Concepts
-------------------

.. ifslides::

    - **Invoking a Program:** Type the command, press enter.
    - **Flags** (``-v``, ``--version``): Specify desired program behavior.
    - **Environment Variables**: Variables in your shell.
    - **Pipe** (``|``): Makes the input to one command the output of another.
    - **Directory**: A folder.
    - **Directory Root**, **Directory Tree**: The abstract directory
      structure.
    - **The** ``$HOME`` **Directory** (``~``): Where you *'live'*.

.. ifnotslides::

    Invoking a Program
      Invoking a program is simple: **type the name of the program into
      the terminal and press** ``Enter``.

      For instance, to start ``top`` enter ``top`` in your shell and press
      the ``Enter`` key.

    Flags / ``-v`` / ``--version``
      Flags (sometimes called Switches) **specify options for running a
      program**.

      **Example:** you want to find the version of a program. To do this you
      would run ``<command> --version``.

      Each program defines it's own command-line flags. The rule of thumb is
      to run ``<command> -h`` or ``<command> --help`` to get the list of
      possible flags and sub-commands.

    Environment Variables
        Just like a program or script can have variables, **your shell can
        have variables** which can be read from, written to, and modified.

        To see a list of variables and values run ``env``.  To set a variable
        run ``export YOUR_VARIABLE_NAME=<value>``.  To print a particular
        variable run ``echo $VARIABLE_NAME``.

    Pipe / ``|``
        Pipes take the text output from one command and pass them as the input
        to the next program.  Pipes can be chained, meaning the output of
        program ``foo`` can be passed to ``bar`` which can have it's output be
        passed to ``baz``.

        **Example:** run this exact command: ``$ ps aux | grep $USER | less``.

        **Hint** Build this chain incrementally. First run ``ps aux``, then
        add `` | grep $USER``, etc.

    Directory
        A **directory is like a folder**.  You will find yourself "in a
        directory" a lot while navigating an OS via the shell. This is just
        like you having a folder open on your desktop.

    Directory Root / Directory Tree
        The **Root** of your directory structure is the base directory which
        contains all other directories.  Since all other folders are contained
        within it, one can think of this as the 'root' of a directory 'tree'.

        **Hint:** Run `tree /` in your shell.

    The ``$HOME`` Directory (``~``)
        Your ``$HOME`` is the **root of your user's directory tree** on the OS.
        This is analogous to your desktop folder.


Basic Shell Commands
--------------------

.. ifnotslides::

    The most basic job of a shell is to enable the user to execute programs and
    navigate the OS.  Below are a few of the commands you will use to do this.

::

    $ pwd    # Prints the current working directory (where you are)
    $ ls     # Prints the contents of the current working directory
    $ cd <path/to/other/directory>   # Navigates to a new directory.
    $ echo "some thing $AND_VARS"    # Prints a string to the screen.
    $ cat  foo.txt bax.txt # Prints the contents of a file(s) to the screen.
    $ grep foo file.txt    # Searches `file.txt` for the string `foo`
    $ less  file.txt       # Prints a file to the screen so you can arrow up/down.
    $ env    # Prints environment variables to the screen.
    $ whoami # Prints out current user
    $ help   # When in doubt, always type help.

Shell Scripts
-------------

.. ifnotslides::

    Shell scripts are files which contain command run on your behalf by the
    shell.

    Each shell is also a programming langauge, so you can write logic, loops,
    functions, and declare local variables in your scripts.

``about_me.sh``

.. code:: sh

    #!/bin/sh
    if [ $(whoami) == "root" ]; then
      echo "Your root!"
    else
      echo "Your username is $(whoami)"
      echo "Your home-directory is $HOME"
      echo "Your current directory is $PWD"
      echo "Your computer's host-name is $HOSTNAME"
    fi

Invoke with:

::

    $ chmod +x about_me.sh  # Tell Linux that this can be run as a program.
    $ ./about_me.sh         # Invoke the script.

File Paths
----------

.. ifnotslides::

    File Paths describe the location of a file in the directory tree.

    Files are an important part of using an OS through the shell.  Being able
    to find, navigate to, and use files is important.  The first part of doing
    that is understanding some basics about directories.

``.``
    The current directory.

``..``
    The parent directory.

``~``
    Alias for your home directory.

``/``
    Separates directories: ``one_dir/another_dir/last_dir``

    Alone, or at the start of a path, it is the root directory.

.. nextslide::

::

    $ tree -F
    .
    |-- bar/
    |   |-- one
    |   `-- two
    |-- baz/
    `-- foo/
        `-- a/
            `-- b/

    5 directories, 2 files

Special Characters
------------------

.. ifnotslides::

    When using a shell (and in general) there are special characters.  These
    serve a functional purpose (carry special meaning) in addition to being a
    character, so you can't use them willy-nilly.  You should know what those
    are and what they mean.

Wildcard (``*``)
    Used as a stand-in for any character(s).

    **Example:** ``cat *.log`` cats all files in the current working directory
    ending in ``.log``.

End of line (``$``)
    Used to specify the end of a regex. We'll cover what regex is later.

Curl braces (``{ }``)
    Used to specify a set.

    **Example:** ``ls {foo,bar,baz}ley-thing`` expands to ``ls fooley-thing
    barley-thing bazley-thing``

Escape special characters (treat them as normal characters) with the escape
character (``\``).


Type Less, Tab More
-------------------

Pressing the ``tab`` key auto-completes a command, file-path, or argument in
your shell.

Pressing ``tab`` multiple times completes the command to the best of the
shells ability and then lists the possible completions (if there are any).

::

    $ ls b    # <tab>
    $ ls ba   # <tab>
    bar_thing/ baz_thing/
    $ ls bar  # <tab>
    $ ls bar_thing


TODO
----

.. TODO: Add activity
.. TODO: Add Answer Key
.. They've already changed their passwords, what else would be a good
.. challenge?


Further Reading
---------------

`BASH Programming - Introduction HOW-TO`_
    A free online resoruce of learning bash programming.  Covers some concepts
    we'll get to later in DOBC, but a good resoruce to have on hand.

.. _BASH Programming - Introduction HOW-TO:
      http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html
