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
        - Ways to use a Database.


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
    databases have been used to catalog everything from our personal
    and banking information, to movies and which `types of glue are best for a
    job`_.

.. ifslides::

    A program that can efficiently store and retrieve large amounts of data.

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
    structured data, just like the relationships we've laid out between all of
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

::

    <Table 1>
    +------------------+------------------+
    | <Name>           | <Major>          |
    +------------------+------------------+
    | Linus Torvalds   | Computer Science |
    | Richard Stallman | Computer Science |
    +------------------+------------------+
    <Table 2>
    +------------------+--------------+----------------+
    | <Major>          | <School>     | <Advisor Name> |
    +------------------+--------------+----------------+
    | Computer Science | Engineering  | Dennis Ritchie |
    +------------------+--------------+----------------+
    <Table 1> JOIN <Table 2>
    +------------------+------------------+-------------+----------------+
    | <Name>           | <Major>          | <School>    | <Advisor Name> |
    +------------------+------------------+-------------+----------------+
    | Linus Torvalds   | Computer Science | Engineering | Dennis Ritchie |
    | Richard Stallman | Computer Science | Engineering | Dennis Ritchie |
    +------------------+------------------+-------------+----------------+

.. nextslide::

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

.. image:: /static/monthly-internet-traffic.png
    :align: center
    :scale: 50%
    :alt: Global Internet traffic by year

*Note: 1 PB = 1,000,000 GB*

.. ifnotslides::

    A significant portion of this data probably never touches a database (For
    example, static file uploads/downloads), but the Internet handles a *lot*
    of data.

    Databases are very good at efficiently storing large amounts of data.
    Whether you are storing a simple kitchen app or a whole social network,
    databases are very good at storing, retrieving, updating, and deleting
    data.

    The catch is that your data must be *well structured* by a schema.  You
    can't just dump data into a database, the data must first be defined in a
    *schema* and inserted to fit in that schema.  That is almost always a
    worth-while trade-off when dealing with *big data*.


Concurrent Read/Writes
~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Because databases have to deal with *lots* of data and work with it very
    fast they are usually able to optimize their operations, concurrently read
    and write to disk, and buffer their operations so they waste as few CPU
    cycles as possible.

    This is good when tens or hundreds of people are logging in, checking
    their data, logging hours, etc.  Everybody can use the same pool of data
    and *rarely* (if ever) have data collide or get lost.

    In order to quantify how well a database engine handles the demands of a
    concurrent world, it is assessed by the properties of **ACID**:

Atomicity:
  Either the entire transaction succeeds or it fails completely
Consistency:
  Transactions always leave the database in a valid state
Isolation:
  Concurrent operations look like they took place sequentially
Durability:
  Transactions are permanent after they're committed

When *not* to use a Database
----------------------------

.. ifnotslides::

    Databases have many appealing features, but your application may not need
    them. In some situations databases can be overkill or introduce attack
    vectors into your application if you don't configure and manage them
    correctly.

Databases might not be particularly useful for:
    - Storing content for a website that rarely updates
        - **Alternative**: Use a static site generator such as Pelican or Jekyll
    - Hosting large individual files
        - **Alternative**: Store the files on disk


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

    SQL databases are very prevalent, but at the end of the day a company or
    developer needs to weigh their tools against their needs and sometimes an
    SQL database doesn't do it, or is just overkill.

    In cases like these a NoSQL database can be used to store you database in
    different / more flexible ways.

    NoSQL databases can also offer more flexibility in storage options,
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

.. ifslides::

    - Schemas
    - Migrations


Schemas
~~~~~~~

Schemas are how you define what a table looks like, what data will populate it,
and what each field will be called.  The schema also defines relationships
between tables; more or less the blueprint of your database.

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

Migrations are the process of updating tables and fields in your database.
Since databases *might* need to change in the future (you never know!) you can
create and run a migrations to modify your schema as needed.

.. ifnotslides::

    This process will move (migrate) your data from one schema in the database
    to another inline, so you don't need to turn your database off, or restart
    from scratch, to change your schema.

    Migrations are either done with specialized tools or with a series of
    scripts that are sequentially applied to the database to migrate data
    one step at a time. Many popular web frameworks have built-in tools to
    create and apply database migrations.

.. code-block:: python

    from django.db import migrations, models

    class Migration(migrations.Migration):
        dependencies = [
            ('app', '0001_initial')
        ]

        operations = [
            migrations.AddField("Nobel", "topic", models.CharField(80))
        ]

Raw SQL Syntax
--------------

There are many tools out there that allow you to *avoid* writing raw SQL, but
it's always good to know the syntax.  One day you may need to write raw SQL
queries, and at the very least you'll need to *read* SQL for debugging purposes.

.. ifslides::

    - SELECT
    - INSERT
    - UPDATE
    - DELETE


SELECT
~~~~~~

Select statements **get** data from the database which matches the requirements
you have.

.. code-block:: sql

    SELECT
        yr, subject, winner
    FROM
        nobel
    WHERE
        yr = 1960 AND subject='medicine';

::

    +------+------------+-------------------------------+
    | yr   | subject    | winner                        |
    +------+------------+-------------------------------+
    | 1960 | "medicine" | "Sir Frank Macfarlane Burnet" |
    | 1960 | "medicine" | "Sir Peter Brian Medawar"     |
    +------+------------+-------------------------------+


INSERT
~~~~~~

Insert statements create an entry into a table and populate the fields
appropriately.

.. code-block:: sql

    INSERT INTO
        nobel
    VALUES
        ('2013','Literature','Herta Müller');

::

    +-----+------+--------------+----------------+
    | id  | yr   | subject      | winner         |
    +-----+------+--------------+----------------+
    | ... | ...  | ...          | ...            |
    | 873 | 2013 | "Literature" | "Herta Müller" |
    | ... | ...  | ...          | ...            |
    +-----+------+--------------+----------------+


UPDATE
~~~~~~

Update statements modify an existing entry in a table.

.. code-block:: sql

    UPDATE
        nobel
    SET
        winner='Andrew Ryan'
    WHERE
        subject='Peace' AND yr='1951';

::

    +-----+------+---------+----------------+
    | id  | yr   | subject | winner         |
    +-----+------+---------+----------------+
    | ... | ...  | ...     | ...            |
    | 120 | 1951 | "Peace" | "Andrew Ryan"  |
    | ... | ...  | ...     | ...            |
    +-----+------+---------+----------------+


DELETE
~~~~~~

Delete statements... You can guess what a delete statement does I bet.

.. code-block:: sql

    DELETE FROM
       nobel
    WHERE
       yr = 1989 AND subject = 'peace';


TODO: Crafting Queries!
-----------------------

Craft a query to get the following data out of our Nobel table:

- Who won the prize for Medicine in 1952?
- Who won the 1903 Nobel in Physics?
- Which prize(s) were awarded to Linus Pauling?
- How many people have won more than once? (Difficult)

Don't worry about getting it exactly right!  Craft pseudo-SQL!

.. Included so the answers aren't peeking from the right side of the screen
.. nextslide::

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
    AND (n0.yr!=n1.yr or n0.subject!=n1.subject); #(16)


TODO: Using a *Real* Database
-----------------------------

Now that we have belabored the *theory* of databases and SQL, lets actually
start *doing* work with databases.

Throughout this exercise we will load it up with some data and learn to interact
with it via the command line interface.

Importing Data
~~~~~~~~~~~~~~

.. code-block:: bash

    # Create a table for Nobel prizes
    $ mysqladmin -u root create nobel
    # Get the database from the osl server
    $ wget http://osl.io/nobel -O nobel.sql.gz
    # Gunzip the file and import it into the nobel db
    $ gunzip nobel.sql.gz
    $ mysql nobel < nobel.sql
    # OR do it in one step!
    $ zcat nobel.sql.gz | mysql nobel
    # Open up mysql shell to execute queries
    $ mysql nobel

.. code-block:: sql

    # List all the tables
    SHOW TABLES;
    # Print the layout of the database to the screen
    DESCRIBE nobel;

Ways to Use a Database
----------------------

Now that you have a working database you have a few options for how you want to
use it.

- Raw SQL Queries
- Native Queries
- ORMs


Raw Queries
~~~~~~~~~~~

We've already done this in the previous exercise.  You use your choice of
program to interact with the database exclusively via SQL and run the queries
you want.  This is rarely the way to go and isn't very useful for most
applications.  The SQL language is only good for doing database *stuff*.

.. code-block:: sql

    mysql> SELECT subject, yr, winner FROM nobel
           WHERE yr=1960;

::

    +------+------------+-----------------------------+
    | yr   | subject    | winner                      |
    +------+------------+-----------------------------+
    | 1960 | Chemistry  | Willard F. Libby            |
    | 1960 | Literature | Saint-John Perse            |
    | ...  | ...        | ...                         |
    +------+------------+-----------------------------+


Native Queries
~~~~~~~~~~~~~~

.. ifnotslides::

    Native Queries are a *better* method of interacting with databases.  Your
    programming language of choice takes a SQL query as a string, runs that
    query on your behalf through a language-native database connection, and
    parses the response as a language-native data-type.

See :download:`nobel.py <static/nobel.py>`

.. literalinclude:: static/nobel.py


Object Relational Mappers
~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    An Object Relational Mapper (ORM) is a library which allows you to write in
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

.. TODO: Use an ORM
.. ----------------

.. TODO: Add activity
.. Something using SQLAlchemy
.. Probably create some skeleton code to avoid problems with setup.

Further Reading
---------------

CS 340
    The CS 340 course at OSU (titled "Databases") is a great introduction to
    this topic.  If you have the option to take it you should!

.. TODO: Add further reading
