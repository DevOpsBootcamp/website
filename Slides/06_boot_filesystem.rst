Lesson 6: Boot and the Filesystem Hierarchy
===========================================

.. note::
    - grub, filesystem stuff based roughly on Frostsnow's talk
    - basics of kernel and differences between virtualization/physical (the
      picture that kevin draws)

Before we begin
---------------

|

::

    $ sudo yum install man man-pages man-pages-overrides
    $ man hier # a massive man page explaining the filesystem hierarchy

::

    $ echo $PATH
    /usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/sbin:\
    /home/vagrant/bin

``$PATH`` is used as a colon-delimited list of places to
look for binaries by your shell

::

    $ which pwd
    /bin/pwd

The ``which`` command tells you which binary it is running for a given name.

Before we begin
---------------

* File := Device in the context of a file system
* You can view a files information with any of the following commands::

    $ ls -l $file #
    $ file $file # will state long name of file type
    $ stat $file

Permission Bits
---------------

All files have 2 entry bytes and 12 permission bits:

* 2 entry bytes for type:

  * one of: regular, block, character, dir, link, fifo, socket, or whiteout

* 3 permission bits for user

  * read, write, execute

* 3 permission bits for group

  * read, write, execute

* 3 permission bits for everyone

  * read, write, execute

* 3 permission bits for special things:

  * sticky, setgid, setuid

Permission Bits
---------------

::

    ls -la /home
    drwxr-xr-x.  3 root    root    4096 Oct 29 16:06 .
    dr-xr-xr-x. 23 root    root    4096 Nov 13 20:21 ..
    drwx------.  3 vagrant vagrant 4096 Nov 13 21:53 vagrant

* First ten chars are permission bits, first ``-`` means regular file
* Every other ``-`` means either read, write, execute bit not set
* First three ``rwx`` is for user, then group, then other
* Change permissions with ``chmod``

Permissions (Octal)
-------------------

* 2 bytes for entry type

* 1 byte each for:

  * special, user, group, others

.. csv-table:: Permissions (Octal)
   :header: Category,Execute,Read,Write

   Special,1000 (sticky),2000 (setgid),4000 (setuid)
   User,0100,0200,0400
   Group,0010,0020,0040
   Other,0001,0002,0004

* Sum the 4 bytes to get total permissions, summing is bijective:

Permissions Example (Octal)
---------------------------

.. csv-table:: **1775**
   :header: Category,Execute,Read,Write

   Special,set (sticky), not set, not set
   User,set,set,set
   Group,set,set,set
   Other,set,not set,set

.. csv-table:: **0644**
   :header: Category,Execute,Read,Write

   Special,not set,not set,not set
   User,not set,set,set
   Group,not set,not set,set
   Other,not set,not set,set

The Linux Filesystem Hierarchy
------------------------------

|

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

|

- **How the system's files are arranged on the disk**
- How the disk actually holds the files

  - FAT and NTFS are old but Windows-compatible
  - ext4 is standard, ext3 is older, xfs is being used less

    - journaling tracks changes before write

  - ZFS is awesome, but has meh Linux support (but getting better)
  - btrfs is similar to ZFS, but less mature
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

    $ ls /
    bin   dev  home  lib64       media  opt   root  selinux  sys  usr      var
    boot  etc  lib   lost+found  mnt    proc  sbin  srv      tmp  vagrant

\/bin & \/sbin
--------------

|

* Store binaries that are used to boot system and mount other fileystems
* binaries for all users in ``/bin``, binaries used by root are in ``/sbin``
* Things like ``mount``, ``echo``, ``chmod``, ``hostname``

\/usr (Historical Context)
--------------------------

* People were running out of disk space so:

  * All binaries not required for base system + booting + mounting other devices went in /usr/bin and /usr/sbin
  * These binaries were typically manually compiled and installed by the user
  * Eventually some unices (linux didn't exist yet) took over 
    /usr/bin and /usr/sbin for the location that packages 
    were installed to.
  * Now manually installed (without package manager) binaries go in
    ``/usr/local/bin`` and ``/usr/local/sbin``.

\/usr (Modern Context)
----------------------

::

    ls /usr
    bin  etc  games  include  lib  lib64  libexec  local  sbin  share src

.. csv-table::
   :header: Location, Description

   /usr/bin,Packages installed by package manager
   /usr/sbin,Packages installed by package manager
   /usr/etc,Rarely used; files from /etc can be symlinked here
   /usr/games,Binaries for games and educational programs

\/usr (Modern Context)
----------------------

.. csv-table::
   :header: Location, Description

   /usr/include,Include files for the C compiler
   /usr/lib,Object libraries (including dynamic libs); some unusual binaries
   /usr/lib64,64-bit libraries
   /usr/libexec,Executables used with libraries; not used much
   /usr/local,Programs (and their configuration) locally installed by user go here

\/usr (Modern Context)
----------------------

.. csv-table::
   :header: Location, Description

   /usr/share,Application data; typically examples and documentation
   /usr/src/linux,Kernel source goes here

\/dev
-----

* Device files, which often refer to physical devices

  * ``/dev/sd?``
  * ``/dev/sr?``
  * ``/dev/tty*``

* Special character devices:

  * ``/dev/null`` -- sink for writes
  * ``/dev/random`` -- high quality randomness (blocking)
  * ``/dev/urandom`` -- non-blocking random
  * ``/dev/zero`` -- always reads 0s

\/etc
-----

|

* Configuration files local to the machine
* Programs almost always look here for configuration first

\/home
------

|

* Contains homedirs of regular users
* Sometimes symlinked to ``/usr/home``, but rarely on linux

\/lib & \/lib64
---------------

|

* Libraries needed to boot and run commands related to bootstrapping

\/media & \/mnt
---------------

|

* Used as mount points for other devices (usb sticks, nfs, etc)
* Most Desktop Environments automatically mount things to ``/media``

\/proc
------

|

* Special filesystem ``procfs`` contains a file-representation of
  the current state of the kernel and running processes.

\/sys
-----

|

* File-representation of device drivers, subsystems, and hardware
  loaded into the kernel
* Similar to ``sysctl`` on other Unixy systems

\/var
-----

|

* Multi-purpose: log, temporary, transient, and spool files
* Typically contains run-time data
* Cache

Devices
-------

.. csv-table:: Types of Devices
   :header: Type,Letter,Description

   Block,b,Used to interact with devices; programs can skip around and read different chunks. Example: ``/dev/sda``
   Character,c,Unbuffered direct access to a device; Example: ``/dev/zero``

Devices
-------

.. csv-table:: Types of Devices
   :header: Type,Letter,Description

   Pseudo,None Used,Devices that don't correspond to a physical device; Pseudo devices are also either a Block or Character device; example: ``/dev/null`` (pseudo + character)
   Directory,d,Contains other files/devices; example: ``/``

Devices
-------

.. csv-table::
   :header: Type,Letter,Description

   Symbolic Link,l,Points to another device by name; example: ``/usr/tmp`` which points to ``/var/tmp`` (use ``ls -l`` to find where a link points)
   FIFO/LIFO,p,First in First out; Last in First out; example: ``/var/spool/postfix/public/pickup``

Devices
-------

.. csv-table::
   :header: Type,Letter,Description

   Regular File,\-,Exactly what you are used to
   Whiteout,w,A special device used in some Unices (not Linux) for unioned filesystems
   Socket,s,Communication point (inter-process communication; networking; etc)   
   

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

devfs
-----

.. code-block:: bash

    /dev/sd*
    /dev/sr*
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
- ext4’s three modes of journaling:

  - :journal: Data and metadata to journal.
  - :ordered: Data updates to filesystem, then metadata committed to journal.
  - :writeback: Metadata comitted to journal, possibly before data updates.

- ext4 journaling differs from ext3 because it uses a single-phase
  checksum transaction, allowing it to be done asynchronously.

Booting
-------

|

* POST
* Bootloader
* Kernel
* [Ramdisk] -- initrd
* init
* Everything else

POST
----

|

* Power On Self Test
* BIOS
* Initializes hardware at very low level

  * ensures it is accessible
  * does **not** load drivers

Bootloader
----------

|

* Responsible for booting the kernel
* Contained in first 512 bytes (MBR scheme)
* Can chainload to another bootloader

Bootloader
----------

|

* Most linux-based systems use GRUB

  * GRand Unified Bootloader

* LILO (LInux LOader) is an uncommon alternative
* syslinux, isolinux are often used for usb/cd images

GRUB
----

|

* Version 2 vs 0.97 (and 0.98)
* 2 is more complex, but does more
* 0.97/8 is simple and easy to use

GRUB Configuration
------------------

|

* CentOS 6 (your VMs) use GRUB 0.97
* Main configuration is in ``/boot/grub/menu.lst``
* kernels and initrds live in ``/boot``
::

    title CentOS 6 (2.6.32-504.el6.x86_64)
	root (hd0,0)
	kernel /vmlinuz-2.6.32-504.el6.x86_64 ro root=/dev/mapper/VolGroup-lv_root rd_NO_LUKS LANG=en_US.UTF-8 rd_NO_MD rd_LVM_LV=VolGroup/lv_swap SYSFONT=latarcyrheb-sun16 crashkernel=auto rd_LVM_LV=VolGroup/lv_root  KEYBOARDTYPE=pc KEYTABLE=us rd_NO_DM rhgb quiet
	initrd /initramfs-2.6.32-504.el6.x86_64.img

GRUB Configuration
------------------

|

* root -- boot partition
* kernel -- your linux kernel!
* initrd -- initial ram disk which is mounted to help you boot

initrd
------

* Initial Ram Disk
* Ram disk contains enough to mount ``/``
* runs ``/init`` on the ramdisk (before mounting the **real** ``/``)
  , which mounts ``/`` and runs the new init::

     for f in /mount/*.sh; do
       [ -f "$f" ] && . "$f"
       [ -d "$NEWROOT/proc" ] && break;
     done
     ...
     exec switch_root "$NEWROOT" "$INIT" $initargs

* mostly necessary if you are using ``lvm``, ``cryptsetup (LUKS)``, or other
  complex configurations


real init
---------

|

* PID 1 (because it is the first thing that runs!)
* Ancestor to every other process
* Runs all other startup scripts (networking, etc)
* Most linuces are settling on ``systemd`` as their init system

  * alternatives: systemv, openrc, bsd-style, upstart
  * your centos 6 VM uses upstart, centos 7 uses systemd
