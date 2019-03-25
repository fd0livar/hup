# -*- coding: utf-8 -*-
#
# Copyright (C) 2019 Frootlab
#
# This file is part of the Frootlab Shared Library (flib)
# https://www.frootlab.org/flib
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
"""Unittests for module 'flib.base.stack'."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

from flib.base import stack, test
from flib.typing import Module

#
# Test Cases
#

class TestStack(test.ModuleTest):
    module = stack

    def test_get_caller_module_name(self) -> None:
        name = stack.get_caller_module_name()
        self.assertEqual(name, __name__)

    def test_get_caller_module(self) -> None:
        module = stack.get_caller_module()
        self.assertIsInstance(module, Module)

    def test_get_caller_name(self) -> None:
        thisname = stack.get_caller_name()
        self.assertEqual(thisname, __name__ + '.test_get_caller_name')
