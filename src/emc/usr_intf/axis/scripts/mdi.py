#!/usr/bin/env python3
#    This is a component of AXIS, a front-end for LinuxCNC
#    Copyright 2004, 2005, 2006 Jeff Epler <jepler@unpythonic.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

'''Manual Data Input - issue a single line of G-code to the running system

mdi.py may be specified on the commandline, e.g.,
        bin/mdi g0 x0
'''
import sys, os
import linuxcnc

#if len(sys.argv) > 1:
#    linuxcnc.nmlfile = sys.argv[1]
#    del sys.argv[1]

c = linuxcnc.command()
s = linuxcnc.stat()

if len(sys.argv) > 1:
    c.mode(linuxcnc.MODE_MDI)
    c.mdi(" ".join(sys.argv[1:]))
else:
    try:
        while 1:
            mdi = eval(input("MDI> "))
            if mdi == '':
                s.poll()
                print(s.position)
            else:
                c.mode(linuxcnc.MODE_MDI)
                c.mdi(mdi)
    except (SystemExit, EOFError, KeyboardInterrupt): pass

# vim:sw=4:sts=4:et:
