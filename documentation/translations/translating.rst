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
<https://python-docs-translations.github.io/dashboard/>`__ for
details.

.. list-table::
   :header-rows: 1

   * - Language
     - Contact
     - Links
   * - Arabic (ar)
     - Abdur-Rahmaan Janhangeer (:github-user:`Abdur-rahmaanJ`)
     - :github:`GitHub <Abdur-rahmaanJ/python-docs-ar>`
   * - Bengali (bn_IN)
     - Kushal Das (:github-user:`kushaldas`)
     - :github:`GitHub <python/python-docs-bn-in>`
   * - `French (fr) <https://docs.python.org/fr/>`__
     - Julien Palard (:github-user:`JulienPalard`)
     - :github:`GitHub <python/python-docs-fr>`
   * - Greek (gr)
     - Lysandros Nikolaou (:github-user:`lysnikolaou`),
       Fanis Petkos (:github-user:`thepetk`),
       Panagiotis Skias (:github-user:`skpanagiotis`)
     - :github:`GitHub <pygreece/python-docs-gr>`
   * - Hindi (hi_IN)
     - Sanyam Khurana (:github-user:`CuriousLearner`)
     - :github:`GitHub <CuriousLearner/python-docs-hi-in>`
   * - Hungarian (hu)
     - Tamás Bajusz (:github-user:`gbtami`)
     - :github:`GitHub <python/python-docs-hu>`,
       `mailing list <https://mail.python.org/pipermail/python-hu>`__
   * - `Indonesian (id) <https://docs.python.org/id/>`__
     - Irvan Putra (:github-user:`irvan-putra`),
       Jeff Jacobson (:github-user:`jwjacobson`)
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
     - Alireza Shabani (:github-user:`revisto`)
     - :github:`GitHub <revisto/python-docs-fa>`
   * - `Polish (pl) <https://docs.python.org/pl/>`__
     - Maciej Olko (:github-user:`m-aciek`)
     - :github:`GitHub <python/python-docs-pl>`,
       `Transifex <tx_>`_,
       `original mail <https://mail.python.org/pipermail/doc-sig/2019-April/004106.html>`__
   * - Portuguese (pt)
     - Gustavo Toffo
     -
   * - `Brazilian Portuguese (pt-br) <https://docs.python.org/pt-br/>`__
     - Rafael Fontenelle (:github-user:`rffontenelle`),
       Marco Rougeth (:github-user:`rougeth`)
     - :github:`GitHub <python/python-docs-pt-br>`,
       `wiki <https://python.org.br/traducao/>`__,
       `Telegram <https://t.me/pybr_i18n>`__,
       `article <https://rgth.co/blog/python-ptbr-cenario-atual/>`__
   * - Romanian (ro)
     - Octavian Mustafa (:github-user:`octaG-M`, `email <mailto:octawian@yahoo.com>`__)
     - :github:`GitHub <octaG-M/python-docs-ro>`
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


How should I translate code examples?
-------------------------------------

Translate values in code examples (i.e. string literals) and comments.
Don't translate keywords or names,
including variable, function, class, argument, and attribute names.

.. _translation_wg: https://wiki.python.org/psf/TranslationWG/Charter
.. _translation_ml: https://mail.python.org/mailman3/lists/translation.python.org/
