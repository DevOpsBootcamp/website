.. _frameworks:


Lesson 10: Frameworks
=====================

========= =====================================================================
Homepage  http://devopsbootcamp.osuosl.org
Content   FILL THIS IN
Slides    FILL THIS IN
Video     FILL THIS IN
========= =====================================================================

.. include:: unfinished.txt


.. ifslides::

    Overview
    --------

    - What a framework is.
    - Types of frameworks.
    - Examples of frameworks.
    - Anatomy of a web-framework

      - Model View Controller
      - URL Routing
      - Templating Engine

.. ifnotslides::

    .. contents:: Overview


Frameworks
----------

.. ifnotslides::

    Frameworks are collections of classes, functions, and constants designed
    to make completing a tast easier. Examples include:

- Web-development frameworks.
- Game-development frameworks.

.. ifnotslides::

    Frameworks dictate a specific look to an application and limit the design
    choices a developer can make in favor of making the code easier to read
    and write.


The job of a framework
~~~~~~~~~~~~~~~~~~~~~~

    *To take care of the boring stuff.*

.. ifnotslides::

    Frameworks are meant to make the life of a developer easier by supplying
    programmers with tools and design patters to accomplish a task in an
    expressive and relatively simple way.

    Frameworks simplify a program by doing implementing tedious parts of a
    program to let the programmer focus on the "Big Picture" and "Application
    Specific Needs".

    Frameworks tend to exist for commonly developed types of applications to
    reduce the amount of time spent on repeated development steps like
    recieving HTTP requests or drawing sprites to a screen.


Why and When to use a Framework
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use a framework if you are making a *cookie cutter* application.

.. ifnotslides::

    Applications which lend themselves to frameworks are those which have been
    developed many times over.  Web applications are a good example: There are
    hundreds of thousands of web applications, if each one had to reinvent the
    wheel in how they dealt with web requests and rendered HTML pages, the
    industry as a whole would be wasting a lot of time.

If a framework exists for what you're doing, consider using it.


Types of Frameworks
~~~~~~~~~~~~~~~~~~~

- Testing Frameworks
- Web-app Frameworks
- Game Frameworks

.. ifnotslides::

    Things to keep in mind when looking for a framwork:

    - There are many frameworks in the world, some are better than others so
      do your research.
    - Just because a framework does what you want make sure there isn't a
      *better tool for the job*.
    - Most popular languages have at least two or three frameworks for common
      applicatiosn (listed above), so figure out which those are and which one
      looks best:

        - Has a good community.
        - Is well documented.
        - gives you the freedom/lack of freedom you're looking for.


Web Frameworks
--------------

.. ifnotslides::

    We're going to focus on web frameworks because they are easy to
    demonstrate and usually very polished.


Static vs Dynamic Sites
~~~~~~~~~~~~~~~~~~~~~~~

There are two types of websites: Static and Dynamic.

.. ifnotslides::

    A static site delivers the same content to anybody visiting.

    A dynamic site customizes the page based on who is visiting. A socal
    network or search engine is a good example of this.  Web Frameworks are
    primarily used in dynamic sites and rarely in static sites.

Static Site
    Rarely changes, looks the same for all visitors (Blog, News, Document)

Dynamic Site
    Changes based on who you are and what you do. (Search Engine, Login)


Popular Web Frameworks
~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Each language has a slew of web framewoks to choose from.  We will cover
    common frameworks for popular programming languages including Python,
    Ruby, and NodeJS.

Python
    `Django`_
        Offers many feature out of the box: Admin page, easy database
        management, simple templating, convenient URL routing. Well documented
        too.

    `Flask`_
        Sparsely featured, offers very little out of the box and lets you
        build *up* the features you need.  Well supported with community
        libraries and add-ons.

.. nextslide::

Ruby
    `Rails`_
        Arguably the most popular web-framework out there.  Similar to Django
        in it's features out of the box.

    `Sinatra`_
        Analogous to Flask on the Python side, very simple and easy to start
        with, encourages building *up* the features you need.

Node.js
    `ExpressJS`_
        A bare-bones NodeJS application, similar again to Flask.

.. _Django: https://www.djangoproject.com/
.. _Flask: http://flask.pocoo.org/
.. _Rails: http://rubyonrails.org/
.. _Sinatra: http://www.sinatrarb.com/
.. _ExpressJS: http://expressjs.com/


Note: Model, View, Controller
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /static/mvc.png
    :target: https://commons.wikimedia.org/wiki/File:MVC-Process.svg
    :alt: model view controller diagram
    :align: center

.. ifnotslides::

    Most webapps consist of three components:

    Model
        The data represented in someway, usually a database.

    View
        What the user sees, the webpage you look at.

    Controller
        The code that manipulates the data in the database.

    Each of these components is a seperate component.  Some apps make each of
    these very seperate while others blur the line between what code is
    controlling the view, the model, and the controller.

    For now understanding the MVC architecture isn't that important, but it is
    something to be aware of.  Most web frameworks are built around the MVC
    model, so it is easier to develop MVC apps over others.


URL Routing
~~~~~~~~~~~

.. ifnotslides::

    A core component in every web-framework is URL routing.

    This is where you tell a framework what to do when a user goes to a web
    address.

::

    app.route('/delete', delete_account)

.. ifnotslides::

    In the above pseudocode the ``'/delete'`` endpoint causes the application
    to call the ``delete_account`` method.  In a seperate section of the code,
    the routes functions are defined:

::

    def delete_account():
        if username was passed in the query parameters
            and password was passed in the query parameters
            and the user is in the database
            and passed password is correct

            database.remove_user(username)
            return success
        else
            return failure


Templating Engines (mad-libs!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Templating engines are the "Views" part of the MVC architecture.  They
    take a string, or file, with places for variables and stick the specific
    values in.

    For instance:

::

    data = {"animal": "Cat", "number": 5}
    template.render("You have {{ number }} {{ animal}}s! That's crazy.", data)

.. ifnotslides::

    Produces a string that looks like:

::

    You have 5 cats! That's crazy.


TODO: Dynamic Website
~~~~~~~~~~~~~~~~~~~~~

Read the documentation on `Flask`_, a simple Python Web-Framework and build a
simple "Display the Time in each Timezone" Application.

When a user goes to our website they will see the server's time and when they
go to ``app-url/<timezone code>`` they will see the timezone in that area of
the world.( http://flask.pocoo.org )

.. _Flask: http://flask.pocoo.org/

.. ifnotslides::

    First we are going to create a Python virtual environment and install the
    flask framework.

    ::

        $ mkdir webapp
        $ virtualenv venv
        $ source venv/bin/activate
        (venv)$ pip install flask

    Then we are going to edit a file called ``main.py`` which contains the
    following code:

    ::

        #!/bin/env python
        from flask import Flask
        app = Flask(__name__)

        @app.route("/")
        def hello():
            return "The app works!"

        if __name__ == "__main__":
            app.run()

.. TODO: Complete this activity to include url routing and templating engine.

Further Reading
---------------

.. TODO: Add further reading
