
.. _buildworker:

Running a buildworker
=====================

.. highlight:: bash

Python's :ref:`buildbots` system was discussed earlier.  We sometimes refer to
the collection of *build workers* as our "buildbot fleet".  The machines that
comprise the fleet are voluntarily contributed resources.  Many are run by
individual volunteers out of their own pockets and time, while others are
supported by corporations.  Even the corporate sponsored buildbots, however,
tend to exist because some individual championed them, made them a reality, and
is committed to maintaining them.

Anyone can contribute a buildbot to the fleet.  This chapter describes how
to go about setting up a buildworker, getting it added, and some hints about
buildbot maintenance.

Anyone running a buildbot that is part of the fleet should subscribe to the
`python-buildbots <https://mail.python.org/mailman/listinfo/python-buildbots>`_
mailing list.  This mailing list is also the place to contact if you want to
contribute a buildbot but have questions.

As for what kind of buildbot to run...take a look at our `current fleet
<http://buildbot.python.org/all/#/builders>`_.  Pretty much anything that isn't
on that list would be interesting: different Linux/UNIX distributions,
different versions of the various OSes, other OSes if you or someone are
prepared to make the test suite actually pass on that new OS.  Even if you only
want to run an OS that's already on our list there may be utility in setting it
up. We also need to build and test python under various alternate build
configurations. Post to the mailing list and talk about what you'd like to
contribute.


Preparing for buildworker setup
-------------------------------

Since the goal is to build Python from source, the system will need to have
everything required to do normal python development:  a compiler, a linker, and
(except on windows) the "development" headers for any of the optional modules
(zlib, OpenSSL, etc) supported by the platform.  Follow the steps outlined in
:ref:`setup` for the target platform, all the way through to having a working
compiled python.

In order to set up the buildbot software, you will need to obtain an identifier
and password for your buildworker so it can join the fleet.  Email
python-buildbots@python.org to discuss adding your buildworker and to obtain the
needed workername and password.  You can do some of the steps that follow
before having the credentials, but it is easiest to have them before
the "buildworker" step below.


Setting up the buildworker
--------------------------

Conventional always-on machines
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need a recent version of the `buildbot <http://buildbot.net/>`_ software,
and you will probably want a separate 'buildbot' user to run the buildbot
software.  You may also want to set the buildbot up using a virtual
environment, depending on how you manage your system.  We won't cover how to that
here; it doesn't differ from setting up a virtual environment for any other
software, but you'll need to modify the sequence of steps below as appropriate
if you choose that path.

For Linux:

    * If your package manager provides the buildbot worker software, that is
      probably the best way to install it; it may create the buildbot user for
      you, in which case you can skip that step.  Otherwise, do ``pip install
      buildbot-worker``.
    * Create a ``buildbot`` user (using, eg: ``useradd``) if necessary.
    * Log in as the buildbot user.

For Mac:

    * Create a buildbot user using the OS/X control panel user admin.  It
      should be a "standard" user.
    * Log in as the buildbot user.
    * Install either the Python 2.7 bundle from python.org [#]_, or pip.
    * Open a terminal window.
    * Execute ``pip install buildbot-worker``.

For Windows:

    * Create a buildbot user as a "standard" user.
    * Install the latest version of Python 2.7 from python.org.
    * Open a Command Prompt.
    * Execute ``python -m pip install pypiwin32 buildbot-worker`` (note that
      ``python.exe`` is not added to ``PATH`` by default, making the
      ``python`` command accessible is left as an exercise for the user).

In a terminal window for the buildbot user, issue the following commands (you
can put the ``buildarea`` wherever you want to)::

    mkdir buildarea
    buildworker create-worker buildarea buildbot.python.org:9020 workername workerpasswd

(Note that on Windows, the ``buildworker`` command will be in the
:file:`Scripts` directory of your Python installation.)

Once this initial worker setup completes, you should edit the files
``buildarea/info/admin`` and ``buildarea/info/host`` to provide your contact
info and information on the host configuration, respectively.  This information
will be presented in the buildbot web pages that display information about the
builders running on your buildworker.

You will also want to make sure that the buildworker is started when the
machine reboots:

For Linux:

    * Add the following line to ``/etc/crontab``::

          @reboot buildworker restart /path/to/buildarea

      Note that we use ``restart`` rather than ``start`` in case a crash has
      left a ``twistd.pid`` file behind.

For OSX:

    * Create a bin directory for your buildbot user::

          mkdir bin

    * Place the following script, named ``run_worker.sh``, into that directory::

          #!/bin/bash
          export PATH=/usr/local/bin:/Library/Frameworks/Python.framework/Versions/2.7/bin:$PATH
          export LC_CTYPE=en_US.utf-8
          cd /Users/buildbot/buildarea
          twistd --nodaemon --python=buildbot.tac --logfile=buildbot.log --prefix=worker

      If you use pip with Apple's system python, add '/System' to the front of
      the path to the Python bin directory.

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

For Windows:

    * Add a Scheduled Task to run ``buildworker start buildarea`` as the
      buildbot user "when the computer starts up".  It is best to provide
      absolute paths to the ``buildworker`` command and the :file:`buildarea`
      directory.  It is also recommended to set the task to run in the
      directory that contains the :file:`buildarea` directory.

    * Alternatively (note: don't do both!), set up the buildworker
      service as described in the `buildbot documentation
      <http://trac.buildbot.net/wiki/RunningBuildbotOnWindows#Service>`_.

To start the buildworker running for your initial testing, you can do::

    buildworker start buildarea

Then you can either wait for someone to make a commit, or you can pick a
builder associated with your buildworker from the `list of builders
<http://buildbot.python.org/all/#/builders>`_ and force a build.

In any case you should initially monitor builds on your builders to make sure
the tests are passing and to resolve any platform issues that may be revealed
by tests that fail.  Unfortunately we do not currently have a way to notify you
only of failures on your builders, so doing periodic spot checks is also a good
idea.


Latent workers
^^^^^^^^^^^^^^

We also support running `latent buildworkers
<http://docs.buildbot.net/current/manual/cfg-workers.html#latent-workers>`_
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
<https://mail.python.org/mailman/listinfo/python-buildbots>`_ list to
request that the master be restarted.

Latent worker should also be updated periodically to include operating system
or other software updates, but when do do such maintenance is largely up to you
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


Buildworker operation
---------------------

Most of the time, running a buildworker is a "set and forget" operation,
depending on the level of involvement you want to have in resolving bugs
revealed by your builders.  There are, however, times when it is helpful or
even necessary for you to get involved.  As noted above, you should be
subscribed to ``python-buildbots@python.org`` so that you will be made
aware of any fleet-wide issues.

Necessary tasks include, obviously, keeping the buildbot running.  Currently
the system for notifying buildbot owners when their workers go offline is not
working; this is something we hope to resolve.  So currently it is helpful if
you periodically check the status of your buildworker.  We will also contact you
via your contact address in ``buildarea/info/admin`` when we notice there is a
problem that has not been resolved for some period of time and you have
not responded to a posting on the python-buildbots list about it.

We currently do not have a minimum version requirement for the buildworker
software.  However, this is something we will probably establish as we tune the
fleet, so another task will be to occasionally upgrade the buildworker software.
Coordination for this will be done via ``python-buildbots@python.org``.

The most interesting extra involvement is when your buildworker reveals a unique
or almost-unique problem:  a test that is failing on your system but not on
other systems.  In this case you should be prepared to offer debugging help to
the people working on the bug: running tests by hand on the buildworker machine
or, if possible, providing ssh access to a committer to run experiments to try
to resolve the issue.


Required Ports
--------------

The buildworker operates as a *client* to the *buildmaster*.  This means that
all network connections are *outbound*.  This is true also for the network
tests in the test suite.  Most consumer firewalls will allow any outbound
traffic, so normally you do not need to worry about what ports the buildbot
uses.  However, corporate firewalls are sometimes more restrictive, so here is
a table listing all of the outbound ports used by the buildbot and the python
test suite (this list may not be complete as new tests may have been added
since this table was last vetted):

======= =================== ================================================
Port    Host                Description
======= =================== ================================================
20, 21  ftp.debian.org      test_urllib2net
53      your DNS server     test_socket, and others implicitly
80      python.org          (several tests)
        example.com
119     news.gmane.org      test_nntplib
443     (various)           test_ssl
465     smtp.gmail.com      test_smtpnet
587     smtp.gmail.com      test_smtpnet
9020    python.org          connection to buildmaster
======= =================== ================================================

Many tests will also create local TCP sockets and connect to them, usually
using either ``localhost`` or ``127.0.0.1``.


Required Resources
------------------

Based on the last time we did a `survey
<https://mail.python.org/pipermail/python-dev/2012-March/117978.html>`_ on
buildbot requirements, the recommended resource allocations for a python
buildbot are at least:

    * 2 CPUs
    * 512 MB RAM
    * 30 GB free disk space

The bigmem tests won't run in this configuration, since they require
substantially more memory, but these resources should be sufficient to ensure
that Python compiles correctly on the platform and can run the rest of the test
suite.


Security Considerations
-----------------------

We only allow builds to be triggered against commits to the CPython repository,
or committer-initiated branches hosted on `GitHub <https://github.com/python/cpython>`_.  This means that the
code your buildbot will run will have been vetted by a committer.  However,
mistakes and bugs happen, as could a compromise, so keep this in mind when
siting your buildbot on your network and establishing the security around it.
Treat the buildbot like you would any resource that is public facing and might
get hacked (use a VM and/or jail/chroot/solaris zone, put it in a DMZ, etc).
While the buildbot does not have any ports open for inbound traffic (and is not
public facing in that sense), committer mistakes do happen, and security flaws
are discovered in both released and unreleased code, so treating the buildbot
as if it were fully public facing is a good policy.

Code runs differently as privileged and unprivileged users.  We would love to
have builders running as privileged accounts, but security considerations do
make that difficult, as access to root can provide access to surprising
resources (such as spoofed IP packets, changes in MAC addresses, etc) even on a
VM setup.  But if you are confident in your setup, we'd love to have a buildbot
that runs python as root.

Note that the above is a summary of a `discussion
<https://mail.python.org/pipermail/python-dev/2011-October/113935.html>`_ on
python-dev about buildbot security that includes examples of the tests for
which privilege matters.  There was no final consensus, but the information is
useful as a point of reference.

.. [#] If the buildbot is going to do Framework builds, it is better to
       use the Apple-shipped Python so as to avoid any chance of the buildbot
       picking up components from the installed python.org python.
