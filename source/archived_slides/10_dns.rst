Introductory DNS
================

What is DNS?
------------

* Domain Name System
* Translates domains into ip addresses

  * Does many other types of records too

* Stored as a distributed Tree

Why is it Useful?
-----------------

* No remembering IP addresses
* load balancing!
* mx records for mail
* decouples domains from their addresses
* Extensible with new record types (and many have been added)

A Records
---------

They look like::

    osuosl.org.     300 IN  A   140.211.15.183

``osuosl.org.`` being the query, and ``140.211.15.183`` being the 'answer'
``300`` is the TTL (expiration time), ``IN A`` the type

* One can have more than one A record per domain

MX Records
----------

They look like::

    osuosl.org.     3600    IN  MX  5 smtp3.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp4.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp1.osuosl.org.
    osuosl.org.     3600    IN  MX  5 smtp2.osuosl.org.

* MX records have priority (in this example they are all the same)
* When sending email, the relay looks up the MX record and sends mail there.

NS Records
----------

They look like::

    osuosl.org.     86258   IN  NS  ns1.auth.osuosl.org.
    osuosl.org.     86258   IN  NS  ns2.auth.osuosl.org.
    osuosl.org.     86258   IN  NS  ns3.auth.osuosl.org.

* They inform where to direct DNS queries for a domain
* Point to other domains (which have A records)

NXDOMAIN Records
----------------

* Tell you there is no answer to a query::

    Host something.invalid.osuosl.org not found: 3(NXDOMAIN)

* Some ISPs and others never serve NXDOMAINS

  * Instead they point you at themselves

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
* Information at `http://www.root-servers.org`
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

resolv.conf
-----------

resolv.conf has ``nameserver`` entries which tell which dns servers to use::

    nameserver 140.211.166.130
    nameserver 140.211.166.131

Most distributions provide a package that manages resolv.conf entries when using dhcp (typically called resolvconf)
