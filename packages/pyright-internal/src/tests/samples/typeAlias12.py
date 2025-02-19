# This sample tests the handling of a generic type alias that uses
# a union that collapses to a single type when specialized.

from typing import List, Literal, TypeVar, Union

V = TypeVar("V")
U = TypeVar("U")

Alias = Union[V, U]


def fn(x: Alias[V, V]) -> V:
    return x


def fn2(x: List[Alias[V, V]]) -> List[V]:
    return x


t1: Literal["Type[int]"] = reveal_type(Alias[int, int])
