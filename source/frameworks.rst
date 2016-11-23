.. _frameworks:


Lesson 10: Frameworks
=====================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/frameworks.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/frameworks.html
.. _Video:

.. include:: unfinished.txt


.. ifslides::

    Overview
    --------

    - What is a framework?
    - Types of frameworks
    - Examples of frameworks
    - Anatomy of a web framework

      - Model-View-Controller Pattern
      - HTTP and URL Routing
      - Templating Engines

.. ifnotslides::

    .. contents:: Overview


Frameworks
----------

.. ifnotslides::

    Frameworks are collections of classes, functions, and constants designed
    to make completing a task easier. Examples include:

- Web frameworks
- Game frameworks
- GUI frameworks

.. ifnotslides::

    Frameworks dictate a specific look to an application and limit the design
    choices a developer can make in favor of making the code easier to read
    and write.


The job of a framework
~~~~~~~~~~~~~~~~~~~~~~

    *To take care of the boring stuff.*

.. ifnotslides::

    Frameworks are meant to make the life of a developer easier by supplying
    programmers with tools and design patterns to accomplish a task in an
    expressive and relatively simple way.

    Frameworks simplify a program by implementing tedious parts of a to let
    the programmer focus on the "Big Picture" and "Application Specific Needs".

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

    Things to keep in mind when looking for a framework:

    - There are many frameworks in the world, some are better than others so
      do your research.
    - Just because a framework does what you want doesn't mean there isn't a
      *better tool for the job*.
    - Most popular languages have at least two or three frameworks for common
      applications (listed above), so figure out which those are and which one
      looks best. Good frameworks usually have:

        - Good documentation
        - Active developers
        - A helpful community


Web Frameworks
--------------

.. ifnotslides::

    We're going to focus on web frameworks because they are easy to
    demonstrate and used everywhere.


Static vs Dynamic Sites
~~~~~~~~~~~~~~~~~~~~~~~

There are two types of websites: Static and Dynamic.

.. ifnotslides::

    A static site delivers the same content to anybody visiting. Static sites
    can either be written in pure HTML/CSS/Javascript, or a static site
    generator can be used to write content in another markup language to be
    compiled to HTML

    A dynamic site changes as the user or users interact with it. Social
    networks and search engines are good examples of dynamic sites.  Web
    Frameworks are primarily used in dynamic sites and rarely in static sites.

Static Site
    Rarely changes, looks the same for all visitors (Blog, News, Document)

Dynamic Site
    Changes based on who you are and what you do. (Search Engine, Login)

.. ifnotslides::

    Security will be discussed further in `Lesson 13`_, but static websites
    should be used in place of dynamic ones whenever possible. Dynamic websites
    are vulnerable to a much wider variety of attacks than static websites are.

.. _Lesson 13: security.html


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
        Arguably the most popular web-framework out there. Similar to Django
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


The Model-View-Controller Pattern
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. TODO: Fix image scaling on slides

.. image:: /static/mvc.png
    :target: https://commons.wikimedia.org/wiki/File:MVC-Process.svg
    :alt: model view controller diagram
    :align: center

.. ifnotslides::

    Most webapps consist of three components:

    Model
        The data represented in some way, usually a database.

    View
        What the user sees i.e. the webpage you look at.

    Controller
        The code that manipulates the data in the database.

    Understanding the MVC architecture isn't that important at the moment, but
    it is something to be aware of.  Many popular web frameworks are built
    around the MVC pattern, so knowing how to use it to its advantages can be
    userful.


URL Routing
~~~~~~~~~~~

.. ifnotslides::

    A core component in every web framework is URL routing. This is where you
    tell a framework what to do when a user performs an action on a specific
    URL.

.. ifnotslides::

    In the below pseudocode, using DELETE on the ``'/accounts/<account_name>'``
    endpoint causes the application to call the ``delete_account`` method. For
    the purposes of this lesson, you don't need to worry too much about things
    like what the '@' syntax at the beginning of the function does or what
    DELETE is. If you want to learn more about the Flask framework or HTTP,
    check out our `Further Reading`_ section.

.. code-block:: python

    @app.route('/accounts/<account_name>', methods=['DELETE'])
    def delete_account(account_name):
        if authenticated() and authorized():
            database.remove_account(account_name)
            return 'Success', 200
        else
            return 'Failure', 401

.. TODO: Brief treatment of HTTP

Templating Engines (mad-libs!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Templating engines are the "Views" part of the MVC architecture.  They
    take a string, or file, with places for variables and stick the specific
    values in.

    For instance:

.. TODO: Use template file example

::

    data = {"animal": "cat", "number": 5}
    template.render("You have {{ number }} {{ animal }}s! That's crazy.", data)

.. ifnotslides::

    Produces a string that looks like:

::

    You have 5 cats! That's crazy.


TODO: Dynamic Website
~~~~~~~~~~~~~~~~~~~~~

.. TODO: TODO

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

Further Reading
---------------

`The Flask Microframework`_
    Flask is a web framework that is simple enough for beginners to use but
    configurable enough to allow more advanced users to have full control over
    their application. It has a very active community and fantastic
    documentation.

`Intro to HTTP and REST`_
    HTTP is the protocol that web clients and web servers use to communicate
    with each other, and REST is a set of web design guidelines that is takes
    advantage of HTTP's features and allows different applications to easily
    communicate with each other.

.. _The Flask Microframework: http://flask.pocoo.org/docs/0.11/
.. _Intro to HTTP and REST: http://blog.luisrei.com/articles/rest.html
