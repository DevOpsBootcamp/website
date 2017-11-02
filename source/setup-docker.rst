.. _setup_docker:

Setting up Docker
=================

Docker is a software technology which provides the use of containers which is kind of a light form of virtual machines.
It's used quite a bit in DevOps to setup development environments along with a variety of other uses. For DevOps
Bootcamp, we're going to be using Docker in a variety of ways from acting as a simple Linux machine, to hosting
applications.

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

Running the DOBC image
~~~~~~~~~~~~~~~~~~~~~~

Once you have Docker installed and running, you can spin up a Docker image we've created for DOBC by running the
following:

.. code-block:: console

  $ docker run -p 2222:22 -h dobc --rm --name=dobc1 -e DOBC_PASSWORD=passw04d \
      osuosl/dobc-centos

This should do the following:

#. Map port ``2222`` on your machine to port ``22`` on the container
#. Set the hostname to ``dobc``
#. Remove the container and its image on exit
#. Name the container ``dobc1``
#. Set the password to ``passw04d`` for ssh via setting an environment variable ``DOBC_PASSWORD``
#. Download the latest ``osuosl/dobc-centos`` image from `Docker Hub`_ and use it for the container

.. _Docker Hub: https://hub.docker.com/r/osuosl/dobc-centos/

Alternatively, you can also run the docker container in an interactive mode instead of connecting to it via ssh. If you
do it using this method, you can skip the next section (connecting via ssh):

.. code-block:: console

  $ docker run -h dobc --rm --name=dobc1 -it osuosl/dobc-centos bash

You can log out by typing ``exit`` and then enter which will stop the container.

Connecting to the container via SSH
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Using your SSH client, connect to hostname ``localhost`` and port ``2222``. Login using the username ``dobc`` and the
password ``passw0rd`` (as set above). Go ahead and accept the host key and login. Once in, you'll be logged into a
CentOS based container.

Using a CLI ssh client, you can do that with the following:

.. code-block:: console

	$ ssh -p 2222 dobc@localhost
	The authenticity of host '[localhost]:2222 ([::1]:2222)' can't be established.
	ECDSA key fingerprint is SHA256:guModObCSS8GEpXQVUh9Fy674bCAacIZI1j5lh9LL+U.
	Are you sure you want to continue connecting (yes/no)? yes
	Warning: Permanently added '[localhost]:2222' (ECDSA) to the list of known hosts.
	dobc@localhost's password:
	[dobc@dobc ~]$

Becoming the root user
~~~~~~~~~~~~~~~~~~~~~~

The container image, has ``sudo`` installed which allows you to become the superuser known as ``root``. To become run,
simply run ``sudo su -``. Now you have full access to the container running Linux!

Stopping the container
~~~~~~~~~~~~~~~~~~~~~~

To stop the container, run the following from another terminal window:

.. code-block:: console

  $ docker stop dobc1

If you run ``docker ps``, you shouldn't see any running instances any more. Keep in mind that when you stop the
container, any changes you've made on the container go away!
