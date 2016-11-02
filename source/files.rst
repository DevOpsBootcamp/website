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
- Permissions (what different people can do with it)
- An inode (a low-level description of the file)
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

    The common understanding of a file is "Some bit of data stored on your
    hard drive/solid state drive/floppy disk/etc."  However, the concept of
    files can be extended to include more than data.  Unix and Linux systems
    represent nearly everything - data, processes, memory, sockets, and more -
    as files.

    By representing everything as a file, Linux provides a consistent interface
    to access all kinds of things.  This abstraction allows programmers to use
    the ``open``, ``read``, ``write``, and ``close`` function calls to do
    everything from networking to printing.

    What does that mean exactly?  Well let's say you're programming an
    interface for a medical device that **streams** data from a sensor.  In
    Linux that interface might look something like this:

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

    This is a *very* simplified version of how the program would look, but
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
    require (and doesn't care about) a file's extension.  Also unlike *some*
    operating systems, most Linux desktop environments will open an
    unrecognized file in a text editor as plaintext.

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
references: ``5``                       user: ``test``
group: ``test``                         size: ``4096``
last_modified: ``Nov  6:46``            filename: ``Documents``
======================================= =======================================


Editing Metadata
----------------

.. ifnotslides::

    You can edit the metadata of a file with various commands, but some of the
    most useful commands are ``chown``, ``chmod``, and ``chgrp`` commands.
    These commands allow you to edit the owner, the read/write/execute, and the
    group permissions of a file respectively.

::

    $ chown root myfile
      # Change the owner of myfile to "root".

    $ chown root:staff myfile
      # Change the owner of myfile to "root" and group to "staff".

    $ chown -hR root /mydir
      # Change the owner of /mydir and subfiles to "root".

    $ chgrp -R devops /home/$yourusername/bootcamp
      # Make the group devops own the bootcamp dir

.. ifnotslides::

    .. warning::

        Use recursive metadata editing commands with caution. You can really
        mess things up with a ``sudo chmod -R 777 /``. See "Permission Mishaps"
        at the bottom of the page to learn more about common mistakes made with
        file permissions, but a good rule of thumb is to avoid editing file
        metadata by hand as much as possible outside your home directory.


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


Executing a File?
-----------------

.. ifslides::

    When a file as the ``+x`` permission set, it can be run as a program.

.. ifnotslides::

    When a file has the ``+x`` bit set it means you can invoke this as if it
    were a program.

For instance:

::

    $ ls -alh my-script
    -r-xr-xr-x 1 username username 1.9K Sep 27 09:44 my-script
    $ cat my-script
    #!/bin/bash
    # The above line tells Linux how to invoke the script on my behalf.
    echo 'This is a script being run without using bash!'
    echo 'Heres a calendar:'
    cal
    $ ./my-script  # my-script is invoked just like a compiled binary!
    This is a script being run without using bash!
    Heres a calendar:

    .......


Types of Files
--------------

::

    drwxrwxr-x   5   test     test      4096    Nov  6 11:46 Documents
    -rw-rw-r--   1   test     test         0    Nov 13 14:09 file.txt
    drwxrwxr-x   2   test     test      4096    Nov  6 13:22 Pictures
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


Directories
-----------

*Directories are also files!*

- ``+r`` allows you to read the contents of the directory.
- ``+w`` allows you to add files to the directory.
- ``+x`` allows you to use the directory at all.

::

    $ ls -alh | grep foobarbaz
    drw-rw-rw-  2 voigte   voigte   4.0K Sep 29 10:47 foobarbaz
    $ ls -alh foobarbaz   # Below is the literal output, not psuedo-output
    ls: cannot access foobarbaz/.: Permission denied
    ls: cannot access foobarbaz/..: Permission denied
    total 0
    d????????? ? ? ? ?            ? .
    d????????? ? ? ? ?            ? ..


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

* `Permission Mishaps`_
* `Access the Linux kernel using the /proc filesytem`_

.. _Permission Mishaps: http://serverfault.com/questions/93752/linux-permission-when-things-go-wrong-mishaps-gotchas-for-newbies/93759
.. _Access the Linux kernel using the /proc filesytem: http://www.ibm.com/developerworks/library/l-proc/index.html
