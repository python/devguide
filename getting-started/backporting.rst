.. _backporting:
.. _branch-merge:

Backporting merged changes
==========================

After a pull request has been merged into ``main``, it may need to be backported
to one or more :ref:`maintenance <maintbranch>` or :ref:`security <secbranch>`
branches. The project's backport policy is described in the
:ref:`development cycle guide <maintbranch>`.

The :samp:`needs backport to {X.Y}` labels on a pull request indicate which
versions should receive a backport. ``miss-islington`` will automatically
attempt to create backport pull requests for the versions indicated by these
labels. If it cannot create a backport pull request because of conflicts, use
the :pypi:`cherry-picker` tool to create the backport and resolve the conflicts
manually.

You need the commit hash of the squashed commit that was merged into ``main``.
``miss-islington`` should post a comment when it is unable to create the
backport automatically, including the full command and commit hash. If that
comment is not posted, look for an event on the merged pull request similar to:

.. code-block:: text

   <core_developer> merged commit <commit_sha1> into python:main <sometime> ago.

By following the link to ``<commit_sha1>``, you can get the full commit hash.

Alternatively, you can obtain the commit hash with these Git commands::

   $ git fetch upstream
   $ git rev-parse ":/gh-<PR number>"

These commands print the hash of the commit whose message contains
``gh-<PR number>``.

Use the commit hash and the :pypi:`cherry-picker` tool to create the backport.
In the following command, ``<branch>`` is the target maintenance branch (for
example, ``3.12``):

.. code-block:: text

   $ cherry_picker <commit_sha1> <branch>

Follow the instructions provided. You may need to identify files with
conflicts, fix them, and build and run applicable tests. When you are finished,
stage all modified files and run ``cherry_picker --continue`` to push the
backport.

The tool usually generates the commit message automatically. If it does not,
keep the original commit message unchanged, except for removing the backport
pull request number (``(#XXXXX)``), and append a
``(cherry picked from commit <commit_sha1>)`` line.

The format of a correct backport commit message is:

.. code-block:: text
   :class: good

    [<branch>] gh-XXXXX: <original commit title> (GH-XXXXX)

    <original commit body>

    (cherry picked from commit <commit_sha1>)

Here ``gh-XXXXX`` is the GitHub *issue* number, and ``(GH-XXXXX)`` is the
original *pull request* number.

An example of a bad backport commit message:

.. code-block:: text
   :class: bad

    gh-XXXXX: Custom title (GH-XXXXX) (#XXXXX)

    * Custom message

When opening the backport pull request, its title must follow the same format
as the commit title, beginning with the ``[<branch>]`` prefix and referencing
the original pull request with a ``(GH-XXXXX)`` suffix. For example:

.. code-block:: text
   :class: good

    [3.15] gh-12345: Fix the spam module (GH-24680)

After the backport pull request is opened, ``miss-islington`` will link it to
the original pull request and remove the corresponding backport label.
