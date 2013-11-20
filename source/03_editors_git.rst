===================================
Lesson 3: Editors & Version Control
===================================

Check in from last week
=======================

Is anyone having problems with package management?

Install the packages named git, vim, and emacs


What we'll discuss
==================
* What's a text editor?
* Features of an editor
* Version control: Git!


How do you edit files?
======================

.. figure:: /static/word_screenshot.gif

==============================================
No. Never, Ever edit code in Word/LibreOffice.
==============================================

* Autocorrect is your worst enemy
* Syntax highlighting is nice

Then what should you use?
=========================

* Text editors
    * Command-line
    * available in your package manager
* For coding, an IDE can be helpful   

Integrated Development Environments
===================================

.. figure:: /static/eclipse_screenshot.gif

* Entire toolchain in one place
* Almost always graphical

Sysadmin tools
==============

* Frequently work with remote machines over a ssh connection
    * xforwarding can sort of give you a GUI
    * Not all remote machines have a desktop environment
* Faster to edit file in place than transfer it down then back up
    * Frequent small changes when testing or debugging
* Broken machines often have only terminal via crash cart

Editor Requirements:

* Small program
* Runs in terminal
* Preferably installed by default on most systems


Features of an editor
=====================

* Needs to be installed on your system
* Create files
* Move around within the file
* Add or delete text
* Easily automate tedious tasks

Text Editors
============

.. note:: Quick intro/history:  ed editor
    Pros: low-bandwidth, installed pretty much everywhere, very fast and powerful
    for complicated and repetitive tasks
    Cons: Steep learning curve, different “modes” can be confusing at first

* ed -> Vi -> Vim
* Stallman -> lisp -> emacs

* Avoid: 
    * pico/nano
    * SublimeText

Emacs
=====

.. note:: Originally released 1976
    name from Editor MACros for TECO editor, originally Tape Editor and
    COrrector at MIT in the '60s

But, along the way, I wrote a text editor, Emacs. The interesting idea about
Emacs was that it had a programming language, and the user's editing commands
would be written in that interpreted programming language, so that you could
load new commands into your editor while you were editing. You could edit the
programs you were using and then go on editing with them. So, we had a system
that was useful for things other than programming, and yet you could program
it while you were using it. I don't know if it was the first one of those, but
it certainly was the first editor like that.

 -- Richard Stallman, http://www.gnu.org/gnu/rms-lisp.html

Vim
===

.. note:: originally written for Amiga systems (Commodore PCs), 1988
    vim released 1991
    vimscript, Lua (as of Vim 7.3), Perl, Python, Racket, Ruby, Tcl (tool
    command language).
    vi written by Bill Joy in 1976, visual mode for line editor called ex 
    line editors are from age of teleprinters, no cursors

* Available almost everywhere
* Lightweight
* Design decisions explained in http://docs.freebsd.org/44doc/usd/12.vi/paper.html
* Modal editor (command, insert, visual)

How to choose
=============

* What can the people around you help with?
* Try both
* Choose one and get good at it
* Have a good answer when people ask why you made that choice
    * "Because it's familiar" is tolerated
    * "Because I was initially taught it" is common but accepted (honesty)
    * "Because $usecase" provokes argument but more respected
    * "Because I tried both and picked this one" is rare but good
* Your use case as a sysadmin
ks

Modes
=====

Command, Insert, Visual

How to tell? 

.. code-block:: bash
    -- INSERT --                                          144,1    36%

    -- VISUAL --                                          144,77   36%


Commands
========

.. note:: Moving around in a file
    Search / replace
    Text manipulation, ie: cw, dw, c$, yy / p, x, .

.. figure:: /static/vim_cheatsheet.gif

Configuration/customization
===========================

* .vimrc
* :set

Learning Resources
==================

* $ vimtutor
* http://vim-adventures.com/


Regular expressions (questions to ask)
======================================

You should know basic substitution: 

.. code-block:: bash

    :%s/foo/bar/g

This is not `shell globbing <http://tldp.org/LDP/abs/html/globbingref.html>`_


Editor questions?
=================

* Open an editor, find a cheat sheet, try to add some text
* Modify the text: "disemvowel" it

.. code-block:: bash
    $ vim testvim.txt            $ emacs testemacs.txt
    <i>                          Hello world!
    Hello world!                 <esc
    <esc>                        <
    :s/[aeiou]//g                <esc>
    :wq                          x
                                 replace-regexp
                                 [aeiou]
                                 <enter>

============
Intro to Git
============

Version Control is Hard
=======================

.. figure:: /static/xkcd_1053.png
   :scale: 150%
   :align: center

Image from `XKCD <http://xkcd.com/1053/>`_

Why Bother?
===========

.. figure:: /static/phd_final.gif
    :scale: 75%
    :align: right

Image from
`PhD Comics <http://www.phdcomics.com/comics/archive.php?comicid=1531>`_

Better Options: Version Control
===============================

* Commit = Snapshot of part of your project's state
* Centralized (SVN, CVS) vs. Decentralized (Git, hg)
* We'll look at Git today
    * Easier to learn other VCS from Git
    * Widely used in the open source world

Git
===

.. figure:: /static/Linus_Torvalds.jpeg
    :align: left
git, noun. Brit.informal. 
1. an unpleasant or contemptible person.

Using Git Locally
=================
    
``$ git init``

.. note:: This initializes a git repo. Use `man git-init` for more info.

``$ git add <filename>``

.. note:: This puts <filename> into the staging area. It isn't committed yet.
    Use ``git diff`` to see what changes aren't yet in staging.

``$ git commit -m "I did a thing!"``

.. note:: This actually makes the commit. Use ``git status`` to see what's in
    staging but not yet committed. Use ``git show`` or ``git log`` to see
    recent commits.

* Undo things?
  the `git book <http://git-scm.com/book/en/Git-Basics-Undoing-Things>`_ explains
  well

* Did I remember to commit that?
``$ git status``

* What commits have I made lately?
``$ git log``

More on commits
===============

* Your work goes from unstaged to staging area with 'git add'

.. code-block:: bash
    $ git config --global user.name 'Your Name'
    $ git config --global user.email you@somedomain.com

* Everything in staging gets wrapped up into an object that contains
    * changes
    * timestamp
    * author info
    * parent commit hash

* These live in .git/ in your project directory

* Commits go to other locations with 'git push' 

What Not To Do
==============

* Don't delete the .git files
.. note:: If you kill them, git loses its memory :(
* Avoid redundant copies of the same work in one revision
* Don't make "oops, undoing that" commits.
    * Use git commit --amend
.. note:: Amending is fine as long as you haven't pushed yet. It's generally a
    bad idea to amend or rebase work that you've already shared with others,
    unless you really know what you're doing.

* Don't wait too long between commits
    * You can squash them all together later
.. note:: Commit every time you think you might want to return to the current 
    state. You can revert back to any previous commit, but there is no way to
    magically add a commit in where you forgot to make one.

* Don't commit secrets...

.. note:: Yes, there are ways to sort of take them down off of GitHub, but
    somebody might have cloned your repo while it had the secrets in. Once
    someone has a piece of information, you can't just take it away.

.. figure:: /static/dont_do_this.jpg
    :scale: 50%
    :align: right

http://arstechnica.com/security/2013/01/psa-dont-upload-your-important-passwords-to-github/

Daily workflow
==============

.. figure:: /static/gitflow.png
    :scale: 75%
    :align: right

Pull -> Work -> Add changes -> Commit -> Push

Larger projects have more complex workflows

.. note:: The picture is of the Git Flow branching model, and you'll probably
    see it every single time anyone explains Git branching and merging to you.

GitHub!
=======

.. figure:: /static/octocat.jpg

.. note:: GitHub serves a threefold purpose: 

    * Makes it easier to manage permissions & share code with others
    * Backs up all your work in case bad things happen to your laptop
    * Social/gamification/resume building

    It also has `amazing documentation <https://help.github.com/>`_ which you
    should all go read right now and consult whenever you're the least bit
    confused. It's like the Ubuntu forums in that it's explained in a way the
    newbies can understand, but unlike them in that it's all written by people
    who know what they're doing.

Let's Walk Through
==================

* Creating an account
    * Gravatar
    * How to read a profile

.. note:: you just go to github.com and click the account creation links. To
    make a custom icon, go to gravatar.com and set up an account using the
    same email address as you used for github. The picture you upload on
    Gravatar will then show up for your github account.

    The most important thing about reading profiles is that not all of a
    person's repos will display on the front page of their profile -- to see
    them, got to the 'repositories' tab instead of 'contributions'. 

* Creating SSH keys

.. note:: ``ssh-keygen -t rsa``
    accept most defaults; give it a passphrase; write yourself a hint for the
    passphrase somewhere. For instance if the passphrase is the funny way that
    your friend misheard a song lyric, you might write down the initials of
    the venue where you went to go see that band with that person. Basically
    you want to pick a hint that's meaningful to you but likely to be
    meaningless to anyone else.

* Uploading your SSH key

.. note:: account settings (icon in upper right) -> ssh keys (in menu on left)

* Creating a new repository

.. note:: icon in upper right

* Fork somebody else's repo

.. note:: button in upper right on repo main page

* Edit files online

.. note:: navigate to file, edit button is in the upper right of where the
    file is displayed

* Submit a pull request

.. note:: on main repo, it's that green button with the arrows just to the
    left of where it says which branch you're on

Help, Everythings's Broken!
===========================

.. code-block:: bash

    Permission denied (publickey).
    fatal: The remote end hung up unexpectedly

Solution: ``ssh-add ~/.ssh/id-rsa`` or whatever key you have added on github

.. code-block:: bash

    To git@github.com:edunham/slides.git
     ! [rejected]        master -> master (non-fast-forward)
    error: failed to push some refs to 'git@github.com:edunham/slides.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
    hint: before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.

Solution: To avoid a messy merge commit, ``git pull --rebase``. 

Learn More
==========

* http://git-scm.com/book

* http://try.github.io/levels/1/challenges/1

Hands-On
========

* Create a GitHub account
    * github.com
* Make an ssh key on your VM
    * $ ssh-keygen -t rsa
* Fork the devopsbootcamp-website repo
    * https://github.com/DevOpsBootcamp/website
* Clone a copy of the repo to your VM
    * $ git clone <url from sidebar of your fork>
* Fix a spelling error and save the file
    * $ vim <filename>
    * 'i' to enter insert mode
    * <esc> to get back to command mode
    * :wq to save and quit
* Make a commit with a helpful commit message
    * $ git add <filename>
    * $ git commit -m "your commit message"
* Push to your fork
    * $ git push
