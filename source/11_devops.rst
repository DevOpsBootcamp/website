Devops & Configuration Management Intro
========================================

Session Summary
---------------

- Devops introduction
- Configuration management introduction

Devops Introduction
===================

What is it?

  *"A software development method that stresses communication, collaboration and
  integration between software developers and information technology (IT)
  operations professionals."* [Wikipedia]

.. [Wikipedia] http://en.wikipedia.org/wiki/DevOps

Definition of Devops
--------------------

- Software Engineering
- Technology Operations
- Quality Assurance (QA)

.. figure:: static/Devops.svg
    :scale: 80%
    :align: center

    Wikipedia (cc)

The old view
------------

- **"Dev"** side being the *"makers"*
- **"Ops"** side being the *"people that deal with the creation after its
  birth”*

.. figure:: static/silo-fire.jpg
    :scale: 50%
    :align: right

    photo by http://thoriseador.deviantart.com/ (CC)

This siloed environment has created much harm in the industry and the core
principle behind Devops.

The Agile Approach
------------------

- Iterative, incremental
- Requirements change often thus need to be adaptive
- Very short feedback loop and adaptation cycle
- Quality focus

Manifesto:

  *Individuals and interactions over processes and tools
  Working software over comprehensive documentation
  Customer collaboration over contract negotiation
  Responding to change over following a plan*

  *That is, while there is value in the items on
  the right, we value the items on the left more.*

Adapting Agile to Ops
---------------------

- Widening the principles towards infrastructure

  *"Infrastructure as code"* - i.e. configuration management

- Integrating ops with dev, QA and product in the product teams
- Continuous Integration

  *"Give your developers a pager and put them on call"*

- Utilizing more specific metric and monitoring schemes

Better Tools for Devops
-----------------------

Explosion of new tools over the past few years:

  - Release tools (jenkins, travisci, etc)
  - Config Management (puppet, chef, ansible, cfengine)
  - Orchestration (zookeeper, noah, mesos)
  - Monitoring & Metrics (statsd, graphite, etc)
  - Virtualization & containerization (AWS, Openstack, vagrant, docker)

References
----------

http://theagileadmin.com/what-is-devops/
http://en.wikipedia.org/wiki/DevOps
http://en.wikipedia.org/wiki/Agile_software_development
https://www.youtube.com/watch?v=g-BF0z7eFoU
https://www.youtube.com/watch?v=_I94-tJlovg
https://www.youtube.com/watch?v=h5E--QSBVBY

