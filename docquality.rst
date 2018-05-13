.. _docquality:

Helping with Documentation
==========================

Python is known for having well-written documentation. Maintaining the
documentation's accuracy and keeping a high level of quality takes a lot of
effort. Community members, like you, help with writing, editing, and updating
content, and these contributions are appreciated and welcomed.

This high-level **Helping with Documentation** section provides:

* an overview of Python's documentation
* how to help with documentation issues
* information on proofreading
* guidance on contributing to this Developer's Guide

The next chapter, :ref:`Documenting Python <documenting>`, gives extensive,
detailed information on how to write documentation and submit changes.


Python Documentation
--------------------

The :ref:`Documenting Python <documenting>` section covers the details of how
Python's documentation works. It includes information about the markup
language used, specific formats, and style recommendations. Looking at
pre-existing documentation source files can be very helpful when getting
started. :ref:`How to build the documentation <building-doc>` walks you through
the steps to create a draft build which lets you see how your changes will look
and validates that your new markup is correct.

You can view the documentation built from :ref:`in-development <indevbranch>`
and :ref:`maintenance <maintbranch>` branches at https://docs.python.org/dev/.
The in-development and most recent 3.x (as well as 2.x) maintenance 
:ref:`branches <listbranch>` are rebuilt once per day.

If you would like to be more involved with documentation, consider subscribing
to the `docs@python.org <https://mail.python.org/mailman/listinfo/docs>`_
mailing list. The `issue tracker`_ sends new documentation issues to this 
mailing list, and, less frequently, the list receives some directly mailed bug
reports. The `docs-sig@python.org <https://mail.python.org/mailman/listinfo/doc-sig>`_ 
mailing list discusses the documentation toolchain, projects, and standards.


Helping with documentation issues
---------------------------------

If you look at `documentation issues`_ on the `issue tracker`_, you
will find various documentation problems that may need work. Issues vary from
typos to unclear documentation and items lacking documentation.

If you see a documentation issue that you would like to tackle, you can:

* check to see if there is a paperclip or `octocat`_ icon at the end of the 
  issue's title column.  If there is, then someone has already created a pull
  request for the issue.
* leave a comment on the issue saying you are going to try and create a pull 
  request and roughly how long you think you will take to do so (this allows 
  others to take on the issue if you happen to forget or lose interest).
* submit a :doc:`pull request <pullrequest>` for the issue. 

By following the steps in the :ref:`Quick Guide to Pull Requests <pullrequest-quickguide>`,
you will learn the workflow for documentation pull requests.

.. _issue tracker: https://bugs.python.org
.. _documentation issues: https://bugs.python.org/issue?%40search_text=&ignore=file%3Acontent&title=&%40columns=title&id=&%40columns=id&stage=&creation=&creator=&activity=&%40columns=activity&%40sort=activity&actor=&nosy=&type=&components=4&versions=&dependencies=&assignee=&keywords=6&priority=&status=1&%40columns=status&resolution=&nosy_count=&message_count=&%40group=&%40pagesize=100&%40startwith=0&%40sortdir=on&%40queryname=&%40old-queryname=&%40action=search
.. _octocat: https://github.com/logos


Proofreading
------------

While an issue filed on the `issue tracker`_ means there is a known issue
somewhere, that does not mean there are not other issues lurking about in the
documentation. Proofreading a part of the documentation, such as a "How to" or
OS specific document, can often uncover problems (e.g., documentation that
needs updating for Python 3).

If you decide to proofread, read a section of the documentation from start
to finish, filing issues in the issue tracker for each major type of problem
you find. Simple typos don't require issues of their own, but, instead, submit
a pull request directly. It's best to avoid filing a single issue for an entire
section containing multiple problems; instead, file several issues so that it
is easier to break the work up for multiple people and more efficient review.


.. _helping-with-the-developers-guide:

Helping with the Developer's Guide
----------------------------------

.. highlight:: console

The Developer's Guide (what you're reading now) uses the same process as the
main Python documentation, except for some small differences.  The source
lives in a `separate repository`_ and bug reports should be submitted to the
`devguide GitHub tracker`_.

Our devguide workflow uses continuous integration and deployment so changes to
the devguide are normally published when the pull request is merged. Changes
to CPython documentation follows the workflow of a CPython release and is
published in the release.


Developer's Guide workflow
--------------------------

To submit a :doc:`pull request <pullrequest>`, you can fork the
`devguide repo`_ to your GitHub account and clone it using::

    $ git clone https://github.com/<your_username>/devguide

For your PR to be accepted, you will also need to sign the
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

You will find the generated files in ``_build/html``. Note that ``make check``
runs automatically when you submit a :doc:`pull request <pullrequest>`. You may
wish to run ``make check`` and ``make linkcheck`` to make sure that it runs
without errors.

.. _separate repository:
.. _devguide repo: https://github.com/python/devguide
.. _devguide GitHub tracker: https://github.com/python/devguide/issues
.. _Sphinx: http://www.sphinx-doc.org/
