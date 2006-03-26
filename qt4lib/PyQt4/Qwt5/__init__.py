"""Qwt5 -- a Python interface to the Qwt library.
"""
#
# Copyright (C) 2003-2006 Gerard Vermeulen
#
# This file is part of PyQwt.
#
# PyQwt is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PyQwt is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA


from Qwt import *

try:
    to_na_array = toNumarray
except NameError:
    pass

try:
    to_np_array = toNumeric2
except NameError:
    pass

# Local Variables: ***
# mode: python ***
# End: ***
