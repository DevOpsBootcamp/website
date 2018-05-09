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
    - HTTP
      - HTTP Methods
      - REST

.. ifnotslides::

    .. contents:: Overview


Frameworks
----------

    Frameworks are collections of classes, functions, and constants designed to
    make completing a task easier.

Types of frameworks include:

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


Looking for Frameworks
~~~~~~~~~~~~~~~~~~~~~~

Things to keep in mind when looking for a framework:

- While there are many frameworks to choose from, some are better than others.
- Just because a framework does what you want doesn't mean it's the *best
  tool for the job*.
- Most popular languages have at least two or three frameworks for common
  applications, so research which one works best for your use case. Good
  frameworks usually have:

    - Good documentation
    - Active developers
    - A helpful community


Web Frameworks
--------------

.. image:: /static/flask.png
    :target: https://flask.pocoo.org/
    :alt: The Flask logo
    :align: center

.. ifslides::

    Frameworks for building websites or APIs

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

.. image:: /static/mvc.png
    :target: https://commons.wikimedia.org/wiki/File:MVC-Process.svg
    :alt: model view controller diagram
    :align: center
    :height: 600

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


Templating Engines (mad-libs!)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Templating engines are the "Views" part of the MVC architecture.  They
    take a string, or file, with places for variables and stick the specific
    values in.

    For instance, take this template file:

.. code-block:: html+jinja

    <!DOCTYPE HTML>
    <html>

        <head>
            <title>Template Example</title>
        </head>

        <body>
            <p>Your lucky number today is {{ number }}!</p>
        </body>

    </html>

.. ifnotslides::

    This template uses the Jinja2 templating engine, which is the default
    engine for the Flask framework. To render the template, you could use
    the ``render_template`` function like so:

.. code-block:: python

    render_template("template.html", number=random.randint(0, 99))

::

    Your lucky number today is 42!

.. ifnotslides::

    If you viewed the resulting HTML file in a web browser, the body of the
    page would contain a random number between 0 and 100 that was generated
    in the Python code and inserted into the template.

.. nextslide::

.. ifnotslides::

    With templating engines, you can do more sophisticated things than simple
    string replacement. For example:

.. code-block:: html+jinja

    ...
    <body>
    {% for message in messages %}
        <p>{{ message }}</p>
    {% endfor %}
    </body>
    ...

.. code-block:: python

    messages = ["Welcome!", "Test Message", "Vim > Emacs"]

    render_template("template2.html", messages=messages)

.. ifnotslides::

    This template evaluates just like a regular Python ``for`` loop. Jinja2
    will render each entry in ``messages`` in its own paragraph on the webpage.

::

    Welcome!
    Test Message
    Vim > Emacs

.. ifnotslides::

    There are many more such directives available. If you want to learn more
    in depth about Jinja2, check out its `documentation`_.

.. _documentation: http://jinja.pocoo.org/docs/dev/


HTTP
----

::

    GET http://web.site/page.html HTTP/1.1

    HTTP/1.1 200 OK
    Content-Type: text/html
    ...
    <!DOCTYPE HTML>
    ...

.. ifnotslides::

    Even though web frameworks provide a very high level of abstraction, it's
    vital to have at least a minimal understanding of HTTP, since HTTP
    (Hypertext Transfer Protocol) is the language of the World Wide Web. When
    you're working inside a web framework, these are the most important concepts
    to understand:

    .. list-table:: HTTP Concepts

        * - **Resource**
          - A thing that exists and is accessible using HTTP
        * - **URI**
          - A string that is used to identify the location of a resource
        * - **Request**
          - Data that is sent by the client to the server, asking the server to
            perform some action
        * - **Method**
          - The part of the request specifying the action that the client wants the
            server to perform
        * - **Response**
          - The server's response back to the client after processing the client's
            request
        * - **Error Code**
          - The part of the response summarizing the server's response to the
            request

.. ifslides::

    - **Resource**
    - **URI**
    - **Request**
    - **Method**
    - **Response**
    - **Error Code**


HTTP Methods
~~~~~~~~~~~~

.. ifnotslides::

    HTTP methods are sent with requests, and they specify the action that the
    client wishes to take on the resource specified with the request URI. For
    example, a request to the server that used the **GET** method on a resource
    indicates that the client wants the server to respond with that resource.
    Then the client might send a **PUT** request to update that same resource
    or a **DELETE** request to delete it.

    The most commonly used methods are **GET**, **POST**, **PUT**, and
    **DELETE**, but there are many others.

    .. list-table:: HTTP Methods

        * - **GET**
          - Retrieves a resource from the server
        * - **POST**
          - Create a new resource on the server
        * - **PUT**
          - Update a resource on the server
        * - **DELETE**
          - Delete a resource from the server
        * - **OPTIONS**
          - Get a list of methods that are allowed on a resource
        * - **PATCH**
          - Update (Patch) only one specific part of a resource

.. ifslides::

    - **GET**
    - **POST**
    - **PUT**
    - **DELETE**
    - **OPTIONS**
    - **PATCH**


REST
~~~~

.. ifnotslides::

    REST (Representational State Transfer) is a web architecture that takes
    advantage of HTTP's features by defining a set of rules for how servers
    handle client requests and format their responses. There are many of these
    rules, but the most important are:

- Servers are stateless

.. ifnotslides::

    In this context, the word "state" means "the way that the thing currently
    is". If a server is stateless, then the way that it handles requests
    doesn't change based on previous requests that have been made.

    It can be a bit of a subtle distinction, since storing data and retreiving
    stored data is a common function that web apps perform. However, in that
    case, the web server isn't the component that's storing the data from the
    previous request. The web server stores and retrieves data by talking to a
    database, so the server retains its statelessness.

- Resources are self-contained

.. ifnotslides::

    A self-contained resource is a resource that can be fully parsed and
    updated by the client without requiring any external informtaion. For
    example, a resource might contain some metadata to inform the client that
    it's encoded in JSON, or it might contain other URLs that the client can
    use to interact with the resource further.

- HTTP methods have predictable side-effects

.. ifnotslides::

    This one is fairly self-explanitory. GET requests don't change anything on
    the server's side, DELETE requests delete the requested resource, etc.
    The GET method is called *nullipotent* (no side effects), and the PUT and
    DELETE methods are called *idempotent* (no side effects if the request is
    repeated more than once).

TODO: Dynamic Website
---------------------

.. ifnotslides::

    Over the course of this exercise, you're going to build upon the skeleton
    of a simple web app written using the `Flask`_ microframework. When it's
    finished, our app will be a guestbook that stores data inside a SQLite
    database (More on databases in our `Databases`_ lesson) and allows people
    to both add themselves and view the guests that have already been added.

    To get started, clone the `Bootcamp-Exercises`_ repository in the DevOps
    Bootcamp Github organization, and ``cd`` into the ``2016-2017/frameworks``
    directory. Follow the directions in ``README.md`` to set up and run the app.
    If you don't have ``virtualenv`` installed already, you can install it from
    your distro's package manager (It's usually ``python-virtualenv``). If
    everything goes smoothly, you should get output that looks something like
    this after ``python run.py``:

    ::

        (venv)$ python run.py
         * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
         * Restarting with stat
         * Debugger is active!
         * Debugger pin code: 861-918-611

    You can now access the website in a web browser at
    ``http://localhost:8080``.

.. _Databases: databases.html
.. _Bootcamp-Exercises: https://github.com/DevOpsBootcamp/Bootcamp-Exercises/

.. ifslides::

    ::

        $ git clone https://github.com/DevOpsBootcamp/Bootcamp-Exercises
        $ cd Bootcamp-Exercises/2016-2017/frameworks
        $ virtualenv venv
        $ source venv/bin/activate
        (venv)$ pip install --upgrade pip
        (venv)$ pip install -r requirements.txt
        (venv)$ python run.py
         * Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
        ...

    Go to

    ``http://cloud.devopsbootcamp.osuosl.org:<your_port_number>``

Part One: Writing The Views
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    If you poke around the website as it is, you'll quickly notice that things
    are broken. That's because we haven't added functionality to the website
    yet!

    There are two views that we have to write: The view for adding guests
    (``app/views/add_guest.py``), and the view for looking at the guests that
    have already been added (``app/views/view_guests.py``). See the files for
    more information on how to complete this exercise. If you get stuck, you
    should consult the `Flask documentation`_ for help.

.. ifslides::

    ::

        app/views/add_guest.py
        app/views/view_guests.py

    Adding a guest to the database:

    .. code-block:: python

        guest = Guest(name, message)
        db.session.add(guest)
        db.session.commit()

    Getting a list of guests from the database:

    .. code-block:: python

        guests = Guest.query.all()

.. _Flask documentation: http://flask.pocoo.org/docs/0.12/


Part Two: Writing The Templates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Now that we've written the logic for each endpoint, it's time to fill out
    the templates so that we can present our dynamic data to the user. It
    might be helpful to consult the `Jinja2 documentation`_ and the
    `Flask-WTForms documentation`_ here.

    Just like before, there are two templates that we have to complete: The
    template for the ``add_guests`` view and the template for the
    ``view_guests`` view. The ``add_guests`` template is going to contain the
    form to add a guest (Hint: Use the HTML <form> tag), and the
    ``view_guests`` template is going to contain the list of guests in the
    database (Hint: Use the HTML <table> tag).

.. ifslides::

    ::

        app/templates/add_guest.html
        app/templates/view_guests.html

    Using a form inside a template:

    .. code-block:: html+jinja

        <form method="POST">
            {{ form.csrf_token }}
            {# Put form fields here #}
            <p><input type="submit" value="Submit"></p>
        </form>

    Jinja2 ``for`` loop:

    .. code-block:: html+jinja

        {% for item in list %}
            {# do thing with item #}
        {% endfor %}

.. _Jinja2 documentation: http://jinja.pocoo.org/docs/dev/
.. _Flask-WTForms documentation: https://flask-wtf.readthedocs.io/en/stable/


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
