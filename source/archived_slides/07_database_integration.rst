Lesson 7: Databases
===================

Filesystems Review Questions
----------------------------

- What might happen to a busy ext2 volume on power loss?
- ext3?
- ext4?

.. note::
    * ext2 may not be consistent upon restart
    * ext3 and ext 4 are not
    * but consistency only guarantees metadata is intact

    * What might happen to a busy ext2 volume on power loss?
    * ext3?
    * ext4?

But what about our poor data?
-----------------------------

- Possibly gone, like the wind
- Or worse: Half completed writes!
- **General purpose operating systems, by design, don't understand structured
  data**

Enter the Database
------------------

  A database system's fundamental goal is to provide consistent views of
  structured data using the tools the operating system makes available.

  Chief among them is *fsync(2)*

.. note::
  fsync instructs the operating system to flush all writes to disk before
  returning

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

.. figure:: static/inner-outer-join-venn.jpg
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

Managing MySQL
--------------

.. code-block:: bash

    # Make sure service is running
    $ sudo service mysqld status
    # Ping the database
    $ mysqladmin -u root -p ping
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

    mysql> CREATE USER 'vagrant'@'localhost'
           IDENTIFIED BY 'password';

    mysql> GRANT ALL PRIVILEGES ON nobel.*
           TO 'vagrant'@'localhost'
           WITH GRANT OPTION;

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
       yr = 1960 and subject='medicine';

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

    INSERT VALUES
       ('2013','Literature','Herta Müller')
    INTO
       nobel;

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

    INSERT VALUES ('2009', 'Peace', 'Barack Obama'),
    ('2009', 'Economics', 'Elinor Ostrom and Oliver E. Williamson')
    INTO nobel;

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

Practice
--------

 - Brigid Tenenbaum Medicine prize in 1952

DELETE
------

.. code-block:: sql

    DELETE FROM
       nobel
    WHERE
       yr = 1989, subject = peace;

.. note::
  peace prizes can be controversial, and perhaps there's a political interest in
  censoring our database?

Further Reading, Resources, etc.
--------------------------------

- Codd, E.F. (1970). "A Relational Model of Data for Large Shared Data Banks".
  Communications of the ACM 13 (6): 377–387.
- sqlzoo.net
- CS 275: Databases (Justin Wolford taught my class)

Hands-On: Make a Database
-------------------------

* Create a new database

.. code-block:: sql

    mysql> create database systemview

    mysql> GRANT ALL PRIVILEGES ON systemview.*
           TO 'vagrant'@'localhost'
           WITH GRANT OPTION;


* Grant a user privileges on your new database

.. note::
  challenge them to do this based on the material in the last hour, maybe also
  demo the mysql console. Make sure everyone remembers the username and password
  for the next step.

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

.. code-block:: python

    for subject, yr, winner in session.query(Nobel).filter_by(yr=1960):
        print "%s winner in %s: %s " % (subject, yr, winner)

Much easier to read and understand, but requires some setting up first.

.. note::
  Of course we actually have to do a lot of setup work - setting up the model,
  engine, session, etc - but you do that once and can interact with the database
  as much as you want, without worrying about the cursor or connection. Note
  that we have no SQL in this statement, it is pythonic and has pythonic
  methods. The database table is now an object.

Setting Up the Magic - SqlAlchemy
---------------------------------

SqlAlchemy - a popular Python ORM, frequently used in Flask apps (like
SystemView!)

To use it, we'll need to:

* Import sqlalchemy
* Create a "model" - a representation of our data in code
* Create an "engine" and connect it to the database
* Create a session to store the model instances and transactions

.. note::

  :Model:
    A object with all the properties, attributes, etc of our data, can also
    include code to manipulate that data in order to represent a specific view
    (i.e. automatically returning sorted results). It's just a python class,
    instances are just python objects.
  :Engine:
    This handles the authentication with the database, it's like the
    MySQLdb.connect above.
  :Session:
    An in-memory record of your changes to objects - all the orm objects you
    instantiate live int he session, and are only saved to the database when you
    say so.

How SQLAlchemy is used in Systemview:
-------------------------------------

* Open up `systemview.py`
* Notice on line 25 where we import flask.ext.sqlalchemy -- this is the flask module for working with SQLAchemy
* Next, look at line 45 where we tell it which database to use.  Notice that it looks suspiciously like a URL...
    * Note: You don't have to memorize this syntax -- just know that a database is being created!
* Other notable lines include line 48, line 59, and lines 114 - 129

What's a model? What's an Object?
---------------------------------

* You might notice on line 53 that we pass 'db.Model' to our search function.

* Instead of describing the fields in a database's table using a schema, we can use a model.

* For those of you familiar with Object Oriented Programming, a model is a class which the ORM can
  turn into a database field.
