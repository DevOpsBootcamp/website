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

Slides aren't displayed on readthedocs yet, because it doesn't play nicely
with Hieroglyph by default. The long-term solution is to make readthedocs
build the project in a virtualenv with Hieroglyph installed; the short-term
one is to simply build the slides yourself. 

Building the slides is also necessary if you've been editing them and want to
see how they'll look before you push. 

    $ sudo pip install sphinx
    $ sudo pip install hieroglyph
    $ git clone https://github.com/DevOpsBootcamp/website.git
    $ cd website

    # output lives in build/ and the stuff you want to edit is in source/
    # images and things go in source/static/

    $ make slides # slides will go to build/slides
    $ make html # to preview roughly how it'll look on readthedocs



