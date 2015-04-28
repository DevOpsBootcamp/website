An Introduction to Web Frameworks
=================================

Static vs. Dynamic Websites
---------------------------

* We've covered the difference between static and dynamic things before. What's the difference between a static site and a dynamic site?

.. figure:: static/dynamic-or-static-website.jpg
    :align: center

What is a Web Application Framework?
------------------------------------

* Framework: software providing generic functionality can be selectively changed by additional user-written code, thus providing application-specific software
* A web application framework provides many useful and universal functionalities so that you don't have to worry about them

.. figure:: static/rabbit_banner.jpg
    :align: center
    :width: 60%

Why use a WAF?
--------------

* It saves you a lot of writing and hassle
* You don't have to re-invent the wheel

.. figure:: static/reinvent-wheel.jpg
    :align: center

Popular web frameworks
----------------------

Python:

1. Django: High-level web framework, lots of features.
2. Flask: Lightweight and easy to set up.

.. figure:: static/flask.png
    :align: center

.. nextslide::

Ruby:

1. Rails:
2. Sinatra: Sinatra is to Ruby as Flask is to Python.

.. nextslide::

Node.js:

1. Express: Sweet, simple, relies heavily on third-party middleware to get the
   basics done.
2. Koa: Clean, small, and uses bleeding edge javascript features. Widely viewed
   as the successor to Express
3. Hapi: Web pages are configuration, not code.

.. nextslide::

Java:

1. Swing

PHP:

1. CakePHP

Model View Controller Architecture
----------------------------------

* The Model: How the data is stored and organized, notifies the  view when it is updated
* The View: The user interface, or how the data is displayed.  Gets information from the model
* The Controller: Updates the model's state based on events in the view

.. figure:: static/mvc.png
    :align: center
    :height: 300px

URL Routing
-----------

Frameworks are able to interpret and translate URLs from human-readable
strings into URLs based on how the pages are indexed.  For instance,
"/page.cgi?cat=science&topic=physics" can become "/page/science/physics"
which is easier for humans to read, write, and remember, and is 
also easier for search engines to index. 

.. figure:: static/route662.jpg
    :align: center
    :height: 300px

Object Relational Mappers (ORMs)
--------------------------------

* Most web application frameworks make it easy to work with an ORM, and talk to a database. 
* Some frameworks, like Django, have their own ORMs, while others such as Flask allow you to use discreet ORMs such as SQLAlchemy

Models
------

A model can be thought of as an object; it's a collection of 
information that contains fields and behavior of the data you're 
storing.  Because this is Python, it's basically a class.

Django example:

.. code-block:: python

    from django.db import models

    class Person(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)

Each model generally corresponds to it's own table in a database.

Who likes mad-libs?
-------------------

.. code-block:: text

	"_____________! he said ________ as he jumped into his convertible
	  exclamation            adverb
	______ and drove off with his __________ wife."
	 noun                          adjective

Templating Engines
------------------
* How does facebook put your username on the page? It renders a template,
  mad-libs style, with your name as a variable.
* Different frameworks typically have different templating engines.

.. nextslide::

Jinja, typical pythonic templating engine

.. code-block:: html

    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}

.. nextslide::

Liquid is the templating engine used by Jekyll

.. code-block:: html

    {% for post in site.posts limit: 3 %}
          <li>
          <h3><a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a></h3>
          <span class="post-meta">{{ post.date | date: "%m.%e.%Y" }}</span><br>
          {% if post.fromurl %}
          <span class="post-meta">From: <a href="{{ post.fromurl }}">{{ post.from }}</a></span>
          {% else %}

Other Common Engines
--------------------

* Embedded Ruby, a standard format for embedding arbitrary ruby into any file.
  It's similar to PHP, and can be used for other non-html files as well. Remember Chef
  templates?
* Jade, no html in sight.

Enter Migrations
----------------
* At some point you're probably going to wish you had a database backing your
  webapp.
* Sometimes you'll want to change the layout of the columns in the database.
  Maybe you have a new feature so you want to add a new column.
* However, if the database is running in production you can't just drop it and
  start over.
* Migrations move your data from the old database schema to the new one.
  Migrations can be 'rolled back', or undone like pressing Ctrl-Z.
* Every time you change a model, change the migrations.

Demo
====
