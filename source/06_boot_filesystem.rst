===========================================
Lesson 6: Boot and the Filesystem Hierarchy
===========================================

.. note:: more ops-focused
    1/30/2014
    - grub, filesystem stuff based roughly on Frostsnow's talk
    - basics of kernel and differences between virtualization/physical
      (the picture that kevin draws)

    - build a piece of web app to perform systems monitoring based on ^^

The Linux Filesystem
====================

.. note:: Based on Wade's talk
    https://github.com/clinew/presentation_filesystems/blob/master/presentation.tex

Moving from Windows
-------------------

* Binaries, not executables.
* Directories, not folders.
* Read, not load.
* Symbolic links, not shortcuts.
* Write, not save.

"Program Files"
---------------

* /bin, /sbin, /usr/bin, /usr/sbin, /usr/local/bin, usr/local/sbin
* PATH environment variable
* which command

"Recycle Bin"
-------------

* Depends on the Desktop, not the filesystem.
* “So then what’s Lost+Found?”
    * Lost blocks of the filesystem.
    * Usually not an issue.

Where Things Live
-----------------

* Data stored at /home/<username>
* Configurations in dotfiles within home (/.)


Where are drives mounted?
----------------------------

* Raw file appears under /dev.
    * `dmesg | tail` for the exact name.
* USB filesystem usually mounted under /media.
* Main disk mounts as root (/)

Space on drives
---------------

* Use df to see disk free space.
* Use du to see disk usage.
* Default output is in bytes, -h for human-readable output.

Three Tiers of Filesystem Hierarchy
-----------------------------------

* /, essential for system booting and mounting /usr.
* /usr, read-only system data for normal system operation.
* /usr/local, locally-installed software.
    * Package managers usually install under / and /usr.

Common Directories
------------------

* /bin, binary files.
* /include, header files for C/C++ Programs (stdlib.h, stdio.h, string.h, &c.).
* /lib, libraries for programs.
* /sbin, binary files for root (superuser binaries).


The Boot Process
================

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

  * configuration errors, missing hardware, damaged filesystems

* init -- **Always PID 1**

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

Boot Loaders
------------

.. note::
  Grub
   * next generation PC boot loader
   * no need to “re-run grub” config updates
   * Grub config
   * disks are index based from zero
   * grub install commands
   * netboot, pretty, serial
   * device.map, grub.conf

  robust with weird disk geometry::


* Grub (Grand Unified Bootloader)

  * Dynamic fixes during booting
  * Can read the filesystem
  * Index based – ``(hd0,0) = sda1``
  * Backup Kernel Images

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

  Solaris x86 is different, uses grub

  Typically ask for root password

* What is it used for?

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

* Setting up hostname & timezone
* Checking disks with fsck
* Mounting system's disks
* Configuring network interfaces
* Starting up daemons & network services

System-V
--------

.. note::
  * System-V Most common today
  * Show system changing between different run levels.
  * Slightly different between Distros
  * init replacements

    * upstart (ubuntu)
    * SMF (Service Management Facility) -- Solaris

* Linux derived from System-V
* Run levels
* level 0 – sys is completely down
* level 1 or S – single-user mode
* level 2 through 5 – multi-user levels
* level 6 – reboot level

/etc/inittab
------------

.. note::
  Look at inittab

* Tells init what to do on each level
* Starts getty (terminals)
* Commands to be run or kept running
* Setting up a serial console

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

Shutting Down
-------------

.. note::
  Modern systems are less touchy with hard resets, but still need to be
  careful. Only for emergencies.

  Shutdown -h

  Wall “hey you guys!”

* Not Windows, don't reboot to fix issue
* Can take a long time (i.e. SPARC)
* Reboot only to

  * load new kernel, new hardware, or system-wide configuration changes
* shutdown, reboot, halt, init
* wall
