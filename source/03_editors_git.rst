Lesson 3: Editors & Version Control
===================================

Check in from last week
-----------------------

Is anyone having problems with package management?

Install the packages named git, vim, and emacs


What we'll discuss
------------------

* What's a text editor?
* Features of an editor
* Version control: Git!

How do you edit files?
----------------------
|

.. figure:: /static/word_screenshot.gif
    :align: center
    :scale: 125%

No. Never, Ever edit code in Word/LibreOffice
---------------------------------------------

* Autocorrect is your worst enemy
* Syntax highlighting is nice
* You are editing plain text, not 'documents', i.e. .doc, .rtf, etc

Then what should you use?
-------------------------

* Text editors
    * Command-line
    * available in your package manager
* For coding, an IDE can be helpful

Integrated Development Environments
-----------------------------------

|

.. figure:: /static/eclipse_screenshot.gif
    :scale: 40%
    :align: right

* Entire toolchain in one place
* Usually graphical

Sysadmin tools
--------------

* Frequently work with remote machines over a ssh connection
    * xforwarding can sort of give you a GUI
    * Not all remote machines have a desktop environment
* Faster to edit file in place than transfer it down then back up
    * Frequent small changes when testing or debugging
* Broken machines often have only terminal via crash cart

:Editor Requirements:
  * Small program, runs in terminal
  * Preferably installed by default on most systems


Features of an editor
---------------------

* Needs to be installed on your system
* Create files
* Move around within the file
* Add or delete text
* Easily automate tedious tasks

Text Editors
------------

.. note::

    Quick intro/history:  ed editor
    Pros: low-bandwidth, installed pretty much everywhere, very fast and powerful
    for complicated and repetitive tasks
    Cons: Steep learning curve, different “modes” can be confusing at first
    Sublime and other desktop editors: nice for serious programming, but learn
    the basics of simple text editors even if you want to be a developer, you
    won't always be able to edit your code on your own desktop

* ed -> Vi -> Vim
* Stallman -> lisp -> emacs

.. figure:: /static/xkcd_378.png
    :align: center
    :scale: 85%

Avoid Pico/Nano, Notepad++, SublimeText

Emacs
-----

.. figure:: /static/emacs_logo.jpeg
    :align: right

.. note::

    Originally released 1976
    name from Editor MACros for TECO editor, originally Tape Editor and
    COrrector at MIT in the '60s

But, along the way, I wrote a text editor, Emacs. The interesting idea about
Emacs was that it had a programming language, and the user's editing commands
would be written in that interpreted programming language, so that you could
load new commands into your editor while you were editing. You could edit the
programs you were using and then go on editing with them.

 -- Richard Stallman, http://www.gnu.org/gnu/rms-lisp.html

Vim
---

.. figure:: /static/vim_logo.jpeg
    :align: right

.. note::

    originally written for Amiga systems (Commodore PCs), 1988
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
-------------

* What can the people around you help with?
* Try both; choose one and get good at it
* Have a good answer when people ask why you made that choice
    * "Because it's familiar" is tolerated
    * "Because I was initially taught it" is common but accepted (honesty)
    * "Because ``$usecase``" provokes argument but more respected
    * "Because I tried both and picked this one" is rare but good
* Your use case as a sysadmin or developer

Modes
-----

.. figure:: /static/vim_modes.png
    :align: center
    :scale: 75%

How to tell?

.. code-block:: bash

    -- INSERT --                                          144,1    36%
    -- VISUAL --                                          144,77   36%

Commands
--------

.. note::
    Moving around in a file
    Search / replace
    Text manipulation, ie: cw, dw, c$, yy / p, x, .

.. figure:: /static/vim_cheatsheet.gif
    :scale: 75%

Moving Around
-------------

::

    h move one character to the left.
    j move down one line.
    k move up one line.
    l move one character to the right.
    0 move to the beginning of the line.
    $ move to the end of the line.
    w move forward one word.
    b move backward one word.
    G move to the end of the file.
    gg move to the beginning of the file.
    . move to the last edit.

Configuration / customization
-----------------------------

.. note:: there are many many options and pre-existing packages to make
    editing nice for sysadmins and developers

* ``.vimrc``
* ``:set``

Some sets of Vim plugins and configurations are available

* https://github.com/astrails/dotvim
* https://github.com/carlhuda/janus

Use them for research on what's available to improve dev productivity

Learning Resources
------------------

* ``$ vimtutor``
* http://vim-adventures.com/

.. figure:: /static/learning_curves.jpg
    :align: center
    :scale: 140%

Regular expressions
-------------------

You should know basic substitution:

::

    :%s/foo/bar/g

On IRC, Hamper does rudimentary regex in the form ``s/foo/bar/`` applying only
to the most recent comment.

This is not `shell globbing`_

:Resources for learning:
  * `RegExr`_ - an interactive Regular Expression editor and debugger
  * `Regular-Expressions.info`_ - Tutorials and general information

.. _shell globbing: http://tldp.org/LDP/abs/html/globbingref.html
.. _RegExr: http://gskinner.com/RegExr/
.. _Regular-Expressions.info: http://www.regular-expressions.info/


Editor questions?
-----------------

* Open an editor, find a cheat sheet, try to add some text
* Modify the text: "``disemvowel``" it

.. code-block:: bash

    $ vim testvim.txt            $ emacs testemacs.txt
    <i>                          Hello world!
    Hello world!                 <esc>
    <esc>                        <
    :%s/[aeiou]//g               <alt + x>
    :wq                          replace-regexp
                                 [aeiou]
                                 <enter>
                                 <ctrl + x> <ctrl + s>
                                 <ctrl + x> <ctrl + c>

Lesson 3: Intro to Git
======================

Version Control is Hard
-----------------------
|

.. figure:: /static/xkcd_1053.png
    :scale: 150%
    :align: center

    Image from `XKCD <http://xkcd.com/1053/>`_

Why Bother?
-----------

.. figure:: /static/phd_final.gif
    :scale: 75%
    :align: center

    Image from `PhD Comics`_

.. _PhD Comics: http://www.phdcomics.com/comics/archive.php?comicid=1531

Better Options: Version Control
-------------------------------

.. note:: Collaboration with multiple developers is important to mention

* Commit = Snapshot of part of your project's state
* Centralized (SVN, CVS) vs. Decentralized (Git, hg)
* We'll look at Git today
    * Easier to learn other VCS from Git
    * Widely used in the open source world

Git
---

.. figure:: /static/Linus_Torvalds.jpeg
    :align: left

git
  noun. Brit.informal.
  1. an unpleasant or contemptible person.

Using Git Locally
-----------------

.. code-block:: bash

    # This initializes a git repo. Use `man git-init` for more info.
    $ git init

    # This puts <filename> into the staging area. It isn't committed yet.  Use
    # `git diff` to see what changes aren't yet in staging.
    $ git add <filename>

    # This actually makes the commit. Use `git status` to see what's in staging
    # but not yet committed. Use `git show` or `git log` to see recent commits.
    $ git commit -m "I did a thing!"

* Undo things?
  the `git book`_ explains well

* Did I remember to commit that?
  ``$ git status``

* What commits have I made lately?
  ``$ git log``

.. _git book: http://git-scm.com/book/en/Git-Basics-Undoing-Things

More on commits
---------------

Your work goes from unstaged to staging area with ``git add``.

.. code-block:: bash

    $ git config --global user.name 'Your Name'
    $ git config --global user.email you@somedomain.com

* Everything in staging gets wrapped up into an object that contains
    * changes
    * timestamp
    * author info
    * parent commit hash

* These live in ``.git/`` in your project directory
* Commits go to other locations with ``git push``

What Not To Do
--------------

.. figure:: /static/dont_do_this.jpg
    :scale: 50%
    :align: right

    image from http://arstechnica.com/security/2013/01/psa-dont-upload-your-important-passwords-to-github/

* Don't delete the ``.git`` files

.. note:: If you kill them, git loses its memory :(

* Redundant copies of same work
* "oops, undoing that" commits.
    * Use ``git commit --amend``

.. note:: Amending is fine as long as you haven't pushed yet. It's generally a
    bad idea to amend or rebase work that you've already shared with others,
    unless you really know what you're doing.

* Don't wait too long between commits
    * Squashing them together later is easy

.. note:: Commit every time you think you might want to return to the current
    state. You can revert back to any previous commit, but there is no way to
    magically add a commit in where you forgot to make one.

* Don't commit compiled/generated items

.. note:: Mostly relevant to writing code, .gitignore allows you to avoid
    dealing with compiled binaries, generated output, log files, etc

* Don't commit secrets...

.. note:: Yes, there are ways to sort of take them down off of GitHub, but
    somebody might have cloned your repo while it had the secrets in. Once
    someone has a piece of information, you can't just take it away.

Daily workflow
--------------

.. figure:: /static/gitflow.png
    :scale: 75%
    :align: right

|

* Pull
* Work
* Add changes
* Commit
* Push

Larger projects have more complex workflows

.. note:: The picture is of the Git Flow branching model, and you'll probably
    see it every single time anyone explains Git branching and merging to you.
    If you are working on a larger project or writing code, you'll likely be
    using branches, this allows a project to keep many simultaneous code
    changes organized.

Lesson 3: GitHub
================

.. figure:: /static/octocat.jpg
    :align: right

* Manage permissions on repos
* Back up your work
* Social/gamification
* Amazing documentation: http://help.github.com

.. note:: GitHub serves a threefold purpose:
    It also has `amazing documentation`_ which you should all go read right now
    and consult whenever you're the least bit confused. It's like the Ubuntu
    forums in that it's explained in a way the newbies can understand, but
    unlike them in that it's all written by people who know what they're doing.

    .. _amazing documentation: https://help.github.com/

Let's Walk Through
------------------

.. figure:: /static/octocat.jpg
    :align: right

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
    * ``ssh-keygen -t rsa``
* Uploading your SSH key
* Creating a new repository
* Fork somebody else's repo
* Edit files online
* Submit a pull request

Help, Everythings's Broken!
---------------------------

::

    Permission denied (publickey).
    fatal: The remote end hung up unexpectedly

:Solution: ``ssh-add ~/.ssh/id-rsa`` or whatever key you have added on github

::

    To git@github.com:edunham/slides.git
     ! [rejected]        master -> master (non-fast-forward)
    error: failed to push some refs to 'git@github.com:edunham/slides.git'
    hint: Updates were rejected because the tip of your current branch is behind
    hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
    hint: before pushing again.
    hint: See the 'Note about fast-forwards' in 'git push --help' for details.

:Solution: To avoid a messy merge commit, ``git pull --rebase``.

Learn More
----------

.. figure:: /static/octocat.jpg

* http://git-scm.com/book
* http://try.github.io/levels/1/challenges/1

Hands-On
--------

* Fork the devopsbootcamp dotfiles repo
* Clone a copy of the repo to your VM and make a branch
* Make a commit with a helpful commit message and push to your fork

.. code-block:: bash

    $ ssh-keygen -t rsa # make an SSH key and add it to your account
    $ git clone <url from sidebar of your fork> # clone the repo
    $ cd dotfiles # git commands only work in project directlry
    $ git checkout -b <yourname> # -b creates branch
    $ vim <filename>
        # 'i' to enter insert mode
        # <esc> to get back to command mode
        # :wq to save and quit
    $ git add <filename>
    $ git commit -m "please use a helpful commit message, not like this one"
    $ git push
