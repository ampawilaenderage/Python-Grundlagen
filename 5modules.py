#!/usr/bin/env python3


import mymodul
import mymodul as mm
from mymodul import myFunction
from mymodul import *


#
# Arbeiten mit Modulen - durch import
#

# Es gibt zwei Arten von Python-Dateien:
#
#       Python-(Haupt)-Programm
#           beginnt mit #!/usr/bin/env python3
#           ist ausführbar  z.B.    run progname.py         in der Python-Shell
#                                   python progname.py      Windows-Konsole (z.B. PowerShell)
#                                   ./progname.py           Linux-Terminal
#           kann Python-Module importieren
#
#       Python-Modul
#           ist NICHT ausführbar (sollte es nicht sein !!!)
#           wird importiert
#           enthält (idR) keine eigenen ausführbaren Anweisungen
#               Ausnahme: Initialisierung des Moduls
#           enthält Klassen / Funktionen / ...
#           kann andere Module importieren
#           (Python importiert jedes Modul nur EINMAL)
#

def main():

    # hier beginnt die Ausführung des Programms

    print('ich bin ein Python-Hauptprogramm')


    #
    # Import Varianten
    #

    # - 1 -
    # import modulname
    # es werden ALLE Elemente des Moduls importiert
    # aber NUR modulname landet im Namensraum
    # modulname.funktion()

    # import mymodul
    mymodul.myFunction()
    mc = mymodul.MyClass()
    mc.show()


    # - 2 -
    # import modulname as xy
    # es werden ALLE Elemente des Moduls importiert
    # aber NUR xy landet im Namensraum
    # xy.funktion()

    # import mymodul as mm
    mm.myFunction()
    mc = mm.MyClass()
    mc.show()


    # - 3 -
    # from modulname import funktion, Klasse, ...
    # NUR die aufgeführten Elemente werden importiert UND landen im Namnesraum
    # funktion()
    # k = Klasse()

    # from mymodul import myFunction
    myFunction()
    # mc = MyClass()


    # - 4 -
    # from modulname import *
    # ALLE ELemente des Moduls werden importiert UND landen im Namensraum
    # sehr bequem - aber (in Python) nicht immer die beste Lösung

    # from mymodul import *
    myFunction()
    mc = MyClass()
    mc.show()

    # Informationen über Module:
    #
    #       >>> help('modules')     # Übersicht aller aktuell verfügbaren Module
    #
    # 1oo                 _statistics         ensurepip           pylab
    # 2poly               _string             enum                pymysql
    # 3special            _strptime           errno               pyparsing
    # 4dc                 _struct             faulthandler        pytz
    # 5modules            _suggestions        filecmp             queue
    # 81d243bd2c585b0f4821__mypyc _symtable           fileinput           quopri
    # PIL                 _sysconfig          flask               random
    # PyQt6               _testbuffer         fnmatch             re
    # __future__          _testcapi           fontTools           reprlib
    # __hello__           _testclinic         fractions           requests
    # __phello__          _testclinic_limited ftplib              rlcompleter
    # _abc                _testconsole        functools           runpy
    # _aix_support        _testimportmultiple gc                  sched
    # _android_support    _testinternalcapi   genericpath         secrets
    # _apple_support      _testlimitedcapi    getopt              select
    # _ast                _testmultiphase     getpass             selectors
    # _ast_unparse        _testsinglephase    gettext             shelve
    # _asyncio            _thread             glob                shlex
    # _bisect             _threading_local    graphlib            shutil
    # _blake2             _tkinter            gzip                signal
    # _bz2                _tokenize           hashlib             site
    # _codecs             _tracemalloc        heapq               six
    # _codecs_cn          _types              hmac                smtplib
    # _codecs_hk          _typing             html                socket
    # _codecs_iso2022     _uuid               http                socketserver
    # _codecs_jp          _warnings           idlelib             sqlite3
    # _codecs_kr          _weakref            idna                sre_compile
    # _codecs_tw          _weakrefset         imaplib             sre_constants
    # _collections        _winapi             importlib           sre_parse
    # _collections_abc    _wmi                inspect             ssl
    # _colorize           _zoneinfo           io                  stat
    # _compat_pickle      _zstd               ipaddress           statistics
    # _contextvars        abc                 itertools           string
    # _csv                annotationlib       itsdangerous        stringprep
    # _ctypes             antigravity         jinja2              struct
    # _ctypes_test        argparse            json                subprocess
    # _datetime           array               keyword             symtable
    # _decimal            ast                 kiwisolver          sys
    # _elementtree        asyncio             linecache           sysconfig
    # _functools          atexit              locale              tabnanny
    # _hashlib            base64              logging             tarfile
    # _heapq              bdb                 lzma                tempfile
    # _hmac               binascii            mailbox             test
    # _imp                bisect              markupsafe          textwrap
    # _interpchannels     blinker             marshal             this
    # _interpqueues       builtins            math                threading
    # _interpreters       bz2                 matplotlib          time
    # _io                 cProfile            mimetypes           timeit
    # _ios_support        calendar            mmap                tkinter
    # _json               certifi             modulefinder        token
    # _locale             charset_normalizer  msvcrt              tokenize
    # _lsprof             click               multiprocessing     tomllib
    # _lzma               cmath               mymodul             trace
    # _markupbase         cmd                 netrc               traceback
    # _md5                code                nt                  tracemalloc
    # _multibytecodec     codecs              ntpath              tty
    # _multiprocessing    codeop              nturl2path          turtle
    # _opcode             collections         numbers             turtledemo
    # _opcode_metadata    colorama            numpy               types
    # _operator           colorsys            opcode              typing
    # _osx_support        compileall          operator            unicodedata
    # _overlapped         compression         optparse            unittest
    # _pickle             concurrent          os                  urllib
    # _py_abc             configparser        packaging           urllib3
    # _py_warnings        contextlib          pathlib             uuid
    # _pydatetime         contextvars         pdb                 venv
    # _pydecimal          contourpy           pickle              warnings
    # _pyio               copy                pickletools         wave
    # _pylong             copyreg             pip                 weakref
    # _pyrepl             csv                 pkgutil             webbrowser
    # _queue              ctypes              platform            werkzeug
    # _random             curses              plistlib            winreg
    # _remote_debugging   cycler              poplib              winsound
    # _sha1               dataclasses         posixpath           wsgiref
    # _sha2               datetime            pprint              xml
    # _sha3               dateutil            profile             xmlrpc
    # _signal             dbm                 pstats              xxsubtype
    # _sitebuiltins       decimal             pty                 zipapp
    # _socket             difflib             py_compile          zipfile
    # _sqlite3            dis                 pyclbr              zipimport
    # _sre                doctest             pydoc               zlib
    # _ssl                email               pydoc_data          zoneinfo
    # _stat               encodings           pyexpat
    #
    #   >>> help('mymodul')



if __name__ == '__main__':
    main()
