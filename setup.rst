.. _setup:

Getting Set Up
==============

These instructions cover how to get a source checkout and a compiled version of
the CPython interpreter (CPython is the version of Python available from
http://www.python.org/). It will also tell you how to set up various code
editors. Finally, this document also gives an overview of the directory
structure of a CPython checkout.

.. contents::


Version Control Setup
---------------------

CPython is developed using svn_. Make sure the following settings are in your
svn config file (``~/.subversion/config`` under UNIX)::

 [miscellany]
 enable-auto-props = yes

 [auto-props]
 * = svn:eol-style=native
 *.c = svn:keywords=Id
 *.h = svn:keywords=Id
 *.py = svn:keywords=Id
 *.txt = svn:keywords=Author Date Id Revision

The ``[auto-props]`` line specifies the beginning of the section in the config
file dealing with svn properties and line endings. The ``svn:eol-style``
setting tells Subversion to check out files using the native line endings on
your OS.  It will also automatically convert line endings upon committal so
that they are consistent across all platforms.  The ``svn:keywords`` settings
are to automatically substitute ``$keyword$`` arguments in files that match the
pattern.  ``*.txt`` has more options so as to cover all needed keywords for
PEPs_.

The ``[miscellany]`` section and its one option make svn apply the
various rules in the ``[auto-props]`` section automatically to all added or
imported files into the respository.

.. _svn: http://subversion.tigris.org/


Checking out the code
----------------------

One should always work from a checkout of the CPython source code. While it may
be tempting to work from the downloaded copy you already have installed on your
machine, it is very likely that you will be working from out-of-date code as
the Python core developers are constantly updating and fixing things in their
:abbr:`VCS`. It also means you will have better tool
support through the VCS as it will provide a diff tool, etc.

To get a read-only checkout of CPython's source, you need to checkout the source
code. To get a read-only checkout of
the in-development branch of Python (core developers should read XXX for a
read-write checkout), run::

    svn co http://svn.python.org/projects/python/branches/py3k

If you want a read-only checkout of an already-released version of Python,
i.e., a version in maintenance mode, run something like the following which
gets you a checkout for Python 3.1::

    svn co http://svn.python.org/projects/python/branches/release31-maint

To check out a version of Python other than 3.1, simply change the number in
the above URL to the major/minor version (e.g., ``release27-maint`` for Python
2.7).

Do note that CPython will notice that it is being run from a source checkout.
This means that it if you edit Python source code in your checkout the changes
will be picked up by the interpreter for immediate testing.


Compiling (for debugging)
-------------------------

Python has two features to aid in developing for it. First, there is a
``Py_DEBUG`` compilation flag which turns on some features in the interpreter
which will help with debugging. While this is not the only compilation flag
available (see ``Misc/SpecialBuilds.txt`` in a checkout for all of them), it is
the basic one that you should always use as it tends to catch bugs more often
than running a build of Python without the flag.

The other feature is support for using code directly from a checkout of Python.
This is handy as it means you do not need to install your build of Python but
can just use the build in-place. It also means that when you edit code in your
checkout you get to see the results without having to install the changed files
as well.

The steps to compile a debug version of Python are specified in the `dev FAQ`_.


Editors and Tools
==================

Python includes within its source tree some files to help work with various
popular editors and tools. A list of those tools and what is available for them
can be found in the `dev FAQ`_.


Directory Structure
===================

There are several top-level directories in the Python source tree. Knowing what
which one is meant to hold will help you find where a certain piece of
functionality is implemented. Do realize, though, there are always exceptions to
every rule.

``Doc``
     The official documentation. This is what http://docs.python.org/ uses. The
     tools for building the documentation is kept in another repository. To
     build the docs, see ``Doc/README.txt``.

``Grammar``
     Contains the EBNF grammar file for Python.

``Include``
     Contains all interpreter-wide header files.

``Lib``
     The part of the standard library implemented in pure Python is here.

``Mac``
     Mac-specific code for things such as using IDLE as an OS X application.

``Misc``
     Things that do not belong elsewhere. Typically this is varying kinds of
     documentation.

``Modules``
     The part of the standard library (plus some other code) that is implemented
     as extension modules.

``Objects``
     Code for all built-in types.

``PC``
     Windows-specific code along with build files for VC 6, 7, & 8 along with
     OS/2.

``PCbuild``
     Build files for VC 9 and newer.

``Parser``
     Code related to the parser. The definition of the AST nodes is also kept
     here.

``Python``
     The code that makes Python run. This includes the compiler, eval loop and
     various built-in modules.

``Tools``
     Various tools that are (or have been) used to maintain Python.


.. _dev FAQ: XXX
