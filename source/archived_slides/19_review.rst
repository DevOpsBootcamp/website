Spring Term Review
==================

Hello From Portland!
--------------------

As you are no doubt aware, we are giving this talk via Google Hangouts in
Portland. This week we are attending a conference on writing technical
documentation, a crucial skill you'll learn more about in Technical Writing
class, WR 327.

.. figure:: /static/portland.jpg
	:align: center
	:scale: 20%

What We Covered
---------------

* Configuration management
* Continuous integration
* Web application frameworks
* Testing and development
* Docker

Configuration Management
------------------------

* Automation of many of the mundane tasks that are necessary for maintaining a
  system (such as updating your software).
* Centralized so that the team can work together.
* Standardization, using the same tools to do the same tasks across a large
  system or organization.
* History via source control management (like Github).

CM Platforms
------------

Today there are four major players:

* CFEngine
* Puppet
* Chef
* Ansible

.. nextslide::

**CFengine**

* Lightweight agent system. Manages configuration of a large number of computers
  using the client–server paradigm or stand-alone.

**Puppet**

* Puppet consists of a custom declarative language to describe system
  configuration, distributed using the client–server paradigm.

.. nextslide::

**Chef**

- Chef is a configuration management tool written in Ruby, and uses a pure Ruby
  DSL for writing configuration "recipes". Also a client-server model.

**Ansible**

- Combines multi-node deployment, ad-hoc task execution, and configuration
  management in one package. Utilizes SSH with little to no remote agents.


What Configuration Management Includes
--------------------------------------

* System-wide settings
    * sshd, ntp, ldap, etc.
* Group settings
    * Web, email, database
* Standardize settings globally
* Easy to troubleshoot

CM Platform Comparison
----------------------

* CFEngine scales like mad, not very agile
* Puppet

  - Uses a list of dependencies and figures out what order to run it in
  - The Puppet DSL can become a blocker and a problem, puppet also has scaling
    issues

* Chef

  - Executes commands and scripts as they are listed with minimal amount of
    dependencies
  - Using ruby offers both its advantages and disadvantages

* Each platform offers its own level of complexity


Continuous Integration
----------------------

Development goes like this:

1. Write code & new tests.
2. Run tests.
3. If tests pass and you're ready to release, package your code.
4. ``goto 1``


.. nextslide::

However,

* Running tests is boring.
* Packaging code is boring.
* Let's have the robots do this for us.

.. figure:: /static/robot.png
	:align: right
	:scale: 15%

.. nextslide::

Some common continuous integration tools:

* Buildbot (Python)
* Travis CI
* Drone (Uses Docker!)
* Jenkins

Buildbot
--------

* If you need to compile a browser and test it on 12 operating systems, use
  this.
* Writing arbitrary python is great because it means your tests runner can do anything!
* Your test runners are horribly complex and can break in unforeseen ways.

.. figure:: ./static/buildbot.png
  :align: center
  :width: 70%

Travis CI
---------

* Just does tests, not packaging.
* Awesome Github integration.


.. figure:: ./static/travis.png
  :align: center
  :width: 100%

Jenkins
-------

* Does anything you want.
* A big Web UI.


.. figure:: ./static/jenkins.png
  :align: center
  :width: 100%

Drone
-----

* Travis is nice, but it won't package my code for me, only builds on Ubuntu
  and only supports Github.
* Lets users pull down any old Docker image and build their code in there.

.. figure:: ./static/drone.png
  :align: center
  :width: 100%


Web Application Frameworks
--------------------------

* Framework: software providing generic functionality can be selectively
  changed by additional user-written code, thus providing application-specific
  software
* A web application framework provides many useful and universal
  functionalities so that you don't have to worry about them

* You don't have to re-invent the wheel.
* Web application frameworks have safeguards built in to prevent you from
  making security mistakes.


Popular web frameworks
----------------------

* **Python:** Django, Flask
* **Ruby:** Rails, Sinatra
* **Node.js:** Express, Koa, Hapi

.. figure:: static/flask.png
    :align: center


Order now and for no extra charge you'll get:
---------------------------------------------

* An Object Relational Mapper, which is a way of chucking objects into a
  database and getting them back out.
* Migration tools to upgrade your database schema without losing data.
* Templating engines to play mad-libs with your web pages.


Models
------

A model is a special object which the ORM knows about and can chuck into the
database.

You can't just chuck any object into the database since there needs to be a
table for each type of object.

Django example:

.. code-block:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

Each model generally corresponds to it's own table in a database.


Templating Engines
------------------
* How does facebook put your username on the page? It renders a template,
  mad-libs style, with your name as a variable.
* Different frameworks typically have different templating engines.

Jinja, typical pythonic templating engine

.. code-block:: html

    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}


Testing and development
-----------------------
Testing your software ensures that software:

* meets the requirements that guided its design and development,
* responds correctly to all kinds of inputs,
* performs its functions within an acceptable time,
* is sufficiently usable,
* can be installed and run in its intended environments, and
* achieves the general result its stakeholders desire.


Static vs. Dynamic Testing
--------------------------

* Static testing is similar to linting. It doesn't actually run your code, but
  walks through it to find inconsistencies and common errors.
* Static testing involves verification
* Dynamic testing runs your code and tests various inputs and outputs.
* Dynamic testing involves validation.

Black-box vs. White-box
-----------------------

* White box testing tests the internal structures of software.  These are
  pieces of code that the user doesn't directly interact with, but which are
  required to support the entire system.

* Black box testing treats the software as a black box. It assumes that you,
  the end user, don't actually know how the internal code works.

.. figure:: static/black-box.png
    :align: center
    :height: 300px


Types of Testing
----------------

**Unit Testing:** Verifies the functionality of a specific section of code.
This is probably the majority of test writing that you'll do, at least in
school.


**Integration Testing:** Integration testing ensures that the different
components of a software system work together properly.

**System Testing:** This is the last type of testing you'll do in building a
system.  It tests how the entire sytem works from start to finish, and verifies
that it meets all of the requirements.

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

.. nextslide::

.. code-block:: python

    import mock
    from unittest import TestCase

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


Docker
------

*What are Containers?*

* Not VMs.
* Containers are a way to put a program in an imaginary box where it thinks
  it's the only program besides the OS running on the computer.
* Containers are just the host OS lying to the program, so they don't need to
  run a second OS.
* Containers allow programs to be isolated from the host system without the
  overhead of VMs. Since VMs run a whole OS on top of an OS, they're slow.
* As a side affect, it changes the way you configure and run your applications.

Docker
------

* Docker is one of the most prominent tools which uses containers.
* It is a way of reproducibly building and running images which have all the
  necessary software to run your program.
* Each part of the application runs inside its own container
    - The database
    - The webapp
    - The caching layer (redis, rabbitmq)

Docker Terminology
------------------
- *Image*: This is just like the VM image. It is the set of files and
  directories which make up the container. Images can inherit from other images
  kind of like classes.
- *Container*: An instance of an image the same way an object is an instance
  of a class.
- *Dockerfile*: A file which describes how to build a docker image.

.. figure:: /static/docker_logo.png
	:align: center
	:scale: 25%

Pulling a Docker Image
----------------------
Many people upload their images to a website called DockerHub. You can use the
docker tool to pull down their images and run them. This is really handy
because you don't need to rewrite a lot of commonly used Docker containers like
the MySQL database container.

.. code-block:: sh

	$ docker pull mysql

Running a Docker Image
----------------------

Now that you have the docker image locally, you can run it.

.. code-block:: sh


	$ docker run -d --name my_mysql_container \
	  -e MYSQL_ROOT_PASSWORD=password \
	  mysql

Here are the what these options do:

* `-d` runs the Docker container in the background so you can do other things
  in the terminal.
* `--name` gives the new container a name. If you don't pass this flag, ddocker
  will choose a random one for you.

Running a Program in That Docker Container
------------------------------------------

You can enter the container and run arbitrary commands.
The `-it` flags make the command run interactively.

.. code-block:: sh

	$ docker exec -it my_mysql_container bash
	root@3d8dd4e19779:/# exit
	$  docker exec -it my_mysql mysql -p
	Enter password:
	mysql> SELECT * FROM table;

Dockerfiles
-----------

Docker images are built from Dockerfiles. Let's take a look at (part of) the
MySQL Dockerfile.

.. nextslide::

.. code-block:: sh

	# This indicates that Docker should use the Debian image as a base for
	# this one
	FROM debian:wheezy

	# create the mysql user and add them to the mysql group
	RUN groupadd -r mysql && useradd -r -g mysql mysql

	# Install the perl programming language with mysql requires
	RUN apt-get update && apt-get install -y perl mysql-server

	# Set some useful environment variables
	ENV MYSQL_MAJOR 5.6
	ENV MYSQL_VERSION 5.6.24

	# Expose this port to the host
	EXPOSE 3306

	# Run this command when everything is done
	CMD ["mysqld"]

.. nextslide::

* *FROM* Images inherit from parent images. This image is set up like a Debian
  Linux system.
* *RUN* This just runs a command.
* *ENV* This sets an environment variable.
* *EXPOSE* This exposes a port to the host system.
* *CMD* This is the command to run once the image starts. It is a list of
  strings.
