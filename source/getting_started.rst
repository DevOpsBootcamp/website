Getting Started
===============

First, we recommend you make a directory or folder to save all your Devops-related files
in.  You can title it anything you'd like, though "devops" isn't a bad choice.  When 
you download the following, try to either download it into that folder/directory,
or move it there once it's been downloaded.  

Install:
--------

If you have windows, you need to install PuTTY to be able to use SSH:

* `PuTTY <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_ (Just download first link, 'putty.exe')

Regardless of your operating system, you'll need the following: 

* `Virtualbox <https://www.virtualbox.org/wiki/Downloads>`_
* `CentOS Box <https://github.com/2creatives/vagrant-centos/releases/download/v6.5.3/centos65-x86_64-20140116.box>`_
* `Vagrant <https://www.vagrantup.com/downloads.html>`_


Clone our Vagrant Repo:
-----------------------

You can save `this file 
<https://raw.githubusercontent.com/DevOpsBootcamp/Vagrant/master/Vagrantfile>`_
to the same directory that you downloaded the above into.

If you have git installed already, you can also jsut clone the repo and grab the file.
.. code-block:: bash

    $ git clone git@github.com:DevOpsBootCamp/devopsbootcamp-vagrant.git
    $ cd devopsbootcamp-vagrant


Now, start your virtual machine!
--------------------------------

.. code-block:: bash

    # Initialize VM
    $ vagrant box add centos centos-65-x86_64-20140116.box #Or whatever the name of the .box file you downloaded is!
    
    # Start your VM -- you'll have to run this every time you want to access the VM
    $ vagrant up
    
    # Get into your VM
    $ vagrant ssh

Now you're all set up to work with us!  If you're in the middle of a lesson, go ahead
and try to catch up to where we are.  
Check out `our vagrant cheat sheet <http://devopsbootcamp.osuosl.org/vagrant.html>`_ if you 
need help remembering commands and so on!

Getting on IRC:
---------------

You'll want to use irssi or weechat to connect to IRC

.. code-block:: bash

    # SSH to set up persistent IRC
    # Onid username is the username that you log into MyOSU with, or that your OSU email has.
    # Usually it's your last name and first initial, or some variation of that.
    $ ssh <onid username>@onid.oregonstate.edu #Ask someone what to do if you aren't an OSU student

    # Start a new screen session and name it 'irc'
    $ screen -S irc
    # You can also man screen if you aren't sure what it does
    $ man screen

    # Start your client -- for now, we recommend weechat, but you can also use irssi
    $ weechat-curses

Now you're running IRC!

Setting up IRC:
---------------

.. code-block:: bash

    # First things first, connect to freenode, the primary irc network
    /connect chat.freenode.net

    # Give yourself a nickname, and register with nickserv
    /nick <yournickname>
    /q nickserv register <password> <email>
    # You should get a confirmation email -- follow the instructions!
    # If your nickname is already registered to a different user, your nickname
    # next to the input box won't change.  If that happens, simply choose another nickname
    
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


And you're done! Welcome to IRC!  To disconnect, you can either run 'ctrl+a d', 'ctrl+d', or just close the window that IRC is in.
When you want to come back, just run

.. code-block:: bash

    $ ssh <username>@shell.onid.oregonstate.edu
    $ screen -dr irc

And you can see irc again. Things to note: you are always online, it's simply a matter of
whether you are looking at irc or not.  The above command doesn't start irc back up, or
log you back in -- irc is always running, and you are always logged in.  It just brings
the actual graphics of irc to your computer.   

Getting on Github:
------------------

First thing's first: install git in your VM

.. code-block:: bash

    $ sudo yum install git
    $ git config --global user.name "My Name"
    $ git config --global user.email "myemail@email.com"
    $ git config --global core.editor "nano"
    $ git config --global push.default "upstream"

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
    $ man git
    # For a list of git commands and what they do, or 
    $ man git-<command>
    # For more details about a certain git command, such as git-push

Using a text-editor:
--------------------

In your terminal:

.. code-block:: bash

    $ nano

This should open up a text editor called nano. You can see the 
commands that it uses on the bottom of the screen.  Just know
that '^' means ctrl.  So, to save the document ('writeout'), 
you would type 'ctrl+o'.  To exit, 'ctrl+x', and so on.
This is where you can write and edit code!


Now you're all set up to do what we're doing.  Happy learning!
