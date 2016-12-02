.. _continuous_integration:


Lesson 12: Continuous Integration
=================================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/continuous-integration.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/continuous-integration.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What Is CI?
    - Automated Testing
    - Tools:
      - Travis CI
      - Jenkins


Continuous Integration
----------------------

.. image:: /static/continuous-integration.png
    :align: center
    :target: http://www.agilenutshell.com/continuous_integration
    :alt: Rough diagram of CI workflow

.. ifnotslides::

    Continuous Integration is a name for any kind of automated tool that
    performs the following tasks:

    #. Detects changes to your project
    #. Runs a suite of tests on the changed code
    #. Alerts the people that care if something good/bad happened

    CI tools are also known to do a slew of other things:

    - Builds and releases new versions of a package when they're needed
    - Builds documentation and other parts of a project with each new release


Automated Testing
-----------------

.. image:: /static/automated-testing.png
    :alt: Automated Testing integrated into Github
    :align: center

.. ifnotslides::

    Automated testing is the most common, and easiest to setup, CI tool.
    It integrates with Github (Or whatever service you're using to host your
    code), and can be set up to detect changes to a codebase (new Pull Request,
    new branch, new commit on master/develop, etc). When it's triggered, it
    runs your tests automatically.  If it finds a problem, it will notify the
    correct people, usually via email.


Tool: Travis CI
---------------

.. image:: /static/travis.png
    :align: right
    :alt: Travis CI logo
    :target: https://travis-ci.org
    :width: 50%

.. ifnotslides::

    Travis CI is very popular among Github users because it is easy to setup
    with Github projects and integrates well with Github workflows.  It's
    also free for Open Source projects, although the service itself is not
    Open Source.

Runs test suites for:

- C / C++
- Java
- Javascript
- Python
- Ruby
- *Many* more on `the Travis CI docs`_!

.. _the Travis CI docs: https://docs.travis-ci.com/


Tool: Jenkins
-------------

.. ifnotslides::

    Jenkins is a more powerful version of Travis, but as a result is more
    complicated to use and set up.  While you can pay to use a public instance
    of Jenkins, it is more common to run your own instance of Jenkins.

- Does pretty much anything you can tell a computer to do, automatically.
- Builds and uploads binaries (releases).
- Runs tests.
- Reports build successes/failures.
- Also has plugins!

TODO: Setup Travis on a GH Repo
-------------------------------

.. ifnotslides::

    We've spent the past two lessons building and testing a web app. Now, let's
    upload it to Github and set up CI on it. First, if you haven't already,
    create a `Github`_ account.

    Once you've done that, go to "Create New" in the upper right corner of the
    page and click on "New Repository". Fill the fields out using these values:

    .. image:: /static/gh-repository.png
        :align: center
        :alt: Creating a new Github repository
        :width: 80%

    - **Repository name**: You can put anything you want here!
    - **Description**: You can also put anything you want here!
    - **Public**: Check this field
    - **Initialize this repository**: Check this field as well
    - **Add .gitignore**: Python
    - **Add a license**: Apache License 2.0

    Click "Create repository" and you will be taken to your newly created
    repository. Next, click "Clone or download" and copy the URL inside the
    textbox. Inside your command line, run ``git clone <url_you_copied>`` to
    make a clone of your repository.

    Copy the contents of the "Frameworks" exercise directory into the cloned
    repository, then add them to Git with ``git add -A`` and commit them with
    ``git commit``. To push your code to Github, use
    ``git push origin master``. Refresh the repository in your web browser to
    check that your code was successfully pushed.

    Next, go to the `Travis CI`_ website and click on "Sign in with GitHub".
    This will automatically sync all of your Github repositories to Travis.
    Go to your profile and locate your repository, then click on the button to
    enable Travis.

    To finish setting up Travis on our respository, we have to add a
    ``.travis.yml`` file. Travis will look for this file in your repository
    whenever it runs and use it to set configuration options. There are
    detailed guides and examples for a variety of languages in the Travis
    documentation, but for our project we're going to put this in the
    ``.travis.yml`` file:

    .. code-block:: yml

        language: python

        python:
            - "2.7"

        install:
            - pip install -r requirements.txt

        script:
            - python run_tests.py

    Add and commit the file, then push it to Github once more. If everything
    was set up correctly, you should see Travis trigger automatically and start
    testing your app.

.. _Github: https://github.com
.. _Travis CI: https://travis-ci.org


Further Reading
---------------

`Jenkins Documentation`_
    The Jenkins project documentation.  If you need a broad overview read the
    *Getting Started with...* docs.

`TravisCI Documentation`_
    If you end up working on a large project on GitHub you're going to
    interface with TravisCI sooner or later.

`CircleCI Documentation`_
    CircleCI is a tool we didn't get to touch on.  It is very similar to
    Travis.

.. _Jenkins Documentation: https://jenkins.io/doc/
.. _TravisCI Documentation: https://docs.travis-ci.com/
.. _CircleCI Documentation: https://circleci.com/docs/
