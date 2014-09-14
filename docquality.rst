.. _docquality:

Helping with Documentation
==========================

Python is known for having good documentation. But maintaining all of it and
keeping a high level of quality takes a lot of effort. Help is always
appreciated with the documentation, and it requires little programming
experience (with or without Python).

:ref:`Documenting Python <documenting>` covers the details of how Python's documentation works.
It includes an explanation of the markup used (although you can figure a lot
out simply by looking at pre-existing documentation) and :ref:`how to build
<building-doc>` the documentation (which allows you to see how your changes
will look along with validating that your new markup is correct).

The documentation built from the :ref:`in-development <indevbranch>` and
:ref:`maintenance <maintbranch>` branches can be viewed from
http://docs.python.org/dev/.  The in-development and most recent 2.x and 3.x
maintenance :ref:`branches <listbranch>` are rebuilt once per day.

If you care to get more involved with documentation, you may also consider
subscribing to the
`docs@python.org mailing list <http://mail.python.org/mailman/listinfo/docs>`_.
Documentation issues reported on the `issue tracker`_ are sent here as well as
some bug reports being directly emailed to the mailing list. There is also the
`docs-sig@python.org mailing list
<http://mail.python.org/mailman/listinfo/doc-sig>`_ which discusses the
documentation toolchain, projects, standards, etc.


Helping with issues filed on the issue tracker
----------------------------------------------

If you look at `documentation issues`_ on the `issue tracker`_, you
will find various documentation problems that need work. Issues vary from
typos, to unclear documentation, to something completely lacking documentation.

If you decide to tackle a documentation issue, you simply :ref:`create a patch
<patch>` for the issue and upload it. If you are worried that someone else might
be working simultaneously on the issue, simply leave a comment on the issue
saying you are going to try and create a patch and roughly how long you think
you will take to do it (this allows others to take on the issue if you happen
to forget or lose interest).

.. _issue tracker: http://bugs.python.org
.. _documentation issues: http://bugs.python.org/issue?%40search_text=&ignore=file%3Acontent&title=&%40columns=title&id=&%40columns=id&stage=&creation=&creator=&activity=&%40columns=activity&%40sort=activity&actor=&nosy=&type=&components=4&versions=&dependencies=&assignee=&keywords=&priority=&%40group=priority&status=1&%40columns=status&resolution=&nosy_count=&message_count=&%40pagesize=50&%40startwith=0&%40queryname=&%40old-queryname=&%40action=search


Proofreading
------------

While an issue filed on the `issue tracker`_ means there is a known issue
somewhere, that does not mean there are not other issues lurking about in the
documentation. Simply proofreading parts of the documentation is enough to
uncover problems (e.g., documentation that needs to be updated for Python 3
from Python 2).

If you decide to proofread, then read a section of the documentation from start
to finish, filing issues in the issue tracker for each problem you find. Don't
file a single issue for an entire section containing multiple problems as that
makes it harder to break the work up for multiple people to help with.


.. _helping-with-the-developers-guide:

Helping with the Developer's Guide
----------------------------------

.. highlight:: bash

The Developer's Guide uses the same process as the main Python documentation,
except for some small differences.  The source lives in a `separate
repository`_.  Bug reports and patches should be submitted to the `Python
bug tracker`_ using the ``devguide`` component.  Changes to the devguide
are normally published within a day, on a schedule that may be different from
the main documentation.

.. _separate repository: https://hg.python.org/devguide
.. _Python bug tracker: http://bugs.python.org

To clone the Developer's Guide::

    $ hg clone https://hg.python.org/devguide

Core developers should use::

    $ hg clone ssh://hg@hg.python.org/devguide

instead so that they can push back their edits to the server.

To build the devguide, you must have `Sphinx`_ installed.  The devguide HTML
can be built by running::

    $ make html

in the checkout directory, which will write the files to the ``_build/html``
directory.

.. _Sphinx: http://sphinx.pocoo.org/
