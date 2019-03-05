# -*- coding: utf-8 -*-
# Copyright (C) 2019 Frootlab Developers
#
# This file is part of the Frootlab Shared Library (flib)
# https://github.com/frootlab/flib
#
#  The Frootlab Shared Library is free software: you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or (at your
#  option) any later version.
#
#  The Frootlab Shared Library is distributed in the hope that it will be
#  useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
#  Public License for more details. You should have received a copy of the GNU
#  General Public License along with the frootlab shared library. If not, see
#  <http://www.gnu.org/licenses/>.
#
"""Unittests for module 'flib.base.phonetic'."""

__license__ = 'GPLv3'
__copyright__ = 'Copyright (c) 2019 Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__docformat__ = 'google'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

from flib.base import phonetic, test
from flib.base.test import Case

#
# Test Cases
#

class TestPhonetic(test.ModuleTest):
    module = phonetic

    def test_soundex(self) -> None:
        self.assertCaseEqual(phonetic.soundex, [
            Case(('Smith', ), {}, 'S530'),
            Case(('Robert', ), {}, 'R163'),
            Case(('Rupert', ), {}, 'R163'),
            Case(('Rubin', ), {}, 'R150'),
            Case(('Ashcraft', ), {}, 'A261'),
            Case(('Tymczak', ), {}, 'T522'),
            Case(('Pfister', ), {}, 'P236'),
            Case(('Honeyman', ), {}, 'H555')])
