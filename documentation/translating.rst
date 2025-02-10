.. _translating:

===========
Translating
===========

.. highlight::  rest

Python documentation translations are governed by :PEP:`545`.
They are built by `docsbuild-scripts
<https://github.com/python/docsbuild-scripts/>`__ and hosted on
docs.python.org. There are several documentation translations already
in production; others are works in progress. See `the dashboard
<https://m-aciek.github.io/pydocs-translation-dashboard/>`__ for
details.

.. list-table::
   :header-rows: 1

   * - Language
     - Contact
     - Links
   * - Arabic (ar)
     - Abdur-Rahmaan Janhangeer (:github-user:`Abdur-rahmaanJ`)
     - :github:`GitHub <Abdur-rahmaanJ/python-docs-ar>`
   * - Bengali as spoken in India (bn_IN)
     - Kushal Das (:github-user:`Kushal997-das`)
     - :github:`GitHub <python/python-docs-bn-in>`
   * - `French (fr) <https://docs.python.org/fr/>`__
     - Julien Palard (:github-user:`JulienPalard`)
     - :github:`GitHub <python/python-docs-fr>`
   * - Greek (gr)
     - Lysandros Nikolaou (:github-user:`lysnikolaou`),
       Fanis Petkos (:github-user:`thepetk`),
       Panagiotis Skias (:github-user:`skpanagiotis`)
     - :github:`GitHub <pygreece/python-docs-gr>`
   * - Hindi as spoken in India (hi_IN)
     - Sanyam Khurana (:github-user:`CuriousLearner`)
     - :github:`GitHub <CuriousLearner/python-docs-hi-in>`
   * - Hungarian (hu)
     - Tamás Bajusz (:github-user:`gbtami`)
     - :github:`GitHub <python/python-docs-hu>`,
       `mailing list <https://mail.python.org/pipermail/python-hu>`__
   * - `Indonesian (id) <https://docs.python.org/id/>`__
     - Oon Arfiandwi (:github-user:`oonid`)
     - :github:`GitHub <python/python-docs-id>`
   * - Italian (it)
     - Alessandro Cucci (`email <mailto:alessandro.cucci@gmail.com>`__)
     - :github:`GitHub <python/python-docs-it>`,
       `original mail <https://mail.python.org/pipermail/doc-sig/2019-April/004114.html>`__
   * - `Japanese (ja) <https://docs.python.org/ja/>`__
     - Kinebuchi Tomohiko (:github-user:`cocoatomo`),
       Atsuo Ishimoto (:github-user:`atsuoishimoto`)
     - :github:`GitHub <python/python-docs-ja>`
   * - `Korean (ko) <https://docs.python.org/ko/>`__
     - 오동권 (:github-user:`flowdas`)
     - :github:`GitHub <python/python-docs-ko>`
   * - Marathi (mr)
     - Sanket Garade (:github-user:`sanketgarade`, `email <mailto:garade@pm.me>`__)
     - :github:`GitHub <sanketgarade/python-doc-mr>`
   * - Lithuanian (lt)
     - Albertas Gimbutas (:github-user:`albertas`, `email <mailto:albertasgim@gmail.com>`__)
     - `Original mail <https://mail.python.org/pipermail/doc-sig/2019-July/004138.html>`__
   * - Persian (fa)
     - Revisto (:github-user:`revisto`)
     - :github:`GitHub <revisto/python-docs-fa>`
   * - `Polish (pl) <https://docs.python.org/pl/>`__
     - Maciej Olko (:github-user:`m-aciek`)
     - :github:`GitHub <python/python-docs-pl>`,
       `Transifex <tx_>`_,
       `original mail <https://mail.python.org/pipermail/doc-sig/2019-April/004106.html>`__
   * - Portuguese (pt)
     - Gustavo Toffo
     -
   * - `Portuguese as spoken in Brasil (pt-br) <https://docs.python.org/pt-br/>`__
     - Marco Rougeth
     - :github:`GitHub <python/python-docs-pt-br>`,
       `wiki <https://python.org.br/traducao/>`__,
       `Telegram <https://t.me/pybr_i18n>`__,
       `article <https://rgth.co/blog/python-ptbr-cenario-atual/>`__
   * - Russian (ru)
     - Daniil Kolesnikov (:github-user:`MLGRussianXP`, `email <mailto:mlgrussianxp@gmail.com>`__)
     - :github:`GitHub <MLGRussianXP/python-docs-ru>`,
       `mail <https://mail.python.org/pipermail/doc-sig/2019-May/004131.html>`__
   * - `Simplified Chinese (zh-cn) <https://docs.python.org/zh-cn/>`__
     - Shengjing Zhu (:github-user:`zhsj`),
       Du, Meng (:github-user:`dumeng`)
     - :github:`GitHub <python/python-docs-zh-cn>`,
       `Transifex <tx_>`_
   * - `Spanish (es) <https://docs.python.org/es/>`__
     - Raúl Cumplido
     - :github:`GitHub <python/python-docs-es>`
   * - `Traditional Chinese (zh-tw) <https://docs.python.org/zh-tw/>`__
     - 王威翔 Matt Wang (:github-user:`mattwang44`),
       Josix Wang
     - :github:`GitHub <python/python-docs-zh-tw>`
   * - `Turkish (tr) <https://docs.python.org/tr/>`__
     - Ege Akman (:github-user:`egeakman`)
     - :github:`GitHub <python/python-docs-tr>`,
       `RTD <https://python-docs-tr.readthedocs.io/>`__
   * - `Ukrainian (uk) <https://docs.python.org/uk/>`__
     - Dmytro Kazanzhy (:github-user:`kazanzhy`, `email <mailto:dkazanzhy@gmail.com>`__)
     - :github:`GitHub <python/python-docs-uk>`,
       `Transifex <tx_>`_

.. _tx: https://explore.transifex.com/python-doc/python-newest/

Starting a new translation
==========================

First subscribe to the `translation mailing list <translation_ml_>`_,
and introduce yourself and the translation you're starting. Translations
fall under the aegis of the `PSF Translation Workgroup <translation_wg_>`_

Then you can bootstrap your new translation by using our `cookiecutter
<https://github.com/JulienPalard/python-docs-cookiecutter>`__.

The important steps look like this:

- Create the GitHub repo (anywhere) with the right hierarchy (using the
  cookiecutter).
- Gather people to help you translate. You can't do it alone.
- You can use any tool to translate, as long as you can synchronize with Git.
  Some use Transifex, and some use only GitHub. You can choose another
  way if you like; it's up to you.
- Ensure we update this page to reflect your work and progress, either via a
  PR or by asking on the `translation mailing list <translation_ml_>`_.
- When ``bugs.html``, ``tutorial``, and ``library/functions`` are 100%
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


How to get help
===============

Discussions about translations occur on the Python Docs Discord
`#translations channel <https://discord.gg/h3qDwgyzga>`_, `translation
mailing list <translation_ml_>`_, and there's a `Libera.Chat IRC
<https://libera.chat/>`_ channel, ``#python-doc``.


Translation FAQ
===============

Which version of the Python documentation should be translated?
---------------------------------------------------------------

Consensus is to work on the current stable version. You can then propagate your
translation from one branch to another using :pypi:`pomerge`.


Are there tools to help in managing the repo?
---------------------------------------------

Here's what we're using:

- :pypi:`pomerge` to propagate translations from one file to others.
- :pypi:`pospell` to check for typos in ``.po`` files.
- :pypi:`powrap` to rewrap the ``.po`` files
  before committing. This helps keep Git diffs short.
- :pypi:`potodo` to list what needs to be translated.
- :pypi:`sphinx-lint` to validate reST syntax in translation files.


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


The entry for my translation is missing/not up to date on this page
-------------------------------------------------------------------

Ask on the `translation mailing list <translation_ml_>`_, or better, make a PR on the `devguide
<https://github.com/python/devguide/>`__.


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


How should I translate code examples?
-------------------------------------

Translate values in code examples (i.e. string literals) and comments.
Don't translate keywords or names,
including variable, function, class, argument, and attribute names.

.. _translation_wg: https://wiki.python.org/psf/TranslationWG/Charter
.. _translation_ml: https://mail.python.org/mailman3/lists/translation.python.org/
