Introduction to DNS
===================

What it is and how it makes the internet *go*.

What is DNS?
------------

    The Domain Name System (DNS) is a hierarchical distributed naming system
    for computers, services, or any resource connected to the Internet or a
    private network.

* The ``Domain Name System``
* Translates human readable words like ``devopsbootcamp.osuosl.org`` into
  computer addresses like ``140.211.15.183`` *
* Stores ``records`` in a distributed tree (more on that later).
* Wildcard handling like ``*.osuosl.org``..


What does it solve?
-------------------

Do you want to remember 140.211.15.183? You do? Weirdo...

* No remembering IP addresses.
* Load Balancing.
* Scales well.

.. figure:: /static/xkcd-google-dns.png
   :align: center
   :target: http://xkcd.com/1361/

Obligatory History Lesson
-------------------------

Back around ARPANET we used to have to remember things like 140.211.15.183 (1
was MIT, 2 was Yale, 3 was Harvard, 4 was AT&T for example).

Numbers are hard to remember so they created and shared a file called HOSTS.TXT
which aliased names with corresponding numbers.

This worked but didn't scale well with the 'net, as you can imagine (think:
Sharing a word document with 500 friends, all making changes).

Back between 1983 - 1987 a lot of really smart people in a lot of smart
Universities and Organizations developed DNS to solve this problem.

How does it work
----------------

#. Computer A wants to fetch data from devopsbootcamp.osuosl.org (notice
   the ``.`` at the end of devopsbootcamp.osuosl.org)

#. Computer A checks it's local cache.

#. If no cache was found it contacts the DNS root server.

    * There are a few layers of cache checked on the way. Read up for more
      info on that.

#. The root node tells A to check the ``org`` node.

#. The ``org`` node is contacted and tells A to check the ``osuosl`` node.

#. The ``osuosl`` node tells it to check the ``devopsbootcamp`` node.

The DNS Tree
------------

.. figure:: /static/dns-graph.png
    :align: center
    :target: https://en.wikipedia.org/wiki/File:Domain_name_space.svg

A DNS Request *
---------------

#. A computer makes a request for ``http://osuosl.org.``.
#. This request gets sent to the root (``.``) of the DNS tree.
#. The root sends it off to the ``org`` (top level domain) branch.
#. The ``org`` node sends it off to the ``osuosl`` (domain) branch.
#. The ``osuosl`` node sends it to the ``devopsbootcamp`` (subdomain) branch.

\* **sans caching**

.. figure:: /static/dns-example.png
   :align: center
   :target: https://en.wikipedia.org/wiki/File:An_example_of_theoretical_DNS_recursion.svg

Records
-------

There are many types of DNS records. Here are a few:

================================= =========
Name                              Acronym
================================= =========
IP Addresses                      A, AAAA
SMTP Mail Exchangers              MX
Name Servers                      NS
DNS Zone Authority                SOA
Pointers for Reverse DNS Lookups  PTR
Domain Name Aliases               CNAME
================================= =========

A Records
---------

They look like::

    osuosl.org.     300 IN  A   140.211.15.183

``osuosl.org.`` being the query, and ``140.211.15.183`` being the 'answer'
``300`` is the TTL (expiration time), ``IN A`` the type

*One can have more than one A record per domain*

MX Records
----------

They look like::

    osuosl.org.     3600    IN  MX  5 smtp3.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp4.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp1.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp2.osuosl.org.

*MX records have priority (in this example they are all the same)*

*When sending email, the relay looks up the MX record and sends mail there.*

NS Records
----------

They look like::

    osuosl.org.     86258   IN  NS  ns1.auth.osuosl.org.
    osuosl.org.     86258   IN  NS  ns2.auth.osuosl.org.
    osuosl.org.     86258   IN  NS  ns3.auth.osuosl.org.

*They inform where to direct DNS queries for a domain*

*Point to other domains (which have A records)*

NXDOMAIN Records
----------------

Tells you there is no answer to a query::

    Host something.invalid.osuosl.org not found: 3(NXDOMAIN)

*Some ISPs and others never serve NXDOMAINS, instead they point you at
themselves*

The Root
--------

``.`` is the root of the DNS tree::

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
------------

Thirteen Nameservers

* ``[a-m].root-servers.net``
* Information at http://www.root-servers.org
* a, j are run by Verisign

The Thirteen
------------

  * Information Sciences Institute - USC
  * Cogent Communications
  * University of Maryland
  * NASA
  * Internet Systems Consortium
  * USA DOD
  * USA Army
  * Netnod (Autonomica) - Sweden
  * RIPE NCC
  * ICANN
  * WIDE - Japan

The Thirteen
------------

* Typically use Anycast
* Each runs on as few as 1 (USC) servers, or as many as 155 (ICANN)

.. figure:: /static/hedgehog.png
   :align: center

Authoritative (SOA)
-------------------

* A DNS server is **authoritative** if it has a Start of Authority (SOA) record for a domain
* The root-servers contain SOA records for the TLDs and gTLDs
* The NS servers for each (g)TLD contain SOA records for each registered domain
* and so on...

Recursive Example
-----------------

First we query a **NS** record for **.**::

    $ dig ns .
    ;; QUESTION SECTION:
    ;.              IN  NS

    ;; ANSWER SECTION:
    .           518400  IN  NS  i.root-servers.net.
    .           518400  IN  NS  a.root-servers.net.
    .           518400  IN  NS  l.root-servers.net.
    .           518400  IN  NS  f.root-servers.net.
    .           518400  IN  NS  b.root-servers.net.
    .           518400  IN  NS  d.root-servers.net.
    .           518400  IN  NS  k.root-servers.net.
    .           518400  IN  NS  g.root-servers.net.
    .           518400  IN  NS  h.root-servers.net.
    .           518400  IN  NS  m.root-servers.net.
    .           518400  IN  NS  e.root-servers.net.
    .           518400  IN  NS  c.root-servers.net.
    .           518400  IN  NS  j.root-servers.net.

Recursive Example
-----------------

Next we query **NS** for **org.**::

    $ dig ns com. @a.root-servers.net
    ;; QUESTION SECTION:
    ;org.               IN  NS

    ;; AUTHORITY SECTION:
    org.            172800  IN  NS  a0.org.afilias-nst.info.
    org.            172800  IN  NS  a2.org.afilias-nst.info.
    org.            172800  IN  NS  b0.org.afilias-nst.org.
    org.            172800  IN  NS  b2.org.afilias-nst.org.
    org.            172800  IN  NS  c0.org.afilias-nst.info.
    org.            172800  IN  NS  d0.org.afilias-nst.org.

    ;; ADDITIONAL SECTION:
    a0.org.afilias-nst.info. 172800 IN  A   199.19.56.1
    a2.org.afilias-nst.info. 172800 IN  A   199.249.112.1
    b0.org.afilias-nst.org. 172800  IN  A   199.19.54.1
    b2.org.afilias-nst.org. 172800  IN  A   199.249.120.1
    <truncated>

Recursive Example
-----------------

Next we query **NS** for **osuosl.org.**::

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

Recursive Example
-----------------

Next we query **A** for **osuosl.org.**::

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

Recursive Example
-----------------

That was a lot of work, so we have dns caches to help us:

  * bind
  * unbound
  * dnscache ({n,}djbdns)


CNAME Records
-------------

Canonical Name is the thing pointed at, query is what points to it::

    ;; QUESTION SECTION:
    ;www.osuosl.org.          IN A

    ;; ANSWER SECTION:
    www.osuosl.org.     86399 IN CNAME web1.osuosl.org.
    web1.osuosl.org.    86400 IN A     140.211.15.183

CNAME Records
-------------

* Query for A, get A record.

* Query for CNAME, get the canonical name (NOT the ip address)

You can run a DNS server
------------------------

Because DNS is distributed you can run your own DNS server and handle DNS
requests.

Some things to look up in addition to 'how do I run my own DNS server?':

* ``tinydns``
* ``bind``

Further Reading / Activitys
---------------------------

#. Try running ``dig`` on some of your favorite websites and see what you find.
#. Read the manpage on ``dig`` and see what else you can find in the output.
#. Try registering your own domain name and run a website using the `Github
Student Pack`_ resources like Digital Ocean and DNSimple.

.. _Github Student Pack: https://education.github.com/pack


