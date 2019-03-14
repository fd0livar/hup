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
"""Collection of Structural Types for Static Typing."""

__copyright__ = '2019 Frootlab Developers'
__license__ = 'GPLv3'
__docformat__ = 'google'
__author__ = 'Frootlab Developers'
__email__ = 'contact@frootlab.org'
__authors__ = ['Patrick Michl <patrick.michl@frootlab.org>']

import os
import types
from typing import Any, Callable, ClassVar, Dict, Hashable, IO, Iterable
from typing import Iterator, List, Mapping, Optional, Sequence, Set, Tuple
from typing import Type, TypeVar, Union, Container, Sized, Generic

# Type-Variables for Generic Structural Types
S = TypeVar('S')
T = TypeVar('T')

# Type-Surrogates
TypeHint = Generic[T] # pylint: disable=E1136

#
# Constants
#

NaN = float('nan') # Standard Constant for the representation of "Not a Number"
Infty = float('inf') # Standard Constant for the representation of infinity
void: Callable[..., None] = lambda *args, **kwds: None

#
# Structural Types for Literals and Collections of Literals
#

# Numbers
RealNumber = Union[int, float]
Number = Union[RealNumber, complex]
OptNumber = Optional[Number]

# Literals
OptType = Optional[type]
OptStr = Optional[str]
OptInt = Optional[int]
OptFloat = Optional[float]
OptComplex = Optional[complex]
OptBool = Optional[bool]
OptBytes = Optional[bytes]
StrOrBool = Union[str, bool]
OptStrOrBool = Optional[StrOrBool]
StrOrInt = Union[str, int]
BytesLike = Union[bytes, bytearray, memoryview]
BytesLikeOrStr = Union[BytesLike, str]

# Classes
Class = Type[Any]
OptClass = Optional[Class]
ClassInfo = Union[Class, Tuple[Class, ...]]
OptClassInfo = Optional[ClassInfo]

# Collections of numbers
RealVector = Sequence[RealNumber]
Vector = Sequence[Number]

# Collections of literals
HashDict = Dict[Hashable, Any]
AnyDict = Dict[Any, Any]
StrSet = Set[str]
StrPair = Tuple[str, str]
StrTuple = Tuple[str, ...]
StrList = List[str]
StrDict = Dict[str, Any]
IntSet = Set[int]
IntPair = Tuple[int, int]
IntTuple = Tuple[int, ...]
IntList = List[int]
IntDict = Dict[int, Any]
FloatPair = Tuple[float, float]
StrIter = Iterable[str]

# Unions of Collections of Literals
StrOrDict = Union[str, AnyDict]
StrOrType = Union[type, str]
OptSet = Optional[Set[Any]]
OptPair = Optional[Tuple[Any, Any]]
OptTuple = Optional[Tuple[Any, ...]]
OptList = Optional[List[Any]]
OptDict = Optional[Dict[Any, Any]]
OptStrDict = Optional[StrDict]
OptStrList = Optional[StrList]
OptStrTuple = Optional[StrTuple]
OptStrOrDict = Optional[StrOrDict]
OptIntList = Optional[IntList]
OptIntTuple = Optional[IntTuple]
OptStrIter = Optional[StrIter]

# Compounds of Literals and Collections of Literals
StrPairDict = Dict[StrPair, Any]
StrListPair = Tuple[StrList, StrList]
StrTupleDict = Dict[Union[str, Tuple[str, ...]], Any]
RecDict = Dict[Any, StrDict]
DictOfRecDicts = Dict[Any, RecDict]

# Classvariables of Compounds
ClassStrList = ClassVar[StrList]
ClassDict = ClassVar[AnyDict]
ClassStrDict = ClassVar[StrDict]

#
# Callable Types and Collection Types for Callables
#

# Callable Types
AnyOp = Callable[..., Any]
BoolOp = Callable[..., bool]
StrOp = Callable[..., str]
IntOp = Callable[..., int]
DictOp = Callable[..., dict]
OpOp = Callable[..., AnyOp]
Void = Callable[..., None]
KeyOp = Callable[[Any, Any], bool]
SeqOp = Callable[[Sequence[Any]], Any]
SeqHom = Callable[[Sequence[Any]], Sequence[Any]]

# Unions of Operators and Literals
OptOp = Optional[AnyOp]
OptVoid = Optional[Void]
OptBoolOp = Optional[BoolOp]
OptSeqOp = Optional[SeqOp]

# Operator Collections
DictOfOps = Dict[str, AnyOp]
DictOfKeyOps = Dict[str, KeyOp]

# Unions of Operator Collections and Literals
OptDictOfOps = Optional[DictOfOps]
OptDictOfKeyOps = Optional[DictOfKeyOps]

#
# Specific Structural Types
#

# Containers and Mappings
OptContainer = Optional[Container]
OptSized = Optional[Sized]
OptMapping = Optional[Mapping]

# Exceptions / Errors
ErrMeta = Type[BaseException]
ErrType = BaseException
ErrStack = types.TracebackType

# File Like
FileLike = IO[Any]
BinaryFileLike = IO[bytes]
TextFileLike = IO[str]

# Functions, Methods and Modules
Function = types.FunctionType
Method = types.MethodType
Module = types.ModuleType

# Iterators
IterAny = Iterator[Any]
IterNone = Iterator[None]

# None Type
NoneType = None.__class__

# Path Like
Path = os.PathLike
OptPath = Optional[Path]
PathList = List[Path]
StrDictOfPaths = Dict[str, Path]
PathLike = Union[str, Path]
PathLikeList = List[PathLike]
OptPathLike = Optional[PathLike]
