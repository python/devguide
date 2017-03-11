.. _patch:

Lifecycle of a Pull Request
===========================


Creating
--------

CPython uses a workflow based on pull requests. What this means is
that you create a branch in Git, make your changes, push those changes
to GitHub, and than create a pull request.
`GitHub's help pages <https://help.github.com/>`_ are good and there
are tons of pages out there for help with Git.  As such, this
document does not go into any great detail as the assumption is there
is a resource out there which will explain things in a way that makes
sense for you personally when it comes to general Git and GitHub
details.


Tool Setup
''''''''''

.. _workflow:

If you have not already done so, you will want to fork the
`CPython repository`_. You can read GitHub's documentation on how to
`fork a repository <https://help.github.com/articles/fork-a-repo/>`_
if you are not already familiar with how to do this. This will make
sure that you have a clone of your fork of CPython on your computer
and the appropriate remote repositories.

You will then want to create a branch to contain your work. GitHub has
instructions on how to
`create a branch <https://help.github.com/articles/creating-and-deleting-branches-within-your-repository/>`_
within your fork through their website.


.. _CPython repository: https://github.com/python/cpython


Preparation
'''''''''''

When creating a patch for submission, there are several things that you should
do to help ensure that your patch is accepted.

First, make sure to follow Python's style guidelines. For Python code you
should follow :PEP:`8`, and for C code you should follow :PEP:`7`. If you have
one or two discrepancies those can be fixed by the core developer who commits
your patch. But if you have systematic deviations from the style guides your
patch will be put on hold until you fix the formatting issues.

Second, be aware of backwards-compatibility considerations. While the core
developer who eventually handles your patch will make the final call on whether
something is acceptable, thinking about backwards-compatibility early
will help prevent having your patch rejected on these grounds. Put yourself in
the shoes of someone whose code will be broken by the change(s) introduced by
the patch. It is quite likely that any change made will break
someone's code, so you need to have a good reason to make a change as you will
be forcing someone to update their code. (This obviously does not apply to new
classes or functions; new arguments should be optional and have default values
which maintain the existing behavior.) If in doubt, have a look at
:PEP:`387` or :ref:`discuss <communication>` the issue with experienced
developers.

Third, make sure you have proper tests to verify your patch works as expected.
Patches will not be accepted without the proper tests!

Fourth, make sure the entire test suite :ref:`runs <runtests>` **without
failure** because of your changes.  It is not sufficient to only run whichever
test seems impacted by your changes, because there might be interferences
unknown to you between your changes and some other part of the interpreter.

Fifth, proper :ref:`documentation <documenting>`
additions/changes should be included.


.. _patch-generation:

Generation
''''''''''

To perform a quick sanity check on your patch, you can run::

   make patchcheck

This will check and/or fix various common things people forget to do for
patches, such as adding any new files needed for the patch to work (note
that not all checks apply to non-core developers).  On Windows, use this
command (after any successful build of Python)::

   python.bat Tools/scripts/patchcheck.py


.. _pullrequest-quickguide:

Quick Guide
'''''''''''

`Clear communication`_ is key to contributing to any project, especially an
`Open Source`_ project like Python.

Here is a quick overview of you can contribute to CPython on GitHub:

1.  If an Issue doesn't exist, `create an Issue`_ that describes your change

2.  Prepare your system by :ref:`setup`

3.  Fork `CPython`_ on GitHub (using the Fork button in the upper-right on GitHub)

4.  Start :ref:`compiling` to build Python

5.  Begin :ref:`runtests` after you have built Python

6.  Set your Git :ref:`remote-configuration` to add an "upstream" remote (using SSH, or you can `use HTTPS`_)

7.  Create :ref:`committing-active-branches` in Git where you can work on changes

8.  Continue :ref:`runtests`

9. Prepare for :ref:`committing-push-changes` to your GitHub repo

10. `Create Pull Request`_ for your changes to be reviewed then merged into `CPython`_

11. Review and address `comments on your Pull Request`_

12. When your changes are merged, celebrate contributing to Python! :)

.. _Clear communication: https://opensource.guide/how-to-contribute/#how-to-submit-a-contribution
.. _Open Source: https://opensource.guide/
.. _create an Issue: https://bugs.python.org/
.. _CPython: https://github.com/python/cpython
.. _use HTTPS: https://help.github.com/articles/which-remote-url-should-i-use/
.. _Create Pull Request: https://help.github.com/articles/creating-a-pull-request/
.. _comments on your Pull Request: https://help.github.com/articles/commenting-on-a-pull-request/


.. _pullrequest-steps:

Quick Guide Step-by-step
''''''''''''''''''''''''

Set up your system (using SSH, or you can `use HTTPS`_)::

  git clone git@github.com:YOUR_GITHUB_ID/cpython.git

Replace **YOUR_GITHUB_ID** with your GitHub account name above, then add upstream (using SSH, or you can `use HTTPS`_)::

  git remote add upstream git://github.com/python/cpython.git

Work on new features or fixes::

  git checkout -b MY_BRANCH_NAME upstream/master
  
As you work, commit changes::

  git commit

Then fetch upstream to see if anything conflicts with your changes::

  git fetch upstream
  
Then push your work to your clone on GitHub::

  git push origin MY_BRANCH_NAME

Make a Pull Request on GitHub from your changes in **MY_BRANCH_NAME**.

.. note::
   You can upload a patch to https://bugs.python.org/, but Pull Requests 
   on GitHub are preferred.


Licensing
---------

For non-trivial changes, we must have your formal approval for distributing
your work under the `PSF license`_.  Therefore, you need to fill out a
`contributor form`_ which allows the `Python Software Foundation`_ to
license your code for use with Python (you retain the copyright).

.. note::
   You only have to sign this document once, it will then apply to all
   your further contributions to Python.

You will also need to specify you GitHub username on the
`issue tracker`_ on the *Your Details* link found on the
homepage.


.. _PSF license: http://docs.python.org/dev/license.html#terms-and-conditions-for-accessing-or-otherwise-using-python
.. _contributor form: http://www.python.org/psf/contrib/
.. _Python Software Foundation: http://www.python.org/psf/


Submitting
----------

Once you are satisfied with your work you will want to commit your
changes to your branch. In general you can run ``git commit -a`` and
that will commit everything. You can always run ``git status`` to see
what changes are outstanding.

When all of your changes are committed (i.e. ``git status`` doesn't
list anything), you will want to push your branch to your fork::

  git push origin <branch name>

This will get your changes up to GitHub.

Now you want to
`create a pull request from your fork <https://help.github.com/articles/creating-a-pull-request-from-a-fork/>`_.
If this is pull request in response to a pre-existing issue on the
`issue tracker`_, please make sure to reference the issue number in
your pull request message.

If this is a patch for an unreported issue (assuming you already performed a
search on the issue tracker for a pre-existing issue), create a new issue and
reference it in the pull request. Please fill in as much relevant detail
as possible to prevent patch reviewers from having to delay reviewing your
patch because of lack of information.


.. _issue tracker: http://bugs.python.org


Reviewing
---------

To begin with, please be patient! There are many more people
submitting pull requests than there are people capable of reviewing
your pull request. Getting your pull request reviewed requires a
reviewer to have the spare time and motivation to look at your pull
request (we cannot force anyone to review pull requests and no one is
employed to look at pull requests). If your pull request has not
received any notice from reviewers (i.e., no comment made) after one
month, first "ping" the issue on the `issue tracker`_ to remind the
nosy list that the patch needs a review.  If you don't get a response
within a week after pinging the issue, then you can try emailing
python-dev@python.org to ask for someone to review your patch.

When someone does manage to find the time to look at your pull request
they will most likely make comments about how it can be improved
(don't worry, even core developers of Python have their patches sent
back to them for changes).  It is then expected that you update your
pull request to address these comments, and the review process will
thus iterate until a satisfactory solution has emerged.

How to Review a Pull Request
''''''''''''''''''''''''''''

One of the bottlenecks in the Python development
process is the lack of code reviews.
If you browse the bug tracker, you will see that numerous issues
have a fix, but cannot be commited to the main source code repository,
because no one has reviewed the proposed solution.
Reviewing a pull request can be just as informative as providing a
pull request and it will allow you to give constructive comments on
another developer's work. This guide provides a checklist for
submitting a code review. It is a common misconception that in order
to be useful, a code review has to be perfect. This is not the case at
all! It is helpful to just test the patch and/or play around with the
code and leave comments in the pull request or issue tracker.

1. If you have not already done so, get a copy of the CPython repository
   by following the :ref:`setup guide <setup>`, build it and run the tests.

2. Check the bug tracker to see what steps are necessary to reproduce
   the issue and confirm that you can reproduce the issue in your version
   of the Python REPL (the interactive shell prompt), which you can launch
   by executing ./python inside the repository.

3. Apply the pull request (GitHub has instructions with each pull
   request on how to do this).

4. If the patch affects any C file, run the build again.

5. Launch the Python REPL (the interactive shell prompt) and check if
   you can reproduce the issue. Now that the patch has been applied, the issue
   should be fixed (in theory, but mistakes do happen! A good review aims to
   catch these before the code is committed to the Python repository). You should
   also try to see if there are any corner cases in this or related issue that the author
   of the fix may have missed.

6. If you have time, run the entire test suite. If you are pressed for time,
   run the tests for the module(s) where changes were applied.
   However, please be aware that if you are recommending a patch as 'commit-ready',
   you should always make sure the entire test suite passes.


Committing/Rejecting
--------------------

Once your patch has reached an acceptable state (and thus considered
"accepted"), it will either be committed or rejected. If it is rejected, please
do not take it personally! Your work is still appreciated regardless of whether
your patch is committed. Balancing what *does* and *does not* go into Python
is tricky and we simply cannot accept everyone's contributions.

But if your pull request is committed it will then go into Python's
:abbr:`VCS (version control system)` to be released
with the next major release of Python. It may also be backported to older
versions of Python as a bugfix if the core developer doing the commit believes
it is warranted.


Crediting
---------

Non-trivial contributions are credited in the ``Misc/ACKS`` file (and, most
often, in a contribution's ``Misc/NEWS`` entry as well).  You may be
asked to make these edits on the behalf of the core developer you
accepts your pull request.
