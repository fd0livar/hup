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
"""Multithreading functions."""

__copyright__ = '2019 Frootlab Developers'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'frootlab@gmail.com'
__authors__ = ['Patrick Michl <patrick.michl@gmail.com>']

import threading
from typing import Any
from flib.typing import AnyOp

def create(func: AnyOp, *args: Any, **kwds: Any) -> object:
    """Create and start thread for given callable and arguments."""
    thr = threading.Thread(
        target=(lambda func, args, kwds: func(*args, **kwds)),
        args=(func, args, kwds))

    thr.daemon = True
    thr.start()

    return thr
