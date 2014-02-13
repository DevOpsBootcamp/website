===================================
Lesson 8: Security & Authentication
===================================

.. note::

    edunham
    - basic concepts & philosophies
        - authentication vs authorization
        - identity (persistent vs authoritative(?))
        - system security (close ports, firewalls, fail2ban)
            - process isolation
        - principle of least authority
            - users/groups/permissions
        - passwords/hashing (plaintext -> hash -> salt)

    Pono
    - key pairs
    - ssh keys (passphrase vs none; automation; authorized_keys)
    - GPG keys, signing stuff, publishing to keyservers
    - certificates (SSL/TLS)

    Jack???? (else dean/emily/ken w/ emily presenting)
    - web app security
        - parameterize or sanitize inputs
        - SQL injection
        - XSS, csrf tokens
        - https://www.owasp.org/index.php/Top_10_2013-Top_10
        - filesystem & user permissions (remember lesson 2?)

    - mention social engineering type attacks

What is security?
=================

se·cu·ri·ty

siˈkyo͝oritē/

noun

* the state of being free from danger or threat.
* the safety of a state or organization against criminal activity such as terrorism, theft, or espionage.
* procedures followed or measures taken to ensure the safety of a state or organization.
* the state of feeling safe, stable, and free from fear or anxiety.

Types of security
-----------------

* Physical security
* Software security
* Network security
    * Active vs. passive

.. figure:: static/xkcd_416.png
    :align: center

Authentication vs. Authorization
--------------------------------

.. figure:: static/xkcd_1121.png
    :align: center

Authentication: Are they who they say they are?

Authorization: Are they allowed access here?

* Authentication requires proof of identity
* Authorization requires authentication, plus permission from an authority

Identity
--------

**Persistent vs. authoritative**

Imagine an identity thief who takes out lines of credit in their victim's name then pays all the bills on time...

* Is their identity *persistent*?
* Is their identity *authoritative*?

How about a project maintainer who never uses their real name online, but uses the same handle and email address across all sites?

How about a project maintainer who loses the domain which was hosting their email, and thus changes addresses abruptly?

If you're a sysadmin who works with multiple projects, you will run into these concerns often.

.. figure:: static/xkcd_565.png
    :align: center

System Security
---------------

.. figure:: static/xkcd_538.png
    :align: right

* Close ports
* Firewalls
* fail2ban
* Process isolation

Principle of Least Authority
----------------------------

* User & Group management
* ACLs
* File permissions

Other Attacks
-------------

.. figure:: static/xkcd_538.png
    :align: right

* Social engineering
    * Pretexting
    * Phishing
    * Baiting
    * quid pro quo
    * tailgaiting
* Zero-Day vulnerabilities

Passwords
---------

.. figure:: static/xkcd_936.png
    :align: center

* Don't reuse them
* pwgen
* Hashing / salt

TODO: add examples and more explanation and stuff 

What to do if you discover a vulnerability
------------------------------------------

First, disclose it *privately* to those responsible for fixing it

Provide examples -- it's basically a bug report, but through private channels (not public tracker yet!)

Give them time to release a patch before announcing it

Some places have bug bounties

Keys
====
