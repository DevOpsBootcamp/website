Lesson 6: Boot and the Filesystem Hierarchy
===========================================

.. note::
    - grub, filesystem stuff based roughly on Frostsnow's talk
    - basics of kernel and differences between virtualization/physical (the
      picture that kevin draws)

The Linux Filesystem Hierarchy
------------------------------

.. note:: Based on Wade's talk
    https://github.com/clinew/presentation_filesystems/blob/master/presentation.tex

What's a filesystem?

    In computing, a file system is used to control how information is stored and
    retrieved. Without a file system, information placed in a storage area would
    be one large body of information with no way to tell where one piece of
    information stops and the next begins.

                       - (http://en.wikipedia.org/wiki/Filesystem)

Filesystem can mean:
--------------------

- **How the system's files are arranged on the disk**
- How the disk actually holds the files

  - FAT and NTFS are old but Windows-compatible
  - ext3 is standard, ext4 is newer, xfs has fancier journaling

    - journaling tracks changes before write
  - sysadmins will encounter NFS and its competitors like Gluster

.. note::
  Moving from Windows?

  - Binaries, not executables.
  - Directories, not folders.
  - Read, not load.
  - Symbolic links, not shortcuts.
  - Write, not save.

The File System
---------------
|

.. figure:: static/you_are_here.jpg
    :align: center
    :scale: 75%

.. code-block:: bash

    $ ls
    bin   etc         initrd.img.old  lost+found  opt   run      srv  usr
    boot  home        lib             media       proc  sbin     sys  var
    dev   initrd.img  lib64           mnt         root  selinux  tmp  vmlinuz


Installed programs and utilities
--------------------------------

.. code-block:: bash

    /bin                /usr/sbin
    /sbin               /usr/local/bin
    /usr/bin            /usr/local/sbin

* ``PATH`` environment variable

.. code-block:: bash

    $ echo $PATH
    /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

* ``which`` command

.. code-block:: bash

    $ which bash
    /bin/bash

User-Specific Data & Configuration
----------------------------------

* Data stored at ``/home/<username>``
    * Desktop environment creates folders Documents, Pictures, Videos, etc.
* Configurations in dotfiles within home (``/.``)

* Lost+Found is **not** your desktop trash can
    * Lost blocks of the filesystem.
    * Usually not an issue.
    * If your desktop provides backups of deleted files, they'll be somewhere
      in ``/home/<username>/``


Where are drives mounted?
----------------------------

* Raw device appears under ``/dev``.

.. code-block:: bash

    $ dmesg | tail
    [260930.208715]  sdb: sdb1
    [260930.320756] sd 6:0:0:0: >[sdb] Asking for cache data failed
    [260930.320765] sd 6:0:0:0: >[sdb] Assuming drive cache: write through
    [260930.320771] sd 6:0:0:0: >[sdb] Attached SCSI removable disk

* USB filesystem under ``/media``, main disk ``/``
* You can manually mount devices with ``mount``
    * "Everything's a file"
    * ``umount`` to unmount

* ``/etc/fstab`` tells things where to mount
* ``/etc/mtab`` shows where things are currently mounted

Space on drives
---------------

* Use df to see disk free space.

.. code-block:: bash

    $ df -h /
    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sda8        73G   29G   41G  42% /

* Use du to see disk usage.

.. code-block:: bash

    $ du -sh /home/
    21G /home/

* Default output is in bytes, ``-h`` for human-readable output.

Three Tiers of Filesystem Hierarchy
-----------------------------------

* /, essential for system booting and mounting /usr.
* /usr, read-only system data for normal system operation.
* /usr/local, locally-installed software.
    * Package managers usually install under / and /usr.

.. figure:: /static/hierarchy.jpg
    :align: center
    :scale: 60%

Common Directories
------------------

=========  =============================================
Directory  Contents
=========  =============================================
/bin       Binary files
/include   Header files for C/C++ programs
/lib       Libraries
/sbin      Binary files for root (superuser)
/boot      Files essential for booting kernel, initramfs
/dev       Virtual filesystem, exports hardware devices
/etc       System-wide configurations
/home      Individual users' data
/media     Removable storage devices
/mnt       Like media -- place to mount disks and things
=========  =============================================

Common Directories
------------------

==========  ===========================================
Directory   Contents
==========  ===========================================
/opt        "Add-on application software packages"
/proc       Virtual filesystem exporting system data
/root       homedir for root
/run        Volatile information accumulated since boot
/sys        Virtual filesystem exporting kernel objects
/tmp        Temporary files
/var        Data which varies -- logs, mail, etc.
/usr/share  Architecture-independent, read-only data
/usr/src    Kernel source code
==========  ===========================================

/proc has lots of useful system information
-------------------------------------------

Which Linux kernel version are you running?

.. code-block:: bash

    $ cat /proc/version
    Linux version 3.5.0-17-generic (buildd@allspice) (gcc version 4.7.2
    (Ubuntu/Linaro 4.7.2-2ubuntu1) ) #28-Ubuntu SMP Tue Oct 9 19:31:23 UTC 2012

Learn about system's hardware

.. code-block:: bash

    $ less /proc/cpuinfo
    $ less /proc/meminfo

Some parts of /proc can be written as well as read...

.. code-block:: bash

    $ echo 3 > /proc/sys/vm/drop_caches # drop caches

Commands for working with filesystems
-------------------------------------

Creating filesystems

.. code-block:: bash

    $ mkfs

Mounting filesystems

.. code-block:: bash

    $ mount
    # -t for type
    # -o for options
    # requires device path and mount point

Loopback devices

.. code-block:: bash

    $ losetup
    $ /dev/loop*
    # makes it look like a device instead of a file

devfs
-----

.. code-block:: bash

    sd*
    sr*
    /dev/null
    /dev/random
    /dev/urandom
    /dev/zero

Blocks and dd
-------------

* Block size is the size of chunks allocated for files

* dd
    * Disk duplicator (or disk dump).
        * if=<path>, input file.
        * of=<path>, ooutput file.
        * bs=<size>, block size.
        * count=<size>, number of block to transfer.

.. code-block:: bash

    $ dd if=/dev/random of=/dev/sda
    # What will this do?


Filesystem Consistency
----------------------

* Metadata vs. data
    * Metadata is extra information the filesystem tracks about the file
    * Data is the file's contents

* Filesystem is **consistent** if all metadata is intact
    * ``fsck`` is FileSystem Consistency Check

More about Journaling
---------------------

- Filesystem consistency tool; protections against system freezes, power
  outages, etc.
- Replaying the journal.
- ext3’s three modes of journaling:

  - :journal: Data and metadata to journal.
  - :ordered: Data updates to filesystem, then metadata committed to journal.
  - :writeback: Metadata comitted to journal, possibly before data updates.

The Boot Process
----------------

* Bootstrapping
* Steps in the process
* Boot loaders
* Startup scripts
* Boot levels

.. figure:: static/xkcd-fight.png
    :align: center
    :scale: 100%

Bootstrapping
-------------

.. note::
  kernel loaded into memory, initialization tasks, and available to users

  Init
    * kernel spawns init which is always PID 1
    * controls the boot process
    * can be a simple script to a binary

* *Pull itself up by its own bootstraps*
* Automatic and manual booting
* Driver Loading
* Period of vulnerability

  * configuration errors
  * missing hardware
  * damaged filesystems

* ``init`` -- **Always Process ID (PID) #1**

  * First process to start
  * Either a binary or can be a simple script (even a bash shell!)

Steps in boot process
---------------------

.. note::
  Kernel
   * 1st stage – bootloader, 2nd, boot the kernel
   * boot from boot loader
   * load into memory
   * located in /boot/ on Linux
  Hardware config
   * locate & initialize hardware
   * print out what it does
  System processes
   * init, kswapd, pdflush, etc
   * init only real process
   * Others look like processes for scheduling (appear as [kswapd] with ps)

|

.. figure:: static/booting.png
    :align: right
    :scale: 70%

#. Kernel initialization
#. Hardware configuration
#. System processes
#. Operator intervention (single-user)
#. Execution of start-up scripts
#. Multi-user operation

Booting
-------

.. note::
  On hardware specific to UNIX (i.e. Sun)
   * firmware knows how to use devices
   * talk to the network
   * understand filesystems
   * all accessible via the commandline

  BIOS smarter than they used to be
   * Not standardized
   * Most servers support PXE

* PCs vs Proprietary hardware

  * BIOS, UEFI, OpenBoot PROM, etc
* BIOS

  * **B**\ asic **I**\ nput/**O**\ utput **S**\ ystem
  * Very simple compared to OpenBoot PROM / UEFI
  * Select devices to boot from
  * MBR (first 512 bytes)

* UEFI

  * **U**\ nified **E**\ xtensible **F**\ irmware **I**\ nterface
  * Successor to BIOS
  * Flexible pre-OS environment including network booting

Boot Loaders (Grub)
-------------------

.. note::
  Grub
   * next generation PC boot loader
   * no need to “re-run grub” config updates
   * Grub config
   * disks are index based from zero
   * grub install commands
   * netboot, pretty, serial
   * device.map, grub.conf
   * robust with weird disk geometry

* **Gr**\ and **U**\ nified **B**\ ootloader
* Dynamic fixes during booting
* Can read the filesystem
* Index based – ``(hd0,0) = sda1``
* Grub "version 1" vs. "version 2"

  * Version 2 has more features, but more complicated
  * Latest Debian, Ubuntu and Fedora use v2

.. code::

  grub> root (hd0,0)    (Specify where your /boot partition resides)
  grub> setup (hd0)     (Install GRUB in the MBR)
  grub> quit            (Exit the GRUB shell)

  grub-install

Single User Mode
----------------

.. note::
  Show on VM
   * enter grub, hit ESC, pick kernel, hit “e” for edit
   * use arrows

  Typically ask for root password

* What is it used for?

.. figure:: static/single-user-mode.png
    :align: right
    :scale: 60%
..

  * Troubleshoot problems
  * Manual Filesystem Checks
  * Booting with bare services
  * Fix boot problems
  * Add “single” to kernel option

* Solaris/BSD

  * ``boot -s``

Startup Script Tasks
--------------------

.. note::
  Verbose and print out description of what its doing.

  Old days were to manually adjust scripts, not anymore. Most are configurable now.

|

.. figure:: static/fsck.jpg
    :align: center
    :scale: 75

* Setting up hostname & timezone
* Checking disks with fsck
* Mounting system's disks
* Configuring network interfaces
* Starting up daemons & network services

System-V Boot Style
-------------------

.. note::
  * System-V Most common today
  * Show system changing between different run levels.
  * Slightly different between Distros

* Linux derived from System-V originally
* Alternative init systems

  * **systemd** - Fedora 15+, Redhat 7+ and Debian* (dependency driven)
  * **upstart** - Ubuntu, Redhat 6 (event driven, faster boot times)

Run levels:

================= =============================
level 0           sys is completely down (halt)
level 1 or S      single-user mode
level 2 through 5 multi-user levels
level 6           reboot level
================= =============================

/etc/inittab
------------

.. note::
  Look at inittab

* Tells init what to do on each level
* Starts ``getty`` (terminals, serial console)
* Commands to be run or kept running
* ``inittab`` not used with systemd or upstart

.. code::

  # The default runlevel.
  id:2:initdefault:

  # What to do in single-user mode.
  ~~:S:wait:/sbin/sulogin

  # What to do when CTRL-ALT-DEL is pressed.
  ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now

  # terminals
  1:2345:respawn:/sbin/getty 38400 tty1
  T0:23:respawn:/sbin/getty -L ttyS0 9600 vt100


init.d Scripts
--------------

.. note::
  sshd init script
   * case statement
   * functions
   * chkconfig

* One script for one service/daemon
* Start up services such as sshd, httpd, etc
* Commands

  * start, stop, reload, restart
* sshd init script

.. code-block:: bash

  $ service sshd status
  openssh-daemon (pid  1186) is running...

  $ service sshd restart
  Stopping sshd:                                             [  OK  ]
  Starting sshd:                                             [  OK  ]

Starting services on boot
-------------------------

.. note::
  Show sshd script
  show list, adding, removing, enabling, disabling

* rc\ **level**\ .d (rc0.d, rc1.d)
* S = start, K = stop/kill
* Numbers to set sequence (S55sshd)
* chkconfig / update-rc.d

  * Easy way to enable/disable services in RH/Debian
* Other distributions work differently

.. code-block:: bash

  $ chkconfig --list sshd
  sshd            0:off 1:off 2:on  3:on  4:on  5:on  6:off

  $ chkconfig sshd off

  $ chkconfig --list sshd
  sshd            0:off 1:off 2:off 3:off 4:off 5:off 6:off

Configuring init.d Scripts
--------------------------

.. note::
  show sendmail & network config examples for CentOS

  /etc/defaults seems to be more common between UNIX's

* /etc/sysconfig (RH) or /etc/defaults (Debian)
* source Bash scripts
* Daemon arguments
* Networking settings
* Other distributions are vastly different

.. code-block:: bash

  $ cat /etc/sysconfig/ntpd
  # Drop root to id 'ntp:ntp' by default.
  OPTIONS="-u ntp:ntp -p /var/run/ntpd.pid -g"

Shutting Down
-------------

.. note::
  Modern systems are less touchy with hard resets, but still need to be
  careful. Only for emergencies.

  Shutdown -h

* Not Windows, don't reboot to fix issue
* Can take a long time (i.e. servers)
* Reboot only to

  * load new kernel
  * new hardware
  * system-wide configuration changes
* ``shutdown``, ``reboot``, ``halt``, ``init``
* ``wall`` - send system-wide message to all users

.. code-block:: bash

  $ wall hello world
  Broadcast message from root@devops-bootcamp (pts/0) (Fri Jan 31 00:40:29 2014):

  hello world

Homework
--------
