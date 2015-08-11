.. _daycamp_04:

Version Control
===============

What We'll Cover
----------------

* Nano, a command line editor
* What's Git
* Using ``git``
* What's GitHub
* More resources

Nano
----

* type like normal
* Use arrow keys to move around
* ^ means hold control while pressing the key

.. figure:: /static/nano.png
   :align: center

Version Control is Hard
-----------------------

.. figure:: /static/xkcd_1296.png
   :scale: 150%
   :align: center

Image from `XKCD <http://xkcd.com/1296>`_

Why Bother?
-----------

.. figure:: /static/phd_final.gif
    :scale: 75%
    :align: right

Image from
`PhD Comics <http://www.phdcomics.com/comics/archive.php?comicid=1531>`_

Better Options: Version Control
-------------------------------

* Commit = Snapshot of part of your project's state
* Centralized (SVN, CVS) vs. Decentralized (Git, hg)
* We'll look at Git today
    * Easier to learn other VCS from Git
    * Widely used in the open source world

Git
---

.. figure:: /static/Linus_Torvalds.jpeg
    :align: left

git, noun. Brit.informal.
1. an unpleasant or contemptible person.

Setting up Git
--------------

* In VM:

.. code-block:: bash

    $ sudo yum install git
    $ git config --global user.name "My Name"
    $ git config --global user.email "myself@gmail.com"
    $ git config --global core.editor "nano"

Using Git Locally
-----------------

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

What Not To Do
--------------

* Don't delete the .git files

.. note:: If you kill them, git loses its memory :(

* Avoid redundant copies of the same work in one revision
* Don't make "oops, undoing that" commits.
    * Use git commit --amend or git revert

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

Git Exercise
------------

.. code-block:: none

    $ mkdir my_test_repo
    $ cd my_tets_repo
    $ git init
    $ wget http://some.url/script.py
    $ git add script.py
    $ git commit -m "My first git commit!"

.. code-block:: none

    $ nano script.py

.. code-block:: python

    def f(x):
        return x**x

Daily workflow
--------------

.. figure:: /static/gitflow.png
    :scale: 75%
    :align: right

Pull -> Work -> Add changes -> Commit -> Push

Larger projects have more complex workflows

.. note:: The picture is of the Git Flow branching model, and you'll probably
    see it every single time anyone explains Git branching and merging to you.

GitHub!
-------

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

* Free online code storage
* Easily share and collaborate on code
* Great Git documentation
* Easily findable source-code

.. Let's Walk Through
.. ------------------
..
.. * Creating an account
..     * Gravatar
..     * How to read a profile
..
.. .. note:: you just go to github.com and click the account creation links. To
..     make a custom icon, go to gravatar.com and set up an account using the
..     same email address as you used for github. The picture you upload on
..     Gravatar will then show up for your github account.
..
..     The most important thing about reading profiles is that not all of a
..     person's repos will display on the front page of their profile -- to see
..     them, got to the 'repositories' tab instead of 'contributions'.
..
.. * Creating SSH keys
..
.. .. note:: ``ssh-keygen -t rsa``
..     accept most defaults; give it a passphrase; write yourself a hint for the
..     passphrase somewhere. For instance if the passphrase is the funny way that
..     your friend misheard a song lyric, you might write down the initials of
..     the venue where you went to go see that band with that person. Basically
..     you want to pick a hint that's meaningful to you but likely to be
..     meaningless to anyone else.
..
.. * Uploading your SSH key
..
.. .. note:: account settings (icon in upper right) -> ssh keys (in menu on left)
..
.. * Creating a new repository
..
.. .. note:: icon in upper right
..
.. * Fork somebody else's repo
..
.. .. note:: button in upper right on repo main page
..
.. * Edit files online
..
.. .. note:: navigate to file, edit button is in the upper right of where the
..     file is displayed
..
.. * Submit a pull request
..
.. .. note:: on main repo, it's that green button with the arrows just to the
..     left of where it says which branch you're on
..
.. Help, Everythings's Broken!
.. ---------------------------
..
.. .. code-block:: bash
..
..     Permission denied (publickey).
..     fatal: The remote end hung up unexpectedly
..
.. Solution: ``ssh-add ~/.ssh/id-rsa`` or whatever key you have added on github
..
.. .. code-block:: bash
..
..     To git@github.com:edunham/slides.git
..      ! [rejected]        master -> master (non-fast-forward)
..     error: failed to push some refs to 'git@github.com:edunham/slides.git'
..     hint: Updates were rejected because the tip of your current branch is behind
..     hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')
..     hint: before pushing again.
..     hint: See the 'Note about fast-forwards' in 'git push --help' for details.
..
.. Solution: To avoid a messy merge commit, ``git pull --rebase``.

Other Resources
---------------

`Git Visualizations <http://www.wei-wang.com/ExplainGitWithD3/#>`_
