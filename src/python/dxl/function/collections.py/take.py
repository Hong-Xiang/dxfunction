import collections.abc
import operator
from functools import singledispatch

from dxl.data import Function

from .base import func

__all__ = ['Take', 'head']


class Take(Function):
    def __init__(self, n):
        self.n = n

    def __call__(self, xs):
        return _take(xs, self.n)


@singledispatch
def _take(xs, n):
    raise TypeError(f"Can't Take on {type(x)}")


@_take.register(collections.abc.Sequence)
def _(xs, n):
    return xs[:n]


@_take.register(collections.abc.Iterable)
def _(xs, n):
    for _ in range(n):
        yield from xs


@func
def head(xs):
    return _head(xs)


@singledispatch
def _head(xs):
    raise TypeError


@_head.register(collections.abc.Sequence)
def _(xs):
    return Take(1)(xs)[0]


@_head.register(collections.abc.Sequence)
def _(xs):
    return Take(1)(xs)


def fold(f, xs, init):
    ...


def is_mono(f, xs):
    return fold(operator.and_, fmap(decay, xs), True)
