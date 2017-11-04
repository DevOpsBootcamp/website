.. _shell_navigation:


Lesson 4: Shell Navigation
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
		- Text editors


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
		a shell runs in (GNOME terminal, tty1, etc).	A shell is run in a
		terminal, a terminal is the widow you use the shell in.


Shell Examples
~~~~~~~~~~~~~~

.. ifnotslides::

		As with all things in Open Source, there are many options to choose from
		when deciding on a shell.  Below is a short list of popular choices.	Each
		shell has it's positives and negatives. If you don't have an optionion you
		should probably use what comes by default when you open your terminal.

.. csv-table::
  :widths: 3, 10

  ``sh``, Required by all POSIX Operating Systems.
  ``bash``, Default on most GNU/Linux-based Operating Systems.
  ``csh``, Default shell on most BSD (Unix) based Operating Systems
  ``fish``, Useful but not ``sh`` compliant shell.
  ``zsh``, The *hip new shell on the block*.

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

				To see a list of variables and values run ``env``.	To set a variable
				run ``export YOUR_VARIABLE_NAME=<value>``.	To print a particular
				variable run ``echo $VARIABLE_NAME``.

		Pipe / ``|``
				Pipes take the text output from one command and pass them as the input
				to the next program.	Pipes can be chained, meaning the output of
				program ``foo`` can be passed to ``bar`` which can have it's output be
				passed to ``baz``.

				**Example:** run this exact command: ``$ ps aux | grep $USER | less``.

				**Hint** Build this chain incrementally. First run ``ps aux``, then
				add ``| grep $USER``, etc.

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
		navigate the OS.	Below are a few of the commands you will use to do this.

.. code-block:: bash

  # Prints the current working directory (where you are)
  $ pwd
  # Prints the contents of the current working directory
  $ ls
  # Navigates to a new directory.
  $ cd <path/to/other/directory>
  # Prints a string to the screen.
  $ echo "some thing $AND_VARS"
  # Prints the contents of a file(s) to the screen.
  $ cat foo.txt bax.txt
  # Searches `file.txt` for the string `foo`
  $ grep foo file.txt
  # Prints a file to the screen so you can arrow up/down.
  $ less file.txt
  # Prints environment variables to the screen.
  $ env
  # Prints out current user
  $ whoami
  # When in doubt, always type help.
  $ help

Shell Scripts
-------------

.. ifnotslides::

		Shell scripts are files which contain command run on your behalf by the
		shell.

		Each shell is also a programming langauge, so you can write logic, loops,
		functions, and declare local variables in your scripts.

``about_me.sh``

.. code-block:: sh

  #!/bin/sh
  if [ $(whoami) == "root" ]; then
    echo "You're root!"
  else
    echo "Your username is $(whoami)"
    echo "Your home-directory is $HOME"
    echo "Your current directory is $PWD"
    echo "Your computer's host-name is $HOSTNAME"
  fi

.. nextslide::

Invoke with:

.. code-block:: console

  # Tell Linux that this can be run as a program
  $ chmod +x about_me.sh
  # Invoke the script.
  $ ./about_me.sh
  Your username is dobc
  Your home-directory is /home/dobc
  Your current directory is /home/dobc
  Your computer's host-name is dobc

Useful Symbols
--------------

.. code-block:: sh

  $ grep 'searchstring' files/* | less

  $ true || echo 'never gets here'
  $ false && echo 'never gets here'

  $ echo 'this now an error message' 1>&2 | grep -v error
  this is now an error message

  !$ # last argument to last command
  $ cat /dir
  cat: /dir/: Is a directory
  $ cd !$
  cd /dir
  $ pwd
  /dir

More Useful Symbols
-------------------

.. code-block:: sh

  $ for x in 1 2 3; do echo $x; done # Use seq for longer sequences
  1
  2
  3

  $ var='this is a var'; echo ${var//this is } # Deletes 'this is '
  a var

  $ ls -l `which bash`
  -rwxr-xr-x 1 root root 1029624 Nov 12 15:08 /bin/bash

Combining These Together
------------------------

.. code-block:: sh

  $ set -a blocks
  $ blocks="10.0.0.0/24"
  $ set -a ips
  $ ips=`fping -g 10.0.0.0/24 2>&1 | grep unreachable | tr \\  \\n`
  $ for ip in $ips; do
  $   nmap -p 22 $ip && ips=`echo ${ips//$ip} \
      | tr -s \\n`
  $ done
  $ echo $ips

Function Definitions
--------------------

.. code-block:: sh

  name () {
  # code goes here
  }

Internal Variables
------------------

You should know the following:

.. csv-table::
   :header: Variable,Meaning

   ``$*``,All arguments passed
   ``$?``,Return code of last command run
   ``"$@"``,All arguments passed as a list
   ``$CDPATH``,Colon-delimited list of places to look for dirs
   ``$HOME``, Location of user homedir
   ``$IFS``,Internal Field Seperator
   ``$OLDPWD``,Previous PWD

Internal Variables
------------------

.. csv-table::
   :header: Variable,Meaning

   ``$PATH``,Colon-delimited list of places to find executables
   ``$PWD``,Present Working Directory
   ``$SHELL``,Path to running shell
   ``$UID``, User ID
   ``$USER``,Username

You should also read the EXPANSION section of the bash man page.

File Paths
----------

.. ifnotslides::

		File Paths describe the location of a file in the directory tree.

		Files are an important part of using an OS through the shell.  Being able
		to find, navigate to, and use files is important.  The first part of doing
		that is understanding some basics about directories.

.. csv-table::
  :widths: 3, 10

  ``.``, The current directory
  ``..``,The parent directory
  ``~``,Alias for your home directory
  ``/``,"Separates directories: ``one_dir/another_dir/last_dir`` Alone, or at the start of a path, it is the root
  directory."

.. nextslide::

.. code-block:: console

  $ tree -F
  .
  ├── bar/
  │   ├── one/
  │   └── two
  ├── baz/
  └── foo/
      └── a/
          └── b
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

  **Example:** ``cat *.log`` cats all files in the current working directory ending in ``.log``.

End of line (``$``)
  Used to specify the end of a regex. We'll cover what regex is later.

Curl braces (``{ }``)
  Used to specify a set.

  **Example:** ``ls {foo,bar,baz}ley-thing`` expands to ``ls fooley-thing barley-thing bazley-thing``

Escape special characters (treat them as normal characters) with the escape character (``\``).


Type Less, Tab More
-------------------

Pressing the ``tab`` key auto-completes a command, file-path, or argument in your shell.

Pressing ``tab`` multiple times completes the command to the best of the shells ability and then lists the possible
completions (if there are any).

.. code-block:: console

  $ ls b    # <tab>
  $ ls ba   # <tab>
  bar_thing/ baz_thing/
  $ ls bar  # <tab>
  $ ls bar_thing

Text Editor: Nano
-----------------

.. ifnotslides::

    We are going to with a quick tangent by learning to use the terminal-based text editor **Nano**.

.. image:: /static/nano.png
    :align: center
    :alt: nano in action

- User types like normal.
- Arrow keys used to to navigate the cursor.
- ``^ + <key>`` Commands (``control + key``)

.. nextslide::

Nano is a great terminal text editor to start with.  Later in your career you may start using ``emacs`` or ``vi/vim``
but to start with ``nano`` is familiar, easy to use, and gets the job done.

To use ``nano`` simply execute it like any other command in the terminal.

.. code-block:: console

    $ nano              # Open with empty file
    $ nano <file_name>  # Edit a specific file

This editor is almost exactly like any word processor or plain-text editor except that you don't have a mouse -- only
keyboard shortcuts. The instruction bar at the bottom of the screen is explains all of the key-bindings from saving, to
exiting, to cut and pasting.

Bash Hello World
~~~~~~~~~~~~~~~~

Using ``nano`` create a file called ``hello_world.sh`` and put the following in it:

.. code-block:: bash

  #!/bin/bash
  # declare STRING variable
  STRING="Hello World"
  # print variable on a screen
  echo $STRING

Now make the script executable using ``chmod`` and run the script. What does it do?

.. rst-class:: build

.. code-block:: console

  $ chmod +x hello_world.sh
  $ ./hello_world.sh
  Hello World

Passing arguments to the bash script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When you pass arguments to a bash script, you can reference them inside of the script using ``$1``, ``$2``, etc. This
means if you do something like '``foo.sh bar``', ``$1`` will return ``bar``. You can also use ``$@`` to reference all
arguments.

For example:

.. code-block:: bash

  #!/bin/bash
  echo $1   # prints argument #1 given to script
  echo $@   # prints all arguments given to script

Reading User Input
~~~~~~~~~~~~~~~~~~

You can also take input using the ``read`` command which then stores it in a variable. If you pass ``read`` '``-a``',
it puts the input into a bash array.

For example:

.. code-block:: bash

  #!/bin/bash
  echo -e "Tell me a word: \c"
  read word
  echo "Your word is $word"

.. rst-class:: build

.. code-block:: console

  $ ./read.sh
  Tell me a word: foo
  Your word is foo

Simple Bash if/else statement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Bash conditionals use ``if``, ``else``, ``then`` and ``fi`` operators. You can compare strings, files and even command
output. An example:

.. code-block:: bash

  #!/bin/bash
  if [ "$1" == "foo" ] ; then
    echo "You said $1"
  else
    echo "You did not say foo"
  fi

.. rst-class:: build

.. code-block:: console

  $ ./sayfoo.sh foo
  You said foo
  $ ./sayfoo.sh bar
  You did not say foo

Exercises: Bash
---------------

- Using the ``tar`` command, write a script named ``backup.sh`` which backs up the ``dobc`` user home directory into a
  file ``/tmp/dobc-backup.tar.gz`` . *Hint: use the man page for tar or type 'tar -h'.*
- Create a script called ``args.sh`` that takes three arguments and prints all of the args and then prints them in
  reverse using ``echo``.
- Create a script named ``input.sh`` which takes input for three args and then prints them in a sentence (of your
  choosing).
- Create a script named ``ifelse.sh`` which takes two arguments. If both arguments match, print ``"Yay, they match!"``,
  if they don't, then print ``"Boo, they don't match :("``.

.. ifslides::

	*We likely won't have enough time to cover these all, but feel free to try later!*

Exercise Answer Key
-------------------

Simple Backup script
~~~~~~~~~~~~~~~~~~~~

.. rst-class:: build

.. code-block:: bash

  #!/bin/bash
  # The flags for tar do the following:
  # v - verbose
  # c - compress
  # z - use gzip
  # f - output to file
  tar -vczf /tmp/dobc-backup.tar.gz /home/dobc


.. rst-class:: build

.. code-block:: console

  $ ./backup.sh
  tar: Removing leading `/' from member names
  /home/dobc/
  /home/dobc/backup.sh
  /home/dobc/hello_world.sh
  /home/dobc/.bash_profile
  /home/dobc/.bashrc
  /home/dobc/.bash_logout

.. rst-class:: build

**Bonus: How could you list the contents of the file?**

Passing arguments to the bash script
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: build

.. code-block:: bash

  #!/bin/bash
  echo $@
  echo $3 $2 $1

.. rst-class:: build

.. code-block:: console

  $ chmod +x args.sh
  $ ./args.sh DOBC is awesome
  DOBC is awesome
  awesome is DOBC

.. rst-class:: build

**Bonus #1: What happens if you give the script nothing?**
**Bonus #2: What happens if you give it the string "DOBC is awesome" with quotes?**

Reading User Input
~~~~~~~~~~~~~~~~~~

.. rst-class:: build

.. code-block:: bash

  #!/bin/bash
  echo -e "Tell me a noun: \c"
  read noun
  echo -e "Tell me a verb: \c"
  read verb
  echo -e "Tell me an adjective: \c"
  read adj
  echo "I plan to $verb a $adj $noun"

.. rst-class:: build

.. code-block:: console

  $ ./input.sh
  Tell me a noun: apple
  Tell me a verb: eat
  Tell me an adjective: large
  I plan to eat a large apple

Simple Bash if/else statement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. rst-class:: build

.. code-block:: bash

  #!/bin/bash
  if [ "$1" == "$2" ] ; then
    echo "Yay, they match!"
  else
    echo "Boo, they don't match :("
  fi

.. rst-class:: build

.. code-block:: console

  $ ./ifelse.sh foo foo
  Yay, they match!
  $ ./ifelse.sh foo bar
  Boo, they don't match :(

Further Reading
---------------

`BASH Programming - Introduction HOW-TO`_
	A free online resource of learning bash programming.	Covers some concepts
	we'll get to later in DOBC, but a good resource to have on hand.

`Advanced Bash-Scripting Guide`_
	An in-depth exploration of the art of shell scripting. Covers more advanced concepts with Bash.

`Running rm -rf / on Linux`_
	This video demonstrates what happens when you 'delete your hard-drive' on Linux. A fun watch!

Next: :ref:`users_groups_permissions`

.. _BASH Programming - Introduction HOW-TO: http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO.html
.. _Advanced Bash-Scripting Guide: http://tldp.org/LDP/abs/html/
.. _Running rm -rf / on Linux: https://youtu.be/D4fzInlyYQo

