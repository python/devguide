.. _docquality:

Helping with Documentation
==========================

Python is known for having good documentation. But maintaining all of it and
keeping a high level of quality takes a lot of effort. Help is always
appreciated with the documentation, and it requires little programming
experience (with or without Python).

`Documenting Python`_ covers the details of how Python's documentation works.
It includes an explanation of the markup used (although you can figure a lot
out simply by looking at pre-existing documentation) and how to build the
documentation (which allows you to see how your changes will look along with
validating that your new markup is correct).

The current in-development version of the documentation is available at
http://docs.python.org/dev/. It is re-generated from source once a day from the
``Doc/tools/dailybuild.py`` script as found in Python's source tree.

If you would like a technical documentation style guide, the `Apple
Publications Style Guide
<http://developer.apple.com/mac/library/documentation/UserExperience/Conceptual/APStyleGuide/APSG_2009.pdf>`_
is recommended.

If you care to get more involved with documentation, you may also consider
subscribing to the
`docs@python.org mailing list <http://mail.python.org/mailman/listinfo/docs>`_.
Documentation issues reported on the `issue tracker`_ are sent here as well as
some bug reports being directly emailed to the mailing list. There is also the
`docs-sig@python.org mailing list
<http://mail.python.org/mailman/listinfo/doc-sig>`_ which discusses the
documentation toolchain, projects, standards, etc.

.. _Documenting Python: http://docs.python.org/py3k/documenting/index.html


Helping with issues filed on the issue tracker
----------------------------------------------

If you look at `issues assigned to docs@python`_ on the `issue tracker`_, you
will find various documentation problems that need work. Issues vary from
typos, to unclear documentation, to something completely lacking documentation.

If you decide to tackle a documentation issue, you simply :ref:`create a patch
<patch>` for the issue and upload it. If you are worried that someone else might
be working simultaneously on the issue, simply leave a comment on the issue
saying you are going to try and create a patch and roughly how long you think
you will take to do it (this allows others to take on the issue if you happen
to forget or lose interest).

.. _issue tracker: http://bugs.python.org
.. _issues assigned to docs@python: http://bugs.python.org/issue?%40sort0=activity&%40sortdir0=on&%40sort1=creation&%40sortdir1=on&%40group0=priority&%40group1=&%40columns=title%2Cid%2Cactivity%2Cstatus&%40filter=assignee%2Cstatus&status=1&assignee=12260&%40pagesize=50&%40startwith=0




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
