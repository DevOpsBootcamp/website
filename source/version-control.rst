.. _version_control:


Lesson 8: Version Control
=========================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/version-control.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/version-control.html
.. _Video:

.. include:: unfinished.txt

.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - Overview of VCS
      - What it is
      - What it solves
      - Types
    - Introduction to Git
      - How to use Git
      - What not to do with Git
      - Workflows

Version Control Systems
-----------------------

VCS is how one tracks changes, modifications, and updates to source files over
time.  Creating a **history of changes** for a project over time.

Used for:
    - Documentation
    - Code
    - Configuration
    - Collaboration

Other Names Include:
    - Source Control Management (SCM)
    - Version Control Software
    - Revision Control Software


What VCS Solves
~~~~~~~~~~~~~~~

.. image:: /static/phd_final.gif
    :align: center
    :alt: PHD Comics 'Final Draft'.
    :target: http://www.phdcomics.com/comics/archive.php?comicid=1531
    :width: 50%

.. nextslide::

Version control solves a lot of problems:
    - *I have changes I want to integrate (merge) into the main project.*
    - *I want to track the state of this project over time.*
    - *I want to make some changes without possibly breaking what I have.*
    - ... and much more.

.. ifnotslides::

    Most VCS software does this by storing *metadata* about a project,
    specifically differences (diffs) between between points in history.

    VCS is a broad and complicated topic.  It might not come easy to you, but
    experience will help.


Principles of VCS
~~~~~~~~~~~~~~~~~

.. ifslides::

    =============== ==========================================================
    **Repository:** A project.
    **Diff:**       Delta between two points in history.
    **Commit:**     A snapshot of project in time.
    **Branch:**     Modifications made in parallel with the main project.
    **Merge:**      Introducing changes from one branch into another.
    **Clone:**      Downloading a local copy of a project.
    **Fork:**       A modified version of an existing project.
    =============== ==========================================================

.. ifnotslides::

    Below is a list of concepts / vocabulary you'll encounter when working
    with VCS.  Some systems use slightly different verbiage to describe these
    ideas but you can get by with these words.

    Repository:
        Your project.

        *"I created a new repository (repo) for my school project so we can
        collaborate more easily."*

    Diff:
        The delta (additions and deletions) between two states of a project.

        *"The diff between draft one and two was very long thanks to the help of
        the skilled editor."*

    Commit:
        A snapshot of your project's state at a point in history.  Records the
        difference between two points in history with a **diff**.

        *"Your last commit modified two methods and introduced a bug somewhere."*

    Branch:
        Modifications to a project (main branch = trunk) made in parallel with the
        a main branch, but not affecting the main branch.

        *"My branch introduces some changes which might break production so I'm
        not going to merge it until it's well tested."*

    Merge:
        Introducing changes from one branch into another.

        *"I merged three commits into the Master branch so we can have those
        features in the next release."*

    Clone:
        Downloading a local copy of a project.

    Fork:
        Your own version of somebody else's project where you take the original
        code-base and make modifications.  May include many changes or just a few
        bug-fixes.  Sometimes you end up merging those changes back *upstream*.


Types of VCS
~~~~~~~~~~~~

.. ifslides::

    Centralized VCS
        *"I'm going to work at the designated work-bench.  Nobody else can
        work on this until I'm done."*

        - Subversion
        - CVS

    Distributed VCS
        *"I'm going to work over here for a while and tell you about what I
        did later."*

        - Git
        - Mercurial

.. ifnotslides::

    There are two main types of VCS: distributed and centralized.  They each
    have their pros and cons.

    Centralized VCS
        *"I'm going to work at the designated work-bench.  Nobody else can
        work on this until I'm done."*

        Centralized Version Control Systems require a persistent connection
        with a centralized server.

    Examples include:
        - Subversion
        - CVS

    Distributed VCS
        *"I'm going to work over here for a while and tell you about what I
        did later."*

        Distributed version control systems are those in which each person
        working on a project downloads a local copy of the project, makes
        their changes, and manually fetches changes from other copies.

    Examples include:
        - Git
        - Mercurial


Git
---

    *Git is a Free and Open Source distributed version control system
    designed to handle everything from small to very large projects with
    speed and efficiency.* ( https://git-scm.com )

.. image:: /static/git-logo.png
    :target: https://commons.wikimedia.org/wiki/File:Git-logo.svg
    :alt: Git logo
    :align: center

.. ifnotslides::

     Git has become the de facto VCS tools used by new Open Source projects.
     It is supported on platforms including Github, Bitbucket, and Gitlab and
     is used by projects like the Linux Kernel, the Go langauge, and of course
     Git itself.

     It is not the *only* VCS out there.  Your future job may require you to
     use a different tool for VCS.  Thankfully the *principles* of SCM are
     very similar everywhere you go, so pay attention!  There's a lot to learn
     here and it's not all about the commands you should type.


Setting up Git
~~~~~~~~~~~~~~

.. ifnotslides::

    Before using Git we need to make sure we have it configured.  We will do
    this by telling Git what our name, email, and preferred text editor is.

::

    $ git config --global user.name "My Name"
    $ git config --global user.email "myself@gmail.com"
    $ git config --global core.editor "nano"


TODO: Use Git Locally
~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    First we will create a repo. In Git a repo is just a directory that we
    have run ``git init`` inside of.

Create a project with Git:

::

    $ mkdir my-project
    $ cd my-project    # Always run `git init` inside of a project folder!
    $ git init         # Never inside of your home directory.

.. ifnotslides::

    Next we are going to add a file to our project.  This is as easy as
    creating it, staging it (``git add <filename>``) and committing it.

Add and commit a file to your project with Git:

::

    $ touch newfile.txt
    $ git add newfile.txt
    $ git commit  # Edit message in Nano, save the file, exit to commit.

To see which files are staged, unstaged, or untracked:

::

    $ git status

.. nextslide::

To look through your repository history:

::

    $ git log

To create and checkout a branch:

::

    #Note the `*` which indicates the current branch
    $ git checkout -b "new-branch"
    $ git branch
    master
    * new-branch

TODO: Working With a Git Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Checkout a new feature branch on your repository.

    ::

        $ git checkout -b "add-awesome-feature"

Create/Edit files on the new branch.

    ::

        $ echo "Some awesome text" > awesomefile.txt
        $ git status
        # On branch add-awesome-feature
        # Untracked files:
        ...
        #         awesomefile.txt
        ...

        $ git add awesomefile.txt
        $ git commit -m "Short awesome commit message"

.. nextslide::

View the diff between the two.

    ::

        $ git diff master
        diff --git a/awesomefile.txt b/awesomefile.txt
        new file mode 100644
        index 0000000..08cec7f
        --- /dev/null
        +++ b/awesomefile.txt
        @@ -0,0 +1 @@
        +Some awesome text

.. nextslide::

Locally merge the changes from your new branch into Master.

    ::

        $ git checkout master
        $ git merge add-awesome-feature
        Updating 459de26..5c4ca48
        Fast-forward
        awesomefile.txt | 1 +
        1 file changed, 1 insertion(+)
        create mode 100644 awesomefile.txt


What not to do with Git
-----------------------

.. ifslides::

    - Do not delete the ``.git`` directory.
    - Do not change history.
    - Do not make redundant commits or revert commits.
    - Do not wait too long between commits.
    - Avoid redundant copies of the same work.
    - Do not commit secrets. They never go away.

.. ifnotslides::

    Do not delete the ``.git`` directory.
        The ``.git`` directory is the file which contains your entire Git
        repository.  All history and metadata about your repo is kept in that
        folder, deleting it deletes your project except for the code you have
        right now.

    Do not change history.
        You will eventually learn some commands to modify history (change
        commit messages or changes in a commit).  You *can* do this but you
        should only do it with caution and only when you fully understand what
        you're doing.  It has the potential to ruin other people's day.

        Well -- don't change history with the exception of the next two
        points...

    Do not make redundant commits or revert commits.
        After making a commit, use ``git commit --amend`` if you want to make
        changes to avoid cluttering your history with *Oops, changing that*
        messages.

    Don't wait too long between commits.
        Commits are cheap and you can never make too many.  If you wait too
        long you might as well not use it!  Once you're done with a feature
        you can ``squash`` many commits into one.

    Avoid redundant copies of the same work.
        If you want to make changes to something, but also want to keep the
        original, make a branch!  There are very few cases where making a copy
        of something in the same repository is the best thing to do.

    Don't commit secrets. They never go away.
        Ars Technica wrote about the topic, check it out:
        http://arstechnica.com/security/2013/01/psa-dont-upload-your-important-passwords-to-github/


Workflow(s)
-----------

Everybody uses VCS differently.  Choose the workflow that works best for
everybody involved.

.. image:: /static/gitflow.png
    :alt: git-flow diagram
    :align: center
    :target: http://nvie.com/posts/a-successful-git-branching-model/
    :width: 50%

.. ifnotslides::

    Unfortunately we can't really prescribe a *best* Git workflow.  There are
    definitely better workflows out there, but you should do what works for
    you, and when you join a project explicitly ask what their workflow is so
    you can stay on the same page as your peers.


Centralizing Git
----------------

.. ifnotslides::

    While Git is *distributed* it can be made more centralized by pushing and
    pulling with a common *remote* repository. Tools for centralizing Git
    include:

Gitlab
    Open Source, free to run, feature rich.

Github
    Very popular. Not Open Source but free for Open Source projects.

Bitbucket
    Also popular, similar to Github, unlimited free private and public
    repositories.

Gitolite
    *Bare-bones*.  Fewer features than the previous three. Open Source, useful
    for learning the nitty-gritty on how Git *really* works.

.. ifnotslides::

    Each of these services is either free to use, or Open Source (so you can
    setup and run it yourself).


Cloning a Repository
~~~~~~~~~~~~~~~~~~~~

To contribute to someone else's repository you first need to *clone* the repo.

::

    $ cd /path/to/my/projects
    $ git clone <some git url>
    $ cd <new repo directory>
    $ ls

Once you clone a repository you can make as many local changes as you want
without affecting the original (central) copy. You can experiment and work
without the original owner even knowing what you're doing!


TODO: Cloning Exercise
~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    In this exercise we will clone an application and run it in our remote
    GNU/Linux box.

    First, clone the ``tinsy-flask-app`` repository from the DevOpsBootcamp
    organization on Github.

::

    $ cd ~
    $ git clone https://github.com/DevOpsBootcamp/tinsy-flask-app.git
    $ cd tinsy-flask-app

See http://git.io/vcVmB for more details about the ``tinsy-flask-app``
repository.

.. ifnotslides::

    After cloning we need to setup the project.  This is similar to building
    an application from source because we downloaded the source code and want
    to run it!

    Most repositories include a file called README which includes instructions
    on how to setup and run the code included in the repo.  Those instructions
    tell us to run the following commands.

    If you are using our docker image, you won't be able to access the webserver
    without adding a port forwarding rule for TCP port 8080 on the container,
    similar to how SSH is forwarded on the container.  See 'Setting up Docker'
    on the left for info on how to add port mappings to a docker container.

.. nextslide::

::

    #Setup python virtual environment
    $ virtualenv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements.txt
    #Run server
    (venv) $ python script.py
    #When finished, deactivate virtual environment
    (venv) $ deactivate
    $

.. ifnotslides::

    .. note::

        You may need to install the ``python``, ``virtualenv``, and ``pip``
        packages.  How would you do that?

    Now if you go to ``<your ip address>:<http port>`` in your web-browser to see
    a live version of the app!

.. ifslides::

    Now if you go to ``dobc-shell.osuosl.org:<http port>`` in your web-browser to see
    a live version of the app!

    Your ``<http port>`` is the same as your SSH port, but the first 2 numbers
    are changed from ``33`` to ``34``. For example, ``33005`` -> ``34005``


Further Reading
---------------

The `Online Git Docs`_
    This is a portal to all of the official docs on `git-scm.com`_.  It
    includes everything from *Getting Started* to *Git Internals*.  Check it
    out!

`Git workflow tutorial`_
    This is the tutorial provided on https://git-scm.com/about/distributed.
    It is a good high-level overview of some common git workflows.

`A successful Git branching model`_
    This blogpost describes a git workflow (git-flow) that the Open Source Lab
    bases their workflow on.

.. _Online Git Docs: https://git-scm.com/doc
.. _git-scm.com: https://git-scm.com
.. _Git workflow tutorial: https://git-scm.com/about/distributed
.. _A successful Git branching model:
        http://nvie.com/posts/a-successful-git-branching-model/
