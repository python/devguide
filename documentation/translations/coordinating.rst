============
Coordinating
============

Starting a new translation
==========================

First subscribe to the `translation mailing list <translation_ml_>`_,
and introduce yourself and the translation you're starting. Translations
fall under the aegis of the `PSF Translation Workgroup <translation_wg_>`_

Then you can bootstrap your new translation by using `cookiecutter
<https://github.com/JulienPalard/python-docs-cookiecutter>`__ or
`bootstrapper <https://github.com/python-docs-translations/python-docs-bootstrapper>`__.

The important steps look like this:

- Create the GitHub repo (anywhere) with the right hierarchy (using one
  of the bootstrappers).
- Gather people to help you translate. You can't do it alone.
- You can use any tool to translate, as long as you can synchronize with Git.
  Some use Transifex, and some use only GitHub. You can choose another
  way if you like; it's up to you.
- Ensure we update this page to reflect your work and progress, either via a
  PR or by asking on the `translation mailing list <translation_ml_>`_.
- When ``bugs``, ``tutorial``, and ``library/functions`` are 100%
  completed, ask on the `translation mailing list <translation_ml_>`_ for
  your language to be added in the language switcher on docs.python.org.


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

There is no election; each translation has to sort this out.  Here are some suggestions.

-  Coordinator requests are to be public on the `translation mailing list <translation_ml_>`_.
-  If the given language has a native core dev, the core dev has their
   say on the choice.
-  Anyone who wants to become coordinator for their native language and shows
   motivation by translating and building a community will be named
   coordinator.
-  In case of concurrency between two persons, no one will sort this out
   for you.  It is up to you two to organize a local election or whatever is
   needed to sort this out.
-  If a coordinator becomes inactive or unreachable for a long
   period of time, someone else can ask for a takeover on the `translation mailing list <translation_ml_>`_.

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


The entry for my translation is missing/not up to date on this page
-------------------------------------------------------------------

Ask on the `translation mailing list <translation_ml_>`_, or better, make a PR on the `devguide
<https://github.com/python/devguide/>`__.
