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

Modern Standards Organizations
------------------------------

ICANN: Internet Corporation for Assigned Names and Numbers
    * Allocation of addresses & domain names
    * Protocol port numbers
ISOC: Internet Society
    * Parent of IETF, Internet Engineering Task Force
    * IETF issues RFCs (Requests for Comment)
ISO: International Organization for Standardization
    * Parent of Open Systems Interconnection project
    * OSI model describes components of network

The OSI Model
=============

Open Systems Interconnection
* Layers of abstraction
    * Not all systems contain all layers

.. figure:: static/osi-layers.jpg
    :align: center

* Reference model is not a functional spec

.. note:: "Create a layer of easily localized functions so that the layer
    could be totally redesigned and its protocols changed in a major way...
    without changing the services expected from and provided to adjacent
    layers"

Layer 1: Physical
-----------------

Networking Hardware
    * Connector shapes
    * Wire, optical fiber, or radio signal specifications

.. figure:: static/cat5_cable.jpg
    :align: center

RS-232

.. figure:: static/db25.png

Layer 2: Data Link
------------------


TCP/IP Model
============

.. figure:: static/tcp-ip-model.png

