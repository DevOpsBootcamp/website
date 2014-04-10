====================
Lesson 9: Networking
====================

* What's a network?
* Big Picture
  * OSI Model of networks (1-4)
    * Physical
      * Medium used
      * Ethernet / RJ-45
    * Data Link
      * MAC address
      * Ethernet Datagrams
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

Who is this talk for?
----------------

Someone with little or no networking knowledge. 

ECE/CS 372 at OSU covers this content, more or less

What is a network? 
-----------------

"a group or system of interconnected people or things"

To us, a network is:
* Electronic devices
* Sending signals over wire, fiber, or radio
* Communicating data using a standardized protocol

What is a protocol? 
-----------------
A protocol is:

"A set of agreed upon rules for communication"

* Defines a sequence & format of packets being sent

The OSI Model
=============

Open Systems Interconnection
* Layers of abstraction

.. figure:: static/osi-layers.jpg
    :align: center

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

Network and host addressing

* IPv4
* IPv6

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
In a linux terminal run:::

  ip a

This will display a lot of information about your network interfaces.
See also:::

  ifconfig
  iwconfig


Example output:
===============

::
user@host:~$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN 
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth2: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN qlen 1000
    link/ether 33:77:00:44:66:33 brd ff:ff:ff:ff:ff:ff
3: wlan1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP qlen 1000
    link/ether 24:77:33:44:55:66 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.55/24 brd 192.168.1.255 scope global wlan1
    inet6 fe80::2677:3ff:fed4:538c/64 scope link 
       valid_lft forever preferred_lft forever

Netmask:
========
====================    ====================================
Decimal IP Address          Binary IP Address          
--------------------    ------------------------------------
192.168.1.55             11000000.10101000.00000001.00110111
255.255.255.0            11111111.11111111.11111111.00000000
====================    ====================================

Perform the binary and operation on the mask, IP

=======================    ===================================
Part of address            Corresponding address
-----------------------    -----------------------------------
Network (Decimal)          192.168.1.0                
Network (Binary)           11000000.10101000.00000001.00000000
Host (Decimal)             0.0.0.55
Host (Binary)              00000000.00000000.00000000.00110111
=======================    ===================================


Netmask Example:
========
====================    ====================================
Decimal IP Address          Binary IP Address          
--------------------    ------------------------------------
192.168.1.55             11000000.10101000.00000001.00110111
255.255.255.0            11111111.11111111.11111111.00000000
====================    ====================================

Perform the binary and operation on the mask, IP

=======================    ===================================
Part of address            Corresponding address
-----------------------    -----------------------------------
Network (Decimal)          192.168.1.0                
Network (Binary)           11000000.10101000.00000001.00000000
Host (Decimal)             0.0.0.55
Host (Binary)              00000000.00000000.00000000.00110111
=======================    ===================================

Clever Slide Title
===============

user@host:~$ route
Kernal IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         www.asusnetwork 0.0.0.0         UG    0      0        0 wlan1
link-local      *               255.255.0.0     U     1000   0        0 wlan1
192.168.1.0     *               255.255.255.0   U     2      0        0 wlan1

user@host:~$ route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.1.1     0.0.0.0         UG    0      0        0 wlan1
169.254.0.0     0.0.0.0         255.255.0.0     U     1000   0        0 wlan1
192.168.1.0     0.0.0.0         255.255.255.0   U     2      0        0 wlan1


Bootstrapping
=============

What happens when your computer connects to a network?

1. Duplex negotiation
2. Static or dynamic configuration is applied


Static Configuration
====================

Must in advance know:
* IP Address
* Netmask
* Default Gateway
* DNS Servers (optional in some cases)

Dynamic Configuration
=====================

All of the staticly defined parameters are retrieved over the network via DHCP
