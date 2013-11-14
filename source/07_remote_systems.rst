===========================
Working with Remote Systems
===========================

What's SSH?
===========

* Secure Remote Shell
* Replaced un-secure rsh, rlogin, and telnet
* Useful tricks
    * Port forwarding
    * SOCKS proxy server
    * Remote command automation
    * Remote X applications
    * Copy files securely

.. note:: ssh user@host
    ssh -p 2000 user@host
    ssh -L5901:localhost:5901 host
    ssh -D 8080 host
    ssh -X host

SSH keys
========

* Public/Private key authentication
* No password “over the wire”
* ssh-agent – “passwordless” logins
* ssh-keygen
* RSA vs DSA
* Remote script automation

