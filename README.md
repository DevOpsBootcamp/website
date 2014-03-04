DevOps Bootcamp Website & Curriculum
====================================

The site is hosted at
[devopsbootcamp.osuosl.org](http://devopsbootcamp.osuosl.org/en/latest/). 

This repository has a post-commit hook set up to update the main site every
time the master branch is changed. If the site doesn't update within a couple
of minutes, the build may have failed. Check that `make html` doesn't throw
any errors in your copy of the repo, and ask someone with admin access on
readthedocs to investigate what it reports is broken.

Viewing Slides: 
---------------

Slides are available on http://slides.osuosl.org/devopsbootcamp/ , and rebuild
automatically whenever new content is pushed to the master branch of this repo.

The script in scripts/build.sh automatically removes the slides that were built
of non-slides content, based on the assumption that the filenames of all actual 
slides start with the week number.   

You can also build the slides locally if you've been editing them and want to
see how they'll look before you push, or if you don't have push access to the
project: 

    $ sudo pip install virtualenv
    $ git clone https://github.com/DevOpsBootcamp/website.git
    $ virtualenv website
    $ cd website
    $ source bin/activate # enter the virtual environment
    $ pip install -r requirements.txt

    # output lives in build/ and the stuff you want to edit is in source/
    # images and things go in source/static/

    $ make slides # slides will go to build/slides
    $ make html # to preview roughly how it'll look on readthedocs

    $ deactivate # leave the virtual environment


