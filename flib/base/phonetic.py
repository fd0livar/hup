# -*- coding: utf-8 -*-
# Copyright (C) 2019 Frootlab Developers
#
# This file is part of the Frootlab Shared Library, https://github.com/frootlab
#
#  The Frootlab Shared Library (flib) is free software: you can redistribute it
#  and/or modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation, either version 3 of the License,
#  or (at your option) any later version.
#
#  The Frootlab Shared Library (flib) is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#  Public License for more details. You should have received a copy of the GNU
#  General Public License along with the frootlab shared library. If not, see
#  <http://www.gnu.org/licenses/>.
#
"""Phonetic Algorithms."""

__license__ = 'GPLv3'
__copyright__ = 'Copyright (c) 2019 Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__docformat__ = 'google'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

def soundex(string: str) -> str:
    """Calculate Soundex Index.

    Soundex is a phonetic algorithm for indexing names by sound, as pronounced
    in English. The goal is for homophones to be encoded to the same
    representation so that they can be matched despite minor differences in
    spelling.

    """
    # Clear String
    string = ''.join(filter(str.isalpha, string)).upper()
    if len(string) < 2:
        return string.ljust(4, '0')[:4]

    # Apply Soundex Replacement Rules
    first = string[0]
    src = 'AEIOUYHWBFPVCGJKQSXZDTLMNR'
    tgt = '000000**111122222222334556'
    trans = str.maketrans(src, tgt)
    string = string.translate(trans).replace('*', '')
    for c in '123456':
        string = string.replace(c * 2, c)
    string = string.replace('0', '')

    # Apply Representation
    if first.translate(trans) == string[0]:
        string = string[1:]
    return first + string.ljust(3, '0')[:3]
