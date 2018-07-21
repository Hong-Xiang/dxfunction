import collections.abc
from functools import singledispatch
from .function import Function, function

__all__ = ['Take', 'head']


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


class Take(Function):
    def __init__(self, n):
        self.n = n

    def __call__(self, xs):
        return _take(xs, self.n)


head = function(lambda xs: Take(1)(xs)[0])
