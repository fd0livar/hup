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
"""Errors and Exceptions."""

__copyright__ = '2019 Frootlab'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

from collections.abc import Sized, Collection
from numbers import Number
from typing import Any, Callable

#
# Protected helper functions for object representation
#

def _repr_items(obj: Collection, sep: str = 'and') -> str:
    """Get an enumerated representation of a collection.

    Args:
        sep: String used as separator for collection items.

    Returns:
        Natural language representation of collection.

    """
    if isinstance(obj, str):
        return repr(obj)

    if hasattr(obj, '__name__'):
        return repr(getattr(obj, '__name__', ''))

    if isinstance(obj, Collection):
        if isinstance(obj, set):
            item = 'element'
        else:
            item = 'item'
        size = len(obj)
        if size == 0:
            return f'no {item}s'
        if size == 1:
            name = repr(str(obj.__iter__().__next__()))
            return f'{item} {name}'
        if size < 4:
            sep = f' {sep} '
            items = [repr(str(each)) for each in obj]
            return f'{item}s ' + sep.join(items)
        return f'some {item}s'

    return repr(obj)

#
# Generic Application Exceptions
#

class UserException(Exception):
    """Base class for user exceptions."""

    def __init__(self, msg: str):
        super().__init__(msg.strip(' .'))

class UserError(UserException):
    """Exception for user errors."""

class UserAssert(UserError, AssertionError):
    """Exception for user asserts."""

#
# Type Errors
#

class MissingKwError(UserAssert, TypeError):
    """Raise when a required keyword argument is not given."""

    def __init__(self, argname: str, obj: Callable) -> None:
        name = getattr(obj, '__name__', obj.__class__.__name__)
        msg = f"{name} missing required keyword argument '{argname}'"
        super().__init__(msg)

class InvalidTypeError(UserAssert, TypeError):
    """Raise when an object is required to be of a given type."""

    def __init__(self, name: str, obj: object, info: object = None) -> None:
        has = obj.__class__.__name__

        if isinstance(info, str):
            msg = f"{name} requires to be {info}"
        elif isinstance(info, type):
            should = info.__name__
            msg = f"{name} requires to be of type {should} not {has}"
        elif isinstance(info, tuple):
            should = _repr_items(info, sep='or')
            msg = f"{name} requires to be of type {should} not {has}"
        else:
            msg = f"{name} has invalid type {has}"

        super().__init__(msg)

class InvalidClassError(UserAssert, TypeError):
    """Raise when an object is required to be of a given subclass."""

    def __init__(self, name: str, obj: object, cls: type) -> None:
        should = cls.__name__
        has = obj.__class__.__name__
        msg = f"{name} requires to be a subclass of {should} not {has}"
        super().__init__(msg)

class NotClassError(UserAssert, TypeError):
    """Raise when an object is required to be a class."""

    def __init__(self, name: str, obj: object) -> None:
        has = obj.__class__.__name__
        msg = f"{name} requires to be a class not {has}"
        super().__init__(msg)

class NotCallableError(UserAssert, TypeError):
    """Raise when an object is required to be callable."""

    def __init__(self, name: str, obj: object) -> None:
        has = obj.__class__.__name__
        msg = f"{name} requires to be callable not {has}"
        super().__init__(msg)

#
# Value Errors
#

class InvalidFormatError(UserAssert, ValueError):
    """Rasise when a string has an invalid format."""

    def __init__(self, name: str, val: str, fmt: str) -> None:
        msg = f"{name} '{val}' does not have the required format {fmt}"
        super().__init__(msg)

class IsPositiveError(UserAssert, ValueError):
    """Raise when a value may not be positive."""

    def __init__(self, name: str, val: Number) -> None:
        msg = f"{name} is required not to be a negative number not {val}"
        super().__init__(msg)

class IsNegativeError(UserAssert, ValueError):
    """Raise when a value may not be negative."""

    def __init__(self, name: str, val: Number) -> None:
        msg = f"{name} is required to be a positive number not {val}"
        super().__init__(msg)

class NotPositiveError(UserAssert, ValueError):
    """Raise when a value must be positive."""

    def __init__(self, name: str, val: Number) -> None:
        msg = f"{name} is required to be a strictly positive number not {val}"
        super().__init__(msg)

class NotNegativeError(UserAssert, ValueError):
    """Raise when a value must be negative."""

    def __init__(self, name: str, val: Number) -> None:
        msg = f"{name} is required to be a strictly negative number not {val}"
        super().__init__(msg)

class ItemNotFoundError(UserAssert, ValueError):
    """Raise when an item is not found within a container."""

    def __init__(self, name: str, val: Any, container: str) -> None:
        msg = f"item {val} of {name} is not contained in {container}"
        super().__init__(msg)

class DublicateError(UserAssert, ValueError):
    """Raise when a collection contains dublicates."""

    def __init__(self, name: str, dubl: set) -> None:
        msg = f"{name} contains dublicates {_repr_items(dubl)}"
        super().__init__(msg)

class NoSubsetError(UserAssert, ValueError):
    """Raise when sequence elements are not contained within another."""

    def __init__(self, a: str, seta: set, b: str, setb: set) -> None:
        diff = set(seta) - set(setb)
        items = _repr_items(diff)
        are = 'are' if len(diff) > 1 else 'is'
        msg = f"{items} of {a} {are} not contained in {b}"
        super().__init__(msg)

class SizeError(UserAssert, ValueError):
    """Raise when a sized object has an invalid size."""

    def __init__(self, name: str, obj: Sized, size: int) -> None:
        msg = (
            f"{name} contains {len(obj)} elements"
            f", but exactly {size} are required")
        super().__init__(msg)

class MinSizeError(UserAssert, ValueError):
    """Raise when a sized object has too few elements."""

    def __init__(self, name: str, obj: Sized, min_len: int) -> None:
        msg = (
            f"{name} contains only {len(obj)} elements"
            f", but at least {min_len} are required")
        super().__init__(msg)

class MaxSizeError(UserAssert, ValueError):
    """Raise when a container has too many elements."""

    def __init__(self, name: str, obj: Sized, max_len: int) -> None:
        msg = (
            f"{name} contains {len(obj)} elements"
            f", but at most {max_len} are allowed")
        super().__init__(msg)

#
# Attribute Errors
#

class InvalidAttrError(UserAssert, AttributeError):
    """Raise when a not existing attribute is called."""

    def __init__(self, obj: object, attr: str) -> None:
        name = getattr(obj, '__name__', obj.__class__.__name__)
        msg = f"{name} has no attribute '{attr}'"
        super().__init__(msg)

class ReadOnlyAttrError(UserAssert, AttributeError):
    """Raise when a read-only attribute's setter method is called."""

    def __init__(self, obj: object, attr: str) -> None:
        name = getattr(obj, '__name__', obj.__class__.__name__)
        msg = f"'{attr}' is a read-only attribute of {name}"
        super().__init__(msg)

#
# OS Errors
#

class DirNotEmptyError(UserAssert, OSError):
    """Raise on remove requests on non-empty directories."""

class FileNotGivenError(UserAssert, OSError):
    """Raise when a file or directory is required, but not given."""

class FileFormatError(UserAssert, OSError):
    """Raise when a referenced file has an invalid file format."""

    def __init__(self, name: str, fmt: str) -> None:
        if name:
            msg = f"the referenced file '{name}' has not a valid {fmt} format"
        else:
            msg = f"the referenced file has not a valid {fmt} format"
        super().__init__(msg)

#
# Lookup Errors
#

class ExistsError(UserAssert, LookupError):
    """Raise when an already existing unique object shall be created."""

class FoundError(UserAssert, LookupError):
    """Raise when an already registered unique object shall be registered."""

class NotExistsError(UserAssert, LookupError):
    """Raise when a non existing unique object is requested."""

class NotFoundError(UserAssert, LookupError):
    """Raise when a unique object is not found in a registry."""

#
# Table Errors
#

class TableError(UserError):
    """Base Exception for Table Errors."""

class RowLookupError(TableError, LookupError):
    """Row Lookup Error."""

    def __init__(self, rowid: int) -> None:
        super().__init__(f"row index {rowid} is not valid")

class ColumnLookupError(TableError, LookupError):
    """Column Lookup Error."""

    def __init__(self, colname: int) -> None:
        super().__init__(f"column name '{colname}' is not valid")

#
# Proxy Errors
#

class ProxyError(UserError):
    """Base Exception for Proxy Errors."""

class PushError(ProxyError):
    """Raise when a push-request could not be finished."""

class PullError(ProxyError):
    """Raise when a pull-request could not be finished."""

class ConnectError(ProxyError):
    """Raise when a proxy connection can not be established."""

class DisconnectError(ProxyError):
    """Raise when a proxy connection can not be closed."""
