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
"""Runner script for unittests."""

__copyright__ = '2019 Frootlab Developers'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

import fnmatch
import importlib
import os
import sys
import unittest
from flib.base import pkg

#
# Script Configuration
#

package_name = 'flib'

#
# Runner Script
#

if __name__ == "__main__":
    argv = sys.argv[1:]
    module = argv[0] if argv else None

    # Import package and tests
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, path)
    package = importlib.import_module(package_name)
    tests = importlib.import_module('tests')

    # Search and filter TestCases within tests
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    cases = pkg.search(
        module=tests, classinfo=unittest.TestCase, val='reference', errors=True)
    for ref in cases.values():
        if module:
            if not hasattr(ref, 'module'):
                continue
            if not hasattr(ref.module, '__name__'):
                continue
            if not fnmatch.fnmatch(ref.module.__name__, f'*{module}*'):
                continue
        suite.addTests(loader.loadTestsFromTestCase(ref))

    # Initialize TestRunner and run TestCases
    package_version = getattr(package, '__version__', '')
    print(f"testing {package_name} {package_version}")
    runner = unittest.TextTestRunner(stream=sys.stderr, verbosity=2)
    runner.run(suite)
