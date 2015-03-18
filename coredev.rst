.. _coredev:

How to Become a Core Developer
==============================

What it Takes
-------------

When you have consistently contributed patches which meet quality standards
without requiring extensive rewrites prior to being committed,
you may qualify for
commit privileges and become a core developer of Python. You must also work
well with other core developers (and people in general) as you become an
ambassador for the Python project.

Typically a core developer will offer you the chance to gain commit privilege.
The person making the offer will become your mentor and watch your commits for
a while to make sure you understand the development process. If other core
developers agree that you should gain commit privileges you are then extended
an official offer.

You may request commit privileges yourself, but do not be surprised if your
request is turned down. Do not take this personally! It simply means that other
core developers think you need more time contributing patches before you are
able to commit them without supervision.

A complete list of core developer usernames can be found at
https://hg.python.org/committers.txt. :ref:`developers` lists when and why
someone received commit privileges.


Gaining Commit Privileges
-------------------------

When you have been extended an official offer to become a Python core
developer, there are several things you must do.

Mailing Lists
'''''''''''''

You are expected to subscribe to python-committers, python-dev,
python-checkins, and one of new-bugs-announce or python-bugs-list. See
:ref:`communication` for links to these mailing lists.


Issue Tracker
'''''''''''''

If you did not gain the Developer role in the `issue tracker`_ before gaining
commit privileges, please say so. This will allow issues to be assigned to you.
A tracker admin should also flip your "is committer" bit in the tracker's
account screen.

It is expected that on the issue tracker you have a username in the form of
"first_name.last_name". If your initial issue tracker username is not of this
form, please change it. This is so that it is easier to assign issues to the
right person.


SSH
'''

You need to provide an SSH-2 key to be able to commit code. You may have
multiple keys if you wish (e.g., for work and home). Using Ed25519 keys is
encouraged. Send your key as an attachment in an email to
hgaccounts@python.org. Help in generating an SSH key can be found in the
:ref:`faq`.

Your SSH key will be set to a username in the form of "first_name.last_name".
This should match your username on the issue tracker.

You can verify your commit access by looking at
https://hg.python.org/committers.txt which lists all core developers by
username.  If you want to practice, there is a `test repository
<https://hg.python.org/test/>`_ where you can freely commit and push any
changes you like::

   hg clone ssh://hg@hg.python.org/test/ hgtest

An entry in the :ref:`developers` should also be entered for you.
Typically the person who sponsored your application to become a core developer
makes sure an entry is created for you.


.. _contributor_agreement:

Sign a Contributor Agreement
''''''''''''''''''''''''''''

Submitting a `contributor form for Python`_ licenses any code you contribute to
the Python Software Foundation. While you retain the copyright, giving the PSF
the ability to license your code means it can be put under the PSF license so
it can be legally distributed with Python.

This is a very important step! Hopefully you have already submitted a
contributor agreement if you have been submitting patches. But if you have not
done this yet, it is best to do this ASAP, probably before you even do your
first commit so as to not forget.


.. _contributor form for Python: http://www.python.org/psf/contrib/



Read/Write Checkout
'''''''''''''''''''

With your commit privileges working and your contributor form submitted, you
can now get a read/write checkout of the code. URLs for read/write checkouts
are different than those for read-only checkouts as SSH is used instead of
HTTP.

You can clone the repository (which contains all active branches) with::

   hg clone ssh://hg@hg.python.org/cpython

The default branch in that repository is the current development branch.
You can of course switch your working copy to one of the maintenance branches,
for example::

   hg update 2.7


Responsibilities
----------------

As a core developer, there are certain things that are expected of you.

First and foremost, be a good person. This might sound melodramatic, but you
are now a member of the Python project and thus represent the project and your
fellow core developers whenever you discuss Python with anyone. We have a
reputation for being a very nice group of people and we would like to keep it
that way.

Second, please be prompt in responding to questions. We are all volunteers so
what little free time one can dedicate to Python should be spent being
productive. If you have been asked to respond to an issue or answer a question
and you put it off it ends up stalling other people's work. It is completely
acceptable to say you are too busy, but you need to say that instead of
stringing people along. This obviously applies to anything you do on the issue
tracker as well.

Third, please list what areas you want to be considered an expert in the
:ref:`experts`. This allows triagers to direct issues to you which involve
an area you are an expert in. But,
as stated in the second point above, if you do not have the time to answer
questions promptly then please remove yourself as needed from the file so that
you will not be bothered in the future. Once again, we all understand how life
gets in the way, so no one will be insulted if you remove yourself from the
list.

And finally, enjoy yourself! Contributing to open source software should be fun
(overall). If you find yourself no longer enjoying the work then either take a
break or figure out what you need to do to make it enjoyable again.
