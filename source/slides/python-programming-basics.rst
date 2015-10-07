.. _python_programming_basics:

Python and Programming Basics
=============================

Types
-----

* Static vs. Dynamic
* Strong vs. Weak
* Duckly-typed
* A few common types:

  * Int (the only truly necessary type!)
  * Double (or float)
  * Char

.. figure:: /static/duckly-typed.jpg
    :align: center
    :height: 200px

Variables & Constants
---------------------

* **Avoid Globals**
* Using another name to refer to something in memory
* Know your scope!

.. figure:: /static/bad-math.jpg
    :align: center
    :height: 400px

Control Statements
------------------

* Change order of execution of statements
* If and other conditionals
* For loop
* While loop

Input & Output (I/O)
--------------------

* Program needs to be able to communicate with your machine.
* Try debugging without print statements

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

* Count to 20 programmatically (can't say "print 1; print 2; print3;"!)
* Get the users name and print it
* Generate prime numbers (more advanced)

Keep in mind:

* What are the steps?
* Don't worry about details

Python
======

.. code::

    sudo [apt|yum] install python

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

* boolean
* integer
* long
* float
* string
* list
* dict (map)
* tuple
* object
* None 

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
    >>> name = # Your name
    >>> age = # Your age
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

Words
-----

If it highlights, **don't use it as a variable name**

Some words to know:

* 

Functions
---------

There's nothing unique about functions, but there 
are a few of them in the exercises, so here's 
an example:

.. code-block:: python

    def myfunction(arg1, arg2):
        return arg1 + arg2
    
    print myfunction(1, 5)
    

Libraries
---------

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

Let's do stuff!
===============

.. _And more: https://wiki.python.org/moin/UsefulModules
