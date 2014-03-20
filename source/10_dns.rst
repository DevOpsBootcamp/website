===
DNS
===

* What it's for
* Caching vs authoritative
* Email servers
    * Better to have locan DNS
* Restrict
    * Caching access to trusted network
    * Zone transfers

.. note:: Running a local caching server gives you control

    On CentOS, to install a caching nameserver, do the following:
     yum install caching-nameserver

    Primary config file is /etc/named.conf

    In CentOS, all data files are in /var/named
