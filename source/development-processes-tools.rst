.. _development_processes_tool:


Lesson 15: Dev Processes & Tools
================================

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

    - Code Analysis

        - Code Linting
        - Web Consoles

    - Code Coverage
    - IDE
    - Style Guides
    - Dependency Isolation



Code Analsis
------------

::

    (How to( find( the missing parenthesis)).

.. ifnotslides::

    Code Analysis is one of the main tools in a programmer's arsenel to
    produce code that is bug-free.  It is the act of using a computer to look
    at your code to check it for correctness.  This can range from making sure
    it adheres to style guides to making sure your functions actually return
    what you expect them to.

    Code Analysis tools come in two flavors:

Static
    These tools look at your code *files* and never actually run the program.

    Includes Linting and Type Checking.  

Dynamic
    Dynamic Code Analysis tools actually run your code and make verifications
    by watching how your program acts, where it fails, what it does in memory,
    and if your tests are adequate enough.

    Includes Debuggers, Memory Profiling Tools, and Code Coverage.


Debugging Tools
---------------

.. ifnotslides::

    Debugging tools are programs that run your code and report important
    information either automatically or that you explicitly request:

- Print (broken) variables.
- Read and reports error messages.
- Highlight (incorrect) syntax.

.. ifnotslides::

    Most of what a debugger does is what you do already.  You print variables
    and correct wrong syntax, a debugger makes it easy and fast so you can
    iterate and fix your problems more quickly.


CLI Tools
~~~~~~~~~

.. ifnotslides::

    Command-line tools are utilities you can use to debug your code from the
    terminal.

C/C++
    - ``GDB``: Used to inspect and debug everything in a C program from
      variables to why it encountered a fatal failure. Generally called the
      swiss-army-knife of debugging, a great tool to use in programming,
      allows you to set *'break points'* where the program stops mid-run and
      you can see what it's doing.

    - ``Valgrind``: Used specifically to inspect and debug memory issues.

.. ifnotslides::

    For example, here is some ``valigrind`` output.

::

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

.. ifnotslides::

    It is verbose, but it runs your code and gives you a necessarily thorough
    summary so you know exactly where your program is taking up a lot of memory
    (leaking) and how to possibly fix it.

Python
    - ``PDB``: The GDB tool for python.

    - ``Stack Traces``: A feature built into Python. Explains what function
      calls triggered a fatal failure.  Not interactive but very useful for
      debugging in development.

.. ifnotslides::

    For example, here is a Python Stack Trace.

    **Hint** The last line is the most important.

::

    $ python some_script.py
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
        File "<stdin>", line 2, in f
    TypeError: unsupported operand type(s) for * : 'int' and 'NoneType'

NodeJS
    - ``node debug``: Built into NodeJS used to debug programs in the language.

    - ``Node Inspector``: External tool for debugging NodeJS programs.


Web Consoles
~~~~~~~~~~~~

.. ifnotslides::

    Web Consoles are useful tools built directly into your browswer for
    debugging and modifying website HTML, CSS, and Javascript *on the fly*.

    You can access the web console (which is the javascript-specific part)
    using the following commands:

.. image:: /static/web_console.png
    :align: center
    :alt: Firefox Console

- ``Ctrl+Shift+K`` (``Command+option+k``) in Firefox
- ``Ctrl+Shift+I`` (``Cmd+opt+I``) in Chrome


Linters
~~~~~~~

.. ifnotslides::

    Linters inspect your code and flags suspicious usage.  This can be to
    enforce a style guide or to flag code which will probably not compile or
    break the program when it is running.

Examples:
    - ``flake8`` (Python)
    - ``slint`` (C)
    - ``jshint`` (NodeJS)

::

    src/times.js: line 407, col 20, Expected '{' and instead saw 'return'.
    src/times.js: line 415, col 49, Missing semicolon.
    src/times.js: line 407, col 58, 'error' is not defined.



TODO: Lint the Code!
~~~~~~~~~~~~~~~~~~~~

.. TODO: Add activity


Code Coverage
-------------

.. ifnotslides::

    Code Coverage is the process of running your tests and keeping track of
    which lines, logic branches, and files are used in the test suite.  Code
    coverage programs keep tabs on the lines of code (or not run) in each of
    your tests and outputs a report showing a percentage of your codebase that
    is run during the test suite, as well as a more detailed list of which
    lines, methods, and logic-branches are tested in your suite.

    This is useful because it demonstrates how much your tests are actually
    doing (proving your program does what it should) and proves if you're
    carrying around a bunch of dead code.  In general a good target-coverage
    is 80% of your code should be tested in your test suite.  100% coverage is
    all but impossible.


Integrated Development Environments (IDE)
-----------------------------------------

.. image:: /static/minecraft_debug.gif
    :align: center
    :alt: Debugging in Minecraft
    :target: https://www.reddit.com/r/Minecraft/comments/3pnwgn/the_new_debug_screen/

.. ifnotslides::

    IDEs are programs used to help developers get their job done by integrating
    many essential tools into one ecosystem.

    Most IDEs act as a debugger, text editor, linter, syntax hi-lighter, and
    even a version control GUI.  These are useful features to combine into one;
    instead of learning many tools you only need to learn one, largely
    click-button-based tool.

    IDEs can also drastically simplify a complicated ecosystem by tracking
    dependencies and hiding boiler-plate code from the developer.  In Java it
    is almost unheard of to program without an IDE because setting up source
    code by hand is so tedious and error-prone.

.. nextslide::

Examples:
    - Netbeans: Java
    - Visual Studio: .NET
    - PyCharm: Python
    - Eclipse: Misc


Style Guides
------------

.. image:: /static/code_quality.png
    :alt: XKCD Code Quality comic
    :target: https://xkcd.com/1513/
    :align: center

.. ifnotslides::

    Code is read much more than it is written.  If we assume this is true then
    we can conclude that it'd be nice for our code to look good, or at least be
    consistent (a book is hard to read when it keeps changing tenses and
    time-line)

    Style Guides are rules for formatting your code in a consistent way.  This
    is to avoid differences in aesthetic as well as functional style of a
    program.  They are always a nice thing to have for larger projects and are
    absolutely necessary for projects with large teams of contributors.

    Style Guides, when enforced correctly, make the code-base of a project more
    readable and understandable.  Instead of formatting blocks in a mish-mash
    of ways and designing functions sometimes do one thing or sometimes do many
    things the code is consistent and easier to manage.


Example: Linux Kernel Standards
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Linux kernel style guidelines are actually fun to read:

    First off, I’d suggest printing out a copy of the GNU coding standards, and
    NOT read it. Burn them, it’s a great symbolic gesture.

    [ https://www.kernel.org/doc/Documentation/CodingStyle ]

NASA’s Jet Propulsion Laboratory style guidelines are very short and are
concerned with automated tooling to do code analysis:

    All loops shall have a statically determinable upper-bound on the maximum
    number of loop iterations.

    [ http://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf ]


Style Guides Enforced by Linters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Style guides may be enforced by linters.  This allows you to integrate
    style-guide enforcement into your Continuous Integration toolchain.  This
    usually requires formalizing your style guide in your linter's
    configuration file.


Dependency Isolation
--------------------

.. ifslides::

    *The process of -- wait for it -- isolating project dependencies.*

.. ifnotslides::

    Dependency isolation is the process of -- wait for it -- isolating the
    dependencies of a project.  This is a suprisingly hard problem and many
    consider it largely un-solved.

    The root of the issue is that you might be developing two programs: FooFOSS
    and BarEnterprise.  They both depend on the library bazUseful but on
    depends on version 1.1.7 and the other depends on the more stable 1.0.1a.
    You can't just install the most recent one and call it good, you've got to
    figure something else out instead.


Python: Virtualenv
~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    The way python handles the issue is with Virtual Environments (venvs),
    which should not be confused with Virtual Machines which are *completely
    different*.

    You have to activate a venv to be *inside the venv*.  Once you have done
    that your environment is told "When you want to use this library, look in
    this directory only."  Then all of your dependencies are placed in that
    directory thus isolating your dependencies.

    It isn't a perfect system but it works for the Pythonista ecosystem and
    hasn't been replaced yet.

Setup and *enter* the virtual environment.

::

    $ virtualenv <virtualenv name>
    New python executable in /path/to/<venv name>/bin/python
    Installing setuptools, pip, wheel...
    done.
    $ soruce <venv name>/bin/activate

Install a package.  This installs it in the current working directory and so
does not ask for root permissions.

::

    (<venv name>) $ pip install flask
    [...]

.. nextslide::

To list all packages in the venv:

::

    (<venv name>) $ pip freeze
    click==6.6
    Flask==0.11.1
    itsdangerous==0.24
    Jinja2==2.8
    MarkupSafe==0.23
    Werkzeug==0.11.11

Deactivate (leave) the venv.

::

    (<venv name>) $ deactivate
    $


Other Examples
~~~~~~~~~~~~~~

.. ifnotslides::

    Many other languages attack the dependencies issue in smarter and less smart
    ways.

Node.js:
    Creates a ``node_modules`` directory and tracks dependencies in
    ``package.json``.

Go:
    Dependencies are tracked via git repositories and using the go get command.

Rust:
    Dependencies and versions are specified in ``Cargo.toml``.  All compiled
    code (and dependencies) are stored in a ``target`` directory.


Development Servers
-------------------

    *A Carbon Copy of the Production Environment(s)*

.. ifnotslides::

    Development servers are used to test that your code works in a real
    environment, with a real server, and real data.  You shouldn't throw your
    code up on a *production* website to see if it works, so a development
    server is as close to the real thing as you can get.


TODO
----

.. TODO: Add activity


Further Reading
---------------

- The `Community Ruby Style Guide`_ is a good resource for anybody learning
  Ruby.  It's the style guide that `Rubocop`_ enforces.

- The `Official Python Style Guide`_ is a well respected style guide for
  Python and is commonly accepted as *the* python style guide.

.. TODO: Add futher reading.

.. _Community Ruby Style Guide:
        https://github.com/bbatsov/ruby-style-guide#prelude
.. _Rubocop: https://github.com/bbatsov/rubocop
.. _Official Python Style Guide: https://www.python.org/dev/peps/pep-0008/
