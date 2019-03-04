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
"""Unittests for module 'flib.base.call'."""

__license__ = 'GPLv3'
__copyright__ = 'Copyright (c) 2019 Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__docformat__ = 'google'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

from collections import OrderedDict
from flib.base import call, test
from flib.base.test import Case

#
# Test Cases
#

class TestCall(test.ModuleTest):
    module = call

    def test_safe_call(self) -> None:
        f = call.parameters
        self.assertCaseEqual(call.safe_call, [
            Case(args=(f, list), value=OrderedDict()),
            Case(args=(f, list), kwds={'test': True}, value=OrderedDict())])

    def test_parameters(self) -> None:
        f = call.parameters
        self.assertCaseEqual(call.parameters, [
            Case(args=(f, ), value=OrderedDict()),
            Case(args=(f, list), value=OrderedDict([('op', list)])),
            Case(args=(f, list), kwds={'test': True},
                value=OrderedDict([('op', list), ('test', True)]))])

    def test_parse(self) -> None:
        self.assertEqual(call.parse("f(1., 'a', b = 2)"),
            ('f', (1.0, 'a'), {'b': 2}))
