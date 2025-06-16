============
Coordinating
============

Python documentation translations are governed by :PEP:`545`.
They are built by `docsbuild-scripts
<https://github.com/python/docsbuild-scripts/>`__ and hosted on
docs.python.org.

Starting a new translation
==========================

First subscribe to the `translation mailing list <translation_ml_>`_,
and introduce yourself and the translation you're starting. Translations
fall under the aegis of the `PSF Translation Workgroup <translation_wg_>`_

.. https://github.com/python/editorial-board/issues/32

Then you can bootstrap your new translation by using `cookiecutter
<https://github.com/JulienPalard/python-docs-cookiecutter>`__ or
`bootstrapper <https://github.com/python-docs-translations/python-docs-bootstrapper>`__.

The important steps look like this:

- Create the GitHub repo (any account) with the correct hierarchy by using one
  of the bootstrappers.
- Gather people to help you translate. You can't do it alone.
- You can use any tool to translate, as long as you can synchronize with Git.
  Some use Transifex, and some use only GitHub. You can choose another
  way if you like; it's up to you.
- Update :doc:`this page <translating>` to reflect your work and progress, either via a
  PR or by asking on the `translation mailing list <translation_ml_>`_.
- When ``bugs``, ``tutorial``, and ``library/functions`` are 100%
  completed, ask on the `translation mailing list <translation_ml_>`_ for
  your language to be added in the language switcher on docs.python.org.


How to get help
===============

Discussions about translations occur on the Python Docs Discord
`#translations channel <https://discord.gg/h3qDwgyzga>`_, `translation
mailing list <translation_ml_>`_, and and the
`translations subsection <https://discuss.python.org/c/documentation/translations/>`_
of the Python Discourse.


PEP 545 summary
===============

Here are the essential points of :PEP:`545`:

- Each translation is assigned an appropriate lowercased language tag,
  with an optional region subtag, and joined with a dash, like
  ``pt-br`` or ``fr``.

- Each translation is under CC0 and marked as such in the README (as in
  the cookiecutter).

- Translation files are hosted on
  ``https://github.com/python/python-docs-{LANGUAGE_TAG}`` (not
  mandatory to start a translation, but mandatory to land on
  ``docs.python.org``).

- Translations having completed ``tutorial/``, ``library/stdtypes``
  and ``library/functions`` are hosted on
  ``https://docs.python.org/{LANGUAGE_TAG}/{VERSION_TAG}/``.


Coordinating FAQ
================

Are there tools to help in managing the repo?
---------------------------------------------

Here's what we're using:

- :pypi:`pomerge` to propagate translations from one file to others.
- :pypi:`pospell` to check for typos in ``.po`` files.
- :pypi:`powrap` to rewrap the ``.po`` files
  before committing. This helps keep Git diffs short.
- :pypi:`potodo` to list what needs to be translated.
- :pypi:`sphinx-lint` to validate reST syntax in translation files.

More related tools and projects can be found in the
`python-docs-translations`__ organisation on GitHub.

__ https://github.com/python-docs-translations

How is a coordinator elected?
-----------------------------

There is no election. Each translation will sort out the number of coordinators.
We recommend 2 or 3 coordinators, though you may begin with one.  Here are some general suggestions.

-  Coordinator requests are to be public on the `translation mailing list <translation_ml_>`_.
-  If the given language has a native core dev, the core dev has input
   on the coordinator request.
-  Anyone who wants to become coordinator for their native language and shows
   motivation by translating and building a community will be named
   coordinator.
-  We expect the local community to self-organize coordinators and contributors.
   If you have questions, please ask on the mailing list or Discourse.
-  If a coordinator becomes inactive or unreachable for a long
   period of time, someone else can ask to be added as a primary coordinator on the `translation mailing list <translation_ml_>`_.
   As a community resource, we aim to keep translations up to date with active contributors, including coordinators.

I have a translation, but it's not in Git. What should I do?
------------------------------------------------------------

You can ask for help on the `translation mailing list <translation_ml_>`_, and
the team will help you create an appropriate repository. You can still use tools like transifex,
if you like.


My Git hierarchy does not match yours. Can I keep it?
-----------------------------------------------------

No, inside the ``github.com/python`` organization we’ll all have the
exact same hierarchy so bots will be able to build all of our
translations. So you may have to convert from one hierarchy to another.
Ask for help on the `translation mailing list <translation_ml_>`_ if you’re
not sure on how to do it.


What hierarchy should I use in my GitHub repository?
----------------------------------------------------

As for every project, we have a *branch* per version.  We store ``.po``
files in the root of the repository using the ``gettext_compact=0``
style.


.. XXX Explain necessary folder structure


Which version of the Python documentation should be translated?
---------------------------------------------------------------

Consensus is to work on the current stable version. You can then propagate your
translation from one branch to another using :pypi:`pomerge`.


The entry for my translation is missing/not up to date
------------------------------------------------------

Ask on the `translation mailing list <translation_ml_>`_, or better, make a PR on the `devguide
<https://github.com/python/devguide/>`__.


Is there a Weblate instance we can translate on?
------------------------------------------------

There is currently no Weblate instance for use by Python translations because of
certain limitations, these include word count limits and organization of
translation source.

.. _translation_wg: https://wiki.python.org/psf/TranslationWG/Charter
.. _translation_ml: https://mail.python.org/mailman3/lists/translation.python.org/
