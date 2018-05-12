.. _development_processes_tool:


Lesson 15: Dev Processes & Tools
================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/development-processes-tools.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/development-processes-tools.html
.. _Video:

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



Code Analysis
-------------

Code analysis tools are some of the most important tools in a developer's
arsenal when it comes to finding and fixing bugs. Code analysis tools come in
two flavors:

.. ifslides::

  Static Analysis:
    A tool performs static analysis if it works without running your code.
    Examples include linters and type checks.

  Dynamic Analysis:
    Dynamic Code Analysis tools actually run your code and verify it by watching
    how the program acts. Examples include rspec for Ruby.

.. ifnotslides::

  - **Static Analysis**

    A tool performs static analysis if it works without running your code.
    Static analysis tools such as linters and type checkers are usually the
    first line of defense against bad code because they can be automatically
    run by Continuous Integration every time code is pushed to a remote
    repository.

    Static analysis can be an incredibly valuable tool in situations where
    it's very important that the code works perfectly every single time,
    such as in missile defense systems or stock trading.

  - **Dynamic Analysis**

    Dynamic Code Analysis tools actually run your code and verify it by
    watching how the program acts, where it fails, how it uses resources
    such as processor time and memory, how long it takes to finish running,
    and if your tests are adequate enough.


Debugging Tools
---------------

Debuggers are interactive dynamic analysis tools that are used to inspect your
code as it runs.

- Print (broken) variables.
- Read and reports error messages.
- Highlight (incorrect) syntax.

.. ifnotslides::

    Even if you've never used a debugger before, chances are that at some point
    you've debugged your code by using print statements to check the contents of
    your variables at different points throughout your program (Also called
    "printf debugging"). If you find yourself doing this often, however, it's
    usually more efficient to learn how to use a proper debugger.


CLI Debugging Tools
~~~~~~~~~~~~~~~~~~~

**C/C++ Tools**

- GDB

    .. ifnotslides::

        Used to inspect and debug everything in a C program from
        variables to why it encountered a fatal failure. Generally called the
        swiss-army-knife of debugging, a great tool to use in programming,
        allows you to set *'break points'* where the program stops mid-run and
        you can see what it's doing.

- Valgrind

    .. ifnotslides::

        Valgrind is a program that keeps track of a program's memory usage and
        reports on any definite or potential memory leaks. For example:

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

**Python Tools**

- PDB

    .. ifnotslides::

        PDB is a Python debugger that comes default in the Python Standard
        Library. It's similar to GDB and other debuggers, but with the added
        features of being able to easily extend its functionality and run
        Python code directly inside the debugger interface.

**NodeJS Tools**

- node debug

    .. ifnotslides::

        Barebones debugger that comes with NodeJS. Possible to use for simple
        debugging tasks like setting breakpoints and stepping through code, but
        not much past that.

- Node Inspector

    .. ifnotslides::

        A more fully-featured NodeJS debugger.


Web Consoles
~~~~~~~~~~~~

.. ifnotslides::

    Web Consoles are useful tools built directly into your browser for
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

Linters inspect your code and flags suspicious usage.  This can be to enforce a
style guide or to flag code which will probably not compile or break the program
when it is running.

Examples:
    - ``flake8`` (Python)
    - ``rubocop`` (Ruby)
    - ``splint`` (C)
    - ``jshint`` (NodeJS)

::

    src/times.js: line 407, col 20, Expected '{' and instead saw 'return'.
    src/times.js: line 415, col 49, Missing semicolon.
    src/times.js: line 407, col 58, 'error' is not defined.


Code Coverage
-------------

.. ifslides::

  Code Coverage is the process of running your tests and keeping track of which
  lines, logic branches, and files are used in the test suite.

  This is useful because it demonstrates how much your tests are actually doing
  (proving your program does what it should) and proves if you're carrying
  around a bunch of dead code.

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

::

    Name                      Stmts   Miss  Cover   Missing
    -------------------------------------------------------
    my_program.py                20      4    80%   33-35, 39
    my_other_module.py           56      6    89%   17-23
    -------------------------------------------------------
    TOTAL                        76     10    87%


Integrated Development Environments (IDE)
-----------------------------------------

.. image:: /static/minecraft_debug.gif
    :align: center
    :width: 80%
    :alt: Debugging in Minecraft
    :target: https://www.reddit.com/r/Minecraft/comments/3pnwgn/the_new_debug_screen/


IDEs are programs used to help developers get their job done by integrating many
essential tools into one ecosystem.

.. ifnotslides::

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
    - **Netbeans**  (Java)
    - **Visual Studio**  (.NET)
    - **PyCharm**  (Python)
    - **Eclipse**  (Many)
    - **Atom** (Many)


Style Guides
------------

.. image:: /static/code_quality.png
    :alt: XKCD Code Quality comic
    :target: https://xkcd.com/1513/
    :align: center

.. ifslides::

  Style Guides are rules for formatting your code in a consistent way.  This is
  to avoid differences in aesthetic as well as functional style of a program.

  Style Guides, when enforced correctly, make the code-base of a project more
  readable and understandable.

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


Example: Real-World Style Guides
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Linux kernel style guidelines are actually fun to read:

    "First off, I’d suggest printing out a copy of the GNU coding standards, and
    NOT read it. Burn them, it’s a great symbolic gesture."

    -- `Linux Kernel Coding Style`_

NASA’s Jet Propulsion Laboratory style guidelines are very short and are
concerned with automated tooling to do code analysis:

    "All loops shall have a statically determinable upper-bound on the maximum
    number of loop iterations."

    -- `JPL Coding Standard`_


.. _Linux Kernel Coding Style: https://tinylab.gitbooks.io/linux-doc/content/en/CodingStyle.html
.. _JPL Coding Standard: https://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf


Dependency Isolation
--------------------

Dependency isolation is the process of -- wait for it -- isolating the
dependencies of a project.  This is a surprisingly hard problem and many
consider it largely unsolved.

.. ifslides::
    - Two applications: ``FooFOSS`` and ``BarEnterprise``
    - They both depend on the library ``bazUseful``
    - One depends on version 1.1.7 and the other depends on the more stable
      1.0.1a.

.. ifnotslides::

    The root of the issue is that you might be developing two programs:
    ``FooFOSS`` and ``BarEnterprise``.  They both depend on the library
    ``bazUseful`` but one depends on version 1.1.7 and the other depends on the
    more stable 1.0.1a.  You can't just install the most recent one and call it
    good, you've got to figure something else out instead.


TODO: Python Virtualenvs
~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    The way Python handles the issue is with Virtual Environments (venvs).
    Venvs should not be confused with Virtual Machines which are *completely
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
    $ source <venv name>/bin/activate

Install a package.  This installs it in the current working directory and so
does not ask for root permissions.

::

    (<venv name>) $ pip install flask
    [...]

.. nextslide::

To list all packages in the venv:

::

    (<venv name>) $ pip freeze
    click==6.7
    Flask==1.0.2
    itsdangerous==0.24
    Jinja2==2.10
    MarkupSafe==1.0
    Werkzeug==0.14.1

Deactivate (leave) the venv.

::

    (<venv name>) $ deactivate
    $


Other Examples
~~~~~~~~~~~~~~

.. ifnotslides::

    Many other languages attack the dependencies issue in smarter and less smart
    ways. Whether each solution is more or less intelligent than the others is
    a popular topic for both friendly and unfriendly debate over the internet.

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

Development servers are used to test that your code works in a real environment,
with a real server, and real data.  You shouldn't throw your code up on a
*production* website to see if it works, so a development server is as close to
the real thing as you can get.


Further Reading
---------------

- The `Community Ruby Style Guide`_ is a good resource for anybody learning
  Ruby.  It's the style guide that `Rubocop`_ enforces.

- The `Official Python Style Guide`_ (PEP8) is a well respected style guide for
  Python and is commonly accepted as *the* python style guide.

.. TODO: Add futher reading.

.. _Community Ruby Style Guide:
        https://github.com/bbatsov/ruby-style-guide#prelude
.. _Rubocop: https://github.com/bbatsov/rubocop
.. _Official Python Style Guide: https://www.python.org/dev/peps/pep-0008/
