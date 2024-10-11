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

Names followed by a '^' indicate old bugs.python.org usernames, for people
that did not transition to GitHub.

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
argparse
array
ast                   benjaminp, pablogsal, isidentical, JelleZijlstra, eclips4
asyncio               1st1, asvetlov, gvanrossum, graingert, kumaraditya303, willingc
atexit
base64
bdb
binascii
bisect                rhettinger*
builtins
bz2
calendar
cmath
cmd
code
codecs                malemburg, doerwalter
codeop
collections           rhettinger*
collections.abc       rhettinger*, stutzbach^
colorsys
compileall            carljm
concurrent.futures    pitrou, brianquinlan, gpshead*
configparser          ambv*
contextlib            ncoghlan, 1st1
contextvars
copy                  avassalotti
copyreg               avassalotti
cProfile
csv                   smontanaro (inactive)
ctypes                theller (inactive), abalkin, amauryfa, meadori
curses                Yhg1s
dataclasses           ericvsmith*, carljm
datetime              abalkin, pganssle
dbm
decimal               facundobatista, rhettinger
difflib               tim-one (inactive)
dis                   1st1
doctest               tim-one (inactive)
email                 warsaw, bitdancer*, maxking
encodings             malemburg
ensurepip             ncoghlan, dstufft, pradyunsg, pfmoore
enum                  eliben*, warsaw, ethanfurman*
errno                 Yhg1s
faulthandler          vstinner, gpshead
fcntl                 Yhg1s
filecmp
fileinput
fnmatch
fractions
ftplib                giampaolo*
functools             rhettinger*
gc                    pitrou, pablogsal
getopt
getpass
gettext
glob
grp
gzip
hashlib               tiran, gpshead*
heapq                 rhettinger*, stutzbach^
hmac                  tiran, gpshead*
html                  ezio-melotti*
http
idlelib               kbkaiser (inactive), terryjreedy*, serwy (inactive),
                      taleinat
imaplib
imghdr
importlib             brettcannon
inspect               1st1
io                    benjaminp, stutzbach^
ipaddress             pmoody^
itertools             rhettinger*
json                  etrepum (inactive), ezio-melotti, rhettinger
keyword
libmpdec
linecache
locale                malemburg
logging               vsajip
lzma
mailbox
marshal
math                  rhettinger, stutzbach^
mimetypes
mmap                  Yhg1s
modulefinder          theller (inactive), jvr^
msilib
msvcrt
multiprocessing       applio*, pitrou, jnoller^ (inactive), sbt^ (inactive), gpshead*
netrc
nis
nntplib
numbers
operator
optparse              mitsuhiko
os
os.path               serhiy-storchaka
ossaudiodev
parser                pablogsal
pathlib               barneygale*
pdb                   gaogaotiantian
pickle                avassalotti
pickletools           avassalotti
pipes
pkgutil
platform              malemburg
plistlib
poplib
posix                 larryhastings, gpshead
pprint                freddrake
profile
pstats
pty                   Yhg1s*
pwd
py_compile            carljm
pyclbr                isidentical
pydoc                 AA-Turner
queue                 rhettinger*
quopri
random                rhettinger
re                    ezio-melotti, serhiy-storchaka
readline              Yhg1s
reprlib
resource              Yhg1s
rlcompleter
runpy                 ncoghlan
sched
secrets
select
selectors             neologix^, giampaolo
shelve
shlex
shutil                tarekziade, giampaolo
signal                gpshead
site
smtplib
sndhdr
socket                gpshead
socketserver
spwd
sqlite3               ghaering^, erlend-aasland*
ssl                   jackjansen, tiran, dstufft, alex
stat                  tiran
statistics            stevendaprano, rhettinger
string
stringprep
struct                meadori
subprocess            astrand^ (inactive), giampaolo, gpshead*
symtable              benjaminp
sys
sysconfig             FFY00
syslog                jafo^*
tabnanny              tim-one (inactive)
tarfile               gustaebel
tempfile
termios               Yhg1s
test                  ezio-melotti
textwrap
threading             pitrou, gpshead
time                  abalkin, pganssle
timeit
tkinter               gpolo^, serhiy-storchaka
token
tokenize              meadori
tomllib               hauntsaninja*
trace                 abalkin
traceback             iritkatriel
tracemalloc           vstinner
tty                   Yhg1s*
turtle                gregorlingl^, willingc
turtledemo            terryjreedy*
types                 1st1
typing                gvanrossum, JelleZijlstra*, AlexWaygood*, carljm, sobolevn*
unicodedata           malemburg, ezio-melotti
unittest              voidspace*, ezio-melotti, rbtcollins, gpshead
unittest.mock         voidspace*
urllib                orsenthil
uu
uuid
venv                  vsajip
warnings
wave
weakref               freddrake
webbrowser
winreg                stutzbach^
winsound
wsgiref               pjenvey
xdrlib
xml.dom
xml.dom.minidom
xml.dom.pulldom
xml.etree             eliben*, scoder
xml.parsers.expat
xml.sax
xml.sax.handler
xml.sax.saxutils
xml.sax.xmlreader
xmlrpc
zipapp                pfmoore
zipfile               alanmcintyre^, serhiy-storchaka, Yhg1s, gpshead
zipimport             Yhg1s*
zlib                  Yhg1s, gpshead*
====================  =============================================


Tools
=====

==================  ===========
Tool                Maintainers
==================  ===========
Argument Clinic     larryhastings, AlexWaygood*, erlend-aasland
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
Cygwin                jlt63^, stutzbach^
Emscripten            hoodmane, pmp-p, rdb, rth, ryanking13
FreeBSD
HP-UX
iOS                   freakboy3742, ned-deily
Linux
macOS                 ronaldoussoren, ned-deily, freakboy3742
NetBSD1
OS2/EMX               aimacintyre^
Solaris/OpenIndiana   jcea
Windows               tjguk, zware, zooba, pfmoore
JVM/Java              frank.wierzbicki^
===================   ===========


Miscellaneous
=============

==================  ==========================================================
Interest Area       Maintainers
==================  ==========================================================
algorithms          rhettinger*
argument clinic     larryhastings, AlexWaygood*, erlend-aasland
ast/compiler        benjaminp, 1st1, pablogsal, markshannon, isidentical, brandtbucher, carljm, iritkatriel
autoconf/makefiles  Yhg1s*
bsd
issue tracker       ezio-melotti
buildbots           zware, pablogsal
bytecode            benjaminp, 1st1, markshannon, brandtbucher, carljm, iritkatriel
context managers    ncoghlan
core workflow       Mariatta, ezio-melotti, hugovk, AA-Turner
cryptography        gpshead, dstufft
data formats
database            malemburg
devguide            merwok, ezio-melotti, willingc, Mariatta, hugovk,
                    AA-Turner
documentation       ezio-melotti, merwok, JulienPalard, willingc, hugovk,
                    AA-Turner, AlexWaygood*
emoji               Mariatta
extension modules   encukou, ncoghlan
filesystem          giampaolo
frozen modules      ericsnowcurrently, gvanrossum, kumaraditya303
f-strings           ericvsmith*
GUI
i18n                malemburg, merwok
import machinery    brettcannon, ncoghlan, ericsnowcurrently
io                  benjaminp, stutzbach^, gpshead
JIT                 brandtbucher*
locale              malemburg
mathematics         malemburg, stutzbach^, rhettinger
memory management   tim-one, malemburg, Yhg1s
memoryview
networking          giampaolo, gpshead
object model        benjaminp, Yhg1s
packaging           tarekziade, malemburg, alexis^, merwok, dstufft, pfmoore
pattern matching    brandtbucher*
peg parser          gvanrossum, pablogsal, lysnikolaou
performance         vstinner, serhiy-storchaka, 1st1, rhettinger, markshannon, brandtbucher, carljm, Fidget-Spinner,
                    AlexWaygood*
pip                 ncoghlan, dstufft, pfmoore, Marcus.Smith^, pradyunsg
py3 transition      benjaminp
release management  tarekziade, malemburg, benjaminp, warsaw,
                    gvanrossum, anthonybaxter^, merwok, ned-deily,
                    birkenfeld, JulienPalard
runtime lifecycle   ericsnowcurrently, kumaraditya303, zooba
str.format          ericvsmith*
subinterpreters     ericsnowcurrently, kumaraditya303
symbol table        JelleZijlstra, carljm
testing             voidspace, ezio-melotti
test coverage
threads             gpshead
time and dates      malemburg, abalkin, pganssle
unicode             malemburg, ezio-melotti, benjaminp
version control     merwok, ezio-melotti
==================  ==========================================================


Documentation translations
==========================

For a list of translators, see :ref:`this table about translations <translating>`.
