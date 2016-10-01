.. _databases:


Lesson 14: Databases
====================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/databases.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/databases.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

        - About Databases.
        - When to use Databases.
        - When *not* to use Databases.
        - Database Concepts.
        - SQL Syntax.
        - Ways to use a Datbase.


Databases
---------

.. ifnotslides::

    Databases are collections of data, usually organized under a schema, and
    stored in a format which is efficient for storing and retrieving the data.

    When people talk about databases they tend to talk about the underlying
    Database Management System (DBMS).  These are programs like MySQL or PostgreSQL
    which are designed to complete the tasks of storing, retrieving, updating,
    caching, deleting, and other data manipulation.

    Databases are another big topic we won't be able to to justice.  For as
    long as computers have been able to store notable amounts of data,
    databases have been used to catalog everyhing from our personal
    and banking information, to movies and which `types of glue are best for a
    job`_.

.. _types of glue are best for a job: http://www.thistothat.com/


Relating Data
~~~~~~~~~~~~~

    Imagine a kitchen cupboard program that stores food currently in stock,
    where it is, recipes using it, expiration dates, etc.

.. ifslides::

    - Everything has a **relationship** with everything else.  How would you
      store it in the program?

        - Ingredients for recipes.
        - Location.
        - Classifications.

.. ifnotslides::

    All of this data relates to one-another:
        - Recipes have ingredients (foods, spices, etc)
        - Everything has a location (fridge, cupboard, shelving, etc)
        - Foods have a status (full, half-empty, etc)
        - Ingredients have types (vegetable, spice, fruit, meat, gluten free,
          kosher etc)

    Imagine this data is stored in files on a hard drive.
        - Is it stored by food name? If so, how can we select only items that are
          expiring soon?
        - Is it stored by type? Location?


Databases and Structure
~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    A database system’s fundamental goal is to provide consistent views of
    structured data, just like the relationships we’ve laid out between all of
    this food.

Structure
    SQL databases are based on around Relational Algebra

.. ifnotslides::

    - **Tables** are the way we look at our data.
    - **Columns** are **fields** in the table.
    - **Rows** define a relation between **fields**.
    - A **Primary key** is a set of columns that **uniquely** identify rows in
      a table.
    - A **Foreign key** is a column that matches the **primary key** of
      another table.

::

    <Table 1>
    +---------------+-----------+-----------+
    | <Primary key> | <Field 1> | <Field 2> |
    +---------------+-----------+-----------+
    | 1             | value     | value`    |
    | ...           | ...       | ...       |
    +---------------+-----------+-----------+

    <Table 2>
    +---------------+-----------+--------------------------+
    | <Primary key> | <Field 1> | <Foreign key to Table 1> |
    +---------------+-----------+--------------------------+
    | 1             | val       | 7                        |
    | ...           | ...       | ...                      |
    +---------------+-----------+--------------------------+


Concept: Relational Algebra
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /static/inner-outer-join-venn.jpg
    :align: center
    :alt: Relational Algebra Example

.. ifnotslides::

    Databases are designed under the mathematical principles of Relational
    Algebra (and relational calculus).  This area of mathematics focuses on
    how best to relate data to one another, and how to craft queries to
    discover the relationship between your data.  Most database queries have
    an equivalent Relational Algebra statement.  If you like math and
    databases, this would be a good subject to learn about!


When to use a Database
----------------------

    *When you have to work with a lot of well structured data*.

Databases are useful for two situations:
    #. Lots of data.
    #. High throughput.

.. ifnotslides::

    Some DBMS are optimal for specific situations.  For instance SQLite is good
    for small databases since it stores data in a file on disk.  MySQL is good for
    large projects, but can be a pain to setup and manage.


Lots of Data
~~~~~~~~~~~~

.. ifnotslides::

    Databases are very good at efficiently storing large amounts of data.
    Whether you are storing a simple kitchen app or a whole social network,
    databases are very good at storing, retrieving, updating, and deleting
    data.

    The catch is that your data must be *well structured* by a schema.  You
    can't just dump data into a database, the data must first be defined in a
    *schema* and inserted to fit in that schema.  That is almost always a
    worth-while tradeoff when dealing with *big data*.


Concurrent Read/Writes
~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Because databases have to deal with *lots* of data and work with it very
    fast they are usually able to optimize their operations, concurretly read
    and write to disk, and buffer their operations so they waste as few CPU
    cycles as possible.

    This is good when tens or hundreds of people are logging in, checking
    their data, logging hours, etc.  Everybody can use the same pool of data
    and *rarely* (if ever) have data collide or get lost.


When *not* to use a Database
----------------------------

.. ifnotslides::

    Databases are appealing, but if you're application may not need them.

    If you rarely read and write data to disk there are other options:
        - Storing data in files.
        - Storing data in memory.
        - Storing data with a remote service.


Types of Databases
------------------

There are two broad types of databases.

- **SQL:** Stores data in tables organized by column and field.
- **NoSQL:** Stores data differently than an SQL database.
- **NewSQL:** A middle-ground between SQL and NoSQL

SQL
~~~

.. ifnotslides::

    SQL databases are the *classic* database, and are what we default to
    talking about when we teach databases.

    SQL Databases are interfaced with SQL Queries (more on that later) and
    require a great deal of structure.  SQL databases are not known for their
    flexibility and require a lot of forethought before being created.  That
    said they tend to be very fast and are standardized in the industry.

Examples:
    - MySQL/MariaDB
    - PostgreSQL
    - SQLite


NoSQL
~~~~~

.. ifnotslides::

    SQL databases are very prevelant, but at the end of the day a company or
    developer needs to weigh their tools against their needs and sometimes an
    SQL database doesn't do it, or is just overkill.

    In cases like these a NoSQL database can be used to store you database in
    different / more flexible ways.

    NoSQL databases can also offer more flexibilty in storage options,
    allowing one to spread data across many machines more easily than SQL
    databases tend to do.

Examples:
    - MongoDB
    - Apache Casandra
    - Dynamo
    - Redis


Database Concepts
-----------------

.. ifnotslides::

    We've touched on a few concepts already, but now we're going to dive
    directly into some (SQL) Database concepts.


Schemas
~~~~~~~

.. ifnotslides::

    Schemas are how you define what a table looks like, what data will
    populate it, and what each field will be called.  The schema also defines
    relationships between tables; more or less the blueprint of your database.

.. code-block:: sql

    CREATE TABLE nobel (
        id int(11)
            NOT NULL
            AUTO_INCREMENT,
        yr int(11),
        subject varchar(15),
        winner varchar(50)
    )
    ENGINE = InnoDB;


Migrations
~~~~~~~~~~

.. ifnotslides::

    Migrations are the process of updating tables and fields in your database.
    Since databases *might* need to change in the future (you never know!) you
    can create and run a migrations to modify your schema as needed.

    This process will move (migrate) your data from one schema in the database
    to another inline, so you don't need to turn your database off, or restart
    from scratch, to change your schema.


Raw SQL Syntax
--------------

.. ifnotslides::

    There are many tools out there that allow you to *avoid* writing raw SQL,
    but it's always good to know the syntax.  One day you may need to write
    raw SQL queries, and at the very least you'll need to *read* SQL for
    debugging purposes.


SELECT
~~~~~~

.. ifnotslides::

    Select statements **get** data from the database which matches the
    requirements you have.

Example:

.. code-block:: sql

    SELECT
        yr, subject, winner
    FROM
        nobel
    WHERE
        yr = 1960 AND subject='medicine';


INSERT
~~~~~~

.. ifnotslides::

    Insert statements create an entry into a table and populate the fields
    appropriately.

Example:

.. code-block:: sql

    INSERT INTO
        nobel
    VALUES
        ('2013','Literature','Herta Müller');


UPDATE
~~~~~~

.. ifnotslides::

    Update statements modify an existing entry in a table.

Example:

.. code-block:: sql

    UPDATE
        nobel
    SET
        winner='Andrew Ryan'
    WHERE
        subject='Peace' AND yr='1951';


DELETE
~~~~~~

.. ifnotslides::

    Delete statements... you can guess what a delete statement does I bet.

Example:

.. code-block:: sql

    DELETE FROM
       nobel
    WHERE
       yr = 1989 AND subject = 'peace';


TODO: Crafting Queries!
-----------------------

Craft a query to get the following data out of our Nobel table:

- Who won the prize for Medicine in 1952?
- How many people were awarded the 1903 Nobel in Physics?
- How many prizes were awarded to Linus Pauling?
- How many people have won more than once? (Difficult)

Don't worry about getting it exactly right!  Craft pseudo-SQL!

Answers
~~~~~~~

.. code-block:: sql

    SELECT winner FROM nobel
    WHERE yr=1952 AND subject='medicine'; #(Selman A. Wksman)

    SELECT * FROM nobel
    WHERE yr=1903 AND subject='physics'; #(3)

    SELECT * FROM nobel
    WHERE winner='Linus Pauling'; #(2)

    SELECT COUNT(*) FROM nobel
    AS n0 INNER JOIN nobel AS n1 on n0.winner=n1.winner
    AND (n0.yr!=n1.1 or n0.subject!=n1.subject); #(16)


TODO: Using a *Real* Database
-----------------------------

.. ifnotslides::

    Now that we have belabored the *theory* of databases and SQL, lets actually
    start *doing* work with databases.

    Throughout this exercise we will


Installing MySQL
~~~~~~~~~~~~~~~~

.. ifnotslides::

    To start we're going to install and setup MySQL.  We're not going to get
    too fancy with our setup, just install and run it locally on our Linux
    boxes.

::

    # Install mysql -- hit 'enter' to name your user root, and then enter
    # again for password
    $ sudo yum install mysql-server

    $ sudo service mysqld start # Start the service

    $ mysql_secure_installation # Use this to set the root password

    # There is no current password
    # Hit 'yes' or 'y' for all options
    # Add a sensible password which you will remember
    # DO NOT MAKE IT YOUR USUAL PASSWORD.

    $ sudo service mysqld status # Make sure service is running

    $ mysqladmin -u root -p ping # Ping the database

    $ mysqladmin -u root -p create nobel # Create a table for Nobel prizes


Configuration
~~~~~~~~~~~~~

.. ifnotslides::

    Configuration files are something we haven't touched on in this course all
    that much.  They are files read by a specific program to tell it how to
    behave.  You will get more experience with these as you use Linux more.

#. Open and edit ``/etc/my.cnf``.
#. Add ``default_storage_engine = InnoDB`` to your file.

.. ifnotslides::

    The only change we really want to make on to our MySQL configuration file
    is to edit the ``default_storage_engine`` option.

    InnoDB offers a lot of great features the default Database Engine does not:

    - crash recovery
    - caching
    - foreign keys


Users
~~~~~

.. ifnotslides::

    Just like on a linux system, there are users for a database.  Each of
    user has various levels of access.

Login to the mysql shell with your ``root`` user credentials:

::

    $ sudo mysql -p

::

    mysql> CREATE USER 'me'@'localhost'
           IDENTIFIED BY 'password';

    mysql> GRANT ALL PRIVILEGES ON nobel.*
           TO 'me'@'localhost'
           WITH GRANT OPTION;

    mysql> exit


Importing Data
~~~~~~~~~~~~~~

::

    # Get the database from the osl server
    $ wget http://osl.io/nobel -O nobel.sql
    # put the database in a file called nobel.sql
    $ sudo mysql -p nobel < nobel.sql
    # Open up mysql shell to execute queries
    $ sudo mysql -p nobel


.. code-block:: sql

    # List all the tables
    SHOW TABLES;
    # Print the layout of the database to the screen
    DESCRIBE nobel;


Ways to Use a Database
----------------------

.. ifnotslides::

    Now that you have a working database you have a few options for how you
    want to use it.


Raw Queries
~~~~~~~~~~~

.. ifnotslides::

    We've already done this in the previous exercise.  You use your choice of
    program to interact with the database exclusively via SQL and run the
    queries you want.  This is rarely the way to go and isn't very useful for
    most applications.  The SQL language is only good for doing database
    *stuff*.


Native Queries
~~~~~~~~~~~~~~

.. ifnotslides::

    Native Queries are a *better* method of interacting with databases.  Your
    programming language of choice takes a SQL query as a string, runs that
    query on your behalf through a language-native database connection, and
    parses the response as a language-native data-type.

.. code-block:: python

    #!/usr/bin/python
    import MySQLdb

    db = ("localhost","testuser","test123","nobel" )

    cursor = db.cursor()

    cursor.execute("SELECT subject, yr, winner FROM nobel WHERE yr = 1960")

    data = cursor.fetchall()

    for winner in data:
        print "%s winner in %s: %s " % (winner[0], winner[1], winner[2])

    db.close()


Object Relational Mappers
~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Object Relational Mappers (ORMs) is a library which allows you to write in
    a native programming language to interface with a database.  So instead of
    crafting SQL queries you express in your native langauge what you want the
    database to do.  This means you don't write *any* SQL, the programming
    langauge handles those specifics for you.

    The real benefit of an ORM is that you can use any database backend you
    want and the ORM will compile your native code into a query for that
    database.

    As an example you can write all of your queries for your database.  In
    testing you use an in-memory SQLite database (very fast) and in production
    you use a PostgreSQL database.  Testing with a Postgres database is a pain
    to setup, but you probably wouldn't want to run SQLite in production.

- Maps an Object in an application to a database table or relationship.
- Talks SQL to the database, your favorite language to you.
- Lets you point to different databases with the same syntax.
- Intelligently manages transactions to the database.

.. code-block:: python

    # SELECT * FROM nobel WHERE yr = 1960
    for subject, yr, winner in session.query(Nobel).filter_by(yr=1960):
        print "%s winner in %s: %s " % (subject, yr, winner)

TODO: Use an ORM
----------------

.. TODO: Add activity
.. Something using SQLAlchemy
.. Probably create some skeleton code to avoid problems with setup.

Further Reading
---------------

CS 340
    The CS 340 course at OSU (titled "Databases") is a great introduction to
    this topic.  If you have the option to take it you should!

.. TODO: Add further reading
