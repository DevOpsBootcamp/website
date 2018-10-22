.. _files:

Lesson 6: Files
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


What are files?
----------------

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

============= ==========================

Owner         atime, ctime, mtime
Group         POSIX ACLs
Permissions   Spinlock
Inode         i_ino
Size          read, write and link count
Filename

============= ==========================

.. code-block:: console

    $ ls -il
    total 8
    2884381 drwxrwxr-x 5 test test 4096 Nov  6 11:46 Documents
    2629156 -rw-rw-r-- 1 test test    0 Nov 13 14:09 file.txt
    2884382 drwxrwxr-x 2 test test 4096 Nov  6 13:22 Pictures

Everything is a file?
---------------------

Yes. Except the things that aren't...

.. ifnotslides::

    The basic understanding of a file is "Some chunk of data stored on your
    hard drive/solid state drive/floppy disk/etc."  However, the concept of
    files can be extended to include more than just data.  Unix and Linux
    systems represent nearly everything -- data, processes, storage devices,
    sockets, and more -- as files.

    By representing everything as files, Linux provides a consistent interface
    to easily access all kinds of things.  This abstraction allows users to
    interact with data, software, and hardware alike by reading from and
    writing to files.

    For example, you might change your screen's brightness by running this
    command:

    .. code-block:: console

      $ echo 5 > /sys/class/backlight/acpi_video0/brightness

This functionality isn't just limited to the shell!  Let's say you're
programming an interface for a device that **streams** data from a sensor.
Using the *"Everything is a file"* philosophy, we could read data from the
device like so:

.. code-block:: c

    int read_device_data(int device_file_pointer) {
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
    its own special way.  The end user experience might be the same, but the
    programmer's life is much easier when everything looks like a file.

More file metadata
------------------

.. rst-class:: codeblock-sm

.. code-block:: console

  $ ls -l
  crw-rw-rw- 1 root  tty   5, 0 Jan  6 13:45 /dev/tty
  brw-rw---- 1 root  disk  8, 0 Dec 21 14:12 /dev/sda
  srw-rw-rw- 1 root  root  0    Dec 21 14:13 /var/run/acpid.socket
  prw------- 1 lance lance 0    Jan  5 17:44 /var/run/screen/S-lance/12138.ramereth
  lrwxrwxrwx 1 root  root  4    Nov 25 09:26 /var/run -> /run

  $ stat /etc/services
    File: `/etc/services'
    Size: 19303       Blocks: 40         IO Block: 4096   regular file
  Device: fc00h/64512d  Inode: 525111      Links: 1
  Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
  Access: 2015-01-07 08:22:43.768316048 -0800
  Modify: 2012-05-03 09:01:30.934310452 -0700
  Change: 2012-05-03 09:01:30.982310456 -0700
   Birth: -

File Extensions
---------------

``.jpg``, ``.txt``, ``.py``

Not necessary, more of a recommendation.

File contains information about its encoding

.. ifnotslides::

    Most of the time a file contains enough metadata (information about its
    contents) that the OS is able to figure out what type of file it is.
    Unlike some operating systems, Linux does not require (and doesn't care
    about) a file's extension.  Also unlike *some* operating systems, most
    Linux desktop environments will open an unrecognized file in a text editor
    as plaintext.

    The ``file`` command takes a filename and uses its metadata and its
    contents to try and guess at what kind of file it is.

.. code-block:: console

    $ ls
    some_text_file  squirrel

    $ file some_text_file
    some_text_file: ASCII text

    $ file squirrel
    squirrel: JPEG image data, JFIF standard 1.01


Hidden Files
------------

Any file starting with ``.`` is called a **hidden file** and is not listed by
default.

.. ifnotslides::

    Hidden files are a way of only showing users the files they care about.

    **For instance:** I probably want to see my ``Documents`` folder all the
    time so I am reminded of it's existence, but a ``.cache`` folder or a
    ``.embarassing_diary_entry.txt`` should go unseen most of the time.

    Many programs use files that begin with ``.`` to store configuration
    options. These configuration files are aptly called "dotfiles".

Adding the ``-a`` flag to ``ls`` command includes hidden files in your output.

.. code-block:: console

    $ ls
    Documents  file.txt  Pictures

    $ ls -a
    .  ..  Documents  file.txt  .hidden_file  Pictures  .vimrc

.. ifnotslides::

    .. note::

        The ``.`` and ``..`` at the beginning of that ``ls -a`` output are
        file representations of the current working directory (``.``) and the
        parent directory (``..``).


Finding Metadata with ``ls -l``
-------------------------------


.. ifnotslides::

    Metadata is the information **about** a file.  The easiest way to get the
    most important information about files is by running ``ls -l``. This shows
    you metadata such as the file type, file permissions, references count (Number of
    files that point to the same data; hardlinks), file owner, file size, and
    the date and time the file was last modified.

::

    $ ls -l
    drwxrwxr-x   5   test     test     4096   Nov  6 11:46 Documents
    -rw-rw-r--   1   test     test        0   Nov 13 14:09 file.txt
    drwxrwxr-x   2   test     test     4096   Nov  6 13:22 Pictures
    ----------   -   ----     ----     ----   ------------ --------------
        |        |    |        |         |         |             |
        |        |    |        |         |         |        File Name
        |        |    |        |         |         +--- Modification Time
        |        |    |        |         +-------------  Size (in bytes)
        |        |    |        +-----------------------       Group
        |        |    +--------------------------------       Owner
        |        +-------------------------------------  References Count
        +----------------------------------------------  File Permissions
                                                             & Type


Editing Metadata
----------------

You can edit the metadata of a file with various commands, but some of the most useful commands are ``chown``,
``chmod``, and ``chgrp`` commands.  These commands allow you to edit the owner, the read/write/execute, and the group
permissions of a file respectively.

.. code-block:: console

  # Change the owner of myfile to "root".
  $ chown root myfile

  # Change the owner of myfile to "root" and group to "staff".
  $ chown root:staff myfile

  # Change the owner of /mydir and subfiles to "root".
  $ chown -hR root /mydir

  # Make the group devops own the bootcamp dir
  $ chgrp -R devops /home/$yourusername/bootcamp

.. ifnotslides::

    .. warning::

        Use these commands with caution. You can really mess things up with a
        ``sudo chmod -R 777 /``. See "Permission Mishaps" at the bottom of the
        page to learn more about common mistakes such as these and avoid making
        them yourself, but a good rule of thumb is to avoid large recursive
        edits unless you're *really* confident that you know what you're doing.

chmod and Octal Permissions
---------------------------

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

-  u, g, o for user, group, other
-  -, +, = for remove, add, set
-  r, w, x for read, write, execute

.. nextslide::

Example:

.. code-block:: console

  $ chmod ug+x my_script.sh    # Adds the permission to execute the file
                               # to its owner user and owner group.

  $ chmod o-w myfile.txt       # Removes the permission to write to the
                               # file from users other than its owners.

Executing a File?
-----------------

.. ifslides::

    When a file has the ``+x`` permission set, it can be run as a program.

.. ifnotslides::

    When a file has the ``+x`` bit set it means you can invoke this as if it
    were a program.

For instance:

.. code-block:: console

    $ ls -alh my-script
    -r-xr-xr-x 1 username username 1.9K Sep 27 09:44 my-script

    $ cat my-script
    #!/bin/bash
    # The above line tells Linux how to invoke the script on my behalf.
    echo 'This is a script being run without using bash!'

    $ ./my-script  # my-script is invoked just like a compiled binary!
    This is a script being run without using bash!


Types of Files
--------------

- ``-`` is a normal file
- ``d`` is a directory
- ``b`` is a block device
- ``l`` is a symlink

.. ifnotslides::

    Linux has all kinds of special file types, but these are the most common
    ones that you'll encounter.

Directories
-----------

*Directories are also files!*

- ``+r`` allows you to read the contents of the directory.
- ``+w`` allows you to add files to the directory.
- ``+x`` allows you to use the directory at all.

.. code-block:: console

  $ ls -alh | grep foobarbaz
  drw-rw-rw-  2 voigte   voigte   4.0K Sep 29 10:47 foobarbaz

  # Below is the literal output, not psuedo-output
  $ ls -alh foobarbaz
  ls: cannot access foobarbaz/.: Permission denied
  ls: cannot access foobarbaz/..: Permission denied
  total 0
  d????????? ? ? ? ?            ? .
  d????????? ? ? ? ?            ? ..

Exercise: Messing with Files
----------------------------

.. code-block:: console

  # create empty file called foo
  $ touch foo

- Create an empty file in ``/home/dobc/bootcamp``.
- Who can do what to the file?
- Change the group to ``devops``.
- Make a file called ``allperms`` and give user, group, and world ``+rwx``.
- Make more files and practice changing their permissions.

Exercise Answer Key
-------------------

.. rst-class:: build

.. code-block:: console

  $ touch bootcamp/emptyfile
  $ ls -alh bootcamp/emptyfile
  -rw-rw-r-- 1 dobc dobc 0 Nov  3 22:38 bootcamp/emptyfile
  # You may need to create the devops group.
  $ sudo chown dobc:devops bootcamp/emptyfile
  # Alternatively, you can also do the following
  $ sudo chgrp devops bootcamp/emptyfile
  $ touch allperms
  $ chmod ugo+rwx allperms
  $ ls -l allperms
  -rwxrwxrwx 1 dobc dobc 0 Nov  3 22:39 allperms

.. rst-class:: build

**Bonus: What's another way of giving a file all permissions?**

Further Reading
---------------

* `Permission Mishaps`_
* `Access the Linux kernel using the /proc filesytem`_

Next: :ref:`packages_software_libraries`

.. _Permission Mishaps: http://serverfault.com/questions/93752/linux-permission-when-things-go-wrong-mishaps-gotchas-for-newbies/93759
.. _Access the Linux kernel using the /proc filesytem: http://www.ibm.com/developerworks/library/l-proc/index.html
