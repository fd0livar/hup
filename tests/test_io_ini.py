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
"""Unittests for module 'flib.io.ini'."""

__license__ = 'GPLv3'
__copyright__ = 'Copyright (c) 2019 Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__docformat__ = 'google'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

import configparser
from flib.base import env, test
from flib.io import ini

#
# Test Cases
#

class TestIni(test.ModuleTest):
    module = ini

    def setUp(self) -> None:
        self.filepath = env.get_temp_file(suffix='.ini')
        self.comment = '-*- coding: utf-8 -*-'
        self.obj = {
            'n': {'a': 's', 'b': True, 'c': 1},
            'l1': {'a': 1}, 'l2': {'a': 2}}
        self.scheme = {
            'n': {'a': str, 'b': bool, 'c': int},
            'l[0-9]*': {'a': int}}
        self.text = (
            "# -*- coding: utf-8 -*-\n\n"
            "[n]\na = s\nb = True\nc = 1\n\n"
            "[l1]\na = 1\n\n[l2]\na = 2\n\n")
        ini.save(self.obj, self.filepath, comment=self.comment)

    def test_parse(self) -> None:
        parser = configparser.ConfigParser()
        setattr(parser, 'optionxform', lambda key: key)
        parser.read_string(self.text)
        obj = ini.parse(parser, scheme=self.scheme) # type: ignore
        self.assertEqual(obj, self.obj)
        obj = ini.parse(parser, autocast=True)
        self.assertEqual(obj, self.obj)

    def test_encode(self) -> None:
        text = ini.encode(self.obj, comment=self.comment)
        self.assertEqual(text, self.text)

    def test_decode(self) -> None:
        obj = ini.decode(self.text, scheme=self.scheme) # type: ignore
        self.assertEqual(obj, self.obj)
        obj = ini.decode(self.text, autocast=True)
        self.assertEqual(obj, self.obj)

    def test_save(self) -> None:
        self.assertTrue(self.filepath.is_file())

    def test_load(self) -> None:
        obj = ini.load(self.filepath, scheme=self.scheme) # type: ignore
        self.assertEqual(obj, self.obj)
        obj = ini.load(self.filepath, autocast=True)
        self.assertEqual(obj, self.obj)

    def test_get_comment(self) -> None:
        comment = ini.get_comment(self.filepath)
        self.assertEqual(comment, self.comment)

    def tearDown(self) -> None:
        if self.filepath.is_file():
            self.filepath.unlink()
