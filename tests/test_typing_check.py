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
"""Unittests for module 'flib.typing.check'."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

from typing import Any, Callable, Union
from flib.base import test
from flib.base.test import Case
from flib.typing import check

#
# Test Cases
#

class TestCheck(test.ModuleTest):
    module = check

    def test_has_type(self) -> None:
        self.assertCaseNotRaises(TypeError, check.has_type, [
            Case(args=('', 0, int)),
            Case(args=('', '', str)),
            Case(args=('', list(), list)),
            Case(args=('', dict(), dict)),
            Case(args=('', object, Callable)),
            Case(args=('', object, Any))])

        self.assertCaseRaises(TypeError, check.has_type, [
            Case(args=('', '', int)),
            Case(args=('', 1., int)),
            Case(args=('', 1, float)),
            Case(args=('', dict(), list)),
            Case(args=('', None, Callable))])

    def test_is_identifier(self) -> None:
        self.assertCaseNotRaises(ValueError, check.is_identifier, [
            Case(args=('', 'id')),
            Case(args=('', 'ID')),
            Case(args=('', 'Table')),
            Case(args=('', 'Table1'))])

        self.assertCaseRaises(ValueError, check.is_identifier, [
            Case(args=('', '')),
            Case(args=('', '1')),
            Case(args=('', 'a b')),
            Case(args=('', 'a.b'))])

    def test_has_opt_type(self) -> None:
        self.assertCaseNotRaises(TypeError, check.has_opt_type, [
            Case(args=('', None, int)),
            Case(args=('', None, str)),
            Case(args=('', list(), list)),
            Case(args=('', dict(), dict))])

        self.assertCaseRaises(TypeError, check.has_opt_type, [
            Case(args=('', '', int)),
            Case(args=('', 1., int)),
            Case(args=('', 1, float)),
            Case(args=('', dict(), list))])

    def test_is_callable(self) -> None:
        self.assertCaseNotRaises(TypeError, check.is_callable, [
            Case(args=('', int)),
            Case(args=('', dict)),
            Case(args=('', list)),
            Case(args=('', str))])

        self.assertCaseRaises(TypeError, check.has_type, [
            Case(args=('', None)),
            Case(args=('', 0)),
            Case(args=('', '')),
            Case(args=('', set()))])

    def test_is_typehint(self) -> None:
        self.assertCaseNotRaises(TypeError, check.is_typehint, [
            Case(args=('', str)),
            Case(args=('', (int, float))),
            Case(args=('', Any)),
            Case(args=('', Callable))])

        self.assertCaseRaises(TypeError, check.is_typehint, [
            Case(args=('', None)),
            Case(args=('', 0)),
            Case(args=('', '')),
            Case(args=('', Union))])

    def test_is_class(self) -> None:
        self.assertCaseNotRaises(TypeError, check.is_class, [
            Case(args=('', int)),
            Case(args=('', dict)),
            Case(args=('', list)),
            Case(args=('', str))])

        self.assertCaseRaises(TypeError, check.is_class, [
            Case(args=('', None)),
            Case(args=('', 0)),
            Case(args=('', '')),
            Case(args=('', set()))])

    def test_is_subclass(self) -> None:
        self.assertCaseNotRaises(TypeError, check.is_subclass, [
            Case(args=('', int, object)),
            Case(args=('', dict, dict)),
            Case(args=('', list, object)),
            Case(args=('', str, str))])

        self.assertCaseRaises(TypeError, check.is_subclass, [
            Case(args=('', int, str)),
            Case(args=('', dict, list)),
            Case(args=('', object, float)),
            Case(args=('', str, complex))])

    def test_is_subset(self) -> None:
        self.assertCaseNotRaises(ValueError, check.is_subset, [
            Case(args=('', set(), '', set())),
            Case(args=('', {1}, '', {1, 2})),
            Case(args=('', {2}, '', {1, 2})),
            Case(args=('', {2, 1}, '', {1, 2}))])

        self.assertCaseRaises(ValueError, check.is_subset, [
            Case(args=('', {1}, '', set())),
            Case(args=('', {2}, '', {1})),
            Case(args=('', {1, 2}, '', {1})),
            Case(args=('', {1, 2, 3}, '', set()))])

    def test_no_dublicates(self) -> None:
        self.assertCaseNotRaises(ValueError, check.no_dublicates, [
            Case(args=('', set())),
            Case(args=('', {1, 1, 2, 3})),
            Case(args=('', [1, 2, 3])),
            Case(args=('', {1: 1, 2: 2}))])

        self.assertCaseRaises(ValueError, check.no_dublicates, [
            Case(args=('', (1, 1))),
            Case(args=('', [1, 2, 2]))])

    def test_is_positive(self) -> None:
        self.assertCaseNotRaises(ValueError, check.is_positive, [
            Case(args=('', 1)),
            Case(args=('', 1.))])

        self.assertCaseRaises(ValueError, check.is_positive, [
            Case(args=('', 0)),
            Case(args=('', -1)),
            Case(args=('', -1.))])

    def test_is_negative(self) -> None:
        self.assertCaseNotRaises(ValueError, check.is_negative, [
            Case(args=('', -1)),
            Case(args=('', -1.))])

        self.assertCaseRaises(ValueError, check.is_negative, [
            Case(args=('', 0)),
            Case(args=('', 1)),
            Case(args=('', 1.))])

    def test_is_not_positive(self) -> None:
        self.assertCaseNotRaises(ValueError, check.is_not_positive, [
            Case(args=('', 0)),
            Case(args=('', -1)),
            Case(args=('', -1.))])

        self.assertCaseRaises(ValueError, check.is_not_positive, [
            Case(args=('', 1)),
            Case(args=('', 1.))])

    def test_is_not_negative(self) -> None:
        self.assertCaseNotRaises(ValueError, check.is_not_negative, [
            Case(args=('', 0)),
            Case(args=('', 1)),
            Case(args=('', 1.))])

        self.assertCaseRaises(ValueError, check.is_not_negative, [
            Case(args=('', -1)),
            Case(args=('', -1.))])

    def test_has_attr(self) -> None:
        self.assertCaseNotRaises(AttributeError, check.has_attr, [
            Case(args=('', 'format')),
            Case(args=(0, 'real')),
            Case(args=(1j, 'imag'))])

        self.assertCaseRaises(AttributeError, check.has_attr, [
            Case(args=(list(), 'keys')),
            Case(args=(0, ''))])

    def test_has_size(self) -> None:
        self.assertCaseNotRaises(ValueError, check.has_size, [
            Case(args=('', set()), kwds={'size': 0}),
            Case(args=('', set()), kwds={'min_size': 0}),
            Case(args=('', tuple([1])), kwds={'max_size': 1}),
            Case(args=('', [1, 2]), kwds={'min_size': 1, 'max_size': 3})])

        self.assertCaseRaises(ValueError, check.has_size, [
            Case(args=('', set()), kwds={'size': 1}),
            Case(args=('', tuple()), kwds={'min_size': 1}),
            Case(args=('', set([1])), kwds={'max_size': 0}),
            Case(args=('', [1, 2]), kwds={'min_size': 3, 'max_size': 5})])

    def test_not_empty(self) -> None:
        self.assertCaseNotRaises(ValueError, check.not_empty, [
            Case(args=('', 'x')),
            Case(args=('', {1})),
            Case(args=('', [1])),
            Case(args=('', {1: 1}))])

        self.assertCaseRaises(ValueError, check.not_empty, [
            Case(args=('', set())),
            Case(args=('', tuple())),
            Case(args=('', [])),
            Case(args=('', ''))])
