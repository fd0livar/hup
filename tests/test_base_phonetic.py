# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab
#
# This file is part of Frootlab Hup, https://www.frootlab.org/hup
#
#  Hup is free software: you can redistribute it and/or modify it under the
#  terms of the GNU General Public License as published by the Free Software
#  Foundation, either version 3 of the License, or (at your option) any later
#  version.
#
#  Hup is distributed in the hope that it will be useful, but WITHOUT ANY
#  WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
#  A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#  You should have received a copy of the GNU General Public License along with
#  Hup. If not, see <http://www.gnu.org/licenses/>.
#
"""Unittests for module 'hup.base.phonetic'."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

from hup.base import phonetic, test
from hup.base.test import Case

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
