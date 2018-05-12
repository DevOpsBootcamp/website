.. _setup_docker:

Setting up Docker
=================

`Docker`_ is a software technology which provides the use of containers which is kind of a light form of virtual
machines.  It's used quite a bit in DevOps to setup development environments along with a variety of other uses. In
addition to Docker, we're going to be using `Docker Compose`_ which is used for running multi-container environment.
For DevOps Bootcamp, we're going to be using Docker in a variety of ways from acting as a simple Linux machine, to
hosting applications.

.. _Docker: http://docker.com/
.. _Docker Compose: https://docs.docker.com/compose/

Installing Docker
~~~~~~~~~~~~~~~~~

Docker can be installed on `Windows`_, `Mac`_ and a variety of Linux operating systems (`Ubuntu`_, `Debian`_,
`CentOS`_, `Fedora`_). Please be sure you read the installation instructions closely to ensure your system supports
running Docker and has the needed BIOS features enabled. If you have any trouble getting it installed, feel free to ask
in our Slack channel.

.. _Windows: https://docs.docker.com/docker-for-windows/install/
.. _Mac: https://docs.docker.com/docker-for-mac/install/
.. _Ubuntu: https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/
.. _Debian: https://docs.docker.com/engine/installation/linux/docker-ce/debian/
.. _CentOS: https://docs.docker.com/engine/installation/linux/docker-ce/centos/
.. _Fedora: https://docs.docker.com/engine/installation/linux/docker-ce/fedora/

Installing Docker Compose
~~~~~~~~~~~~~~~~~~~~~~~~~

Docker Compose can be `installed`_ on Windows, Mac and a variety of Linux operating systems. Please read the
installation instructions for your platform *carefully*.

.. _installed: https://docs.docker.com/compose/install/#install-compose

Running the DOBC image
~~~~~~~~~~~~~~~~~~~~~~

First you need you need to clone the `Bootcamp-Exercises`_ repository:

.. _Bootcamp-Exercises: https://github.com/DevOpsBootcamp/Bootcamp-Exercises

.. code-block:: console

  $ git clone https://github.com/DevOpsBootcamp/Bootcamp-Exercises.git

Once you have Docker and Docker Compose installed and running and also have the `Bootcamp-Exercises`_ repository
cloned, you can spin up a Docker image we've created for DOBC by running the following from the root of the repository
directory:

.. code-block:: console

  $ docker-compose up -d
  $ docker-compose run dobc bash

You can log out by typing ``exit`` and then enter which will stop the container.

Stopping the container
~~~~~~~~~~~~~~~~~~~~~~

To stop the container, run the following:

.. code-block:: console

  $ docker-compose kill
  $ docker-compose rm --all
