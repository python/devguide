.. highlight:: console

.. _sprintguide:

PyCon Sprint Guide
==================

This guide is written for PyCon US 2017 sprint.  For other sprints, we may need
to come up with a different set of easy b.p.o. issues.

Everyone at the sprint needs to follow the `PSF Code of Conduct <http://python.org/psf/codeofconduct/>`_.


.. contents::

Installations
-------------

The following resources take time to download.  You may not want to rely on the
on the conference venue's wifi to download these.  Do them before you come to
the sprint.

#. Go through the :ref:`setup` guide.  Install the necessary dependencies
   for your machine.

#. Install sphinx v1.6.1::

      pip install sphinx~=1.6.1

#. Fork and clone the CPython repo.  Set your clone as the ``origin``, and
   ``https://github.com/python/cpython`` as ``upstream``.

#. Fork and clone the Dev Guide repo. Set your clone as the ``origin``, and
   ``https://github.com/python/devguide`` as ``upstream``.

Reading materials
-----------------

#. :ref:`Quick Start <index>` section of CPython Developer's Guide.

#. :ref:`Documenting Python <documenting>`.

#. :ref:`gitbootcamp`.

#. :ref:`exploring`.

#. :ref:`helptriage`.

Others
------

#. The bug tracker is at:  https://bugs.python.org

#. Create an account at the bug tracker.

#. Link your GitHub account to the bug tracker account.

#. Sign the :ref:`CLA <licensing>`.

Communication
-------------

#. Core-mentorship `mailing list <https://mail.python.org/mailman/listinfo/core-mentorship/>`_.

#. Comment on the issue, say that you're working on it. If an issue is assigned,
   please ask first.

#. #python-dev on `freenode <http://webchat.freenode.net/>`_.


Dev Guide Issues
----------------

#. Document git worktree `python/devguide#105 <https://github.com/python/devguide/issues/105>`_.

#. Mention the "Green Tree Snakes" AST guide `python/devguide#184 <https://github.com/python/devguide/issues/184>`_.

#. Clarify policy of personal branches `python/devguide#191 <https://github.com/python/devguide/issues/191>`_.

#. Document how to apply mercurial patch to git `python/devguide#193 <https://github.com/python/devguide/issues/193>`_.

#. Promote helping with reviews `python/devguide#194 <https://github.com/python/devguide/issues/194>`_.

#. Improve commit message `python/devguide#199 <https://github.com/python/devguide/issues/199>`_.

#. Mention the core-workflow mailing list / repo `python/devguide#202 <https://github.com/python/devguide/issues/202>`_.


Easy B.P.O Issues
-----------------

These issues have been set aside for first time contributors only.  If you've
contributed before, you'll find other issues to be more challenging.

#. Docs example: converting mixed types to floating point `bpo-30361 <https://bugs.python.org/issue30361>`_.

#. Small correction in set code sample `bpo-30312 <https://bugs.python.org/issue30312>`_.

#. sum() function docstring lists arguments incorrectly `bpo-23787 <https://bugs.python.org/issue23787>`_.

#. asyncio: set_write_buffer_limits() doc doesn't specify unit of the parameters `bpo-29933 <https://bugs.python.org/issue29933>`_.

#. socket module missing IPPROTO_IPV6, IPPROTO_IPV4 on Windows `bpo-29515 <https://bugs.python.org/issue29515>`_.

Other B.P.O Issues
------------------

These issues are more complicated and require some API design.

#. Please provide a way to disable the warning printed if the signal module's wakeup fd overflows `bpo-30050 <https://bugs.python.org/issue30050>`_.

#. Modernize pydoc to use better HTML and separate CSS `bpo-10716 <http://bugs.python.org/issue10716>`_.

#. Command-line option to suppress "from None" for debugging `bpo-30097 <http://bugs.python.org/issue30097>`_.


Other Long Term Project Ideas
-----------------------------

#. Help port your favorite python library from 2 to 3.

#. The newer features of the language could use more help in documentation.
   For example, write a howto/tutorial for asyncio (`bpo-30145 <https://bugs.python.org/issue30145>`_) or typing.

#. Research and design a replacement for ``pprint``.

#. Convert text based PEPs to reST `python/peps#4 <https://github.com/python/peps/issues/4>`_


Other Ways to Contribute
------------------------

There are various ways to contribute to open source projects and to Python.  It
doesn't always invlove writing code and submitting patches.

#. Help review open pull requests.

#. Apply and test patches on your machine.

#. Issue triage.

#. Be positive.

