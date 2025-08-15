.. _experts:

=============
Experts index
=============

This document has tables that list Python Modules, Tools, Platforms and
Interest Areas and GitHub names for each item that indicate a maintainer or
an expert in the field.  This list is intended to be used by issue submitters,
issue triage people, and other issue participants to find people to @mention
or add as reviewers to issues and pull requests.  People on this list may be
asked to render final judgment on a feature or bug.  If no active maintainer
is listed for a given module, then questionable changes should be discussed
on the `Core Development Discourse category
<https://discuss.python.org/c/core-dev/23>`__,
while any other issues can and should be decided by any committer.

Developers can choose to follow labels, so if a label that they are
following is added to an issue or pull request, they will be notified
automatically.  The :cpy-file:`.github/CODEOWNERS` file is also used to indicate
maintainers that will be automatically added as reviewers to pull requests.

Unless a name is followed by a '*', you should never assign an issue to
that person.  Names followed by a '*' may be assigned issues involving the
module or topic.

The Platform and Interest Area tables list broader fields in which various
people have expertise.  These people can also be contacted for help,
opinions, and decisions when issues involve their areas.

If a listed maintainer does not respond to requests for comment for an
extended period (three weeks or more), they should be marked as inactive
in this list by placing the word 'inactive' in parenthesis behind their
tracker id.  They are of course free to remove that inactive mark at
any time.

Committers should update these tables as their areas of expertise widen.
New topics may be added to the Interest Area table at will.

The existence of this list is not meant to indicate that these people
*must* be contacted for decisions; it is, rather, a resource to be used
by non-committers to find responsible parties, and by committers who do
not feel qualified to make a decision in a particular context.


Stdlib
======

====================  =============================================
Module                Maintainers
====================  =============================================
__future__
__main__              gvanrossum, ncoghlan
_thread
abc
annotationlib         JelleZijlstra*
argparse              savannahostrowski*, serhiy-storchaka*
array
ast                   benjaminp, pablogsal, isidentical, JelleZijlstra, eclips4
asyncio               1st1, asvetlov, gvanrossum, graingert, kumaraditya303, willingc
atexit
base64
bdb
binascii
bisect                rhettinger*
builtins
calendar
cmath
cmd
code
codecs                malemburg
codeop
collections           rhettinger*
collections.abc       rhettinger*
colorsys
compileall            carljm
compression.bz2
compression.gzip
compression.lzma
compression.zlib      Yhg1s, gpshead*, emmatyping
compression.zstd      emmatyping*
concurrent.futures    pitrou, gpshead*
configparser          ambv*
contextlib            ncoghlan, 1st1
contextvars
copy                  serhiy-storchaka*
copyreg               serhiy-storchaka*
cProfile
csv                   serhiy-storchaka*
ctypes
curses                Yhg1s
dataclasses           ericvsmith*, carljm
datetime              pganssle
dbm
decimal               facundobatista, rhettinger
difflib
dis                   1st1
doctest
email                 warsaw, bitdancer*
encodings             malemburg
ensurepip             ncoghlan, dstufft, pradyunsg, pfmoore
enum                  warsaw, ethanfurman*
errno                 Yhg1s
faulthandler          vstinner, gpshead, ZeroIntensity*
fcntl                 Yhg1s
filecmp
fileinput
fnmatch               serhiy-storchaka*
fractions
ftplib
functools             rhettinger*
gc                    pitrou, pablogsal, nascheme
getopt                serhiy-storchaka*
getpath               FFY00
getpass
gettext               tomasr8
glob                  serhiy-storchaka*
grp
hashlib               tiran, gpshead*, picnixz
heapq                 rhettinger*
hmac                  tiran, gpshead*, picnixz
html                  ezio-melotti*
http
idlelib               terryjreedy*, taleinat
imaplib
importlib             brettcannon
inspect               1st1
io                    benjaminp
ipaddress
itertools             rhettinger*
json                  ezio-melotti, rhettinger, serhiy-storchaka*
keyword
libmpdec
linecache
locale                malemburg
logging               vsajip
mailbox
marshal
math                  rhettinger
mimetypes
mmap                  Yhg1s
modulefinder
msvcrt
multiprocessing       pitrou, gpshead*
netrc
numbers
operator
optparse              serhiy-storchaka*
os
os.path               serhiy-storchaka*
parser                pablogsal
pathlib               barneygale*
pdb                   gaogaotiantian
pickle                serhiy-storchaka*
pickletools           serhiy-storchaka*
pkgutil
platform              malemburg
plistlib
poplib
posix                 larryhastings, gpshead
pprint
profile
pstats
pty                   Yhg1s*
pwd
py_compile            carljm
pyclbr                isidentical
pydoc                 AA-Turner, serhiy-storchaka*
queue                 rhettinger*
quopri
random                rhettinger
re                    ezio-melotti, serhiy-storchaka*
readline              Yhg1s
reprlib
resource              Yhg1s
rlcompleter
runpy                 ncoghlan
sched
secrets
select
selectors
shelve
shlex
shutil
signal                gpshead
site
smtplib
socket                gpshead
socketserver
sqlite3               erlend-aasland*
ssl                   tiran, dstufft, alex
stat                  tiran
statistics            rhettinger
string
stringprep
struct
subprocess            gpshead*
symtable              benjaminp
sys
sysconfig             FFY00
syslog
tabnanny
tarfile
tempfile              serhiy-storchaka*
termios               Yhg1s
test                  ezio-melotti, serhiy-storchaka*
textwrap
threading             pitrou, gpshead
time                  pganssle
timeit
tkinter               serhiy-storchaka*
token
tokenize
tomllib               hauntsaninja*
trace
traceback             iritkatriel
tracemalloc           vstinner
tty                   Yhg1s*
turtle                willingc
turtledemo            terryjreedy*
types                 1st1
typing                gvanrossum, JelleZijlstra*, AlexWaygood*, carljm, sobolevn*
unicodedata           malemburg, ezio-melotti
unittest              ezio-melotti, gpshead, serhiy-storchaka*
unittest.mock
urllib                orsenthil
uuid
venv                  vsajip, FFY00
warnings
wave
weakref               nascheme
webbrowser
winreg
winsound
wsgiref
xml.dom
xml.dom.minidom
xml.dom.pulldom
xml.etree             scoder
xml.parsers.expat
xml.sax
xml.sax.handler
xml.sax.saxutils
xml.sax.xmlreader
xmlrpc
zipapp                pfmoore
zipfile               serhiy-storchaka, Yhg1s, gpshead
zipimport             Yhg1s*
====================  =============================================


Tools
=====

==================  ===========
Tool                Maintainers
==================  ===========
Argument Clinic     larryhastings, AlexWaygood*, erlend-aasland,
                    serhiy-storchaka*
Deepfreeze          gvanrossum, kumaraditya303
PEG Generator       gvanrossum, pablogsal, lysnikolaou
==================  ===========


.. _platform-experts:

Platforms
=========

For official contacts for supported platforms, see :pep:`11`.

Platforms listed here are not necessarily supported by CPython.
Some of the experts listed here maintain and distribute Python
for “their” platform as a third-party project.

===================   ===========
Platform              Maintainers
===================   ===========
AIX                   edelsohn, ayappanec
Android               mhsmith
Emscripten            hoodmane, pmp-p, rdb, rth, ryanking13
iOS                   freakboy3742, ned-deily
Linux
macOS                 ronaldoussoren, ned-deily, freakboy3742
NetBSD1
Solaris/OpenIndiana   jcea, kulikjak
Windows               tjguk, zooba, pfmoore
===================   ===========


Miscellaneous
=============

==================  ==========================================================
Interest Area       Maintainers
==================  ==========================================================
algorithms          rhettinger*, serhiy-storchaka
argument clinic     larryhastings, AlexWaygood*, erlend-aasland,
                    serhiy-storchaka*
AST/compiler        benjaminp, 1st1, pablogsal, markshannon, isidentical, brandtbucher, carljm, iritkatriel
autoconf/makefiles  Yhg1s*, emmatyping
issue tracker       ezio-melotti
buildbots           zware, pablogsal
bytecode            benjaminp, 1st1, markshannon, brandtbucher, carljm, iritkatriel
context managers    ncoghlan
core workflow       Mariatta, ezio-melotti, hugovk, AA-Turner
cryptography        gpshead, dstufft, picnixz
data formats
database            malemburg
devguide            merwok, ezio-melotti, willingc, Mariatta, hugovk,
                    AA-Turner
documentation       ezio-melotti, merwok, JulienPalard, willingc, hugovk,
                    AA-Turner, AlexWaygood*
emoji               Mariatta
extension modules   encukou, ncoghlan
filesystem
frozen modules      ericsnowcurrently, gvanrossum, kumaraditya303
f-strings           ericvsmith*
GUI
i18n                malemburg, merwok, tomasr8
import machinery    brettcannon, ncoghlan, ericsnowcurrently, FFY00
initialization      FFY00
io                  benjaminp, gpshead
JIT                 brandtbucher*, savannahostrowski*
locale              malemburg
mathematics         malemburg, rhettinger, serhiy-storchaka
memory management   tim-one, malemburg, Yhg1s, nascheme
memoryview
networking          gpshead
object model        benjaminp, Yhg1s
packaging           malemburg, merwok, dstufft, pfmoore, emmatyping
pattern matching    brandtbucher*
PEG parser          gvanrossum, pablogsal, lysnikolaou
performance         vstinner, serhiy-storchaka*, 1st1, rhettinger, markshannon,
                    brandtbucher, carljm, Fidget-Spinner, AlexWaygood*, nascheme
pip                 ncoghlan, dstufft, pfmoore, pradyunsg
release management  malemburg, benjaminp, warsaw,
                    gvanrossum, merwok, ned-deily,
                    JulienPalard, hugovk
runtime lifecycle   ericsnowcurrently, kumaraditya303, zooba, ZeroIntensity, nascheme
str.format          ericvsmith*
subinterpreters     ericsnowcurrently, kumaraditya303, ZeroIntensity*
symbol table        JelleZijlstra, carljm
testing             ezio-melotti
test coverage
threads             gpshead
time and dates      malemburg, pganssle
Unicode             malemburg, ezio-melotti, benjaminp
version control     merwok, ezio-melotti
==================  ==========================================================


Experts Emeritus
================

Names followed by a '^' indicate old bugs.python.org usernames, for people
that did not transition to GitHub.

Stdlib
------

.. list-table::

   * - Module
     - Expert

   * - codecs
     - doerwalter

   * - collections.abc
     - stutzbach^

   * - concurrent.futures
     - brianquinlan

   * - copy
     - avassalotti

   * - copyreg
     - avassalotti

   * - csv
     - smontanaro

   * - ctypes
     - theller, abalkin, amauryfa, meadori

   * - datetime
     - abalkin

   * - difflib
     - tim-one

   * - doctest
     - tim-one

   * - email
     - maxking

   * - enum
     - eliben

   * - ftplib
     - giampaolo

   * - heapq
     - stutzbach

   * - idlelib
     - kbkaiser, serwy

   * - io
     - stutzbach^

   * - ipaddress
     - pmoody^

   * - json
     - etrepum

   * - math
     - stutzbach^

   * - modulefinder
     - theller, jvr^

   * - multiprocessing
     - applio, jnoller^, sbt^

   * - optparse
     - mitsuhiko

   * - pickle
     - avassalotti

   * - pickletools
     - avassalotti

   * - pprint
     - freddrake

   * - selectors
     - neologix^, giampaolo

   * - shutil
     - tarekziade, giampaolo

   * - sqlite3
     - ghaering^

   * - ssl
     - jackjansen

   * - statistics
     - stevendaprano

   * - struct
     - meadori

   * - subprocess
     - astrand^, giampaolo

   * - syslog
     - jafo^

   * - tabnanny
     - tim-one

   * - tarfile
     - gustaebel

   * - time
     - abalkin

   * - tkinter
     - gpolo^

   * - tokenize
     - meadori

   * - trace
     - abalkin

   * - turtle
     - gregorlingl^

   * - unittest
     - rbtcollins

   * - weakref
     - freddrake

   * - winreg
     - stutzbach^

   * - wsgiref
     - pjenvey

   * - xml.etree
     - eliben

   * - zipfile
     - alanmcintyre^

Platforms
---------

.. list-table::

   * - Platform
     - Expert

   * - Cygwin
     - jlt63^, stutzbach^

   * - JVM/Java
     - frank.wierzbicki^

   * - OS2/EMX
     - aimacintyre^


Miscellaneous
-------------

.. list-table::

   * - Interest Area
     - Expert

   * - filesystem
     - giampaolo

   * - io
     - stutzbach^

   * - mathematics
     - stutzbach^

   * - networking
     - giampaolo

   * - packaging
     - tarekziade, alexis^

   * - pip
     - Marcus.Smith^

   * - release management
     - tarekziade, anthonybaxter^, birkenfeld

   * - time and dates
     - abalkin


Documentation translations
==========================

Translations are within the charter of
`Editorial Board <https://python.github.io/editorial-board/>`_.
For a list of translations and their coordinators, see
:ref:`this table of translations <translation-coordinators>`.
