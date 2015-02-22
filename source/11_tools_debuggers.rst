.. anything with a question mark by it is something I'm
    not certain should be included.  This is just a layout,
    and is highly flexible.  Please add or delete any slides
    according to your judgement

===============================
Development Tools and Debuggers
===============================

How to find the missing parenthesis.

Debugging
=========

Before we even look at what a debugger is, let's talk about
debugging in general. There are lots of ways to debug without
a debugger that you probably already do, like:

* Printing variables
* Reading error messages
* Syntax highlighting

.. figure:: static/youtube-error.jpg
    :align: center


So what is a debugger?
----------------------
A debugger hooks into your program and runs it. Often it uses special symbols
in the executable to say which line in your code your problem came from.
Interpreted languages have debuggers too! There's PDB for python and ``node
--debug`` for nodejs.

.. figure:: static/debugging-phd.gif
    :align: center

Why is a debugger handy?
------------------------
Sometimes you get this message:

.. code-block:: bash
	$ ./a.out
	Segmentation fault: 11

What's wrong? Heck if I know. Staring at the code won't help. Sometimes
printing your variables doesn't help either. Sometimes you can't even 
print to the screen! A debugger is most helpful when your code is 
really complicated, and you can't tell what's going on.

.. figure:: static/seg-fault.png
    :align: center        
    :scale: 80%

Some Examples...
----------------


Coding Standards
----------------
Code is read much more often than it is written.
A consistent style makes it easier for multiple developers to understand what
is going on. Similar to how we have conventions for writing in
english (indent a paragraph, capitalize the first letter of a sentence,
etc.) there are conventions for writing code to make it easier to 
understand.

Here is an example from the python guidelines:

.. note::
	
    Absolute imports are recommended, as they are usually more readable and tend
	to be better behaved [...]:


.. code-block:: bash
	
    # Do this:
	from mypkg import sibling
	# Not this:
	import mypkg.sibling


Example Standards
-----------------

Python uses PEP8:
https://www.python.org/dev/peps/pep-0008

The Linux kernel style guidelines are concerned with code clarity, but they are
actually fun to read:

.. note::
	First off, I'd suggest printing out a copy of the GNU coding standards,
	and NOT read it.  Burn them, it's a great symbolic gesture.

https://www.kernel.org/doc/Documentation/CodingStyle


NASA's Jet Propulstion Labratory style guidelines are very short 
and are concerned with automated tooling to do code analysis:

.. note::
	All loops shall have a statically determinable upper-bound on the maximum
	number of loop iterations. It shall be possible for a static compliance
	checking tool to affirm the existence of the bound
http://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf

There are many many more.


Linters
-------

* Enforce code style.
* Check for common mistakes.
* Static analysis actually include type checking, which is an invaluable tool
  your compiler already does!

For Python code you can use flake8:

.. code-block:: bash
    
	./monte/parser.py:84:9: E265 block comment should start with '# '
	./monte/parser.py:105:80: E501 line too long (86 > 79 characters)
	./monte/parser.py:153:26: E128 continuation line under-indented for visual
	indent
	./monte/parser.py:153:26: W503 line break before binary operator

.. nextslide::

For C/C++ there is splint:

.. code-block:: bash

	$ splint lexer.c
	Splint 3.1.2 --- 16 Feb 2015

	lexer.c: (in function panic)
	lexer.c:5:10: Argument to exit has implementation defined behavior: -1
	  The argument to exit should be 0, EXIT_SUCCESS or EXIT_FAILURE (Use
	  -exitarg to inhibit warning)

Web Console
-----------

* Ctrl+Shift+K (Command+option+k) in Firefox
* Ctrl+Shift+I (Cmd+opt+I) in Chrome

Web console is great for debugging HTML, CSS and Javascript.
'Console' tab is particularly useful.


Development tools
=================

What can we do to make writing code easier?

Virtual Environments
--------------------
* Very python specific.
* "Wrap up all of my dependencies and libraries and put them in a box here"
* Prevents conflicting versions across projects. e.g. PGD uses Django 1.5, but
  Working Waterfronts uses Django 1.7

Create a virtualenv

.. code-block:: bash

	$ virtualenv my-python-libraries
	$ ls -l .
	drwxr-xr-x  10 Ian  staff  340 Feb 17 11:15 my-python-libraries

Activate the virtualenv so you use the right libraries

.. code-block:: bash

	$ source my-python-libraries/bin/activate

.. nextslide::

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
	$

Package managers
----------------

* System packages are great for installing programs on your computer and making sure that all of your programs' libraries work together.
* They typically contain old versions of development libraries.
* Language package managers only work for a specific language.
* Not all languages have them. In Go language code, as opposed to just keeping a list of libraries you need, it's easier to keep a copy of all of your libraries in your project (gross!).

.. nextslide::

Examples:

* pip for python
* npm for the nodejs javascript framework
* bower for web frontend javascript and CSS
* gem for ruby
* cpan for perl
* cargo for rust

.. figure::  static/ruby-gem.png
    :align: center
    :scale: 20%


Integrated Development Environments
-----------------------------------

Pros:

* Powerful refactoring tools.
* Built in linting and autocompletion.
* A GUI for those who don't like the terminal.

Cons:

* Sometimes slower.

However, you can do all of these things from the command line.

.. nextslide::

My takeaway:
IDEs are a must if you're writing  verbose, library heavy language like Java.
No improvements over vim if you're writing python. It's a tool, sometimes it's
useful, sometimes it's not.


Unit Tests and Testing Frameworks
---------------------------------

Unified Modeling Language
-------------------------

Regular Expressions
-------------------

Development Servers
-------------------
