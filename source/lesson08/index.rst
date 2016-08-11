.. _security:


Lesson 8: Security
==================

What is security?
-----------------

se·cu·ri·ty

  siˈkyo͝oritē/

  noun

  - the state of being free from danger or threat.
  - the safety of a state or organization against criminal activity such as
    terrorism, theft, or espionage.

Types of security
-----------------

* Physical security
* Software security
* Network security
    * Active vs. passive

.. figure:: /static/xkcd_416.png
    :align: center

Authentication, Authorization, Identity
---------------------------------------

.. figure:: /static/xkcd_1121.png
    :align: center

:Authentication: Are they who they say they are?

:Authorization: Are they allowed access here?

:Identity: How do you identify a person? What makes you *you*?

Passwords
---------

.. figure:: /static/xkcd_936.png
    :align: right
    :scale: 70%

* http://bash.org/?244321
* Password Managers
* What makes a good password?

Server Side
-----------

.. figure:: /static/rainbow-table.jpg
    :align: center
    :scale: 85%

* Rainbow Table
* Hashing and salt

Certificates and HTTP
---------------------

* Certificate Authorities
* https
* ssl/tls

.. figure:: /static/certificate-of-attendance.jpg
	:align: center
	:height: 400px

Huh?
----

You can see how your connection is being encrypted pretty easily,
including which certificate authority and protocols are being used.

Go to https://github.com and click on the little lock next to the
url.

.. figure:: /static/securepss.png
	:align: center
	:height: 200px

Then click 'More information'. Under 'Verified by', you can see the
certificate authority, and under 'Technical Details' you can see
the encryption scheme used.

What attacks are out there?
---------------------------

.. figure:: /static/attack-statistics.png
	:align: center

Code Injection
--------------

.. figure:: /static/xkcd_327.png
    :align: right
    :scale: 70%

* Attacks

  * SQL Injection
  * Cross-Site Scripting (XSS)
  * Cross-Site Request Forgery (CSRF)
  * Remote Code Execution

* Defenses

  * Sanitize your inputs!

Web Server-Specific Attacks
---------------------------

.. figure:: /static/apache-vulns1.png
    :align: center

    image source
    http://news.netcraft.com/wp-content/uploads/2014/02/apache-vulns1.png

* Version-Based
* Configuration-Based

Problems with Design and Implementation
---------------------------------------

  * Authentication and Authorization
  * Session Management
  * Information Leakage
  * Unauthorized Directory Access

Other Attacks
-------------

.. figure:: /static/xkcd_538.png
    :align: right

- Social engineering

  - Pretexting
  - Phishing
  - Baiting
  - Quid Pro Quo
  - Tailgaiting
- Zero-Day vulnerabilities

What to do if you discover a vulnerability
------------------------------------------

* First, test and document to verify that it exists.
* Then, disclose it *privately* to those responsible for fixing it
* Provide examples -- it's basically a bug report, but through private channels
  (not public tracker yet!)
* Give them time to release a patch before announcing it
* Some places have bug bounties

Ok, so should I worry?
----------------------

- Probably not
- It's all about the tools

Let's do stuff
--------------

Head to http://www.codebashing.com/sql_demo to try
your hand at SQL injection and see how it
really happens!
