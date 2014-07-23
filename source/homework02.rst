Lesson 2: Homework
==================

#. Why is a salt used when storing encrypted passwords in ``/etc/shadow``?
#. What portion of the MD5 hash ``'$1$xxUwcovy$JfV9i7j9H/NFA3RBCrVHN.'`` is the
   salt?
#. What UID is used for the root user?
#. Where is a user's primary ("default") group defined? Specifically which file
   and which "field".
#. Add a user ``foobar`` to your system. Use ``useradd`` to add the user and to
   create their home directory containing files from ``/etc/skel``. Show the
   user's entry in ``/etc/passwd`` as well as the full ``useradd`` command
   needed.
#. Create a group ``bootcamp`` on your system.  Show the command used (not
   editing files by hand).
#. Assume the user ``foobar`` belongs to multiple groups. Add ``foobar`` to the
   ``bootcamp`` group by using a system command (not editing files by hand)
   without changing any of their other groups. Show the command used.
#. What ``chmod`` command (using octal mode) would you use to allow owner read
   and write access and group read access (and *no* other permissions!) to a
   file ``foo``? Using ``chmod`` *without* octal mode, how would you do the
   same?
#. What does it mean for a binary to be setuid?  is setuid a potential security
   risk?  Why is this important for tools such as ``passwd``?
#. You have the following ``foo`` directory

.. code-block:: bash

  drwxr-xr-x 7 lance bootcamp 4096 Mar 31 09:15 foo

..

  What ``chmod`` command can you run to ensure files created inside that directory
  will default to having ``bootcamp`` group ownership? Assume the user creating
  the files is in the ``bootcamp`` group.

