.. _new-buildbot-worker:
.. _buildworker:

====================
New buildbot workers
====================

.. highlight:: bash

Python's :ref:`buildbots` system was discussed earlier.  We sometimes refer to
the collection of *build workers* as our "buildbot fleet".  The machines that
comprise the fleet are voluntarily contributed resources.  Many are run by
individual volunteers out of their own pockets and time, while others are
supported by corporations.  Even the corporate sponsored buildbots, however,
tend to exist because some individual championed them, made them a reality, and
is committed to maintaining them.

Anyone can contribute a buildbot to the fleet.  This document describes how
to go about setting up a buildbot worker, getting it added, and some hints about
buildbot maintenance.

Anyone running a buildbot that is part of the fleet should subscribe to the
`python-buildbots <https://mail.python.org/mailman3/lists/python-buildbots.python.org/>`__
mailing list.  This mailing list is also the place to contact if you want to
contribute a buildbot but have questions.

As for what kind of buildbot to run...take a look at our `current fleet
<builders_>`__.  Pretty much anything that isn't
on that list would be interesting: different Linux/Unix distributions,
different versions of the various OSes, other OSes if you or someone are
prepared to make the test suite actually pass on that new OS.  Even if you only
want to run an OS that's already on our list there may be utility in setting it
up; we also need to build and test python under various alternate build
configurations.  Post to the mailing list and talk about what you'd like to
contribute.


Preparing for buildbot worker setup
===================================

Since the goal is to build Python from source, the system will need to have
everything required to do normal python development:  a compiler, a linker, and
(except on Windows) the "development" headers for any of the optional modules
(zlib, OpenSSL, and so on) supported by the platform.  Follow the steps outlined in
:ref:`setup` for the target platform, all the way through to having a working
compiled Python.

In order to set up the buildbot software, you will need to obtain an identifier
and password for your worker so it can join the fleet.  Open an issue in the
`configuration repository <https://github.com/python/buildmaster-config/issues/new?template=new_worker.yml>`__
to discuss adding your worker and to obtain the
needed workername and password.  You can do some of the steps that follow
before having the credentials, but it is easiest to have them before
the "buildbot worker" step below.


Setting up the buildbot worker
==============================

Conventional always-on machines
-------------------------------

You need a recent version of the `buildbot <https://buildbot.net/>`__ worker
software.  On most platforms the distribution's package manager provides the
``buildbot-worker`` package, which also creates a dedicated service account,
systemd unit (or equivalent), and the necessary directories.  For platforms
where no package exists, ``pip install buildbot-worker`` is the fallback, but
you will need to create the service account, directories, and service unit
manually.  You may also want to set the buildbot up using a virtual
environment, depending on how you manage your system; you'll need to adjust
the steps below as appropriate if you choose that path.

.. tab:: Linux

   .. tab:: Fedora / RHEL / CentOS

      **Fedora**::

         dnf install buildbot-worker

      **RHEL 8** (requires EPEL)::

         subscription-manager repos --enable codeready-builder-for-rhel-8-$(arch)-rpms
         dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
         dnf install buildbot-worker

      **RHEL 9** (requires EPEL)::

         subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms
         dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
         dnf install buildbot-worker

      **CentOS Stream 9 / 10** (requires CRB + EPEL)::

         dnf config-manager --set-enabled crb
         dnf install epel-release epel-next-release
         dnf install buildbot-worker

      The RPM creates a ``buildbot-worker`` system user, installs a
      templated systemd unit ``buildbot-worker@.service``, and creates
      ``/var/lib/buildbot/worker/`` as the base directory for worker
      instances.

      .. tip::

         If your system has most of its disk space on ``/home`` rather than
         on the root partition, create the worker data under ``/home`` and
         symlink it so the packaged systemd unit still works::

            mkdir -p /home/buildbot-worker/worker
            ln -s /home/buildbot-worker/worker /var/lib/buildbot/worker

         Adjust ownership and paths to match your distro's conventions.

      Create the worker (replace ``WORKERNAME`` and ``WORKERPASSWD`` with
      the credentials provided to you from your buildmaster-config issue)::

         sudo -u buildbot-worker buildbot-worker create-worker \
             /var/lib/buildbot/worker/WORKERNAME \
             buildbot-api.python.org:9020 WORKERNAME WORKERPASSWD

      Edit ``info/admin``, ``info/host``, and ``buildbot.tac`` in the worker
      directory (see below for recommended settings).

      Enable and start the service::

         systemctl enable --now buildbot-worker@WORKERNAME.service

   .. tab:: Debian / Ubuntu

      ::

         apt install buildbot-worker

      The package creates a ``buildbot`` system user, installs a templated
      systemd unit ``buildbot-worker@.service``, and creates
      ``/var/lib/buildbot/workers/`` as the base directory for worker
      instances.

      .. tip::

         If your system has most of its disk space on ``/home`` rather than
         on the root partition, create the worker data under ``/home`` and
         symlink it so the packaged systemd unit still works::

            mkdir -p /home/buildbot/workers
            ln -s /home/buildbot/workers /var/lib/buildbot/workers

         Adjust ownership and paths to match your distro's conventions.

      Create the worker (replace ``WORKERNAME`` and ``WORKERPASSWD`` with
      the credentials provided to you from your buildmaster-config issue)::

         sudo -u buildbot buildbot-worker create-worker \
             /var/lib/buildbot/workers/WORKERNAME \
             buildbot-api.python.org:9020 WORKERNAME WORKERPASSWD

      Edit ``info/admin``, ``info/host``, and ``buildbot.tac`` in the worker
      directory (see below for recommended settings).

      Enable and start the service::

         systemctl enable --now buildbot-worker@WORKERNAME.service

   .. tab:: Other / pip

      For distros without a ``buildbot-worker`` package, install via pip::

         pip install buildbot-worker

      **NixOS** users should use the built-in ``services.buildbot-worker``
      NixOS module; see the
      `nixpkgs module source <https://github.com/NixOS/nixpkgs/blob/master/nixos/modules/services/continuous-integration/buildbot/worker.nix>`__
      for available options.

      **Arch Linux** has buildbot packages in the AUR, but they are
      currently unmaintained.  Using pip is more reliable.

      pip does **not** create a system user, directories, or service unit.
      Set these up manually.  On distros with ``useradd``::

         useradd --system --shell /sbin/nologin \
             --home-dir /var/lib/buildbot/worker --create-home buildbot-worker

      On Alpine Linux (BusyBox)::

         adduser -S -D -H -h /var/lib/buildbot/worker -s /sbin/nologin buildbot-worker

      Then create the directories::

         mkdir -p /var/lib/buildbot/worker
         chown buildbot-worker:buildbot-worker /var/lib/buildbot/worker

      Create the worker (replace ``WORKERNAME`` and ``WORKERPASSWD`` with
      the credentials provided to you from your buildmaster-config issue)::

         sudo -u buildbot-worker buildbot-worker create-worker \
             /var/lib/buildbot/worker/WORKERNAME \
             buildbot-api.python.org:9020 WORKERNAME WORKERPASSWD

      Edit ``info/admin``, ``info/host``, and ``buildbot.tac`` in the worker
      directory (see below for recommended settings).

      On systemd-based distros, a service unit must also be installed; see
      the service management section below.


.. tab:: Unix

   .. tab:: FreeBSD

      ::

         pkg install devel/py-buildbot-worker

      The package creates a ``buildbot`` system user, installs an
      ``rc.d`` service with profile support, and creates
      ``/var/db/buildbot/workers/`` as the base directory for worker
      instances.

      Create the worker (replace ``WORKERNAME`` and ``WORKERPASSWD`` with
      the credentials provided to you from your buildmaster-config issue)::

         su -m buildbot -c "buildbot-worker create-worker \
             /var/db/buildbot/workers/WORKERNAME \
             buildbot-api.python.org:9020 WORKERNAME WORKERPASSWD"

      Edit ``info/admin``, ``info/host``, and ``buildbot.tac`` in the worker
      directory (see below for recommended settings).

      Enable and start the service.  The rc.d script uses profile names as
      shell variable identifiers, so pick a short name without hyphens
      (it does not need to match the worker name)::

         sysrc buildbot_worker_enable=YES
         sysrc buildbot_worker_profiles="myworker"
         sysrc buildbot_worker_myworker_enable=YES
         sysrc buildbot_worker_myworker_basedir=/var/db/buildbot/workers/WORKERNAME
         service buildbot-worker start


.. tab:: macOS

   * Create a buildbot user using the macOS control panel user admin.  It
     should be a "standard" user.
   * Log in as the buildbot user.
   * Install the buildbot worker [#]_ by running ``pip install buildbot-worker``.

   In a terminal window for the buildbot user, issue the following commands (you
   can put the ``buildarea`` wherever you want to)::

      mkdir buildarea
      buildbot-worker create-worker buildarea buildbot-api.python.org:9020 WORKERNAME WORKERPASSWD


.. tab:: Windows

   * Create a buildbot user as a "standard" user.
   * Install the latest version of Python from python.org.
   * Open a Command Prompt.
   * Execute ``python -m pip install pywin32 buildbot-worker`` (note that
     ``python.exe`` is not added to ``PATH`` by default, making the
     ``python`` command accessible is left as an exercise for the user).

   On Windows, `the maximum length for a path is limited
   <https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation>`__.
   This might cause some tests to fail, unless long paths support is enabled.

   Use this PowerShell command to check whether long paths are enabled::

      Get-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled"

   If the value is not "1", you can enable long paths using this PowerShell command::

      New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force


   In a terminal window for the buildbot user, issue the following commands.
   (You can put the ``buildarea`` wherever you want to.)
   Note that the ``buildbot-worker`` command will be in the
   :file:`Scripts` directory of your Python installation. Here and in the rest
   of the guide, you may need to launch it using the full path.

   .. code-block::

      mkdir buildarea
      buildbot-worker create-worker buildarea buildbot-api.python.org:9020 WORKERNAME WORKERPASSWD


The ``info/admin`` file in the worker directory should contain your contact
information, and ``info/host`` should describe the host configuration.  This
information is displayed on the buildbot web interface.  Since these pages are
publicly visible, consider obfuscating your email address (for example,
``user AT example.com``) to avoid spam from web scrapers.

The recommended ``buildbot.tac`` settings are:

* ``keepalive = 60`` -- the buildmaster uses a 60-second keepalive interval;
  the default of ``600`` is too high and can cause spurious disconnections.
* ``delete_leftover_dirs = 1`` -- automatically cleans up build directories
  that the master no longer needs.

.. tip::

   Build directories and ``twistd.log`` rotations can accumulate over time.
   Monitor free disk space on the partition that holds the worker directory,
   even with ``delete_leftover_dirs`` enabled.

Service management
~~~~~~~~~~~~~~~~~~

You will also want to make sure that the worker is started when the
machine reboots:

.. tab:: Linux

   .. tab:: Distro package

      If you installed via a distro package (Fedora, RHEL, CentOS, Debian,
      or Ubuntu), the service was already enabled in the installation
      step above.

   .. tab:: Manual systemd

      If you installed via pip, you need to install a systemd unit yourself.
      The upstream buildbot project provides a
      `contributed template unit <https://github.com/buildbot/buildbot/blob/master/worker/contrib/systemd/buildbot-worker%40.service>`__
      along with
      `sysusers.d and tmpfiles.d configs <https://github.com/buildbot/buildbot/tree/master/common/contrib/systemd>`__.

      Create ``/etc/systemd/system/buildbot-worker@.service`` with the
      following contents::

         [Unit]
         Description=Buildbot Worker %i
         Documentation=man:buildbot-worker(1) https://docs.buildbot.net/
         After=network.target
         ConditionDirectoryNotEmpty=/var/lib/buildbot/worker/%i
         ConditionFileNotEmpty=/var/lib/buildbot/worker/%i/buildbot.tac

         [Service]
         Type=simple
         User=buildbot-worker
         Group=buildbot-worker
         WorkingDirectory=/var/lib/buildbot/worker/
         StateDirectory=buildbot/worker
         ExecStart=/usr/local/bin/buildbot-worker start --nodaemon %i
         Restart=always
         ProtectSystem=full
         ProtectHome=yes
         PrivateDevices=yes
         PrivateTmp=yes

         [Install]
         WantedBy=multi-user.target

      Adjust ``User``, ``Group``, ``WorkingDirectory``, and the
      ``ExecStart`` path to match your setup.  If your worker data is
      symlinked from ``/home`` (see the filesystem layout tip above),
      change ``ProtectHome=yes`` to ``ProtectHome=no`` so systemd can
      follow the symlink.  Then::

         systemctl daemon-reload
         systemctl enable --now buildbot-worker@WORKERNAME.service

   .. tab:: SysV init

      For distros without systemd (such as Alpine Linux with OpenRC),
      upstream provides a
      `SysV init script <https://github.com/buildbot/buildbot/blob/master/worker/contrib/init-scripts/buildbot-worker.init.sh>`__
      with a
      `default configuration file <https://github.com/buildbot/buildbot/blob/master/worker/contrib/init-scripts/buildbot-worker.default>`__.
      Install these as ``/etc/init.d/buildbot-worker`` and
      ``/etc/default/buildbot-worker`` respectively, then configure the
      worker instances in the default file.

   .. tab:: Cronjob

      If neither systemd nor a SysV init script is practical, you can use
      a cronjob.  Add the following line to ``/etc/crontab``::

            @reboot buildbot-worker restart /path/to/workerdir

      Note that ``restart`` is used rather than ``start`` in case a crash
      has left a ``twistd.pid`` file behind.

.. tab:: Unix

   .. tab:: rc.d

      If you installed via a package on FreeBSD (or another BSD), the
      service was already enabled in the installation step above.

      If you installed via pip, you will need to write an ``rc.d`` script
      or use the cronjob approach described in the Linux tab.

.. tab:: macOS

   * Create a bin directory for your buildbot user::

         mkdir bin

   * Place the following script, named ``run_worker.sh``, into that directory::

         #!/bin/bash
         export PATH=/usr/local/bin:/Library/Frameworks/Python.framework/Versions/Current/bin:$PATH
         export LC_CTYPE=en_US.utf-8
         cd /Users/buildbot/buildarea
         twistd --nodaemon --python=buildbot.tac --logfile=buildbot.log --prefix=worker

   *  Place a file with the following contents into ``/Library/LaunchDaemons``:

      .. code-block:: xml

         <?xml version="1.0" encoding="UTF-8"?>
         <!DOCTYPE plist PUBLIC "-//Apple Computer//DTD PLIST 1.0//EN"
               "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
         <plist version="1.0">
         <dict>
               <key>Label</key>
               <string>net.buildbot.worker</string>
               <key>UserName</key>
               <string>buildbot</string>
               <key>WorkingDirectory</key>
               <string>/Users/buildbot/buildarea</string>
               <key>ProgramArguments</key>
               <array>
                       <string>/Users/buildbot/bin/run_worker.sh</string>
               </array>
               <key>StandardOutPath</key>
               <string>twistd.log</string>
               <key>StandardErrorPath</key>
               <string>twistd.log</string>
               <key>KeepAlive</key>
               <true/>
               <key>SessionCreate</key>
               <true/>
         </dict>
         </plist>

      The recommended name for the file is ``net.buildbot.worker``.

.. tab:: Windows

   * Add a Scheduled Task to run ``buildbot-worker start buildarea`` as the
     buildbot user "when the computer starts up".  It is best to provide
     absolute paths to the ``buildbot-worker`` command and the :file:`buildarea`
     directory.  It is also recommended to set the task to run in the
     directory that contains the :file:`buildarea` directory.

   * Alternatively (note: don't do both!), set up the worker
     service as described in the `buildbot documentation
     <https://docs.buildbot.net/current/manual/installation/misc.html#launching-worker-as-windows-service>`__.

If you have not already started the worker through a service manager, you
can start it manually for initial testing::

    buildbot-worker start /path/to/workerdir

Then you can either wait for someone to make a commit, or you can pick a
builder associated with your worker from the `list of builders
<builders_>`__ and force a build.

In any case you should initially monitor builds on your builders to make sure
the tests are passing and to resolve any platform issues that may be revealed
by tests that fail.  Unfortunately we do not currently have a way to notify you
only of failures on your builders, so doing periodic spot checks is also a good
idea.

----

Latent workers
--------------

We also support running `latent workers
<https://docs.buildbot.net/current/manual/configuration/workers.html#latent-workers>`__
on the AWS EC2 service.  To set up such a worker:

* Start an instance of your chosen base AMI and set it up as a
  conventional worker.
* After the instance is fully set up as a conventional worker (including
  worker name and password, and admin and host information), create an AMI
  from the instance and stop the instance.
* Contact the buildmaster administrator who gave you your worker
  name and password and give them the following information:

  * Instance size (such as ``m4.large``)
  * Full region specification (such as ``us-west-2``)
  * AMI ID (such as ``ami-1234beef``)
  * An Access Key ID and Access Key.  It is recommended to set up
    a separate IAM user with full access to EC2 and provide the access key
    information for that user rather than for your main account.

The buildmaster cannot guarantee that it will always shut down your
instance(s), so it is recommended to periodically check and make sure
there are no "zombie" instances running on your account, created by the
buildbot master.  Also, if you notice that your worker seems to have been
down for an unexpectedly long time, please ping the `python-buildbots
<https://mail.python.org/mailman3/lists/python-buildbots.python.org/>`__ list to
request that the master be restarted.

Latent workers should also be updated periodically to include operating system
or other software updates, but when to do such maintenance is largely up to you
as the worker owner.  There are a couple different options for doing such
updates:

* Start an instance from your existing AMI, do updates on that instance,
  and save a new AMI from the updated instance.  Note that (especially for
  Windows workers) you should do at least one restart of the instance after
  doing updates to be sure that any post-reboot update work is done before
  creating the new AMI.
* Create an entirely new setup from a newer base AMI using your existing
  worker name and password.

Whichever way you choose to update your AMI, you'll need to provide the
buildmaster administrators with the new AMI ID.


Buildbot worker operation
=========================

Most of the time, running a worker is a "set and forget" operation,
depending on the level of involvement you want to have in resolving bugs
revealed by your builders.  There are, however, times when it is helpful or
even necessary for you to get involved.  As noted above, you should be
subscribed to ``python-buildbots@python.org`` so that you will be made
aware of any fleet-wide issues.

Necessary tasks include, obviously, keeping the buildbot running.  Currently
the system for notifying buildbot owners when their workers go offline is not
working; this is something we hope to resolve.  So currently it is helpful if
you periodically check the status of your worker.  We will also contact you
via your contact address in ``info/admin`` when we notice there is a
problem that has not been resolved for some period of time and you have
not responded to a posting on the python-buildbots list about it.

We currently do not have a minimum version requirement for the worker
software.  However, this is something we will probably establish as we tune the
fleet, so another task will be to occasionally upgrade the buildbot worker software.
Coordination for this will be done via ``python-buildbots@python.org``.

The most interesting extra involvement is when your worker reveals a unique
or almost-unique problem:  a test that is failing on your system but not on
other systems.  In this case you should be prepared to offer debugging help to
the people working on the bug: running tests by hand on the worker machine
or, if possible, providing ssh access to a committer to run experiments to try
to resolve the issue.


Required ports
==============

The worker operates as a *client* to the *buildmaster*.  This means that
all network connections are *outbound*.  This is true also for the network
tests in the test suite.  Most consumer firewalls will allow any outbound
traffic, so normally you do not need to worry about what ports the buildbot
uses.  However, corporate firewalls are sometimes more restrictive, so here is
a table listing all of the outbound ports used by the buildbot and the python
test suite (this list may not be complete as new tests may have been added
since this table was last vetted):

======= ========================== ================================================
Port    Host                       Description
======= ========================== ================================================
20, 21  ftp.debian.org             test_urllib2net
53      your DNS server            test_socket, and others implicitly
80      python.org                 (several tests)
        example.com
119     news.gmane.org             test_nntplib (Python versions < 3.13)
443     (various)                  test_ssl
465     smtp.gmail.com             test_smtpnet
587     smtp.gmail.com             test_smtpnet
9020    buildbot-api.python.org    connection to buildmaster
======= ========================== ================================================

Many tests will also create local TCP sockets and connect to them, usually
using either ``localhost`` or ``127.0.0.1``.


Required resources
==================

Based on the last time we did a `survey
<https://mail.python.org/pipermail/python-dev/2012-March/117978.html>`__ on
buildbot requirements, the recommended resource allocations for a python
buildbot are at least:

* 2 CPUs
* 512 MB RAM
* 30 GB free disk space

Many tests won't run in this configuration, since they require
substantially more memory, but these resources should be sufficient.
Builders with minimal settings might need more maintenance: they check
that Python's resource-hungry tests are tagged and skipped correctly.


Security considerations
=======================

We only allow builds to be triggered against commits to the
`CPython repository on GitHub <https://github.com/python/cpython>`__.
This means that the code your buildbot will run will have been vetted by a committer.
However, mistakes and bugs happen, as could a compromise, so keep this in mind when
siting your buildbot on your network and establishing the security around it.
Treat the buildbot like you would any resource that is public facing and might
get hacked (use a VM and/or jail/chroot/solaris zone, put it in a DMZ, and so on).
While the buildbot does not have any ports open for inbound traffic (and is not
public facing in that sense), committer mistakes do happen, and security flaws
are discovered in both released and unreleased code, so treating the buildbot
as if it were fully public facing is a good policy.

Code runs differently as privileged and unprivileged users.  We would love to
have builders running as privileged accounts, but security considerations do
make that difficult, as access to root can provide access to surprising
resources (such as spoofed IP packets, changes in MAC addresses, and so on) even on a
VM setup.  But if you are confident in your setup, we'd love to have a buildbot
that runs python as root.

Note that the above is a summary of a `discussion
<https://mail.python.org/pipermail/python-dev/2011-October/113935.html>`__ on
python-dev about buildbot security that includes examples of the tests for
which privilege matters.  There was no final consensus, but the information is
useful as a point of reference.

.. [#] If the buildbot is going to do Framework builds, it is better to
       use the Apple-shipped Python so as to avoid any chance of the buildbot
       picking up components from the installed python.org python.

.. _builders: https://buildbot.python.org/#/builders
