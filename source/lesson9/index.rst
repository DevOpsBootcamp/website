.. _databases:


Lesson 9: Databases
===================

Imagine a kitchen cupboard program that stores food currently in stock, where it
is, recipes using it, expiry dates, etc.

Relating Data
-------------

This data has relations to it.

* a recipe has many *related* foods
* a *location* (fridge, cupboard, shelving, etc)
* a status (full, half-empty, etc)
* a type (vegetable, spice, fruit, meat, etc)

How is this stored? How is it accessed?
---------------------------------------

Imagine this data is stored in files on a hard drive.

* Is it stored by food name? If so, how can we select only items that are
  expiring soon?
* Is it stored by type? Location?

Querying this is hard!

Enter the Database
------------------

  A database system's fundamental goal is to provide consistent views of
  structured data, just like the relationships we've laid out between all of
  this food.

Structure
---------

SQL databases are structured around **Relational Algebra**

- Tables
- **Columns** are fields
- **Rows** define a relation between fields
- A **Primary key** is a set of columns that uniquely identify rows in a table
- A **Foreign key** is a column that matches the primary key of another table

Relational Algebra Visualized
-----------------------------

|

.. figure:: /static/inner-outer-join-venn.jpg
    :align: center
    :scale: 150%

.. note:: joins are the principle use of relations.

Installing MySQL
----------------

.. code-block:: bash

    # Install mysql -- hit 'enter' to name your user root, and then enter again for password
    $ sudo yum install mysql-server
    # Start the service
    $ sudo service mysqld start
    # Use this to set the root password
    $ mysql_secure_installation
    # There is no current password
    # Hit 'yes' or 'y' for all options
    # Add a sensible password which you will remember
    # DO NOT MAKE IT YOUR USUAL PASSWORD.
    # 'root' and 'password' are good for this sort of thing

    # Make sure service is running
    $ sudo service mysqld status
    # Ping the database
    $ mysqladmin -u root -p ping
    # Create a table for Nobel prizes
    $ mysqladmin -u root -p create nobel


Configuration
-------------

- ``/etc/my.cnf``
- The most important MySQL tuning rule: almost always prefer **InnoDB**
- InnoDB is a Database Engine, and is wonderful because:
    - It has `crash recovery <https://dev.mysql.com/doc/refman/5.5/en/glossary.html#glos_crash_recovery>`_
    - It caches
    - Foreign keys are a thing (Apparently they aren't in MyISAM)
    - Multiple clients can write to the same database at the same time (Also apprently not in MyISAM)
    - `And more... <https://dev.mysql.com/doc/refman/5.5/en/innodb-default-se.html>`_

.. note::
    we're going to add:
    ``default_storage_engine         = InnoDB``

Users & Permissions
-------------------

.. code-block:: bash

    $ sudo mysql -p

This plops you into the mysql shell -- now you're ready to start writing SQL queries!
These will talk to our database, allowing us to put information into and get information out of it.
Next, we'll create a user vagrant and give it all privileges on the database we just made

.. code-block:: sql

    mysql> CREATE USER 'me'@'localhost'
           IDENTIFIED BY 'password';

    mysql> GRANT ALL PRIVILEGES ON nobel.*
           TO 'me'@'localhost'
           WITH GRANT OPTION;

    mysql> exit

Importing Data
--------------

.. code-block:: bash

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

Basic Queries
-------------

4 basic operations on data:

- SELECT
- INSERT
- UPDATE
- DELETE

SELECT
------
Select is used to get specific data from the database.

.. code-block:: sql

    SELECT
       yr, subject, winner
    FROM
       nobel
    WHERE
       yr = 1960 AND subject='medicine';

Practice
--------

* Who won the prize for Medicine in 1952?
* How many people were awarded the 1903 Nobel in Physics?
* How many prizes were awarded to Linus Pauling?
* How many people have won more than once? (Difficult)

Answers
-------

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

INSERT
------

.. code-block:: sql

    INSERT INTO
        nobel
    VALUES
       ('2013','Literature','Herta Müller');

.. note:: this data stops at 2008, so lets insert some 2009 awards

Practice
--------

In 2009:
 - Barack Obama won the Peace Prize
 - Elinor Ostrom and Oliver E. Williamson won the prize in Economics
 - http://en.wikipedia.org/wiki/List_of_Nobel_laureates

Answers
-------

.. code-block:: sql

    INSERT INTO nobel
    VALUES
        ('2009', 'Peace', 'Barack Obama'),
        ('2009', 'Economics', 'Elinor Ostrom and Oliver E. Williamson');

UPDATE
------

.. code-block:: sql

    UPDATE
       nobel
    SET
       winner='Andrew Ryan'
    WHERE
       subject='Peace' AND yr='1951';

.. note::
  obviously Andrew Ryan deserves the peace price for his work in the Rapture
  planned community

DELETE
------

.. code-block:: sql

    DELETE FROM
       nobel
    WHERE
       yr = 1989 AND subject = 'peace';

.. note::
  peace prizes can be controversial, and perhaps there's a political interest in
  censoring our database?

Further Reading, Resources, etc.
--------------------------------

- Codd, E.F. (1970). "A Relational Model of Data for Large Shared Data Banks".
  Communications of the ACM 13 (6): 377–387.
- sqlzoo.net
- CS 340: Databases

Describing Tables
-----------------

* A table has rows.
* Each row has a bunch of fields.
* You can think of it just like a table in a spreadsheet.
* Tables are defined using a schema.

.. code-block:: sql

    CREATE TABLE nobel (
        id int(11) NOT NULL AUTO_INCREMENT,
        yr int(11),
        subject varchar(15),
        winner varchar(50)) ENGINE = InnoDB;

Databases in Applications
-------------------------

Applications love databases.

* Application data - the information to be displayed and manipulated
* User data - complex authentication and authorization
* Logging, statistics, state and session data, etc...

.. note::

  All the various things an app might use a database for - note that the vast
  majority of web apps use them for something

Native SQL
----------

Most languages allow you to speak directly to a database

Python:

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

.. note::
  Note the plain SQL statement, recognizable from earlier. Point out the
  cumbersome nature of creating the connection, creating a cursor, sending the
  sql, getting data from the cursor (iterating over it if you want multiple
  results), etc. Similar interfaces exist for virtually all languages.

Introducing the ORM
-------------------

Object Relational Mapper

* Maps an Object in an application to a database table or relationship
* Talks SQL to the database, your favorite language to you
* Lets you point to different databases with the same syntax
* Intelligently manages transactions to the database

.. note::
  Make sure people know what you mean by "object", mention possible difference
  between Postgres, sqlite, MySql, etc. Objects may map to one table, but might
  also incorporate relationships. ORMs also often optimize queries and manage
  transactions to make database queries as efficient as possible (like all other
  magic, though, sometimes this can backfire).

Life With a Python ORM
----------------------

|

Look, ma! No SQL!

This is using the SQLAlchemy ORM.

.. code-block:: python

    # SELECT * FROM nobel WHERE yr = 1960
    for subject, yr, winner in session.query(Nobel).filter_by(yr=1960):
        print "%s winner in %s: %s " % (subject, yr, winner)

Much easier to read and understand, but requires some setting up first.

.. note::
  Of course we actually have to do a lot of setup work - setting up the model,
  engine, session, etc - but you do that once and can interact with the database
  as much as you want, without worrying about the cursor or connection. Note
  that we have no SQL in this statement, it is pythonic and has pythonic
  methods. The database table is now an object.
