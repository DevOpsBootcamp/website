Lesson 7: Databases
===================

Filesystems Review Questions
----------------------------

.. rst-class:: build

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

.. rst-class:: build

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

    $ yum install mysql-server
    $ /sbin/service mysqld start
    $ /usr/bin/mysql_secure_installation

Managing MySQL
--------------

.. code-block:: bash

    $ /sbin/service mysqld status
    $ mysqladmin -p ping
    $ mysqladmin -p create nobel

Configuration
-------------

.. rst-class:: build

- ``/etc/my.conf``
- The most important MySQL tuning rule: 

   - almost always prefer **InnoDB**
 
.. note:: 
    we're going to add: 
    ``default_storage_engine         = InnoDB``

Users & Permissions
-------------------

.. code-block:: bash

    $ sudo mysql -p

.. code-block:: sql

    mysql> CREATE USER 'vagrant'@'localhost' 
           IDENTIFIED BY 'password';

    mysql> GRANT ALL PRIVILEGES ON nobel.* 
           TO 'vagrant'@'localhost' 
           WITH GRANT OPTION;

Importing Data
--------------

.. code-block:: bash

    $ wget http://osl.io/nobel -O nobel.sql
    $ mysql -p nobel < nobel.sql
    $ mysql -p nobel

.. code-block:: sql

    SHOW TABLES;
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

.. code-block:: sql

    SELECT 
       yr, subject, winner
    FROM 
       nobel
    WHERE 
       yr = 1960;

Practice
--------

* Who won the prize for Medicine in 1952?
* How many people were awarded the 1903 Nobel in Physics?
* How many prizes were awarded to Linus Pauling?
* How many people have won more than once? (Difficult)

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
- CS 440: Database Management Systems

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

    cursor.execute("SELECT subject, yr, winner FROM nobel WHERE yr = 1960)

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
SystemView!).

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

Let's Databasify Systemview
---------------------------

Project:

- Store search terms, then provide them as links on the search page, so you can
  just click the most common terms you search for.

What else? Ideas?

.. note::
  Solicit ideas for another column or two, maybe number of times the term is
  used (easy incrementing example), or number of results from the least search.

Hands On
--------

* Install the following packages:

.. code-block:: bash

      sudo yum install python-devel
      sudo yum install mysql-devel

* Check out systemview from GitHub (if you don't have it already)

.. code-block:: bash

      git clone git@github.com:DevOpsBootcamp/systemview

Hands On (Cont...)
------------------

* Switch to 'save-search' branch

.. code-block:: bash

      git checkout -tb save-search origin/save-search

* Activate your virtualenv

.. code-block:: bash

      source <path to virtualenv>/bin/activate

* Install the requirements

.. code-block:: bash

      pip install -r requirements.txt

.. note::

  Talk about git branches again, explain tracking, git pull for people who
  already have it cloned, etc. Talk about the virtualenv, have people create a
  new one if they have lost the one they made last time. Talk about pip and what
  requirements.txt is all about - point out how easy it is to set up an app this
  way. Make sure requirements.txt contains sqlalchemy.

  **DANGER!** - people will need mysql-dev package! name varies by distribution,
  for centos it is libmysqlclient-dev

Goals
-----

* Connect the app to your new database
* Add a new column
* Save data to that column whenever someone searches
* Fetch the data from that column and display it on the search page
* challenge: limit the returned result to only 5 terms

http://docs.sqlalchemy.org/en/rel_0_9/orm/tutorial.html

.. note::
  The code in the repo should have a simple model with one column, 'term', you
  can make a ``models.py``, or just put it all in one file. If you separate
  them, talk about MVC. The code should start an sqlalchemy engine and session,
  save the search term normalized (lowercased, stripped), the column should be
  set to unique. Make sure the code handles the case of the term already
  existing in the database (when you add a count, increment the count when the
  term exists).  You should probably initialize the db directly in the code,
  otherwise you'll have to open up a python console, import the app and run the
  db update.
