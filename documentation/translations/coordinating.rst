============
Coordinating
============

Information about the Python documentation translation processes is
found in this devguide and :PEP:`545`.
Translations are built by `docsbuild-scripts
<https://github.com/python/docsbuild-scripts/>`__ and hosted on
docs.python.org. Translations
are overseen by the `Editorial Board <EB_>`_

Starting a new translation
==========================

First subscribe to the `translation mailing list <translation_ml_>`_,
and introduce yourself and the translation you're starting.

Then you can bootstrap your new translation by using the `cookiecutter
<https://github.com/python-docs-translations/python-docs-cookiecutter>`__ or
`bootstrapper <https://github.com/python-docs-translations/python-docs-bootstrapper>`__.
You can also start your translation using `Transifex <https://explore.transifex.com/python-doc/python-newest/>`_
following this `guide <https://python-docs-transifex-automation.readthedocs.io/commands.html>`_.

The important steps look like this:

- Create the GitHub repo (any account) with the correct hierarchy by using one
  of the bootstrappers or Transifex.
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
mailing list <translation_ml_>`_, and the
`translations category <https://discuss.python.org/c/documentation/translations/>`_
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


Transifex
=========

If you need help from a Transifex administrator, open an issue on the
`tracker <https://github.com/python-docs-translations/transifex-automations/issues>`_.


Coordinating FAQ
================

Are there tools to help in managing the repo?
---------------------------------------------

Here's what we're using:

- :pypi:`poutils` which includes:

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

Each translation team will decide on the number of coordinators.
We recommend two or three coordinators, though you may begin with one.
Here are some general suggestions.

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

It's best to work on Python's current stable or beta version. You can then
propagate your translation from one branch to another using :pypi:`pomerge`.


The entry for my translation is missing or not up to date
---------------------------------------------------------

Ask on the `translation mailing list <translation_ml_>`_, or better, make a PR
on the `devguide <https://github.com/python/devguide/>`__.


Is there a Weblate instance we can translate on?
------------------------------------------------

There is currently no Weblate instance for Python translations.
See this `Discourse thread <https://discuss.python.org/t/docs-translation-platform/29940>`_
for updates.


.. _EB: https://python.github.io/editorial-board/
.. _translation_ml: https://mail.python.org/mailman3/lists/translation.python.org/
