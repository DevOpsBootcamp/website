Testing and Development
=======================

Why write tests?
----------------

Testing your software ensures that it:

* meets the requirements that guided its design and development,
* responds correctly to all kinds of inputs,
* performs its functions within an acceptable time,
* is sufficiently usable,
* can be installed and run in its intended environments, and
* achieves the general result its stakeholders desire.

.. figure:: static/qaengineer.png
    :align: center
    :height: 100px

Static vs. Dynamic Testing
--------------------------

* Static testing is similar to linting.  It doesn't actually run your code, but walks through it to find inconsistencies and common errors.
* Static testing involves verification
* Dynamic testing runs your code and tests various inputs and outputs.
* Dynamic testing involves validation.

Black-box vs. White-box
-----------------------

* White box testing tests the internal structures of software.  These are pieces of code that the user doesn't directly interact with, but which are required to support the entire system.
* Black box testing treats the software as a black box. It assumes that you, the end user, don't actually know how the internal code works.

.. figure:: static/black-box.png
    :align: center
    :height: 300px

Testing Levels
--------------

* Unit Testing
* Integration Testing
* System Testing

There are many more!

Unit Testing
------------

Verifies the functionality of a specific section of code.  This is probably the majority of test writing that you'll do, at least in school.

.. figure:: static/unit-test.jpg
    :align: center

Integration Testing
-------------------

Integration testing ensures that the different components of a
software system work together properly.

.. figure:: static/integration-testing.jpg
    :align: center

.. note:: For example, if you're designing an email client then sending mail and receiving mail are probably handled by different components of the system.  You would build and unit-test each component first, then use integration testing to make sure that they work together.

System Testing
--------------

This is the last type of testing you'll do in building a system.
It tests how the entire sytem works from start to finish, and verifies
that it meets all of the requirements.

.. figure:: static/system-testing.png
    :align: center


Testing Frameworks
------------------

Frameworks are libraries which make testing easier. Generally they
will have a template for writing a test, and then tests will be run
with just one command. Like all frameworks, they mostly just make your
life easier.

The python standard library has the ``unittest`` framework built in.

Example using ``unittest``
--------------------------

Code being tested:

.. code-block:: python

    def is_all_numbers(response):
        return all(map(unicode.isdigit, map(unicode, response))):

Test case:

.. code-block:: python

    from unittest import TestCase

    class TestDigitDestroyer(TestCase):

        def test_classify(self):
            match_message = ['1', '2', '3', '1', '1']
            miss_message = ['a', '100']
            self.assertTrue(is_all_numbers(match_message))
            self.assertFalse(is_all_numbers(miss_message))



Mocking Out Functions
---------------------

Mocking is a technique often used in unit tests. Sometimes your code will do
something which requires a response from another piece of code or another
computer. An example is an HTTP request to an API or a webpage. You don't want
your code to fail its tests if the server isn't turned on for testing.

Mocking is complicated. Use it carefully. You don't want to mock out too much
code, otherwise you might mock out the functionality you're trying to test!

An Example of Mocking
---------------------

This function gets the title of the first open issue on a repository.  What
happens if someone opens a new issue?

.. code-block:: python

	import requests
	import json

	def get_open_issue_title(repository_name):
		result = requests.get(
			"https://api.github.com/repos/{}/issues?state=open".format(
				repository_name
			)
		)
		first_issue_title = result.json()[0]['title']
		return first_issue_title

	import mock
	from unittest import TestCase

.. nextslide::

.. code-block:: python

	class TestOpenIssueGetter(TestCase):

		@mock.patch('requests.get')
		def test_get_open_issue_title(self, requests_get):
			get_resp =  [{'title': 'Subscript formatting'}]
			expected_resp =  "Subscript formatting"
			mocked_response = mock.Mock()
			requests_get.return_value = mocked_response
			mocked_response.json.return_value = get_resp
			resp = get_open_issue_title('vmg/redcarpet')
			self.assertEqual(expected_resp, resp)
		import requests
		import json

		def get_open_issue_title(repository_name):
			result = requests.get(
				"https://api.github.com/repos/%s/issues?state=open".format(
					repository_name
				)
			)
			first_issue_title = result.json()[0]["title"]
			return first_issue_title

Tear Down This Wall!
--------------------

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
ensure that it works with the system.
