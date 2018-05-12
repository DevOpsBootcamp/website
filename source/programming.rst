.. _programming:


Lesson 9: Programming
=====================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/programming.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/programming.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - Programming Paradigms.
    - Psuedo-Code exercise.
    - Python Overview.
    - Python practice exercise.

Paradigms
---------

Programming is a big topic.

.. image:: /static/huge.gif
    :align: center
    :target: https://www.tenor.co/view/big-huge-large-billnye-gif-4824554
    :alt: Bill Nye the Science Guy, 'Huge!'

.. ifnotslides::

    We will cover the conceptual basics of programming before doing any
    programming.  Don't worry, you'll be coding soon.


Note: Pseudo-code
~~~~~~~~~~~~~~~~~

.. ifnotslides::

    We will be using pseudo-code (fake code) to express and demonstrate
    concepts.  This isn't necessarily code you can run on a computer; it is
    close to human language to enable teaching *concepts* without getting
    bogged down by exact *syntax* necessary in a formal programming language.

::

    function f(x):
        # This line is a comment, not run by the computer.
        # Comments are only for human eyes.
        if x is less than than 5
            print "x is less than 5"
        else if x is less than than 10
            print "x is greater than five and less than 10"
        else
            print "x is greater than 10"


Variables & Constants
~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Variables are a name used to refer to a piece of data.  In languages that
    use a syntax derived from C, variable assignment will usually look
    something along the lines of ``<variable name> = <variable value>``.
    Some languages have *mutable* variables, meaning a variable can change its
    value, and others have *immutable* variables, meaning once a variable is
    assigned its value does not change.  A large majority of languages support
    both kinds.

    Constants are variables that are *static* (known before the program is
    run).

::

    >>> x = "value"
    >>> print(x)
    value
    >>> x = "different value"
    >>> print(x)
    different value


Data Types
~~~~~~~~~~

    Data types dictate how a piece of data should be handled within a program.

.. ifslides::

    ============ ============================================================
    **Static**   Types are known at compile time and defined by the programmer.
    **Dynamic**  Types may change based on how the program runs.
    **Strongly** Types are enforced and cannot change.
    **Weakly**   Types are fluid and can be 'bent' based on needs.
    ============ ============================================================

    .. nextslide::

    Common types:
        ======= ==========================
        Int     ``1, 5, 10000``
        Float   ``1.5, 3.14159``
        Char    ``'a', 'f', 'g'``
        String  ``"foo", "BAR"``
        Array   ``[1, 2, 3], ['a', 'b', 'c']``
        ======= ==========================

.. ifnotslides::

    Static Vs Dynamic Typing
        In statically typed languages, types are either known or deduced at
        compile time.  When you run a program, the computer knows which
        variables are integers, which variables are strings, etc.  Examples
        of statically typed languages include C, C++, and Java.

        In dynamically typed languages, you don't know what the type of a
        variable is until it has been assigned.  Examples of dynamically typed
        languages include Python, Ruby, and PHP.

    Strong Vs Weak Typing
        Strongly typed languages enforce type safety. What this means is that
        you can't, for example, use an ``int`` in the place of a ``float``.
        However, this can be useful for catching bugs that would otherwise hide
        themselves in large codebases and cause problems.

        Weakly typed languages are permissive in allowing types to act like
        different types.  In reality, though, no language is either strongly
        or weakly typed.  However, some languages are more strongly typed than
        others.

    Common types:
        ======= ==========================
        Int     1, 5, 10000
        Float   1.5, 3.14159
        Char    'a', 'f', 'g'
        String  "foo", "BAR"
        Array   [1, 2, 3], ['a', 'b', 'c']
        ======= ==========================

    You can even combine types to create *data structures*. Data structures
    are another important computer science concept and a topic for another day,
    but they are immensely useful tools.

Flow Control
~~~~~~~~~~~~

    Flow Control allows you to execute code only if certain conditions are met.

.. ifnotslides::

    Think of your program's flow-control as water running in a stream.
    Sometimes the stream hits a rock and flows around, or it encounters a fork,
    causing it to diverge permanently.  Occasionally the stream will go into a
    pool and whirl around for a bit and then return to the main
    path. Eventually, the water will exit into a sea or ocean.

    This isn't a perfect metaphor, but visualizing this as your program
    starting at some single point and having the possibility to branch and
    loop may help you understand what it means for a program to *flow* and for
    you to control that flow.

    Consider a problem: You are writing a program and you want it to make a
    decision.  Given a number you want it to either multiply it by 2 if it's
    too small, or divide it by 2 if it's too big.  This is the perfect
    use-case of an 'if' statement, or more formally a **Conditional**
    statement.

Conditionals: If / Else If / Else
    Conditionals are used to tell the program when to execute commands.

    In pseudocode, they usually look something like

    ::

        if some conditional statement is true
            do something
        else if some other conditional
            do something else
        else
            do a final thing

.. ifnotslides::

    In this conditional block, the first conditional statement is evaluated
    to either True or False. If it's True, the program continues on inside
    the block with ``do something``. If the conditional evaluates to False,
    then the conditional inside ``else if`` is evaluated and handled
    accordingly. You can have any number of ``else if`` statements. At the end,
    the code inside the ``else`` statement executes if none of the other
    conditions were met. The ``else if`` and ``else`` aren't required, but they
    can be useful when you have more sophisticated control flow.

.. nextslide::

.. ifnotslides::

    Now consider a different problem: You want to look through a list of names
    and print out every one that starts with the letter 'Q'.  This is where
    the **Loop** comes in to play.  A loop is exactly what it sounds like-- it
    is any construct that allows you to carry out some operation multiple
    times, without having to copy and paste code for each time the commands are
    executed.

Loops: For / While / Do While
    Loops are used to do multiple things, usually an *indefinite* number
    of things.

    For instance:

    ::

        for every element, let's call it "foo", in a list "my_list"
            if foo is greater than five
                print(foo)
            else
                print(foo + " is too small")

    **While** loops execute indefinitely (while something continues to
    be true).

    **For** loops iterate over a list (array) of elements or to a specific
    number.


Input & Output
~~~~~~~~~~~~~~

.. ifnotslides::

    Programs aren't very useful unless they can get data from the outside
    world and return the results they've found.  I/O is the concept of

    #. Getting input from a user, a file, or the outside world.
    #. Doing something with that data.
    #. Outputting a result.

::

    >>> user_input = get_input("Where would you like to go today? ")
    >>> -> Where would you like to go today? Nebraska
    >>> print(user_input)
    >>> -> nebraska
    >>> print(reverse(user_input))
    >>> -> aksarben

.. ifnotslides::

    IO is useful for making a user-interface and for debugging a program. You
    can print out variables that you think might be getting set wrong, loops
    which might not be working the way you want, etc.


Functions
~~~~~~~~~

.. ifnotslides::

    Functions are how we put a set of functionality in a box.  Instead of
    typing the same code over and over we write a function which runs those
    lines of code for us.  When you make a change in the function it changes
    the behavior of the program every time that function is called.

    Functions take arguments (input) and return values (output). Some
    functions return nothing, i.e. a value called "Null".

::

    function read_file(x):
        # Also check that it exists! How convenient!
        if file_exists(x)
            v = read_file_to_string(x)
            return v
        else
            print("file does not exist")
            return Null

.. ifnotslides::

    In this pseudo-code we've specified the steps for reading the
    contents of a file to a string (text).  The function returns the contents
    of the file if the file exists and returns ``Null`` if the file does not
    exist.  This type of return value is useful because when we use it we can
    check "did this function return a string or Null" to determine if we
    passed a 'good' filename.

    We also called (used) functions in this function, which is totally
    allowed!  The function we used were ``file_exists``,
    ``read_file_to_string`` and ``print``.  The ``file_exists`` function we
    can assume returns a ``bool`` (true/false) and the ``read_file_to_string``
    returns a string type.


Structs
~~~~~~~

.. ifnotslides::

    Structs are collections of logically grouped variables.  They can be
    treated as variables with sub-variables.

    Here is a declaration of a struct ``dog``:

::

    struct dog {
        breed: String
        height: Float
        color: String
        age: Integer
    }

.. ifnotslides::

    To use a struct you access it's *members* like so:

::

    spot = struct dog      # Create a new variable of type `struct dog`
    spot.breed = "corgie"  # Assign each member a variable.
    spot.height = 1.5
    spot.color = "Blond"
    spot.age = 1
    print(spot.breed, spot.height, spot.color, spot.age)

.. ifnotslides::

    In our declaration we specified each member and its type for the struct.
    Each language's implementation (or lack thereof) of structs differs
    slightly but all act about the same.


Objects
~~~~~~~

.. ifnotslides::

    Objects are collections of logically grouped functions *and* variables.
    They are declared in a **class** and an instance of a class is an
    **object**.  The *class*  can be thought of as the **blueprint for an
    object**.

    Objects usually have an initialization function that takes arguments so you
    can create a unique object.

::

    class chair():
        function init(material):
            self.material = material

        function rock():
            print("The ", self.material, " chair rocks slowly.")

.. ifnotslides::

    To create an instance of a class (object), you use some syntax like the
    following:

::

    >>> my_chair = chair.init("plastic")
    >>> my_chair.rock()
    >>> -> The plastic chair rocks slowly.

.. ifnotslides::

    Note that we treated structs like a data type (declaring ``var = struct
    struct_type`` while we treat objects more like functions.  The variable
    my_chair is assigned to the **return value** of the ``chair``'s ``init``
    function.  Once you have an object you can call the object's functions,
    formally referred to as ``methods``.


Libraries
~~~~~~~~~

.. ifnotslides::

    Libraries are collections of functions and constants external to the file
    you're working on.  They may be written by somebody else or written by you
    in a seperate file.

    The usual syntax for **using** a library looks like this:

::

    import math_lib

    print(math_lib.pi, math_lib.pow(2, 5), math_lib.tan(79.3))
    # prints out "3.14 32 .951"


TODO: Write Pseudo-Code
-----------------------

Write pseudo-code to do the following tasks:
    - Count to 20 (hint: ``for`` loop).
    - Get user input and print it.
    - Generate prime numbers.

Hints:
    - Break the problem down to the simplest steps.
    - Don't worry about the details.
    - This is pseudo-code! Get creative.

.. ifnotslides::

    Answers:
        ::

            for i starting at 1 and ending at 20:
                print(i)

        ::

            input = prompt_for_input("Please enter a number: ")
            print("Your input was ", input)

        ::

            i = 2
            while i < 100
                for j starting at i going down to 1:
                    if j is 1:
                        print( i, "is a prime number")

                    if j / i is a round number:
                        Skip to the next iteration of this inner loop.

Python
------

::

    $ sudo <apt or yum> install python

.. image:: /static/python.png
    :target: http://python.org
    :alt: python programming language logo
    :align: center
    :width: 50%

.. ifnotslides::

    Python is a programming language designed for *learning*.  This means it
    is relatively simple to pick-up and run with, and it looks a lot like
    pseudo-code you might write.  It is very popular, modestly fast, and
    commonly used in the programming industry.

    Python is a *scripting language*. While other languages need to be
    *compiled* and then have a binary run, you run the script directly with ``$
    python my_script.py``.

    One advantage to scripts is that you can write functions in a file and
    Python will just run them-- you don't need to write a ``main()`` function
    or anything!


Python Datatypes
~~~~~~~~~~~~~~~~

* You don't need to declare the type of your variables, Python will assume
  the type of your variable and type it for you.
* Python is a duckly-typed language. If it walks like a duck and quacks like
  a duck, then Python treats it like a duck. As long as an object implements
  the proper *interfaces*, it can act like any type it wants.

.. figure:: /static/duckly.gif
    :align: center

.. nextslide::

==========  ===================================================================
Type        Example
----------  -------------------------------------------------------------------
boolean     ``True``
integer     ``7``
long        ``18,446,744,073,709,551,615``
float       ``12.4``
string      ``"Hello World!"``
list        ``['first', 'second']``
dict (map)  ``{'key1': 'value', 'key2', 'value2'}``
tuple       ``('value','paired value')``
object      ``anObjects.variable == <value>``
**None**    |
==========  ===================================================================


Python Variables
~~~~~~~~~~~~~~~~

.. code-block:: python

    # This is a comment
    boolean = True # boolean
    name = "Lucy" # string
    age = 20 # integer
    pi = 3.14159 # float
    alphabet = ['a', 'b', 'c']
    dictionary = {"pi":3.14159, "sqrt 1":1}
    winter = ('December', 'January', 'February', 'March')

    print(name + " is " + str(age+1) + " this " winter[3])


REPL: Try it out
~~~~~~~~~~~~~~~~

Open a REPL (Read Evaluate Print Loop):

.. code-block:: python

    $ python
    >>> print("I'm in a REPL!")
    >>> name =      # <Your name>
    >>> age =       # <Your age>
    >>> print(name + " is " + str(age))
    >>> # We need to convert age from int to string so it can print!


Python Control Flow
~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Below is an example of flow-control in Python.

    **Note** You test equality (is x equivalent to y) with ``==`` not ``=``.

.. code-block:: python

    if name == "Lucy":
        for month in winter:
            print name + " doesn't like " + month
    else:
        print "My name isn't Lucy!"


Python Functions
~~~~~~~~~~~~~~~~

.. ifnotslides::

    Below is the exact syntax for declaring a function in Python.

.. code-block:: python

    def myfunction(arg1, arg2):
        return arg1 + arg2

    print myfunction(1, 5)

.. figure:: /static/function-machine.png
    :align: center
    :height: 300px


Python Libraries
~~~~~~~~~~~~~~~~

There are a few ways to use other code in your code:

.. code-block:: python

    from math import pi
    x = pi

.. code-block:: python

    from math import *
    x = pi


.. nextslide::

There are **hundreds** of Python libraries.  If you're trying to
do something and think "This has probably been solved...", Google it!

Some libraries to know:

* sys
* os
* dateutil
* future
* `And more`_

.. _And more: https://wiki.python.org/moin/UsefulModules


Python (Virtual) Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    When developing a Python project you will want to use a *virtual
    environment*.  This isolates the dependencies of your project from the
    Python software installed on your computer.

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


TODO: Practicing Python
-----------------------

Formalize the last ``TODO`` by writing them in Python.

Prove the program works by running the code!


Further Reading
---------------

`Python on Learnpython.org`_
    The Python programming language's website offers some good (free)
    tutorials and reference documentation.

`Python on Codecademy`_
    Codecademy is a great resource for learning many programming languages and
    offers a good (free) beginner's guide to Python.

`CS 160`_, `161`_, `162`_
    These OSU courses focus on programming fundamentals covered in this lesson
    in greater detail.  Python is used in CS 160 and C/C++ is used in CS 161
    and CS 162.

.. _Python on Codecademy: https://www.codecademy.com/learn/python
.. _Python on Learnpython.org: http://www.learnpython.org/
.. _CS 160: http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=CS&coursenumber=160
.. _161: http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=CS&coursenumber=161
.. _162: http://catalog.oregonstate.edu/CourseDetail.aspx?subjectcode=CS&coursenumber=162
