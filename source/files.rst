.. _files:


Lesson 5: Files
===============

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/files.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/files.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What a file is.
    - Everything is a file (!?)
    - Investigating files
    - Working with files
    - File permissions


About Files
-----------

*Everything in Linux is a file... except the things that aren't.*

.. ifnotslides::

    Although we use files every day we don't usually think about what makes
    them tic.  Most files we think about are just strings of bits that your OS
    reads from and writes to a hard drive; things like documents, music,
    spreadsheets, images, movies, etc.  Files in Linux can be a variety of
    other things like processes, system information, users -- pretty much
    everything is represented as a file in Linux.

    Since files can **be** so many things, what can we say is the **definition
    of a file**?  We can start by thinking about it's properties.

Files have:

- Owners
- Permissions
- An inode
- Size
- Filename

::

    $ ls -il
    total 8
    2884381 drwxrwxr-x 5 test test 4096 Nov  6 11:46 Documents
    2629156 -rw-rw-r-- 1 test test    0 Nov 13 14:09 file.txt
    2884382 drwxrwxr-x 2 test test 4096 Nov  6 13:22 Pictures


Everything is a file!?
----------------------

Yes. Except the things that aren't..

.. ifnotslides::

    Unix and Linux systems represent everything from data, processes, memory,
    sockets, etc as a file.

    This abstraction allows programmers to use the ``open`` ``read`` ``write``
    and ``close`` function calls to do everything from networking to printing.

    What does that mean exactly?  Well let's say you're programming an
    iterface for a medical device that **streams** data from a sensor.  In
    Linux you can write the to look something like this:

.. code:: cpp

    int read_medical_device_data(int device_file_pointer) {
        // Open a connection to the device
        int * stream = open(device_file_pointer);
        // Write the stream of data to the screen
        write(STDOUT, stream);
        // Do some other stuff with that data
        // Close the data stream
        close(stream);

        return EXIT_SUCCESS;
    }

.. ifnotslides::

    This is a *very* simplified version of how this program would look, but
    not by much.  The principles are still the same: you can interface with a
    device just like you would interface with a file.  By taking a file pointer
    (location of the file on disk) one can ``open``, ``read``, ``write``, and
    ``close`` the 'device' just like a text file.

    This is much nicer than having to interface with each type of device in
    it's own special way.  The end user experience might be the same either
    way, but the programmer's life is much easier when everything looks like a
    file.


File Extensions
---------------

    ``.jpg``, ``.txt``, ``.py``

Not necessary, more of a recommendation.

.. ifnotslides::

    Most of the time a file has enough metadata that the OS is able to figure
    out what type of file it is.  Unlike some operating systems, Linux does not
    require (and doesn't care about) a file's extension.

::

    $ file $FILENAME # tells you about the filetype

    $ file some_text_file
    file.txt: ASCII text

    $ file squirrel
    squirrel.jpg: JPEG image data, JFIF standard 1.01


Hidden Files
------------

Any file starting with ``.`` is called a **hidden file** and is not listed by
default.

.. ifnotslides::

    Hidden files are a way of only showing users the files they care about.

    **For instance:** I probably want to see my ``Documents`` folder all the
    time so I am reminded of it's existence, but a ``.cache`` folder or a
    ``.embarassing_diary_entry.txt`` should go unseen most of the time.

Adding the ``-a`` flag to ``ls`` command includes hidden files in your output.

::

    $ ls
    Documents  file.txt  Pictures
    $ ls -a
    .  ..  .hidden_file  Documents  file.txt  Pictures

.. ifnotslides::

    .. note::

        The ``.`` and ``..`` at the beginning of that ``ls -a`` output are
        file representations of the current working directory (``.``) and the
        parent directory (``..``).



Finding Metadata with 'ls -l'
-----------------------------


.. ifnotslides::

    Metadata is the information **about** a file.  The easiest way to get
    important information about files is by running ``ls -l``. This shows you
    the size, ownership bits, owner user, owner group, and date of
    modification of a file.

::

    $ ls -l
    drwxrwxr-x 5 test test 4096 Nov  6 11:46 Documents
    -rw-rw-r-- 1 test test    0 Nov 13 14:09 file.txt
    drwxrwxr-x 2 test test 4096 Nov  6 13:22 Pictures

======================================= =======================================
type: ``d``                             user permissions: ``rwx``
group permissions: ``rwx``              world permissions: ``r-x``
references permissions: ``5``           user: ``test``
size: ``4096``                          date: ``Nov  6:46``
filename: ``Documents``
======================================= =======================================


Editing Metadata
----------------

.. ifnotslides::

    You can edit the metadata of a file by running the ``chown``, ``chmod``,
    or ``chgrp`` commands to edit the owner, the read/write/execute, and the
    group permissions respectively.

::

    $ chown root myfile
      # Change the owner of myfile to "root".

    $ chown root:staff myfile
      # Change the owner of myfile to "root" and group to "staff".

    $ chown -hR root /mydir
      # Change the owner of /mydir and subfiles to "root".

    $ chgrp -R devops /home/$yourusername/bootcamp
      # Make the group devops own the bootcamp dir


``chmod`` and Octal Permissions
-------------------------------

::

    +-----+--------+-------+
    | rwx | Binary | Octal |
    +-----+--------+-------+
    | --- | 000    | 0     |
    | --x | 001    | 1     |
    | -w- | 010    | 2     |
    | -wx | 011    | 3     |
    | r-- | 100    | 4     |
    | r-x | 101    | 5     |
    | rw- | 110    | 6     |
    | rwx | 111    | 7     |
    +-----+--------+-------+

.. nextslide::

-  -, +, = for remove, add, set
-  r, w, x for read, write, execute
-  u, g, o for user, group, other

.. ifnotslides::

    Example:

    ::

        $ chmod ug+x my_script.sh    # sets a script as executable for the user
                                     # and group.
        $ chmod o-w myfile.txt       # Removes the write permissions from a
                                     # file for the world.

::

    $ chmod o-rw    # Stops all non owners from reading and writing the file.


Types of Files
--------------

::

    drwxrwxr-x      5 test    test      4096    Nov  6 11:46 Documents
    -rw-rw-r--      1 test    test         0    Nov 13 14:09 file.txt
    drwxrwxr-x      2 test    test      4096    Nov  6 13:22 Pictures
    ----------     -------  -------  -------- ------------ -------------
        |             |        |         |         |             |
        |             |        |         |         |         File Name
        |             |        |         |         +---  Modification Time
        |             |        |         +-------------   Size (in bytes)
        |             |        +-----------------------        Group
        |             +--------------------------------        Owner
        +----------------------------------------------   File Permissions

- ``-`` is a normal file
- ``d`` is a directory
- ``b`` is a block device
- ``l`` is a symlink

TODO: Messing with Files
------------------------

::

    $ touch foo # create empty file called foo

- Create an empty file in ``/home/$yourusername/bootcamp``.
- Who can do what to the file?
- Change the group to ``devops``.
- Make a file called ``allperms`` and give user, group, and world ``+rwx``.
- Make more files and practice changing their permissions.

.. ifnotslides::

    Answer Key

    ::

        $ touch ~/bootcamp
        $ ls -alh bootcamp
        $ chown $USER:devops  # You may need to create the devops group.
        $ touch ~/allperms
        $ chmod ugo+rwx allperms
        ...


Further Reading
---------------

.. TODO: Add Further Reading
