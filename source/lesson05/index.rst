.. _python_programming_basics:


Lesson 5: Python and Programming Basics
=======================================

Types
-----

    "...a classification identifying one of various types of data"

.. figure:: /static/duckly-typed.jpg
    :align: right
    :height: 200px

* Static vs. Dynamic
* Strong vs. Weak
* Duckly-typed
* A few common types:

  * Int (the only truly necessary type!)
  * Double (or float)
  * Char

Variables & Constants
---------------------

    "...a storage location paired with an associated symbolic name..."

* **Global Variables are Bad**.
* Using another name to refer to something in memory.
* Know your scope!

.. figure:: /static/bad-math.jpg
    :align: center
    :height: 300px

Control Statements
------------------

    "...the specification of the order in which the individual statements,
    instructions or function calls of an imperative program are executed or
    evaluated..."

* The order of execution of statements
* If / Else If / Else and other conditionals
* For / While loop

Input & Output (I/O)
--------------------

    "...the communication between an information processing system, such as a
    computer, and the outside world..."

* Program needs to be able to communicate with your machine.
* Try debugging without print statements -- it's hard!

.. figure:: /static/blackbox-io.png
    :align: center

The Bare Minimum
----------------

* Access to memory
* Arithmetic
* Logic
* I/O
* Control statements

Try it out:
-----------

Write psuedo code to:

#. Count to 20 *programmatically* (hint: ``for`` loop)
#. Get the users name and print it
#. Generate prime numbers

Keep in mind:

* What are the steps?
* Don't worry about details

Python
------

.. code::

    sudo [apt|yum] install python

.. figure:: /static/python.png
    :align: center
    :height: 350px

Datatypes
---------

* Python is a duckly-typed language: you don't need to declare the type
  of your variables, and python will assume the type of your variable
  and implicitly type it.
* It's also dynamically typed, so you can change the type of a variable
  at any time

.. figure:: /static/duckly.gif
    :align: center

.. nextslide::

==========  =========
Type        Example
==========  =========
boolean     ``True``
integer     ``7``
long        ``18,446,744,073,709,551,615``
float       ``12.4``
string      ``"Hello World!"``
list        ``['first', 'second']``
dict (map)  ``{'key1': 'value', 'key2', 'value2'}``
tuple       ``('value','paired value')``
object      ``anObjects.variable == <value>``
None        |
==========  =========

Variables
---------

.. code-block:: python

    # This is a comment
    bool = True # boolean
    name = "Lucy" # string
    age = 20 # integer
    pi = 3.14159 # float
    alphabet = ['a', 'b', 'c']
    dictionary = {"pi":3.14159, "sqrt 1":1}
    winter = ('December', 'January', 'February', 'March')

    print(name + " is " + age+1 + " this " winter[3])

Try it out
----------

Open a repl (read eval print loop):

.. code-block:: python

    $ python
    >>> name =      # <Your name>
    >>> age =       # <Your age>
    >>> print name + " is " + str(age)

* We need to convert age from int to string so it can print!

Control flow
------------

.. code-block:: python

    if name == "Lucy":
        for month in winter:
            print name + " doesn't like " + month
    else:
        print "My name isn't Lucy!"

* Note: Why :code:`==` and not just `=`?

Functions
---------

Functions in python aren't particularly special,
but we will be using them in the exercises so
wanted to provide you with an example.

.. code-block:: python

    def myfunction(arg1, arg2):
        return arg1 + arg2

    print myfunction(1, 5)

.. figure:: /static/function-machine.png
    :align: center
    :height: 300px

Libraries
---------

    "... a collection of non-volatile resources used by computer programs,
    often to develop software..."

There are a few ways to use other code in your code:

.. code-block:: python

    import math.pi
    x = math.pi

.. code-block:: python

    from math import pi
    x = pi

.. code-block:: python

    from math import *
    x = pi


.. nextslide::

There are **hundreds** of python libraries.  If you're trying to
do something an think "This has probably been solved...", google it!

Some libraries to know:

* sys
* os
* dateutil
* future
* `And more`_

.. _And more: https://wiki.python.org/moin/UsefulModules

Environments
------------

* Python virtual environments are unique

.. code-block:: none

    $ sudo apt-get install python-virtualenv
    $ sudo yum install

    # In each project you work on, you'll want to run
    $ virtualenv venv
    $ source venv/bin/activate
    (venv)$ pip install <package>
    (venv)$ deactivate

.. figure:: /static/environments.jpg
    :align: center
    :height: 200px

Let's do stuff!
---------------

Try some of our `exercises`_ to hone
your python skills!

.. _exercises: https://github.com/DevOpsBootcamp/Bootcamp-Exercises/blob/master/programming-basics/exercise.rst
