.. _testing:


Lesson 11: Testing
==================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/testing.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/testing.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What testing is.
    - Why it's important.
    - Anatomy of a test.
    - Types of testing.
    - Mocking.
    - Set-up/Tear-down.


Testing
-------

.. ifnotslides::

    Automated testing, commonly referred to as just 'testing', is writing code
    that tests your code.

    This can be as simple as calling a function and expecting an specific
    output or as complicated as simulating button clicks on a webpage.  The
    field of testing is broad and key to modern development.

::

    def add_double(x, y):
        return 2*(x+y)

    def test_add_double():
        expect(add_double(1, 2) == 6)


Why Testing Matters
-------------------

.. image:: /static/mars.png
    :align: center
    :alt: mars testing example

.. ifnotslides::

    The first program you wrote you probably tested *manually*. This means you
    ran the program, fed it inputs, and read the outputs by hand.

    With automated testing you spend a slightly longer up-front in writing the
    tests up, but then you can run *all* of your tests with a single command
    (or with Continuous Integration, no commands at all!)

    Testing is very important when there's a lot of money or time (or both!)
    invested in a project.


Structure of a Test
-------------------

Most test are consist of the same general structure:

.. ifslides::

    - Set-up
    - Expected output
    - Actual output
    - Comparison
    - Tear-down

.. ifnotslides::

    Set-up
        Any pre-testing steps occur here.  For instance your application may
        use a database, this is where you would populate that database with
        test data.

    Expected output
        The *expected* result some function(s) call(s) is outlined.

    Actual output
        The functionality being tested is used and recorded.

    Comparison
        Now the two values (expected and actual) are compared, usually using
        some form of the syntax ``expect(expected == actual)``. If the
        contents of the ``expect`` call is false then the test-runner (more on
        that later) raises an error, continues running the test, and produces
        a traceback at the end of all tests.

    Tear-down
        The setup and test is un-done.  If data was populated during the test
        that data is removed, if files were written they are deleted.  This is
        to ensure that each test is completed in the same environment and each
        one is self-contained.


Types of Testing
----------------

.. ifslides::

    - **Unit Testing:** How well each piece works.
    - **Integration Testing:** How well the pieces work together.
    - **Systems Testing:** How it all works in production.

.. ifnotslides::

    There isn't just *testing*.  Testing happens at many stages of development
    and in many different ways.  Here we will discuss three major types:

    Unit Testing
        Testing each component (function, struct, class, etc) individually,
        ignoring how the program works as a whole in favor of verifying each
        piece.

        ::

            include app_library

            def test_math_function():
                expected = 5.67
                actual = math_func(1, 2, 3, 4)
                expect(actual == expected)

    Integration Testing
        Testing how each function works together.  Ensuring the components do what
        they are expected to do.

    Systems Testing
        Testing the program as a whole in an environment (computer, operating
        system) similar to it's target platform(s).


Concept: Mocking
----------------

    Simulating behavior external to a program so your tests can run
    independently of other platforms.

    You're testing **your** program, not somebody else's.  Mock other people's
    stuff, not your own.

.. ifnotslides::

    **For example:** If you are writing a library that wraps a web API you
    would mock that API so you can ensure the tests run even when website it
    wraps is down.


Testing Frameworks
------------------

.. ifnotslides::

    Testing frameworks range in the functionality they provide from simply
    running detecting tests functions, to helping programmers articulate tests
    closer to English, to forcing a very logical type of organization on your
    tests.

::

    $ run tests
    Finding tests...
    Running tests in tests/foo.ext
    Running tests in tests/bar.ext
    Running tests in misc/test_baz.ext


Frameworks vs 'The Hard Way'
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

While you *can* write tests the hard way:

::

    var = some_function(x)
    if var == expected_output:
        continue
    else
        print("Test X failed!")

::

    $ run test
    Test 5 failed!

.. nextslide::

It's usually easier to use a framework.

::

    def simple_test():
        expect(some_function(x), expected_output)

::

    $ run tests
    ....x.....
    Test 5 failed.
    Debug information:
    ...


Teardown and Setup
~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    One major advantage all testing frameworks offer is the concept of "setup"
    and "teardown".  This is the process of running a function, or set of
    instructions, before and after each test.

Useful for:
    - populate a test database
    - write and delete files
    - or anything you want!

.. ifnotslides::

    The advantage of setup/teardown is that each test is run in the same
    environment.  This allows you to write the tests and not worry about
    "Wait, is there anything in the database when this is run?  I specifically
    only need X in the database."

::

    def tests_setup():
        connect to database
        populate database with test data

    def tests_teardown():
        delete all data from test database
        disconnect from database

    def some_test()
        setup is called automaically
        use data in database
        asset something is true
        teardown is run automatically


TODO: Using Python's ``unittest``
---------------------------------

.. TODO: Add activity



Further Reading
---------------

CS 362
    This OSU Course covers testing *very* in depth and even covers types of
    testing including *Random* testing and testing analysis.

`Python Unittest Documentation`_
    A good reference for using Python's built-in unit-testing module.

.. TODO: Add one more piece of further reading.

.. _Python Unittest Documentation: https://docs.python.org/2/library/unittest.html
