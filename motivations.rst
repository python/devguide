.. _motivations:

Core Developer Motivations and Affiliations
===========================================

CPython core developers participate in the core development process for a
variety of reasons. Being accepted as a core developer indicates that
an individual is interested in acquiring those responsibilities, has the
ability to collaborate effectively with existing core developers, and has had
the time available to demonstrate both that interest and that ability.

This page allows core developers that choose to do so to provide more
information to the rest of the Python community regarding their personal
situation (such as their general location and professional affiliations), as
well as any personal motivations that they consider particularly relevant.

Core developers that wish to provide this additional information add a new
entry to the :ref:`published-motivations` section below. Guidelines relating
to content and layout are included as comments in the source code for this page.

Core developers that are available for training, consulting, contract, or
full-time work, or are seeking crowdfunding support for their community
contributions, may also choose to provide that information here (including
linking out to commercial sites with the relevant details).

For more information on the origins and purpose of this page, see
:ref:`goals-of-the-motivations-page`.

.. _published-motivations:

Published entries
-----------------

The following core developers have chosen to provide additional details
regarding their professional affiliations and (optionally) other reasons for
participating in the CPython core development process:

.. Entry guidelines:

   We use the "topic" directive rather than normal section headings in order to
   avoid creating entries in the main table of contents.

   Topic headings should be in the form of "Name (Country)" or
   "Name (Continent)" to help give some indication as to the geographic
   distribution of core developers.

   NOTE: The rest of these guidelines are highly provisional - we can evolve
   them as people add entries, and we decide on the style we like. The
   current iteration is based on feedback that the first version (which
   *required* coming up with a personal bio) was a bit excessive.

   Minimal entries just include relevant professional affiliations, as follows:

   .. topic:: <name> (<country/continent>)

      * <company> (<role>)

   Longer entries should be written as short third person biographies, rather
   than being written in first person (See existing entries for examples).

   Entries should be maintained in alphabetical order by last name, or by
   name-as-written (relative to other last names) if "last name" isn't a
   meaningful term for your name.

   Include a "Personal site" bullet point with a link if you'd like to highlight
   a personal blog or other site.

   Include an "Extended bio" bullet point with a link if you'd like to provide
   more than a couple of paragraphs of biographical information. (Use a
   double-trailing underscore on these links to avoid "Duplicate explicit
   target name" warnings from Sphinx/docutils)

   Include an "Available for <activity>" (or activities) bullet point with a
   link if you'd like to be contacted for professional training, consulting or
   contract work, or other employment opportunities. A link to a page with
   additional details is preferred to a direct email address or contact phone
   number, as this is a global site, and folks may not be familiar with the
   relevant practical details that apply to this kind of work in a contributor's
   country of residence.

   Include a "Crowdfunding" bullet point with a link if you'd like to highlight
   crowdfunding services (e.g. Patreon) that folks can use to support your core
   development work.

   Include additional bullet points (without links) for any other affiliations
   you would like to mention.

   If there's a kind of link you'd like to include in your entry that isn't
   already covered by the categories mentioned above, please start a discussion
   about that on the python-committers mailing list.

   python-committers is also the appropriate point of contact for any other
   questions or suggestions relating to this page.

.. topic:: Brett Cannon (Canada)

   * Personal site: `snarky.ca <https://snarky.ca/>`_
   * `Extended bio <https://stackoverflow.com/cv/DrBrettCannon>`__
   * Microsoft (Software Developer)
   * Python Software Foundation (Fellow)

.. topic:: Nick Coghlan (Australia)

   * Personal site: `Curious Efficiency <http://www.curiousefficiency.org/>`_
   * `Extended bio <http://www.curiousefficiency.org/pages/about>`__
   * Red Hat (Software Engineer, Developer Experience)
   * Python Software Foundation (Fellow, Packaging Working Group)

   Nick originally began participating in CPython core development as an
   interesting and enlightening hobby activity while working for Boeing Defence
   Australia. After commencing work for Red Hat, he also became involved in a
   range of topics related directly to improving the experience of Python
   developers on the Fedora Linux distribution and derived platforms, and now
   works for Red Hat's Developer Experience team.

   In addition to his personal and professional interest in ensuring Python
   remains an excellent choice for Linux-based network service and system
   utility development, he is also interested in helping to ensure its
   continued suitability for educational and data analysis use cases.

.. topic:: Christian Heimes (Germany)

   * Red Hat (Software Developer, Security Engineering / Identity Management)
   * Python Software Foundation (Fellow)

.. topic:: R. David Murray (United States)

   * Personal site: `bitdance.com <http://www.bitdance.com>`_
   * Available for `Python and Internet Services Consulting
     and Python contract programming <http://www.murrayandwalker.com/>`_

   David has been involved in the Internet since the days when the old IBM
   BITNET and the ARPANet got cross connected, and in Python programming since
   he first discovered it around the days of Python 1.4.  After transitioning
   from being Director of Operations for dialup Internet providers (when that
   business started declining) to being a full time independent consultant,
   David started contributing directly to CPython development.  He became a
   committer in 2009.  He subsequently took over primary maintenance of the
   email package from Barry Warsaw, and contributed the unicode oriented API.
   David is also active in mentoring new contributors and, when time is
   available, working on the infrastructure that supports CPython development,
   specifically the Roundup-based bug tracker and the buildbot system.

   David currently does both proprietary and open source development work,
   primarily in Python, through the company in which he is a partner, `Murray &
   Walker, Inc <http://www.murrayandwalker.com>`_.  He has done contract work
   focused specifically on CPython development both through the PSF (the
   kickstart of the email unicode API development) and directly funded by
   interested corporations (additional development work on email funded by
   QNX, and work on CPython ICC support funded by Intel).  He would like to
   spend more of his (and his company's) time on open source work, and so is
   actively seeking additional such contract opportunities.

.. topic:: Victor Stinner (France)

   * `Personal website <https://haypo-notes.readthedocs.io/>`__
   * Red Hat (Senior Software Engineer)

   Victor is hacking the development version of CPython to make Python better
   than ever.

.. topic:: Kushal Das (India)

   * `Personal website <https://kushaldas.in>`__
   * Red Hat (Fedora Cloud Engineer)
   * Python Software Foundation (Fellow)


.. _goals-of-the-motivations-page:

Goals of this page
------------------

The `issue metrics`_ automatically collected by the CPython issue tracker
strongly suggest that the current core development process is bottlenecked on
core developer time - this is most clearly indicated in the first metrics graph,
which shows both the number of open issues and the number of patches awaiting
review growing steadily over time, despite CPython being one of the most
active open source projects in the world. This bottleneck then impacts not only
resolving open issues and applying submitted patches, but also the process of
identifying, nominating and mentoring new core developers.

The core commit statistics monitored by sites like `OpenHub`_ provide a good
record as to *who* is currently handling the bulk of the review and maintenance
work, but don't provide any indication as to the factors currently influencing
people's ability to spend time on reviewing proposed changes, or mentoring new
contributors.

This page aims to provide at least some of that missing data by encouraging
core developers to highlight professional affiliations in the following two
cases (even if not currently paid for time spent participating in the core
development process):

* developers working for vendors that distribute a commercially supported
  Python runtime
* developers working for Sponsor Members of the Python Software Foundation

These are cases where documenting our affiliations helps to improve the
overall transparency of the core development process, as well as making it
easier for staff at these organisations to locate colleagues that can help
them to participate in and contribute effectively to supporting the core
development process.

Core developers working for organisations with a vested interest in the
sustainability of the CPython core development process are also encouraged to
seek opportunities to spend work time on mentoring potential new core
developers, whether through the general `core mentorship program`_, through
mentoring colleagues, or through more targeted efforts like Outreachy's paid
`internships`_ and Google's `Summer of Code`_.

Core developers that are available for consulting or contract work on behalf of
the Python Software Foundation or other organisations are also encouraged
to provide that information here, as this will help the PSF to better
facilitate funding of core development work by organisations that don't
directly employ any core developers themselves.

Finally, some core developers seeking to increase the time they have available
to contribute to CPython may wish to pursue crowdfunding efforts that allow
their contributions to be funded directly by the community, rather than relying
on institutional sponsors allowing them to spend some or all of their work
time contributing to CPython development.

.. _issue metrics: https://bugs.python.org/issue?@template=stats
.. _OpenHub: https://www.openhub.net/p/python/contributors
.. _core mentorship program: https://www.python.org/dev/core-mentorship/
.. _internships: https://www.gnome.org/outreachy/
.. _Summer of Code: https://wiki.python.org/moin/SummerOfCode/2016


Limitations on scope
--------------------

* Specific technical areas of interest for core developers should be captured in
  the :ref:`Experts Index <experts>`.

* This specific listing is limited to CPython core developers (since it's
  focused on the specific constraint that is core developer time), but it
  would be possible to create a more expansive listing on the Python wiki that
  also covers issue triagers, and folks seeking to become core developers.

* Changes to the software and documentation maintained by core developers,
  together with related design discussions, all take place in public venues, and
  hence are inherently subject to full public review. Accordingly, core
  developers are NOT required to publish their motivations and affiliations if
  they do not choose to do so. This helps to ensure that core contribution
  processes remain open to anyone that is in a position to sign the `Contributor
  Licensing Agreement`_, the details of which are filed privately with the
  Python Software Foundation, rather than publicly.

.. _Contributor Licensing Agreement: https://www.python.org/psf/contrib/contrib-form/
