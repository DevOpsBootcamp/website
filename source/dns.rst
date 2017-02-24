.. _dns:


Lesson 16: DNS
==============

============= ============= ============= ==========
`Homepage`_   `Content`_    `Slides`_     `Video`_
============= ============= ============= ==========

.. _Homepage: http://devopsbootcamp.osuosl.org
.. _Content: http://devopsbootcamp.osuosl.org/dns.html
.. _Slides: http://slides.osuosl.org/devopsbootcamp/dns.html
.. _Video:

.. warning::

    This lesson is under construction.  Use it for learning purposes at your
    own peril.

    If you have any feedback, please fill out our `General Feedback Survey`_.

.. _General Feedback Survey: https://goo.gl/forms/RyVZkJnownLKu8VI3


.. ifnotslides::

    .. contents:: Overview

.. ifslides::

    Overview
    --------

    - What DNS Solves.
    - History Lesson
    - DNS Records

        - A
        - MX
        - NS
        - SOA
        - CNAME
        - NXDOMAIN

    - Root / The Thirteen

Problems DNS Solves
-------------------

.. image:: /static/xkcd-google-dns.png
    :target: https://xkcd.com/1361/
    :alt: XKCD Google DNS Comic
    :align: center

.. ifnotslides::
    The Domain Name System (DNS) translates human-readable URLs
    (devopsbootcamp.osuosl.org) into computer IP addresses (140.211.15.183).

    It works by storing records in a distributed tree-like hierarchy.  It was
    designed like this because it scales well.

.. ifslides::

    ::

        devopsbootcamp.osuosl.org ===(DNS)===> 140.211.15.183


Obligatory History Lesson
~~~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    To really explain DNS you need to understand the history of the entire
    internet.  Unfortunately we don't have time for *that* but we can do a
    quick overview.

    The pre-cursor to the *Internet* was *ARPANET*.  To use ARPANET people had
    to remember addresses for each machine they wanted to connect to *(1 was
    MIT, 2 was Yale, 3 was Harvard, 4 was AT&T for example)*, similar to
    modern IP addresses or Phone Numbers.

    Since numbers are hard to remember, people shared a file called
    ``HOSTS.TXT`` which was a mapping between computer addresses and common
    aliases.

::

    MIT         1
    Yale        2
    Harvard     3
    ATT         4

.. ifnotslides::

    This worked but did not scale well with the ‘net, as you can imagine
    **(think: Sharing a word document with 500 friends, all making changes)**.

::

    ...
    joeBillson  14895
    susan-gill  15832

.. ifnotslides::

    Back between 1983 - 1987 a lot of really smart people in a lot of smart
    Universities and Organizations developed DNS to solve this problem.  There
    have since been many implementations of the DNS protocol, and additions to
    it's functionality, but the core design is about the same.


How DNS Works
-------------

.. ifnotslides::

    To explain how DNS works, let's work through a simple example of *how* a
    computer finds the address of a computer based on it's name.

#. Computer **A** wants to fetch data from ``devopsbootcamp.osuosl.org.``
   (notice the ``.``  at the end of the address).

#. Computer **A** checks the local cache.

#. If the address isn't in the cache, **A** contacts the DNS ``root`` server.
   (We're actually skipping a few layers of cache. Read up for more info on
   that.)

#. One of the ``root`` nodes tells **A** to check the ``org`` node.

#. The ``org`` node is contacted and tells **A** to check the ``osuosl`` node.

#. The ``osuosl`` node tells it to check the ``devopsbootcamp`` node.

.. ifnotslides::

    This tries to demonstate the fact that DNS starts by checking it's cache,
    then starts at the top of the DNS *tree* and works it's way down.  Each
    server has authority over a certain domain and directs traffic to the next
    step down.


A DNS Request
-------------

.. ifnotslides::

    To further elaborate, because DNS really does need a lot of examples to
    make sense, here is a DNS request from a different angle.

    #. A computer makes a request for ``http://osuosl.org.``.
    #. This request gets sent to the ``root`` (``.``) of the DNS tree.
    #. The root sends it off to the ``org`` (top level domain) branch.
    #. The ``org`` node sends it off to the ``osuosl`` (domain) branch.
    #. The ``osuosl`` node sends it to the ``devopsbootcamp`` (subdomain) branch.

.. image:: /static/dns-example.png
    :align: center
    :alt: An example DNS request
    :target: https://en.wikipedia.org/wiki/File:An_example_of_theoretical_DNS_recursion.svg


DNS Records
-----------

.. ifnotslides::

    There are a few core types of DNS records, each surving their own purpose.

======== =================================
Acronym  Name
-------- ---------------------------------
A, AAAA  IP Addresses
MX       SMTP Mail Exchangers
NS       Name Servers
SOA      DNS Zone Authority
PTR      Pointers for Reverse DNS Lookups
CNAME    Domain Name Aliases
======== =================================


A Records
~~~~~~~~~

    The ``A`` record is used to map an IP address to a domain name.  This is as
    close to a 'regular' record as you can get.

.. ifnotslides::

    ``AAAA`` records are the same as ``A`` records, except that they map to
    IPv6 (``xx:xx:xx:xx:xx:xx``) addresses instead of IPv4
    (``xxx.xxx.xxx.xxx``) addresses.

    One can have more than one A record per domain

::

    osuosl.org.     300 IN  A   140.211.15.183

.. ifnotslides::

    In the following example,  ``osuosl.org.`` is the query, and
    ``140.211.15.183`` is the ‘answer’. 300 is the TTL (expiration time), and
    ``IN A`` is the type


MX Records
~~~~~~~~~~

    The ``MX`` record is for tracking mail servers.

.. ifnotslides::

    When you send an email to *someuser@example.org* the mail program does a
    lookup for the MX record of example.org. Multiple MX records can have
    separate priority (in this example they are all the same).

::

    osuosl.org.     3600    IN  MX  5 smtp3.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp4.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp1.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp2.osuosl.org.


NS Records
~~~~~~~~~~

    Servers with a ``NS`` record are allowed to speak with authority on a
    domain and DNS requests.

.. ifnotslides::

    ``NS`` records are the type of record identifying nodes in the DNS
    hierarchy instead of just the websites DNS maps.

    NS records point to other domains (which have ``A`` records).

::

    osuosl.org.     86258   IN  NS  ns1.auth.osuosl.org.
    osuosl.org.     86258   IN  NS  ns2.auth.osuosl.org.
    osuosl.org.     86258   IN  NS  ns3.auth.osuosl.org.


SOA (Authority) Records
~~~~~~~~~~~~~~~~~~~~~~~

    ``SOA`` is the record for proving authority over a site or zone.

.. ifnotslides::

    For example, the head of the ``org`` heirarchy has a ``SOA`` record proving
    its authority over ``org`` websites.

    - A DNS server is authoritative if it has a Start of Authority (SOA) record for
      a domain
    - The root-servers contain SOA records for the TLDs and gTLDs
    - The NS servers for each (g)TLD contain SOA records for each registered domain
    - ... and so on...

::

    osuosl.org.     86400   IN  SOA ns1.auth.osuosl.org. ...


CNAME Records
~~~~~~~~~~~~~

    ``CNAME`` is an record for aliasing old names to redirect to new names.

::

    bar.example.com.  86400  IN  CNAME  foo.example.com


NXDOMAIN Records
~~~~~~~~~~~~~~~~

Tells you there is no answer to a query:

::

    Host something.invalid.osuosl.org not found: 3(NXDOMAIN)

Some ISPs and others never serve NXDOMAINS, instead they point you at
themselves.


The Root
--------

.. ifnotslides::

    Because DNS is setup in a Hierarchy there has to be a *top*.  We call the
    *top* the *root* of the *DNS tree*.

::

    $ dig ns .
    ;; ANSWER SECTION:
    .           512297  IN  NS  i.root-servers.net.
    .           512297  IN  NS  e.root-servers.net.
    .           512297  IN  NS  d.root-servers.net.
    .           512297  IN  NS  j.root-servers.net.
    .           512297  IN  NS  b.root-servers.net.
    .           512297  IN  NS  a.root-servers.net.
    .           512297  IN  NS  f.root-servers.net.
    .           512297  IN  NS  h.root-servers.net.
    .           512297  IN  NS  g.root-servers.net.
    .           512297  IN  NS  c.root-servers.net.
    .           512297  IN  NS  m.root-servers.net.
    .           512297  IN  NS  k.root-servers.net.
    .           512297  IN  NS  l.root-servers.net.


The Thirteen
~~~~~~~~~~~~

.. ifnotslides::

    Because it is very time consuming to make a DNS request across the world
    there are actually 13 DNS root servers spread out across the world.

    Each runs on as few as 1 (USC) servers, or as many as 155 (ICANN)

.. image:: /static/hedgehog.png
    :alt: The Thirteen traffic throughout the day
    :align: center
    :target: http://stats.dns.icann.org/hedgehog/

.. ifnotslides::

    - Information Sciences Institute - USC
    - Cogent Communications
    - University of Maryland
    - NASA
    - Internet Systems Consortium
    - USA DOD
    - USA Army
    - Netnod (Autonomica) - Sweden
    - RIPE NCC
    - ICANN
    - WIDE - Japan


Tool: dig
---------

``dig`` is a command-line tool for performing DNS lookups.

Syntax:

::

    dig @server name type

Examples:

::

    dig @ns1.osuosl.org osuosl.org A

.. ifnotslides::

    This queries the nameserver ``ns1.osuosl.org`` for DNS records relating to
    ``osuosl.org`` of type ``A`` (IPv4 Address)


Example: Recursive Request
--------------------------

.. ifnotslides::

    In this example we follow the path that your browser uses to find the
    location of a sever given the domain name.

    **Quick note** this example completely ignores caching, which is a very big
    part of DNS lookups.  This is a *pure* view of a DNS lookup, *sans-cache*.

First we query a NS record for ``.``:

::

    $ dig ns .
    ;; QUESTION SECTION:
    ;.              IN  NS

    ;; ANSWER SECTION:
    .           518400  IN  NS  i.root-servers.net.
    .           518400  IN  NS  a.root-servers.net.
    .           518400  IN  NS  l.root-servers.net.
    .           518400  IN  NS  f.root-servers.net.
    .           518400  IN  NS  b.root-servers.net.

    etc...

.. nextslide::

Next we query ``NS`` for ``org.``:

::

    $ dig ns com. @a.root-servers.net
    ;; QUESTION SECTION:
    ;org.               IN  NS

    ;; AUTHORITY SECTION:
    org.            172800  IN  NS  a0.org.afilias-nst.info.
    org.            172800  IN  NS  a2.org.afilias-nst.info.

    etc...

    ;; ADDITIONAL SECTION:
    a0.org.afilias-nst.info. 172800 IN  A   199.19.56.1

    etc...

.. nextslide::

Next we query ``NS`` for ``osuosl.org.``:

::

    $ dig ns osuosl.org. @199.19.56.1
    ;; QUESTION SECTION:
    ;osuosl.org.            IN  NS

    ;; AUTHORITY SECTION:
    osuosl.org.     86400   IN  NS  ns3.auth.osuosl.org.
    osuosl.org.     86400   IN  NS  ns2.auth.osuosl.org.
    osuosl.org.     86400   IN  NS  ns1.auth.osuosl.org.

    ;; ADDITIONAL SECTION:
    ns1.auth.osuosl.org.    86400   IN  A   140.211.166.140
    ns2.auth.osuosl.org.    86400   IN  A   140.211.166.141
    ns3.auth.osuosl.org.    86400   IN  A   216.165.191.53

.. nextslide::

Next we query ``A`` for ``osuosl.org.``:

::

    $ dig a osuosl.org. @140.211.166.140
    ;; QUESTION SECTION:
    ;osuosl.org.            IN  A

    ;; ANSWER SECTION:
    osuosl.org.     300 IN  A   140.211.15.183

    ;; AUTHORITY SECTION:
    osuosl.org.     86400   IN  NS  ns1.auth.osuosl.org.
    osuosl.org.     86400   IN  NS  ns2.auth.osuosl.org.
    osuosl.org.     86400   IN  NS  ns3.auth.osuosl.org.

    ;; ADDITIONAL SECTION:
    ns1.auth.osuosl.org.    86400   IN  A   140.211.166.140
    ns2.auth.osuosl.org.    86400   IN  A   140.211.166.141
    ns3.auth.osuosl.org.    3600    IN  A   216.165.191.53

.. ifnotslides::

    And there you have it!  We have successfully traversed the DNS tree to find
    osuosl.org.  Of course there is a lot of cache involved so the process is
    much faster than this, but it's good to practice anyway.


TODO: Traverse the DNS Tree with ``dig``
----------------------------------------

Can you traverse the DNS tree to get to these websites? Give it a try!

    - github.com
    - web.archive.org
    - en.wikipedia.org


Further Reading
---------------

.. TODO: Add further reading

- Try running ``dig`` on some of your favorite websites and see what you find.
- Read the manpage on ``dig`` and see what else you can find in the output.
- Try registering your own domain name and run a website using the `Github
  Student Pack`_ resources like Digital Ocean and DNSimple.

.. _Github Student Pack: https://education.github.com/pack
