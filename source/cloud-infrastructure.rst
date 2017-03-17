.. _cloud_infrastructure:


Lesson 19: Cloud Infrastructure
===============================

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/cloud-infrastructure.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/cloud-infrastructure.html
.. _Video:

.. include:: unfinished.txt


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What the Cloud Looks Like
    - Advantages over Bare Hardware
    - Private Clouds
    - Public Clouds
    - Cloud + Configuration Management
    - Advantages and Disadvantages


What the Cloud Looks Like
-------------------------

    *[...] a model for enabling ubiquitous, on-demand access to a shared pool of
    configurable computing resources.*

.. image:: /static/cloud_infra_shapes_and_sizes.png
    :align: center
    :alt: A series of Cloud Platform logos
    :width: 70%

.. ifnotslides::

    *The Cloud* is a vague term which more or less means "Computing resources
    somewhere else".  This can be remote digital storage, a virtual machine
    you log into from your laptop, a place to chat with friends, or a database
    someone else hosts.  Either way its *many* tools acting together in a
    complicated ecosystem of machines, web APIs, operating systems, and
    hosting providers.

    Some of the biggest cloud providers currently are
    **Amazon AWS, Windows Azure, and Google Cloud Platform**.


Advantages over Bare Hardware
-----------------------------

.. ifnotslides::

    In the Stone Ages you used to buy a computer, install an OS on it, give it
    an IP address, and then you had a website.  This worked for some people,
    and small projects, but it doesn't scale well.

    Let's propose a hypothetical scenario: You are Netflix.  You have times
    when lots of people are watching shows, and other times when very few
    people are watching shows.  You somehow need to be able to have enough
    servers for lots of people to watch, but you don't want to waste resources
    when *nobody* is watching.  The solution? Use the cloud!

    Netflix uses AWS, a cloud provider, to add and remove servers from its
    clusters as they're needed.  This means they pay a lot of money on
    Saturday night when people are inside watching movies, and they pay very
    little Wednesday morning when people are at work.

    The reasons you would use the cloud is because you need something that
    either needs to scale fast, be cost effective, or will only exist for a
    short period of time.


Private Clouds
--------------

.. ifnotslides::

    Private clouds are software which you run on your own servers.  They give
    you the advantages of cloud flexiblity while giving you the control over
    the machines you run.

    This requires a higher startup cost, requiring the purchase of machines
    and time to install the cloud software, but then you don't have to
    worry about your cloud usage being restricted during peak hours. In
    addition, it's more cost-effective in the long run. Once all the equipment
    is bought and set up you just have to pay the cost of running and
    maintaining it instead of having to pay money to another company so they can
    both maintain it and make a profit.


Public Clouds
-------------

.. ifnotslides::

    Public clouds are services which allow you to run and rent server-space on
    somebody else's cloud.  This is cheap to start and easy to work with, but
    may be more expensive in the long run and restricted during times of heavy
    use.


Cloud + Configuration Management
--------------------------------

.. ifnotslides::

    Configuration Management is a very useful tool for managing lots of machines
    at once in the cloud.  Being able to spin up hundreds of machines isn't
    practical if you have to manually configure each one. Many companies use
    configuration management tools to provision their cloud machines
    automatically.


Advantages
----------

Running your software on a cloud is:

- **Ephemeral**

.. ifnotslides::

    Creating and destroying machines is quick and painless. If you need to
    quickly spin up 100 new Linux boxes to run a test, you can do that and then
    delete them afterwards with a few commands.

- **Cost effective**

.. ifnotslides::

    Since you only pay for the resources that you're currently using, clouds
    can be very cost effective. Instead of worrying about upgrading your servers
    in order to handle increased load at peak hours, you can just spin up new
    machines as needed and only pay for the exact amount of extra capacity that
    you need.

- **Low startup cost**

.. ifnotslides::

    Initial investment is cheap, <$100 as opposed to >$1,000+ (unless you are
    running a private cloud). This can be especially beneficial to startups,
    since they don't have to worry about spending the money and taking the time
    to set up costly infrastructure.


Disadvantages
-------------

Clouds can be great tools, but they have some disadvantages:

- **Central Point of Failure**

.. ifnotslides::

    Have you ever had trouble one day trying to visit your favorite websites
    but you were unable to reach them? Afterwards, you might have heard that it
    was because "AWS was down". AWS (Amazon Web Services) is one of the major
    backbones of the internet that hosts many popular websites and services.
    However, it has caused the internet to become increasingly centralized.
    If someone at Amazon makes a mistake and brings an important part of AWS
    down, half of the internet goes with it.

.. TODO: Add more here


TODO
----

.. TODO: Add activity.


Further Reading
---------------

AWS provides a *lot* of services, not all of which are named very well.
`This article`_ explains what each service does in plain English.

.. _This article: https://www.expeditedssl.com/aws-in-plain-english

.. TODO: Add further reading.
.. Suggestion:
   - Docs on Open Stack
   - Docs on AWS
   - Something about starting with The Cloud.
