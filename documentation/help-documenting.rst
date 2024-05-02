.. _help-documenting:
.. _docquality:

==========================
Helping with documentation
==========================

Python is known for having well-written documentation. Maintaining the
documentation's accuracy and keeping a high level of quality takes a lot of
effort. Community members, like you, help with writing, editing, and updating
content, and these contributions are appreciated and welcomed.

This high-level **Helping with Documentation** section provides:

* an overview of Python's documentation
* how to help with documentation issues
* information on proofreading

You will find extensive and detailed information on how to write documentation
and submit changes on the :ref:`Documenting Python <documenting>` page.


Python documentation
====================

The :ref:`Documenting Python <documenting>` section covers the details of how
Python's documentation works. It includes information about the markup
language used, specific formats, and style recommendations. Looking at
pre-existing documentation source files can be very helpful when getting
started. :ref:`How to build the documentation <building-doc>` walks you through
the steps to create a draft build which lets you see how your changes will look
and validates that your new markup is correct.

You can view the documentation built from :ref:`in-development <indevbranch>`
and :ref:`maintenance <maintbranch>` branches at https://docs.python.org/dev/.
The in-development and recent maintenance branches are rebuilt once per day.

If you would like to be more involved with documentation, consider subscribing
to the `Documentation category on the Python Discourse
<https://discuss.python.org/c/documentation/26>`_ and the
`docs@python.org <https://mail.python.org/mailman3/lists/docs.python.org/>`_ mailing list
where user issues are raised and documentation toolchain, projects, and standards
are discussed.


Helping with documentation issues
=================================

If you look at `documentation issues`_ on the `issue tracker`_, you
will find various documentation problems that may need work. Issues vary from
typos to unclear documentation and items lacking documentation.

If you see a documentation issue that you would like to tackle, you can:

* check to see if there is pull request icon to the right of the issue's title,
  or an open pull request listed under :guilabel:`Linked PRs` in the issue body.
  If there is, then someone has already created a pull
  request for the issue.
* leave a comment on the issue saying you are going to try and create a pull
  request and roughly how long you think you will take to do so (this allows
  others to take on the issue if you happen to forget or lose interest).
* submit a :ref:`pull request <pullrequest>` for the issue.

By following the steps in the :ref:`Quick Guide to Pull Requests <pullrequest-quickguide>`,
you will learn the workflow for documentation pull requests.

.. _documentation issues: https://github.com/python/cpython/issues?q=is%3Aissue+is%3Aopen+label%3Adocs
.. _octocat: https://github.com/logos


Proofreading
============

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

For help with the finer points of English technical writing, mention the
`@python/proofreaders <https://github.com/orgs/python/teams/proofreaders>`__
team in your issue or pull request in any `@python <https://github.com/python/>`__
repo. If you'd like to join the team,
`open a core-workflow issue <https://github.com/python/core-workflow/issues/new/choose>`__
similar to
`python/core-workflow#461 <https://github.com/python/core-workflow/issues/461>`__.

.. _issue tracker: https://github.com/python/cpython/issues
