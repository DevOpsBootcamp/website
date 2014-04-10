====================
Lesson 9: Networking
====================

* What's a network?
* Big Picture
  * OSI Model of networks (1-4)
    * Physical
      * Medium used
    * Data Link
      * MAC address
    * Network
      * IP Address
    * Transport
      * What happens if something goes wrong?
* Get your hands dirty
  * Run the command 'ip a'
  * Run the command 'route -n'
  * traceroute
* Bootstrapping
  * Full Duplex / Half Duplex
  * Configuration: Static vs Dynamic
  * IP Addresses: Public vs Private, reserved addresses
* Network Devices
  * Wireless Router demystified
  * Hubs and Switches
  * Routers
* Bonus Material
  * Control Layer
  * Collisions
  * NAT/PAT

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
* Layers of abstraction

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

MAC: Media Access Control
    * MAC address should be globally unique

ARP: Address Resolution Protocol (between layer 2 & 3)
    * Converts IP address to physical address
    * NDP (neighbor discovery protocol) used in IPv6

Flow control & error checking

Layer 3: Network
----------------

Packet forwarding and routing

Host Addressing

* IPv4/IPv6

Layer 4: Transport
------------------

Interact directly with program
same-order delivery, reliability, flow control, congestion avoidance,

TCP: Transmission Control Protocol
    * used by HTTP, HTTPS, SMTP, POP3, IMAP, SSH, FTP, Telnet

UDP: User Datagram Protocol
    * No error checking built in
    * No retransmission delays
    * VoIP, media, games

Get your hands dirty
============
In a linux terminal run:

::

  ip a

This will display a lot of information about your network interfaces.
See also::

  ifconfig
  iwconfig





