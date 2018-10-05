.. _packages_software_libraries:

Lesson 7: Packages, Software, Libraries
=======================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/packages-software-libraries.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/packages-software-libraries.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - Anatomy of a Package.

      - Software
      - Libraries

    - Package manager functionality.
    - System package manager examples.
    - Language package manager examples.
    - Exercise: Install ``sl`` and group from source


Software
--------

Everything that isn't hardware.

.. ifnotslides::

    Software is what makes modern computers useful.  When you install a piece of
    software you can then invoke that program using your computer to do a
    useful task.

    Software is everything running on a computer, from web-browsers to the
    operating system itself.

- Code that is run on a Computer.
- Binaries.
- Scripts.
- Packages

Libraries
---------

.. ifnotslides::

    Libraries are pieces of code that are used by multiple programs, but which
    are not usually run on their own.

    **For Example**: Your OS might come with a "MathFunction" library for a
    given programming langauge since math is something almost every program
    ends up doing at least a little bit.

- Often used to make development easier.
- Rarely run on it's own.
- Shared code.
- Binaries are linked dynamically to libraries (kind of like DLL's in Windows)

.. code-block:: console

  $ ldd /usr/bin/nano
    linux-vdso.so.1 =>  (0x00007ffc1fdcd000)
    libncursesw.so.5 => /lib64/libncursesw.so.5 (0x00007ff2cfaee000)
    libtinfo.so.5 => /lib64/libtinfo.so.5 (0x00007ff2cf8c4000)
    libc.so.6 => /lib64/libc.so.6 (0x00007ff2cf500000)
    libdl.so.2 => /lib64/libdl.so.2 (0x00007ff2cf2fc000)
    /lib64/ld-linux-x86-64.so.2 (0x000055e46c4b4000)

Package Management
------------------

.. ifnotslides::

    Package Managers are the tool used to manage Software and Libraries
    (together called **Packages**) in your OS.  Some are very easy to use,
    some work very well, and none of them are perfect.

- Automagically manage software and libraries on your system.
- Examples:

  - Android Play Store
  - Apple App store
  - Steam
  - apt (Debian/Ubuntu)
  - yum (CentOS/Fedora/RHEL)

Package Management
------------------

  *Take care of installation and removal of software*

.. ifslides::

  * Install, Upgrade & uninstall packages easily
  * Resolve package dependencies
  * Install packages from a central repository
  * Search for information on installed packages and files
  * Pre-built binaries (usually)
  * Find out which package provides a required library or file

.. ifnotslides::

    While *all* package managers don't have *every* feature listed below, most
    of them end up accomplishing most of these tasks out of necessity.

    Install, upgrade, and uninstall packages easily.
        Below is a hypothetical package manager carrying out these operations:

        ::

            $ pkg-mgr install firefox
            Finding [firefox] on pkg-mgr servers...............................
            Downloading [firefox]..............................................
            Are you sure you want to install [firefox]? (Y/n) y
            Installing [firefox]...............................................
            Cleaning up........................................................
            $ pkg-mgr upgrade firefox
            Checking for updates to [firefox]..................................
            Packages [firefox] are up to date. Nothing to do!
            $ pkg-mgr uninstall firefox
            Are you sure you want to un-install [firefox]? (Y/n) y
            Removing [firefox].................................................
            [firefox] successfully uninstalled!

        The package manager took the name of a program you wanted, found it on
        some trusted servers, downloaded the package, and placed the
        downloaded files in the correct place.  It seems obvious but they
        weren't always around, especially not in their current form.

    Resolve package dependencies.
        Resolving dependencies is when you download all of the packages
        another package needs to run.

        #. Program ``foo`` and program ``bar`` both need library ``baz``.
        #. You install ``foo`` first.
        #. Your package manager installs ``baz``.
        #. You then install ``bar``.
        #. Your package manager checks that it already has the ``baz``
           dependency.
        #. It installs ``bar`` without installing ``baz`` again.

    Install packages from a central repository.
        Most package managers download packages from a pre-defined set of
        trusted servers.  This is for security reasons related to trust.

        Plus -- how else would it find the packages?  Google?

    Search for information on installed packages and files.
        You can usually search all packages and descriptions for a given
        string.  For instance:

        ::

            $ pkg-mgr search python
            Search Results:
            - python2   : The python programming language (version 2)
            - pyhton3   : The python programming langauge (version 3)
            - virtualenv : A program for managing python virtual environments.

    Download and install pre-built binaries (usually).
        Package managers used to download the source code for a program and
        would compile the code locally.  Now packages are built once on a
        server and the binaries (which are much smaller) are downloaded to
        your computer.

    Find package that provide a required library or file.
        This is like reverse-searching an image and it can be useful when
        developing software.  Very useful when you're trying to find a
        dependency during development or while building a program from source.


Popular Linux System Package Managers
-------------------------------------

.. ifnotslides::

    These are package managers used to install system packages like
    Web-browsers, terminals, network managers, etc.  Although they are
    default OS package managers, a package manager itself is really just a
    package itself, so one can install *any* package manager they want.

**.rpm**

* yum - RPM Package manager with repo support
* rpm - low level package manager tool used by yum
* Used by RedHat, CentOS, Fedora and others

**.deb**

* apt - Debian package manager with repo support
* dpkg - low level package manager tool used by apt
* Used by Debian, Ubuntu, Linux Mint and others

Yum vs. Apt
-----------

**Yum**

* XML repository format
* Automatic metadata syncing
* Supports a plugin module system to make it extensible
* Checks all dependencies before downloading

**Apt**

* Upgrade and Dist-Upgrade

  * Dist-Upgrade applies intelligent upgrading decisions during a major system
    upgrade

* Can completely remove all files including config files


.. ifnotslides::

    These two managers accomplish the same tasks as any modern Linux package
    manager but differ in their exact file-format, command-line interfaces,
    and tons of other minutia necessary in writing a package manager.


Programming Language Package Managers
-------------------------------------

.. ifnotslides::

    These are also package managers for programming languages! They can be
    used to download packages developed in a specific language, but mostly
    they are used to provide libraries and tools for a specific language.

Examples:

- Python: ``pip``
- Ruby: ``gem``, ``rubygems``
- Haskell: ``cabal``
- NodeJS: ``npm``
- ... and so on forever ...


Other Package Managers
----------------------

.. ifnotslides::

    Below are a few more notable/interesting package managers.

Portage
    The Source-based package manager for  Gentoo.

Yaourt
    An Arch User Repository wrapper for Pacman, the Arch Linux Package manager.

Nix
    A 'Fully Functional/Transactional' package manager.

Brew
    An *Open Source* package manager for OSX.

Chocolatey
    A package manager for Windows.


Installation from Source
------------------------

.. ifnotslides::

    Despite the fact that we have package managers sometimes they aren't an
    option for package installation.  The package may not registered with the
    package manager, we want to use a newer/older version of the package, or
    we want to develop with a custom version of the package.  When this
    happens we have to **install from source**.  This is scary until you do it
    once or twice and then you realize it's not that bad.

**How to install a package from source:**

.. ifslides::

    #. Download source code ``.zip`` (Zip) or ``.tar.xz/bz2/xz`` (Tarball).
    #. Unpack the downloaded code.
    #. Run the setup and configuration scripts.
    #. Build the program.
    #. Resolve any unmet dependencies and repeat previous two steps if it
       fails.
    #. Place the binaries in a consistent location.

.. ifnotslides::

    #. Download source code ``.zip`` (Zip) or ``.tar.xz/bz2/xz`` (Tarball)
        First you need to *obtain* the source code. This is done by downloaded
        an archive of the code, which is basically a way to put the code in a
        box so it can be transferred as a single file.

    #. Unpack the downloaded code.
        Once you have the source code you need to unpack it.  This is either
        using the ``tar`` program or ``unzip`` program depending on the type
        of archive.

    #. Run the setup and configuration scripts.
        These scripts can run a series of checks and configuration from
        detecting the OS you're running to make optimizations all the way to
        yelling at you to manually install a dependency.

        If you're not sure what setup and config scripts to run, check the
        source code's README file.  It should have one.  If not, try running
        ``make config``, ``make``, and ``make install``. If all else fails
        look up "How to install <package name>" or "How to install a <package
        langauge> from source".

    #. Build the program.
        Just like in programming class, when you run ``gcc myfile.c -o a.out``
        you will be building a binary from all of the source files you
        downloaded.  Unlike class you will be running a wrapper like ``make``
        or ``build`` which will run *many* commands for you automagically.

    #. Resolve any unmet dependencies and repeat last two steps until it works.
        This is by far the most painful part of the manual installation
        process.  If the install fails it will hopefully tell you why and hint
        at any libraries or external packages you need to install.  Thankfully
        **you can still use your package manager to install dependencies**.

    #. Place the binaries in a consistent location.
        You'll need to place binaries (have the ``+x`` bit flipped) in a place
        that your shell can find them.  You should place it in a directory in
        your ``PATH`` environment variable.

    These are the steps that a **from-source** package manager follows, you
    just have to do the by hand.

    Using ``grep`` as an example:

    ::

        $ wget http://mirrors.kernel.org/gnu/grep/grep-3.1.tar.xz
        $ tar -Jxvf grep-3.1.tar.xz
        $ cd grep-3.1
        $ ./configure --prefix=$HOME/bin/
        $ make
        $ make install

Exercise: Install ``sl``
------------------------

#. Install the ``git``, ``gcc``, ``make`` and ``ncurses-devel`` packages via package manager.
#. Clone https://github.com/mtoyoda/sl.git using ``git``
#. Build the software using ``make``
#. Copy the compiled ``sl`` binary into the directory ``~/local/bin/``.
#. Update your ``$PATH`` to include ``$HOME/local/bin``
#. Run '``whereis sl``' to ensure it's in your path
#. Run ``sl`` and see what happens!

Answer: Install ``sl``
----------------------

.. rst-class:: build

.. code-block:: console

  $ sudo yum install git gcc make ncurses-devel
  $ git clone https://github.com/mtoyoda/sl.git
  $ cd sl
  $ make
  gcc -O -o sl sl.c -lncurses
  $ mkdir -p ~/local/bin
  $ cp sl ~/local/bin/
  $ echo "export PATH=$HOME/local/bin:$PATH" >> ~/.bashrc
  $ source ~/.bashrc
  $ whereis sl
  sl: /home/dobc/local/bin/sl
  $ sl

.. ifslides::

Exercise: Install ``grep``
--------------------------

#. Check the current version of grep
#. Double check it's location using ``which``
#. Download the latest tarball: http://mirrors.kernel.org/gnu/grep/grep-3.1.tar.xz
#. Unpack using ``tar``
#. ``cd`` into the unpacked folder
#. Run '``./configure --prefix=$HOME/local/``', '``make``' and then '``make install``'
#. Run '``hash -r``' to ensure your environment knows about the new binary
#. Check the current version of grep (it should be 3.1 now!)
#. Double check it's location using ``which``

Answer: Install ``grep``
------------------------

.. rst-class:: build

.. code-block:: console

  $ grep --version
  grep (GNU grep) 2.20
  $ which grep
  alias grep='grep --color=auto'
          /usr/bin/grep
  $ wget http://mirrors.kernel.org/gnu/grep/grep-3.1.tar.xz
  $ tar -Jxvf grep-3.1.tar.xz
  $ cd grep-3.1
  $ ./configure --prefix=$HOME/local/
  $ make
  $ make install
  $ hash -r
  $ grep --version
  grep (GNU grep) 3.1
  $ which grep
  alias grep='grep --color=auto'
          ~/local/bin/grep

Further Reading
---------------

