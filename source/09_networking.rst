====================
Lesson 9: Networking
====================

* What's a network?
* OSI Model of internet (1-4)
    * Relevant devices
    * IPs and what they mean
        * 3 reserved spaces
        * protocol when no router detected & 2 devices trying to BS it
        * class D vs class E
        * DHCP vs static
        * subnet masks
        * broadcast?
        * ports
            * 3 port ranges -- 0-1024 god ports, 1025-?? less hard-set, others
              allocated by system
    * MAC addresses
    * IPV4 vs IPV6
    * TCP/UDP/ping protocol (ICMP?)
* layers 5/6/7 basics
* Modern internet vs. intranets etc.
    * NAT    
* hosts files

What's a network? 
-----------------

"a group or system of interconnected people or things"

To us, a network is:
* Electronic devices
* Sending signals over wire, fiber, or radio
* Communicating data using a standardized protocol

ECE372 at OSU teaches this content, more or less

The OSI Model
=============

Open Systems Interconnection
Layers of abstraction

.. figure:: static/osi-layers.jpg
    :align: center


Layer 1: Physical
-----------------

* Digital vs analog

.. figure:: static/cat5_cable.jpg
    :align: center

Layer 2: Data Link
------------------ 
