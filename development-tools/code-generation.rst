.. _code-generation:

=====================
Code generation tools
=====================

CPython uses scripts to generate some source files from higher-level inputs.
When changing an input that has generated files, use the corresponding
``make`` target from the root of the checkout to update the generated output.

Frozen modules
==============

The ``Tools/build/freeze_modules.py`` script generates C sources for frozen
standard-library modules.  Run the ``regen-frozen`` target after changing a
module that is frozen::

    make regen-frozen

The build invokes ``Tools/build/deepfreeze.py`` to turn frozen bytecode into C
data.  It is normally run as part of the build process rather than as a manual
regeneration command.

Global objects
==============

The ``Tools/build/generate_global_objects.py`` script generates definitions for
global objects and strings.  The ``regen-global-objects`` target also runs
Argument Clinic first, then updates the generated global-object files::

    make regen-global-objects

See :ref:`clinic` for details about editing Argument Clinic input and
regenerating its output.  For parser changes, see the :ref:`parser guide
<grammar>`.

To run the set of regeneration targets listed by ``regen-all``::

    make regen-all

This may update generated files for tools beyond the ones described here.
Inspect the changes and include only generated files relevant to your change.

