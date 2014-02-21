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

    Pono
    - passwords, keys, encryption

     - passwords/hashing (plaintext -> hash -> salt)
     - key pairs
     - ssh keys (passphrase vs none; automation; authorized_keys)
     - GPG keys, signing stuff, publishing to keyservers
     - certificates (SSL/TLS)
     - ciphers
     - https

    Jack???? (else dean/emily/ken w/ emily presenting)
    - web app security

     - parameterize or sanitize inputs
     - SQL injection
     - XSS, csrf tokens
     - https://www.owasp.org/index.php/Top_10_2013-Top_10
     - filesystem & user permissions (remember lesson 2?)
     - CRIME attack

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

Passwords
---------

.. figure:: static/xkcd_936.png
    :align: center

* Don't reuse them
* pwgen
* Hashing / salt
* Password managers (LastPass, 1Password)

TODO: add examples and more explanation and stuff 

What to do if you discover a vulnerability
------------------------------------------

First, test and document to verify that it exists.

Then, disclose it *privately* to those responsible for fixing it

Provide examples -- it's basically a bug report, but through private channels (not public tracker yet!)

Give them time to release a patch before announcing it

Some places have bug bounties

Keys
====

Web application security
========================

.. figure:: static/2013-vulnerability-summary_290x250.png
    :align: right

* Who needs to worry about web application security?

  * Everyone!

* What kinds of attacks are seen in the wild?

  * Many!

* What can devops do about these attacks?

  * A lot!

(image source: https://info.cenzic.com/rs/cenzic/images/2013-vulnerability-summary_290x250.png)

.. note::

   Everyone needs to worry about web application security.  You need
   to worry, because you're learning how to write web applications.
   You want to avoid making decisions which could lead to exposing
   vulnerabilities and letting bad people use your service to do bad
   things.  You also need to worry even if you're not writing web
   applications, because you're *using* web applications.  The web is
   still a wild and wooly place, and the last line of defense for the
   user is their own common sense.

   What kinds of attacks are seen in the wild?  The image shows a
   dizzying array of acronyms and shorthand but we'll be going over
   those in a little more detail.

   And what can devops like us do about these attacks?  Plenty -- wait
   and see.

Code Injection
--------------

.. figure:: static/xkcd_327.png
    :align: right

* Attacks

  * SQL Injection
  * Cross-Site Scripting (XSS)
  * Cross-Site Request Forgery (CSRF)
  * Remote Code Execution

* Defenses

  * Sanitize your inputs!

http://bobby-tables.com/
https://docs.djangoproject.com/en/dev/ref/contrib/csrf/
http://guides.rubyonrails.org/security.html

.. note:: 

   These types of attacks consist of code that is introduced into the
   application causing unexpected behavior.  This code can be
   introduced unintentionally by typical users who use quotes or
   ampersands in their inputs as well as intentionally by nefarious folks.

   The comic demonstrates a classic SQL injection attack.  Bobby took
   advantage of the school's software not properly sanitizing their
   inputs by including a command to drop the students table, causing
   the kind of chaos often seen in xkcd comics.  

   Cross-site scripting works much the same way: someone posts a
   comment on a blog which includes Javascript which gets executed
   when you view the comment.  When it is executed, it does something
   horrible like send them your cookie for that blog site.

   Cross-site request forgeries are similar but instead of Javascript
   you'll see image links that really point to another site like your
   bank, hoping that your cookies will let them transfer money from
   your accounts to theirs.  

   Remote site execution is what it sounds like: just like the SQL
   injection attack, but instead running a shell command on the web
   server.  I think by now you all have enough experience with running
   commands on your virtual machines to know how bad that could be.

   Luckily, each of these threats can be addressed the same way:
   listen to Bobby's mom and sanitize your inputs!  There's a web site
   dedicated to helping developers with SQL injection threats which
   I've listed above, but the same concepts apply to the other
   threats.  Want to stop cross-site scripting?  Don't allow users to
   contribute arbitrary Javascript in comments.  Want to stop cross
   site request forgeries?  Make sure your GET requests are free of
   side-effects, and include tokens in your forms.  As a bonus, Django
   will do that last bit for you if you let it -- check out that
   second link up there for more details.  That third link is the
   Rails security guide and provides advice on these issues as well as
   many others.


Web Server-Specific Attacks
---------------------------

.. figure:: static/apache-vulns1.png
    :align: right

* Version-Based
* Configuration-Based

(image source http://news.netcraft.com/wp-content/uploads/2014/02/apache-vulns1.png)

.. note:: 

   There is a constant battle between developers and the bad guys --
   one side discovers vulnerabilities, the other side fixes them.  One
   of the easiest things to do to keep the bad guys out is to use the
   most up-to-date version of your web server, regardless of whether
   it's Apache or IIS or nginx.

   The graph above shows the most popular versions of Apache as of
   February 2014 according to Netcraft.  Apache encourages admins to
   run the latest major release of the 2.4 stable branch, which is
   Apache 2.4.7.  How many of those releases do you see in that image?
   That's right -- none.  Heck, two of the top fifteen are EOLed --
   they aren't even receiving security updates any longer!  This is
   bad.  Don't be like them.

   But it's not enough to run the latest version.  You should also
   make sure your configuration files are updated as well.  Some
   default configurations will include accounts or passwords which can
   be guessed by hackers.  Other times certain features will be
   enabled by default, which can introduce vulnerabilities you don't
   expect even though you're not using those features.  Read the
   release notes when you update your software.  Pay attention to
   details.  They will.  You should too.
   

Problems with Design and Implementation
---------------------------------------

  * Authentication and Authorization
  * Session Management
  * Information Leakage
  * Unauthorized Directory Access

.. note:: 

   The remaining threats facing the typical web developer come down to
   design and implementation problems.  The fine points of
   authentication and authorization have been discussed already: make
   sure that all your actions are authorized by authenticated users
   and you should be okay.  

   Also, don't let your cookies have infinite lifetimes.  Better to
   have your users occasionally log in again than let them be
   vulnerable to those cross-site attacks we covered before.  Pro tip:
   PHP has a default setting for "session.cookie_lifetime" of zero,
   which means they never expire.  If you're using PHP, fix that.

   Information leakage is pretty sneaky.  Let's say your app allows
   users to request a password reset by entering their email
   addresses.  If your app behaves differently when valid and invalid
   addresses are input, congratulations, you're leaking information.
   Unauthorized directory access is a specialized form of information
   leakage -- while it's nice to let people know how to contact your
   staff, you might not want to let them download everyone's email
   address and such.

Other Attacks
-------------

.. figure:: static/xkcd_538.png
    :align: right

* Social engineering
    * Pretexting
    * Phishing
    * Baiting
    * Quid Pro Quo
    * Tailgaiting
* Zero-Day vulnerabilities

.. note::

   There are two other major categories of attacks that haven't been
   discussed, mainly because they're different than the broad
   categories previously mentioned.  

   Social engineering leverages those person-to-person skills us
   computer folks are so well known for not having.  Can someone let
   me borrow their laptop for a minute?  I just want to tell my mom
   I'll be home late tonight... honest!

   Pretexting is when someone contacts you with a pretext.  They sound
   like they're authentic because they know something about you which
   they probably got off Facebook or something else.  "Hi, I'm calling
   from Chase Bank and I noticed that your card might have been used
   at a location where fraud was committed.  I have your name as Bob
   Smith and your date of birth as May third, 1992.  Can you read me
   your card number and the three digits on the back?"

   Phishing is something we've all been warned about.  We all know
   that eBay and Paypal aren't going to email us asking for our bank
   account information.  Just don't fall for it and you'll be okay.

   Baiting is a little more interesting.  Ever walk down the street
   and notice a thumb drive or SD card on the ground?  Hey -- free
   thumb drive, right?  Let's just put it in the computer, what could
   go wrong?  Plenty.  If it's too good to be true, it probably is.

   Quid pro quo is a trade -- I'll give you something if you give me
   something.  Would you trade your password for a chocolate bar?
   According to the BBC, someone tried this outside a subway station
   in London in 2004, and more than seventy percent of people took
   that trade!  Thirty-four percent gave it up for free.  Don't do
   that.

   I suspect many of you who live in the dorms have been told about
   tailgating.  You're unlocking the dorm door and someone comes up
   and says "hey, I forgot my key in my room, can you let me in" or
   maybe they're wearing a Domino's uniform and are carrying a pizza.
   You're a nice person, you want to help them.  Don't do it.

   And that leaves us with zero-day vulnerabilities.  The term 'zero
   day' refers to the amount of time that the folks who write and
   maintain the code have had to fix it.  If they don't know about it,
   they can't fix it.  This is why it's so important for us to report
   vulnerabilities when we discover them as was discussed earlier.


What Not to Do: The Exercise
============================

Getting Up to Date
------------------

* ssh into your vagrant environment
* change directory to your local systemview repo

    .. code-block:: bash

        $ cd ~/projects/systemview
    

* Make sure your local copy is up to date

    .. code-block:: bash

        $ git pull

    * If you've modified code you'll need to follow these instructions

    .. code-block:: bash

        $ git stash save "some witty name about your work"
        $ git pull --rebase


Let's Check out Dean's (not so) Awesome Code
--------------------------------------------

.. code-block:: bash

    $ git checkout <not so awesome code branch goes here>
