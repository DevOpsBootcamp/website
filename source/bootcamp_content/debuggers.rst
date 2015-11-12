Development Tools and Debuggers
===============================

.. code-block:: none

    (How to( find( the missing parenthesis)).


Topics
------

* Code Analysis (conceptual)
* Debuggers
    * CLI tools
    * Web Consoles
* Linters
    * Style Guides
* Testing
    * Code Coverage
* Virtual Environments
* Integrated Development Environments


Code Analysis
-------------

======================================  ======================================
Static                                  Dynamic
======================================  ======================================
- Linters                               - Debuggers
- Type checkers                         - Memory profiling tools
|                                       - Coverage testers
======================================  ======================================

Deugging
--------

.. figure:: /static/youtube-error.jpg
    :align: right

"...a computer program that is used to test and debug other programs..."

Debuggers do what you do already:

* Print (broken) variables.
* Read and reports error messages.
* Highlight (incorrect) syntax.

Just very fast very well.

CLI Tools
---------

=========== =============== ================
C / C++     Python          NodeJS
=========== =============== ================
* Valgrind  * PDB           * ``node debug``
* GDB       * Stack Traces  * Node Inspector
=========== =============== ================

Python Stack Trace:

.. code-block:: none

    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 2, in f
    TypeError: unsupported operand type(s) for * : 'int' and 'NoneType'

(The last line is the *really* important one)

Example: Valgrind
-----------------

* A dynamic analysis tool which runs your code and checks for memory leaks and
  other errors.

* Verbose, but tells you what line the problem happened on, and how your
  program got to that line.

.. code-block:: bash

    $ valgrind ./tests/bin/lexer_tests
    ...
    ==6703== Conditional jump or move depends on uninitialised value(s)
    ...
    ==6703==    by 0x4018C1: print_token (lexer.c:36)
    ==6703==    by 0x4011F7: test_get_tok (lexer_tests.c:54)
    ==6703==    by 0x4008CD: main (lexer_tests.c:8)
    ...
    ==6703== LEAK SUMMARY:
    ==6703==    definitely lost: 192 bytes in 8 blocks
    ==6703==    indirectly lost: 162 bytes in 10 blocks


Web Console
-----------

* ``Ctrl+Shift+K`` (``Command+option+k``) in Firefox
* ``Ctrl+Shift+I`` (``Cmd+opt+I``) in Chrome

Web console is great for debugging HTML, CSS and Javascript.
'Console' tab is particularly useful.


Linters
-------

    "...any tool that flags suspicious usage in software written in any
    computer language... generally perform static analysis of source code."

Checks your code *before* you run it to see what problems will probably arise.

Examples: flake8 (python), slint (C)

.. code-block:: none

    src/times.js: line 407, col 20, Expected '{' and instead saw 'return'.
    src/times.js: line 415, col 49, Missing semicolon.
    src/times.js: line 407, col 58, 'error' is not defined.

**MID SLIDE POP QUIZ**
    *What tool would you use to find the missing parenthesis?*

They also enforce **Style Guides**.

Style Guides
------------

    "...a set of standards for the writing and design of documents..."

.. figure:: /static/xkcd/code_quality.png
    :align: center
    :width: 90%
    :target: https://xkcd.com/1513/


Coding Standards
----------------

Guiding Principle: Code is read much more often than it is written.

Here is an example from the python PEP8 guidelines:

    Absolute imports are recommended, as they are usually more readable and
    tend to be better behaved.

.. code-block:: bash

    # Do this:
    from mypkg import sibling
    # Not this:
    import mypkg.sibling


Example: Linux Kernel Standards
-------------------------------

The Linux kernel style guidelines are actually fun to read:

    First off, I'd suggest printing out a copy of the GNU coding standards, and
    NOT read it. Burn them, it's a great symbolic gesture.

https://www.kernel.org/doc/Documentation/CodingStyle

.. nextslide::

NASA's Jet Propulstion Labratory style guidelines are very short
and are concerned with automated tooling to do code analysis:

    All loops shall have a statically determinable upper-bound on the maximum
    number of loop iterations.

http://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf


Testing
-------

    "...an investigation conducted to provide stakeholders with information about
    the quality of the product or service under test."

Test runners tend to give you information about why a test failed, similar to
what a debugger would tell you.


Code Coverage
-------------

    "...a measure used to describe the degree to which the source code of a
    program is tested by a particular test suite."

Coverage tools tell you how thorough your tests are, or at least what code gets
run by your tests.

.. code-block:: none

    [... run's tests ...]
    =============================== Coverage summary =========================
    Statements   : 82.23% ( 833/1013 )
    Branches     : 84.94% ( 327/385 )
    Functions    : 73.87% ( 164/222 )
    Lines        : 82.18% ( 830/1010 )
    ==========================================================================
    [... any errors from the tests ...]

Examples: ``go cover``, ``node-coverage``, ``Coverage.py``


Virtual Environments
--------------------

    "...any software, program or system that implements, manages and controls
    multiple virtual environment instances."

* Mostly Python specific.
* "Wrap up all of my dependencies and libraries and put them in a box here"
* Prevents conflicting versions across projects. e.g. PGD uses Django 1.5, but
  Working Waterfronts uses Django 1.7

Create a virtualenv

.. code-block:: bash

    $ virtualenv my-python-libraries

Using a Virtual Environment
---------------------------

Activate the virtualenv so you use the right libraries

.. code-block:: bash

    $ source my-python-libraries/bin/activate

A special message has been added to our prompt to let us know which
virtualenv we are using

.. code-block:: bash

    (my-python-libraries)$

Install a library

.. code-block:: bash

    (my-python-libraries)$ pip install Flask

Deactivate when you're done

.. code-block:: bash

    (my-python-libraries)$ deactivate


How Others deal with Dependencies
---------------------------------

Many other languages attack the depencies issue in smarter and less smart ways.

Node.js:
    Creates a ``node_modules`` directory and tracks dependencies in
    ``package.json``
Go:
    Dependencies are tracked via git repositories and using the ``go get``
    command.

It is a very hard problem to solve.

Integrated Development Environments
-----------------------------------

    "...a software application that provides comprehensive facilities to
    computer programmers for software development."

.. figure:: /static/minecraft_debug.gif
    :align: center
    :width: 80%
    :target: https://www.reddit.com/r/Minecraft/comments/3pnwgn/the_new_debug_screen/?ref=share&ref_source=link


Development Servers
-------------------

A test server for development purposes only. Includes:

* Test data.
* A minimal, easy to deploy, enviroment.
* Debugging tools are also installed (but not on production usually)
    * Test runners.
    * Code analysis tools.
    * Debuggers.

Activity
--------

Go to `the Bootcamp Exercises`_ repo to get some practice debugging
our tinsy flask app.

.. _the Bootcamp Exercises: https://github.com/DevOpsBootcamp/Bootcamp-Exercises/tree/master/2015-2016
