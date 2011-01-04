Getting Set Up
==============

.. contents::


Checking out the code
=====================

Python always has the in-development version of the current major versions
along with the last minor release of each major version. For instance, if
Python 2.6 was the latest release (and thus has a major version of *2* and a
minor version of *6*), then the in-development 2.7 branch is available along
with the maintenance branch for 2.6.

For each branch there is read-only access for the general public and read-write
access for those with commit privileges (called "core developers"). The
location of these branches and the steps to check out the code are listed in
the `dev FAQ`_.


Compiling for debugging
=======================

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
