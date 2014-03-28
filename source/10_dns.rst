============================
Lesson 10: Networking part 2
============================

* What is DNS
* Why does it matter
* Role of the DNS server
* Record types
    * A
    * AAAA
    * C
    * MX
    * text?
* commands: 
    * dig
    * dig mx
* what's reverse DNS and how's it work
* amplification attacks? 
* caching vs authoritative

.. note:: Running a local caching server gives you control
    restrict caching access to local network, zone transfers

.. code-block:: shell

    $ yum install caching-nameserver
    # primary config file is /etc/named.conf
    # all data files are in /var/named

* RFCs 
    * what they are
    * why they matter


