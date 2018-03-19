.. _docquality:

Helping with Documentation
==========================

Python is known for having good documentation. But maintaining all of it and
keeping a high level of quality takes a lot of effort. Help is always
appreciated with the documentation, and it requires little programming
experience (with or without Python).


Python Documentation
--------------------

:ref:`Documenting Python <documenting>` covers the details of how Python's
documentation works.
It includes an explanation of the markup used (although you can figure a lot
out simply by looking at pre-existing documentation) and :ref:`how to build
<building-doc>` the documentation (which allows you to see how your changes
will look along with validating that your new markup is correct).

The documentation built from the :ref:`in-development <indevbranch>` and
:ref:`maintenance <maintbranch>` branches can be viewed from
https://docs.python.org/dev/.  The in-development and most recent 2.x and 3.x
maintenance :ref:`branches <listbranch>` are rebuilt once per day.

If you care to get more involved with documentation, you may also consider
subscribing to the
`docs@python.org mailing list <https://mail.python.org/mailman/listinfo/docs>`_.
Documentation issues reported on the `issue tracker`_ are sent here as well as
some bug reports being directly emailed to the mailing list. There is also the
`docs-sig@python.org mailing list
<https://mail.python.org/mailman/listinfo/doc-sig>`_
which discusses the documentation toolchain, projects, standards, etc.


Helping with issues filed on the issue tracker
----------------------------------------------

If you look at `documentation issues`_ on the `issue tracker`_, you
will find various documentation problems that may need work. Issues vary from
typos, to unclear documentation, to something completely lacking documentation.

If you decide to tackle a documentation issue, you can simply submit a
:doc:`pull request <pullrequest>` for the issue. If you are worried that someone
else might be working simultaneously on the issue, first check to see if there
is a paperclip or `octocat`_ icon at the end of the title column.  If there
is, then someone has already attached a patch or created a pull request for the
issue.  If there aren't any icons, then simply leave a comment on the issue
saying you are going to try and create a pull request and roughly how long
you think you will take to do it (this allows others to take on the issue if
you happen to forget or lose interest).

.. _issue tracker: https://bugs.python.org
.. _documentation issues: https://bugs.python.org/issue?%40search_text=&ignore=file%3Acontent&title=&%40columns=title&id=&%40columns=id&stage=&creation=&creator=&activity=&%40columns=activity&%40sort=activity&actor=&nosy=&type=&components=4&versions=&dependencies=&assignee=&keywords=6&priority=&status=1&%40columns=status&resolution=&nosy_count=&message_count=&%40group=&%40pagesize=100&%40startwith=0&%40sortdir=on&%40queryname=&%40old-queryname=&%40action=search
.. _octocat: https://github.com/logos


Proofreading
------------

While an issue filed on the `issue tracker`_ means there is a known issue
somewhere, that does not mean there are not other issues lurking about in the
documentation. Simply proofreading parts of the documentation is enough to
uncover problems (e.g., documentation that needs to be updated for Python 3
from Python 2).

If you decide to proofread, then read a section of the documentation from start
to finish, filing issues in the issue tracker for each problem you find. Simple
typos don't require an issue of their own, instead submit a pull request
directly.
Don't file a single issue for an entire section containing multiple problems as
that makes it harder to break the work up for multiple people to help with.


.. _helping-with-the-developers-guide:

Helping with the Developer's Guide
----------------------------------

.. highlight:: console

The Developer's Guide (what you're reading now) uses the same process as the
main Python documentation, except for some small differences.  The source
lives in a `separate repository`_ and bug reports should be submitted to
`its GitHub tracker`_.

To submit a :doc:`pull request <pullrequest>` you can fork the
`devguide repo`_ to your GitHub account and clone it using::

    $ git clone https://github.com/<your_username>/devguide

In order for your PR to be accepted, you will also need to sign the
:ref:`contributor agreement <cla>`.

To build the devguide, some additional dependencies are required (most
importantly, `Sphinx`_), and the standard way to install dependencies in
Python projects is to create a virtualenv, and then install dependencies from
a ``requirements.txt`` file. For your convenience, this is all *automated for
you*. To build the devguide on a Unix-like system use::

   $ make html

in the checkout directory. On Windows use:

.. code-block:: doscon

   > .\make html

You will find the generated files in ``_build/html``.
Note that ``make check`` is automatically run when
you submit a :doc:`pull request <pullrequest>`, so you should make
sure that it runs without errors.

Changes to the devguide are normally published within a day, on a schedule
that may be different from the main documentation.

.. _separate repository:
.. _devguide repo: https://github.com/python/devguide
.. _its GitHub tracker: https://github.com/python/devguide/issues
.. _Sphinx: http://www.sphinx-doc.org/
