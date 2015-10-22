.. _testing_and_ci:

Testing and Continuous Integration
==================================

What are tests?
---------------

Tests are a way to make sure your code does what you think your code does.

They can involve testing input to your software to make sure it handles both
normal and edge cases properly, that it will work in its intended environment,
etc.

.. figure:: /static/qaengineer.png
    :align: center
    :height: 200px

.. rst-class:: title-image

Why do you want to test?
------------------------

.. figure:: /static/mars.png
    :align: center

.. note:: "Mars Climate Orbiter - mishap diagram" by Xession - Own work. Licensed under CC BY 3.0 via Commons - https://commons.wikimedia.org/wiki/File\:\Mars_Climate_Orbiter_-_mishap_diagram.png

Types of Testing
----------------

* Unit Testing
* Integration Testing
* System Testing

Unit Testing
------------

Verifies the functionality of a specific section of code.  This is probably the
majority of test writing that you'll do, at least in school.

For an email client, imagine a function that will take a string and return
whether or not it's a valid email address. This function will have
**unit tests** for each case you want to test.

.. figure:: /static/unit-test.jpg
    :align: center
    :height: 100px

Integration Testing
-------------------

Integration testing ensures that the different components of a
software system work together properly.

For instance, the email client might have integration tests that the Send button
verifies the ``To:`` and ``From:`` and then calls the function to send email.

.. figure:: /static/integration-testing.jpg
    :align: center

System Testing
--------------

This is the last type of testing you'll do in building a system.
It tests how the entire sytem works from start to finish, and verifies
that it meets all of the requirements.

System testing pretends the system is a **black box**. It ignores how the code
actually works, and focuses on how the platform as a whole works.

.. figure:: /static/black-box.png
    :align: center
    :height: 300px


Testing Frameworks
------------------

Frameworks are libraries which make testing easier. Generally they
will have a template for writing a test, and then tests will be run
with just one command. Like all frameworks, they mostly just make your
life easier.

The python standard library has the ``unittest`` framework built in.

.. rst-class:: build

Example using ``unittest``
--------------------------

Code being tested:

.. code-block:: python

    def is_all_numbers(response):
        return all(map(str.isdigit, response))

Test case:

.. code-block:: python

    import unittest

    class TestNumbers(unittest.TestCase):
        def test_classify(self):
            all_numbers = ['1', '2', '3', '1', '1']
            not_all_numbers = ['a', '100']
            self.assertTrue(is_all_numbers(all_numbers))
            self.assertFalse(is_all_numbers(not_all_numbers))


Your Turn!
----------

.. code-block:: python

    #!/usr/bin/env python
    def is_number_prime(number):
        """Returns true if argument is a prime number"""
        for element in reversed(range(number)):
            if number % element == 0 and element != 1:
                # exclude one since primes can be divisible by 1
                return False

        return True

    import unittest
    class PrimesTestCase(unittest.TestCase):
        """Tests for `is_number_prime`."""

        # your tests go here!

    unittest.main()

Mocking Out Functions
---------------------

Mocking is a technique often used in unit tests. Sometimes your code will do
something which requires a response from another piece of code or another
computer. An example is an HTTP request to an API or a webpage. You don't want
your code to fail its tests if the server isn't turned on for testing.

Mocking is complicated. Use it carefully. You don't want to mock out too much
code, otherwise you might mock out the functionality you're trying to test!


Teardown and Setup
------------------

Often you will need to perform an action before or after every test is run.
This is often called **setup** and **teardown**. One example is an program
which interacts with a database. Maybe one test deletes an object from the
database and the next test checks that that object can be updated. Clearly the
object should be reloaded into the database in the setup phase of running the
tests.

Automated Testing
-----------------

Automated testing generally takes form in Continuous Integration,
which automatically runs tests when someone submits changes to code to
ensure the changes work properly.

Two common CI systems:

* Travis CI
* Jenkins

Travis CI
---------

Integrates into Github, allowing your tests to be run each time you push code.

.. figure:: /static/travis.png
    :align: center

Activity
--------

Go to:

https://github.com/DevOpsBootcamp/Bootcamp-Exercises/blob/master/testing
