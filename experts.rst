.. _experts:

Experts Index
=============

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
_thread
_testbuffer           
abc
aifc                  r.david.murray
argparse              rhettinger*
array
ast                   benjamin.peterson, pablogsal
asynchat              josiahcarlson, giampaolo.rodola*, stutzbach
asyncio               yselivanov, asvetlov
asyncore              josiahcarlson, giampaolo.rodola*, stutzbach
atexit
audioop               serhiy.storchaka
base64
bdb
binascii
binhex
bisect                rhettinger*
builtins
bz2
calendar              rhettinger*
cgi                   ethan.furman*
cgitb                 ethan.furman*
chunk
cmath                 mark.dickinson
cmd
code
codecs                lemburg, doerwalter
codeop
collections           rhettinger*
collections.abc       rhettinger*, stutzbach
colorsys
compileall
concurrent.futures    pitrou, bquinlan
configparser          lukasz.langa*
contextlib            ncoghlan, yselivanov
contextvars
copy                  alexandre.vassalotti
copyreg               alexandre.vassalotti
cProfile
crypt                 jafo*
csv                   skip.montanaro (inactive)
ctypes                theller (inactive), belopolsky, amaury.forgeotdarc,
                      meador.inge
curses                twouters
dataclasses           eric.smith
datetime              belopolsky, p-ganssle
dbm
decimal               facundobatista, rhettinger, mark.dickinson
difflib               tim.peters (inactive)
dis                   yselivanov
distutils             eric.araujo, dstufft
doctest               tim.peters (inactive)
dummy_threading       brett.cannon
email                 barry, r.david.murray*, maxking
encodings             lemburg
ensurepip             ncoghlan, dstufft, pradyunsg
enum                  eli.bendersky*, barry, ethan.furman*
errno                 twouters
faulthandler          vstinner
fcntl                 twouters
filecmp
fileinput
fnmatch
formatter
fractions             mark.dickinson, rhettinger
ftplib                giampaolo.rodola*
functools             rhettinger*
gc                    pitrou, pablogsal
getopt
getpass
gettext
glob
grp
gzip
hashlib               christian.heimes, gregory.p.smith
heapq                 rhettinger*, stutzbach
hmac                  christian.heimes, gregory.p.smith
html                  ezio.melotti
http
idlelib               kbk (inactive), terry.reedy*, roger.serwy (inactive),
                      taleinat
imaplib
imghdr
imp
importlib             brett.cannon
inspect               yselivanov
io                    benjamin.peterson, stutzbach
ipaddress             pmoody
itertools             rhettinger*
json                  bob.ippolito (inactive), ezio.melotti, rhettinger
keyword
lib2to3               benjamin.peterson
libmpdec              
linecache
locale                lemburg
logging               vinay.sajip
lzma
mailbox
mailcap
marshal
math                  mark.dickinson, rhettinger, stutzbach
mimetypes
mmap                  twouters
modulefinder          theller (inactive), jvr
msilib
msvcrt
multiprocessing       davin*, pitrou, jnoller (inactive), sbt (inactive)
netrc
nis
nntplib
numbers
operator
optparse              aronacher
os
os.path               serhiy.storchaka
ossaudiodev
parser                benjamin.peterson, pablogsal
pathlib
pdb
pickle                alexandre.vassalotti
pickletools           alexandre.vassalotti
pipes
pkgutil
platform              lemburg
plistlib
poplib
posix                 larry
pprint                fdrake
profile
pstats
pty                   twouters*
pwd
py_compile
pyclbr
pydoc
queue                 rhettinger*
quopri
random                rhettinger, mark.dickinson
re                    effbot (inactive), ezio.melotti, serhiy.storchaka
readline              twouters
reprlib
resource              twouters
rlcompleter
runpy                 ncoghlan
sched
secrets
select
selectors             neologix, giampaolo.rodola
shelve
shlex
shutil                tarek, giampaolo.rodola
signal
site
smtpd                 giampaolo.rodola
smtplib
sndhdr
socket
socketserver
spwd
sqlite3               ghaering
ssl                   janssen, christian.heimes, dstufft, alex
stat                  christian.heimes
statistics            steven.daprano, rhettinger, taleinat
string
stringprep
struct                mark.dickinson, meador.inge
subprocess            astrand (inactive), giampaolo.rodola
sunau
symbol
symtable              benjamin.peterson
sys
sysconfig             tarek
syslog                jafo*
tabnanny              tim.peters (inactive)
tarfile               lars.gustaebel
telnetlib
tempfile
termios               twouters
test                  ezio.melotti
textwrap
threading             pitrou
time                  belopolsky, p-ganssle
timeit
tkinter               gpolo, serhiy.storchaka
token
tokenize              meador.inge
trace                 belopolsky
traceback
tracemalloc           vstinner
tty                   twouters*
turtle                gregorlingl, willingc
types                 yselivanov
typing                gvanrossum, levkivskyi*
unicodedata           lemburg, ezio.melotti
unittest              michael.foord*, ezio.melotti, rbcollins
unittest.mock         michael.foord*
urllib                orsenthil
uu
uuid
venv                  vinay.sajip
warnings
wave
weakref               fdrake
webbrowser
winreg                stutzbach
winsound              effbot (inactive)
wsgiref               pje
xdrlib
xml.dom
xml.dom.minidom
xml.dom.pulldom
xml.etree             effbot (inactive), eli.bendersky*, scoder
xml.parsers.expat
xml.sax
xml.sax.handler
xml.sax.saxutils
xml.sax.xmlreader
xmlrpc
zipapp                paul.moore
zipfile               alanmcintyre, serhiy.storchaka, twouters
zipimport             twouters*
zlib                  twouters
====================  =============================================


Tools
-----
==================  ===========
Tool                Maintainers
==================  ===========
Argument Clinic     larry
PEG Generator       gvanrossum, pablogsal, lys.nikolaou
==================  ===========


Platforms
---------
===================   ===========
Platform              Maintainers
===================   ===========
AIX                   David.Edelsohn
Cygwin                jlt63, stutzbach
FreeBSD
HP-UX
Linux
Mac OS X              ronaldoussoren, ned.deily
NetBSD1
OS2/EMX               aimacintyre
Solaris/OpenIndiana   jcea
Windows               tim.golden, zach.ware, steve.dower, paul.moore
JVM/Java              frank.wierzbicki
===================   ===========


Miscellaneous
-------------
==================  ==========================================================
Interest Area       Maintainers
==================  ==========================================================
algorithms          rhettinger*
argument clinic     larry
ast/compiler        benjamin.peterson, brett.cannon, yselivanov, pablogsal, Mark.Shannon
autoconf/makefiles  twouters*
bsd
bug tracker         ezio.melotti
buildbots           zach.ware, pablogsal
bytecode            benjamin.peterson, yselivanov, Mark.Shannon
context managers    ncoghlan
core workflow       mariatta
coverity scan       christian.heimes, brett.cannon, twouters
cryptography        gregory.p.smith, dstufft
data formats        mark.dickinson
database            lemburg
devguide            eric.araujo, ezio.melotti, willingc, mariatta
documentation       ezio.melotti, eric.araujo, mdk, willingc
emoji               mariatta
extension modules   petr.viktorin, ncoghlan
filesystem          giampaolo.rodola
f-strings           eric.smith*
GUI
i18n                lemburg, eric.araujo
import machinery    brett.cannon, ncoghlan, eric.snow
io                  benjamin.peterson, stutzbach
locale              lemburg
mathematics         mark.dickinson, lemburg, stutzbach, rhettinger
memory management   tim.peters, lemburg, twouters
memoryview          
networking          giampaolo.rodola,
object model        benjamin.peterson, twouters
packaging           tarek, lemburg, alexis, eric.araujo, dstufft, paul.moore
peg parser          gvanrossum, pablogsal, lys.nikolaou
performance         brett.cannon, vstinner, serhiy.storchaka, yselivanov, rhettinger, Mark.Shannon
pip                 ncoghlan, dstufft, paul.moore, Marcus.Smith, pradyunsg
py3 transition      benjamin.peterson
release management  tarek, lemburg, benjamin.peterson, barry,
                    gvanrossum, anthonybaxter, eric.araujo, ned.deily,
                    georg.brandl, mdk
str.format          eric.smith*
testing             michael.foord, ezio.melotti
test coverage
threads
time and dates      lemburg, belopolsky, p-ganssle
unicode             lemburg, ezio.melotti, benjamin.peterson,
version control     eric.araujo, ezio.melotti
==================  ==========================================================


Documentation Translations
--------------------------
=============  ============
Translation    Coordinator
=============  ============
French         mdk
Japanese       inada.naoki
Korean         flowdas
Bengali India  kushal.das
Hungarian      gbtami
Portuguese     rougeth
Chinese (TW)   adrianliaw
Chinese (CN)   zhsj
=============  ============
