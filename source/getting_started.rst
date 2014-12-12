Getting Started
===============

Install:
--------

* `PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_ (Just download first link, 'putty.exe')
* `Virtualbox <https://www.virtualbox.org/wiki/Downloads>`_
* `CentOS Box <https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box>`_
* `Vagrant <https://www.vagrantup.com/downloads.html>`_


Clone our Vagrant Repo:
-----------------------

.. code-block:: bash

    $ git clone git@github.com:DevOpsBootCamp/devopsbootcamp-vagrant.git
    $ cd devopsbootcamp-vagrant


Now, start your virtual machine!
--------------------------------

.. code-block:: bash

    # Initialize VM
    $ vagrant box add centos centos-65-x86_64-20140116.box #Or whatever the name of the .box file you downloaded is!
    $ vagrant init centos
    
    # Start your VM -- you'll have to run this every time you want to access the VM
    $ vagrant up
    
    # Get into your VM
    $ vagrant ssh

Now you're all set up to work with us!  If you're in the middle of a lesson, go ahead
and try to catch up to where we are.  
Check out `our vagrant cheat sheet <http://devopsbootcamp.osuosl.org/vagrant.html>`_ if you need help
remembering commands and so on!

Getting on IRC:
---------------

You'll want to use irssi or weechat to connect to IRC

.. code-block:: bash

    # SSH to set up persistent IRC
    $ ssh <username>@onid.oregonstate.edu #Ask someone what to do if you aren't an OSU student

    # Start a new screen session and name it 'irc'
    $ screen -S irc
    # You can also man screen if you aren't sure what it does
    $ man screen

    # Start your client -- for now, we recommend irssi, but you can also use weechat
    $ weechat-curses

Now you're on IRC!

Setting up IRC:
---------------

.. code-block:: bash

    # First things first, connect to freenode, the primary irc network
    /connect irc.freenode.net

    # Give yourself a nickname, and register with nickserv
    /nick <yournickname>
    /q nickserv register <password> <email>
    # You should get a confirmation email -- follow the instructions!
    
    # To change nicks, run
    /nick <yournickname>

    # To re-identify with nickserv (for instance if the server disconnects), run
    /q nickserv identify <password>

Now you're all registered with nickserv -- time to get into some channels!


Joining Channels:
-----------------

.. code-block:: bash

    # You can join two common channels in the OSU community -- OSU LUG and DevOps BootCamp
    /join #osu-lug
    /join #devopsbootcamp


And you're done! Welcome to IRC!  To disconnect, you can either run 'ctrl+d', or just close the window that IRC is in.
When you want to come back, just run

.. code-block:: bash

    $ ssh <username>@onid.oregonstate.edu
    $ screen -dr irc

And you'll be back online, nothing changed.  

Getting on Github:
------------------

First thing's first: install git in your VM

.. code-block:: bash

    $ sudo yum install git
    $ git config --global user.name "My Name"
    $ git config --global user.email "myemail@email.com"
    $ git config --global core.editor "nano"

You'll also want to make an account with the same email on `github <https://github.com>`_

Using Git Locally:
------------------

.. code-block:: bash

    # Initialize a new git repo
    $ git init

    # Add updated files
    $ git add <filename>

    # Take a snapshot of your repository
    $ git commit -m "I did a thing!"

    #Other good commands to know:
    $ git status
    $ git log

    # To look up:
    $ man git-<command>

Using a text-editor:
--------------------

In your terminal:

.. code-block:: bash

    $ nano

This should open up a text editor called nano. You can see the 
commands that it uses on the bottom of the screen.  Just know
that '^' means ctrl.  So, to save the document ('writeout'), 
you would type 'ctrl+O'.  To exit, 'ctrl+X', and so on.
This is where you can write and edit code!


Now you're all set up to do what we're doing.  Happy learning!
