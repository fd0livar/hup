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
"""Unittests for module 'flib.io.plain'."""

__license__ = 'GPLv3'
__copyright__ = 'Copyright (c) 2019 Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__docformat__ = 'google'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

from flib.base import env, test
from flib.base.test import Case
from flib.io import plain

#
# Test Cases
#

class TestPlain(test.ModuleTest):
    module = plain

    def setUp(self) -> None:
        self.filepath = env.get_temp_file(suffix='.txt')
        self.comment = "comment line"
        self.content = ['first content line', 'second content line']
        self.text = f"# {self.comment}\n\n" + '\n'.join(self.content)
        plain.save(self.text, self.filepath)

    def test_get_name(self) -> None:
        name = self.filepath.name
        path = self.filepath
        string = str(self.filepath)
        fh = self.filepath.open(mode='r')
        self.assertCaseEqual(plain.get_name, [
            Case(args=(path, ), value=name),
            Case(args=(string, ), value=name),
            Case(args=(fh, ), value=name)])

    def test_openx(self) -> None:
        filepath = env.get_temp_file(suffix='.txt')
        with self.subTest(file=filepath):
            with plain.openx(filepath, mode='w') as fh:
                fh.write(self.text)
            if filepath.is_file():
                with plain.openx(filepath, mode='r') as fh:
                    text = fh.read()
                filepath.unlink()
                self.assertTrue(text == self.text)
        file = filepath.open(mode='w')
        with self.subTest(file=file):
            with plain.openx(file, mode='w') as fh:
                fh.write(self.text)
            if not file.closed:
                file.close()
                file = filepath.open(mode='r')
                with plain.openx(file, mode='r') as fh:
                    text = fh.read()
                if not file.closed:
                    file.close()
                    self.assertTrue(text == self.text)
        if not file.closed:
            file.close()
        if filepath.is_file():
            filepath.unlink()

    def test_save(self) -> None:
        self.assertTrue(self.filepath.is_file())

    def test_load(self) -> None:
        text = plain.load(self.filepath)
        self.assertEqual(text, self.text)

    def test_get_comment(self) -> None:
        comment = plain.get_comment(self.filepath)
        self.assertEqual(comment, self.comment)

    def test_get_content(self) -> None:
        content = plain.get_content(self.filepath)
        self.assertEqual(content, self.content)

    def tearDown(self) -> None:
        if self.filepath.is_file():
            self.filepath.unlink()
