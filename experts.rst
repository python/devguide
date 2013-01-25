.. _experts:

Experts Index
=================

This document has tables that list Python Modules, Tools, Platforms and
Interest Areas and names for each item that indicate a maintainer or an
expert in the field.  This list is intended to be used by issue submitters,
issue triage people, and other issue participants to find people to add to
the nosy list or to contact directly by email for help and decisions on
feature requests and bug fixes.  People on this list may be asked to render
final judgement on a feature or bug.  If no active maintainer is listed for
a given module, then questionable changes should go to python-dev, while
any other issues can and should be decided by any committer.

Unless a name is followed by a '*', you should never assign an issue to
that person, only make them nosy.  Names followed by a '*' may be assigned
issues involving the module or topic.

.. TODO document automatic assignment/nosy: people need not add them manually

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

See also :PEP:`291` and :PEP:`360` for information about certain modules
with special rules.


Stdlib
------
====================  =============================================
Module                Maintainers
====================  =============================================
__future__
__main__              gvanrossum, ncoghlan
_dummy_thread         brett.cannon
_thread               pitrou
abc
aifc                  r.david.murray
argparse              bethard
array
ast                   benjamin.peterson
asynchat              josiahcarlson, giampaolo.rodola, stutzbach
asyncore              josiahcarlson, giampaolo.rodola, stutzbach
atexit
audioop
base64
bdb
binascii
binhex
bisect                rhettinger
builtins
bz2                   nadeem.vawda
calendar              rhettinger
cgi
cgitb
chunk
cmath                 mark.dickinson
cmd
code
codecs                lemburg, doerwalter
codeop
collections           rhettinger
collections.abc       rhettinger, stutzbach
colorsys
compileall
concurrent.futures    bquinlan
configparser          lukasz.langa*
contextlib            ncoghlan
copy                  alexandre.vassalotti
copyreg               alexandre.vassalotti
cProfile
crypt                 jafo*
csv                   skip.montanaro (inactive)
ctypes                theller (inactive), belopolsky, amaury.forgeotdarc,
                      meador.inge
curses
datetime              belopolsky
dbm
decimal               facundobatista, rhettinger, mark.dickinson
difflib               tim_one (inactive)
dis                   ncoghlan
distutils             tarek*, eric.araujo*
doctest               tim_one (inactive)
dummy_threading       brett.cannon
email                 barry, r.david.murray*
encodings             lemburg, loewis
errno
exceptions
fcntl
filecmp
fileinput
fnmatch
formatter
fpectl
fractions             mark.dickinson, rhettinger
ftplib                giampaolo.rodola
functools             ncoghlan, rhettinger
gc                    pitrou
getopt
getpass
gettext               loewis
glob
grp
gzip
hashlib
heapq                 rhettinger, stutzbach
hmac
html                  ezio.melotti
http
idlelib               kbk
imaplib
imghdr
imp
importlib             brett.cannon
inspect
io                    pitrou, benjamin.peterson, stutzbach
ipaddress             pmoody, ncoghlan
itertools             rhettinger
json                  bob.ippolito (inactive), ezio.melotti, rhettinger, pitrou
keyword
lib2to3               benjamin.peterson
linecache
locale                loewis, lemburg
logging               vinay.sajip
lzma                  nadeem.vawda
macpath
mailbox               petri.lehtinen
mailcap
marshal
math                  mark.dickinson, rhettinger, stutzbach
mimetypes
mmap
modulefinder          theller (inactive), jvr
msilib                loewis
msvcrt
multiprocessing       jnoller, sbt*
netrc
nis
nntplib               pitrou
numbers
operator
optparse              aronacher
os                    loewis
ossaudiodev
packaging             tarek*, eric.araujo*, alexis
parser                benjamin.peterson
pdb                   georg.brandl*
pickle                alexandre.vassalotti, pitrou
pickletools           alexandre.vassalotti
pipes
pkgutil
platform              lemburg
plistlib
poplib                giampaolo.rodola
posix
pprint                fdrake
profile               georg.brandl
pstats                georg.brandl
pty
pwd
py_compile
pybench               lemburg, pitrou
pyclbr
pydoc
queue                 rhettinger
quopri
random                rhettinger
re                    effbot (inactive), pitrou, ezio.melotti
readline
reprlib
resource
rlcompleter
runpy                 ncoghlan
sched                 giampaolo.rodola
select
shelve
shlex
shutil                tarek, hynek
signal
site
smtpd                 giampaolo.rodola
smtplib
sndhdr
socket                pitrou
socketserver
spwd
sqlite3               ghaering
ssl                   janssen, pitrou, giampaolo.rodola
stat
string                georg.brandl*
stringprep
struct                mark.dickinson, meador.inge
subprocess            astrand (inactive)
sunau
symbol
symtable              benjamin.peterson
sys
sysconfig             tarek
syslog                jafo*
tabnanny              tim_one (inactive)
tarfile               lars.gustaebel
telnetlib
tempfile              georg.brandl, ncoghlan
termios
test                  ezio.melotti
textwrap              georg.brandl
threading             pitrou
time                  belopolsky
timeit                georg.brandl
tkinter               gpolo
token                 georg.brandl
tokenize              meador.inge
trace                 belopolsky
traceback             georg.brandl*
tty
turtle                gregorlingl
types
unicodedata           loewis, lemburg, ezio.melotti
unittest              michael.foord*, ezio.melotti
unittest.mock         michael.foord*
urllib                orsenthil
uu
uuid
warnings
wave
weakref               fdrake, pitrou
webbrowser            georg.brandl
winreg                brian.curtin*, stutzbach
winsound              effbot (inactive)
wsgiref               pje
xdrlib
xml.dom
xml.dom.minidom
xml.dom.pulldom
xml.etree             effbot (inactive), eli.bendersky
xml.parsers.expat
xml.sax
xml.sax.handler
xml.sax.saxutils
xml.sax.xmlreader
xmlrpc                loewis
zipfile               alanmcintyre
zipimport
zlib                  nadeem.vawda
====================  =============================================


Tools
-----
==================  ===========
Tool                Maintainers
==================  ===========
pybench             lemburg
==================  ===========


Platforms
---------
===================   ===========
Platform              Maintainers
===================   ===========
AIX
Cygwin                jlt63, stutzbach
FreeBSD
HP-UX
Linux
Mac OS X              ronaldoussoren, ned.deily, hynek
NetBSD1
OS2/EMX               aimacintyre
Solaris/OpenIndiana   jcea
Windows               tim.golden, brian.curtin
===================   ===========


Miscellaneous
-------------
==================  ===========
Interest Area       Maintainers
==================  ===========
algorithms
ast/compiler        ncoghlan, benjamin.peterson, brett.cannon, georg.brandl
autoconf/makefiles
bsd
bug tracker         ezio.melotti
buildbots           pitrou
bytecode            pitrou, georg.brandl
context managers    ncoghlan
coverity scan       christian.heimes, brett.cannon
data formats        mark.dickinson, georg.brandl
database            lemburg
devguide            ncoghlan, eric.araujo, ezio.melotti
documentation       georg.brandl, ezio.melotti, eric.araujo
GUI
i18n                lemburg, eric.araujo
import machinery    brett.cannon, ncoghlan
io                  pitrou, benjamin.peterson, stutzbach, hynek
locale              lemburg, loewis
mathematics         mark.dickinson, eric.smith, lemburg, stutzbach
memory management   tim_one, lemburg
networking          giampaolo.rodola, pitrou
packaging           tarek, lemburg, alexis, eric.araujo
py3 transition      benjamin.peterson
release management  tarek, lemburg, benjamin.peterson, barry, loewis,
                    gvanrossum, anthonybaxter, eric.araujo, ned.deily,
                    georg.brandl
str.format          eric.smith
testing             michael.foord, pitrou, ezio.melotti
test coverage       ncoghlan, giampaolo.rodola
threads             pitrou
time and dates      lemburg, belopolsky
unicode             lemburg, ezio.melotti, haypo, benjamin.peterson, pitrou
version control     eric.araujo, georg.brandl, ezio.melotti
==================  ===========
