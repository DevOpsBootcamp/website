==================================================
Lesson 7: A data base with a clever soup pun (TBD)
==================================================


.. note:: more dev-focused
    2/6/2014

Review Questions About Filesystems
---------------------------------------

.. rst-class:: build

- What might happen to a busy ext2 volume on power loss?
- ext3?
- ext4?

.. note:: ext2 may not be consistent upon restart 
    * ext3 and ext 4 are not
    * but consistency only guarentees metadata is intact

    * What might happen to a busy ext2 volume on power loss?
    * ext3?
    * ext4?

But what about our poor data?
-----------------------------

.. rst-class:: build

- Possibly gone, like the wind

- Or worse: Half completed writes!

- **General purpose operating systems, by design, don't understand structured data**

Enter the Database
==================
 
  A database system's fundamental goal is to provide consistent views of structured
  data using the tools the operating system makes available.
  
  Chief among them is *fsync(2)*

.. note:: fsync instructs the operating system to flush all writes to disk before returning

Structure
=========

  Relational Algebra
  - Tables
  - Rows, Columns
  - Relations form a structure between tables

Joins
-----
 * Venn diagrams of join types

.. note:: join are the principle use of relations.

Installing MySQL
================

- yum install mysql-server
- /usr/bin/mysql_secure_installation

Managing MySQL
--------------
- /sbin/service mysqld start
- mysqladmin ping
- mysqladmin create nobel


Users & Permissions
-------------------
- sudo mysql
- mysql> CREATE USER 'vagrant'@'localhost' IDENTIFIED BY 'password';
- mysql> GRANT ALL PRIVILEGES ON nobel.* TO 'vagrant'@'localhost' WITH GRANT OPTION;

Importing Data
--------------

- wget http://osl.io/nobel -O nobel.sql
- mysql nobel < nobel.sql
- mysql nobel
- mysql> DESCRIBE nobel;

Basic Queries
=============

4 basic operations on data:
- SELECT
- INSERT
- UPDATE
- DELETE

SELECT
------
SELECT 
   yr, subject, winner
FROM 
   nobel
WHERE 
   yr = 1960;

Practice
--------

Who won the prize for Medicine in 1952?


INSERT
------
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
UPDATE 
   nobel
SET 
   winner='Andrew Ryan'
WHERE 
   subject='Peace' AND yr='1951';

.. note:: obviously Andrew Ryan deserves the peace price for his work 
          in the Rapture planned community

Practice
--------

 - Brigid Tenenbaum Medicine prize in 1952

DELETE
------

DELETE FROM 
   nobel 
WHERE 
   yr = 1989, subject = peace;

.. note:: peace prizes can be contraversial, and perhaps there's a political interest in censoring our database?

Further Reading, Resources, etc.
--------------------------------

  * Codd, E.F. (1970). "A Relational Model of Data for Large Shared Data Banks". Communications of the ACM 13 (6): 377–387.
  * sqlzoo.net
  * CS 440: Database Management Systems



Parking lot
===========
- indicies, performance)
- connect app to DB

