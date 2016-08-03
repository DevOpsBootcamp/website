.. _cloud_infrastructure:


Lesson 19: Cloud Infrastructure
===============================

========= =====================================================================
Homepage  http://devopsbootcamp.osuosl.org
Content   FILL THIS IN
Slides    FILL THIS IN
Video     FILL THIS IN
========= =====================================================================

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
    - Cattle VS Pets
 

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

    The software which powers *The Cloud* is vast, but a few of the big names
    are **Amazon AWS, Windows Azure, CoreOS Tectonic, and Openstack**.  Some
    of these are cheap, fast, new, old, but each offer it's own set of
    advantages.


Advantages over Bare Hardware
-----------------------------

.. ifnotslides::

    In the Stone Ages you used to buy a computer, install an OS on it, give it
    an IP address, and then you had a website.  This worked for some people,
    and small projects, but it doesn't scale well.

    Let's propose a hypothetical: You are Netflix.  You have times when lots
    of people are watching your shows, and other times when very few people
    are watching shows.  You somehow need to be able to have enough servers
    for lots of people to watch, but you don't want to waste resources when
    *nobody* is watching.  The solution? Use the cloud!

    Netflix uses AWS, a cloud provider, to add and remove servers from its
    clusters as they're needed.  This means they pay a lot of money on
    Saturday night when people are inside watching Stranger Things, and they
    pay very little Wednesday morning when people are at work.

    The reasons you would use the cloud is because you need something that
    either needs to scale fast, be cost effective, or will only exist for a
    short period of time.

    **TLDR:** Here is why you'd want to use The Cloud: 

- **Ephemeral:** Creating and Destroying operating systems is quick and
  painless.

- **Cost effective:** Pay for what you use.

- **Low startup cost:** Initial investment is cheap, <$100 as opposed to
  >$1,000+. (unless you are running a private cloud, more on that in a
  second).  


Private Clouds
--------------

.. ifnotslides::

    Private clouds are software which you run on your own servers.  They give
    you the advantages of cloud flexiblity while giving you the control over
    the machines you run.

    This requires a higher startup cost, requiring the purchase of machines
    and time to install the cloud software, but then you don't have to
    worry about your cloud usage being restricted during peak hours.


Public Clouds
-------------

.. ifnotslides::

    Public clouds are services you subscribe to which allow you to run and rent
    server-space on somebody else's cloud.  This is cheap and easy to work
    with, but may be restricted during times of heavy use.


Cloud + Configuration Management
--------------------------------

.. ifnotslides::

    Configuration Management is a very useful tool in using the Cloud as a
    developer.  Being able to spin up hundreds of machines isn't useful if you
    have to manually set each one up to run your application.  Many companies
    use some form of configuration management to provision their cloud-based
    boxes automatically.


Cattle VS Pets
--------------

.. ifnotslides::

    This is where the metaphors of Cattle vs Pets (from
    :ref:`configuration_management`) makes more sense.  As we mentioned,
    servers ought to be treated like Cattle.  With a cloud resource provdier a
    limitless number cattle can be spun up and destroyed.  Without *The Cloud*
    you can probably get away with treating your severs like pets.


Advantages
~~~~~~~~~~

.. TODO: Fill this section out.


Disadvantages
~~~~~~~~~~~~~

.. TODO: Fill this section out.


TODO
----

.. TODO: Add activity.


Further Reading
---------------

.. TODO: Add further reading.
.. Suggestion:
   - Docs on Open Stack
   - Docs on AWS
   - Something about starting with The Cloud.
