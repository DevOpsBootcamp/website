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
    :scale: 75%

Authentication vs. Authorization
--------------------------------



