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

.. TODO: Add an activity.

.. Something like: Fork a devopsbootcamp repo, setup traivs on it, check your
.. status, etc.
.. I suggest building off of whatever project that was done in the 'testing'
.. lesson.


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
