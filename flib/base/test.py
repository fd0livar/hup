# -*- coding: utf-8 -*-
#
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
"""Unittests."""

__copyright__ = '2019 Frootlab Developers'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

import functools
import inspect
from typing import Any, Dict, List, NamedTuple, Tuple
import unittest
from flib.base import otree
from flib.typing import AnyOp, Method, ErrMeta, Module, Function

try:
    import numpy as np
except ModuleNotFoundError:
    np = None

Cases = List['Case']

#
# Global Test Settings
#

skip_completeness_test: bool = False

#
# Parameter Classes
#

class Case(NamedTuple):
    """Class for the storage of Case parameters."""

    args: Tuple[Any, ...] = tuple()
    kwds: Dict[Any, Any] = {}
    value: Any = None

#
# Test Cases
#

class GenericTest(unittest.TestCase):
    """Custom testcase."""

    def assertExactEqual(self, a: object, b: object) -> None:
        """Assert that two objects are equal in type and value."""
        self.assertEqual(type(a), type(b))
        self.assertEqual(a, b)

    def assertAllEqual(self, a: object, b: object) -> None:
        """Assert that two objects are equal."""
        if np and isinstance(a, np.ndarray):
            self.assertTrue(np.alltrue(a == b))
        else:
            self.assertEqual(a, b)

    def assertNotRaises(
            self, cls: ErrMeta, func: AnyOp, *args: Any, **kwds: Any) -> None:
        """Assert that an exception is not raised."""
        try:
            func(*args, **kwds)
        except cls:
            raise AssertionError(
                f"function {func.__name__} raises error {cls.__name__}")

    def assertIsSubclass(self, cls: type, supercls: type) -> None:
        """Assert that a class is a subclass of another."""
        self.assertTrue(issubclass(cls, supercls))

    def assertCaseIsSubclass(
            self, func: AnyOp, supercls: type, cases: Cases) -> None:
        """Assert outcome type of a class constructor."""
        for case in cases:
            with self.subTest(case):
                self.assertIsSubclass(func(*case.args, **case.kwds), supercls)

    def assertCaseIn(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations are in the given values."""
        for case in cases:
            with self.subTest(case):
                self.assertIn(func(*case.args, **case.kwds), case.value)

    def assertCaseNotIn(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations are in the given values."""
        for case in cases:
            with self.subTest(case):
                self.assertNotIn(func(*case.args, **case.kwds), case.value)

    def assertCaseContain(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations comprise the given values."""
        for case in cases:
            with self.subTest(case):
                self.assertIn(case.value, func(*case.args, **case.kwds))

    def assertCaseNotContain(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations comprise the given values."""
        for case in cases:
            with self.subTest(case):
                self.assertNotIn(case.value, func(*case.args, **case.kwds))

    def assertCaseTrue(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations cast to True."""
        for case in cases:
            with self.subTest(case):
                self.assertTrue(func(*case.args, **case.kwds))

    def assertCaseFalse(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations cast to False."""
        for case in cases:
            with self.subTest(case):
                self.assertFalse(func(*case.args, **case.kwds))

    def assertCaseEqual(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations equal the given values."""
        for case in cases:
            with self.subTest(case):
                self.assertAllEqual(func(*case.args, **case.kwds), case.value)

    def assertCaseNotEqual(self, func: AnyOp, cases: Cases) -> None:
        """Assert that all function evaluations differ from the given values."""
        for case in cases:
            with self.subTest(case):
                self.assertNotEqual(func(*case.args, **case.kwds), case.value)

    def assertCaseRaises(self, cls: ErrMeta, func: AnyOp, cases: Cases) -> None:
        """Assert that all function parameters raise an exception."""
        for case in cases:
            with self.subTest(case):
                self.assertRaises(cls, func, *case.args, **case.kwds)

    def assertCaseNotRaises(
            self, cls: ErrMeta, func: AnyOp, cases: Cases) -> None:
        """Assert that no function parameter raises an exception."""
        for case in cases:
            with self.subTest(case):
                self.assertNotRaises(cls, func, *case.args, **case.kwds)

class ModuleTest(GenericTest):
    """Custom testcase."""

    module: Module

    def assertModuleIsComplete(self) -> None:
        """Assert that all members of module are tested."""
        if not hasattr(self, 'module') or not self.test_completeness:
            return

        # Get reference to module
        module = getattr(self, 'module', None)
        if not isinstance(module, Module):
            raise AssertionError(f"module has not been specified")

        # Get module members
        members = set()
        candidates = getattr(module, '__all__', None)
        if not candidates:
            LruWrapper = functools._lru_cache_wrapper # pylint: disable=W0212
            classinfo = (type, Function, LruWrapper)
            candidates = otree.get_members(module, classinfo=classinfo)
        for name in candidates:
            if name.startswith('_'):
                continue # Filter protected members
            obj = getattr(module, name)
            if obj.__module__ != module.__name__:
                continue # Filter imported members
            if BaseException in getattr(obj, '__mro__', []):
                continue # Filter exceptions
            if inspect.isabstract(obj):
                continue # Filter abstract classes
            members.add(name)

        # Get tested module members
        tested = set(name[5:] for name in otree.get_members(
            self, classinfo=Method, pattern='test_*'))

        # Get untested module members
        untested = members - tested
        if not untested:
            return

        # Raise error on untested module members
        raise AssertionError(
            f"module '{self.module.__name__}' comprises "
            f"untested members: {', '.join(sorted(untested))}")

    def test_completeness(self) -> None:
        self.assertModuleIsComplete()
