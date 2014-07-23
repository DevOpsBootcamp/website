Vagrant
=======

Trying Linux as a virtual machine with Vagrant
----------------------------------------------

In order to create a stable learning environment, we're going to have everyone
use a Devop tool called `Vagrant`_. Vagrant is typically used to help assist
both developers and system engineers in ensuring that their application and
system deployments work predictably. For our purposes we're going to use it as
an easy way for new people to get to a Linux prompt quickly with no fear of
breaking their system.

Vagrant basically interfaces with hypervisors such as `VirtualBox`_ with a
unified command line interface. This makes it portable between Mac, Windows and
even Linux! Vagrant itself is just a collection of ruby scripts while Virtualbox
does all the virtual machine magic.

We will go in more depth with how to install Linux manually, but for now we've
done all the hard work and have create pre-made Linux images.

.. _Vagrant: http://www.vagrantup.com/
.. _VirtualBox: https://www.virtualbox.org/

Installing Virtualbox
---------------------

VirtualBox is a *free* and open source virtual machine manager that you can
install on a variety of operating system platforms such as Mac and Windows.

#. Go to the `VirtualBox download page`__ and download the latest copy of
   VirtualBox.
#. Go through the installer and use the default settings when prompted.
#. Once completed, see if you can open up the VirtualBox Manager
#. If it asks you to download the latest extensions, go ahead and do that.

.. __: https://www.virtualbox.org/wiki/Downloads

Installing Vagrant
------------------

Vagrant is a *free* and open source tool used to build complete devops
environments.

#. Go to the `Vagrant download page`__ and choose the newest version available.
#. Choose all the defaults during the install if it asks you any questions

.. __: http://downloads.vagrantup.com/

Testing Vagrant
---------------

#. If you're on a Mac, open up the Terminal. If you're on windows, open up a DOS
   prompt (*cmd.exe*).
#. Type: ``vagrant status``
#. If there are no errors then Vagrant was installed correctly!

Cloning the Vagrant Repo
------------------------

We keep all of our vagrant configuration in a git version controlled repository.
If you don't have git installed, please go `download git`_ and install it.

Once you have downloaded and installed git, go to a folder where you want to
keep the repository and type the following::

  git clone https://github.com/DevOpsBootcamp/devopsbootcamp-vagrant.git

If installing git is too difficult, you can also download a `zip file`_
containing the repository. We will teach you more about git later in the year,
so don't worry!

.. _download git: http://git-scm.com/downloads
.. _zip file: https://github.com/DevOpsBootcamp/devopsbootcamp-vagrant/archive/master.zip

Using Vagrant
-------------

Now that we have the entire environment working, lets get to playing with Linux!
Open the terminal and get to the directory where the ``devopsbootcamp-vagrant``
repo is at. You can run the following commands:

.. code-block:: bash

  # Start the VM
  vagrant up

  # SSH into the VM
  vagrant ssh

  # Stop and halt the VM
  vagrant halt

  # Destroy and remove the VM
  vagrant destroy

Also check out the `Vagrant Documentation`__ for more information. You can also
always type ``-h`` to find out more information about a command.

.. __: http://docs.vagrantup.com/v2/cli/index.html

Troubleshooting
---------------

Depending on how your laptop or computer is confused in the BIOS, you may or may
not run into issues getting Vagrant and VirtualBox to work properly.

Booting the VM takes forever and never completes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The most common problem is when you type ``vagrant up`` the system just waits
and waits and never finishes the boot process. The most likely cause is because
your system doesn't have hardware virtualization enabled in the BIOS. You can
either enable the feature or you can disable the requirement in the
``Vagrantfile``.

**1. Enabling Hardware Virtualization**

Reboot your machine and press the appropriate buttons to get into the BIOS or
Setup screen. This is usually done by hitting a combination of the escape or
function keys.

Once you get into the BIOS, find a screen that has some options for the CPU.
Each BIOS is different but you are basically trying to find a feature called
*Hardware Virtualization*. Once you find it, go ahead and enable it and reboot
your system.

**2. Disabling HW Virtualization in Vagrant**

Open the ``Vagrantfile`` with your favorite editor of choice. Find the line that
says ``hwvirtex`` and remove the ``#`` from the front of the line. Now run
``vagrant destroy -f`` and then ``vagrant up`` again. This should boot the VM
properly now.
