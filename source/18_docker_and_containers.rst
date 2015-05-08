Docker and Containers
=====================
* Configuration management is approaching 15 years old.
* Some of the command line utilities we use date back to times when people used
  electric typewriters instead of computer screens (we aren't kidding)
* Today we're going to explore a technology which is in its angsty teenage
  years, it's not fully mature.


Quick Review of VMs
-------------------
* The host OS is the one running on bare metal, the OS which the VM runs
  inside.
* The guest OS is the OS running inside the VM.
* Software running inside VMs is slower than software running on the host
  machine.

.. figure:: /static/nesting_dolls.png
    :align: center
    :scale: 70%


What are Containers?
--------------------

* Not VMs.
* Containers are a way to put a program in an imaginary box where it thinks
  it's the only program besides the OS running on the computer.
* Containers allow programs to be isolated from the host system without the
  overhead of VMs. Since VMs run a whole OS on top of an OS, they're slow.
  Containers are just the host OS lying to the program, so they don't need to
  run a second OS, or keep programs inside the VM from messing with files
  outside of it.
* As a side affect, it changes the way you configure and run your applications.

A Brief history of Containers
-----------------------------

* FreeBSD, an OS very similar to Linux, has had container like things since the
  2000s, but they never saw widespread use.
* Linux got containers in 2008, but they are just now beginning to be used.

Docker
------

* Docker is one of the most prominent tools which uses containers.
* It is a way of reproducibly building and running images which have all the
  necessary software to run your program.
* Each part of the application runs inside its own container
    - The database
    - The webapp
    - The caching layer (redis, rabbitmq)

Docker Terminology
------------------
- *Layer*: A set of changes to the 
- *Image*: 
- *Container*: An instance of an image the same way an object is an instance
  of a class.
- *Dockerfile*: A file which describes how to build a docker image.

Docker Alternatives
-------------------
* Rocket is very similar to Docker, supposed to be more secure, but not yet 
  ready for prime time.
* Manipulate raw Linux containers with the init system systemd.

Installing Docker
-----------------
We assume that you're using the VM we provided. If you have trouble, ask for
help.

First install the EPEL repository. This is allows you to install packages which
the CentOS developers didn't include in their list of packages.
After that, install the ``docker-io`` package.

.. code-block:: shell

	$ sudo yum install epel-release
	$ sudo yum install docker-io

Pulling a Docker Image
----------------------
Many people upload their images to a website called DockerHub. You can use the
docker tool to pull down their images and run them. This is really handy
because you don't need to rewrite a lot of commonly used Docker containers like
the MySQL database container.

.. code-block:: shell

	$ docker pull mysql

Running a Docker Image
----------------------

Now that you have the docker image locally, you can run it.

.. code-block:: shell


	$ docker run -d --name my_mysql_container \
	  -e MYSQL_ROOT_PASSWORD=password \
	  mysql

Here are the what these options do:

* `-d` runs the Docker container in the background so you can do other things
  in the terminal.
* `--name` gives the new container a name. If you don't pass this flag, ddocker
  will choose a random one for you.

Running a Program in That Docker Container
------------------------------------------

You can enter the container and run arbitrary commands.
The `-it` flags make the command run interactively.

.. code-block:: shell

	$ docker exec -it my_mysql_container bash
	root@3d8dd4e19779:/# exit
	$  docker exec -it my_mysql mysql -p
	Enter password:
	mysql> SELECT * FROM table;

Dockerfiles
-----------

Docker images are built from Dockerfiles. Let's take a look at (part of) the
MySQL Dockerfile.

.. code-block:: shell
	# This indicates that Docker should use the Debian image as a base for
	# this one
	FROM debian:wheezy

	# create the mysql user and add them to the mysql group
	RUN groupadd -r mysql && useradd -r -g mysql mysql

	# Install the perl programming language with mysql requires
	RUN apt-get update && apt-get install -y perl mysql-server mysql

	# Set some useful environment variables
	ENV MYSQL_MAJOR 5.6
	ENV MYSQL_VERSION 5.6.24

	# Expose this port to the host
	EXPOSE 3306

	# Run this command when everything is done
	CMD ["mysqld"]




Activity
--------
Write a ``Dockerfile`` for systemview.

Resources:
- https://docs.docker.com/reference/builder/
- https://www.digitalocean.com/community/tutorials/docker-explained-using-dockerfiles-to-automate-building-of-images


