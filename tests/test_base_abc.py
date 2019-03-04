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
"""Unittests for module 'flib.base.abc'."""

__license__ = 'GPLv3'
__copyright__ = 'Copyright (c) 2019 Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__docformat__ = 'google'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

from flib.base import abc, test

#
# Test Cases
#

class TestModule(test.ModuleTest):
    module = abc

    def test_SingletonMeta(self) -> None:
        pass # Implicitly tested by test_Singleton()

    def test_Singleton(self) -> None:
        T = type('Singleton', (abc.Singleton, ), {})

        self.assertTrue(T() is T())
        self.assertTrue(T(1) is T(2))

    def test_IsolatedMeta(self) -> None:
        pass # Implicitly tested by test_Isolated()

    def test_Isolated(self) -> None:
        T = type('Isolated', (abc.Isolated, ), {})

        self.assertFalse(type(T()) is type(T()))

    def test_sentinel(self) -> None:

        @abc.sentinel
        class Sentinel(abc.Singleton):
            def __init__(self) -> None:
                self.test = True

        self.assertEqual(Sentinel.__name__, type(Sentinel).__name__)
        self.assertTrue(hasattr(Sentinel, 'test'))
        self.assertTrue(Sentinel.test)

    def test_MultitonMeta(self) -> None:
        pass # Implicitly tested by test_Multiton()

    def test_Multiton(self) -> None:
        f = type('Multiton', (abc.Multiton, ), {})

        self.assertTrue(f() is f())
        self.assertTrue(f(1) is f(1))
        self.assertFalse(f(1) is f(2))