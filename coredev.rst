.. _coredev:

How to Become a Core Developer
==============================

What it Takes
-------------

When you have consistently contributed patches which have met quality standards
to be committed without requiring extensive rewrites, you may qualify for
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

XXX list of people


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

It is expected that on the issue tracker you have a username in the form of
"first_name.last_name". If your initial issue tracker username is not of this
form, please change it. This is so that it is easier to assign issues to the
right person.


SSH
'''

You need to generate an SSH 2 RSA key to be able to commit code. You may have
multiple keys if you wish (e.g., for work and home). Send your key as an
attachment in an email to python-committers (do not paste it in the email as
SSH keys have specific formatting requirements).

Your SSH key will be set to a username in the form of "first_name.last_name".
This should match your username on the issue tracker.

You can verify your commit access by looking at
http://www.python.org/dev/committers which lists all core developers by
username. You can also execute the follow command and look for the word
"success" in the output::

    ssh pythondev@svn.python.org

For Windows users using Pageant::

    c:\path\to\putty\plink.exe pythondev@svn.python.org

An entry in the ``Misc/Developers.txt`` file should also be entered for you.
Typically the person who sponsored your application to become a core developer
makes sure an entry is created for you.


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



Read-write Checkout
'''''''''''''''''''

XXX




Responsibilities
----------------

XXX
