.. _security:


Lesson 13: Security
===================

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

    - Types of security.
    - Threat models.
    - Authentication, Authorization, Identification.
    - Passwords and Passphrases.
    - HTTPS and certificates.
    - Types of attacks.
    - Disclosing a vulnerability.


Security
--------

    se·cu·ri·ty ( siˈkyo͝oritē/ ) [ noun ]
        The state of being free from danger or threat.

        The safety of a state or organization against criminal activity such as
        terrorism, theft, or espionage.

.. ifnotslides::

    Computer Security is a **big** topic.  DOBC will only be able to scratch
    the surface, but if you're interested at all you should 100% do more
    research on the topic.  It is a fascinating field and well worth knowing
    about, even if you're not intending to be a security professional.


Types of Security
-----------------

.. image:: /static/xkcd_416.png
    :align: center
    :target: https://xkcd.com/416/
    :alt: XKCD on WiFi Security

There are three main types of security in computing:

.. ifslides::

    - **Physical Security:** How safe something is from physical interaction.
    - **Software Security:** Exploitation through software.
    - **Network Security:** Exploitations through network servies.

        - **Active:** Breaking into a networked service.
        - **Passive:** 'Sniffing' networked traffic over the wire.

.. ifnotslides::

    Physical Security
        How secure a physical piece of hardware is (put it in a safe).

    Software Security
        Anything which can obtain secret data from a piece of software.

    Network Security
        Security pertaining to networked services (websites, databases, etc).

        - Active: in which an intruder initiates commands to disrupt the
          network's normal operation (Denial-of-Service, Buffer Overflow, SQL
          Injection)
        - Passive: a network intruder intercepts data traveling through the
          network. (Man-in-the-Middle, Wiretapping, Idle Scan)

    Each of these encompases a field of computer security unto itself.  We
    will at least mention each of thee in more detail, but we will focus on
    network securty in this course.

Threat Models
-------------

    Threat models allow you to focus and limit your security resources on what
    is *necessary* instead of what is *possible*.

.. ifnotslides::

    Threat models are the assessment of which attacker you are protecting
    against.  This is so you don't spend too much time in a panic attack
    trying to protect your tiny webapp from the NSA.

    For example, your threat model might be protecting against a DDOS attacker.
    You're not worrying about the multitude of *other* types of attacks there
    are out there, you're just focusing on the person that's going to bombard
    your server with too many requests.  There are many ways to protect
    against DDOS attacks that a developer could reasonably implement, allowing
    one to take *action* against a threat instead of just losing sleep over
    it.


Authentication, Authorization, Identity
---------------------------------------

.. image:: /static/xkcd_1121.png
    :align: center
    :target: https://xkcd.com/1121/
    :alt: XKCD Identity Comic

.. ifslides::

    - **Authentication:** Are they who they say they are?

    - **Authorization:** Are they allowed access here?

    - **Identity:** How do you identify a person? What makes you you?

.. ifnotslides::

    These three concepts are useful vocabulary for discussing security.  If
    there is a problem with an application's Authentication that's very
    different form it's Authorization, which is also differnt form it's ability
    to Identify users.

    Authentication:
        Are they who they say they are?

        An example of Authentication would be a **Username** and
        **Passphrase**.  When you are logging into a website or computer you
        are authenticating.

    Authorization:
        Are they allowed access here?

        An example of Authorization is when you try to open a file on a shared
        computer and you are denied access.  Your user (that you
        *authenticated* as) is not allowd to access that file.

    Identity
        How do you identify a person? What makes you you?

        Identity is tricky.  An example with this would be supplying an
        official government website with your Social Security Number,
        Passport Number, or answering a question only **you** would know the
        answer to.  Anything that uniquely identifies (and proves online) that
        **you are you** is a form of identification.

Passwords / Passphrases
-----------------------

.. ifslides::

    - Problems
    - Solutions
    - Choosing

.. ifnotslides::

    Passwords are the defacto form of Authentication for computers, but they
    aren't a perfect solution (to an admittedly difficult problem).

    Passwords are hard to remember and surprisingly easy for computers to guess
    (because people are bad at making up creative ones).  That's okay though,
    the problem of passwords has been studied and there are some solutions
    that anybody can use.


Problems with Passwords
~~~~~~~~~~~~~~~~~~~~~~~

.. ifnotslides::

    Passwords are a necessary part of security.  They aren't great though for a
    few reasons.

- People repeat passwords.
- Many passwords are easy to guess.
- Passwords are hard to remember.


Solutions for Passwords
~~~~~~~~~~~~~~~~~~~~~~~

.. ifslides::

    - Use a password manager.
    - Change your passwords regularly.
    - Use multi-step authentication.

.. ifnotslides::

    Thankfully because passwords have been a problem for so long there are a
    few workarounds including:

    Use a password manager.
        - `LastPass`_ is very popular and convenient.
        - ``pass`` on Linux and OSX, uses FOSS tools to store passwords.

    Change your passwords regularly.
        **Warning** this is considered a 'Securty Best Practice', but only if
        you create a unique password each time you change it.  Don't replace
        your password by adding a ``1`` to the end of it.

    Use multi-step authentication.
        Google, Github, and Steam (as well as many other services) offer
        multi-step authentication.  This is usually implemented with a
        secondary password which is generated every thirty seconds that you
        enter *after* your actual password.  The second password changes so
        often, and is only visible on your devices, so it makes sneaking into
        your account almost impossible.

.. _LastPass: https://lastpass.com/


Choosing Pass-phrases
~~~~~~~~~~~~~~~~~~~~~

.. ifslides::

    - Let the password manager generate them for you.
    - Use pass *phrases* instead of *words*.

.. ifnotslides::

    Let the password manager generate them for you.
        You might like to create your own passwords, but you are far worse
        than a computer at generating them.  Anything you can remember easily
        is convenient for a computer to guess, and anything that **isn't**
        easy to remember is just a waste of your time.

    Use pass *phrases* instead of *words*.
        When you can't use a password manager consider making your password a
        *sentence* or *phrase* instead of a word.  This is harder for a
        computer to guess and easy for you to remember.

        For instance ``the dog jumped over 85 cats`` is more secure and easier
        to remember than ``xc456zkqt55``, and way more secure.

`Relevant funny bash.org post`_

.. nextslide::

.. image:: /static/xkcd_936.png
    :align: center
    :target: https://xkcd.com/936/
    :alt: XKCD passwords comic

.. _Relevant funny bash.org post: http://bash.org/?244321


Certificates and HTTPS
----------------------

.. image:: /static/securepass.png
    :align: center
    :alt: HTTPS Lock in Browser URL Bar

.. ifslides::

    - **HTTPS:** Hyper Text Transfer Protocol *Secure*.

    - **Certificate Authorities:** An entity that issues digital certificates
      for HTTPS connections.

    - **SSL/TLS:** Secure Socket Layer/Transport Layer Security.

.. ifnotslides::

    Certiciates are what allows your computer to create a secure connection
    with a server and transfer sensitive data across *the wire*. 

    HTTPS
        Hyper Text Transfer Protocol *Secure*.

        This is an alternative to the HTTP protocol used for secure web
        communication.

    Certificate Authorities
        An entity that issues digital certificates for HTTPS connections.  These
        certificates are *trusted* by Browsers through a *web of trust*.  Anybody
        can create their own certificates, but only certificate authorities can
        issue a certificate signed by a *trusted* organization.

    SSL/TLS
        Secure Socket Layer/Transport Layer Security.

        This is the actual protocol used for secure connections over the web.
        TLS is the new protocol that replaced SSL, but they are sometimes
        discussed as one / interchangeably.

    To learn more about a website's HTTPS certificate and security info, click
    the little Lock icon in the URL bar.  You should be able to find more
    information about the certificate including which authority it comes from,
    and more information about it.


Types of Attacks
----------------

.. image:: /static/attack-statistics.png
    :align: center
    :alt: Frequency of online attacks (37% Cross Site Scripting, 16% SQL Injection, etc)


Code Injection
~~~~~~~~~~~~~~

.. ifnotslides::

    Code Injection is the act of inserting code into a running process
    (website, webapp, etc) with malicious intention.  These are a few common
    attacks and a way to start fighting against code injection.

.. image:: /static/xkcd_327.png
    :align: center
    :alt: Billy Droptables XKCD Comic
    :target: https://xkcd.com/327/


Code Injection Attacks
~~~~~~~~~~~~~~~~~~~~~~

.. ifslides::

    - SQL Injection

    ::

        +-----------+---------------------------------------+
        | username: | admin                                 |
        +-----------+---------------------------------------+
        | password: | pass' || true); DROP TABLES STUDENTS; |
        +-----------+---------------------------------------+

    - Cross-Site Scripting (XSS)

    - Cross-Site Request Forgery (CSRF)

.. ifnotslides::

    SQL Injection
        SQL Injection is when you take advantage of the fact that a form input
        is inserted directly into a SQL query.  You write some password and
        then write a new SQL query which drops all tables, or returns all
        data, exploiting an easy security hole.

    ::

        +-----------+---------------------------------------+
        | username: | admin                                 |
        +-----------+---------------------------------------+
        | password: | pass' || true); DROP TABLES STUDENTS; |
        +-----------+---------------------------------------+

    Cross-Site Scripting (XSS)
        Cros-Site Scripting is when a malicious script is sent to, and run on,
        a person's computer.  This tends to take advantage of the fact that
        your browser blindly runs any JavaScript you tell it to.

    Cross-Site Request Forgery (CSRF)
        CSRF is when one website on your browser tries to carry out an action
        *as you* on a different website.  For instance you're an admin of some
        big social media website, you get an email, embedded in the email is a
        CSRF script which tries to *delete all user accounts* on your website.
        Since you've got your credentials cached your browser doesn't know
        better and can run that command becuase it looks like any other
        command.

::

    <img src="http://example.com/?action="Delete All Accounts"


Code Injection Defenses
~~~~~~~~~~~~~~~~~~~~~~~

.. ifslides::

    - Sanitize Inputs
    - CSRF Tokens

.. ifnotslides::

    Some of these attacks are very hard to fight against, but they all have
    industry-tested solutions that are easy enough to implement in an
    application of your own.

    Sanitize Inputs
        Input sanitation is when your code sniffs a piece of input to see if
        it looks like a SQL or code of any kind.  If it does look like code
        it's probably malicious so your program errors out and tells the user
        to enter a *real* password.

    CSRF Tokens
        A CSRF token is a unique string that has to be tied to each request
        you send to a server.  You don't need to log back in each time you get
        a new one but the application won't complete your action unless the
        token is included in your query.  This means only the website you're
        logged into can send a real query because only that website knows the
        CSRF token.


Web Server Attacks
~~~~~~~~~~~~~~~~~~

.. image:: /static/apache-vulns1.png
    :align: center
    :alt: Apache Version Vulnerability
    :target: http://news.netcraft.com/wp-content/uploads/2014/02/apache-vulns1.png

.. ifnotslides::

    Web Server attacks take advantage in vulnerabilities of specific versions
    or default configurations of webservers.

    For instance a webserver's default configuration might allow you to turn it
    off by sending a special request.  The config file tells you to change that
    special request but most people dont.

    As far as versions go, software has bugs.  Developers do their best to fix
    those bugs but when you're running a big website and your infrastructure is
    fragile you don't usually want to update *anything* including the webserver
    software you're running.  So dispite the bug being fixed, not everybody is
    on the same page.


Discovering Vulnerabilites
--------------------------

.. ifnotslides::

    As you begin to grow and push the technology you're using you might find
    real vulnerabilities that could affect real people.  In that case, take a
    deep breath and take responsible action.  Here is a good set of guidelines
    to follow if that happens:

#. Test and document the bug to verify it exists.
    If you think you encountered a bug, make sure you can replicate it.  If
    you can't how can you expect the developers to recreate it?

#. Disclose it **privately** to those responsible for fixing it.
    Provide examples – it’s basically a bug report, but through private
    channels (not public tracker yet!)

#. Give them time to release a patch before announcing it.
    Google waits 90 days to announce a bug after informing the developers.

.. ifnotslides::

    If you are interested in making a pretty penny off of your bug, many
    projects have *bug bounties* which give a $$$ reward for bugs.


TODO
----

.. TODO: Add activities

Further Reading
---------------

`codebashing.com/sql_demo`_
    Try your hand at *actual* SQL Injection attacks

.. TODO: Add more further reading
.. TODO: Suggestion: Bugbounties.

.. _codebashing.com/sql_demo: http://www.codebashing.com/sql_demo
